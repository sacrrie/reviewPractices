package app;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {//method
        //static means it does not need an instance for runing
        System.out.println("Hello ");
        student s = new student();
        s.major="CS";
        s.firstName="ga";
        s.lastName="tech";
        teacher t = new teacher();
        t.firstName="georgia";
        t.lastName="tech";

        List<user> uss= new ArrayList<user>();
        uss.add(s);
        uss.add(t);
        for (user u:uss){
            u.sayHello();
        }

    }
}
// literals: the value  
// for primitive types no need for the type x = new type;
//final is for making constant
/*
byte can store both integer or char
short int long are three digit range for int number
use double would be suitable for the most cases only use float when
it became memory constraint

for the comparison sign ==, primitives work but objects don't
since obj stores the references to the objects, a.k.a. pointers
comparison operators the same with python
the same with logical operators
similiar to C, conditional operator like:
int points = name.equals("clare")? 5:10;
single line if statement, only that later part gonna get executed
if (a==b) c=1;
array.sort
array.parallesort(merge sort for large array)
Arrays.equals for comparing between arrays
2d array doesn't have to be a rectangle size
transform list to array then to string to print
*/