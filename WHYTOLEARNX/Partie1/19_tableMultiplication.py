"""
Exercice 19:

Écrire un programme en Python qui affiche la table de multiplication d'un entier saisi par l'utilisateur, en utilisant la boucle "for".
"""

nombre = int(input("Entrer un nombre : "))

def calcule_table_multiplication(n):
    for i in range(0, 11):
        print(f"{n} * {i} = {i * n}")
    return ""
print(f"table {nombre} :")
print(calcule_table_multiplication(nombre))