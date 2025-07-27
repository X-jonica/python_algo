# Exercice 3 : compter les lettres de l'alphabet 
text = "hello world"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for lettre in alphabet:
  count = text.count(lettre)
  print(f"{lettre} : {count}")
