package com.zqy;

import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Main{
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("127.0.0.1", 1234);
            BufferedWriter bufferedWriter =new BufferedWriter(
                new OutputStreamWriter(socket.getOutputStream())
            );
            String str = "你好，这是我的第一个socket";
            bufferedWriter.write(str);
        }catch (IOException e) {
            e.printStackTrace();
        }
    }
}



// public class Main{
//     public static void main( String[] args ){
//         System.out.println( "Hello World!" );
//         Task task = new Task();
//         Person p = new Person();
//         task.hello(p);
//     }
    
// }

