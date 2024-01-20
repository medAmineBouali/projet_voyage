class Voyage():
    def _init_(self, ref_offre):
        self.ref_offre = ref_offre
        self.ville_depart = input("Ville de départ : ")
        self.ville_arrivee = input("Ville d'arrivée : ")

    def affichage(self):
        print(f"Ref. offre : {self.ref_offre}\nVille de départ : {self.ville_depart}\nVille d'arrivée : {self.ville_arrivee}")

    def infos_generaux_dico(self):
        dico1 = {"Ref. Offre": self.ref_offre, "Ville-depart": self.ville_depart, "Ville-arrivee": self.ville_arrivee}
        return str(dico1)

    def sauvegarder_dans_fichier(self, nom_fichier, dictionnaire):
        with open(nom_fichier, 'w') as f:
            f.write(str(dictionnaire))


class Date():
    def __init__(self):
        self.jour = int(input("enter le jour:"))
        self.mois = int(input("enter le mois:"))
        self.annee = int(input("enter le annee:"))
    def printDate(self):
        print(f"{self.jour}/{self.mois}/{self.annee}")    


    def affichage_date(self):
        print(f"{self.jour}/{self.mois}/{self.annee}")


class OffreAller(Voyage):
    def _init_(self, ref_offre, ville_depart, ville_arrivee, date, prix):
        super()._init_(ref_offre)
        self.date = Date(*date)
        self.prix = float(input("Prix : "))

    def affichage_offre_aller(self):
        print(f"{self.date.affichage_date()} - {self.prix}")

    def info_offre_aller_dico(self):
        dico2 = {"date": self.date.affichage_date(), "prix": self.prix}
        return str(dico2)


class AllerRetour(Voyage):
    def _init_(self, ref_offre, date_depart, date_arrivee):
        super()._init_(ref_offre)
        self.date_depart = Date(*date_depart)
        self.date_arrivee = Date(*date_arrivee)

    def afficher_aller_retour(self):
        print(f"{self.date_depart.affichage_date()} - {self.date_arrivee.affichage_date()}")

    def info_aller_retour_dico(self):
        dico3 = {
            "date_depart": self.date_depart.affichage_date(),
            "date_arrivee": self.date_arrivee.affichage_date()
        }
        return str(dico3)


class Hebergement(Voyage):
    def _init_(self, ref_offre, date_debut, nbr_nuit, type_hebergement, prix_par_nuit):
        super()._init_(ref_offre)
        self.date_debut = Date(*date_debut)
        self.nbr_nuit = int(nbr_nuit)
        self.type_hebergement = type_hebergement
        self.prix_par_nuit = prix_par_nuit

    def affichage_hebergement(self):
        print(f"{self.date_debut.affichage_date()}, {self.nbr_nuit} nuits, {self.type_hebergement}, {self.prix_par_nuit}")

    def info_hebergement_dico(self):
        dico4 = {'Date_debut': self.date_debut.affichage_date(), 'Nbr_nuit': self.nbr_nuit, 'Type': self.type_hebergement, 'Prix_par_nuit': self.prix_par_nuit}
        return str(dico4)


class FormuleComplete(Voyage):
    def _init_(self, ref_offre, date, prix, date_depart, date_arrivee, type_formule):
        super()._init_(ref_offre)
        self.offre_aller = OffreAller(ref_offre, "", "", date, prix)
        self.aller_retour = AllerRetour(ref_offre, date_depart, date_arrivee)
        self.type_formule = type_formule

    def definir_type_periode(self):
        while self.type_formule not in ["weekend", "Semaine"]:
            self.type_formule = input("Saisissez votre type de formule (weekend, Semaine) : ")

    def affichage_formule_complete(self):
        print(f"Type de formule : {self.type_formule}")

    def info_formule_complete_dico(self):
        dico5 = {"Type de formule": self.type_formule}
        return str(dico5)


class Reservation(Voyage):
    def _init_(self):
        self.ref_reservation = input("Référence de la réservation : ")
        self.type_offre = input("Type d'offre : ")
        self.date_depart = Date(input("Date de départ (jour mois annee) : ").split())
        self.date_retour = Date(input("Date de retour (jour mois annee) : ").split())
        self.genre = input("Genre : ")
        self.nom = input("Nom : ")
        self.prenom = input("Prénom : ")
        self.pays = input("Pays : ")
        self.num_passport = input("Numéro de passeport : ")
        self.etat_reservation = input("État de la réservation : ")
        self.total_a_payer = 0
        self.prix_transport = float(input("Prix du transport : "))
        self.prix_hebergement = int(input("Prix de l'hébergement : "))

    def definir_etat_reservation(self):
        while self.etat_reservation not in ["en cours", "annulée", "confirmée"]:
            self.etat_reservation = input("L'état doit être (en cours, annulée, confirmée) : ")

    def calculer_total_a_payer(self):
        self.total_a_payer = self.prix_transport + self.prix_hebergement
        return self.total_a_payer

    def affichage_reservation(self):
        print(f"{self.ref_reservation}, {self.type_offre}, {self.date_depart.affichage_date()}, {self.date_retour.affichage_date()}, {self.genre}, {self.nom}, {self.prenom}, {self.pays}, {self.num_passport}, {self.etat_reservation}, {self.total_a_payer}")

    def info_reservation_dico(self):
        dico6 = {
            "Ref_reservation": self.ref_reservation,
            "Type_offre": self.type_offre,
            "Date_depart": self.date_depart.affichage_date(),
            "Date_retour": self.date_retour.affichage_date(),
            "Genre": self.genre,
            "Nom": self.nom,
            "Prenom": self.prenom,
            "Nationalite": self.pays,
            "Passport": self.num_passport,
            "Etat_reservation": self.etat_reservation,
            "Total_a_payer": self.total_a_payer
        }
        return str(dico6)


def declaration_type_offre():
    type_offre = input("Veuillez entrer le type d'offre : ")
    if type_offre == "Aller Simple":
        return OffreAller("", "", "", [], 0)
    elif type_offre == "Aller Retour":
        return AllerRetour("", [], [])
    elif type_offre == "Formule Complete":
        return FormuleComplete("", [], 0, [], [], "")
    else:
        type_offre = input("Votre choix doit être parmi (Aller Simple, Aller Retour, Formule Complete) : ")
        return type_offre


def changer_date(date_actuelle, nouvelle_date):
    nouvelle_date = input("Veuillez entrer la nouvelle date : ")
    date_actuelle = Date(nouvelle_date)
    return date_actuelle


def bloquer_reservation(reponse):
    if reponse == "Oui":
        print('Votre réservation est bloquée.')
    elif reponse == "Non":
        print("Votre réservation n'est pas bloquée.")
    else:
        reponse = input("Votre choix doit être Oui ou Non : ")


def afficher_selon_type(type_offre):
    if type_offre == "Aller Simple":
        return OffreAller()
    elif type_offre == "Aller Retour":
        return AllerRetour()
    elif type_offre == "Formule Complete":
        return FormuleComplete()


def afficher_selon_date(date_recherche):
    if date_recherche == Date():
        return OffreAller()
    elif date_recherche == Date():
        return AllerRetour()
    else:
        return FormuleComplete()


def faire_reservation():
    return Reservation()


def confirmer():
    print("Votre offre est confirmée.")


def annuler():
    print("Votre offre est annulée.")


def menu():
    print("Menu :")
    print("1. Déclarer une offre.")
    print("2. Changer la date.")
    print("3. Bloquer l'offre.")
    print("4. Afficher selon le type.")
    print("5. Afficher selon une période.")
    print("6. Faire une réservation.")
    print("7. Confirmer.")
    print("8. Annuler.")
    print("9. Quitter.")



def menu_choix():
    date_entre = Date()
    while True:
        choix = input("Faites votre choix : ")
        if choix == '1':
            declaration_type_offre()
        elif choix == '2':
            changer_date()
        elif choix == '3':
            reponse = input("Voulez-vous bloquer l'offre ? (Oui/Non) : ")
            bloquer_reservation(reponse)
        elif choix == '4':
            afficher_selon_type()
        elif choix == '5':
            afficher_selon_date()
        elif choix == '6':
            faire_reservation()
        elif choix == '7':
            confirmer()
        elif choix == '8':
            annuler()
        elif choix == '9':
            break

if __name__ == "_main_":
    menu_choix()