#include <stdio.h>
int judge(int i,int sam)
{
	while(i>0)
	{
		if(i%10!=sam%10) return 0;
		i/=10;
		sam/=10;
	}
	return 1;
}
int main()
{
	int i,n=0; 
	for(i=1;i<=10000;i++)
		if(judge(i,i*i*i))
		 {
		 	printf("%d,%d\n",i,i*i*i);
		 	n++;
		 }
	printf("%d",n);
	return 0;
}
