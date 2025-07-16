# 🧩 Exercice 1 — Supprimer les voyelles d’un texte

text = "bonjour le monde"

text_to_list = list(text)
print('text to list  : {}'.format(text_to_list))

voyelles = list('aeyuio')
print('\nlises des voyelles : {}'.format(voyelles))


for char in text:
    if char.lower() in voyelles:
        delete_voyelles = text_to_list.pop(text_to_list.index(char))

print("".join(text_to_list))
        