"""
Exercice 16:

Ecrivez un programme en Python qui calcule la somme de 1 à 10. En utilisant la boucle "for".
"""

l = 1
somme = 0

for i in range(1, 11):
    somme += l
    l += 1

print(f"somme : {somme}")