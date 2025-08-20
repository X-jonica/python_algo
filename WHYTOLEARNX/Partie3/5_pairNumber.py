"""
Exercice 5:

Écrire un programme en Python pour afficher les nombres pairs entre 0 et N, où N est saisi par l’utilisateur.
"""
n = int(input("Saisisser un nombre: "))

def afficher_nombre_pair_jusqu_a_n(n):
    nombre_paires = []
    for i in range(0, n, 2):
        nombre_paires.append(i)
    return nombre_paires

print(f"nombre paire de 0 a {n} : {afficher_nombre_pair_jusqu_a_n(n)}")