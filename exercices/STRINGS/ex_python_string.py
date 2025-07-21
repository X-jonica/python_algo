# exercice python string 

def saut_de_ligne():
    print('\n')

#! ✅ 1. Multiline Strings

'''
Utilisation des triples guillemets """ """ pour écrire plusieurs lignes.

🧪 Exercices :
Crée une variable bio contenant une présentation personnelle sur trois lignes, puis affiche-la.

Stocke dans une variable citation une citation célèbre sur plusieurs lignes, puis affiche-la.

Crée une variable adresse qui contient ton adresse complète (nom, rue, ville) sur plusieurs lignes, et affiche-la.

'''
bio = """Bonjour je suis jonica,
un developpeur web et mobile,
ouvert pour les offre de stage/CDI/CDD"""
print(bio)

saut_de_ligne()

citation = '''"qui semme le vent , recolte la tempete",
"on a rien sans rien",
"l'amour rends aveugle" '''
print(citation)

saut_de_ligne()

adresse = """nom : HENINTSOA Hasimanitriniaina Jonica, 
rue: Amontana LALAZANA , 
ville: FIANARANTSOA Madagascar"""
print(adresse)


#! ✅ 2. Strings are Arrays
print("\n--- Exercice 2 ---")
"""
On peut accéder à un caractère avec un index : chaine[0], chaine[3]...

🧪 Exercices :
Affiche le premier, le cinquième et le dernier caractère de la chaîne "Python est puissant".

Stocke la chaîne "Programmation" dans une variable et affiche le caractère à la position 4.

Crée une variable mot contenant "ordinateur" et affiche les caractères aux positions 1, 3 et 6.
"""
text = "Python est puissant"

print(text[0], text[4], text[-1])

saut_de_ligne()

var = "Programmation"
print(var[3])

saut_de_ligne()

word = "ordinateur" 
print(word[0], word[2], word[5])


#! ✅ 3. Looping Through a String
print("\n--- Exercice 3 ---")

"""
En théorie, on utilise une boucle, mais ici on va juste manuellement afficher plusieurs caractères pour comprendre la structure.

🧪 Exercices :
Stocke "banane" dans une variable, puis affiche un par un les caractères "b", "a", "n" sans boucle.

Écris "data" dans une variable et affiche les 4 caractères sur 4 lignes séparées.

Affiche chaque lettre de "fruit" en appelant chaque index individuellement ([0], [1], etc.).
"""

fruit = "banane" 
for x in fruit:
    print('"{}"'.format(x))

saut_de_ligne()

data = "data"
for x in data:
    print(x)

saut_de_ligne()

y = "fruit"
print(y[0])
print(y[1])
print(y[2])
print(y[3])
print(y[4])


#! ✅ 4. String Length
print("\n--- Exercice 4 ---")
"""
Utilisation de len() pour obtenir la longueur d’une chaîne.

🧪 Exercices :
Calcule et affiche la longueur de "informatique".

Crée une variable phrase = "Python est cool" et affiche sa longueur.

Stocke "1234567890" dans une variable et affiche le nombre de caractères.
"""

print(len("informatique"))

saut_de_ligne()

phrase = "Python est cool"
print(len(phrase))

saut_de_ligne()

nombres = "1234567890" 
print(len(nombres))


#! ✅ 5. Check String (keyword in)
print("\n--- Exercice 5 ---")
"""
Vérifier si un mot ou un caractère existe dans une chaîne.

🧪 Exercices :
Vérifie si "cool" est dans "Python est cool".

Vérifie si "x" est présent dans "exemple".

Crée une variable message = "Bienvenue sur la plateforme" et vérifie si "plateforme" s'y trouve.
"""
phrase_1 = "Python est cool"
if ("cool" in phrase_1):
    print("OUI, cool est dans '{}' ".format(phrase_1))

saut_de_ligne()

exemple = "exemple"
if ("x" in exemple):
    print('OUI, x est dans "exemple" ')

saut_de_ligne()

welcome = "Bienvenue sur la plateforme"
print("plateforme" in welcome)


#! ✅ 6. Check if NOT in String (keyword not in)
print("\n--- Exercice 6 ---")
"""
Vérifier si un mot ou un caractère n'existe pas dans une chaîne.

🧪 Exercices :
Vérifie si "voiture" n’est pas dans "Je vais à l’école".

Crée une variable text = "formation développeur" et vérifie si "design" n’est pas dans text.

Vérifie si "@" n’est pas dans "exemple.com".
"""

print("voiture" not in "Je vais à l’école")

saut_de_ligne()

txt = "formation développeur"
print("design" not in txt)

saut_de_ligne()

print("@" not in "exemple.com")

