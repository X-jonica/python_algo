"""
Exercice 1:

Écrire un programme Python pour compter les lettres, les espaces, les chiffres et les autres caractères d’une chaîne saisie.
"""

chaine = list("Rue 45, Quartier Sain Denis:France")
letters = list("abcdefghijklmnopqrstuvwxyz")
numbers = list("0123456789")
others = list("#,;:!ù^$£¨µ%/.?*+-")

def count_char(txt):
    count_letter = 0
    count_number = 0
    count_other = 0
    count_space = txt.count(" ")

    for i in txt:
        if (i.lower() in letters):
            count_letter += 1
        elif (i in numbers):
            count_number += 1
        elif (i in others):
            count_other += 1

    print(f"nombre de lettre : {count_letter}")
    print(f"nombre d'espace : {count_space}")
    print(f"nombre de chiffre : {count_number}")
    print(f"nombre d'autre caractere : {count_other}")

    return ""

print(count_char(chaine))

# the correction is on : https://waytolearnx.com/2024/08/exercice-corrige-python-pour-debutant-partie-2.html



