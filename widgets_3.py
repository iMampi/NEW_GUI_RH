import tkinter as tk
from tkinter import ttk
import base_ex as m
import datetime as dt
from dateutil.relativedelta import relativedelta
#TODO : bind keyTab with tk.text to change widget instead of 4spaces

class ValidateMixin :
    def __init__(self,*args,error_var=None, **kwargs) :
        self.error_var = error_var or tk.StringVar()
        super().__init__(*args, **kwargs)
        vcmd = self.register(self._validate)
        invcmd = self.register(self._invalid)
        self.configure(
            validate='all',
            validatecommand=(vcmd,'%P', '%s', '%S', '%V', '%i', '%d'),
            invalidcommand=(invcmd,'%P', '%s', '%S', '%V', '%i', '%d')
        )

    def _toggle_error(self,on=False):
        self.configure(foreground='red' if on==True else 'black')

    def _validate(self, proposed, current, char, event, index, action):
        self._toggle_error(False)
        self.error_var.set('')
        valid=True
        if event == 'focusout':
            valid = self._focusout_validate(event=event)
        elif event == 'key':
            valid = self._key_validate(proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action)
        return valid

    def _focusout_validate(self,**kwargs):
        return True

    def _key_validate(self,**kwargs):
        return True

    def _invalid(self,proposed, current, char, event, index, action):
        if event == 'focusout':
            self._focusout_invalid(event=event)
        elif event =='key':
            self._key_invalid(proposed=proposed,
                current=current,
                char=char,
                event=event,
                index=index,
                action=action)

    def _focusout_invalid(self,**kwargs):
        self._toggle_error(on=True)

    def _key_invalid(self,**kwargs):
        pass

    def trigger_focusout(self):
        valid=self._validate('','','',"focusout",'','')
        if not valid:
            self._focusout_invalid(event='focusout')
        return valid

class ValidEntry(ValidateMixin,ttk.Entry):
    def _focusout_validate(self,event):
        valid=True
        if not self.get():
            valid=False
            self.error_var.set('Veuillez compléter.')
        return valid

#todo mmake a better key valid for dates - months and days
class ValidDate(ValidateMixin,ttk.Entry):
    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error_var.set('Veuillez compléter.')
        try:
            dt.datetime.strptime(self.get(),"%d/%m/%Y")
        except ValueError:
            self.error_var.set('Date non valide.')
            valid=False

        return valid

    def _key_validate(self,action,index,char,**kwargs):
        valid = True
        if action=='0':
            valid=True
        elif index in ('0','1','3','4','6','7','8','9'):
            valid=char.isdigit()
        elif index in ('2','5'):
            valid= char=='/'
        else:
            valid=False
        return valid

class ValidAge(ValidDate):
    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error_var.set('Veuillez compléter.')
        try:
            bd=dt.datetime.strptime(self.get(), "%d/%m/%Y")
            age = relativedelta(dt.datetime.today(), bd)
            if age.years < 18:
                valid = False
                self.error_var.set('Employé mineur.')
        except ValueError:
            self.error_var.set('Date non valide.')
            valid = False
        return valid

    def _key_validate(self, action, index, char, **kwargs):
        valid = True
        if action == '0':
            valid = True
        elif index in ('0', '1', '3', '4', '6', '7', '8', '9'):
            valid = char.isdigit()
        elif index in ('2', '5'):
            valid = char == '/'
        else:
            valid = False
        return valid

class ValidCombobox(ValidateMixin,ttk.Combobox):
    def _focusout_validate(self, event):
        valid = True
        if not self.get():
            valid = False
            self.error_var.set('Veuillez compléter.')
        if self.get() not in self.cget('values'):
            self.error_var.set('Ne fais pas partie de la liste.')
        return valid

    def _key_validate(self,proposed, action, **kwargs):
        valid = True
        if action == '0':
            self.set('')
            return True
        myvalues=self.cget('values')
        matching =[x for x in myvalues
                   if x.lower().startswith(proposed.lower())]
        if len(matching)==0:
            valid=False
        elif len(matching)==1:
            self.set(matching[0])
            self.icursor(tk.END)
            valid=False
        return valid
    
class ValidMail(ValidateMixin,ttk.Entry):
    def _focusout_validate(self,event):
        data=self.get()
        valid=True
        if not self.get():
            valid=False
            self.error_var.set('Veuillez compléter.')
        elif not all(["@" in data, any([x in data for x in  (".com",".org",".mg",'.uk','.fr','.us','.jp')])]):
            valid=False
            self.error_var.set('Mail non valide.')
        return valid

class ValidPhone(ValidateMixin,ttk.Entry):
    def _focusout_validate(self,event):
        valid=True
        if not self.get():
            valid=False
            self.error_var.set('Veuillez compléter.')
        elif not all((self.get().isdigit(),len(self.get())==10)):
            valid = False
            self.error_var.set('Numéro non valide.')
        elif not any((self.get().startswith(x) for x in ('034','033','032'))):
            valid = False
            self.error_var.set('Numéro non valide.')
        return valid

class ValidMatricule(ValidateMixin,ttk.Entry):
    def _focusout_validate(self,event):
        data=self.get()

        valid=True
        if not self.get():
            valid=False
            self.error_var.set('Veuillez compléter.')
        elif data.lower().startswith("rh") :
            if data.split('rh')[1].isdigit():
                valid=True
            else:
                self.error_var.set('Matricule non valide.')
        else:
            valid=False
            self.error_var.set('Matricule non valide.')
        return valid



         
#TODO : implémenter les dialogbox
#TODO : intégrer les messages d'erreur dans dialogbox

#TODO : implement the img downloader annd imge widget displayer
class LabelInput(tk.Frame):
    #change variable type for image file and tk.Text
    field_type ={
        m.FieldTypes.string :{"type":tk.StringVar,"input_type":ValidEntry},
        m.FieldTypes.string_list : {"type":tk.StringVar,"input_type":ValidCombobox},
        m.FieldTypes.iso_date_string : {"type":tk.StringVar,"input_type":ValidDate},
        m.FieldTypes.iso_date_age_string : {"type":tk.StringVar,"input_type":ValidAge},
        m.FieldTypes.string_long : {"type":tk.StringVar,"input_type":tk.Text},
        m.FieldTypes.decimal : {"type":tk.DoubleVar,"input_type":ValidEntry},
        m.FieldTypes.integer : {"type":tk.IntVar,"input_type":ValidEntry},
        m.FieldTypes.boolean : {"type":tk.BooleanVar,"input_type":ValidEntry},
        m.FieldTypes.image_file : {"type":tk.StringVar,"input_type":ValidEntry},
        m.FieldTypes.string_mail: {"type": tk.StringVar, "input_type": ValidMail},
        m.FieldTypes.string_phone: {"type": tk.StringVar, "input_type": ValidPhone},
        m.FieldTypes.string_matricule: {"type": tk.StringVar, "input_type": ValidMatricule}
        }
    
    def __init__(self,parent,mode=None,label=None, **kwargs):
        super().__init__(parent,**kwargs)
        self.mode=mode
        if self.mode in ["creation", "modification", "consultation"]:
            self.MyInfos=m.MyInfos
        else:
            self.MyInfos=m.MyConges

        MyInfo=self.MyInfos.data.get(label,"Error 404")
        self.var_type = self.field_type[MyInfo['type']]["type"]()
        input_class = self.field_type[MyInfo["type"]]["input_type"]



        #we create a dict that will hold the kwargs for the widgets. so it can be procedural
        #mieux structutrer les if avec les changements de mode
        input_args={}
        label_args={}
        error_args = {}
        if self.mode=="creation":
            if MyInfo.get("values",None):
               input_args["values"]=MyInfo.get("values",None)
        if self.mode=="consultation":
            if "Valid" in str(input_class) or input_class==ttk.Combobox :
                input_class=ttk.Entry

        if self.mode=="fire":
            if label in ["Sexe","Etat civil","Département"]:
                input_class=ttk.Entry


        if "Valid" in str(input_class) or ttk.Entry:
            if self.mode=="fire":
                input_args["state"] = MyInfo["fire"]["state"]
            elif self.mode=="consultation":
                input_args["state"] = "readonly"

        #if input_class==tk.Text:
        #    input_args["height"] = 20
        if input_class==tk.Text:
            input_args["height"]=4
            label_args["height"]=4
            #self.var_type=None
            if self.mode=="consultation":
                input_args["state"] = "disabled"
                input_args["background"] = 'light grey'

        #TODO : add the thing for the consultation mode
        # from disabled to normal ,get var,set var, disabled for tk.Text

        else:
            input_args["textvariable"]=self.var_type

        input_args["width"]=20
        
        #var=self.var_type()

        self.LabelsFrame=parent.LabelsFrame
        self.EntriesFrame=parent.EntriesFrame

        
        #self.LabelsFrame.rowconfigure(0,weight=1)
        #self.LabelsFrame.rowconfigure(0,weight=1)
        
                
        self.MyInput = input_class(self.EntriesFrame,**input_args,**kwargs)
        if input_class not in [tk.Text,ttk.Entry]:
            self.error_var = self.MyInput.error_var
            error_args['textvariable']=self.error_var
        else:
            pass
            #self.error_var = tk.StringVar(value='')
        self.MyLabel = tk.Label(self.LabelsFrame,text=label,anchor="ne",**label_args)
        self.ErrorLabel = tk.Label(self.EntriesFrame, **error_args)

        #self.MyError =
        
                
    def grid(self,row=None,column=None,sticky="we",**kwargs):
        
        #super().grid(sticky=sticky,**kwargs)

        self.MyLabel.grid(row=row,column=column,sticky=sticky,padx=2,pady=2)
        self.MyInput.grid(row=row,column=column,sticky=sticky,padx=2,pady=2)
        self.ErrorLabel.grid(row=row,column=column+1,sticky=sticky,padx=2,pady=2)
        #self.MyLabel.columnconfigure(0, weight=1)
        #self.MyInput.columnconfigure(0, weight=1)
        
    def get(self):
        try:

            if type(self.MyInput) == tk.Text:
                return self.MyInput.get('1.0', tk.END)
            elif self.var_type:
               return self.var_type.get()
            else:
                return self.MyInput.get()
        except (TypeError, tk.TclError):
            # happens when numeric fields are empty.
            return ''

    def set(self, value, *args, **kwargs):
        if type(self.var_type) == tk.BooleanVar:
                self.var_type.set(bool(value))
        elif self.var_type:
                self.var_type.set(value, *args, **kwargs)
        elif type(self.MyInput) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.MyInput.select()
            else:
                self.MyInput.deselect()
        elif type(self.MyInput) == tk.Text:
            self.MyInput.delete('1.0', tk.END)
            self.MyInput.insert('1.0', value)
        else:
            self.MyInput.delete(0, tk.END)
            self.MyInput.insert(0, value)

    def delete(self):
        try:
            if type(self.MyInput) == tk.Text:
                self.MyInput.delete('1.0', tk.END)
            elif self.var_type:
               self.MyInput.delete(0,tk.END)
            else:
                self.MyInput.delete(0,tk.END)
            #FIXME handle this exception
        except (TypeError, tk.TclError):
            print ("Error while deleting")
            # happens when numeric fields are empty.
            return ''

"""
MyInfos=m.MyInfos
MyInfo=MyInfos.data.get("Matricule","Error 404")
var_type = LabelInput.field_type[MyInfo["type"]]["type"]
print(var_type)
"""
"""
##EXAMPLE##
root=tk.Tk()
MF=tk.Frame(root,width=60)
MF.grid(row=0,column=0)
counter=0
lab=tk.Label(root)
lab.grid(row=0,column=0)
labb=tk.Label(root)
labb.grid(row=1,column=0)
e=ValidAge(root,foreground="blue")
e.grid(row=0,column=1)

ee=ValidEntry(root,foreground="blue")
ee.grid(row=1,column=1)
lab.configure(textvariable=e.error_var)
labb.configure(textvariable=ee.error_var)

""""""
for field in m.MyInfos.data.keys():
    print(field)
    if m.MyInfos.data[field]['creation']['mode']==True:
        x=Label_Input(MF,label=field)
        x.grid(row=counter,column=0)
        root.columnconfigure(0,weight=1)
        root.columnconfigure(1,weight=1)
        counter+=1
""""""
        
#x=Label_Input(MF,label="Noms")
#y=Label_Input(MF,label="Sexe")

#x.grid(row=0,column=0)
#y.grid(row=1,column=0)


#root.columnconfigure(0,weight=1)
#root.columnconfigure(1,weight=1)

root.mainloop()
"""



        
        
