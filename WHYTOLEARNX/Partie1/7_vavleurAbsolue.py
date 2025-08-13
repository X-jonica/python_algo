"""
Exercice 7:

Écrire un programme Python qui prend un nombre entière et calcule sa valeur absolue.
"""

nombre = int(input("Entrer un nombre: "))

def valeur_absolue(n):
    absolue_n = n
    if (n < 0):
        absolue_n = n * (-1)

    return absolue_n

print(f"|{nombre}| = {valeur_absolue(nombre)}")

# Autre alternative plus simple

print(f"|{nombre}| = {abs(nombre)}")