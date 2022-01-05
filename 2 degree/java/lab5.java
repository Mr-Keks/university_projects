package com.company;
import java.util.Scanner;

public class Main
{
   public static void main(String[] args) {
       //task1
       System.out.print("What your name?: ");
       Scanner s = new Scanner(System.in);
       System.out.println("Hello " + s.nextLine());
       System.out.print("How old are you?: ");
       System.out.println(s.nextLine() + " is cool age");
       System.out.print("When you born?: ");
       System.out.println(s.nextLine() + " really?  me too)");
       System.out.println();
       
//task2
       float TF = 451;
       float TC;
       TC = (TF - 32) * 5/9;
       System.out.println("Fahrenheit temperature: " + TC);
   }
}
