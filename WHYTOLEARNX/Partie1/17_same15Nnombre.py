"""
Exercice 17:

Ecrivez un programme en Python qui calcule la somme de 1 à N, où N est saisi par l'utilisateur. En utilisant la boucle "for".
"""
nombre = int(input("Entrer un nombre : "))

l = 1
somme_3 = 0

for i in range(1, nombre + 1):
    somme_3 += l
    l += 1

print(f"somme : {somme_3}")