"""
Exercice 24:

Écrire un programme en Python qui vérifie si une chaîne est un palindrome. Un palindrome est un mot qui s’écrit de la même manière après l’inversion de ce dernier. ‘ada’ est un palindrome.
"""

chaine = str(input("Entrer une chaine : "))

def siPalyndrome(chaine):
    if chaine[::-1] == chaine :
        return "palyndrome"
    return "pas palyndrome"

print(f"{chaine} : {siPalyndrome(chaine)}")

# Et c'est la fin de la partie 1 ;