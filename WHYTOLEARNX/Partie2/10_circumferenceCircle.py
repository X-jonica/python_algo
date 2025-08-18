"""
Exercice 10:

Écrire un programme Python pour calculer le périmètre et la surface d'un cercle dont le rayon est 5.
"""

def calcule_circomference_circle(r):
    pi = 3.14
    circomference = 2 * pi * r
    return circomference

def calcule_surface_circle(r):
    pi = 3.14
    surface = pi * (r**2)
    return surface

print(f"Périmètre du cercle = {calcule_circomference_circle(5)} cm")
print(f"Surface du cercle = {calcule_surface_circle(5)} cm²")

# Ainsi s' acheve la pertie 2