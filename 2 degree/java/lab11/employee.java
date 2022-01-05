package com.company;
import java.lang.reflect.Field;
import java.lang.reflect.Modifier;
import java.text.ParseException;
import java.util.ArrayList;
import java.util.List;

public class Employee {
   private final String surname;
   private String position;
   private String department;
   private final int empnumber;
   private final String certification;
   private boolean presence;
   private String time;


   public Employee(String surname, String position, String department,
                   int empNumber, String certification, boolean presence, String time) {
       this.surname = surname;
       this.position = position;
       this.department = department;
       this.empnumber = empNumber;
       this.certification = certification;
       this.presence = presence;
       this.time = time;
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
   public String getTime(){
       return this.time;
   }

   //setters
   public void setPosition(String newPositon){
       this.position = newPositon;
   }
   public void setDepartment(String newDepartment){
       this.department = newDepartment;
   }
   public void setPresence(boolean presence){
       this.presence = presence;
   }
   public void setTime(String newTime){
       this.time = time;
   }

   @Override
   public String toString(){
       return "Surname: " + this.surname + " | position: " + this.position +
               " | department: " + this.department + " | employee number: " +
               this.empnumber + " | presence in territory: " + this.presence +
               " | last entrance/exit: " + this.time;
   }
}
