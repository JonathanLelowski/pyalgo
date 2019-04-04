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

"""
compare function
@param firstVal First value to compare
@param secondVal Second value to compare
@param howTo Mode de comparaison souhaité
@return greater or lower value of two depends on howto params
"""

def compare(firstVal, secondVal, desc=True):
        if (desc):
                return getLowerOf(firstVal, secondVal)
        
        return getGreaterOf(firstVal, secondVal)

"""
min function
@param anArray The array from which I want to get the min value
@return theMin the min value of anArray
"""

def min(anArray):
        theMin = anArray[0]
        for value in anArray[1:]:
                theMin = compare(theMin, value, True)

        return theMin

"""
max function
@param anArray The array from which I want to get the max value
@return theMax the max value of anArray
"""

def max(anArray):
        theMax = anArray[0]
        for value in anArray[1:]:
                theMax = compare(theMax, value, False)

        return theMax

"""
average function
@param anArray Array from 
"""
def average(anArray):
        total = 0
        nbItems = 0
        for val in anArray:
                total = total + val
                nbItems = nbItems + 1
        return total/ nbItems

def fact(anArray):
        total = 1
        for val in anArray:
                total = total * val
        return total

#Déclaration du tableau de démonstration
monTableau = [15,3,25,12,7,-15]
monAutreTableau = [5, 48, 56, -5, -13, 24, 4, 11]
monTableauFact = [5, 2, 3]

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
        valeurMinimale = compare(valeurMinimale, val, True)
print("La valeur minimale est :", valeurMinimale)

#Déterminer la valeur la plus grande
valeurMaximale = monTableau[0]
for val in monTableau[1:]:
         valeurMaximale = compare(valeurMaximale, val, False)
print("La valeur maximale est :", valeurMaximale)

#Déterminer la valeur la plus petite (fonction min)
print("La valeur min est :", min(monTableau))

#Déterminer la valeur la plus grande (fonction max)
print("La valeur max est :", max(monTableau))

#Moyenne de monTableau
print("La moyenne de mon tableau est :", average(monTableau))

#Moyenne de monAutreTableau
print("La moyenne de mon autre tableau est :", average(monAutreTableau))

#Factorielle de monTableau
print("la factorielle de mon tableau est :", fact(monTableauFact))

#Fact
print(fact(monTableau))