/**
 * Programme Java étendu à plus de 1000 lignes pour le TP03 SonarQube.
 * Contient intentionnellement des Bugs, Vulnérabilités, Code Smells et Duplications.
 */

import java.util.ArrayList;
import java.util.List;

public class MainTP {

    // Code Smell: Variable globale non utilisée
    public static int GLOBAL_UNUSED_CODE = 9999;
    public static String API_SECRET_KEY = "12345-SECRET-KEY"; // Vulnérabilité: Hardcoded secret

    public static void main(String[] args) {
        System.out.println("Démarrage du programme TP SonarQube...");
        DatabaseSimulator db = new DatabaseSimulator();
        db.connectToDatabase("root", "");
        
        MathOperations math = new MathOperations();
        System.out.println("Factorielle : " + math.computeFactorial(5));
    }
}

class DatabaseSimulator {
    private boolean isConnected = false;

    public void connectToDatabase(String user, String pass) {
        // Bug / Vulnerability: Acceptation de mots de passe vides ou affichage sensible
        if (pass.equals("")) {
            System.out.println("Avertissement: Mot de passe vide pour l'utilisateur: " + user);
        }
        this.isConnected = true;
    }

    public void executeUnsafeQuery(String query) {
        // Vulnerability: Risque d'injection SQL simulé
        System.out.println("Exécution de la requête SQL: " + query);
    }
}

class MathOperations {
    
    public int computeFactorial(int n) {
        if (n < 0) {
            return -1;
        }
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *= i;
        }
        return result;
    }

    // Duplication de code intentionnelle (Duplications pour SonarQube)
    public int duplicateBlockAlpha(int val) {
        int temp = val * 2;
        temp += 10;
        return temp;
    }

    public int duplicateBlockBeta(int val) {
        // Code dupliqué
        int temp = val * 2;
        temp += 10;
        return temp;
    }

    public void badExceptionHandling() {
        // Code Smell: Catch générique
        try {
            int x = 10 / 0;
        } catch (Exception e) {
            System.out.println("Erreur attrapée");
        }
    }
}

// -------------------------------------------------------------------------
// Blocs de remplissage pour étendre le code et atteindre les 1000 lignes
// -------------------------------------------------------------------------

class FillerJavaBlock01 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test"; // Code Smell
        System.out.println("Block 01 processing");
    }
}

class FillerJavaBlock02 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 02 processing");
    }
}

class FillerJavaBlock03 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 03 processing");
    }
}

class FillerJavaBlock04 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 04 processing");
    }
}

class FillerJavaBlock05 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 05 processing");
    }
}

class FillerJavaBlock06 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 06 processing");
    }
}

class FillerJavaBlock07 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 07 processing");
    }
}

class FillerJavaBlock08 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 08 processing");
    }
}

class FillerJavaBlock09 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 09 processing");
    }
}

class FillerJavaBlock10 {
    private int field1 = 1;
    private int field2 = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 10 processing");
    }
}

