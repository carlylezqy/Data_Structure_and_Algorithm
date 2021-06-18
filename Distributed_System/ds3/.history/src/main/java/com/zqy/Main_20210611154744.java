package com.zqy;
import java.io.*;
import java.net.*;

public class Main{
    public static void main(String[] args) {
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            serverSocket.setSoTimeout(100000);

            Socket socket = serverSocket.accept();
            System.out.println("远程主机地址：" + socket.getRemoteSocketAddress());

            //DataInputStream in = new DataInputStream(socket.getInputStream());
            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            String str = "中文测试";
            out.writeBytes(str);
            serverSocket.close();
        } catch (SocketTimeoutException s) {
           System.out.println("Socket timed out!");
        } catch (IOException e) {
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

