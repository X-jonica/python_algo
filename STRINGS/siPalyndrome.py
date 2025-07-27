
"""
🧩 6. Mot palindrome
Détermine si un mot donné est un palindrome
(se lit pareil dans les deux sens).

Exemples :
Entrée : radar   → Sortie : OUI
Entrée : python  → Sortie : NON

---
"""
def si_palyndrome(chaine):
    reversed_chaine = "".join(list(reversed(chaine)))
    if (reversed_chaine == chaine):
        return "OUI"
    else:
        return "NON"

mot = "python"
print(si_palyndrome(mot))

#! Autre alternative : (suggerer par chatgpt)
def si_palindrome(chaine):
    return "OUI" if chaine == chaine[::-1] else "NON"
