import tkinter as tk
from tkinter import ttk
import widgets_3 as w
import base_ex as m
import views3 as v
import time


class MyRoot(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.mode=None

        self.mycsv = m.MyInfos("mydb.csv")
        self.data=self.mycsv.load_records()
        self.current_index=None

        self.callbacks={"Save":self.save_,
                        "Previous":self.previous_,
                        "Next":self.next_,
                        "creation":self.mode_creation,
                        "consultation":self.mode_consultation,
                        "modification":self.mode_modification,
                        "fire":self.mode_fire
                        }
        self.MyMainFrame=None

        self.construction()
        self.minsize(width=660, height=900)


    def construction(self,myindex=None):
        self.current_index=myindex
        self.MyMainFrame=v.MyMainFrame(self,mode=self.mode,callbacks=self.callbacks)
        if myindex==None:
            pass
        else:
            self.MyMainFrame.MyViewFrame.set(self.data[self.current_index])

        self.MyMainFrame.grid(row=0,column=0,sticky="nswe")
        #self.MyMainFrame.propagate()
        
        self.MyMainFrame.update_idletasks()
        #self.MyMainFrame.configure(width=self.MyMainFrame.w,height=self.MyMainFrame.h)
        self.MyMainFrame.update_idletasks()
        #self.MyMainFrame.propagate(0)
        #self.MyMainFrame.pw1.configure(height=self.MyMainFrame.h)

        #we set minimum size. we can shrink and expand but it wont go beyond this min size.


        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)


        #to use to check the window size
        print("the mode is {}".format(self.mode))
        self.MyMainFrame.MyViewFrame.update_idletasks()
        print(self.MyMainFrame.MyViewFrame.winfo_geometry())
        print(self.MyMainFrame.winfo_geometry())

        #print(self.MyMainFrame.w)
        #print(self.MyMainFrame.h)

    def save_(self):

        mydata=self.MyMainFrame.MyViewFrame.get()

        # mycsv=m.MyInfos("mydb.csv")
        print("récupération des données")
        self.mycsv.save_record(mydata)
        print ("Sauvegardé")
        self.MyMainFrame.MyViewFrame.reset()

    def previous_(self):
        self.current_index=self.current_index-1
        self.MyMainFrame.MyViewFrame.set(self.data[self.current_index])
        pass
    
    def next_(self):
        self.current_index = self.current_index + 1
        self.MyMainFrame.MyViewFrame.set(self.data[self.current_index])


        pass

    #todo : les fonctions precedent et suivant
    #todo : dans consultation, les soldes congés, date fin et motif contrat sont en mode obligatoire,
    # ce qui trigger les error_label

    def MyTreeview(self):
        self.TV=v.ViewAll(self.data,self.callbacks)
        self.TV.populate()
        self.TV.bind('<<TreeviewOpen>>', self.doubleclick)

    def doubleclick(self,*args):
        current = self.TV.treeview.selection()
        values = self.TV.treeview.set(current)
        mat=values["Matricule"]
        for row,values in enumerate(self.data):
            if values['Matricule']==mat:
                row_index=row
                self.construction(myindex=row_index)
                self.TV.destroy()
                break




    def mode_creation(self):
        self.MyMainFrame.MyViewFrame.destroy()
        print("creation")
        self.mode="creation"
        self.construction()
        self.MyMainFrame.MyViewFrame.set(self.mycsv.new_matricule())

    def mode_consultation(self):
        self.mode = "consultation"
        self.MyTreeview()
        #self.MyMainFrame.MyViewFrame.destroy()
        print("consultation")

    def mode_modification(self):
        #FIXME : pour self mode changing first everywhere
        #TODO : add bind : when we choose a number, the new viewframe gets created
        self.mode = "modification"

        self.MyMainFrame.MyViewFrame.destroy()
        print("modification")

        self.construction()

    def mode_fire(self):
        self.MyMainFrame.MyViewFrame.destroy()
        print("fire")
        self.mode="fire"
        self.construction()




        #         # or another alternative
        #         # current=self.treeview.item(self.treeview.focus())
        #         values = self.treeview.set(current)
        #         # return a dict of values from the selected row
        #         return values



    # def populate_form(self,*args):
    #         current = v.ViewAll.treeview.selection()
    #         # or another alternative
    #         # current=self.treeview.item(self.treeview.focus())
    #         values = self.treeview.set(current)
    #         # return a dict of values from the selected row
    #         return values
    #
    #
    #
    #
    #
    #     mat = v.ViewAll.get_values(*args)
    #     for row in self.data:
    #         if row['Matricule']==mat:
    #             return row
    #
    #     # for v.MyMainFrame.MyViewFrame

    

        

r=MyRoot()
r.mainloop()

