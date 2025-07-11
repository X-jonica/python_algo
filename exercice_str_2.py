# 🧩 Exercice 1 — Supprimer les voyelles d’un texte

text = "bonjour le monde"
list_text = list(text)
print("--- avant ---")
print(text)
print("----")

voyelle = list("aeyuio")
print(voyelle)

for char in text:
    if char.lower() in voyelle:
        index_char = list_text.index(char)
        print(char, index_char)
        new_list = list_text.pop(index_char)

print("--- après ---")
print("".join(list_text))
print("-----")
