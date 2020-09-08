import tkinter as tk
from tkinter import ttk
import base_ex as m




class Label_Radiobox:
    def __init__(self,parent,label=None,MyInfos=None):
        self.label = label
        MyInfo=MyInfos.data.get(label,"Error 404")
        self.var_type = self.field_type[MyInfo["type"]]
         


#TODO : implement the img downloader annd imge widget displayer
class Label_Input(tk.Frame):
    #change variable type for image file and tk.Text
    field_type ={
        m.FieldTypes.string :{"type":tk.StringVar,"input_type":ttk.Entry},
        m.FieldTypes.string_list : {"type":tk.StringVar,"input_type":ttk.Combobox},
        m.FieldTypes.iso_date_string : {"type":tk.StringVar,"input_type":ttk.Entry},
        m.FieldTypes.string_long : {"type":tk.StringVar,"input_type":tk.Text},
        m.FieldTypes.decimal : {"type":tk.DoubleVar,"input_type":ttk.Entry},
        m.FieldTypes.integer : {"type":tk.IntVar,"input_type":ttk.Entry},
        m.FieldTypes.boolean : {"type":tk.BooleanVar,"input_type":ttk.Entry},
        m.FieldTypes.image_file : {"type":tk.StringVar,"input_type":ttk.Entry}
        }
    
    def __init__(self,parent,mode=None,label=None, MyInfos=m.MyInfos,**kwargs):
        super().__init__(parent,**kwargs)
        self.mode=mode
        self.MyInfos=MyInfos
        MyInfo=self.MyInfos.data.get(label,"Error 404")
        self.var_type = self.field_type[MyInfo['type']]["type"]
        input_class=self.field_type[MyInfo["type"]]["input_type"]
        
        #we create a dict that will hold the kwargs for the widgets. so it can be procedural
        #mieux structutrer les if avec les changements de mode
        input_args={}
        label_args={}
        if self.mode=="consultation":
            if input_class==ttk.Combobox:
                input_class=ttk.Entry
        if self.mode=="fire":
            if label in ["Sexe","Etat civil","Département"]:
                input_class=ttk.Entry
        if self.mode=="creation":
            if MyInfo.get("values",None):
               input_args["values"]=MyInfo.get("values",None)
               
        if input_class==ttk.Entry:
            if self.mode=="fire":
                input_args["state"] = MyInfo["fire"]["state"]
            elif self.mode=="consultation":
                input_args["state"] = "readonly"

        #if input_class==tk.Text:
        #    input_args["height"] = 20
        if input_class==tk.Text:
            input_args["height"]=4
            label_args["height"]=4
        #TODO : add the thing for the consultation mode from disabled to normal ,get var, disabled

        else:
            input_args["textvariable"]=self.var_type()

        input_args["width"]=20
        
        var=self.var_type()

        self.LabelsFrame=parent.LabelsFrame
        self.EntriesFrame=parent.EntriesFrame
        
        #self.LabelsFrame.rowconfigure(0,weight=1)
        #self.LabelsFrame.rowconfigure(0,weight=1)
        
                
        self.MyInput = input_class(self.EntriesFrame,**input_args)
        self.MyLabel = tk.Label(self.LabelsFrame,text=label,anchor="ne",**label_args)


        #self.MyError =
        
                
    def grid(self,row=None,column=None,sticky="we",**kwargs):
        
        #super().grid(sticky=sticky,**kwargs)

        self.MyLabel.grid(row=row,column=column,sticky=sticky,padx=2,pady=2)
        self.MyInput.grid(row=row,column=column,sticky=sticky,padx=2,pady=2)
        #self.MyLabel.columnconfigure(0, weight=1)
        #self.MyInput.columnconfigure(0, weight=1)
        
    def get(self):
        try:
            if self.var_type:
                return self.var_type.get()
            elif self.field_type[MyInfo["type"]]["input_type"] == tk.Text:
                return self.MyInput.get('1.0', tk.END)
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


MyInfos=m.MyInfos
MyInfo=MyInfos.data.get("Matricule","Error 404")
var_type = Label_Input.field_type[MyInfo["type"]]["type"]
print(var_type)
"""
##EXAMPLE##
root=tk.Tk()
MF=tk.Frame(root,width=60)
MF.grid(row=0,column=0)
counter=0

for field in m.MyInfos.data.keys():
    print(field)
    if m.MyInfos.data[field]['creation']['mode']==True:
        x=Label_Input(MF,label=field)
        x.grid(row=counter,column=0)
        root.columnconfigure(0,weight=1)
        root.columnconfigure(1,weight=1)
        counter+=1
        
        
#x=Label_Input(MF,label="Noms")
#y=Label_Input(MF,label="Sexe")

#x.grid(row=0,column=0)
#y.grid(row=1,column=0)


#root.columnconfigure(0,weight=1)
#root.columnconfigure(1,weight=1)

root.mainloop()
"""


        
        
