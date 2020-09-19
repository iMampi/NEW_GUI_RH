import tkinter as tk
from tkinter import ttk
import widgets_3 as w
import base_ex as m
import tkinter.font as tkf

#TODO: add frame to view pictures
#todo : prepare treeview for option "see all" with selectable line
#todo : add selector with combobox to choose with to edit and which to see

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
            self.EntriesFrame.columnconfigure(0,weight=1,minsize=150)
            self.EntriesFrame.columnconfigure(1, weight=1, minsize=100)

        #counter = 0
        # a reformuler
        if self.mode in ["creation", "modification", "consultation"]:
            for field in m.MyInfos.data.keys():
                if m.MyInfos.data[field][self.mode]["mode"] == True:
                    self.inputs[field] = w.LabelInput(self, mode=self.mode, label=field)
                    # changer en ref to data>type>widget type pour le cas image
                    # self.grid_propagate(0)
                    self.inputs[field].grid(row=m.MyInfos.data[field][self.mode]["row"], column=0)
                    self.columnconfigure(0, weight=0,minsize=100)
                    self.columnconfigure(1, weight=1,minsize=150)
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



    def grid(self,**kwargs):
        super().grid(**kwargs)

    def get(self):
        data={}
        for key,widget in self.inputs.items():
            print(key)
            data[key]=widget.get()
        print("data from get :")
        print(data)
        return data

    def reset(self):
        for widget in self.inputs.values():
            widget.delete()

        #todo : insert dialog box
        print('RESET')

    def set(self,data_dict):
        print("trying to set")
        #todo : it works for the new matricule. must try on setting all values
        for key,new_data in data_dict.items():
            try:
                self.inputs[key].set(new_data)
            except KeyError:
                pass


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
                            command=self.callbacks[m.MyActionButtons.data[button]["callback"]]
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

class SelectFrame(tk.Frame):
    def __init__(self,parent,*args,**kwargs):
        super().__init__(parent,*args,**kwargs)
        self.s_lab=tk.Label(self,text="Who u gonna choose?")
        self.s_lab.grid(row=0,column=0,sticky="nswe",)

        self.s_var=tk.StringVar()
        self.s_entry=ttk.Entry(self,textvariable=self.s_var)
        self.s_entry.grid(row=1,column=0)

        #Todo:create and associate the command
        self.s_bt=ttk.Button(self,text="Voir")
        self.s_bt.grid(row=1,column=1)


class ViewAll(tk.Toplevel):
    def __init__(self,data,callbacks,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.callbacks=callbacks
        self.geometry("500x400")
        self.minsize(width=500, height=400)
        self.title("Sélectionnez l'individu")
        self.data=data
        self.data_form=None

        self.control_frame = SelectFrame(self)
        print('args from trace:')
        self.control_frame.s_var.trace("w", callback=self.myfilter)

        self.control_frame.grid(row=0,column=0,sticky="nswe",padx=12,pady=10)

        tv_frame = tk.Frame(self)
        tv_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nswe")
        tv_frame.columnconfigure(0, weight=1)
        tv_frame.columnconfigure(1, weight=0)
        tv_frame.rowconfigure(0, weight=1)
        tv_frame.rowconfigure(1, weight=0)

        self.tv_canvas =tk.Canvas(tv_frame, bd=-3)
        self.tv_canvas.grid(row=0,column=0, sticky="nswe")
        self.tv_canvas.columnconfigure(0, weight=1)
        self.tv_canvas.rowconfigure(0, weight=1)
        self.tv_canvas.rowconfigure(1, weight=1)

        tv_xscrollbar=ttk.Scrollbar(tv_frame,orient="horizontal",command=self.tv_canvas.xview)
        tv_xscrollbar.grid(row=1,column=0,sticky='swe')
        tv_yscrollbar = ttk.Scrollbar(tv_frame, orient="vertical", command=self.tv_canvas.yview)
        tv_yscrollbar.grid(row=0, column=1, sticky='nse')

        self.tv_canvas.configure(xscrollcommand=tv_xscrollbar.set)
        self.tv_canvas.bind('<Configure>',
                            lambda e: self.tv_canvas.configure(scrollregion = self.tv_canvas.bbox("all")))
        self.tv_canvas.configure(yscrollcommand=tv_yscrollbar.set)
        self.tv_canvas.bind('<Configure>',
                            lambda e: self.tv_canvas.configure(scrollregion=self.tv_canvas.bbox("all")))

        self.headers=[]
        for key in m.MyInfos.data.keys():
            if m.MyInfos.data[key].get("csvheader"):
                self.headers.append(key)
        self.treeview = ttk.Treeview(self.tv_canvas,selectmode='browse',
                                     columns=[*self.headers],height=100)
        self.treeview.heading('#0',text="Ligne")
        self.treeview.column('#0',minwidth=40,width=40,stretch=True)
        for header in self.headers:
            self.treeview.heading(header,text=header)
            self.treeview.column(header, minwidth=40, width=80,stretch=True)
            #todo : take callback from controller
        # self.treeview.bind('<<TreeviewSelect>>', self.get_values)


        #self.treeview.insert('','end',iid='1',text='Listbox',values=['rh032','IR',"Mampi"])

        self.treeview.grid(row=1,column=0,sticky="nswe")

        self.tv_canvas.create_window((0,0),window=self.treeview,anchor='nw')
        self.rowconfigure(1,weight=1)
        self.columnconfigure(0,weight=1)
        #self.columnconfigure(1, weight=1)

        #self.treeview.bind(<<TreeviewOpen>>,self.get_matricule)
        #Todo:title and champ de saisie pour filtrer la sélection
        #todo : bind rolling wheel of mouse


    def myfilter(self,*args):
        #fixme : optimize maybe
        #fixme  : it is case sensitive. make it so it is not

        init_iids=self.treeview.get_children()
        for iid in init_iids:
            self.treeview.delete(iid)

        self.populate()
        characters = self.control_frame.s_entry.get()
        if characters=='':
            return
        else:
            myiids=list(self.treeview.get_children())
            print('my initial iids')
            print(myiids)
            for myiid in myiids:
                values=self.treeview.set(myiid)
                headers=['Matricule','Noms','Prénoms']
                test=[]
                for header in headers:
                    test.append(characters not in values[header])
                if all(test):
                        self.treeview.delete(myiid)

    def get_values(self, *args):

        # return iid
        current = self.treeview.selection()
        # or another alternative
        # current=self.treeview.item(self.treeview.focus())
        values = self.treeview.set(current)
        # return a dict of values from the selected row
        # MyViewFrame.set(data_dict=values)
        print(values)
        self.data_form=values

        return values





    def populate(self,data=None):
        # if data==None:
        counter=0
        for row_data in self.data:
            row_values = [row_data[header] for header in self.headers ]
            self.treeview.insert('', 'end', iid=counter, values=row_values)
            counter += 1
        #else:









                
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
