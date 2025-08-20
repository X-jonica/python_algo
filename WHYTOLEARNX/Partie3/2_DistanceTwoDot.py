"""
Exercice 2:
Écrire un programme Python pour calculer la distance entre deux points.

sqrt((x2 - x1)² + (y2 - y1)²)

Remarque: x1, y1, x2, y2 sont tous des valeurs flottants.
"""
import math

# coordonnée point 01 :
x1 = 10
y1 = 18

# Coordonné point 2 :
x2 = 40
y2 = 20

def calcule_distance_entre_deux_point(x1, y1, x2, y2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

print(f"Distance entre ces points est:  {calcule_distance_entre_deux_point(10, 18, 40, 20)}")