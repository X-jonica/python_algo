"""
Exercice 9:

Écrire un programme Python pour trouver le nombre max à partir de trois nombres.
"""
confirmation = int(input("Vous souhaitez effectuer combien d'essais? :  "))

nombres = []

for i in range(1, confirmation + 1):
    n = int(input(f"Entrer le nombre n°{i} : "))
    nombres.append(n)

def max_nombre(tab):
    return max(tab)

print(f"Le max entre {nombres} est : {max_nombre(nombres)}")