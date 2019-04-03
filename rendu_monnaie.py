"""
@name rendu_monnaie.py
@author Aélion
@version 0.0.1
A poor coins cunter
Use // to get an integer division
Use % to get rest of int div
Use raw_input() function to get 
"""

#Prix démandé
prix = 3

#Argent donné par le client
argent = 50

somme = argent - prix

print("Vous avez donné :", argent, "euros")
print("Votre achat coûte :", prix, "euros")
billet100 = somme // 100
reste100 = somme % 100
billet50 = reste100 // 50
reste50 = reste100 % 50
billet20 = reste50 // 20
reste20 = reste50 % 20
billet10 = reste20 // 10
reste10 = reste20 % 10
billet5 = reste10 // 5
reste5 = reste10 % 5
piece2 = reste5 // 2
reste2 = reste5 % 2
piece1 = reste2 // 1
reste1 = reste2 % 1

#La machine vous rend
print("La caissière vous rend :", somme, "euros")
print (billet100, "x 100€")
print (billet50, "x 50€")
print (billet20, "x 20€")
print (billet5, "x 5€")
print (piece2, "x 2€")
print (piece1, "x 1€")