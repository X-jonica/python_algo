"""
Exercice 9:

Ecrivez un programme Python pour calculer le périmètre et la surface d'un rectangle d'une hauteur de 8 cm et d'une largeur de 4 cm.

"""

def calcule_circumference_rectangle(long, larg):
    circumference = (long + larg) * 2
    return circumference

def calcule_surface_rectangle(long, larg):
    surface = long * larg
    return surface


print(f"Perimettre du rectangle = {calcule_circumference_rectangle(8,4)} cm")
print(f"Surface du rectangle = {calcule_surface_rectangle(8, 4)} cm²")
