"""
Exercice 22:

Écrire un programme en Python qui inverse une chaîne de caractères en utilisant une boucle while.
"""

original_chaine = "WayToLearnX"
chaine_inverse = ""

# compter le mot (-1 pour le parcour d'apres)
i = len(original_chaine) -1

while i >= 0:
    # addition de chaine de caractère
    chaine_inverse = chaine_inverse + original_chaine[i]

    # decrementation de i jusqu'a a 0
    i -= 1

print(f"Inverse de  : '{original_chaine}' = '{chaine_inverse}'")