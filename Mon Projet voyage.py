from fontions import *
from classes import *


list_offres = {} #form {ref:instant}
reservations = {}
menu_principale = ["Afficher les offres.","Ajouter des offres.","Modifier un offre.","Faire une Reservation.","Afficher les statistiques.","Quitter"]
menu_affichage = ["Afficher tous les offres.","Afficher un type specifique.","Afficher par periode."]
menu_ajouter = ["Ajouter un voyage aller simple.","Ajouter un voyage aller et retour","ajouter un voyage complete","sauvgarde et retour"]

voyage = Voyage_complet()
while True:
    choix = menu(menu_principale)
    if choix == 1:
        choix = menu(menu_affichage)
        affichage_offres(choix,list_offres)
    elif choix == 2:
        while True:
            choix = menu(menu_ajouter)
            if choix == 1:
                voyage = Voyage_simple()
                voyage.set_voyage()
                voyage.sauvgarder(list_offres)
            elif choix == 2:
                voyage = Voyage_aller_retour()
                voyage.set_voyage()
                voyage.sauvgarder(list_offres)
            elif choix == 3:
                voyage = Voyage_complet()
                voyage.set_voyage()
                voyage.sauvgarder(list_offres)
            elif choix == 4:
                sauvgarder_modification(list_offres,"Offre_de_voyage.txt")
                break
    
    elif choix == 3:
        modifier_offre(list_offres)
    elif choix == 4:
        offre = choisir_offre(list_offres)
        reservation = Reservation()
        reservation.set_reservation(offre)
        reservation.confirmation()
        reservation.sauvgarder(reservation)
        sauvgarder_modification(reservation,"Offre_de_voyage.txt")
    elif choix == 5:
        print("en cours de maintenance....")
    elif choix == 6:
        print("bon Voyage!")
        break

"""
voyage1 = Voyage_aller_retour()
voyage1.set_voyage()
voyage2 = Voyage_simple()
voyage2.set_voyage()

voyage1.Sauvgarder_Offre()
voyage2.Sauvgarder_Offre()
"""