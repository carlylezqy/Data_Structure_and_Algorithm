package com.zqy;
import java.net.ServerSocket;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;

public class Main{
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            serverSocket.setSoTimeout(10000);

            Socket socket = serverSocket.accept();

            DataInputStream in = new DataInputStream(server.getInputStream());
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

