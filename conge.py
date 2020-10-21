import datetime as dt
import calendar, itertools, os

class Conge:
    td = dt.date.today()
    checkingfile=True
    updateconge=True
    updated=True
    jours_feries={"Noel":dt.date(td.year,12,25),"Nouvel an":dt.date(td.year,1,1)}
    filename='reftoday.txt'
    existfile = os.path.exists(filename)
    #on recup la date de derniere maj de conge via la fichier
    #todo : add chechking the validyty of data in the file
    #fixme : make it prettier
    while checkingfile:
        if existfile:
            with open(filename, 'r', encoding='utf8') as f:
                reader=f.read(10)
            #on compare reader à la date d'aujourd'hui
            try:
                ld=dt.datetime.strptime(reader,'%Y-%m-%d')
            except ValueError:
                with open(filename, 'w', encoding='utf8') as f:
                    writer = f.write(str(td))
                checkingfile==False
                print("Date expected. we fixed it")

            if ld<dt.datetime(td.year,td.month,td.day) :
                with open(filename, 'w', encoding='utf8') as f:
                    reader = f.write(str(td))
                    checkingfile=False

                #todo : insert lauchn update conge genere, consomme et solde
            elif ld==dt.datetime(td.year,td.month,td.day):
                checkingfile=False
                updateconge=False
                updated=False
                pass
            else :
                #todo : insert message box : something wrong with date : 'last time file was opened was in the future'
                print("Something's wrong. you updated things in the future")
                checkingfile==False
                updateconge=False
                updated=False

                break
        else:
            with open(filename, 'w', encoding='utf8') as f:
                writer = f.write(str(td))
            checkingfile = False

    def __init__(self,data,base_conge):
        self.data = data
        self.recap_conge = {}
        self.base_conge = base_conge
        print('base conge :')
        print(self.base_conge)
        while self.updateconge:
            for employee in self.data:
                self.genererconge(employee['Matricule'], employee['Date de début'])
                self.congesconsommes(employee['Matricule'])
                self.update_solde(employee['Matricule'])
            self.updateconge = False



    def genererconge(self,matricule,datedebut):
        #fixme : we use too much memory. stocking 2 time the same data
        date_sample=datedebut.split('/')
        delta_years=self.td.year-int(date_sample[2])
        delta_months=self.td.month-int(date_sample[1])
        ratio_day1=1-(int(date_sample[0])-1)/calendar.monthrange(int(date_sample[2]),int(date_sample[1]))[1]
        ratio_day2=(self.td.day)/calendar.monthrange(int(self.td.year),int(self.td.month))[1]
        final=(((delta_years*12)+delta_months)*2.5)+(ratio_day1*2.5)+(ratio_day2*2.5)
        self.recap_conge[matricule]=final

        #fixme : make it prettier
        mymat=(x['Matricule'] for x in self.data)
        mat_ref = enumerate(mymat)
        for num,mat in mat_ref:
            if mat == matricule:
                myref = num
        self.data[myref]['Congés générés'] = final

    def congesconsommes(self,matricule):
        #todo : add a way to not take the future dayooff in the future not taken yet
        #todo : add a field that return all dayoff already consummed and those not consummed yet
        # todo : add update for "conge recp.csv"
        #todo : add case handler if mat not in base_conge

        #tuple of all mat in self.data
        datamat=(x['Matricule'] for x in self.data)
        mat_ref = enumerate(datamat)
        for num,mat in mat_ref:
            if mat == matricule:
                myref = num

        #tuple of all mat in self.base_conge (generator)
        basecongemat=(x['Matricule'] for x in self.base_conge)
        basecongemat_length=sum(1 for matricule in basecongemat)
        #first verify if base_conge is not empty
        if basecongemat_length>0:
            for mat in datamat:
                #we calcul the congeconsomme only if the matricule is in base_conge
                if mat in basecongemat:
                    checker=[]
                    for entry in self.base_conge:
                        if entry.get('Matricule','')==matricule:
                            checker.append(1)
                        else:
                            checker.append(0)
                    #fixme : to sum as a generator
                    consommation = sum(list(itertools.compress(self.base_conge,checker)))
                    if consommation=='':
                        consommation=0
                    self.data[myref]['Congés consommés'] = consommation
        else :
            for employee in self.data:
                employee['Congés consommés'] = 0

        #todo: verifier si ca update directement controller.application.data ou juste la ref ici.


    def update_solde(self,matricule):
        #todo : add trigger when a new conge is created
        #todo : add case handler if mat not in base_conge

        mymat=(x['Matricule'] for x in self.data)
        mat_ref = enumerate(mymat)
        for num,mat in mat_ref:
            if mat == matricule:
                myref = num

        new_solde=self.data[myref]['Congés générés']-self.data[myref]['Congés consommés']
        # new_solde=0
        # congegen=self.data[myref]['Congés générés']
        # congecons=self.data[myref]['Congés consommés']

        self.data[myref]['Solde congés disponibles']=new_solde
        #todo : add update for "conge recp.csv"
        pass
    def update_conge_csv(self):
        return self.updated,self.data

    def new_jour_ferie(self):
        pass

