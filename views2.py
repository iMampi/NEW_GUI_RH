import tkinter as tk
from tkinter import ttk
import widgets_ as w
import base_ex as m

class MyViewFrame(tk.Frame):
    def __init__(self,parent,mode=None,callbacks=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.mode=mode
        self.inputs={}
        self.callbacks=callbacks
        self.LabelsFrame=tk.Frame(parent,bd=3,relief="sunken")
        self.EntriesFrame=tk.Frame(parent,bd=3,relief="sunken")

        BigTitle=tk.Label(parent,text=self.mode,bd=3,relief="sunken",height=1)
        BigTitle.grid(row=0,column=0,sticky="nswe",columnspan=2,rowspan=1)
        
        if mode:
            self.LabelsFrame.grid(row=1,column=0,sticky="nswe")
            self.EntriesFrame.grid(row=1,column=1,sticky="nswe")
            self.LabelsFrame.columnconfigure(0,weight=1)
            self.EntriesFrame.columnconfigure(0,weight=1)

        ButtonsFrame=tk.Frame(parent)
        ButtonsFrame.grid(row=2, column=0, sticky="we", columnspan=2)
        button_counter=0
        #add cllback for bottom buttons later
        for button in m.MyActionButtons.data.keys():
            if m.MyActionButtons.data[button][self.mode]:
                bt=ttk.Button(
                    ButtonsFrame,
                    text=button,
                    )
                bt.grid(row=0, column=button_counter, sticky="nswe",columnspan=1,padx=2,pady=2)
                ButtonsFrame.columnconfigure(button_counter, weight=1)
                button_counter += 1
        
        #self.columnconfigure(0,weight=1)
        #self.columnconfigure(1,weight=1)
        

        counter=0
        #a reformuler
        if self.mode in ["creation","modification","consultation"] :
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]==True:
                    x=w.Label_Input(self,mode=self.mode,label=field)
                    #changer en ref to data>type>widget type pour le cas image
                    x.grid(row=counter,column=0)
                    self.columnconfigure(0,weight=1)
                    self.columnconfigure(1,weight=1)
                    self.inputs['field']=x.MyInput
                    counter+=1
        
    def grid(self,**kwargs):
        super().grid(**kwargs)

    def get(self):
        data={}
        for key,widget in self.inputs:
            data['key']=widget.get()

class MySideFrame(tk.Frame):
    def __init__(self, parent,mode=None,callbacks=None,*args, **kwargs):
        super().__init__(parent, relief="ridge", bd=5,*args, **kwargs)
        button_counter=0
        self.callbacks=callbacks
        self.mode=mode
        for button in m.MySideButtons.data.keys():
            bt=ttk.Button(self,text=button,command=self.callbacks[m.MySideButtons.data[button]["callback"]])
            bt.grid(row=button_counter, column=0, sticky="nswe")
            self.columnconfigure(0, weight=1)
            self.rowconfigure(button_counter, weight=1)

            button_counter += 1
        

##y a de la redondance ici. the met sles element dans une frame, qui sera mis dans une frame qui sera mis dans une
# autre frame. trop de frame

    
class MyMainFrame(tk.Frame):
    def __init__(self,parent,mode=None,callbacks=None,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.callbacks=callbacks
        self.mode=mode
        
        pw1=tk.PanedWindow(self,bd=5)
        #replace this label by a series a buttons
        #lab=tk.Label(pw1, text="LABEL 001",bd=5, relief="ridge")

        self.MySideButtons=MySideFrame(pw1,callbacks=self.callbacks,mode=self.mode)

        pw1.paneconfigure(self.MySideButtons,sticky="nswe")
        pw1.grid(row=0,column=0,sticky="nswe")
        pw1.rowconfigure(0,weight=1)
        pw1.columnconfigure(0,weight=1)
        
        pw2=tk.PanedWindow(pw1,bd=5, relief="ridge")
        pw1.paneconfigure(pw2,sticky="nswe")

        ##quelque chose cloche avec le mode consultation, voir ce que c'est
        if self.mode:
            self.MyViewFrame=MyViewFrame(pw2,mode=self.mode,bd=5, relief="ridge")
        else:
            self.MyViewFrame=tk.Label(text="Choose an action")
            
        pw2.paneconfigure(self.MyViewFrame,sticky="nwe")
        pw2.rowconfigure(0,weight=1)
        pw2.columnconfigure(0,weight=1)

        #for test purpose
        #pw3=tk.PanedWindow(pw1,orient="horizontal",bd=5, relief="ridge")
        #pw1.paneconfigure(pw3,sticky="nswe")
        #lab=tk.Label(pw3, text=myvar)
        #pw3.paneconfigure(lab,sticky="nswe")
        
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
                
