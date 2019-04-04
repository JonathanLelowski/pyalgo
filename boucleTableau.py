"""
@name boucle_tableau.py
@
Tableau de valeurs et Boucle
"""

"""
getLowerOf function
return the lowest value of two params
"""
def getLowerOf(firstVal, secondVal):
        if firstVal < secondVal:
                return firstVal
        else:
                return secondVal

"""
getGreaterOf function
return the greater value of two params
"""
def getGreaterOf(firstVal, secondVal):
        if firstVal > secondVal:
                return firstVal
        else:
                return secondVal


#Déclaration du tableau de démonstration
monTableau = [15,3,25,12,7,-15]

#Simple poor loop
for indice, val in enumerate(monTableau):
        print(monTableau[indice] * 2)

#More complex loop with condition
for indice, val in enumerate(monTableau):
    if indice % 2 == 0:
        print("Les valeurs paires sont les suivantes :", monTableau[indice] * 2)

#Déterminer la valeur la plus petite
valeurMinimale = monTableau[0]
for val in monTableau[1:]:
        valeurMinimale = getLowerOf(valeurMinimale, val)
print("La valeur minimale est :", valeurMinimale)


#Déterminer la valeur la plus grande
valeurMaximale = monTableau[0]
for val in monTableau[1:]:
         valeurMaximale = getGreaterOf(valeurMaximale, val)
print("La valeur maximale est :", valeurMaximale)

#Déterminer la valeur la plus petite (fonction min)
valeurMin = min(monTableau)
print("La valeur min est :", valeurMin)

#Déterminer la valeur la plus grande (fonction max)
valeurMax = max(monTableau)
print("La valeur max est :", valeurMax)