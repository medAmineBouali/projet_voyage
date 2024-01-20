class Date:
    def _init_(self):
        self.jour = 0
        self.mois = 0
        self.anne = 0

    def saisir_Date(self):
        while True:
            print("Veuillez saisir la date du contrat:\n")
            self.jour = int(input("Veuillez entrer le jour du contrat\n"))
            if self.jour > 31 or self.jour <= 0:
                print("Répétez à nouveau et veuillez entrer le jour du contrat correctement !!!\n")
                continue

            self.mois = int(input("Veuillez saisir le mois du contrat\n"))
            if self.mois > 12 or self.mois <= 0:
                print("Répétez à nouveau et veuillez entrer le mois du contrat correctement !!!\n")
                continue

            self.anne = int(input("Veuillez saisir l'année du contrat\n"))
            if len(str(self.anne)) != 4:
                print("Répétez à nouveau et veuillez entrer l'année du contrat correctement!!!\n")
                continue

            break

        E = f"{self.jour}/{self.mois}/{self.anne}"
        print("La date du contrat est :", E)
        return E
    #def UPDATE(self):
       # print("vous vouler mettre a jour votre date")
laila=Date()
laila.saisir_Date()
        

class Contrat:
    def _init_(self):
        self.Ref_du_Contrat = 0
        self.Salutation_Assure = ""
        self.Nom_Assure = ""
        self.Prenom_Assure = ""
        self.CIN_Assure = 0
        self.date = Date()
        self.Duree_Validation = 0
        

    def saisir_infos_contrat(self):
      while True:
       try:   
        self.Ref_du_Contrat = int(input("Veuillez saisir la référence de votre contrat\n"))
        self.Nom_Assure = str(input("Veuillez saisir votre nom\n"))
        self.Prenom_Assure = str(input("Veuillez saisir votre prénom\n"))
        self.CIN_Assure = int(input("Veuillez saisir votre numéro de la carte nationale\n"))
        C=self.date.saisir_Date()
        print(C)
        self.Duree_Validation = int(input("Veuillez saisir votre durée de validation\n"))
        B = f"{self.Ref_du_Contrat} {self.Nom_Assure} {self.Prenom_Assure} {self.CIN_Assure} {str(self.date)} {self.Duree_Validation}"  
       except ValueError:
            print("Erreur de saisie. Veuillez entrer des valeurs correctes.")
            continue  # Redémarre la boucle pour une nouvelle saisie en cas d'erreur
       else:
            break  # Sort de la boucle si toutes les saisies sont correctes
            return B
    def affichage_saisie_Contrat(self):
        B=self.saisir_infos_contrat()
        print("les informations contrat a ne pa partager\n")
        print(B)
    def mise_a_jour_contrat(self):
        print("ces instructions pour mettre a jour votre date contrat\n")
        B=self.date.saisir_Date()
        print("la date apres la mise a jour\n")
        print(B) 
    def bloquer_contrat(self):
        print("vous  etes ici pour bloquer votre contrat\n")
        self.etat_contrat="bloque"
        print("votre contrat est bloqué")
    def debloquer_contrat(self):
        print("vous etes ici pour debloquer votre contrat\n")
        self.etat_actif="actif"
        print("votre contrat est débloqué")
    def date_fin_contrat(self):
        jour_fin = self.date.jour
        mois_fin = self.date.mois + self.Duree_Validation
        annee_fin = self.date.anne
        print("Votre contrat expire le :\n", f"{jour_fin}/{mois_fin}/{annee_fin}")    
#laila= Contrat()
#laila.saisir_infos_contrat()
#laila.date_fin_contrat()
      
        

        
        
class ContratAssuranceHabitation(Contrat):
    def _init_(self):
        super()._init_()
        self.Adresse_habitation = ""
        self.code_postal_habitation = 0
        self.ville_habitation = ""
        self.pays_habitation = ""
        self.type_habitation = ""
        self.tarif_mensuel_contrat = 0

    def saisir_infos_hebergement(self):
      while True:
       try:   
        self.saisir_infos_contrat()
        self.Adresse_habitation = str(input("Veuillez saisir votre adresse d'hébergement\n"))
        self.code_postal_habitation = int(input("Veuillez entrer le code postal\n"))
        self.pays_habitation = str(input("Veuillez saisir votre pays d'hébergement"))
        self.ville_habitation = str(input("Veuillez saisir votre ville\n "))
        L = ["Studio", "T1", "T2", "T3", "T4", "T5", "Pavillon", "Maison", " Villa"]
        while True:
            self.type_habitation = str(input("Veuillez saisir le type soit: Studio, T1, T2, T3, T4, T5, Pavillon, Maison, Villa\n"))
            if self.type_habitation in L:
                break
            else:
                print("Veuillez saisir à nouveau")
        self.tarif_mensuel_contrat = int(input("Veuillez saisir votre tarif mensuel de la contrat\n"))
        A=f"{self.Adresse_habitation}{self.code_postal_habitation}{self.pays_habitation}{self.ville_habitation}{self.tarif_mensuel_contrat}"
       except ValueError:
            print("Erreur de saisie. Veuillez entrer des valeurs correctes.")
            continue  # Redémarre la boucle pour une nouvelle saisie en cas d'erreur
       else:
            break  # Sort de la boucle si toutes les saisies sont correctes
            return A
    def affichage_inofs_contrat_hebergement(self):
        print("les informations contrat hebergement  sont:")
        B=self.saisir_infos_hebergement()
        print(B)#on veut mettre a jour le tarif mensuel du contrat
    def mise_a_jour_trf(self) :
       print("ces instructions pour mettre a jour le prix du tarid mensuel \n")
       self.tarif_mensuel_contrat=0 
       while(True):
        self.tarif_mensuel_contrat = int(input("Veuillez saisir votre tarif mensuel de la contrat\n"))   
        if(self.tarif_mensuel_contrat!=0):
            break
        else:
            print("vous aver tromper!!!")
        return  self.tarif_mensuel_contrat