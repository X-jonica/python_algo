"""
🧩 4. Inverse d’une chaîne
Écris un programme qui lit une chaîne et l'affiche en ordre inverse.

Exemple :
Entrée : Python
Sortie : nohtyP
---
"""
def inverser_chaine(chaine):
    return "".join(list(reversed(chaine)))

word = "Python"
print(inverser_chaine(word))

#! Autre alternative : # Autre alternative :
def inverser_chaine(chaine):
    return chaine[::-1]
