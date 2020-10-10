import datetime as dt
import calendar

class Conge:
    td = dt.date.today()
    jours_feries={"Noel":dt.date(td.year,12,25),"Nouvel an"dt.date(td.year,1,1)}

    def __init__(self,matricule,datedebut,congesgeneres=0):
        self.matricule=matricule
        self.datedebut=dt.datetime.strptime(datedebut,"%d/%m/%Y")
        self.congesgeneres=congesgeneres
        self._update()

    def _genererconge(self):

        delta_years=td.year-self.datedebut.year
        delta_months=td.month-self.datedebut.month
        ratio_day1=1-(td.day-1)/calendar.monthrange(int(td.year),int(td.month))[1]
        ratio_day2=self.datedebut.day/calendar.monthrange(int(self.datedebut.year),int(self.datedebut.month))[1]
        final=(((delta_years*12)+delta_months)*2.5)+(ratio_day1*2.5)+(ratio_day2*2.5)
        return final

    def _update_solde(self):
        pass

    def _new_jour_ferie(self):
        pass

