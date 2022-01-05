package com.company;

public class Checkpoint {
   Employee[] emp;

   public Checkpoint(Employee[] emp){
       this.emp = emp;
   }

   public void outputAll(){
       for(Employee e : emp){
           System.out.println(e.toString());
       }
   }

   public void presenceEmployees(){
       for(Employee e : emp){
           if(e.getPresence())
               System.out.println(e.toString());
       }
   }

   public void absentEmployees(){
       for(Employee e : emp){
           if(!(e.getPresence()))
               System.out.println(e.toString());
       }
   }

   public void findEmployee(String surname){
       for (Employee e: emp){
           if(e.getSurname().equals(surname)){
              System.out.println(e.toString());
           }
       }
   }
}
