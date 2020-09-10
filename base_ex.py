import csv
import os

class FieldTypes:
    string = 1
    string_list = 2
    iso_date_string = 3
    string_long = 4
    decimal = 5
    integer = 6
    boolean = 7
    image_file = 8
    iso_date_age_string = 9
    string_mail = 10
    string_phone = 11


class MyLists:
    sexe_list=["Femme","Homme"]
    etat_civil_list=["Célibataire","Divorcé(e)","Marié(e)","Veuf(ve)"]
    departement_list=["Commercial","Comptable et Financier","Logistique"]
    motif_fin_list=["Non renouvelé","Licenciement","Démission"]


class MyTitles:
    data={"creation":"NOUVEL EMPLOYE",
          "consultation":"CONSULTATION DE LA FICHE DE L'EMPLOYE",
          "modification":"MODIFICATION DE LA FICHE DE L'EMPLOYE",
          "fire":"DEPART D'UN EMPLOYE"
    }
    #todo corriger les champs a afficher en fonction du mode
class MyInfos:
    data={
        "Error 404":{"csvheader":False,
                     "creation":{"mode":False,"row":30},
                     "consultation":{"mode":False,"row":30},
                     "modification":{"mode":False,"row":30},
                     "fire":{"mode":False,"row":30,"state":"normal"},
                     "type":FieldTypes.string
                     },
        "Matricule":{"csvheader":True,
                     "creation":{"mode":True,"row":0},
                     "consultation":{"mode":True,"row":0},
                     "modification":{"mode":True,"row":0},
                     "fire":{"mode":True,"row":3,"state":"readonly"},
                     "type":FieldTypes.string
                     },
        "Noms":{"csvheader":True,
                "creation":{"mode":True,"row":1},
                "consultation":{"mode":True,"row":1},
                "modification":{"mode":True,"row":1},
                "fire":{"mode":True,"row":4,"state":"readonly"},
                "type":FieldTypes.string
                },
        "Prénoms":{"csvheader":True,
                   "creation":{"mode":True,"row":2},
                   "consultation":{"mode":True,"row":2},
                   "modification":{"mode":True,"row":2},
                   "fire":{"mode":True,"row":5,"state":"readonly"},
                   "type":FieldTypes.string
                   },
        "Date de naissance":{"csvheader":True,
                             "creation":{"mode":True,"row":3},
                             "consultation":{"mode":True,"row":3},
                             "modification":{"mode":True,"row":3},
                             "fire":{"mode":True,"row":6,"state":"readonly"},
                             "type":FieldTypes.iso_date_age_string
                             },
        "Lieu de naissance":{"csvheader":True,
                             "creation":{"mode":True,"row":4},
                             "consultation":{"mode":True,"row":4},
                             "modification":{"mode":True,"row":4},
                             "fire":{"mode":True,"row":7,"state":"readonly"},
                             "type":FieldTypes.string
                             },
        "Sexe":{"csvheader":True,
                "creation":{"mode":True,"row":5},
                "consultation":{"mode":True,"row":5},
                "modification":{"mode":True,"row":5},
                "fire":{"mode":True,"row":8,"state":"readonly"},
                "type": FieldTypes.string_list,
                "values":MyLists.sexe_list
                },
        "CIN":{"csvheader":True,
               "creation":{"mode":True,"row":6},
               "consultation":{"mode":True,"row":6},
               "modification":{"mode":True,"row":6},
               "fire":{"mode":True,"row":9,"state":"readonly"},
               "type":FieldTypes.string
               },
        "Date de délivrance":{"csvheader":True,
                              "creation":{"mode":True,"row":7},
                              "consultation":{"mode":True,"row":7},
                              "modification":{"mode":True,"row":7},
                              "fire":{"mode":True,"row":10,"state":"readonly"},
                              "type":FieldTypes.iso_date_string
                              },
        "Lieu de délivrance":{"csvheader":True,
                              "creation":{"mode":True,"row":8},
                              "consultation":{"mode":True,"row":8},
                              "modification":{"mode":True,"row":8},
                              "fire":{"mode":True,"row":11,"state":"readonly"},
                              "type":FieldTypes.string
                              },
        "Adresse Réel":{"csvheader":True,
            "creation":{"mode":True,"row":9},
                        "consultation":{"mode":True,"row":9},
                        "modification":{"mode":True,"row":9},
                        "fire":{"mode":True,"row":12,"state":"readonly"},
                        "type":FieldTypes.string
                        },
        "Adresse Administrtive":{"csvheader":True,
            "creation":{"mode":True,"row":10},
                                 "consultation":{"mode":True,"row":10},
                                 "modification":{"mode":True,"row":10},
                                 "fire":{"mode":True,"row":13,"state":"readonly"},
                                 "type":FieldTypes.string
                                 },
        "Téléphone 01":{"csvheader":True,
            "creation":{"mode":True,"row":11},
                        "consultation":{"mode":True,"row":11},
                        "modification":{"mode":True,"row":11},
                        "fire":{"mode":True,"row":14,"state":"readonly"},
                        "type":FieldTypes.string_phone
                        },
        "Téléphone 02":{"csvheader":True,
            "creation":{"mode":True,"row":12},
                        "consultation":{"mode":True,"row":12},
                        "modification":{"mode":True,"row":12},
                        "fire":{"mode":True,"row":15,"state":"readonly"},
                        "type":FieldTypes.string_phone
                        },
        "Email perso":{"csvheader":True,
            "creation":{"mode":True,"row":13},
                        "consultation":{"mode":True,"row":13},
                        "modification":{"mode":True,"row":13},
                        "fire":{"mode":True,"row":16,"state":"readonly"},
                        "type":FieldTypes.string_mail
                        },
        "Etat civil":{"csvheader":True,
                      "creation":{"mode":True,"row":14},
                      "consultation":{"mode":True,"row":14},
                      "modification":{"mode":True,"row":14},
                      "fire":{"mode":True,"row":17,"state":"readonly"},
                      "type":FieldTypes.string_list,
                      "values":MyLists.etat_civil_list
                      },
        "Nombre d'enfants":{"csvheader":True,
            "creation":{"mode":True,"row":15},
                            "consultation":{"mode":True,"row":15},
                            "modification":{"mode":True,"row":15},
                            "fire":{"mode":True,"row":18,"state":"readonly"},
                            "type":FieldTypes.integer
                            },
        "N° CNAPS":{"csvheader":True,
            "creation":{"mode":True,"row":16},
                "consultation":{"mode":True,"row":16},
                "modification":{"mode":True,"row":16},
                "fire":{"mode":True,"row":19,"state":"readonly"},
                    "type":FieldTypes.string
                    },
        "Date de début":{"csvheader":True,
            "creation":{"mode":True,"row":17},
                "consultation":{"mode":True,"row":17},
                "modification":{"mode":True,"row":17},
                "fire":{"mode":True,"row":20,"state":"readonly"},
                         "type":FieldTypes.iso_date_string
                         },
        "Salaire de base":{"csvheader":True,
            "creation":{"mode":True,"row":18},
                "consultation":{"mode":True,"row":18},
                "modification":{"mode":True,"row":18},
                "fire":{"mode":True,"row":21,"state":"readonly"},
                           "type":FieldTypes.decimal
                           },
        "Email pro":{"csvheader":True,
            "creation":{"mode":True,"row":19},
                "consultation":{"mode":True,"row":19},
                "modification":{"mode":True,"row":19},
                "fire":{"mode":True,"row":22,"state":"readonly"},
                     "type":FieldTypes.string_mail
                     },
        "Poste":{"csvheader":True,
            "creation":{"mode":True,"row":20},
                "consultation":{"mode":True,"row":20},
                "modification":{"mode":True,"row":20},
                "fire":{"mode":True,"row":23,"state":"readonly"},
                 "type":FieldTypes.string
                 },
        "Département":{"csvheader":True,
            "creation":{"mode":True,"row":21},
                "consultation":{"mode":True,"row":21},
                "modification":{"mode":True,"row":21},
                "fire":{"mode":True,"row":24,"state":"readonly"},
                       "type":FieldTypes.string_list,
                       "values":MyLists.departement_list
                       },
        "Solde congés disponibles":{"csvheader":True,
                                    "creation":{"mode":False,"row":22},
                                    "consultation":{"mode":True,"row":22},
                                    "modification":{"mode":True,"row":22},
                                    "fire":{"mode":True,"row":25,"state":"readonly"},
                                  "type":FieldTypes.decimal
                                  },
        "Congés consommés":{"csvheader":True,
            "creation":{"mode":False,"row":23},
                "consultation":{"mode":True,"row":23},
                "modification":{"mode":True,"row":23},
                "fire":{"mode":True,"row":26,"state":"readonly"},
                            "type":FieldTypes.decimal
                            },
        "Date fin":{"csvheader":True,
                    "creation":{"mode":False,"row":24},
                    "consultation":{"mode":True,"row":24},
                    "modification":{"mode":True,"row":24},
                    "fire":{"mode":True,"row":0,"state":"normal"},
                    "type":FieldTypes.iso_date_string
                    },
        "Motif fin de contrat":{"csvheader":True,
                                "creation":{"mode":False,"row":25},
                                "consultation":{"mode":True,"row":25},
                                "modification":{"mode":True,"row":25},
                                "fire":{"mode":True,"row":1,"state":"normal"},
                                "type":FieldTypes.string_list,
                                "values":MyLists.motif_fin_list
                                },
        "Note":{"csvheader":True,
            "creation":{"mode":True,"row":26},
                "consultation":{"mode":True,"row":26},
                "modification":{"mode":True,"row":26},
                "fire":{"mode":True,"row":2,"state":"normal"},
                "type":FieldTypes.string_long
                },
        "Image CIN":{"csvheader":True,
            "creation":{"mode":True,"row":27},
                "consultation":{"mode":True,"row":27},
                "modification":{"mode":True,"row":27},
                "fire":{"mode":True,"row":27,"state":"readonly"},
                     "type":FieldTypes.image_file
                     },
        "Photo de l'employé":{"csvheader":True,
                              "creation":{"mode":True,"row":28},
                              "consultation":{"mode":True,"row":28},
                              "modification":{"mode":True,"row":28},
                              "fire":{"mode":True,"row":28,"state":"readonly"},
                              "type":FieldTypes.image_file
                              }
        }

    def __init__(self, filename):
        
        self.filename = filename

    def save_record(self, data, rownum=None):
        newfile= not os.path.exists(self.filename)

        if rownum==None:
            #saving a new entry
            with open(self.filename, 'a') as fh:
                csvwriter = csv.DictWriter(fh,
                                           fieldnames=[x for x in self.data.keys() if self.data[x]['csvheader']],
                                           delimiter=";"
                                           )
                if newfile:
                    csvwriter.writeheader()
                csvwriter.writerow(data)
        else:
            #saving a modification on old entry
            pass
            
class MySideButtons:
    #update the callbacks
    
    data={
        "New employee(destroy)":{"mode":"creation",
                        "callback":"creation"},

        "Update about an employee":{"mode":"modification",
                                    "callback":"modification"},

        "See an employee's profil":{"mode":"consultation",
                                    "callback":"consultation"},

        "Dismiss an employee":{"mode":"fire",
                               "callback":"fire"},
        }

class MyActionButtons:
    data = {"Précédent":{"creation":False,
                "consultation":True,
                "modification":False,
                "fire": False,
                "callback" : "Previous"
                        },
        "Suivant":{"creation":False,
                "consultation":True,
                "modification":False,
                "fire": False,
                "callback" : "Next"
                        },
        "Sauvegarder":{"creation" : True,
                "consultation" : True,
                "modification" : True,
                "fire": True,
                "callback" : "Save"
                        },
            }
    
        
        


        
        
        
        
