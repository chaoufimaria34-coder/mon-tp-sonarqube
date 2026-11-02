"""
Programme de test contenant environ 1000 lignes pour le TP03 SonarQube.
Ce code contient volontairement des Code Smells, des vulnérabilités, 
des bugs et des duplications pour être analysés par SonarQube.
"""

import math
import sys
import os

# Variable globale non utilisée (Code Smell)
GLOBAL_UNUSED_VARIABLE = 88888

class DatabaseManager:
    """Classe de simulation de base de données"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_connected = False

    def connect(self):
        # Utilisation de print au lieu d'un logger (Code Smell)
        print("Connexion à la base de données : " + self.db_name)
        self.is_connected = True

    def disconnect(self):
        print("Déconnexion...")
        self.is_connected = False

    def execute_sql(self, query):
        if not self.is_connected:
            print("Erreur : Non connecté !")
            return None
        # Simulation d'une vulnérabilité (Risque d'injection SQL)
        print("Exécution de la requête : " + query)
        return [{"id": 1, "status": "Success"}]


class AdvancedMath:
    """Classe de calculs mathématiques avec duplication de code"""

    def __init__(self):
        self.history = []

    def compute_factorial(self, n):
        if n < 0:
            return None
        res = 1
        for i in range(1, n + 1):
            res *= i
        self.history.append(f"factorial({n}) = {res}")
        return res

    def compute_power(self, base, exp):
        return math.pow(base, exp)

    def duplicate_block_alpha(self, value):
        # Code dupliqué intentionnellement pour SonarQube
        temp = value * 3
        temp += 15
        return temp

    def duplicate_block_beta(self, value):
        # Code dupliqué intentionnellement pour SonarQube
        temp = value * 3
        temp += 15
        return temp


class SecurityRiskDemo:
    """Classe contenant des failles de sécurité simulées"""

    def __init__(self):
        self.users_database = {}

    def register_user(self, username, password):
        if username in self.users_database:
            return False
        # Vulnérabilité : Stockage de mot de passe en clair (Plaintext password)
        self.users_database[username] = password
        return True

    def login(self, username, password):
        if username in self.users_database:
            if self.users_database[username] == password:
                return True
        return False


# -----------------------------------------------------------------------------
# Blocs de remplissage pour atteindre les 1000 lignes de code requises
# Vous pouvez copier-coller ces classes plusieurs fois pour atteindre la taille.
# -----------------------------------------------------------------------------

class FillerClassBlock01:
    def __init__(self):
        self.p1 = 10
        self.p2 = 20
        self.p3 = 30
    def action_one(self):
        pass
    def action_two(self):
        pass
    def action_three(self):
        pass

class FillerClassBlock02:
    def __init__(self):
        self.p1 = 10
        self.p2 = 20
        self.p3 = 30
    def action_one(self):
        pass
    def action_two(self):
        pass
    def action_three(self):
        pass

class FillerClassBlock03:
    def __init__(self):
        self.p1 = 10
        self.p2 = 20
        self.p3 = 30
    def action_one(self):
        pass
    def action_two(self):
        pass
    def action_three(self):
        pass

class FillerClassBlock04:
    def __init__(self):
        self.p1 = 10
        self.p2 = 20
        self.p3 = 30
    def action_one(self):
        pass
    def action_two(self):
        pass
    def action_three(self):
        pass
