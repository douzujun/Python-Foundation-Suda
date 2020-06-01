#include<stdio.h>
#include<stdlib.h>

int check(int n)
{
	int i;
	if(n==0||n==1) return 0;
	for(i=2;i<=n/2;++i)
	{
		if(n%i==0) return 0;
	}
	if(i>n/2) return 1;
}

int dao(int n)
{
	int k=0;
	while(n)
	{
		k=k*10+n%10;
		n/=10;
	}
	return k;
}
void write()
{
	FILE *write;
	int i,k;
	if((write=fopen("G:\\file_2007.txt","w+"))==NULL)
	{
		printf("The file could'n be openned!\n");
		system("pause");
		exit(0);
	}
	for(i=10,k=1;i<1000;++i)
	{
		if(check(i)&&check(dao(i)))
		{
			fprintf(write," %d  ",i),++k;
			if(k%20==0)
			{	fprintf(write,"%c",'\n');}
		}
	}
	fclose(write);
	
}

int main()
{
	write();
	system("pause");
	return 0;
}