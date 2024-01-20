def menu(listes_choix:list):
    
    while True:
        i = 1
        print("Veuillez choisir une operation:\n")
        for line in listes_choix:
            print(str(i)+")"+line+"\n")
            i += 1
        try:
            choix = int(input())
            assert choix in range(1,len(listes_choix) + 1),"choix invalide"
            break
        except Exception as e:
            print("Erreur:" , e)
    return choix

def validation_Date(jour:int,mois:int,annee:int) -> None:
    jour_dans_mois = {1: 31, 2: 28,3: 31,4: 30,5: 31,6: 30,7: 31,8: 31, 9: 30,10: 31,11: 30, 12: 31}
    if jour <= 0 or mois <= 0 or annee <= 0:
        raise ValueError("un ou plusieurs valeur sont tros petite")
    if annee % 4 == 0:
         jour_dans_mois[2] += 1
    if mois >= 13:
        raise ValueError("le mois entrer n'existe pas")
    if jour_dans_mois[mois] < jour:
        raise ValueError("le jours entrer n'existe pas")
    if len(str(annee)) != 4:
        raise ValueError("l'annee entre et invalide")

def saisirElement(inf:int, sup:int, message=""):
    while True:
        try:
            element = int(input(message))
            if element in range(inf, sup + 1):
                return element
            print(f"{element} doit être compris entre {inf} et {sup} ")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def NbToStr(Numb:int):
   if Numb in range(10):
       return '0'+str(Numb)
   return str(Numb)

def input_type_hebergement():
    l = ["dejeuner","demi-pension","pension complète"]
    while True:
        try:
            choix = int(input("entrer le type de pension parmi le suivant: \n1 pour un dejeuner\n2 de pour demi-pension\n3 pour pension complète:\n"))
            assert choix in range(1,4)
            break
        except Exception as e:
            print("Error: ",e)
    return l[choix - 1]

def input_type_duree():
    l = ["week-end","semaine"]
    while True:
        try:
            choix = int(input("choisisez le type de voyage: \n entrez 1 pour weekend ou 2 pour semaine:\n"))
            assert choix in range(1,3)
            break
        except Exception as e:
            print("Error: ",e)
    return l[choix - 1]

def sauvgarder_modification(list_offres:dict,nom_fichier):
    with open(nom_fichier, 'w') as file:
            file.truncate(0)
    for offre in list_offres.values():
        offre.sauvgarder_dans_fichier()

def modifier_offre(list_offres:dict):
    print("voila les refs des offres disponible:\n")
    for ref,offre in list_offres.items():
        print("--"+ref+"---"+offre.type_offre)
    while True:
        try:
            ref = str(input("entre le ref d'offre a modifier:\n"))
            assert ref in list_offres.keys(), f"le ref entre n'exist pas\n"
            break
        except Exception as e:
            print(e,"\n")
    list_offres[ref].Mettre_A_Jour()
    
def choisir_offre(list_offres:dict):
    print("voila les refs des offres disponible:\n")
    for ref,offre in list_offres.items():
        print("--"+ref+"---"+offre.type_offre)
    while True:
        try:
            ref = str(input("entre le ref d'offre a pour reserver:\n"))
            assert ref in list_offres.keys(), f"le ref entre n'exist pas\n"
            break
        except Exception as e:
            print(e,"\n")
    return list_offres[ref]

