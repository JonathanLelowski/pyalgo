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
tableauLettreMin = ["a", "b"]
grandTableau = [tableauLettreMaj, tableauChiffre, tableauCaract, tableauLettreMin]

print(grandTableau[0])
print(grandTableau[1])
print(grandTableau[2])
print(grandTableau[3])

#Var 
nbCaract = 0
password = str() 
maj = str()
chiffre = str()
caract = str()

from random import *
nbCaract = int(uniform(8, 12))
#print("nombre de caractère :", nbCaract)

#Déterminer les caractères obligatoires du mdp
#Maj
indiceMaj = int(uniform(0, len(tableauLettreMaj)))
maj = tableauLettreMaj[indiceMaj]
print(maj)
#Chiffre
indiceChiffre = int(uniform(0, len(tableauChiffre)))
chiffre = tableauChiffre[indiceChiffre]
print(chiffre)
#Caract
indiceCaract = int(uniform(0, len(tableauCaract)))
caract = tableauCaract[indiceCaract]
print(caract)

#Déterminer les caractères restants du mdp
if len(password) < nbCaract-3:
    for i in range(nbCaract-3):
        whichType = int(uniform(0,4))
        print("tableau choisi :", whichType)
        indice = int(uniform(0,len(grandTableau[whichType])))
        #print(indice)
        val = grandTableau[whichType][indice]
        #print(val)
        password = password + val
    print("première partie du mdp :", password)

#Association password + chiffre + Lettre + Caract