import tkinter as tk
from tkinter import ttk
import widgets_3 as w
import base_ex as m
import tkinter.font as tkf

#TODO: add frame to view pictures


class MyViewFrame(tk.Frame):
    def __init__(self, parent, mode=None, callbacks=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.mode = mode
        self.inputs = {}
        self.callbacks = callbacks
        self.LabelsFrame = tk.Frame(self)
        self.EntriesFrame = tk.Frame(self)


        titles_font = tkf.Font(size=15, weight="bold")
        BigTitle=tk.Label(self,text=m.MyTitles.data[self.mode],height=1,font=titles_font)
        BigTitle.grid(row=0, column=0, sticky="nswe", columnspan=2, rowspan=1)
        
        if mode:
            #self.LabelsFrame.grid_propagate(False)
            self.LabelsFrame.grid(row=1,column=0,sticky="nswe")
            self.EntriesFrame.grid(row=1,column=1,sticky="nswe")
            self.LabelsFrame.columnconfigure(0,weight=1,minsize=100)
            self.EntriesFrame.columnconfigure(0,weight=1,minsize=100)

        #counter = 0
        # a reformuler
        if self.mode in ["creation", "modification", "consultation"]:
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]["mode"] == True:
                    x = w.LabelInput(self, mode=self.mode, label=field)
                    # changer en ref to data>type>widget type pour le cas image
                    # self.grid_propagate(0)
                    x.grid(row=m.MyInfos.data[field][self.mode]["row"], column=0)
                    self.columnconfigure(0, weight=0,minsize=100)
                    self.columnconfigure(1, weight=1,minsize=100)
                    self.inputs[field] = x.MyInput
                    #counter += 1
        elif self.mode is "fire":
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]["mode"] == True:
                    x = w.LabelInput(self, mode=self.mode, label=field)
                    # changer en ref to data>type>widget type pour le cas image
                    # self.grid_propagate(0)
                    x.grid(row=m.MyInfos.data[field][self.mode]["row"], column=0)
                    self.columnconfigure(0, weight=0,minsize=100)
                    self.columnconfigure(1, weight=1,minsize=100)
                    self.inputs[field] = x.MyInput
                    #counter += 1


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
        
        pw1=tk.PanedWindow(self,bd=5,showhandle=True)
        #replace this label by a series a buttons
        #lab=tk.Label(pw1, text="LABEL 001",bd=5, relief="ridge")

        self.MySideButtons=MySideFrame(pw1,callbacks=self.callbacks,mode=self.mode)

        pw1.paneconfigure(self.MySideButtons,sticky="nswe")
        pw1.grid(row=0,column=0,sticky="nswe")

        
        pw2=tk.PanedWindow(pw1,orient="vertical",bd=5, relief="ridge")
        pw1.paneconfigure(pw2,sticky="nswe")

        #MYVIEWFRAME
        if self.mode:
            self.MyViewFrame=MyViewFrame(pw2,callbacks=self.callbacks,mode=self.mode)
            pw2.paneconfigure(self.MyViewFrame, sticky="nswe")

            # BOTTOM BUTTONS
            ButtonsFrame = tk.Frame(pw2)
            pw2.paneconfigure(ButtonsFrame, sticky="swe")
            button_counter = 0
            # add callback for bottom buttons later
            for button in m.MyActionButtons.data.keys():
                try:
                    if m.MyActionButtons.data[button][self.mode]:
                        bt = ttk.Button(
                            ButtonsFrame,
                            text=button,
                        )
                        bt.grid(row=0, column=button_counter, sticky="nswe", columnspan=1, padx=2, pady=2)
                        ButtonsFrame.columnconfigure(button_counter, weight=1)
                        # pw2.paneconfigure(bt, sticky="swe")
                        button_counter += 1
                except:
                    print("case of mode 'None' for {}".format(button))
                    pass

        else:
            self.MyViewFrame=tk.Label(text="Choose an action")
            pw2.paneconfigure(self.MyViewFrame, sticky="nswe")


        #self.lbt=ttk.Button(pw2,text="test last button")
        #pw2.paneconfigure(self.lbt, sticky="swe" )


        pw2.rowconfigure(0,weight=1)
        pw2.rowconfigure(1, weight=1)
        pw2.columnconfigure(0,weight=1)
        pw2.columnconfigure(1, weight=1)

        pw1.rowconfigure(0, weight=1)
        pw1.columnconfigure(0, weight=1)
        self.rowconfigure(0,weight=1)
        self.columnconfigure(0,weight=1)
        
                
"""
root=tk.Tk()
callbacks={"Save":None,
            "Previous":None,
            "Next":None,
            "creation":None,
            "consultation":None,
            "modification":None
            }
MVF=MyMainFrame(root,mode="creation",callbacks=callbacks)
MVF.pack()
root.mainloop()
"""
