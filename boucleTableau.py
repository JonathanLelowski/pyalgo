"""
@name boucle_tableau.py
@
Tableau de valeurs et Boucle
"""

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
        if  monTableau[indice] < valeurMinimale :
                valeurMinimale = monTableau[indice]
print("La valeur minimale est :", valeurMinimale)


#Déterminer la valeur la plus grande
valeurMaximale = monTableau[0]
for val in monTableau[1:]:
        if  monTableau[indice] > valeurMaximale :
                valeurMaximale = monTableau[indice]
print("La valeur max est :", valeurMaximale)

#Déterminer la valeur la plus petite (fonction min)
valeurMin = min(monTableau)
print("La valeur min est :", valeurMin)

#Déterminer la valeur la plus grande (fonction max)
valeurMax = max(monTableau)
print("La valeur max est :", valeurMax)