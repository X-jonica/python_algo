"""
Exercice 21:

Écrire un programme en Python qui calcule les nombres de Fibonacci jusqu'à 50.
"""
n1 = 1
n2 = 1
result = 0
fibo_tab = [n1, n2]

for _ in range(7):
    result = n1 + n2
    n1 = n2
    n2 = result
    fibo_tab.append(result)

print(fibo_tab)