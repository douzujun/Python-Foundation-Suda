#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void read(char num[][10],int *count)
{
	FILE *read;
	char ch;
	int i;
	if((read=fopen("G:\\file_2009_r.txt","r+"))==NULL)
	{
		printf("The file could be openned £¡\n");
		system("pause");
		exit(0);
	}
	*count=0;
	ch=fgetc(read);
	while(!feof(read))
	{
		i=0;
		while(ch!=','&&!feof(read))
		{
			num[*count][i]=ch;
			++i;
			ch=fgetc(read);
		}
		num[*count][i]='\0';
		++*count;
		ch=fgetc(read);
		while(ch==','&&!feof(read))
			ch=fgetc(read);
	}
}
void del_b(char num[][10],int *count,char num1[][10])
{
	int i,j,k;
	for(i=0;i<*count;++i)
	{
		for(j=0,k=0;num[i][j]!='\0';++j)
			if(num[i][j]!=' ')
				num1[i][k]=num[i][j],++k;
		num1[i][k]='\0';
	}

	for(i=0;i<*count;++i)
	{
		printf("%s\n",num1[i]);
	}
}

int e_t_o(char num[])
{
	int data=0;
	int i=0;
	while(num[i]!='\0')
	{
		data=data*8+num[i]-'0';
		++i;
	}
	return data;
}
void turn(char num1[][10],int *count,int data[])
{
	int i;
	for(i=0;i<*count;++i)
	{
		if(num1[i][0]!='0')
			data[i]=atoi(num1[i]);
		else
			data[i]=e_t_o(num1[i]);
	}
	for(i=0;i<*count;++i)
	{
		printf("%d\n",data[i]);
	}
}
void sort(int data[],int n)
{
	int i,j,t;
	for(i=0;i<n-1;++i)
	{
		for(j=0;j<n-1-i;++j)
			if(data[j]<data[j+1])
				t=data[j],data[j]=data[j+1],data[j+1]=t;
	}
	for(i=0;i<n;++i)
	{
		printf("%d\n",data[i]);
	}
}
void write(int data[],int n)
{
	int i;
	FILE *write;
	if((write=fopen("G:\\file_2009_w.txt","w+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
	}
	for(i=0;i<n;++i)
	{
		fprintf(write,"%d\n",data[i]);
	}
}

int main()
{
	char num[10][10],num1[10][10];
	int data[10];
	int count;
	read(num,&count);
	del_b(num,&count,num1);
	turn(num1,&count,data);
	sort(data,count);
	write(data,count);
	system("pause");
	return 0;
}