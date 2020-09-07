import tkinter as tk
from tkinter import ttk
import base_ex as m


root = tk.Tk()

class Label_Radiobox:
    def __init__(self,parent,label=None,MyInfos=None):
        self.label = label
        MyInfo=MyInfos.data.get(label,"Error 404")
        self.var_type = self.field_type[MyInfo["type"]]
         

class Label_Input(tk.Frame):
    #change variable type for image file
    field_type ={
        m.FieldTypes.string :{"type":tk.StringVar,"input_type":"MyEntry"},
        m.FieldTypes.string_list : {"type":tk.StringVar,"input_type":"MyCombobox"},
        m.FieldTypes.iso_date_string : {"type":tk.StringVar,"input_type":"MyEntry"},
        m.FieldTypes.string_long : {"type":tk.StringVar,"input_type":"MyText"},
        m.FieldTypes.decimal : {"type":tk.DoubleVar,"input_type":"MyEntry"},
        m.FieldTypes.integer : {"type":tk.IntVar,"input_type":"MyEntry"},
        m.FieldTypes.boolean : {"type":tk.BooleanVar,"input_type":"MyEntry"},
        m.FieldTypes.image_file : {"type":None,"input_type":None}
        }
    
    def __init__(self,parent,label=None, MyInfos=m.MyInfos):
        super().__init__(parent)
        
        self.label = label
        MyInfo=MyInfos.data.get(label,"Error 404")
        self.var_type = self.field_type[MyInfo["type"]]["type"]
        
        self.MyLabel = tk.Label(parent,text=label)
        
        MyEntry = tk.Entry(parent,textvariable=self.var_type)
        MyCombobox = ttk.Combobox(parent,textvariable=self.var_type,values=MyInfo.get("values",None))
        self.MyInput=eval(self.field_type[MyInfo["type"]]["input_type"])
        
        
        self.MyLabel.grid(row=0,column=0,sticky="WE")
        
        self.MyInput.grid(row=0,column=1,sticky="WE")
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)

    def grid(self,sticky="WE",**kwargs):
        super().grid(sticky=sticky,**kwargs)
        
    def get(self):
        try:
            if self.var_type:
                return self.var_type.get()
            elif self.field_type[MyInfo["type"]]["input_type"] == "MyText":
                return self.MyInput.get('1.0', tk.END)
            else:
                return self.MyInput.get()
        except (TypeError, tk.TclError):
            # happens when numeric fields are empty.
            return ''

    def set(self, value, *args, **kwargs):
        if type(self.variable) == tk.BooleanVar:
                self.variable.set(bool(value))
        elif self.variable:
                self.variable.set(value, *args, **kwargs)
        elif type(self.input) in (ttk.Checkbutton, ttk.Radiobutton):
            if value:
                self.input.select()
            else:
                self.input.deselect()
        elif type(self.input) == tk.Text:
            self.input.delete('1.0', tk.END)
            self.input.insert('1.0', value)
        else:
            self.input.delete(0, tk.END)
            self.input.insert(0, value)

        



x=Label_Input(root,label="Noms")
#y=Label_Input(root,label="Sexe")
x.grid(row=0,column=0)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)
root.mainloop()
        
        

        
        
