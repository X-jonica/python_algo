
"""
🧩 5. Factorielle
Calcule la factorielle d’un entier N (N! = 1 × 2 × 3 × ... × N)

Exemple :
Entrée : 4
Sortie : 24

---
"""
def factoriel_nombre(entier):
    if entier == 0:
        return 1
    result = 1
    for i in range(1, entier + 1):
        result *= i

    return result

nombre = 4
print("{}! = {}".format(nombre, factoriel_nombre(nombre)))

#! Autre alternative : (suggerer par chatgpt)
import math
def factoriel_nombre(entier):
    return math.factorial(entier)
