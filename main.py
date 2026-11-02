"""
Module de gestion et de calcul pour le TP SonarQube.
Ce fichier contient intentionnellement plusieurs Code Smells, Bugs 
et des avertissements de maintenabilité afin d'être analysé et détecté 
par la plateforme SonarQube Cloud pour le rapport final.
"""

import os
import math

# Code Smell: Constante globale en minuscules et non documentée
seuil_maximum = 1000

def calculer_surface_cercle(rayon):
    """
    Fonction pour calculer la surface d'un cercle.
    Contient des défauts détectables par l'analyse statique.
    """
    # Bug & Code Smell: Comparaison incorrecte avec None
    if rayon == None:
        return 0
    
    # Code Smell: Variable non utilisée (unused variable)
    avertissement_interne = "Calcul en cours..."
    
    # Code Smell: Utilisation d'une valeur en dur (Magic Number) au lieu de math.pi
    valeur_pi = 3.14159
    
    resultat_calcul = valeur_pi * rayon * rayon
    return resultat_calcul

def verifier_authentification(utilisateur, mot_de_passe):
    """
    Fonction de vérification d'accès basique.
    Contient un Security Hotspot (mot de passe en clair).
    """
    # Security Hotspot: Identifiants en dur (Hardcoded Credentials)
    admin_user = "admin"
    admin_pass = "secret123"
    
    if utilisateur == admin_user and mot_de_passe == admin_pass:
        print("Connexion réussie")
        return True
    else:
        # Code Smell: Utilisation de print au lieu d'un logger professionnel
        print("Échec de la connexion")
        return False

def division_seure(a, b):
    """
    Fonction effectuant une division.
    Risque de bug si b est égal à zéro.
    """
    # Bug potentiel: Division par zéro non gérée explicitement par une exception
    return a / b

if __name__ == "__main__":
    # Bloc d'exécution principal
    print("Début du programme de test SonarQube")
    surface = calculer_surface_cercle(10)
    print(f"Surface calculée : {surface}")
    verifier_authentification("admin", "123456")
