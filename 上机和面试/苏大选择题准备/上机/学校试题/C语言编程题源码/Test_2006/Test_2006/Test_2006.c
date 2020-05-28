#include<stdio.h>
#include<stdlib.h>

int check(int n)
{
	int i;
	if(n==0||n==1) return 0;
	for(i=2;i<=n/2;++i)
	{
		if(n%i==0) 
			return 0;
	}
	if(i>n/2)
		return 1;
}

int check_9(int n)
{
	while(n)
	{
		if(n%10==9)
			return 0;
		n/=10;
	}
	return 1;
}

void get_su(int a[],int *n)
{
	int i,j;
	j=0;
	for(i=100;i<1000;i++)
	{
		if(check(i)&&check_9(i))
			a[j]=i,++j;
	}
	*n=j;
}

void write(int a[],int n)
{
	FILE *write;
	int i;
	if((write=fopen("G:\\file_2006.txt","w+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
		exit(0);
	}
	for(i=0;i<n;++i)
	{
		fprintf(write,"%d",a[i]);
		fprintf(write,"%s  "," ");
		if((i+1)%20==0)
			fprintf(write,"%s  ","\n");
	}
}

int main()
{
	int data[1000],count;
	get_su(data,&count);
	write(data,count);
	system("pause");
	return 0;
}