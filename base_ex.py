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
    image_file =8


class MyLists:
    sexe_list=["Femme","Homme"]
    etat_civil_list=["Célibataire","Divorcé(e)","Marié(e)","Veuf(ve)"]
    departement_list=["Commercial","Comptable et Financier","Logistique"]
    motif_fin_list=["Non renouvelé","Licenciement","Démission"]
    
class MyInfos:
    data={
        "Error 404":{"creation":"404",
                     "consultation":"404",
                     "modification":"404",
                     "fire":"404",
                     "type":"404"
                     },
        "Matricule":{"creation":True,
                     "consultation":True,
                     "modification":True,
                     "fire":"disabled",
                     "type":FieldTypes.string
                     },
        "Noms":{"creation":True,
                "consultation":True,
                "modification":True,
                "fire":"disabled",
                "type":FieldTypes.string
                },
        "Prénoms":{"creation":True,
                   "consultation":True,
                   "modification":True,
                   "fire":"disabled",
                   "type":FieldTypes.string
                   },
        "Date de naissance":{"creation":True,
                             "consultation":True,
                             "modification":True,
                             "fire":"disabled",
                             "type":FieldTypes.string
                             },
        "Lieu de naissance":{"creation":True,
                             "consultation":True,
                             "modification":True,
                             "fire":"disabled",
                             "type":FieldTypes.string
                             },
        "Date de naissance":{"creation":True,
                             "consultation":True,
                             "modification":True,
                             "fire":"disabled",
                             "type":FieldTypes.string
                             },
        "Sexe":{"creation":True,
                "consultation":True,
                "modification":True,
                "type":FieldTypes.string_list,
                "fire":"disabled",
                "values":MyLists.sexe_list
                },
        "CIN":{"creation":True,
               "consultation":True,
               "modification":True,
               "fire":"disabled",
               "type":FieldTypes.string
               },
        "Date de délivrance":{"creation":True,
                              "consultation":True,
                              "modification":True,
                              "fire":"disabled",
                              "type":FieldTypes.string
                              },
        "Lieu de délivrance":{"creation":True,
                              "consultation":True,
                              "modification":True,
                              "fire":"disabled",
                              "type":FieldTypes.string
                              },
        "Adresse Réel":{"creation":True,
                        "consultation":True,
                        "modification":True,
                        "fire":"disabled",
                        "type":FieldTypes.string
                        },
        "Adresse Administrtive":{"creation":True,
                                 "consultation":True,
                                 "modification":True,
                                 "fire":"disabled",
                                 "type":FieldTypes.string
                                 },
        "Téléphone 01":{"creation":True,
                        "consultation":True,
                        "modification":True,
                        "fire":"disabled",
                        "type":FieldTypes.string
                        },
        "Téléphone 02":{"creation":True,
                        "consultation":True,
                        "modification":True,
                        "fire":"disabled",
                        "type":FieldTypes.string},
        "Email perso":{"creation":True,
                       "consultation":True,
                       "modification":True,
                       "fire":"disabled",
                       "type":FieldTypes.string},
        "Etat civil":{"creation":True,
                      "consultation":True,
                      "modification":True,
                      "fire":"disabled",
                      "type":FieldTypes.string_list,
                      "values":MyLists.etat_civil_list
                      },
        "Nombre d'enfants":{"creation":True,
                            "consultation":True,
                            "modification":True,
                            "fire":"disabled",
                            "type":FieldTypes.integer
                            },
        "N° CNAPS":{"creation":True,
                    "consultation":True,
                    "modification":True,
                    "fire":"disabled",
                    "type":FieldTypes.string
                    },
        "Date de début":{"creation":True,
                         "consultation":True,
                         "modification":True,
                         "fire":"disabled",
                         "type":FieldTypes.string
                         },
        "Salaire de base":{"creation":True,
                           "consultation":True,
                           "modification":True,
                           "fire":"disabled",
                           "type":FieldTypes.decimal
                           },
        "Email pro":{"creation":True,
                     "consultation":True,
                     "modification":True,
                     "fire":"disabled",
                     "type":FieldTypes.string
                     },
        "Poste":{"creation":True,
                 "consultation":True,
                 "modification":True,
                 "fire":"disabled",
                 "type":FieldTypes.string
                 },
        "Département":{"creation":True,
                       "consultation":True,
                       "modification":True,
                       "fire":"disabled",
                       "type":FieldTypes.string_list,
                       "values":MyLists.departement_list
                       },
        "Solde congés disponibles":{"creation":False,
                                  "consultation":True,
                                  "modification":True,
                                  "fire":"disabled",
                                  "type":FieldTypes.decimal
                                  },
        "Congés consommés":{"creation":False,
                            "consultation":True,
                            "modification":True,
                            "fire":"disabled",
                            "type":FieldTypes.decimal
                            },
        "Date fin":{"creation":False,
                    "consultation":True,
                    "modification":True,
                    "fire":"NORMAL",
                    "type":FieldTypes.string
                    },
        "Motif fin de contrat":{"creation":False,
                                "consultation":True,
                                "modification":True,
                                "fire":"NORMAL",
                                "type":FieldTypes.string_list,
                                "values":MyLists.motif_fin_list
                                },
        "Note":{"creation":True,
                "consultation":True,
                "modification":True,
                "fire":"NORMAL",
                "type":FieldTypes.string_long
                },
        "Image CIN":{"creation":True,
                     "consultation":True,
                     "modification":True,
                     "fire":"disabled",
                     "type":FieldTypes.image_file
                     },
        "Photo de l'employé":{"creation":True,
                              "consultation":True,
                              "modification":True,
                              "fire":"NORMAL",
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
                csvwriter = csv.DictWriter(fh, fieldnames=self.fields.keys())
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
                               "callback":"modification"},
        }

class MyActionButtons:
    data = {"Précédent":{"creation":False,
                "consultation":True,
                "modification":False,
                "callback" : "Previous"
                        },
        "Suivant":{"creation":False,
                "consultation":True,
                "modification":False,
                "callback" : "Next"
                        },
        "Sauvegarder":{"creation" : True,
                "consultation" : True,
                "modification" : True,
                "callback" : "Save"
                        },
            }
    
        
        


        
        
        
        
