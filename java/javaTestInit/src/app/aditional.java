package app;

import java.util.List;

public class aditional {
    private String FirstName="default first";
    private String LastName="default last";//property
    String favFood;//field
    //通过方法来更改内部属性的工作范式叫做encapsulation
    //这种方法隔绝了直接对属性的操作，为今后内部重建做出
    //灵活性保障
    public void setFirst(String f){
        this.FirstName=f;
    }
    public void setLast(String l){
        this.LastName=l;
    }
    public String getFullName(){
        return FirstName + LastName;
    }
    public static void printUser(List<aditional> users) {
        for (aditional u : users){
            System.out.println(u.getFullName());
        }
    }
    public static void printUser(List<aditional> users, int times) {
        for(int i=0;i<times;i++){
            for (aditional u : users){
                System.out.println(u.getFullName());
            }
        }
    }
    @Override
    public String toString(){
        return "the full name is"+getFullName();
    }
    
    //by writing the same function/method with different parameters
    //it is okay to deal with different kinds of input
    //this is called overloading
    
}