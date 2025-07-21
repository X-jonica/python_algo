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


"""
🧩 6. Mot palindrome
Détermine si un mot donné est un palindrome
(se lit pareil dans les deux sens).

Exemples :
Entrée : radar   → Sortie : OUI
Entrée : python  → Sortie : NON

---
"""
def si_palyndrome(chaine):
    reversed_chaine = "".join(list(reversed(chaine)))
    if (reversed_chaine == chaine):
        return "OUI"
    else:
        return "NON"

mot = "python"
print(si_palyndrome(mot))

#! Autre alternative : (suggerer par chatgpt)
def si_palindrome(chaine):
    return "OUI" if chaine == chaine[::-1] else "NON"

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
"""

Bonne chance ! Résous-les un par un et envoie-moi ton code pour correction ou amélioration ! 🔥🐍
"""
