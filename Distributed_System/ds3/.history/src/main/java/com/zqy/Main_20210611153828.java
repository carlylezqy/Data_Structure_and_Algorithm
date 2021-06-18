package com.zqy;
import java.net.ServerSocket;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.OutputStreamWriter;
import java.net.Socket;
import java.io.*;

public class Main{
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            serverSocket.setSoTimeout(100000);

            Socket socket = serverSocket.accept();
            System.out.println("远程主机地址：" + socket.getRemoteSocketAddress());
            


            //DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            String str = "Hello,socket";
            out.writeUTF(str);
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

