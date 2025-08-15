"""
Exercice 14:

Ecrivez un programme en Python qui calcule la somme de 1 à 10. En utilisant la boucle "while".
"""
nombre = int(input("Entrer un nombre : "))
i = 1
somme = 0

while (i <= nombre):
    somme += i
    i += 1

print(f"somme n°1 : {somme}")

print("\n ----- AUTRE ALTERNATIVE -----")

somme_2 = 0
nombres = []

while(somme_2 < nombre):
    somme_2 += 1
    nombres.append(somme_2)

print(f"somme n°2 : {sum(nombres)}")

print("\n ----- AUTRE ALTERNATIVE -----")

l = 1
somme_3 = 0

for i in range(1, nombre + 1):
    somme_3 += l
    l += 1

print(f"somme n°3 : {somme_3}")

print("\n ----- AUTRE ALTERNATIVE -----")

indice = 0
tab_nombres = []

for i in range(1, nombre + 1):
    indice += 1
    tab_nombres.append(indice)

print(f"somme n°2 : {sum(tab_nombres)}")

