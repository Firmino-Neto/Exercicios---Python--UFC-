package Exercicios;

import java.util.Scanner;

public class Exer_03 {
    public static void main(String[] args){        

        Scanner ano = new Scanner(System.in);
        Scanner meses = new Scanner(System.in);
        Scanner dias = new Scanner(System.in);
        
        System.out.println("Informe os anos:");
        int A = ano.nextInt();
        
        System.out.println("Informe os meses:");
        int M = meses.nextInt();
        
        System.out.println("Informe os dias:");
        int D = dias.nextInt();
        
        int idade = 365*A + M*30 + D;
              
        System.out.println("Idade em dias é "+idade);
    }
    
}