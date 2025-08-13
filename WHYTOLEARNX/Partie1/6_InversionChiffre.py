"""
Exercice 6:

Ecrivez un programme en Python pour inverser les chiffres d'un nombre saisi par l'utilisateur.

Exemple de sortie:
"""

nombre = int(input("Entrer un nombre (deux min , ex  : 10 ) : "))

def inverser_nombre(n):
    n_str = str(n)
    n_str_reverse = n_str[::-1]
    n_str_rereverse = int(n_str_reverse)

    return n_str_rereverse;

print(f"inverse({nombre}) = {inverser_nombre(nombre)}")

# Autre alternative plus optimiser

def inverser_nombre_chat(n):
    return int(str(n)[::-1])

print(f"inverse({nombre}) = {inverser_nombre_chat(nombre)}")

