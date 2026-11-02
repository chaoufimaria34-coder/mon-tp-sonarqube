"""
Code source modifié pour TP03 SonarQube.
Ce fichier contient intentionnellement des erreurs, des vulnérabilités, 
des duplications et des code smells pour faire réagir SonarQube.
"""

import math
import sys
import os

# 1. Code Smell: Variables globales non utilisées
UNAUTHORIZED_ACCESS_CODE = 9999
TEMP_TOKEN = "abc-123-xyz"

class UserAuthentication:
    """Classe de gestion des utilisateurs avec des failles de sécurité"""

    def __init__(self):
        # 2. Vulnerability: Utilisation d'un mot de passe en clair (Plaintext Password)
        self.admin_password = "admin123_password"
        self.user_database = {}

    def register_user(self, username, password):
        # 3. Bug / Code Smell: Pas de vérification si le mot de passe est vide
        self.user_database[username] = password
        print("Utilisateur enregistré avec succès : " + username)

    def login(self, username, password):
        # 4. Vulnerability: Risque de timing attack ou mauvaise gestion de validation
        if username in self.user_database:
            if self.user_database[username] == password:
                return True
        return False

    def unsafe_eval_input(self, user_input):
        # 5. Major Vulnerability: Utilisation de eval() (Dangereux)
        return eval(user_input)


class FinancialCalculator:
    """Calculs financiers avec des duplications de code et bugs potentiels"""

    def __init__(self, balance):
        self.balance = balance

    def calculate_interest(self, rate, years):
        # 6. Bug potentiel: Division par zéro possible si years == 0
        if years == 0:
            return 0
        
        # Code dupliqué intentionnellement (Duplications)
        total = self.balance * math.pow((1 + rate / 100), years)
        return total

    def calculate_interest_duplicate(self, rate, years):
        # Code dupliqué intentionnellement (Duplications pour SonarQube)
        if years == 0:
            return 0
        total = self.balance * math.pow((1 + rate / 100), years)
        return total

    def bad_exception_handling(self):
        # 7. Code Smell: Attrape une exception générale (Catching generic exception)
        try:
            result = 10 / 0
        except Exception as e:
            print("Erreur survenue")


class DataProcessor:
    """Processeur de données avec des Code Smells"""

    def process_items(self, items):
        output = []
        # 8. Code Smell: Boucle qui peut être optimisée ou variable mal nommée
        for i in range(len(items)):
            if items[i] != None:
                output.append(items[i] * 2)
            else:
                output.append(0)
        return output

    def redundant_method_a(self, x):
        # Duplication supplémentaire
        val = x + 10
        val = val * 2
        return val

    def redundant_method_b(self, x):
        # Duplication supplémentaire
        val = x + 10
        val = val * 2
        return val


# -----------------------------------------------------------------------------
# Pour atteindre les 1000 lignes demandées par l'encadreur avec des erreurs visibles,
# vous pouvez dupliquer les blocs ci-dessous plusieurs fois.
# -----------------------------------------------------------------------------

class FillerErrorBlock1:
    def __init__(self):
        self.error_code = 500
    def trigger_smell(self):
        # Variable non utilisée (Code Smell)
        unused_local = "test"
        print("Trigger 1")

class FillerErrorBlock2:
    def __init__(self):
        self.error_code = 500
    def trigger_smell(self):
        unused_local = "test"
        print("Trigger 2")

class FillerErrorBlock3:
    def __init__(self):
        self.error_code = 500
    def trigger_smell(self):
        unused_local = "test"
        print("Trigger 3")

class FillerErrorBlock4:
    def __init__(self):
        self.error_code = 500
    def trigger_smell(self):
        unused_local = "test"
        print("Trigger 4")

class FillerErrorBlock5:
    def __init__(self):
        self.error_code = 500
    def trigger_smell(self):
        unused_local = "test"
        print("Trigger 5")
