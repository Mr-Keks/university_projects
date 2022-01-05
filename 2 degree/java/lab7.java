package com.company;
import  java.util.Scanner;

import java.util.Scanner;

public class Main {
   public static long factorial(int number) {
       long result = 1;

       for (int factor = 2; factor <= number; factor++) {
           result *= factor;
       }

       return result;
   }
   public static void main(String[] args) {
      float sum = 0f;
      int i = 1, N;
      Scanner s = new Scanner(System.in);

      System.out.print("Enter N number: ");
       N = s.nextInt();

       System.out.println("***For***");
       for(int j = 1; j <= N; j++){
           sum = sum + (float) j/factorial(j);
       }
       System.out.println("for sum = " + sum);

       sum = 0;
       System.out.println();
       System.out.println("***While***");
       while (i <= N){
           sum += (float) i/factorial(i);
           i++;
       }
       System.out.println("while sum = " + sum);

       sum = 0;
       i = 1;
       System.out.println();
       System.out.println("***Do While***");
       do {
           sum += (float) i/factorial(i);
           i++;
       }while (i <= N);
       System.out.println("do while sum = " + sum);
   }
}