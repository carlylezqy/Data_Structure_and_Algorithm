
#include "stdafx.h"
#include <iostream>
using namespace std;


class Fibonacci{

	public:
		int num;
		int fib(int n){
			if(n<=0) num=0;
			else if(n==1) num=1;
			else{
				num = fib(n-1)+fib(n-2);
			}
			return num;
		}
};


int _tmain(int argc, _TCHAR* argv[])
{
	Fibonacci fib1;
	int a = fib1.fib(10);
	cout<<a<<endl;
	return 0;
}

