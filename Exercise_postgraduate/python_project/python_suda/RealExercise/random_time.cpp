#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <cmath>
#include <ctime>
#include <fstream>
using namespace std;

int main()
{
	const int maxn = 100;
	int num[] = {8,6,2,25,5,2,3,9,1,10,34,12,45,83,102,7,5,13,79,0,0,0,0,0,0,0,0,0,0,0,0,0};
//	for (int i = 0; i < 16; i++)
//	{
//		num[i] = rand();
//	}
	
	FILE *fp = fopen("./file/test.bat", "wb");
	if (fp == NULL)
	{
		printf("failure!");
	}
	
	for (int i = 0; i < 32; i++)
	{
		fwrite(&num[i], sizeof(int), 1, fp);
	}
	
	fclose(fp);	
		
	
	FILE *read = fopen("./file/test.bat", "rb");
	if (read == NULL) {
		printf("failure read!");
	}
	
	int pnum = 0;
	while (fread(&pnum, sizeof(int), 1, read) > 0)
	{
		cout << pnum << endl;	
	}
	
	fclose(read);
	
	return 0;
	
}









