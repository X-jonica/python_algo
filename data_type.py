# In programming, data type is an important concept.
"""
Variables can store data of different types, and different types can do different things.

Python has the following data types built-in by default, in these categories:


# Text Type:	    str 

# Numeric Types:    int, float, complex

# Sequence Types:	list, tuple, range

# Mapping Type:	    dict 

# Set Types:	    set, frozenset

# Boolean Type:	    bool

# Binary Types:	    bytes, bytearray, memoryview

# None Type:	    NoneType

"""

print('\n------------------------------------------------------------------------')


# ✅ set = pas d’ordre, pas de doublons, recherche rapide.

x = {"apple", "banana", "cherry"}

#display x:
print(x)

#display the data type of x:
print(type(x)) 

# exemple de "set" 
for i in range(5):
    print({"apple", "banana", "cherry", "cherry"})

print('\n------------------------------------------------------------------------')

# Type Frozenset 
"""
🔐 Pourquoi utiliser un frozenset ?
Parce qu’il est :

✅ Immuable :
Tu ne peux pas le modifier une fois créé. C’est utile pour garantir que les données ne changent jamais (comme une constante).

✅ Hashable :
Un set ne peut pas être une clé de dictionnaire car il est mutable (modifications = casse du système de hachage).
Mais un frozenset, lui, peut servir de clé dans un dictionnaire ou élément dans un autre set.
"""

x = frozenset({"apple", "banana", "cherry"})

print(x)              # frozenset({'cherry', 'banana', 'apple'})
print(type(x))        # <class 'frozenset'>

# x.add("mango")      ❌ Erreur ! 'frozenset' object has no attribute 'add'

print('\n------------------------------------------------------------------------')


# Type bytes 
"""
📌 Pourquoi utiliser bytes ?

- Les objets bytes sont utilisés :
- Quand tu travailles avec des fichiers binaires
- Pour les transmissions de données (réseaux, sockets, API)
- Pour encoder/décoder des chaînes (str ↔ bytes)
"""

x = b"Hello"

#display x:
print(x)

#display the data type of x:
print(type(x)) 

"""
Propriétés de bytes: 
✅ Immuable (comme frozenset)
✅ Peut être parcouru (for b in x:)
❌ Ne contient que des entiers entre 0 et 255
❌ Ne supporte pas directement les méthodes string (replace, lower...) sauf si converti
"""

print('\n------------------------------------------------------------------------')

# byearray

"""
🧪 En résumé :
x = bytearray(5) crée 5 octets : [0, 0, 0, 0, 0]
C’est mutable → tu peux faire x[0] = 65 etc.
C’est utile quand tu veux travailler avec des données binaires et pouvoir les modifier.
"""
# exemple 

x = bytearray(5)
x[0] = 65
x[1] = 66
x[2] = 67
print(x)         # bytearray(b'ABC\x00\x00')
print(x.decode())  # 'ABC\x00\x00' (si tu veux le lire comme une string)



"""
🧠 À retenir sur memoryview :
- Sert à accéder et manipuler des blocs mémoire sans duplication
- Très utile pour les gros volumes de données
- Plus utilisé dans les domaines scientifiques, bas niveau, ou réseau
- Plus rapide et efficace que de copier des données avec slice ou bytes()
"""