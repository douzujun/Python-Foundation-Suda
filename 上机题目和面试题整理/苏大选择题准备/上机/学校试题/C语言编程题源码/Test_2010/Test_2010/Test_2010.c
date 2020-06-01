#include<stdio.h>
#include<stdlib.h>
void write()
{
	FILE *write;
	int data[]={1,2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
	int n=sizeof(data)/4;
	int i;
	if((write=fopen("G:\\file_2010.txt","wb+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
		exit(0);
	}
	for(i=0;i<n;++i)
	{
		//printf("%d ",data[i]);
		fwrite(&data[i],4,1,write);
	}
	fclose(write);
}
void read(int all[],int *count_all)
{
	FILE *read;
	int i;
	int data;
	if((read=fopen("G:\\file_2010.txt","rb+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
		exit(0);
	}
	*count_all=0;
	while(!feof(read))
	{

		//fscanf(read,"%d",&data);
		fread(&data,4,1,read);
		//printf("%d ",data);
		if(data!=0)
		{
			all[*count_all]=data;
			++*count_all;
		}
	}
	//for(i=0;i<*count_all;++i)
	//{
	//	printf("%d\n",all[i]);
	//}
}
int check_su(int n)
{
	int i;
	if(n<2) return 0;
	for(i=2;i<=n/2;++i)
	{
		if(n%i==0) return 0;
	}
	if(i>n/2) return 1;
}
void get_su(int all[],int su[],int count_all,int *count_su)
{
	int i,j;
	for(i=0,j=0;i<count_all;++i)
		if(check_su(all[i]))
			su[j]=all[i],++j;
	*count_su=j;
}

void sort(int data[],int n)
{
	int i,j,t;
	for(i=0;i<n-1;++i)
		for(j=0;j<n-1-i;++j)
		{
			if(data[j]>data[j+1])
				t=data[j],data[j]=data[j+1],data[j+1]=t;
		}
	//for(i=0;i<n;++i)
	//{
	//	printf("%d\n",data[i]);
	//}
}
int main()
{
	int all[2048],su[2048];
	int count_all,count_su;
	int max,min;
	int mid_max,mid_min;
	int max_su;
	write();
	read(all,&count_all);
	get_su(all,su,count_all,&count_su);
	sort(all,count_all);
	max=all[count_all-1];
	min=all[0];
	sort(su,count_su);
	max_su=su[count_su-1];
	mid_max=all[count_all/3*2-1];
	mid_min=all[count_all/3];
	printf("Max number is : %d \n",max);
	printf("Min number is : %d \n",min);
	printf("Max_su number is : %d \n",max_su);
	printf("Mid_max number is : %d \n",mid_max);
	printf("Mid_min number is : %d \n",mid_min);
	system("pause");
	return 0;
}