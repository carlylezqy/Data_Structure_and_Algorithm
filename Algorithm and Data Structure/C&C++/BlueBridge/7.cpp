#include <stdio.h>
int sum(int *a,int *s);
int sum(int *a,int *s)
{
	int i,sum=a[0];
	for(i=0;i<48;i++)
		if(s[i])
		{
			sum-=a[i-1];
			sum+=a[i-1]*a[i];
		}	
		else
			sum+=a[i+1];
	return sum;
}
int add(int *s)
{
	int i,sum=0;
	for(i=0;i<48;i++)
	sum+=s[i];
	return sum;
}
int main()
{
	int a[49]={0},s[48]={0};
	int i,j;
	for(i=1;i<50;i++)
		a[i-1]=i;
	while(!(sum(a,s)==2015 && add(s)==2))
		for(i=0;i<48;i++)
		{
			s[0]++;
			if(i=0;i<)
		}	
	for(i=0;i<48;i++)
	{
		printf("%d\n",s[i]);
	}
	
	for(i=0;i<48;i++)
	{
		if(s[i]) printf("*%d",a[i+1]);
		else printf("+%d",a[i+1]);
	}
}
