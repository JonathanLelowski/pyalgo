"""
Génération de mot de passe aléatoire
@Minimun 8 caratères, maximum 12
@Au moins 1 lettre en Maj
@Au moins 1 caractère de ponctuation
@AU moins 1 chiffre
"""
"""
Fonction : fonction (algo) RANDOM (x,y) retourne 1 nb aléatoire compris entre x, y
"""

#Tableaux
tableauLettreMaj = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
tableauChiffre = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
tableauCaract = ["*", ",", ";", "/", "+", "-", ")", "(", "[", "]"]
tableauLettreMin = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
grandTableau = [tableauLettreMaj, tableauChiffre, tableauCaract, tableauLettreMin]

#Vars
nbCaract = 0
passwordtr = str() 
maj = str()
chiffre = str()
caract = str()

from random import *
nbCaract = int(uniform(8, 12))
#print("nombre de caractère :", nbCaract)

#Déterminer le caractère obligatoire "Maj" du mdp
indiceMaj = int(uniform(0, len(tableauLettreMaj)))
maj = tableauLettreMaj[indiceMaj]
##print("La majuscule obligatoire :", maj)

#Déterminer le caractère obligatoire "Chiffre" du mdp
indiceChiffre = int(uniform(0, len(tableauChiffre)))
chiffre = tableauChiffre[indiceChiffre]
##print("Le chiffre obligatoire :", chiffre)

#Déterminer le caractère obligatoire "Caractère" du mdp
indiceCaract = int(uniform(0, len(tableauCaract)))
caract = tableauCaract[indiceCaract]
##print("Le caractère obligatoire :", caract)

#Déterminer les caractères restants du password tronqué "passwordtr"
if len(passwordtr) < nbCaract-3:
    for i in range(nbCaract-3):
        whichType = int(uniform(0,4))
        #print("tableau choisi :", whichType)
        indice = int(uniform(0,len(grandTableau[whichType])))
        #print(indice)
        val = grandTableau[whichType][indice]
        #print(val)
        passwordtr = passwordtr + val
    ##print("première partie du mdp :", passwordtr)

#Association password tronqué + chiffre + Lettre + Caract
passwordInt3 = passwordtr + maj + chiffre + caract
##print(passwordInt3)

#Mélange du password
import random
passwordFinal = "".join(random.sample(passwordInt3,len(passwordInt3)))
print("Voici votre mot de passe aléatoire :", passwordFinal)