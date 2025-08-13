"""
Exercice 8:

Écrire un programme en Python qui demande à l'utilisateur deux nombres n1 et n2 et lui indique ensuite si le produit de ces deux nombres est positif ou négatif. On prévoit dans le programme le cas où le produit peut être nul.
"""

nombre1 = int(input("Entrer un nombre n1: "))
nombre2 = int(input("Entrer un nombre n2: "))

def signe_produit(n1, n2):
    if (n1 * n2 < 0):
        return "Le produit est négatif"
    elif (n1 * n2 > 0):
        return "Le produit est positif"

    return "Le produit est nul"

print(signe_produit(nombre1, nombre2))