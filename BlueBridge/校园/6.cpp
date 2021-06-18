#include <stdio.h>
int jugde(int n1,int n2)
{
	int i,v[10]={0},sum=0,p=0;
	while(n1>0)
	{
		v[n1%10]=1;
		n1/=10;
		p++;
	}
	while(n2>0)
	{
		v[n2%10]=1;
		n2/=10;
		p++;
	}
	for(i=0;i<10;i++)
	sum+=v[i];
	if(sum!=10) return 0;
	return 1;
}
int main()
{ 
	int i;
	for(i=0;;i++)
	if(jugde(i*i,i*i*i)) break;
	printf("%d %d %d",i,i*i,i*i*i);
	return 0;
}
