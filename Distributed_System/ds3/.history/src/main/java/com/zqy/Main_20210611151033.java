package com.zqy;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.ServerSocket;
import java.net.Socket;

public class Main{
    public static void main(String[] args) {
        try {
            Socket socket = new Socket("127.0.0.1",1234);
            Socket socket = serverSocket.accept(); //等待客户端的连接
            BufferedReader bufferedReader =new BufferedReader(
                new InputStreamReader(socket.getInputStream()) //获取输入流
            );
            String str = bufferedReader.readLine(); //读取一行数据
            System.out.println(str); //输出打印
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

