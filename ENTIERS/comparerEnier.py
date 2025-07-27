"""
🧠 Défis de logique - Niveau facile (style CodinGame)
Langage : Python

---

🧩 1. Plus grande des deux valeurs
Écris une fonction qui prend en entrée deux entiers `a` et `b`,
et retourne le plus grand des deux.

Exemple :
Entrée : 5 9
Sortie : 9

---
"""
def comparer_deux_nombre(entier1, entier2):
    if(entier1 > entier2):
        return entier1
    else:
        return entier2
    
print(comparer_deux_nombre(5, 9))