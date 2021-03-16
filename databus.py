

Ligne1 = '1_Poisy-ParcDesGlaisins.txt'
Ligne2 = '2_Piscine-Patinoire_Campus.txt'


try:
    with open(Ligne1, 'r') as a:
        l1 = a.read()
    with open(Ligne2, 'r') as b:
        l2 = b.read()

except OSError:
    # Message si il n'y a pas les fichier txt.
    print("Le fichier n'est pas la !")
    



def datedico(dates):
    dic = {}
    separ = dates.split("\n")
    for stop_dates in separ:
        tmp = stop_dates.split(" ")
        dic[tmp[0]] = tmp[1:]
    return dic


#Premiere separation des fichiers txt, Ligne 1.
  
Coupure = l1.split("\n\n")
Nom_arret = Coupure[0]
Date_normal_alle = datedico(Coupure[1])
Date_normal_retour = datedico(Coupure[2])
Nom_arret_vac = Coupure[3]
Date_special_alle = datedico(Coupure[4])
Date_special_retour = datedico(Coupure[5])


#Premiere separation des fichiers txt, Ligne 2

  
Coupure = l2.split("\n\n")
Nom_arret2 = Coupure[0]
Date_normal_alle2 = datedico(Coupure[1])
Date_normal_retour2 = datedico(Coupure[2])
Nom_arret_vac2 = Coupure[3]
Date_special_alle2 = datedico(Coupure[4])
Date_special_retour2 = datedico(Coupure[5])

#Creation de liste de dictionnaire pour une utilisation dans mon Main.
Date_normal_alleX = [Date_normal_alle , Date_normal_alle2]
Date_normal_retourX = [Date_normal_retour , Date_normal_retour2]
Date_special_alleX = [Date_special_alle, Date_special_alle2]
Date_special_retourX = [Date_special_retour, Date_special_retour2]
