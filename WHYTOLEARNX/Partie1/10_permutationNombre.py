"""
Exercice 10:

Écrire un programme Python pour échanger deux nombres sans utiliser une troisième variable.Exercice 10:
Écrire un programme Python pour échanger deux nombres sans utiliser une troisième variable.
"""

nombre1 = 5
nombre2 = 2

print(f"avant permutation n1 = {nombre1}, n2 = {nombre2}")

nombre1 = nombre1 + nombre2
nombre2 = nombre1 - nombre2
nombre1 = nombre1 - nombre2

print(f"avant permutation n1 = {nombre1}, n2 = {nombre2}")
