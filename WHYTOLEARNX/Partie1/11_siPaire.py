"""
Exercice 11:

Écrire un programme Python pour vérifier si un nombre est pair ou impair.
"""
nombre = int(input("Entrer un nombre : "))

def si_paire(n):
    if (n % 2 == 0):
        return "paire"
    return "impaire"

print(f"{nombre} est {si_paire(nombre)}")