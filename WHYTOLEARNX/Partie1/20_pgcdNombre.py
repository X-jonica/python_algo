"""
Exercice 20:

Écrire un programme en Python permettant de calculer le plus grand commun diviseur (PGCD) entre deux nombres entiers entrés par l'utilisateur.
"""

nombre1 = int(input("Entrer un premier nombre : "))
nombre2 = int(input("Entrer un second nombre : "))


def calcule_pgcd(n1, n2):
    diviseurs_communs = []
    if (n1 < n2):
        for i in range(1, n1 + 1):
            if(n1 % i == 0 and n2 % i == 0):
                diviseurs_communs.append(i)
    else:
        for i in range(1, n2 - 1):
            if(n2 % i == 0 and n1 % i == 0):
                diviseurs_communs.append(i)

    print(f"diviseur commun : {diviseurs_communs}")

    return max(diviseurs_communs)

print(f"PGCD({nombre1} , {nombre2}) = {calcule_pgcd(nombre1, nombre2)}")


# OPTIMISATION DE L'IDEE BRUTE
print("\n ------ AUTRE ALTERNATIVE ----")

def calcule_pgcd_optimise(n1, n2):
    plus_petit = min(n1, n2)
    diviseurs_communs = []

    for i in range(1, plus_petit + 1):
        if(n1 % i == 0 and n2 % i == 0):
            diviseurs_communs.append(i)

    print(f"diviseur communs : {diviseurs_communs}")

    return max(diviseurs_communs)

print(f"PGCD({nombre1} , {nombre2}) = {calcule_pgcd_optimise(nombre1, nombre2)}")
