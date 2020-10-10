import datetime as dt
import calendar
import csv

class Conge:
    def __init__(self,matricule,datedebut,congesgeneres=0):
        self.matricule=matricule
        self.datedebut=dt.datetime.strptime(datedebut,"%d/%m/%Y")
        self.congesgeneres=congesgeneres
        self._update()

    def _open_recap(self):
        #todo : add if file is missing,so it is new, must create new one
        with open("recap_conge.csv", 'r', newline='') as fh:
            csvreader = csv.DictReader(fh,delimiter=";")
            data = list(csvreader)
            return data

    def _genererconge(self):
        td=dt.date.today()
        delta_years=td.year-self.datedebut.year
        delta_months=td.month-self.datedebut.month
        ratio_day1=1-(td.day-1)/calendar.monthrange(int(td.year),int(td.month))[1]
        ratio_day2=self.datedebut.day/calendar.monthrange(int(self.datedebut.year),int(self.datedebut.month))[1]
        final=(((delta_years*12)+delta_months)*2.5)+(ratio_day1*2.5)+(ratio_day2*2.5)
        return final

    def _update(self):

