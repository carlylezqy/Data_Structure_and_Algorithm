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
            String str = "123";
            out.writeBytes(str);

            DataInputStream in = new DataInputStream(socket.getInputStream());

            int count = is.available();//原文出自【易百教程】，商业转载请联系作者获得授权，非商业请保留原文链接：https://www.yiibai.com/java_io/datainputstream.read_byte_b.html


            byte[] bs = new byte[count];

            dis.read(bs);
            for (byte b : bs) {
                char c = (char) b;
                System.out.print(c);
            }

            System.out.println(in.readString());

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

