//统计篇文章中各英文字母的个数

#include<stdio.h>
#include<stdlib.h>

typedef struct word
{
	char w;
	int time;
}word;

void read(char filename[],char all_w[],int *n)
{
	FILE *read;
	char a;
	int i;
	*n=0;
	if((read=fopen("G:\\file_2005.txt","r+"))==NULL)
	{
		printf("Couldn't open the file！\n");
		system("pause");
		exit(0);
	}
	while(!feof(read))
	{
		a=getc(read);
		if((a<='z'&&a>='a')||(a>='A'&&a<='Z'))
			all_w[*n]=a,++*n;
	}
	fclose(read);
}

int check(word w[],char a,int count)
{
	int i;
	for(i=0;i<count;++i)
	{
		if(w[i].w==a)
			return i+1;
	}
	return 0;
}

void del(word w[],char all_c[],int count_all,int *count)
{
	int i,j,k;
	*count=0;
	i=0,j=0,k=0;
	w[0].w=all_c[i];
	w[0].time=1;
	++j;
	++*count;
	for(i=1;i<count_all;++i)
	{
		if(check(w,all_c[i],*count))
		{
			++(w[check(w,all_c[i],*count)-1].time);
		}
		else
		{
			w[j].w=all_c[i];
			w[j].time=1;
			++j;
			++*count;
		}
	}
	*count=j;
	printf("一共有字母 %d 个\n",count_all);
	printf("除去重复字母有 %d 个 \n",*count);
	for(i=0;i<*count;++i)
	{
		printf(" %c : %d \n",w[i].w,w[i].time);
	}
}

int main()
{
	char filename[20];
	char all_c[1000];
	word w[200];
	int count_all,count;
	//printf("Please enter the name of file: ");
	//scanf("%s",filename);
	read(filename,all_c,&count_all);
	del(w,all_c,count_all,&count);
	system("pause");
	return 0;
}