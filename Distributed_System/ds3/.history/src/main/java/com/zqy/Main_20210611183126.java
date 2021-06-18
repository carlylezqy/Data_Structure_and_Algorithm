package com.zqy;
import java.io.*;
import java.net.*;
import java.util.Arrays;

public class Main{
    private static void send(Task task){
        try {
            ServerSocket serverSocket = new ServerSocket(1234);
            serverSocket.setSoTimeout(100000);

            Socket socket = serverSocket.accept();
            System.out.println("Remote Socket Address is " + socket.getRemoteSocketAddress());

            ByteArrayOutputStream baos = new ByteArrayOutputStream();
            ObjectOutputStream obj_out = new ObjectOutputStream(baos);
            obj_out.writeObject(task);

            DataOutputStream out = new DataOutputStream(socket.getOutputStream());
            out.write(baos.toByteArray());

            //System.out.println(Arrays.toString(buffer.toByteArray()));
            
            ByteArrayInputStream get_buffer = new ByteArrayInputStream(baos.toByteArray());
            try (ObjectInputStream input = new ObjectInputStream(get_buffer)){
                Task task_2 = (Task) input.readObject();
                System.out.println(task_2.str1 + task_2.str2);
            } catch (ClassNotFoundException e){
                e.printStackTrace();
            }

            DataInputStream in = new DataInputStream(socket.getInputStream());

            int count = in.available();
            byte[] bs = new byte[count];
            System.out.println(length(bs));
            in.read(bs);

            for (byte b : bs) {
                char c = (char) b;
                System.out.print(c);
            }

            serverSocket.close();
            obj_out.close();
        } catch (SocketTimeoutException s) {
           System.out.println("Socket timed out!");
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
    public static void main(String[] args){
        Task task = new Task();
        send(task);
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

