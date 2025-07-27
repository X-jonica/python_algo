"""
🧩 Sujet : Le plus petit nombre pair supérieur à N

Écris un programme qui prend en entrée un entier N et qui affiche 
le plus petit nombre pair strictement supérieur à N.

Entrée :
    Un entier N (entre -10⁶ et 10⁶)

Sortie :
    Un entier pair, strictement supérieur à N.

Exemples :
    Entrée : 4      → Sortie : 6
    Entrée : 7      → Sortie : 8
    Entrée : -3     → Sortie : -2

Conseil :
    - Un nombre pair est divisible par 2 (x % 2 == 0)
    - Le résultat doit être STRICTEMENT supérieur à N
"""

entier = int(input("Entrer un nombre : "))

def plus_petit_nombre_pair_suiant(entier):
    n = entier + 1
    if (n % 2 != 0):
        n += 1
    return n

print(plus_petit_nombre_pair_suiant(entier))
