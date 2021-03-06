
## 1. 隔行变色

Excel表的格子很多，为了避免把某行的数据和相邻行混淆，可以采用隔行变色的样式。
小明设计的样式为：第1行蓝色，第2行白色，第3行蓝色，第4行白色，....
现在小明想知道，从第21行到第50行一共包含了多少个蓝色的行。

请你直接提交这个整数，千万不要填写任何多余的内容。

## 2.立方尾不变

有些数字的立方的末尾正好是该数字本身。
比如：1,4,5,6,9,24,25,....
请你计算一下，在10000以内的数字中（指该数字，并非它立方后的数值），符合这个特征的正整数一共有多少个。

请提交该整数，不要填写任何多余的内容。

## 3.三羊献瑞

观察下面的加法算式：

	      祥 瑞 生 辉
	  +   三 羊 献 瑞
	-------------------
	    三 羊 生 瑞 气

其中，相同的汉字代表相同的数字，不同的汉字代表不同的数字。
祥a 生b 辉c 三d 羊e 献f 瑞g
请你填写“三羊献瑞”所代表的4位数字（答案唯一），不要填写任何多余内容。


## 4.格子中输出

StringInGrid函数会在一个指定大小的格子中打印指定的字符串。
要求字符串在水平、垂直两个方向上都居中。
如果字符串太长，就截断。
如果不能恰好居中，可以稍稍偏左或者偏上一点。

下面的程序实现这个逻辑，请填写划线部分缺少的代码。

```C
#include <stdio.h>
#include <string.h>

void StringInGrid(int width, int height, const char* s)
{
	int i,k;
	char buf[1000];
	strcpy(buf, s);
	if(strlen(s)>width-2) buf[width-2]=0;

	printf("+");
	for(i=0;i<width-2;i++) printf("-");
	printf("+\n");

	for(k=1; k<(height-1)/2;k++){
		printf("|");
		for(i=0;i<width-2;i++) printf(" ");
		printf("|\n");
	}

	printf("|");

	printf("%*s%s%*s",_____________________________________________);  //填空

	printf("|\n");

	for(k=(height-1)/2+1; k<height-1; k++){
		printf("|");
		for(i=0;i<width-2;i++) printf(" ");
		printf("|\n");
	}	

	printf("+");
	for(i=0;i<width-2;i++) printf("-");
	printf("+\n");	
}

int main()
{
	StringInGrid(20,6,"abcd1234");
	return 0;
}
```

对于题目中数据，应该输出：　　

	+------------------+  
	|                  |  
	|     abcd1234     |  
	|                  |  
	|                  |  
	+------------------+  

注意：只填写缺少的内容，不要书写任何题面已有代码或说明性文字。　　


## 5.串逐位和

给定一个由数字组成的字符串，我们希望得到它的各个数位的和。
比如：“368” 的诸位和是：17
这本来很容易，但为了充分发挥计算机多核的优势，小明设计了如下的方案：

	int f(char s[], int begin, int end)
	{
		int mid;
		if(end-begin==1) return s[begin] - '0';
		mid = (end+begin) / 2;
		return ____________________________________;  //填空
	}
	
	int main()
	{
		char s[] = "4725873285783245723";
		printf("%d\n",f(s,0,strlen(s)));
		return 0;
	}

你能读懂他的思路吗？ 请填写划线部分缺失的代码。

注意：只填写缺少的部分，不要填写已有代码或任何多余内容。

## 6.奇妙的数字
小明发现了一个奇妙的数字。它的平方和立方正好把0~9的10个数字每个用且只用了一次。
你能猜出这个数字是多少吗？

请填写该数字，不要填写任何多余的内容。

## 7.加法变乘法
我们都知道：
	1+2+3+ ... + 49 = 1225
现在要求你把其中两个不相邻的加号变成乘号，使得结果为2015

比如：
	1+2+3+...+10\*11+12+...+27\*28+29+...+49 = 2015
就是符合要求的答案。

请你寻找另外一个可能的答案，并把位置靠前的那个乘号左边的数字提交（对于示例，就是提交10）。

注意：需要你提交的是一个整数，不要填写任何多余的内容。

## 8.饮料换购

乐羊羊饮料厂正在举办一次促销优惠活动。乐羊羊C型饮料，凭3个瓶盖可以再换一瓶C型饮料，并且可以一直循环下去(但不允许暂借或赊账)。

请你计算一下，如果小明不浪费瓶盖，尽量地参加活动，那么，对于他初始买入的n瓶饮料，最后他一共能喝到多少瓶饮料。

输入：一个整数n，表示开始购买的饮料数量（0<n<10000）
输出：一个整数，表示实际得到的饮料数

例如：
用户输入：100
程序应该输出：149

用户输入：101
程序应该输出：151

资源约定：
峰值内存消耗 < 256M
CPU消耗  < 1000ms

请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。
所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。
提交时，注意选择所期望的编译器类型。

## 9.打印大X

小明希望用星号拼凑，打印出一个大X，他要求能够控制笔画的宽度和整个字的高度。
为了便于比对空格，所有的空白位置都以句点符来代替。

要求输入两个整数m n，表示笔的宽度，X的高度。用空格分开(0<m<n, 3<n<1000, 保证n是奇数)
要求输出一个大X

例如，用户输入：3 7
程序应该输出：

	***.....***
	.***...***.
	..***.***..
	...*****...
	....***....
	...*****...
	..***.***..
	.***...***.
	***.....***

（如有对齐问题，参看【图1.jpg】）

再例如，用户输入：
4 21
程序应该输出

	****................****
	.****..............****.
	..****............****..
	...****..........****...
	....****........****....
	.....****......****.....
	......****....****......
	.......****..****.......
	........********........
	.........******.........
	..........****..........
	.........******.........
	........********........
	.......****..****.......
	......****....****......
	.....****......****.....
	....****........****....
	...****..........****...
	..****............****..
	.****..............****.
	****................****

资源约定：
峰值内存消耗 < 256M
CPU消耗  < 1000ms

请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。
所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。
提交时，注意选择所期望的编译器类型。

## 10.垒骰子
赌圣atm晚年迷恋上了垒骰子，就是把骰子一个垒在另一个上边，不能歪歪扭扭，要垒成方柱体。
经过长期观察，atm 发现了稳定骰子的奥秘：有些数字的面贴着会互相排斥！
我们先来规范一下骰子：1 的对面是 4，2 的对面是 5，3 的对面是 6。
假设有 m 组互斥现象，每组中的那两个数字的面紧贴在一起，骰子就不能稳定的垒起来。 
atm想计算一下有多少种不同的可能的垒骰子方式。
两种垒骰子方式相同，当且仅当这两种方式中对应高度的骰子的对应数字的朝向都相同。
由于方案数可能过多，请输出模 10^9 + 7 的结果。

不要小看了 atm 的骰子数量哦～

「输入格式」
第一行两个整数 n m
n表示骰子数目
接下来 m 行，每行两个整数 a b ，表示 a 和 b 数字不能紧贴在一起。

「输出格式」
一行一个数，表示答案模 10^9 + 7 的结果。

「样例输入」
2 1
1 2

「样例输出」
544

「数据范围」
对于 30% 的数据：n <= 5
对于 60% 的数据：n <= 100
对于 100% 的数据：0 < n <= 10^9, m <= 36

资源约定：
峰值内存消耗 < 256M
CPU消耗  < 2000ms

请严格按要求输出，不要画蛇添足地打印类似：“请您输入...” 的多余内容。
所有代码放在同一个源文件中，调试通过后，拷贝提交该源码。
注意: main函数需要返回0
注意: 只使用ANSI C/ANSI C++ 标准，不要调用依赖于编译环境或操作系统的特殊函数。
注意: 所有依赖的函数必须明确地在源文件中 #include <xxx>， 不能通过工程设置而省略常用头文件。
提交时，注意选择所期望的编译器类型。

