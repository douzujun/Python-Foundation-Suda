#include<stdio.h>
#include<stdlib.h>
#include<string.h>
void del_the(char all_word[][15],int *count)
{
	int i,j;
	for(i=0;i<*count;)
	{
		if(strcmp(all_word[i],"The")==0||strcmp(all_word[i],"the")==0)
		{
			for(j=i;j<*count-1;++j)
				strcpy(all_word[j],all_word[j+1]);
			--*count;
		}
		else
			++i;

	}
}

void a_t_A(char all_word[][15],int *count)
{
	int i;
	for(i=0;i<*count;++i)
	{
		if(all_word[i][0]>='a'&&all_word[i][0]<='z')
			all_word[i][0]-=32;
	}
	for(i=0;i<*count;++i)
	{
		printf("%s ",all_word[i]);
	}
	printf("%s","\n");
}

void del_same(char all_word[][15],int *count)
{
	int i,j,k;
	for(i=0;i<*count;++i)
	{
		for(j=i+1;j<*count;)
			if(strcmp(all_word[i],all_word[j])==0)
			{
				for(k=j;k<*count-1;++k)
					strcpy(all_word[k],all_word[k+1]);
				--*count;
			}
			else
				++j;
	}
}

void read(char all_word[][15],int *count)
{
	FILE *read;

	char word[15];
	char ch;
	int i;
	*count=0;
	if((read=fopen("G:\\file_2008.txt","r+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
		exit(0);
	}
	while(!feof(read))
	{
		fscanf(read,"%s",word);
		strcpy(all_word[*count],word);
		printf("%s ",word);
		++*count;
	}
	printf("\n");
	printf("%d\n",*count);
	fseek(read,-1,2);
	ch=fgetc(read);
	if(ch==' ')
		--*count;
	for(i=0;i<*count;++i)
		printf("%s ",all_word[i]);
	printf("%d\n",*count);
	fclose(read);
}
void write(char all_word[][15],int *count)
{
	FILE *write;
	int i;
	if((write=fopen("G:\\file_2008_w.txt","w+"))==NULL)
	{
		printf("The file couldn't be openned!\n");
		system("pause");
		exit(0);		
	}
	for(i=0;i<*count;++i)
	{
		fprintf(write,"%s",all_word[i]);
		if(!(i==*count-1))
			fprintf(write,"%c",'\n');
	}
}
int main()
{
	char all_word[100][15];
	int count_all;
	read(all_word,&count_all);
	del_the(all_word,&count_all);
	del_same(all_word,&count_all);
	a_t_A(all_word,&count_all);
	write(all_word,&count_all);
	system("pause");
	return 0;
}