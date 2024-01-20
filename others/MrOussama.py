def saisirElement(inf, sup, message=""):
    while True:
        try:
            element = int(input(message))
            if element in range(inf, sup + 1):
                return element
            print(f"{element} doit être compris entre {inf} et {sup}")
        except ValueError:
            print("Veuillez entrer un nombre entier.")


class Date:
    def __init__(self, jj=1, mm=1, AA=2023):
        self.jour = jj
        self.mois = mm
        self.annee = AA

    def SaisirDate(self):
        self.jour = saisirElement(1, 31, "Entrer le jour :")
        self.mois = saisirElement(1, 12, "Entrer le mois :")
        self.annee = int(input("Entrer l'année:"))

    def return_Date(self):
        return f"{self.jour}/{self.mois}/{self.annee}"

    def is_before(self, other_date):
        return (self.annee, self.mois, self.jour) < (other_date.annee, other_date.mois, other_date.jour)

    def is_after(self, other_date):
        return not self.is_before(other_date) and (self.annee, self.mois, self.jour) != (
            other_date.annee, other_date.mois, other_date.jour)

class Offre_Voyage:
    List_Offers = []

    def __init__(self, Ref="", V_Depart="", V_Arrive="", Statut="Active"):
        self.Ref_Offre = Ref
        self.Ville_Depart = V_Depart
        self.Ville_Arrive = V_Arrive
        self.Statut_Co = Statut
        Offre_Voyage.List_Offers.append(self)

    def Sauvgarder_Offre(self):
        with open("Offre_de_voyage.txt", 'a') as file:
            data = self.__dict__
            for key in data.keys():
                if isinstance(data[key], Date):
                    data[key] = data[key].return_Date()

            file.write(str(data) + "\n")

    def declarer_offre(self):
        print("Remplir le formulaire suivant")
        self.Ref_Offre = input("Reference Contrat: ")
        self.Ville_Depart = input("Ville de départ: ")
        self.Ville_Arrive = input("Ville d'arrivée: ")

    def Bloquer_offre(self):
        self.Statut_Co = "Bloque"

    def Afficher_Offre(self):
        data = self.__dict__
        for key in data.keys():
            if isinstance(data[key], Date):
                data[key] = data[key].return_Date()
        print(data)

    @classmethod
    def filtrer_par_type(cls, offer_type):
        return [offer for offer in cls.List_Offers if isinstance(offer, offer_type)]

    @classmethod
    def Afficher_filtre_par_type(cls, offer_type):
        filtered_by_type = cls.filtrer_par_type(offer_type)
        for instance in filtered_by_type:
            instance.Afficher_Offre()



class Transport_Aller_Simple(Offre_Voyage):
    Nbr_Aller_simple = 0

    def __init__(self, Ref="", V_Depart="", V_Arrive="", Statut_CO="Active", Date_Aller=Date(), Prix=0.00):
        super().__init__(Ref, V_Depart, V_Arrive, Statut_CO)
        Transport_Aller_Simple.Nbr_Aller_simple += 1
        self.Date_Aller = Date_Aller
        self.Prix = Prix

    def declarer_offre(self):
        super().declarer_offre()
        print("Date ALLer:")
        self.Date_Aller.SaisirDate()
        self.Prix = float(input("Prix :"))

    def Mettre_A_JOUR(self):
        print("1: Mettre à jour le prix:")
        print("2: Mettre à jour la date Aller  :")
        print("3: Mettre à jour le prix et date aller:")
        print("4:Mettre a jour la date de retour(Cas Trans_Aler_Retour):")
        print("5:Mettre a jour date de retour et prix:")
        print("6:Mettre a jour la date Aller et retour")
        print("7:Mettre a jour tous les 3 :")

        choix = saisirElement(1, 7, "Choix:")

        if choix % 2 == 1:
            print("Entrer le nouveau prix")
            self.Prix = float(input("Entrer le nouveau prix:"))

        if choix == 2 or choix == 3 or choix == 6 or choix == 7:
            print("Entrer la nouvelle date aller:")
            self.Date_Aller = Date()
            self.Date_Aller.SaisirDate()
        if choix >= 4:
            print("Entrer la date de retour:")
            return choix

    def Afficher_Offre(self):
        super().Afficher_Offre()


class Transport_Aller_Retour(Transport_Aller_Simple):
    Nbr_Aller_Retour = 0

    def __init__(self, Ref="", V_Depart="", V_Arrive="", Statut_CO="Active", Date_Aller=Date(), Prix_Aler_Retour=0.00,
                 Date_Retour=Date()):
        Transport_Aller_Retour.Nbr_Aller_Retour += 1

        super().__init__(Ref, V_Depart, V_Arrive, Statut_CO, Date_Aller, Prix_Aler_Retour)
        self.Date_Arrive = Date_Retour

    def declarer_offre(self):
        super().declarer_offre()
        self.Date_Arrive = Date(0, 0, 0)
        print("Date de Retour")
        self.Date_Arrive.SaisirDate()

    def Afficher_Offre(self):
        super().Afficher_Offre()

    def Mettre_A_JOUR(self):
        choix = super().Mettre_A_JOUR()
        if choix >= 4:
            self.Date_Arrive = Date()
            self.Date_Arrive.SaisirDate()


class Hebergement(Offre_Voyage):
    def __init__(self, Ref="", V_Depart="", V_Arrive="", Statut="", Date_debut=Date(0, 0, 0), Nb_Nuits=0,
                 Type="déjeuner", Prix_nuit=0.00):
        super().__init__(Ref, V_Depart, V_Arrive, Statut)
        assert Type in ["déjeuner", "demi-pension", "pension", "complète"], f"{Type} non valable"
        self.Date_debut = Date_debut
        self.Nb_Nuits = Nb_Nuits
        self.Type_Heb = Type
        self.Prix_nuit = Prix_nuit

    def declarer_offre(self):
        super().declarer_offre()
        self.Date_debut.SaisirDate()
        self.Nb_Nuits = int(input("Nombres de nuits :"))
        self.Type_Heb = input("Type d'hébergement (déjeuner, demi-pension, pension, complète):")
        self.Prix_nuit = float(input("Prix Par nuit:"))

    def Mettre_A_Jour(self):
        print("1: Mettre à jour le prix par nuit:")
        print("2: Mettre à jour la date de début:")
        print("3: Mettre à jour les deux:")
        choix = saisirElement(1, 3, "Choix:")
        if choix == 1 or choix == 3:
            self.Prix_nuit = float(input("Entrer le nouveau prix par nuit:"))
        if choix == 2 or choix == 3:
            self.Date_debut = Date()
            self.Date_debut.SaisirDate()

    def Sauvgarder_Offre(self):
        super().Sauvgarder_Offre()

    def Afficher_Offre(self):
        super().Afficher_Offre()


class Formule_complete(Transport_Aller_Retour, Hebergement):
    def __init__(self, Ref="", V_Depart="", V_Arrive="", Statut_CO="", Date_Aller=Date(0, 0, 0),
                 Prix_Aler_Retour=0.00, Date_Retour=Date(), Date_debut=Date(0, 0, 0), Nb_Nuits=0,
                 Type="déjeuner", Prix_nuit=0.00,
                 type1="Week-End"):
        assert type1 in ["Week-End", "Semaine"], f"{type1} non valable"
        Transport_Aller_Retour.__init__(self, Ref, V_Depart, V_Arrive, Statut_CO, Date_Aller, Prix_Aler_Retour, Date_Retour)
        Hebergement.__init__(self, Ref, V_Depart, V_Arrive, Statut_CO, Date_debut, Nb_Nuits, Type, Prix_nuit)

        self.type1 = type1

    def declarer_offre(self):
        Transport_Aller_Retour.declarer_offre(self)
        Hebergement.declarer_offre(self)

    def Afficher_Offre(self):
        Transport_Aller_Retour.Afficher_Offre(self)
        Hebergement.Afficher_Offre(self)

    def Mettre_A_JOUR(self):
        Transport_Aller_Retour.Mettre_A_JOUR(self)
        Hebergement.Mettre_A_Jour(self)


class Reservation:
    def __init__(self, Ref_res="", Type_Offre="", Ref_Offre="", Date_depart=Date(),
                 Date_retour=None, Genre="", Nom="", Prenom="", Nationalite="", Num_Passeport="",
                 Etat_Reservation="En cours", Total_A_Payer=0.00):
        self.Ref_reservation = Ref_res
        self.Type_Offre = Type_Offre
        self.Ref_Offre = Ref_Offre
        self.Date_depart = Date_depart
        self.Date_retour = Date_retour
        self.Genre = Genre
        self.Nom = Nom
        self.Prenom = Prenom
        self.Nationalite = Nationalite
        self.Num_Passeport = Num_Passeport
        self.Etat_Reservation = Etat_Reservation
        self.Total_A_Payer = Total_A_Payer

    def saisir_reservation(self, transport_instance, hebergement_instance):
        print("Remplir le formulaire de réservation:")
        self.Ref_reservation = input("Référence de réservation: ")
        self.Type_Offre = input("Type d'offre: ")
        self.Ref_Offre = input("Référence de l'offre associée: ")
        print("Date de départ:")
        self.Date_depart.SaisirDate()
        self.Date_retour = None
        if self.Type_Offre.lower() == "aller_retour":
            print("Date de retour (Cas de l'offre Aller-Retour):")
            self.Date_retour = Date()
            self.Date_retour.SaisirDate()
        self.Genre = input("Genre: ")
        self.Nom = input("Nom: ")
        self.Prenom = input("Prénom: ")
        self.Nationalite = input("Pays d'origine du passeport (Nationalité): ")
        self.Num_Passeport = input("N° Passeport: ")
        self.Etat_Reservation = "En cours"
        self.calculer_total_a_payer(transport_instance, hebergement_instance)

    def calculer_total_a_payer(self, transport_instance, hebergement_instance):
        total_transport = 0
        if isinstance(transport_instance, Transport_Aller_Retour):
            total_transport = transport_instance.Prix
        elif isinstance(transport_instance, Transport_Aller_Simple):
            total_transport = transport_instance.Prix

        total_hebergement = hebergement_instance.Prix_nuit * hebergement_instance.Nb_Nuits if isinstance(
            hebergement_instance, Hebergement) else 0
        self.Total_A_Payer = total_transport + total_hebergement
        self.Total_A_Payer *= 0.9

    def afficher_reservation(self):
        data = self.__dict__
        for key in data.keys():
            if isinstance(data[key], Date):
                data[key] = data[key].return_Date()
        print(str(data))


T = Transport_Aller_Retour("A125", "Tanger", "Fes", "Active", Date(2, 5, 2024), 1233, Date(12, 12, 2024))
T2 = Transport_Aller_Simple("A12", "Khmiss Zmamra", "Fes", "Active", Date(6, 6, 2024), 123)

print("All offers:")
Offre_Voyage.Afficher_filtre_par_type(Offre_Voyage)

print("\nFiltered by Transport_Aller_Retour:")
Offre_Voyage.Afficher_filtre_par_type(Transport_Aller_Retour)

start_Date = Date(2, 3, 2024)
end_Date = Date(10, 5, 2024)

print("\nFiltered by Period:")
Offre_Voyage.Afficher_filtre_par_period(start_Date, end_Date)

