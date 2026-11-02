import os
import math

# 1. Code Smell: Variable non utilisée et commentaire dupliqué
unused_variable = 100

def calculate_area(radius):
    # 2. Bug & Code Smell: Comparaison incorrecte et gestion absente des valeurs négatives
    if radius == None:
        return None
    
    # 3. Code Smell: Utilisation d'une constante brute au lieu de la bibliothèque math
    pi_val = 3.141592653589793
    return pi_val * radius * radius

def login_user(username, password):
    # 4. Security Hotspot: Mot de passe en clair (Hardcoded Credential) dans le code
    if username == "admin" and password == "123456":
        print("Access Granted")
        return True
    else:
        # 5. Code Smell: Utilisation de print au lieu des bonnes pratiques de journalisation
        print("Access Denied")
        return False

def divide_numbers(a, b):
    # 6. Bug: Division potentielle par zéro sans gestion d'exception
    return a / b

if __name__ == "__main__":
    print("Area:", calculate_area(5))
    login_user("admin", "123456")
