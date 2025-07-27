
"""

🧩 3. Somme des entiers jusqu'à N
Écris une fonction qui calcule la somme de tous les entiers
de 1 jusqu'à `N` inclus.

Exemple :
Entrée : 5
Sortie : 15   (1 + 2 + 3 + 4 + 5)

---
"""
import math

def somme_entiers(entier):
    results = []
    for i  in range(0, entier):
        i += 1
        results.append(i)
    return sum(results)

print(somme_entiers(5))

# Autre alternative 1 (Pythonique) :
def somme_entiers(n):
    return sum(range(1, n + 1))

#! Autre alternative 2 (Math) : (suggerer par chatgpt)
def somme_entiers(n):
    return n * (n + 1) // 2
