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
    #Hamza Laouar
    while True:
        try:
            element = int(input(message))
            if element in range(inf, sup + 1):
                return element
            print(f"{element} doit être compris entre {inf} et {sup} ")
        except ValueError:
            print("Veuillez entrer un nombre entier.")

def NbToStr(Numb:int):
   #Hamza Laouar
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
    #Hamza Laouar
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

def stat_offer_par_type(offers):
    offer_count_by_type = {}

    for offer in offers.values():
        type_offre = offer.type_offre
        offer_count_by_type[type_offre] = offer_count_by_type.get(type_offre, 0) + 1

    total_offers = len(offers)

    return offer_count_by_type, total_offers

def stat_offer_par_type_et_period(offers, start_date, end_date):
    offer_count_by_type = {}
    total_offers = 0

    for offer in offers.values():
        if offer.Date_depart.is_between(start_date, end_date):
            type_offre = offer.type_offre
            offer_count_by_type[type_offre] = offer_count_by_type.get(type_offre, 0) + 1
            total_offers += 1

    return offer_count_by_type, total_offers

def stat_reservation_par_etat(reservations, status_filter=None):
    status_count = {}

    for reservation in reservations.values():
        if status_filter is None or reservation.Etat_Reservation.lower() == status_filter.lower():
            status_count[reservation.Etat_Reservation] = status_count.get(reservation.Etat_Reservation, 0) + 1

    return status_count

def stat_reservation_confirme_par_filter(reservations, filter_type, filter_value, start_date=None, end_date=None):
    confirmed_count = 0

    for reservation in reservations.values():
        if reservation.Etat_Reservation.lower() == 'confirmée':
            if (start_date is None or reservation.Date_depart >= start_date) and \
               (end_date is None or reservation.Date_depart <= end_date):
                if filter_type == 'period':
                    confirmed_count += 1
                elif filter_type == 'destination' and reservation.Ref_Offre == filter_value:
                    confirmed_count += 1
                elif filter_type == 'client' and reservation.Nom == filter_value:
                    confirmed_count += 1
                elif filter_type == 'nationality' and reservation.Nationalite == filter_value:
                    confirmed_count += 1

    return confirmed_count

def stat_total_revenue(reservations, offers):
    total_revenue = 0

    for reservation in reservations.values():
        if reservation.Etat_Reservation.lower() == 'confirmée':
            offer_ref = reservation.Ref_Offre
            total_revenue += offers[offer_ref].prix

    return total_revenue

def stat_revenue_by_filter(reservations, offers, filter_type, filter_value, start_date=None, end_date=None):
    revenue = 0

    for reservation in reservations.values():
        if reservation.Etat_Reservation.lower() == 'confirmée':
            if (start_date is None or reservation.Date_depart >= start_date) and \
               (end_date is None or reservation.Date_depart <= end_date):
                offer_ref = reservation.Ref_Offre
                if filter_type == 'period':
                    revenue += offers[offer_ref].prix
                elif filter_type == 'type' and offers[offer_ref].type_offre == filter_value:
                    revenue += offers[offer_ref].prix
                elif filter_type == 'destination' and offer_ref == filter_value:
                    revenue += offers[offer_ref].prix
                elif filter_type == 'nationality' and reservation.Nationalite == filter_value:
                    revenue += offers[offer_ref].prix

    return revenue
