#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <sys/socket.h>

#define BUF_SIZE 40

int main(){
    int server_sock = socket(AF_INET, SOCK_STREAM, 0);

    //向服务器（特定的IP和端口）发起请求
    struct sockaddr_in sockAddr;

    memset(&sockAddr, 0, sizeof(sockAddr));  //每个字节都用0填充
    sockAddr.sin_family = AF_INET;  //使用IPv4地址
    sockAddr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
    sockAddr.sin_port = htons(1234);  //端口

    //bind(server_sock, (struct sockaddr*)&sockAddr, sizeof(sockAddr));
    //listen(server_sock, 20);

    //读取服务器传回的数据
    char buffer_send[40];
    char buffer_recv[40];

    while(true){
        //创建套接字
        int sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
        connect(sock, (struct sockaddr*)&sockAddr, sizeof(sockAddr));

        //获取用户输入的字符串并发送给服务器
        printf("Input a string: ");
        fgets(buffer_send, sizeof(buffer_send) / sizeof(buffer_send[0]), stdin);
        write(sock, buffer_send, strlen(buffer_send));
        //接收服务器传回的数据
        read(sock, buffer_recv, BUF_SIZE);
        char bufferRecvBinary[100];
        //read(bufferRecvBinary, buffer_recv, sock, , BUF_SIZE);
        //输出接收到的数据
        printf("Message form server: %s\n", buffer_recv);

        memset(buffer_send, 0, BUF_SIZE);  //重置缓冲区
        memset(buffer_recv, 0, BUF_SIZE);  //重置缓冲区
        close(sock);  //关闭套接字
    }

    return 0;
}