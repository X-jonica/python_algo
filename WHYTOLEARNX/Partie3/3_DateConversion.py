"""
Exercice 3:

Écrire un programme Python pour convertir les jours spécifiés en années, semaines et jours. Note : Ne pas tenir en compte les années bissextiles.
"""

def conversion_jours_en_annee_semaine_jours(jours):
    annees = jours / 365
    print(f"Années : {int(annees)}")

    semaines = int((jours % 365) / 7)
    print(f"Semaines : {round(semaines)}")

    jours = jours - ((annees*365) + (semaines*7))
    print(f"Jours : {round(jours)}")
    return ""

nombre_jours = int(input("Entrer le nombre de jours: "))
print(conversion_jours_en_annee_semaine_jours(nombre_jours))
