#include<stdio.h>
int judge(int *a)
{
	int i,v[10]={0};
	for(i=0;i<8;i++)
		v[a[i]%10]++;
	for(i=0;i<10;i++)
	if(v[i]>1) return 0;
	return 1;
}
int main()
{
	int a[8];
	int m,n,p;
	for(a[0]=1;a[0]<=9;a[0]++)
	for(a[1]=0;a[1]<=9;a[1]++)
	for(a[2]=0;a[2]<=9;a[2]++)
	for(a[3]=1;a[3]<=9;a[3]++)
	for(a[4]=0;a[4]<=9;a[4]++)
	for(a[5]=0;a[5]<=9;a[5]++)
	for(a[6]=0;a[6]<=9;a[6]++)
	for(a[7]=0;a[7]<=9;a[7]++)
	{
		m=a[0]*1000+a[6]*100+a[1]*10+a[2];
		n=a[3]*1000+a[4]*100+a[5]*10+a[6];
		p=a[3]*10000+a[4]*1000+a[5]*100+a[6]*10+a[7];
		if(m+n==p && judge(a)) printf("%d+%d=%d\n",m,n,p);
	}
		
	return 0;
}
