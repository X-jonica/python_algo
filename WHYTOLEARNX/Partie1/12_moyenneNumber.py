"""
Exercice 12:

Écrire un programme Python qui calcule la moyenne de trois nombres saisis par l'utilisateur.
"""
nombres = []

for i in range(1, 4):
    n = float(input(f"Entre le nombre °{i}: "))
    nombres.append(n)

def calcule_moyenne_nombre(tab):
    return sum(tab) / len(tab)

print(f"moyenne de {nombres} = {calcule_moyenne_nombre(nombres)}")