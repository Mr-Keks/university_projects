package com.company;
import java.io.Serializable;
import java.time.LocalTime;


public class Employee implements Serializable {
   private final String surname;
   private String position;
   private String department;
   private final int empnumber;
   private final String certification;
   private boolean presence;
   private String stringPresence;
   private LocalTime time;


   public Employee(String surname, String position, String department,
                   int empNumber, String certification, String stringPresence, LocalTime time) {
       this.surname = surname;
       this.position = position;
       this.department = department;
       this.empnumber = empNumber;
       this.certification = certification;
       this.stringPresence = stringPresence;
       this.time = time;
       this.presence = this.stringPresence.equals("yes");
   }
   //getters
   public String getSurname(){
       return this.surname;
   }
   public String getPosition(){
       return this.position;
   }
   public String getDepartmente(){
       return this.department;
   }
   public int getEmpnumber(){
       return this.empnumber;
   }
   public String getCertification(){
       return this.certification;
   }
   public boolean getPresence(){
       return this.presence;
   }
   public LocalTime getTime(){
       return this.time;
   }

   //setters
   public void setPosition(String newPositon){this.position = newPositon;}
   public void setDepartment(String newDepartment){
       this.department = newDepartment;
   }
   public void setPresence(String presence)
   {
       this.stringPresence = presence;
       this.presence = this.stringPresence.equals("yes");

   }
   public void setTime(LocalTime newTime){ this.time = newTime;}

   @Override
   public String toString(){
       return "Surname: " + this.surname + "\nposition: " + this.position +
               "\ndepartment: " + this.department + "\nemployee number: " +
               this.empnumber + "\npresence in territory: " + this.stringPresence +
               "\nlast entrance/exit: " + this.time;
   }
}
