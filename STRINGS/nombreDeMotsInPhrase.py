"""
🧩 7. Nombre de mots dans une phrase
Compte le nombre de mots dans une phrase (mots séparés par des espaces).

Exemple :
Entrée : Bonjour le monde
Sortie : 3

---
"""
def compter_nombre_mots(phrase):
    phrase_to_list = phrase.split(" ")
    return len(phrase_to_list)

phrase = "bonjour le monde"
print(compter_nombre_mots(phrase))

# Autre alternative :
def compter_nombre_mots(phrase):
    return len(phrase.strip().split())
