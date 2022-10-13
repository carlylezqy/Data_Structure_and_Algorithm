#include <stdio.h>
#include <string.h>
int f(char s[], int begin, int end)
{
	int mid;
	if(end-begin==1) return s[begin] - '0';
	mid = (end+begin) / 2;
	return f(s,begin+1,mid)+f(s,mid,end-1);  //ÃÓø’
}
	
int main()
{
	char s[] = "4725873285783245723";
	printf("%d\n",f(s,0,strlen(s)));
	return 0;
}
