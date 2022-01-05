package com.company;

import java.io.IOException;
import java.util.Locale;
import java.util.Scanner;

import java.time.LocalTime;

public class Engine {

   public static String checkCorrectValue(String message) throws IOException, InterruptedException{
       String s;
       while(true){
           clearScreen();
           System.out.print(message);
           s = d.nextLine();
           if(s.equals("")){
               System.out.println("Please enter correct value or select '0' to go back!");
           }
           else if(s.equals("0")){
               return null;
           }
           else{
               clearScreen();
               return s;
           }

       }
   }

   public static Checkpoint ch = new Checkpoint();

   public static Checkpoint getCheckpoint(){
       return ch;
   }

   public static boolean endProgram(){
       return false;
   }

   public static Scanner d = new Scanner(System.in);

   public static void clearScreen() throws IOException, InterruptedException {
       new ProcessBuilder("cmd", "/c", "cls").inheritIO().start().waitFor();
   }
   public static LocalTime Lt() throws IOException, InterruptedException{
       int hour = 1, minute = 1;
       int k = 0;
       int Sswitch = 0;

       while (true){
           try {
               clearScreen();
               if(Sswitch == 0){
                   System.out.print("Enter hour: ");
                   hour = Integer.parseInt(d.nextLine());
                   if(hour >= 0 & hour <= 60) Sswitch += 1;
                   else {
                       clearScreen();
                       System.out.println("Hour must be bigger or equal to 0 and less and equals to 60!");
                       d.nextLine();
                   }
               }
               else{
                   System.out.print("Enter minute: ");
                   minute = Integer.parseInt(d.nextLine());
                   if(minute > 0 & minute <= 60) break;
                   else{
                       clearScreen();
                       System.out.println("Minute must be bigger or equal to 0 and less and equals to 60!");
                       d.nextLine();
                   }
               }
               if(hour == 0 || minute == 0){k = 1; break;}
           }catch (NumberFormatException nf){
               clearScreen();
               System.out.println("Please enter number or press '0' to go back!");
               d.nextLine();
           }catch (Exception e){e.printStackTrace();}
           clearScreen();
       }
       if(k == 0) return LocalTime.of(hour, minute);
       else return null;
   }

   public static String setPresence(){
       Scanner s = new Scanner(System.in);
       String presence;
       try{
           while (true){
               clearScreen();
               System.out.print("Enter presence (yes/no): ");
               String temp = s.nextLine().toLowerCase(Locale.ROOT);
               switch (temp) {
                   case "yes":
                       presence = "yes";
                       return presence;
                   case "no":
                       presence = "no";
                       return presence;
                   case "0":
                       return null;
                   default:
                       clearScreen();
                       System.out.println("incorrect value, if you want to go back select '0'");
                       s.nextLine();
               }
           }
       }catch (Exception exp){
           exp.printStackTrace();
       }
       return "";
   }
   //add new Employee
   public static void addEmployee() throws IOException, InterruptedException{
       clearScreen();
       String surname;
       String position;
       String department;
       String empnumber;
       String certification;
       String presence = "yes";
       LocalTime time;
       Scanner s = new Scanner(System.in);

       surname = checkCorrectValue("Enter surname: ");
       if(surname == null) return;

       position = checkCorrectValue("Enter position: ");
       if(position == null) return;

       department = checkCorrectValue("Enter department: ");
       if(department == null) return;

       while(true){
           clearScreen();
           System.out.print("Enter employee number: ");
           empnumber = s.nextLine();
           if(empnumber.equals("0")) return;
           try{
               Integer.parseInt(empnumber);
               clearScreen();
               break;
           }catch (NumberFormatException nf){
               clearScreen();
               System.out.println("Please enter integer number or select '0' to go back!");
               d.nextLine();
           }catch (Exception e){d.nextLine();}
       }

       certification = checkCorrectValue("Enter certification: ");

       setPresence();

       clearScreen();
       time = Lt();
       if(time == null) return;

       ch.addEmp(new Employee(surname, position, department, Integer.parseInt(empnumber), certification, presence, time));
       ch.writeToFile();
       clearScreen();
       System.out.println("New employee '" + empnumber + "' successful created!");
   }

   //delete Employee
   public static void deleteEmployee() throws IOException, InterruptedException{
       while (true){
           System.out.print("Enter employee number: ");
           String empNum = d.nextLine();
           if(empNum.equals("0")){
               break;
           }else{
               if(ch.deleteEmployee(empNum) == null){
                   clearScreen();
                   System.out.println("Can`t find '"+ empNum +"' employee!");
                   System.out.println("Please try again or select '0' to go back!");
                   d.nextLine();
                   clearScreen();
               }
               else {
                   ch.writeToFile();
                   clearScreen();
                   System.out.println("Employee number: '" + empNum + "' successful deleted!");
                   break;
               }
           }
       }
   }

   //edit Employee
   public static void editEmployee() throws IOException, InterruptedException{
       String result;
       Employee n = null;
       boolean t = true;
       while (true) {
           clearScreen();
           System.out.print("Enter employee number: ");
           result = d.nextLine();
           if (result.equals("0"))
           {
               t = false;
               break;
           }
           else if (ch.getEmployee(result) == null) {
               clearScreen();
               System.out.println("Can`t find '"+ result +"' employee!");
               System.out.println("Please try again or select '0' to go back!");
               d.nextLine();
               clearScreen();
           }
           else{
               n = ch.getEmployee(result);
               break;
           }
       }
       while (t) {
           clearScreen();
           System.out.println("1. position");
           System.out.println("2. department");
           System.out.println("3. presence");
           System.out.println("4. time");
           System.out.print("Choose what you want change: ");
           String chooseNumber = d.nextLine();
           if (chooseNumber.equals("0")) break;
           else {
               clearScreen();
               switch (chooseNumber) {
                   case ("1") -> {
                       System.out.print("Enter new position: ");
                       n.setPosition(d.nextLine());
                   }
                   case ("2") -> {
                       System.out.print("Enter new department: ");
                       n.setDepartment(d.nextLine());
                   }
                   case ("3") -> {
                       System.out.print("Enter new presence: ");
                       n.setPresence(setPresence());
                   }
                   case ("4") -> {
                       n.setTime(Lt());
                   }
                   default -> {
                       System.out.print("Error value, try again or select '0' to" +
                               "go back");
                       d.nextLine();
                       continue;
                   }
               }
               ch.writeToFile();
               clearScreen();
               System.out.println("Value successful changed");
               t = false;
           }
       }
   }
}
