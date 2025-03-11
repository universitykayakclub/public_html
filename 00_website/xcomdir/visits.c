#include <stdio.h>
#include <strings.h>

#define MAXCHAR 10000	  /*This is the Maximum File Length 
						  or at least the length of the piece read*/

int	printAfile(const char *afilestr);

int printafile(const char *afilestr)
{
	FILE *fp;
	int	i = 0;
	char c;
	
	fp = fopen(afilestr,"r");
	while ( (c = getc(fp)) != EOF && i < MAXCHAR-1)  {
		putchar(c);
		i++;
	}
	fclose(fp);
	
	return(i);
}

int main()
{
	char time[30];

	printf("Content-type: text/html\n\n");
	printf("<html>\n<head>\n<TITLE>UKC Visitors</TITLE>\n</head>\n\n");	
	printf("<BODY BACKGROUND=\"http://students.washington.edu/~ukc/bits/swirl.gif\" TEXT=\"#000000\" link=\"0022dd\" vlink=\"#660099\">\n\n");	
	printf("<H1>The Last Few UKC Visitors</H1>\n<p>\n");	
	printf("Consecutive hits from the same site are not counted.<hr>\n");	
	
	printafile("/dw00/d18/ukc/main/yakker.dat");

	printf("<hr>\n</BODY>\n</html>");	
	fflush(stdout);
}



