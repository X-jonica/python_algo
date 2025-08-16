"""
Exercice 23:

Écrivez un programme Python pour afficher la valeur ascii d’un caractère donné.
"""

#! ASCII = American Standard Code for Information Interchange

caractere = input("Entrer un caractere : ")

def reconnaitre_ascii(char):
    return ord(char)

print(f"la valeur ASCII du caractere '{caractere} est : '{reconnaitre_ascii(caractere)}'")

#? EUREKA! Je iens de decouvrir cete fonction

