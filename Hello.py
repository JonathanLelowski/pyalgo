"""
Algorithme 0.0.1
Declare var
Store some arithmetics into the var
Display Result
Operands and Operators, functions

@version 0.0.2
Add two operands and replace compute method


"""

#Définir une fonction
def addition(operande1, operande2):
    if operande1 < 0:
        operande1 = operande1 * -1
        return operande1 + operande2

resultat = 0 # Définition de la variable
operande1 = -3
operande2 = 2
resultat = addition(5, 3) # Call addition function with 5 and 3 as params
print(addition(operande1,operande2))
print(resultat)

if resultat > 0 :
    print("Résultat positif")
else :
    print("Résultat négatif")

"""
Fin de l'algorithme
"""