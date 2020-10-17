import datetime as dt
import calendar
import itertools

class Conge:
    td = dt.date.today()
    checkingfile=True
    updateconge=True
    jours_feries={"Noel":dt.date(td.year,12,25),"Nouvel an":dt.date(td.year,1,1)}
    filename='reftoday.txt'
    existfile = os.path.exists(filename)
    while checkingfile:
        if existfile:
            with open(filename, 'r', encoding='utf8') as f:
                reader=f.read(10)
            #on compare reader à la date d'aujourd'hui
            ld=dt.datetime.strptime(reader,'%Y-%m-%d')
            if ld<td :
                with open(filename, 'w', encoding='utf8') as f:
                    reader = f.write(td)
                    checkingfile=False
                #todo : insert lauchn update conge genere, consomme et solde
            elif ld==td:
                checkingfile=False
                updateconge=False
                pass
            else :
                #todo : insert message box : something wrong with date : 'last time file was opened was in the future'
                print("Something's wrong. you updated things in the future")
                checkingfile==False
                updateconge=False
                break
        else:
            with open(filename, 'w', encoding='utf8') as f:
                reader = f.write(td)


    def __init__(self,data,base_conge):
        self.data = data
        self.recap_conge = {}
        self.base_conge = base_conge

        while self.updateconge:
            for employee in data:
                self._genererconge(employee['Matricule'],employee['Date de début'])
                self._congesconsommes(employee['Matricule'])
                self._update_solde(employee['Matricule'])
            self.updateconge==False



    def _genererconge(self,matricule,datedebut):
        #fixme : we use too much memory. stocking 2 time the same data
        delta_years=self.td.year-datedebut.year
        delta_months=self.td.month-datedebut.month
        ratio_day1=1-(self.td.day-1)/calendar.monthrange(int(self.td.year),int(self.td.month))[1]
        ratio_day2=datedebut.day/calendar.monthrange(int(datedebut.year),int(datedebut.month))[1]
        final=(((delta_years*12)+delta_months)*2.5)+(ratio_day1*2.5)+(ratio_day2*2.5)
        self.recap_conge[matricule]=final

        mat_ref = enumerate(self.data['Matricule'])
        for mat in mat_ref:
            if mat[1] == matricule:
                myref = mat[0]
        self.data[myref]['Congés générés'] = final

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
        #todo: verifier si ca update directement controller.application.data ou juste la ref ici.


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

