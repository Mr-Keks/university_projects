package com.company;
import java.util.Scanner;

public class Main {

   public static void main(String[] args) {
      Scanner s = new Scanner(System.in);
       int a, b, c;
       int min, max;
       max = 0;
       min = 0;

       System.out.print("Enter first number: ");
       a = s.nextInt();
       System.out.print("Enter second number: ");
       b = s.nextInt();
       System.out.print("Enter third number: ");
      c = s.nextInt();


      //max
      if(a >= b & a >= c)
      {
          max = a;
       }
      else if (b >= a & b >= c){
          max = b;
       }
      else if (c >= a & c >= b){
          max = c;
       }

      //min
       if(a <= b & a <= c)
       {
           min = a;
       }
       else if (b <= a & b <= c){
           min = b;
       }
       else if (c <= a & c <= b){
           min = c;
       }

       System.out.println("min = " + min);
       System.out.println("max = " + max);
       if(a != max & a != min){
           System.out.print(a + " is averge");
       }
       else if (b != max & b != min){
           System.out.print(b + " is averge");
       }
       else if (c != max & c != min){
           System.out.print(c + " is averge");
       }
   }
}
