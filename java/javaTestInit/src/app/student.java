package app;

public class student extends user {
    public boolean verified=true;
    public String major;
    @Override
    public void sayHello(){
        System.out.println("hi my major is "+major+
        " and my name is "+ firstName+" "+lastName);
    }
    
}