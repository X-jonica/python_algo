"""
Exercice 3:

Ecrivez un programme Python qui accepte un nombre et vérifie s’il est pair ou non. Affiche 1 si le nombre est pair ou 0 s’il est impair.
"""
nbr = int(input("Entrer un nombre : "))

def isEven(number):
    if (number % 2 == 0):
        return 1
    return 0

print(isEven(nbr))