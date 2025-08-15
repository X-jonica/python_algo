"""
Exercice 14:

Ecrivez un programme en Python qui calcule la somme de 1 à 10. En utilisant la boucle "while".
"""

n = 0
tab_n = []

while (n < 10):
    n += 1;
    tab_n.append(n)

print(tab_n)

def somme_nombre(tab):
    return sum(tab)

print(somme_nombre(tab_n))

# Autre alternativve

i = 1
somme = 0

while (i <= 10):
    somme += i
    i += 1

print(f"somme : {somme}")