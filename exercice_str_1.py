# Exercce 1 : Je dois compter les voyelles : 

voyelles = ['a', 'e', 'y', 'u', 'i', 'o']
text = "Bonjour tous le monde"
compteur = 0

for i in text:
  if i.lower() in voyelles:
    compteur += 1
    print(i)

print(compteur)

# Exercice 2 : Inverser une chaîne
text = 'Python'
print(text)

_inverse = text[::-1]
print(_inverse)

# cas numero 2 :
text_list = list(text)
print(text_list)

reverse = list(reversed(text))
print(reverse)

jointure = "".join(reverse)
print(jointure)

# Exercice 3 : compter les lettres de l'alphabet 
text = "hello world"
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for lettre in alphabet:
  count = text.count(lettre)
  print(f"{lettre} : {count}")

