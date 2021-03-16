
import networkx as nx
import databus as data


G = nx.Graph()
"""
Création des arcs entre les différents noeuds.
"""

def initialisation():
    ligne1 = data.Nom_arret.split(" N ")
    ligne2 = data.Nom_arret2.split(" N ")
     
    for i in range(len(ligne1)-1):
        G.add_edge(ligne1[i], ligne1[i+1], nbarc = 1)
     
    for i in range(len(ligne2)-1):
        G.add_edge(ligne2[i], ligne2[i+1], nbarc = 1)

"""
Conversion horraire en Heure:Minute en seconde
"""

def conversion1(horaires):
    horaire=horaires.split(":")
    heure = int(horaire[0])
    heure = heure * 60
    minute = int(horaire[1])
    return heure + minute
        
"""
Conversion inverse de seconde en Heure:Minute.
"""
    
def conversion2(horaire):
    heureprochainbus = []
    heure = horaire // 60
    minute = horaire %60
    heureprochainbus.append(heure)
    heureprochainbus.append(minute)
    return heureprochainbus
    
"""
Fonction pour trouver l'horraire du prochain bus en fonction de l'arret la ligne et la direction
"""

def trouverHoraire(tictac):
    liste=[]
    ligne = input("Sur quelle ligne êtes vous ? \n")
    direction = input("Dans quel sens voulez vous aller? \n")
    jour= input("Etes vous en vacances/week-end (oui ou non) ? \n")
    heure = input("Quelle heure est-il? \n")
    hor=conversion1(heure)
    date = [""]
    if ligne == "1" and direction == "PARC_DES_GLAISINS" and jour == "non":
        date = data.Date_normal_alleX[0][tictac]
    if ligne == "1" and direction == "LYCEE_DE_POISY" and jour == "non":   
        date = data.Date_normal_retourX[0][tictac]
    if ligne == "1" and direction == "PARC_DES_GLAISINS" and jour=="oui":     
        date = data.Date_special_alleX[0][tictac]
    if ligne == "1" and direction == "LYCEE_DE_POISY" and jour=="oui":   
        date = data.Date_special_retourX[0][tictac]
    if ligne == "2" and direction == "CAMPUS" and jour == "non":
        date =  data.Date_normal_alleX[1][tictac]
    if ligne == "2" and direction == "PISCINE-PATINOIRE" and jour == "non":
        date = data.Date_normal_retourX[1][tictac]
    if ligne == "2" and direction == "CAMPUS" and jour=="oui":
        date = data.Date_special_alleX[1][tictac]
    if ligne == "2" and direction == "PISCINE-PATINOIRE" and jour=="oui":
        date = data.Date_special_retourX[1][tictac]
        
    if date == [""]:
        print("Il y a une erreur dans votre itinéraire \n")
        return 0          
    for y in date:
         if y == "-":
                liste.append(".")
         else:
             liste.append(conversion1(y))         
    for z in liste:
        if type(z) != str:
            if (z - hor > 0):
                return conversion2(z)           
       
#Donne le plus court chemin pour aller de l'arret de depart a celui d'arrivé.
def lepluscourt(arret,destination):
    return nx.shortest_path(G,arret,destination)


if __name__ == "__main__":    
    initialisation()
    print(G.nodes)
    arret=input("Quel est votre arrêt ? \n")
    destination=input("Quel est votre destination ? \n")
    h=trouverHoraire(arret)
    short=lepluscourt(arret,destination)
    print("\n")
    print("\n")
    print("Votre prochain bus passera à :", h[0], "h", h[1], "\n")
    print("Voici le chemin le plus court pour y arriver :\n", short)
    
    
    
  

    
