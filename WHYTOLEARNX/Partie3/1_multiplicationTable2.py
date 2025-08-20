"""
Exercice 1:
Écrire un programme en Python qui affiche la table de multiplication de 3. En utilisant la boucle « for ».
"""

def multiplication_table(n):
    for i in range(0, 11):
        print(f"{n} * {i} = {n*i}")
    return ""

print(multiplication_table(3))
