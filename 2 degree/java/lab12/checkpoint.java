package com.company;
import java.io.*;
import java.util.ArrayList;
import java.util.Scanner;

import static com.company.Engine.addEmployee;

public class Checkpoint {
   public ArrayList<Employee> emp = new ArrayList<>();
   private boolean check;
   private static boolean checkShoutDown;

   public void outputAll(){
       if(emp.size() == 0)
           System.out.println("No have any employees...");
       else {
           for (Employee e : emp) {
               System.out.println(e.toString());
               if(emp.get(emp.size()-1) != e)
                   System.out.println("--------------------------------");
           }
       }
   }

   public void presenceEmployees(){
       check = false;
       for(Employee e : emp){
           if(e.getPresence()) {
               System.out.println(e.toString());
               check = true;
           }
       }
       if(!check)
           System.out.println("There are no presence employees");
   }

   public void absentEmployees(){
       check = false;
       for(Employee e : emp){
           if(!(e.getPresence())) {
               System.out.println(e.toString());
               check = true;
           }
       }
       if(!check)
           System.out.println("There are no absent employees");

   }

   public void findEmployee(String empNumber){
       int count = 0;
       for (Employee e: emp){
           if(String.valueOf(e.getEmpnumber()).equals(empNumber)){
               System.out.println(e.toString());
               count = 1;
           }
       }
       if(count == 0) System.out.println("Can`t find '" + empNumber + "' employee..");
   }

   //write to file
   public void writeToFile(){
       try(ObjectOutputStream fOp = new ObjectOutputStream(new FileOutputStream("employee.dat")))        {
           fOp.writeObject(emp);
       }catch(Exception e){
           System.out.println("Exception " + e);
       }
   }
   //read file
   public void readFile() throws IOException, InterruptedException {
       checkShoutDown = false;
       boolean tValue = true;
       while(tValue){
           try(ObjectInputStream ois = new ObjectInputStream(new FileInputStream("employee.dat"))){
               this.emp = (ArrayList<Employee>) ois.readObject();
               tValue = false;
           }
           catch(FileNotFoundException fnf){
               System.out.println("File exist!! \nPlease create new file.\n");
               System.out.println("1. Create new file");
               System.out.println("2. Exit\n");
               System.out.print("Select please: ");
               switch (new Scanner(System.in).nextLine()){
                   case("1") -> {
                       addEmployee();
                       tValue = false;
                       System.out.print("\nPress smth");
                       new Scanner(System.in).nextLine();
                   }
                   case("2") -> {
                       Engine.clearScreen();
                       System.out.println("See you next time");
                       System.out.print("\nPress smth");
                       new Scanner(System.in).nextLine();
                       checkShoutDown = shoutDown();
                       tValue = false;
                   }
               }
           }
           catch(Exception e){
               System.out.println("Exception " + e);
           }
       }
   }
   public static boolean getShoutDown(){
       return checkShoutDown;
   }
   public boolean shoutDown(){
       return true;
   }
   //IndexOutOfBoundsException
   public Employee deleteEmployee(String n){
       try{
           return emp.remove(findEmployeeForDetele(n));
       }catch (IndexOutOfBoundsException iofb){
           return null;
       }catch (Exception e){
           e.printStackTrace();
           return null;
       }
   }

   public void addEmp(Employee e){
       this.emp.add(e);
   }

   public Employee getEmployee(String n){
       try{
           return emp.get(findEmployeeForDetele(n));
       }catch (IndexOutOfBoundsException iofb){
           return null;
       }catch (Exception e){
           e.printStackTrace();
           return null;
       }
   }

   public int findEmployeeForDetele(String empNumber){
       int count = 0;
       for (Employee e: emp){
           if(String.valueOf(e.getEmpnumber()).equals(empNumber)){
               return count;
           }
           count += 1;
       }
       return -1;
   }
}
