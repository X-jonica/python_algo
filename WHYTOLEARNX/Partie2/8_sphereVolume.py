"""
Exercice 8:

Écrire un programme Python qui calcule le volume d'une sphère.

V = (4/3) * pi * r³

"""

import math

rayon = float(input("Entrer le rayon du cercle : "))

def calcule_volum(r):
    pi = 3.14
    volume = (4/3) * pi  * math.pow(r, 3)
    return volume

print(f"Le volume de la sphere est : {calcule_volum(rayon)}")