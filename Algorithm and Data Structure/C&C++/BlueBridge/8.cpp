#include <stdio.h>
int main()
{
	int n,t=0,sum;
	scanf("%d",&n);
	sum=n;
	while(n>0)
	{
		t=n%3;
		sum+=(t+n)/3;
		n/=3;
	}
	printf("%d",sum);
	return 0;
}
