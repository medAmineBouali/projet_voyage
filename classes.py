from fontions import *

class Date():
        #mohamed amine boauli
    def __init__(self):
        self.jour = 0
        self.mois = 0 
        self.annee = 0
    def set_date(self,message = ""):
        while True:
            try:
                jour = saisirElement(1,31,"Entrer le jour "+message+" : ")
                mois = saisirElement(1,12,"Entrer le mois "+message+" : ")
                annee = int(input("Entrer l'année "+message+" : "))
                validation_Date(jour,mois,annee)
                self.jour = jour
                self.mois = mois
                self.annee = annee
                break
            except TypeError:
                print("les valeurs doient etre sous form des nombres")
            except ValueError as e:
                print("Erreur: ",e)
    def set_with_string(self,string:str):
        date = string.split("/")
        self.jour = int(date[0])
        self.mois = int(date[1])
        self.annee = int(date[2])

    def is_between(self, start_date, end_date):
        return start_date <= self <= end_date

    def __lt__(self, other):
        return (self.annee, self.mois, self.jour) < (other.annee, other.mois, other.jour)

    def __eq__(self, other):
        return (self.jour, self.mois, self.annee) == (other.jour, other.mois, other.annee)
    
    def __le__(self, other):
        return self < other or self == other
    
    def __gt__(self, other):
        return not self <= other

    def __ge__(self, other):
        return not self < other
    
    def format_string(self):
        return f"{NbToStr(self.jour)}/{NbToStr(self.mois)}/{NbToStr(self.annee)}"
class Offre():
    #mohamed amine boauli
    def __init__(self):
        self.ref= 0
        self.v_depart = "ville_depart"
        self.v_arrive = "ville d'arrive"
        self.statut = "Active"
    def set_voyage(self):
        while True:
            try:    
                print("Info sur le vole:\n") 
                self.ref= str(input("Entrez le ref de voyage:\n"))
                self.v_depart = str(input("Entrez la ville de depart\n"))
                self.v_arrive = str(input("Entrez la ville d'arrive\n"))
                break
            except Exception as e:
                print(f"erreur: {e}")

    def sauvgarder_dans_fichier(self):
        with open("Offre_de_voyage.txt", "a") as file:
            data = self.__dict__.copy()
            for key,value in data.items():
                if isinstance(value, Date):
                    data[key] = value.format_string()

            file.write(str(data) + "\n")

    def sauvgarder(self,dic:dict):
        #Hamza Laouar
        dic[self.ref] = self
    def info(self):
        return f"vole de ref {self.ref} de {self.v_depart} vers {self.v_arrive}\n"
    def block(self):
        self.statut = "Blocked"
    def unblock(self):
        self.statut = "Active"

class Voyage_simple(Offre):
    #mohamed amine boauli
    def __init__(self):
        super().__init__()
        self.d_depart = Date()
        self.prix = 0
        self.type_offre = "aller_simple"
    def set_voyage(self):
        super().set_voyage()
        self.d_depart.set_date("de depart")
        while True:
            try:
                self.prix = int(input("Entre le prix de cette vole direct:"))
                break
            except Exception as e:
                print(f"erreur: {e}\n")
        
        return self
    
    def Mettre_A_Jour(self):
        print("1: Mettre à jour le prix:")
        print("2: Mettre à jour la date aller :")
        print("3: Mettre à jour le prix et date aller:")

        choix = saisirElement(1, 3, "Choix:")

        if choix  == 1 or choix == 3:
            print("Entrer le nouveau prix")
            self.prix = float(input("Entrer le nouveau prix:"))

        if choix == 2 or choix == 3:
            print("Entrer la nouvelle date aller:")
            self.d_depart.set_date(" d'aller")

    def info(self):
        return f"{super().info()} avec départ le {self.d_depart.format_string()} et prix {self.prix}\n"

class Voyage_aller_retour(Voyage_simple):
    def __init__(self):
        super().__init__()
        self.d_retour = Date()
        self.type_offre = "aller_retour"
    def set_voyage(self):
        super().set_voyage()
        while True:
            try:
                self.d_retour.set_date(" de retour")
                assert self.d_retour > self.d_depart , "date de retour doit etre apres la date de depart\n"
                break
            except Exception as e:
                print(e)
        self.prix *= 2
        return self
    def Mettre_A_Jour(self):
        print("1: Mettre à jour le prix:")
        print("2: Mettre à jour la date aller :")
        print("3: Mettre à jour le prix et date aller:")
        print("4:Mettre a jour la date de retour:")
        print("5:Mettre a jour date de retour et prix:")
        print("6:Mettre a jour la date Aller et retour")
        print("7:Mettre a jour tous les 3 :")

        choix = saisirElement(1, 7, "Choix:")

        if choix % 2 == 1:
            print("Entrer le nouveau prix")
            self.prix = float(input("Entrer le nouveau prix:"))

        if choix == 2 or choix == 3 or choix == 6 or choix == 7:
            print("Entrer la nouvelle date aller:")
            self.d_depart.set_date(" d'aller")
        if choix >= 4:
            print("Entrer la date de retour:")
            while True:
                try:
                    self.d_retour.set_date(" de retour")
                    assert self.d_retour > self.d_depart , "date de retour doit etre apres la date de depart\n"
                    break
                except Exception as e:
                    print(e)
            
    def info(self):
        return f"{super().info()} avec retour le {self.d_retour.format_string()}\n"

class Hebergement(Offre):
    #Hamza Laouar
    def __init__(self):
        self.date_debut = Date()
        self.nombre_nuits = 0
        self.type_hebergement = ""
        self.prix_par_nuit = 0
    def set_hebergement(self):
        self.date_debut.set_date(" de debut d'hebergement")

        while True:
            try:
                self.nombre_nuits = int(input("Entrez le nombre de nuits:\n"))
                self.type_hebergement = input_type_hebergement()
                self.prix_par_nuit = float(input("Entrez le prix par nuit:\n"))
                break
            except ValueError as e:
                print(f"Erreur: {e}\n")

        return self
    def Mettre_A_Jour(self):
        print("1: Mettre à jour le prix par nuit:")
        print("2: Mettre à jour la date de deubut:")
        print("3: Mettre à jour les deux:")
        choix = saisirElement(1, 3, "Choix:")
        if choix == 1 or choix == 3:
            self.prix_par_nuit = float(input("Entrer le nouveau prix par nuit:"))
        if choix == 2 or choix == 3:
            self.Date_debut = Date()
            self.Date_debut.set_date()
    def prix_total(self):
        return self.nombre_nuits * self.prix_par_nuit

    def info_h(self):
        return f"Hebrgemnt avec début le {self.date_debut.format_string()}, {self.nombre_nuits} nuit(s), type: {self.type_hebergement}, prix par nuit: {self.prix_par_nuit:.2f}, prix total: {self.prix_total():.2f}$\n"

class Voyage_complet(Voyage_aller_retour, Hebergement):
    def _init_(self):
        self.type_duree = ""
        Voyage_aller_retour.__init__(self)
        Hebergement.__init__(self)
        self.type_offre = "complet"

    def set_voyage(self):
        self.type_duree = input_type_duree()
        Voyage_aller_retour.set_voyage(self)
        Hebergement.set_hebergement(self)
        
    def Mettre_A_Jour(self):
        Voyage_aller_retour.Mettre_A_Jour(self)
        Hebergement.Mettre_A_Jour(self)
    def info(self):
        return "Voyages Complet:\n" + "-"+Voyage_aller_retour.info(self) + "-"+Hebergement.info_h(self)

class Reservation:
    #Hamza Laouar
    def __init__(self, Ref_res="Ref_res", type_offre="type_offre", Ref_Offre="Ref_Offre",
                 Date_depart=None, Date_retour=None, Genre="Genre", Nom="Nom", Prenom="Prenom",
                 Nationalite="Nationalite", Num_Passeport=0, Etat_Reservation="en cours", Total_A_Payer=0):
        self.Ref_reservation = Ref_res
        self.type_offre = type_offre
        self.Ref_Offre = Ref_Offre
        self.Date_depart = Date_depart if type(Date_depart) is Date else Date()
        self.Date_retour = Date_retour if type(Date_retour) is Date else Date()
        self.Genre = Genre
        self.Nom = Nom
        self.Prenom = Prenom
        self.Nationalite = Nationalite
        self.Num_Passeport = Num_Passeport
        self.Etat_Reservation = Etat_Reservation
        self.Total_A_Payer = Total_A_Payer

    def set_reservation(self, offre_instance):
        self.Genre = str(input("Genre: "))
        self.Nom = str(input("Nom: "))
        self.Prenom = str(input("Prénom: "))
        self.Nationalite = str(input("Pays d'origine du passeport (Nationalité): "))
        self.Num_Passeport = str(input("N° Passeport: "))
        self.Etat_Reservation = "En cours"
        print("Remplir le formulaire de réservation:")
        self.Ref_reservation = str(input("Référence de réservation: "))
        self.type_offre = offre_instance.type_offre

        if isinstance(offre_instance, Voyage_simple):
            self.Ref_Offre = offre_instance.ref
            self.Date_depart = offre_instance.d_depart
            self.Total_A_Payer = offre_instance.prix * 0.9

        elif isinstance(offre_instance, Voyage_aller_retour):
            self.Ref_Offre = offre_instance.ref
            self.Date_depart = offre_instance.d_depart
            self.Date_retour = offre_instance.d_retour
            self.Total_A_Payer = offre_instance.prix * 0.9

        elif isinstance(offre_instance, Voyage_complet):
            self.Ref_Offre = offre_instance.ref
            self.type_duree = offre_instance.type_duree
            self.Date_depart = offre_instance.d_depart
            self.Date_retour = offre_instance.d_retour
            self.Total_A_Payer = (offre_instance.prix * 0.9) + (offre_instance.prix_par_nuit * offre_instance.nombre_nuits * 0.9)


    def afficher_reservation(self):
        data = self.__dict__.copy()
        for key in data.keys():
            if isinstance(data[key], Date):
                data[key] = data[key].format_string()
        print(str(data))
    def sauvgarder_dans_fichier(self):
        with open("reservation.txt", "a") as file:
            data = self.__dict__.copy()
            for key,value in data.items():
                if isinstance(value, Date):
                    data[key] = value.format_string()
            file.write(str(data) + "\n")
    def confirmation(self):
        #Hamza Laouar
        option = ["Confirmer.","Annuler.","Rendre globale."] 
        print("Voulez vous:")
        choix = menu(option)
        if choix == 1:
            self.Etat_Reservation = "confirme"
        elif choix == 2:
            self.Etat_Reservation = "annule"
        elif choix == 3:
            self.Etat_Reservation = "globale"

    def sauvgarder(self,dic:dict):
        dic[self.Ref_reservation] = self

def affichage_offres(filtre:int,list_offres:dict):
    types = ["aller simple","aller retour","complet"]
    if filtre == 1:
        for offre in list_offres.values():
            print(offre.info())
    elif filtre == 2:
        choix = menu(types)
        if choix == 1:
            for offre in list_offres.values():
                if type(offre) is Voyage_simple:
                    print(offre.info())
        elif choix == 2:
            for offre in list_offres.values():
                if type(offre) is Voyage_aller_retour:
                    print(offre.info())
        elif choix == 3:
            for offre in list_offres.values():
                if type(offre) is Voyage_complet:
                    print(offre.info())
