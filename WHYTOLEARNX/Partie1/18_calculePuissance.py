"""
Exercice 18:

Écrire un programme en Python qui prend deux entiers de l'utilisateur (un nombre de base et un exposant) et calcule la puissance.
"""
import math

nombre = int(input("Entrer un nombre : "))
puissance = int(input("Entrer un nombre , ceci a etre la puissance du precedent nombre : "))

def calcule_puissance(n, p):
    return n ** p

print(f"{nombre}^{puissance} = {calcule_puissance(nombre, puissance)}")