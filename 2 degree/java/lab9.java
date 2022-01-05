package com.company;
import javax.annotation.processing.SupportedSourceVersion;
import java.io.*;
import java.lang.Math;
import java.lang.reflect.ParameterizedType;
import java.util.Scanner;


public class Main {
    //Reading file
    public static int[] RF(String file_name){
        BufferedReader br = null;
        int i = 0, j = 0;
        int [] k = new int[2];
        try(FileReader reader = new FileReader(file_name)){
            br = new BufferedReader(new FileReader(file_name));

            String line;
            while ((line = br.readLine()) != null){
                System.out.println(line);
                i = Math.max(i,line.length());
                j+=1;
            }
        } catch (IOException e)
        {
            System.out.println("Exception: " + e);
        }
        finally {
            try{
                br.close();
            }
            catch (IOException e)
            {
                System.out.println("Exception: " + e);
            }
            catch (NullPointerException e){
                System.out.println("file not exist!");
                return null;
            }
        }
        k[0] = i;
        k[1] = j;
        return k;
    }

    //Record file elements to char
    public static char[][] RF(String file_name, char[][] c, int i){
        BufferedReader br = null;
        int k = 0;
        char[] s;

        try(FileReader reader = new FileReader(file_name)){
            br = new BufferedReader(new FileReader(file_name));
            String line;
            while ((line = br.readLine()) != null){
               s = line.toCharArray();
               for(int z = 0; z < i; z++){
                   if(!(line.length() < z+1)){
                       c[k][z] = s[z];
                   }
                   else
                       continue;

               }
                k+=1;
            }
        } catch (IOException e)
        {
            System.out.println("Exception: " + e);
        }
        finally {
            try{
                br.close();
            }
            catch (IOException e)
            {
                System.out.println("Exception: " + e);
            }
        }
        return c;
    }

    //From char to string
    public static String[][] create_normal_matrix(char[][] c, int k[]){
        String[][] normal_matrix = new String[k[1]][k[1]];
        int counter = 0;

        for(int i = 0; i < k[1]; i++){
            for(int j = 0; j < k[1]; j++){
                normal_matrix[i][j] = "";
            }
        }

        for(int i = 0; i < k[1]; i++){
            for(int j = 0; j < k[0]; j++){
                try {
                    if(c[i][j] != ' '){
                        if((j+1) < k[0]){
                            if(c[i][j+1] == ' '){
                                normal_matrix[i][counter] += c[i][j];
                                counter += 1;
                            }
                            else{
                                normal_matrix[i][counter] += c[i][j];
                            }
                        }
                        else{
                            normal_matrix[i][counter] += c[i][j];
                        }
                    }
                    else{
                        continue;
                    }
                }
                catch (ArrayIndexOutOfBoundsException e){
                    System.out.println("matrix not square!");
                    return null;
                }
            }
            counter = 0;
        }
        return normal_matrix;
    }

    //form string to float
    public static float[][] to_float(String[][] s, int k){
        float[][] float_values = new float[k][k];
        for(int i = 0; i < k; i++){
            for(int j = 0; j < k; j++){
                try{
                    float_values[i][j] = Float.parseFloat(s[i][j]);
                }
                catch (NumberFormatException e){
                    if((s[i][j].equals(" "))){
                        System.out.println("not enough elements of the matrix!");
                        System.out.println("must be: " + k + " elements in all rows and cols");
                        return null;
                    }else{
                        System.out.println("cols: " + i + " | rows: " + j);
                        System.out.println("The value \"" + s[i][j] + "\" not number!");
                        return null;
                    }
                }
            }
        }
        return  float_values;
    }

    //The ratio of positive elements to negative ones
    public static float dMv(float[][] a, int k){
        int count_dod = 0;
        int count_vid = 0;
        for(int j = 0; j < k; j++){
            for(int z = 0; z < k; z++){
                if(a[j][z] >= 0){
                    count_dod += 1;
                }
                else
                    count_vid += 1;
            }
        }
        if(count_vid == 0)
            return 0;
        else
            return count_dod / count_vid;
    }

    //changing place elements
    public static float[][] new_matrix(float[][] a, int k){
        float temp;
        double nk = k;
        nk = Math.ceil(nk/2);
        float[][] a1 = new float[k][k];
        for(int i = 0; i < k; i++){
            for(int j = 0; j < k; j++){
                a1[i][j] = a[i][j];
            }
        }

        for(int j = 0; j < k; j++){
            for(int z = 0; z < nk-1; z++){
                temp = a[j][z];
                a[j][z] = a[j][(k-1)-z];
                a[j][(k-1)-z] = temp;
            }
        }
        return a;
    }

    public static int chek(){
        Scanner chek = new Scanner(System.in);
        int i;
        System.out.println("Are want create self matrix?");
        System.out.print("If yes enter 1 or 2 if not: ");
        i = chek.nextInt();
        if(i == 1){
            return 1;
        }
        else if(i == 2){
            return 2;
        }
        else {
            System.out.println("You enter wrong values!");
            return 0;
        }
    }

    public static void write_file(String f_name){
        int c = 0;
        try {
            File file = new File(f_name);
            file.createNewFile();
            Scanner cols = new Scanner(System.in);
            System.out.print("Enter number of columns: ");
            c = cols.nextInt();
            PrintWriter pw = new PrintWriter(file);

            for(int i = 0; i < c; i++){
                for(int j = 0; j < c; j++){
                    System.out.print("Enter column:" + i + "  rows: " + j + " value: ");
                    if(j == c-1)
                        pw.println(cols.nextInt());
                    else
                        pw.print(cols.nextInt() + " ");
                }
            }
            pw.close();
        }catch (IOException e){
            System.out.println(e);
        }
    }

    public static void main(String[] args) {
        int chek = chek();
        if(chek != 0){
            String r_line;
            int[] i;
            if(chek == 2){
                System.out.println("Enter file name: ");
                Scanner name_f = new Scanner(System.in);
                r_line = name_f.nextLine() + ".txt";
                i = RF(r_line);
            }
            else{
                Scanner name_f = new Scanner(System.in);
                System.out.println("Enter file name: ");
                r_line = name_f.nextLine();
                write_file(r_line);
                i = RF(r_line);
            }
            System.out.println("Input matrix:");
            if(i == null){
                System.out.println("end");
            }
            else if((i[1] % 2) == 0){
                System.out.println("the matrix must be odd!");
                System.out.println("end");
            }
            else{
                char[][] n = new char[i[0]][i[0]];
                String n1[][];
                float[][] A;

                System.out.println();

                n = RF(r_line, n, i[0]);
                n1 = create_normal_matrix(n, i);
                if(n1 == null){
                    System.out.println("end");
                }
                else{
                    A = to_float(n1, i[1]);
                    if(A == null){
                        System.out.println("end");
                    }
                    else{
                        float[][] B;
                        B = new_matrix(A, i[1]);

                        System.out.println("The ratio of positive elements to negative ones = " + dMv(A, i[1]));
                        System.out.println();
                        System.out.println("Output matrix:");
                        for(int j = 0; j < i[1]; j++){
                            for(int z = 0; z < i[1]; z++){
                                System.out.print(B[j][z] + " ");
                            }
                            System.out.println();
                        }
                    }
                }
            }
        }
    }
}