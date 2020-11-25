
package Exercicios;

import java.util.Scanner;

public class Exer_05 {
    public static void main(String[] args){
        System.out.println("Digite o raio do circulo: ");				
        Scanner r = new Scanner(System.in);
        
	double raio = r.nextFloat();
        
	double comprimento = 2*raio*Math.PI;					
        double area = Math.PI*raio*raio;						
	
        System.out.println(area);							
	System.out.println(comprimento);
       
    }
    
}

