def NbToStr(Numb):
   if Numb in range(10):
       return '0'+str(Numb)
   return str(Numb)
def saisireElement(inf,sup,message="",mot = "La valeur",phrase = ""):
    if phrase == "":
        phrase = f"{mot} doit ettre entre {inf} et {sup}"
    while inf <= sup:
        element = int(input(message))
        if element in range(inf,sup+1):
           return element
        print(f"{phrase}.\n")
class AbstClass:
    def _init_(self,Att1 = "de départ",Att2 = "du transport",Att3 = 'Date_Depart',Att4 = 'Prix'):
        self.Att1 = Att1
        self.Att2 = Att2
        self.Att3 = Att3
        self.Att4 = Att4
class Date:
    def _init_(self,jj=1,mm=1,AA=2023):
        self.jour = jj
        self.mois = mm
        self.annee = AA
    def SaisirDate(self,message=""):
        self.jour = saisireElement(1,31,"Entrer le jour "+message+" : ")
        self.mois = saisireElement(1,12,"Entrer le mois "+message+" : ")
        self.annee = int(input("Entrer l'année "+message+" : "))
    def DateToStr(self,Sep='/'):
        return NbToStr(self.jour)+Sep+NbToStr(self.mois)+Sep+NbToStr(self.annee)
    def affichDate(self,message="",Sep='/'):
        print("La date "+message+" est "+self.DateToStr(Sep))
 #---------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------      
class Offre_Voyage:
    #------------------------------------------------------------------------------------------------------
    def _init_(self,Ref = "",Depart = "",Arrive = "",Statu = "Active"):
        self.Ref_Offre = Ref
        self.Ville_Depart = Depart
        self.Ville_Arrive = Arrive
        self.Etat_Offre = Statu
    #------------------------------------------------------------------------------------------------------
    def Offre_To_Dic(self):
        Dic = self.__dict__
        for key in Dic.keys():
            if type(Dic[key])== Date:
                Dic[key] = Dic[key].DateToStr()
        return Dic
    #------------------------------------------------------------------------------------------------------
    def Sauvgarder_Offre(self):
          with open("Offre de voyage.txt", 'a') as file:
               file.write(str(self.Offre_To_Dic())+'\n')
    #------------------------------------------------------------------------------------------------------
    def Declare_Offre(self):
        print("veuillez les informations suivant: \n")
        self.Ref_Offre = input("Le Réference de l'offre du voyage : ")
        self.Ville_Depart = input("Ville de départ : ")
        self.Ville_Arrive = input("Ville d'arrivée : ")
        
    #------------------------------------------------------------------------------------------------------
    def AfficheOffre(self):
        print(self.Offre_To_Dic())
    #------------------------------------------------------------------------------------------------------
    def Bloquer_Offre(self):
        self.Etat_Offre = "Bloquée"
    #------------------------------------------------------------------------------------------------------
    def Mettre_A_JOURS(self,m=0):
        T = [AbstClass(),AbstClass("de début","par nuite",'Date_debut','Prix_nuit')]
        print("1: Changer le prix ",T[m%2].Att2," .\n")
        print("2: Changer la date ",T[m%2].Att1," .\n")
        if(m==2):
            print("3: Changer la date d'arrivée .\n")
            print("4: Changer la date de départ et d'arrivée .\n")
        print(3+2*(m//2),": Changer le prix ",T[m%2].Att2," et la date ",T[m%2].Att1," .\n")
        if(m==2):
            print("6: Changer la date d'arrivé et le prix de transport .\n")
            print("7: Changer Les deux dates et le prix de transport .\n")
        Dic = self.__dict__
        Dic1 = {}
        del Dic['Etat_Offre']
        Choix = saisireElement(1, 3+4*(m//2),"Entrer votre choix : ","","Votre choix n'est pas valable")
        Ch = ""
        if (Choix == 1 or Choix == 3+2*(m//2) or Choix >= 6):
            Dic[T[m%2].Att4] = float(input(f"Le nouveau prix {T[m%2].Att2} est : "))
            Ch = "nouveau "
        Dic1[T[m%2].Att4] = f"Le {Ch}prix {T[m%2].Att2} est :{Dic[T[m%2].Att4]}"
        Ch = ""
        if (Choix == 2 or Choix == 4 or Choix == 3+2*(m//2) or Choix == 7):
            Dic[T[m%2].Att3] = Date()
            Dic[T[m%2].Att3].SaisirDate(f"de le nouveau date {T[m%2].Att1}")
            print("Le nouveau date ",T[m%2].Att1," est : ",Dic[T[m%2].Att3].DateToStr())
            Ch = "nouveau "
        Dic1[T[m%2].Att3] = f"Le {Ch}date {T[m%2].Att1} est :{Dic[T[m%2].Att3].DateToStr()}"
        Ch = ""    
        if (m == 2):
            if (Choix == 3 or Choix == 4 or Choix >= 6):
                Dic['Date_Arrive'] = Date()
                Dic['Date_Arrive'].SaisirDate("de le nouveau date d'arrivée")
                print("Le nouveau date d'arrivée est : ",Dic['Date_Arrive'].DateToStr())
                Ch = "nouveau "
            Dic1['Date_Arrive'] = f"Le {Ch}date d'arrivée est :{Dic['Date_Arrive'].DateToStr()}"  
        print("S'il vous plaît, assurez-vous que ces informations sont correctes avant de confirmer la mise à jour, et en cas d'erreur, veuillez annuler l'opération.\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")
        for k in Dic1.keys():
            print(f"{Dic1[k]}\n")
        print("-----------------------------------------------------------------------------------------------------------------------------------------------------\n")
        while True:
            choix1 = input("Vous voulez confimer cette modification?(Oui/Non):")
            if choix1.upper() == 'OUI':
                if m%2 == 0:
                    self.Date_Depart = Dic['Date_Depart']
                    self.Prix = Dic['Prix']
                    if(m == 2):
                        self.Date_Arrive = Dic['Date_Arrive']
                else:
                    self.Date_debut = Dic['Date_debut']
                    self.Prix_nuit = Dic['Prix_nuit']
                break
            elif choix1.upper() == 'NON':
                break
        
#---------------------------------------------------------------------------------------------------------- 
#----------------------------------------------------------------------------------------------------------             
class Transport_Aller_Simple(Offre_Voyage):
    def _init_(self,Ref = "",Depart = "",Arrive = "",Statu = "Active", Date = Date(),Prix = 0.00):
        super()._init_(Ref,Depart,Arrive,Statu)
        self.Date_Depart = Date
        self.Prix = Prix
    def Declare_Offre(self):
        self.Declare_Offre()
        self.Date_Depart.SaisirDate("de la date de départ")
        self.Date_Depart.affichDate("de la date de départ")
    def Mettre_A_JOUR(self):
        self.Mettre_A_JOURS(0)
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class Hebergement(Offre_Voyage):
    def _init_(self,Ref = "",Depart = "",Arrive = "",Statu = "Active",Date_debut = Date(),Nb_Nuite = 0,Type = "déjeuner",Prix_nuit =0.00):
        super()._init_(Ref,Depart,Arrive,Statu)
        assert Type in ["déjeuner", "demi-pension", "pension","complète"], f"{Type} non valable"
        self.Date_debut = Date_debut
        self.Nombre_Nuite = Nb_Nuite
        self.Type_Heb = Type
        self.Prix_nuit = Prix_nuit
    def Declare_Offre(self):
        self.Declare_Offre()
        self.Date_debut.SaisirDate("de la date de début")
        self.Date_debut.affichDate("de la date de début")
        self.Type_Heb = input("Entrer le type de l'hybergement : ")
        self.Prix_nuit = float(input("Entrer le prix par nuit de l'hybergement : "))
    def Mettre_A_JOUR(self):
        self.Mettre_A_JOURS(1)
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------    
class Transport_Aller_Retour(Transport_Aller_Simple):
    def _init_(self,Ref="",Depart = "",Arrive = "",Statu = "Active",Date_Depart = Date(),Prix = 0.00,Date_Arrive=Date()):
        super()._init_(Ref,Depart,Arrive,Statu,Date_Depart,Prix)
        self.Date_Arrive = Date_Arrive
    def Declare_Offre(self):
        self.Declare_Offre()
        self.Date_Arrive.SaisirDate("de la date de d'arrivée")
        self.Date_Arrive.affichDate("de la date de d'arrivée")
    def Mettre_A_JOUR(self):
        self.Mettre_A_JOURS(2)
    
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------  
class Formule_complete(Transport_Aller_Retour, Hebergement):
    def _init_(self, Ref="", Depart="", Arrive="", Date_Depart=Date(), Prix=0.00, Date_Arrive=Date(), Date_debut=Date(), Nb_Nuite=0, Type="déjeuner", Prix_nuit=0.00, type1="Week-End"):
        Transport_Aller_Retour._init_(Ref, Depart, Arrive, Date_Depart, Prix, Date_Arrive)
        Hebergement._init_(Ref, Depart, Arrive, Date, Date_debut, Nb_Nuite, Type, Prix_nuit)
        assert type1 in ["Week-End","Semaine"],f"{type1} non valable"
        self.Type = type1
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------
class Reservation:
    def _init_(self,Ref_Reserv="",Type_Offre="",Ref_Offre="",Date_Depart=Date(),Date_Retour=Date(),Genre="",Nom="",Prenom="",Nat="",Num_Pass="",Etat_Reserv="en cours"):
        self.Ref_Reservation = Ref_Reserv
        self.Type_Offre = Type_Offre
        self.Ref_Offre = Ref_Offre
        self.Date_Depart = Date_Depart
        self.Date_Retour = Date_Retour
        self.Genre = Genre
        self.Nom = Nom
        self.Prenom = Prenom
        self.Pays_Origine = Nat
        self.Num_Passport = Num_Pass
        assert Etat_Reserv in ["en cours", "annulée","confirmée"],f"{Etat_Reserv} non valable"
        self.Etat_Reservation = Etat_Reserv
    def Calcule_Total_A_Payer(self,Prix_Transport,Prix_Hebergement):
        self.Total_A_Payer = 0.90*(Prix_Transport+Prix_Hebergement)
    def Reservation_To_Dic(self):
        Dic = self.__dict__
        for key in Dic.keys():
            if type(Dic[key])== Date:
                Dic[key] = Dic[key].DateToStr()
        return Dic
    def Sauvgarder_Reservation(self):
          with open("Reservation.txt", 'a') as file:
               file.write(str(self.Reservation_To_Dic())+'\n')
#----------------------------------------------------------------------------------------------------------
#----------------------------------------------------------------------------------------------------------        
       
T = Transport_Aller_Retour("A125","Tanger","Fes",Date(2,5,2024),13700.33,Date(9,6,2024))
TE = Transport_Aller_Retour("A125","Tanger","Fes",Date(2,15,2024),13700.33,Date(9,16,2024))
T.Mettre_A_JOUR()