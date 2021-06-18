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
            Socket socket = new Socket("127.0.0.1", 1234);
            BufferedWriter bufferedWriter =new BufferedWriter(new OutputStreamWriter(socket.getOutputStream()));

                        String str="你好，这是我的第一个socket";
            
                        bufferedWriter.write(str);
            
                    }catch (IOException e) {
            
            e.printStackTrace();
            
                    }
            
            }
            
            }
            
            作者：长道
            链接：https://www.jianshu.com/p/cde27461c226
            来源：简书
            著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。


// public class Main{
//     public static void main( String[] args ){
//         System.out.println( "Hello World!" );
//         Task task = new Task();
//         Person p = new Person();
//         task.hello(p);
//     }
    
// }

