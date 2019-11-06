#SHIFUMI:
#-------


name=input("Bonjour, pour commencer la partie veuillez entrer votre nom: ")
scoreUser=0
scoreComp=0

import random
liste = [ 1, 2, 3]






while scoreUser or scoreComp != 3:
    print(name,",tapez:\n 1 pour jouer Pierre,\n 2 pour jouer Ciseaux,\n 3 pour jouer Feuille")  
    user=int(input("Choisissez!"))
    comp= random.choice(liste)

    if user==3 and comp==1:
       print("La feuille bat la pierre!")
    if user==2 and comp==3:
       print("Les Ciseaux battent la Feuille!")
    if user==1 and comp==2:
       print("La Pierre bat les ciseaux")
    if user==comp:
       print("DRAW!")
    

    
    


