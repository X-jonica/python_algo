"""
🧩 2. Compter les voyelles
Écris un programme qui lit une chaîne de caractères et affiche
le nombre de voyelles (a, e, i, o, u, y en minuscule).

Exemple :
Entrée : bonjour
Sortie : 3
---
"""
def compter_voyelles(chaine):
    voyelles = ["a","e","y","u","i","o"]
    result = 0
    list_chaine = list(chaine)
    for i in range(len(chaine)):
        if(list_chaine[i] in voyelles):
            result += 1
    return result

mots = "bonjour"
print(compter_voyelles(mots))