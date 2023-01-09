
package Package;
import java.util.Scanner;




public class Nagy_beni {
private static int szam;

    public static void main(String[] args) {
        Scanner sc = elso();
        System.out.println("Kérek be egy számot");
        int szam = sc.nextInt();
        
        
        
        }

    private static Scanner elso() {
        Scanner sc = masodikfeladat();
        
        System.out.println("Kérj be egy számot");
        int szam = sc.nextInt();
        return sc;
    
    
        
    }

    private static Scanner masodikfeladat() {
        Scanner sc = harmadikfeladat();
        System.out.println("Kérjen be egy számot");
        szam = sc.nextInt();       
        if (!(szam >= 5) && (szam <= 30)){
        } else {
        System.out.println("hiba");
        
    }
        return sc;
    }

    private static Scanner harmadikfeladat() {
        Scanner sc = negyedikfeladat();
         System.out.println("Kérjen be egy számot");
        szam = sc.nextInt();       
        while (!(szam >= 5) && (szam <= 30)){
       System.out.println("szam");
       
                    
            
            
        }
        
        return sc;
    }

    private static Scanner negyedikfeladat() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

   
    }
} 
        
        
    


   