
"""

🧩 8. Remplacer les voyelles par '*'
Remplace toutes les voyelles dans une chaîne par des astérisques '*'.

Exemple :
Entrée : ordinateur
Sortie : *rd*n**t*r

---
"""
def remplacer_voyelles(chaine):
    voyelles = ["a", "e", "y", "u", "i", "o"]
    result = chaine
    for i in chaine:
        if (i in voyelles):
            result = result.replace(i, "*")
            
    return result

print(remplacer_voyelles("ordinateur"))
