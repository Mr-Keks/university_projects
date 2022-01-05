package com.company;
import java.util.Scanner;

public class Main {
   public static int rand(int min, int max)
   {
       max -= min;
       return (int) (Math.random() * ++max) + min;
   }

   public static float average(float[] a)
   {
       int av = 0;
       for(int i = 0; i < a.length; i++){
           av += a[i];
       }
       av = av/a.length;

       return av;
   }

   public static void main(String[] args) {
      int n = 10;
      float[] A = new float [n];
       float[] B = new float [n];
       float[] C = new float [n];
       float av = 0;

       for(int i = 0; i < n; i++){
           A[i] = i;
           B[i] = rand(-2,2);
       }

       av = average(A);
       System.out.println("Average number array A: " + av);
       for(int i = 0; i < n; i++){
           if(B[i] < 0){
               C[i] = av;
           }
           else {
               C[i] = B[i];
           }
       }

       for(int i = 0; i < n; i++){
           System.out.println("A[" + i + "] = " + A[i]);
           System.out.println("B[" + i + "] = " + B[i]);
           System.out.println("C[" + i + "] = " + C[i]);
           System.out.println();
       }
   }
}