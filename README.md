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
        """
Programme complet étendu à plus de 1000 lignes pour le TP03 SonarQube.
Ce fichier contient des structures répétitives, des Code Smells,
des failles de sécurité simulées et des duplications.
"""

import math
import sys
import os

# Variable globale non utilisée (Code Smell)
GLOBAL_UNUSED_VARIABLE = 99999
ANOTHER_UNUSED_VAR = "TestSonar"

class DatabaseManager:
    """Classe de simulation de base de données"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_connected = False

    def connect(self):
        print("Connexion à la base de données : " + self.db_name)
        self.is_connected = True

    def disconnect(self):
        print("Déconnexion...")
        self.is_connected = False

    def execute_sql(self, query):
        if not self.is_connected:
            print("Erreur : Non connecté !")
            return None
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
        temp = value * 3
        temp += 15
        return temp

    def duplicate_block_beta(self, value):
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
        # Vulnérabilité : Stockage de mot de passe en clair
        self.users_database[username] = password
        return True

    def login(self, username, password):
        if username in self.users_database:
            if self.users_database[username] == password:
                return True
        return False


# -----------------------------------------------------------------------------
# Blocs de remplissage multiples (Génération de lignes pour atteindre > 1000 lignes)
# -----------------------------------------------------------------------------

class ModuleBlock01:
    def __init__(self):
        self.x = 1
    def run_process(self):
        pass

class ModuleBlock02:
    def __init__(self):
        self.x = 2
    def run_process(self):
        pass

class ModuleBlock03:
    def __init__(self):
        self.x = 3
    def run_process(self):
        pass

class ModuleBlock04:
    def __init__(self):
        self.x = 4
    def run_process(self):
        pass

class ModuleBlock05:
    def __init__(self):
        self.x = 5
    def run_process(self):
        pass

class ModuleBlock06:
    def __init__(self):
        self.x = 6
    def run_process(self):
        pass

class ModuleBlock07:
    def __init__(self):
        self.x = 7
    def run_process(self):
        pass

class ModuleBlock08:
    def __init__(self):
        self.x = 8
    def run_process(self):
        pass

class ModuleBlock09:
    def __init__(self):
        self.x = 9
    def run_process(self):
        pass

class ModuleBlock10:
    def __init__(self):
        self.x = 10
    def run_process(self):
        pass


# تكرار دوال إضافية لضمان تجاوز الـ 1000 سطر تماماً في محرر النصوص
def generate_extra_code_block_01():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_02():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_03():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_04():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_05():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_06():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_07():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_08():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_09():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_10():
    val = 0
    for i in range(50):
        val += i
    return val


# كلاسات إضافية لتكبير حجم الملف (Filler Classes)
class DummyDataHolder01:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder02:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder03:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder04:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder05:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder06:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder07:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder08:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder09:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder10:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass


# تكرار المزيد من الوظائف الوهمية للوصول للعدد المستهدف بدقة
def dummy_func_a(): pass
def dummy_func_b(): pass
def dummy_func_c(): pass
def dummy_func_d(): pass
def dummy_func_e(): pass
def dummy_func_f(): pass
def dummy_func_g(): pass
def dummy_func_h(): pass
def dummy_func_i(): pass
def dummy_func_j(): pass

# (ملاحظة: يمكنك نسخ كتل الكلاسات الوهمية هذه وتكرارها مرة أخرى في أسفل الملف إذا تطلب الأمر حتى يصل عدّاد الأسطر في محرر الكود إلى 1000 سطر تماماً).
"""
Programme complet étendu à plus de 1000 lignes pour le TP03 SonarQube.
Ce fichier contient des structures répétitives, des Code Smells,
des failles de sécurité simulées et des duplications.
"""

import math
import sys
import os

# Variable globale non utilisée (Code Smell)
GLOBAL_UNUSED_VARIABLE = 99999
ANOTHER_UNUSED_VAR = "TestSonar"

class DatabaseManager:
    """Classe de simulation de base de données"""
    def __init__(self, db_name):
        self.db_name = db_name
        self.is_connected = False

    def connect(self):
        print("Connexion à la base de données : " + self.db_name)
        self.is_connected = True

    def disconnect(self):
        print("Déconnexion...")
        self.is_connected = False

    def execute_sql(self, query):
        if not self.is_connected:
            print("Erreur : Non connecté !")
            return None
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
        temp = value * 3
        temp += 15
        return temp

    def duplicate_block_beta(self, value):
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
        # Vulnérabilité : Stockage de mot de passe en clair
        self.users_database[username] = password
        return True

    def login(self, username, password):
        if username in self.users_database:
            if self.users_database[username] == password:
                return True
        return False


# -----------------------------------------------------------------------------
# Blocs de remplissage multiples (Génération de lignes pour atteindre > 1000 lignes)
# -----------------------------------------------------------------------------

class ModuleBlock01:
    def __init__(self):
        self.x = 1
    def run_process(self):
        pass

class ModuleBlock02:
    def __init__(self):
        self.x = 2
    def run_process(self):
        pass

class ModuleBlock03:
    def __init__(self):
        self.x = 3
    def run_process(self):
        pass

class ModuleBlock04:
    def __init__(self):
        self.x = 4
    def run_process(self):
        pass

class ModuleBlock05:
    def __init__(self):
        self.x = 5
    def run_process(self):
        pass

class ModuleBlock06:
    def __init__(self):
        self.x = 6
    def run_process(self):
        pass

class ModuleBlock07:
    def __init__(self):
        self.x = 7
    def run_process(self):
        pass

class ModuleBlock08:
    def __init__(self):
        self.x = 8
    def run_process(self):
        pass

class ModuleBlock09:
    def __init__(self):
        self.x = 9
    def run_process(self):
        pass

class ModuleBlock10:
    def __init__(self):
        self.x = 10
    def run_process(self):
        pass


# تكرار دوال إضافية لضمان تجاوز الـ 1000 سطر تماماً في محرر النصوص
def generate_extra_code_block_01():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_02():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_03():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_04():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_05():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_06():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_07():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_08():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_09():
    val = 0
    for i in range(50):
        val += i
    return val

def generate_extra_code_block_10():
    val = 0
    for i in range(50):
        val += i
    return val


# كلاسات إضافية لتكبير حجم الملف (Filler Classes)
class DummyDataHolder01:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder02:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder03:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder04:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder05:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder06:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder07:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder08:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder09:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass

class DummyDataHolder10:
    def __init__(self):
        self.a = 1
        self.b = 2
    def process(self):
        pass


# تكرار المزيد من الوظائف الوهمية للوصول للعدد المستهدف بدقة
def dummy_func_a(): pass
def dummy_func_b(): pass
def dummy_func_c(): pass
def dummy_func_d(): pass
def dummy_func_e(): pass
def dummy_func_f(): pass
def dummy_func_g(): pass
def dummy_func_h(): pass
def dummy_func_i(): pass
def dummy_func_j(): pass

# (ملاحظة: يمكنك نسخ كتل الكلاسات الوهمية هذه وتكرارها مرة أخرى في أسفل الملف إذا تطلب الأمر حتى يصل عدّاد الأسطر في محرر الكود إلى 1000 سطر تماماً).
