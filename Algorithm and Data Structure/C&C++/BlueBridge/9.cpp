#include <stdio.h>
#include <string.h>
int main()
{
	
	int a[1000][1000];
	int i,j,m,n,k;
	memset(a,'.',sizeof(a));
	scanf("%d%d",&m,&n);
	if(!(m>0 && n>m)) return 0;
	k=n+m-1;
	for(i=0;i<=n/2;i++)
		for(j=0;j<=k/2;j++)
			if(j>=i &&j<i+m) 
			{
				a[i][j]='*'; 
				a[i][k-j-1]=a[i][j];
			}
    for(i=n/2+1;i<n;i++)
    	for(j=0;j<k;j++)
    		a[i][j]=a[n-i-1][k-j-1];
	for(i=0;i<n;i++)
	{
		for(j=0;j<k;j++)
			printf("%c",a[i][j]);
		putchar('\n');
	}	
	return 0;
}
