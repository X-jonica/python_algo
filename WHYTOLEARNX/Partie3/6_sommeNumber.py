"""
Exercice 6:

Ecrivez un programme en Python qui calcule la somme des nombres impairs compris entre 1 et un nombre entier N saisi par l’utilisateur. Exemple N=10 Somme=1+3+5+7+9=25
"""
n = int(input("Entrer un nombre: "))

def calcule_somme_nombre_impairs_n(n):
    nombre_impairs = []
    for i in range(0, n):
        if(i % 2 != 0):
            nombre_impairs.append(i)
    return sum(nombre_impairs)

print(f"La somme des nombres impairs est: {calcule_somme_nombre_impairs_n(n)}")