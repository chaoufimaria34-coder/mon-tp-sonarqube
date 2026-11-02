# Importation d'un module inexistant pour forcer la détection d'un Bug critique
import module_inexistant_pour_tp

def calculer_moyenne():
    # Variable non définie (Undefined variable / NameError)
    resultat = total_points / nombre_elements
    return resultat

if __name__ == "__main__":
    calculer_moyenne()
