"""
Module de vérification de chaînes de caractères pour déterminer 
si elles sont ou non des palindromes.
"""

### Fonction secondaire

def ispalindrome(p):
    """
    Vérifie si la chaîne 'p' est un palindrome en ignorant la casse, 
    les accents, les espaces et les signes de ponctuation.

    Args:
        p (str): La chaîne de caractères à évaluer.

    Returns:
        bool: True si la chaîne est un palindrome, False sinon.
    """
    # 1. Préparation de la chaîne
    # Mettre la chaîne en minuscules pour ignorer la casse
    p_lower = p.lower()
    # Définition de la table de conversion pour gérer les accents
    accents = "éèêëàâäçîïôöûüù"
    sans_accents = "eeeeaaaaciiouuu"
    # Création de la table de traduction pour remplacer les lettres accentuées
    table_accents = str.maketrans(accents, sans_accents)
    # Application de la traduction
    p_sans_accents = p_lower.translate(table_accents)
    # 2. Nettoyage final
    p_final = ""
    # Filtrer uniquement les caractères alphanumériques (lettres et chiffres).
    # Cela supprime les espaces et la ponctuation, ainsi que les symboles.
    for caractere in p_sans_accents:
        if caractere.isalnum():
            p_final += caractere
    # 3. Vérification du Palindrome
    # Une chaîne est un palindrome si elle est égale à son inverse (slicing [::-1])
    return p_final == p_final[::-1]

### Fonction principale


def main():
    """
    Fonction principale pour tester le bon fonctionnement de ispalindrome().
    """

    # Vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        # Affichage du mot et du résultat de la vérification
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
