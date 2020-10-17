import datetime as dt
import calendar
import itertools

class Conge:
    td = dt.date.today()
    jours_feries={"Noel":dt.date(td.year,12,25),"Nouvel an":dt.date(td.year,1,1)}

    def __init__(self,data,base_conge):
        self.data = data
        self.recap_conge = {}
        self.base_conge = base_conge

        for employee in data:
            self._genererconge(employee['Matricule'],employee['Date de début'])
            self._congesconsommes(employee['Matricule'])
            self._update_solde(employee['Matricule'])



    def _genererconge(self,matricule,datedebut):
        
        delta_years=self.td.year-datedebut.year
        delta_months=self.td.month-datedebut.month
        ratio_day1=1-(self.td.day-1)/calendar.monthrange(int(self.td.year),int(self.td.month))[1]
        ratio_day2=datedebut.day/calendar.monthrange(int(datedebut.year),int(datedebut.month))[1]
        final=(((delta_years*12)+delta_months)*2.5)+(ratio_day1*2.5)+(ratio_day2*2.5)
        self.recap_conge[matricule]=final

    def _congesconsommes(self,matricule):
        #todo : add a way to not take the future dayooff in the future not taken yet
        #todo : add a field that return all dayoff already consummed and those not consummed yet
        # todo : add update for "conge recp.csv"
        checker=[]
        for entry in self.base_conge:
            if entry['Matricule']==matricule:
                checker.append(1)
            else:
                checker.append(0)
        #fixme : to sum as a generator
        consommation = sum(list(itertools.compress(self.base_conge,checker)))

        mat_ref=enumerate(self.data['Matricule'])
        for mat in mat_ref:
            if mat[1]==matricule:
                myref=mat[0]

        self.data[myref]['Congés consommés']=consommation
        # return sum(consommation)


    def _update_solde(self,matricule):
        mat_ref = enumerate(self.data['Matricule'])
        for mat in mat_ref:
            if mat[1] == matricule:
                myref = mat[0]

        new_solde=self.recap_conge.get(matricule,'')-self.data[myref]['Congés consommés']
        self.data[myref]['Solde congés disponibles']=new_solde
        #todo : add update for "conge recp.csv"


        pass

    def _new_jour_ferie(self):
        pass

