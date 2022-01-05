package com.company;
import java.io.IOException;
import java.util.Scanner;

import static com.company.Engine.clearScreen;
import static com.company.Engine.addEmployee;
import static com.company.Engine.deleteEmployee;
import static com.company.Engine.editEmployee;
import static com.company.Engine.endProgram;


public class Main {
   public static Checkpoint ch = Engine.getCheckpoint();
   public static Scanner d = new Scanner(System.in);

   public static void main(String[] args) throws IOException, InterruptedException{
       boolean exit = false;
       clearScreen();
       ch.readFile();

       if(!Checkpoint.getShoutDown()){
           while(!exit) {
               clearScreen();
               System.out.println("1. Operation with employee");
               System.out.println("2. Editing employee");
               System.out.println("3. Exit");
               System.out.print("\nSelect menu: ");
               String chooseNumber = d.nextLine();
               boolean t = true;
               switch (chooseNumber) {
                   case ("1") -> {
                       while(t) {
                           clearScreen();
                           System.out.println("1. Add new employee");
                           System.out.println("2. Delete employee");
                           System.out.println("3. Edit employee");
                           System.out.println("4. Back");
                           System.out.print("\nSelect a menu: ");
                           chooseNumber = d.nextLine();
                           switch (chooseNumber) {
                               case ("1") -> {
                                   clearScreen();
                                   addEmployee();
                               }
                               case ("2") -> {
                                   clearScreen();
                                   deleteEmployee();
                               }
                               case ("3") -> {
                                   clearScreen();
                                   editEmployee();
                               }
                               case ("4") -> t = endProgram();

                           }
                           if(t) {
                               System.out.print("\nPress smth");
                               d.nextLine();
                           }
                       }
                   }
                   case ("2") -> {
                       while (t){
                           clearScreen();
                           System.out.println("1. Show all employees");
                           System.out.println("2. Show absent employees");
                           System.out.println("3. Show present employees");
                           System.out.println("4. Find employee");
                           System.out.println("5. Back");
                           System.out.print("\nSelect a menu: ");
                           chooseNumber = d.nextLine();
                           switch (chooseNumber){
                               case ("1") -> {
                                   clearScreen();
                                   ch.outputAll();
                               }
                               case ("2") -> {
                                   clearScreen();
                                   ch.absentEmployees();
                               }
                               case ("3") -> {
                                   clearScreen();
                                   ch.presenceEmployees();
                               }
                               case ("4") -> {
                                   clearScreen();
                                   String temp;
                                   try{
                                       while(true){
                                           clearScreen();
                                           System.out.print("Enter employee number: ");
                                           temp = d.nextLine();
                                           if(temp.equals("")){
                                               System.out.println("Please, enter correct value or enter '0' to go back!");
                                               d.nextLine();
                                           }
                                           else if(temp.equals("0")) break;
                                           else{
                                               clearScreen();
                                               ch.findEmployee(temp);
                                               break;
                                           }
                                       }
                                   }
                                   catch (Exception e){
                                       e.printStackTrace();
                                   }
                               }
                               case ("5") -> t = endProgram();
                               default ->{
                                   System.out.println("Please select correct number!");
                                   d.nextLine();
                               }
                           }
                           if(t) {
                               System.out.print("\nPress smth");
                               d.nextLine();
                           }

                       }
                   }
                   case ("3") -> {
                       clearScreen();
                       System.out.println("See next time");
                       exit = true;
                   }
                   default ->{
                       System.out.println("Please select correct number!");
                       d.nextLine();
                   }
               }
           }
       }
   }
}
