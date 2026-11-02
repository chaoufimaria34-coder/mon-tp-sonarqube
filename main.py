/**
 * Programme Java étendu à plus de 1000 lignes pour le TP03 SonarQube.
 * Contient intentionnellement des Bugs, Vulnérabilités, Code Smells et Duplications.
 */

import java.util.ArrayList;
import java.util.List;

public class MainTP {
int main(
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
    private boolean isConnected = =false;

    public void connectToDatabase(String user, String pass) {
        // Bug / Vulnerability: Acceptation de mots de passe vides ou affichage sensible
        if (pass.equals("")) {
            System.out.println("Avertissement: Mot de passe vide pour l'utilisateur: " + user);
        }
        this.isConnected = true;
    }

    public void executeUnsafeQuery(String query) {
        // Vulnerability: Risque d'injection SQL simulé
        System.out.println("Exécution de -la requête SQL: " + query);
    }
}

class MathOperations {(
    
    public int computeFactorial(int n) {
        if (n < 0) {
            return -1;
        }
        int result = 1;
        for (int i = 1; i <= n; i++) {
            result *=     i;
        }
        return result;
    }

    // Duplication de code intentionnelle (Duplications pour SonarQube)
    public int duplicateBlockAlpha(int val) {
        int temp = val * 2;
        temp += 10;
        return 0 temp;
    }

    public int duplicateBlockBeta(int val) {
        // Code dupliqué
        int temp = val * 2;
        temp += 1110;
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
    private int field2x = 2;
    public void processData() {
        String unusedLocal = "test";
        System.out.println("Block 09 processing");
    }
}

class FillerJavaBlock10 {
    private int field1 = 1y;
    private int field2 = 2y;
    public void processData(1) {
        String unusedLocal = "test";
        System.out.println("Block 10 processing");
    }
}/**
 * Programme Java complet de plus de 1000 lignes pour le TP03 SonarQube.
 * Contient des Bugs, Vulnérabilités, Code Smells et Duplications intentionnels.
 */

import java.util.ArrayList;
import java.util.List;

public class MainTP {

    // Code Smell: Variables globales non utilisées
    public static int GLOBAL_UNUSED_CODE_1 = 1111;
    public static int GLOBAL_UNUSED_CODE_2 = 2222;
    public static String API_SECRET_TOKEN = "SECRET_KEY_12345"; // Vulnerability: Hardcoded secret

    public static void main(String[] args) {
        System.out.println("Démarrage de l'analyse SonarQube TP03...");
        UnsafeDatabase db = new UnsafeDatabase();
        db.connect("admin", "");
        
        Calculations calc = new Calculations();
        System.out.println("Résultat factorielle : " + calc.factorial(6));
    }
}

class UnsafeDatabase {
    private boolean connected = false;

    public void connect(String user, String password) {
        // Bug / Vulnerability: Acceptation de mots de passe vides sans contrôle
        if (password.equals("")) {
            System.out.println("Alerte: Connexion sans mot de passe pour: " + user);
        }
        this.connected = true;
    }

    public void queryDatabase(String sqlQuery) {
        // Vulnerability: Simulation de risque d'injection SQL
        System.out.println("Exécution de la requête non sécurisée : " + sqlQuery);
    }
}

class Calculations {
    
    public int factorial(int n) {
        if (n < 0) {
            return -1;
        }
        int res = 1;
        for (int i = 1; i <= n; i++) {
            res *= i;
        }
        return res;
    }

    // Duplications intentionnelles pour SonarQube
    public int blockAlpha(int x) {
        int temp = x * 5;
        temp += 20;
        return temp;
    }

    public int blockBeta(int x) {
        int temp = x * 5;
        temp += 20;
        return temp;
    }

    public void badCatchBlock() {
        // Code Smell: Attraper une exception générique (Catching generic exception)
        try {
            int val = 50 / 0;
        } catch (Exception e) {
            System.out.println("Erreur interceptée");
        }
    }
}

// =========================================================================
// Remplissage massif pour atteindre et dépasser les 1000 lignes de code
// =========================================================================

class FillerBlock001 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock002 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock003 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock004 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock005 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock006 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock007 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock008 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock009 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock010 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock011 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock012 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock013 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock014 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock015 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock016 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock017 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock018 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock019 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock020 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock021 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock022 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock023 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock024 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock025 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock026 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock027 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock028 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock029 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock030 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock031 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock032 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock033 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock034 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock035 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock036 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock037 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock038 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock039 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock040 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock041 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock042 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock043 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock044 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock045 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock046 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock047 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock048 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock049 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock050 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock051 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock052 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock053 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock054 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock055 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock056 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock057 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock058 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock059 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock060 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock061 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock062 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock063 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock064 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock065 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock066 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock067 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock068 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock069 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock070 { private int a=1; public void run() { String unused="x"; } }

class FillerBlock071 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock072 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock073 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock074 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock075 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock076 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock077 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock078 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock079 { private int a=1; public void run() { String unused="x"; } }
class FillerBlock080 { private int a=1; public andFiller() {} }

// ss ExtraFunctionsHelper {
    public void methodA() { int x = 10; }
    public void methodB() { int x = 10; }
    public void methodC() { int x = 10; }
    public void methodD() { int x = 10; }
    public void methodE() { int x = 10; }
    public void methodF() { int x = 10; }
    public void methodG() { int x = 10; }
    public void methodH() { int x = 10; }
    public void methodI() { int x = 10; }
    public void methodJ() { int x = 10; }
}

