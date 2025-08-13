"""
Exercice 5:

Écrire un programme en Python pour calculer la factorielle d’un nombre entier saisi par l’utilisateur. (Remarque: le factoriel de 5, qui s’écrit 5! = 5 × 4 × 3 × 2 × 1).
"""

nombre = int(input("Entrer un nombre : "))

def factoriel_nombre(n):
    var = 1
    for i in range(2, n + 1):
        var *= i

    return var

print(f"{nombre}! = {factoriel_nombre(nombre)}")