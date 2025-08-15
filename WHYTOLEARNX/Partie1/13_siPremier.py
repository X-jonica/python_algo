"""
Exercice 13:

Écrire un programme en Python qui permet de savoir si le nombre saisi est Premier ou non. (Un nombre premier est un nombre uniquement divisible par 1 ou par lui-même).
"""
import math

nombre = int(input("entrer un nombre : "))

def si_premier(n):
    if (n == 1):
        return "n'est pas premier"
    if (n == 2):
        return "est premier"
    if (n % 2 == 0):
        return "n'est pas premier"

    # verifions seulement les nombres impaire
    for i in range(3, math.isqrt(n) + 1, 2):
        if (n % i == 0):
            return "n'est pas premier"

    return "est premier"

print(f"{nombre} {si_premier(nombre)} ")