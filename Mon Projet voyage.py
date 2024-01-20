from fontions import *
from classes import *


list_offres = {} #form {ref:instant}
reservations = {}
menu_principale = ["Afficher les offres.","Ajouter des offres.","Modifier un offre.","Faire une Reservation.","Afficher les statistiques.","Quitter"]
menu_affichage = ["Afficher tous les offres.","Afficher un type specifique.","Afficher par periode."]
menu_ajouter = ["Ajouter un voyage aller simple.","Ajouter un voyage aller et retour","ajouter un voyage complete","sauvgarde et retour"]
menu_stats = ["S1.a Nbre d'offres par type et Nbre d'offres total.","S1.b Même question pour une période précise.","S2.a Nbre de réservations annulé, confirmé ou Global","S2.b Nbre de réservations confirmé par période, par destination, par client ou par nationalité","S3.a Chiffre d'affaires global : montant des gains.","S3.b Chiffre d'affaires global par période, par type, par destination et/ou par nationalité.","Retour au menu principal"]
voyage = Voyage_complet()
while True:
    #mohamed amine boauli
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
        #Hamza Laouar
        offre = choisir_offre(list_offres)
        reservation = Reservation()
        reservation.set_reservation(offre)
        reservation.confirmation()
        reservation.sauvgarder(reservations)
        sauvgarder_modification(reservations,"Offre_de_voyage.txt")
    elif choix == 5:
            #mohamed amine boauli
        choix_stats = menu(menu_stats)

        if choix_stats == 1:
            stat_offer_count, total_offers = stat_offer_par_type(list_offres)
            print("Number of offers by type:")
            for offer_type, count in stat_offer_count.items():
                print(f"{offer_type}: {count} offers")
            print(f"Total number of offers: {total_offers}")

        elif choix_stats == 2:
            start_date = Date()
            start_date.set_date("de début de période")
            end_date = Date()
            end_date.set_date("de fin de période")

            stat_offer_count, total_offers = stat_offer_par_type_et_period(list_offres, start_date, end_date)
            print(f"Number of offers by type for the period {start_date.format_string()} to {end_date.format_string()}:")
            for offer_type, count in stat_offer_count.items():
                print(f"{offer_type}: {count} offers")
            print(f"Total number of offers: {total_offers}")

        elif choix_stats == 3:
            status_filter = input("Enter reservation status (confirmed, canceled, global): ")
            stat_reservations = stat_reservation_par_etat(reservations, status_filter)
            print(f"Number of reservations {status_filter.capitalize()}:")
            for status, count in stat_reservations.items():
                print(f"{status}: {count} reservations")

        elif choix_stats == 4:
            period_stat_choice = menu(["Par période", "Par destination", "Par client", "Par nationalité"])
            if period_stat_choice == 1:
                start_date = Date()
                start_date.set_date("de début de période")
                end_date = Date()
                end_date.set_date("de fin de période")

                stat_reservations = stat_reservation_confirme_par_filter(reservations, "confirmed", start_date, end_date)
                print(f"Number of confirmed reservations for the period {start_date.format_string()} to {end_date.format_string()}:")
                for period, count in reservations.items():
                    print(f"{period}: {count} reservations")
            elif period_stat_choice == 2:
                print("en cours de maintenance ...")
            elif period_stat_choice == 3:
                print("en cours de maintenance ...")

            elif period_stat_choice == 4:
                print("en cours de maintenance ...")
        elif choix_stats == 5:
            stat_revenue = stat_total_revenue(list_offres, reservations)
            print(f"Chiffre d'affaires global : montant des gains: {stat_revenue:.2f}$")

        elif choix_stats == 6:
            period_stat_choice = menu(["Par période", "Par type", "Par destination", "Par nationalité"])
            if period_stat_choice == 1:
                start_date = Date()
                start_date.set_date("de début de période")
                end_date = Date()
                end_date.set_date("de fin de période")

            elif period_stat_choice == 2:
                pass
            elif period_stat_choice == 3:
                pass
            elif period_stat_choice == 4:
                pass

        elif choix_stats == len(choix_stats):
            continue

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