package com.zqy;
import java.io.*;
import java.net.*;

public class Main{
    private static void send(){
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            serverSocket.setSoTimeout(100000);

            Socket socket = serverSocket.accept();
            System.out.println("远程主机地址：" + socket.getRemoteSocketAddress());

            //DataInputStream in = new DataInputStream(socket.getInputStream());
            //DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            //String str = "123";
            //out.writeBytes(str);

            

            DataInputStream in = new DataInputStream(socket.getInputStream());

            int count = in.available();
            byte[] bs = new byte[count];
            in.read(bs);

            for (byte b : bs) {
                char c = (char) b;
                System.out.print(c);
            }

            serverSocket.close();

        } catch (SocketTimeoutException s) {
           System.out.println("Socket timed out!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args) {
        Task task = new Task();
        ObjectOutputStream out = new ObjectOutputStream();
        obj_out.writeObject(task);

        //send();
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

