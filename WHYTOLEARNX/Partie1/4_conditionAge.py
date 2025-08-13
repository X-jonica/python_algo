"""
Exercice 4:

Ecrivez un programme en Python qui demande l’âge et permet de renseigner sa catégorie sachant que les catégories sont les suivantes:

Gamin de 6 à 7 ans
Pupille de 8 à 9 ans
Jeune de 10 à 11 ans
Cadet après 12 ans
"""

age_user = int(input("Entrer votre age : "))

def reconnaissaceAge(age):
    if (6 <= age <= 7):
        return "Gamin"
    elif (8 <= age <= 9):
        return "Pupille"
    elif (10 <= age <= 11):
        return "Jeune"
    return "Cadet"

print("Vous etes {}".format(reconnaissaceAge(age_user)))

# Autre alternative !!!

def reconnaissance_age(age):
    categories = {
        range(6, 8): "Gamin",
        range(8, 10): "Pupille",
        range(10, 12): "Jeune"
    }

    for plage, nom in categories.items():
        if age in plage:
            return nom
    return "Cadet"

print(f"vous êtes {reconnaissance_age(age_user)}")