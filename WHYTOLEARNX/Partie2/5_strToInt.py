"""
Exercice 5:

Écrire un programme Python pour convertir une chaîne de caractères en un nombre entier.
"""

#! New syntax : try: except ValueError :

enter = str(input("Entrer une chaine de caractere representant un nombre: "))

print(type(enter))

def string_to_number(str):
    return (f"'{str}' convertie en entier : {int(str)}")

print(string_to_number(enter))

print("\n ------------ CORRECTION ----------")

# Demander à l'utilisateur d'entrer une chaîne de caractères
chaine = input("Entrez une chaîne de caractères représentant un nombre : ")

# Conversion de la chaîne en entier
try:
    n = int(chaine)
    print(f"La chaîne '{chaine}' a été convertie en l'entier : {n}")
except ValueError:
    print("Erreur : La chaîne ne peut pas être convertie!")