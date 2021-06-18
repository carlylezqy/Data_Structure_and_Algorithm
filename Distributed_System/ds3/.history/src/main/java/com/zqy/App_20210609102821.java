package com.zqy;

public class App{
    public static void main( String[] args ){
        System.out.println( "Hello World!" );
        Task task = new Task();
        Person p = new Person();
        System.out.println(task.hello(p));
    }
    
}
