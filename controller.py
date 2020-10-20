import tkinter as tk
from tkinter import ttk
import widgets_3 as w
import base_ex as m
import views3 as v
import time
import conge

#todo change mode_[mode] to personnel_[mode]
#todo add conge_[mode]
#todo : mode "modificaation", faire en sorte que lorsque "save" est exécuter, génération automatique de
# congés generé, congés consommé, et congé disponible
class MyRoot(tk.Tk):
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.mode=None

        self.mycsv = m.MyInfos("mydb.csv")
        #loads list of dictionnary
        self.data = self.mycsv.load_records()
        print(self.data)
        self.conge_data = m.MyConges()._open_base()
        cg=conge.Conge(self.data,self.conge_data)
        updated_conge_data=cg.update_conge_csv()
        if updated_conge_data[0]:
            self.data=updated_conge_data[1]
        print(self.data)
        self.current_index=None


        self.callbacks={"Save":self.save_,
                        "Previous":self.previous_,
                        "Next":self.next_,
                        "creation":self.mode_creation,
                        "consultation":self.mode_consultation,
                        "modification":self.mode_modification,
                        "new_conge":self.new_conge,
                        "see_conge": None,
                        "paie": None,
                        "fire":self.mode_fire,
                        "Edit":self.edit_
                        }
        self.MyMainFrame=None

        # conge(self.data,self.conge_data)

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

        self.MyMainFrame.update_idletasks()
        self.MyMainFrame.update_idletasks()

        self.columnconfigure(0,weight=1)
        self.rowconfigure(0,weight=1)


        #to use to check the window size
        print("the mode is {}".format(self.mode))
        self.MyMainFrame.MyViewFrame.update_idletasks()
        print(self.MyMainFrame.MyViewFrame.winfo_geometry())
        print(self.MyMainFrame.winfo_geometry())
        # print('trying to print var')
        # print(self.MyMainFrame.MyViewFrame.inputs)

        #print(self.MyMainFrame.w)
        #print(self.MyMainFrame.h)



    def save_(self):
        rownum = self.current_index
        mydata=self.MyMainFrame.MyViewFrame.get()
        print("récupération des données")
        print(mydata)

        if rownum == None:
            self.mycsv.save_record(mydata, rownum=rownum)
            print("Sauvegardé")
        else:
            for header,value in mydata.items():
                self.data[rownum][header] = value

            self.mycsv.save_record(self.data, rownum=rownum)
            print("Sauvegardé")

        # self.mycsv.save_record(mydata,rownum=rownum)
        self.MyMainFrame.MyViewFrame.reset()
        self.MyMainFrame.MyViewFrame.set(self.mycsv.new_matricule())

    def previous_(self):
        #todo : add delimitation for when we reach the end or the start of the list, to disable the button
        self.current_index=self.current_index-1
        self.MyMainFrame.MyViewFrame.set(self.data[self.current_index])
        print(self.current_index)

    def next_(self):
        self.current_index = self.current_index + 1
        self.MyMainFrame.MyViewFrame.set(self.data[self.current_index])
        print(self.current_index)

    def edit_(self):
        self.MyMainFrame.MyViewFrame.destroy()
        self.mode="modification"
        self.construction(myindex=self.current_index)
        pass


    def MyTreeview(self):
        self.TV=v.ViewAll(self.data,self.callbacks,self.mode)
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



    def new_conge(self):
        self.MyMainFrame.MyViewFrame.destroy()
        self.current_index=None
        self.mode = "c_creation"
        #todo : mise à jour des congés générés si nouveaux jour d'ouverture du fichier
        #todo : mise à jour des congés générés si base a été modifié
        # (cas des jours fériés ajuté, ou modification durée du congé


        self.MyTreeview()





    def mode_creation(self):
        self.MyMainFrame.MyViewFrame.destroy()
        self.current_index=None
        print("creation")
        self.mode="creation"
        self.construction()
        self.MyMainFrame.MyViewFrame.set(self.mycsv.new_matricule())

    def mode_consultation(self):
        self.MyMainFrame.MyViewFrame.destroy()
        self.mode = "consultation"
        self.MyTreeview()
        #self.MyMainFrame.MyViewFrame.destroy()
        print("consultation")

    def mode_modification(self):
        #FIXME : pour self mode changing first everywhere
        self.MyMainFrame.MyViewFrame.destroy()
        self.mode = "modification"
        self.MyTreeview()
        print("modification")
        #self.MyMainFrame.MyViewFrame.destroy()
        # self.construction()

    def mode_fire(self):
        self.MyMainFrame.MyViewFrame.destroy()
        self.mode="fire"
        self.MyTreeview()

        # self.MyMainFrame.MyViewFrame.destroy()
        print("fire")


r=MyRoot()
r.mainloop()

