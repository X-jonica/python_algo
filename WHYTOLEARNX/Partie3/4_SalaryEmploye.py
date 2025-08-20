"""
Exercice 4:

Écrivez un programme Python qui accepte le nombre total d’heures travaillées au cours d’un mois et le montant que l’employé a reçu par heure. Affichez le salaire (avec deux décimales) de l’employé pour un mois donné.
"""

heur_de_travail = float(input("Saisir les heures de travail: "))

salaire_par_heure = float(input("Montant du salaire/heure: "))

def calcule_salaire_employer(heure_de_travaille, salaire_par_heure):
    salaire_par_mois = heure_de_travaille * salaire_par_heure
    return salaire_par_mois

print(f"Salaire = {calcule_salaire_employer(heur_de_travail, salaire_par_heure)} €")