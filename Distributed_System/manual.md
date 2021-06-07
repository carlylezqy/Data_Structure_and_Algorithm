

[参考资料](http://c.biancheng.net/cpp/html/3030.html)

#### sockaddr_in 结构体(专门用来保存 IPv4 地址的结构体)

```C++
struct sockaddr_in{
    sa_family_t    sin_family;      //地址族（Address Family），也就是地址类型
    uint16_t       sin_port;        //16位的端口号
    struct in_addr sin_addr;        //32位IP地址
    char           sin_zero[8];     //不使用，一般用0填充
};
```

1. `sin_family` 和 socket() 的第一个参数的含义相同，取值也要保持一致，=AF_INET。

2. `sin_prot` 为端口号。uint16_t 的长度为两个字节，理论上端口号的取值范围为 0~65536，但 0~1023 的端口一般由系统分配给特定的服务程序。
	例如 Web 服务的端口号为 80，FTP 服务的端口号为 21，所以我们的程序要尽量在 1024~65536 之间分配端口号。端口号需要用 htons() 函数转换，后面会讲解为什么。

3. `sin_addr` 是 struct in_addr 结构体类型的变量，下面会详细讲解。

4. `sin_zero[8]` 是多余的8个字节，没有用，一般使用 memset() 函数填充为 0。上面的代码中，先用 memset() 将结构体的全部字节填充为 0，再给前3个成员赋值，剩下的 sin_zero 自然就是 0 了。



sockaddr_in6 (用来保存 IPv6 地址)

```C++
struct sockaddr_in6 { 
    sa_family_t sin6_family;    //(2)地址类型，取值为AF_INET6
    in_port_t sin6_port;        //(2)16位端口号
    uint32_t sin6_flowinfo;     //(4)IPv6流信息
    struct in6_addr sin6_addr;  //(4)具体的IPv6地址
    uint32_t sin6_scope_id;     //(4)接口范围ID
};
```



#### in_addr 结构体

sockaddr_in 的第3个成员是 in_addr 类型的结构体，该结构体只包含一个成员，如下所示：

```c++
struct in_addr{
	in_addr_t  s_addr;  //32位的IP地址
};
```

in_addr_t 在头文件 <netinet/in.h> 中定义，等价于 unsigned long，长度为4个字节。也就是说，s_addr 是一个整数，而IP地址是一个字符串，所以需要 inet_addr() 函数进行转换，例如：

```c++
unsigned long ip = inet_addr("127.0.0.1");
printf("%ld\n", ip);
```

运行结果：

```
16777343
```

```C++
struct sockaddr_in serv_addr;
memset(&serv_addr, 0, sizeof(serv_addr));            //每个字节都用0填充
serv_addr.sin_family      = AF_INET;                 //使用IPv4地址
serv_addr.sin_addr.s_addr = inet_addr("127.0.0.1");  //具体的IP地址
serv_addr.sin_port        = htons(1234);             //端口
```

#### sockaddr 结构体

```C++
struct sockaddr{
    sa_family_t  sin_family;   //地址族（Address Family），也就是地址类型
    char         sa_data[14];  //IP地址和端口号
};
```

## 协议（Protocol）

协议（Protocol）就是网络通信的约定，通信的双方必须都遵守才能正常收发数据。协议有很多种，例如 TCP、UDP、IP 等，通信的双方必须使用同一协议才能通信。协议是一种规范，由计算机组织制定，规定了很多细节，例如，如何建立连接，如何相互识别等。

**协议族**（Protocol Family）：就是一组协议（多个协议）的统称。最常用的是 TCP/IP 协议族，它包含了 TCP、IP、UDP、Telnet、FTP、SMTP 等上百个互为关联的协议，由于 TCP、IP 是两种常用的底层协议，所以把它们统称为 TCP/IP 协议族。

2. 



**void \*memset(void \*str, int c, size_t n)**
使用字符c掩盖指针str所指向字符串的前n个字符，并输出其余字符串。



```c++
int serv_sock = socket(AF_INET, SOCK_STREAM, IPPROTO_TCP);
```

**1、**Af 为地址族（Address Family）也就是 IP 地址类型，常用的有 AF_INET 和 AF_INET6。
INET是“Inetnet”的简写。AF_INET 表示 IPv4 地址；AF_INET6 表示 IPv6 地址。
你也可以使用PF前缀，PF是(Protocol Family)的简写，它和AF是一样的。例如，PF_INET 等价于 AF_INET，PF_INET6 等价于 AF_INET6。

**2、数据传输方式**：计算机之间有很多数据传输方式，各有优缺点，常用的有两种：SOCK_STREAM 和 SOCK_DGRAM。

1. SOCK_STREAM 表示面向连接的数据传输方式。数据可以准确无误地到达另一台计算机，如果损坏或丢失，可以重新发送，但效率相对较慢。常见的 http 协议就使用 SOCK_STREAM 传输数据，因为要确保数据的正确性，否则网页不能正常解析。
2. SOCK_DGRAM 表示无连接的数据传输方式。计算机只管传输数据，不作数据校验，如果数据在传输中损坏，或者没有到达另一台计算机，是没有办法补救的。也就是说，数据错了就错了，无法重传。因为 SOCK_DGRAM 所做的校验工作少，所以效率比 SOCK_STREAM 高。

3、

### bind()函数

```C++
bind(serv_sock, (struct sockaddr*)&serv_addr, sizeof(serv_addr));
```

**bind() 第二个参数的类型为 sockaddr，而代码中却使用 sockaddr_in，然后再强制转换为 sockaddr，这是为什么呢？**

sockaddr 和 sockaddr_in 的长度相同，都是16字节，只是将IP地址和端口号合并到一起，用一个成员 sa_data 表示。要想给 sa_data 赋值，必须同时指明IP地址和端口号，例如”127.0.0.1:80“，遗憾的是，没有相关函数将这个字符串转换成需要的形式，也就很难给 sockaddr 类型的变量赋值，所以使用 sockaddr_in 来代替。这两个结构体的长度相同，强制转换类型时不会丢失字节，也没有多余的字节。

可以认为，sockaddr 是一种通用的结构体，可以用来保存多种类型的IP地址和端口号，而 sockaddr_in 是专门用来保存 IPv4 地址的结构体。另外还有 sockaddr_in6，用来保存 IPv6 地址。

正是由于通用结构体 sockaddr 使用不便，才针对不同的地址类型定义了不同的结构体。

| sockaddr | sockaddr_in | sockaddr_in6 |
| ----------------- | -------------- | ----------------- |
| sin_family(2)     | sin_family(2)  | sin6_family(2) |
| sa_data(14) | sin_port(2) | sin6_port(2) |
| - | sin_addr(4) | sin6_flowinfo(4) |
| - | - | - |
| - | sin_zero(8) | sin6_addr(4) |
| - | - | - |
| - | - | sin6_scope_id(4) |
| - | - | - |



### connect()函数

与bind基本相同



### listen()

```c++
int listen(int sock, int backlog);     //Linux
int listen(SOCKET sock, int backlog);  //Windows
```

对于服务器端程序，使用 bind() 绑定套接字后，还需要使用 listen() 函数让套接字进入<u>被动监听</u>状态，再调用 accept() 函数，就可以随时响应客户端的请求了。

<u>被动监听</u>：指当没有客户端请求时，套接字处于“睡眠”状态，只有当接收到客户端请求时，套接字才会被“唤醒”来响应请求的状态。

`sock` 指需要进入监听状态的套接字，`backlog` 指<u>请求队列</u>的最大长度。

<u>请求队列</u>（Request Queue）：当套接字正在处理客户端请求时，如果有新的请求进来，套接字是没法处理的，只能把它放进缓冲区，待当前请求处理完毕后，再从缓冲区中读取出来处理。如果不断有新的请求进来，它们就按照先后顺序在缓冲区中排队，直到缓冲区满。这个缓冲区，就称为请求队列。

缓冲区的长度（能存放多少个客户端请求）可以通过 listen() 函数的 backlog 参数指定，但究竟为多少并没有什么标准，可以根据你的需求来定，并发量小的话可以是10或者20。

如果将 `backlog` 的值设置为 `SOMAXCONN`，就由系统来决定请求队列长度，这个值一般比较大，可能是几百，或者更多。

当请求队列满时，就不再接收新的请求，对于 Linux，客户端会收到 ECONNREFUSED 错误，对于 Windows，客户端会收到 WSAECONNREFUSED 错误。

注意：listen() 只是让套接字处于监听状态，并没有接收请求。接收请求需要使用 accept() 函数。



### accept() 函数

当套接字处于监听状态时，可以通过 accept() 函数来接收客户端请求。它的原型为：

```C++
int accept(int sock, struct sockaddr *addr, socklen_t *addrlen);  //Linux
SOCKET accept(SOCKET sock, struct sockaddr *addr, int *addrlen);  //Windows
```

它的参数与 listen() 和 connect() 是相同的：sock 为服务器端套接字，addr 为 sockaddr_in 结构体变量，addrlen 为参数 addr 的长度，可由 sizeof() 求得。

accept() 返回一个新的套接字来和客户端通信，addr 保存了客户端的IP地址和端口号，而 sock 是服务器端的套接字，大家注意区分。后面和客户端通信时，要使用这个新生成的套接字，而不是原来服务器端的套接字。

最后需要说明的是：listen() 只是让套接字进入监听状态，并没有真正接收客户端请求，listen() 后面的代码会继续执行，直到遇到 accept()。accept() 会阻塞程序执行（后面代码不能被执行），直到有新的请求到来。

### write()函数

Linux 不区分套接字文件和普通文件，使用 write() 可以向套接字中写入数据，使用 read() 可以从套接字中读取数据。

write() 的原型为：

```C++
ssize_t write(int fd, const void *buf, size_t nbytes);
```

fd 为要写入的文件的描述符，buf 为要写入的数据的缓冲区地址，nbytes 为要写入的数据的字节数。

> size_t 是通过 typedef 声明的 unsigned int 类型；
>
> ssize_t 在 "size_t" 前面加了一个"s"，代表 signed，即 ssize_t 是通过 typedef 声明的 signed int 类型。

write() 函数会将缓冲区 buf 中的 nbytes 个字节写入文件 fd，成功则返回写入的字节数，失败则返回 -1。

read() 的原型为：

```C++
ssize_t read(int fd, void *buf, size_t nbytes);
```

fd 为要读取的文件的描述符，buf 为要接收数据的缓冲区地址，nbytes 为要读取的数据的字节数。

read() 函数会从 fd 文件中读取 nbytes 个字节并保存到缓冲区 buf，成功则返回读取到的字节数（但遇到文件结尾则返回0），失败则返回 -1。



