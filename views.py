import tkinter as tk
from tkinter import ttk
import widgets_ as w
import base_ex as m

##y a de la redondance ici. the met sles element dans une frame, qui sera mis dans une frame qui sera mis dans une
# autre frame. trop de frame

class MyViewFrame(tk.Frame):
    def __init__(self,parent,mode=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.mode=mode
        self.inputs={}
        
        #self.MyInfos = MyInfos
        MF=w.MainFrame(self,mode=self.mode,width=60)
        MF.grid(row=0,column=0)
        
       
        counter=0
        if self.mode in ["creation","modification","consultation"] :
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]==True:
                    x=w.Label_Input(MF,mode=self.mode,label=field)
                    #changer en ref to data>type>widget type pour le cas image
                    x.grid(row=counter,column=0)
                    self.columnconfigure(0,weight=1)
                    self.columnconfigure(1,weight=1)
                    self.inputs['field']=x.MyInput
                    counter+=1
        """
        else:
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]["visible"]==True:
                    if m.MyInfos.data[field][self.mode]["editable"]==True:
                        x=w.Label_Input(MF,mode=self.mode,label=field)
                        #changer en ref to data>type>widget type pour le cas image
                        x.grid(row=counter,column=0)
                        self.columnconfigure(0,weight=1)
                        self.columnconfigure(1,weight=1)
                        counter+=1
                        """
    def get(self):
        data={}
        for key,widget in self.inputs:
            data['key']=widget.get()
        
        
        


        
class MyMainFrame(tk.Frame):
    def __init__(self,parent,mode,callbacks,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.callbacks=callback
        self.mode=mode
        pw1=tk.PanedWindow(self,bd=5)
        #replace this label by a series a buttons
        #lab=tk.Label(pw1, text="LABEL 001",bd=5, relief="ridge")
        
        self.MySideButtons=w.SideFrame(pw1)

        pw1.paneconfigure(self.MySideButtons,sticky="nswe")
        pw1.grid(row=0,column=0,sticky="nswe")
        pw1.rowconfigure(0,weight=1)
        pw1.columnconfigure(0,weight=1)
        
        pw2=tk.PanedWindow(pw1,orient=self.mode,bd=5, relief="ridge")
        pw1.paneconfigure(pw2,sticky="nswe")

        ##quelque chose cloche avec le mode consultation, voir ce que c'est
        self.MyViewFrame=MyViewFrame(pw2,mode="creation")
        pw2.paneconfigure(self.MyViewFrame,sticky="nswe")
        pw2.rowconfigure(0,weight=1)
        pw2.columnconfigure(0,weight=1)
        
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
                
        
       

        
        

#root=tk.Tk()

#####
"""
p1=tk.PanedWindow(bd=5,bg="red")
l1=tk.Label(p1,text="XXXX")
l1.grid(row=0,column=0)
p1.add(l1)
p1.grid(row=0,column=0)
"""
#####
"""
p1=MyMainFrame(root)
p1.grid(row=0,column=0,sticky="nswe")
root.rowconfigure(0,weight=1)
root.columnconfigure(0,weight=1)
"""


#root.mainloop()

