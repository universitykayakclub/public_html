#include <stdio.h>
#include <stdlib.h>
#include <strings.h>
#include <time.h>

int strScan(const char *str1,const char *str2, char *str3);
int fixAscii(char *str);
int htoi(char *s);
long theDate(char *str);
void cleanStr(char *astr);

#define MAXCHAR 10000	/*Max Length of an individual record*/

main()
{
	char istr[MAXCHAR];		/*Used as an input string*/
	int c;				/*Dummy character for file copy*/
	int i, n;			/*Dummy Variables*/

	FILE *fp;
	char s1[50];			/*Dummy string*/
	int newm,month,day,year;
	
/*Reading and Parsing Data*/	
	if (getenv("CONTENT_LENGTH"))
		n = atoi(getenv("CONTENT_LENGTH"));
	for (i=0; (i<n) && (i<MAXCHAR-2) ; i++)
		istr[i] = getchar();
	
	istr[i++] = '&';
	istr[i] = '\0';
	
	strScan(istr,"new",s1);
	sscanf(s1,"%d",&newm);
	if (newm <1 || newm >100)
		newm = 0;
	    
	strScan(istr,"month",s1);
	sscanf(s1,"%d",&month);
	if (month <1 || month >12)
		month = 0;  

	strScan(istr,"day",s1);
	sscanf(s1,"%d",&day);
	if (day <1 || day >31)
		month = 0;
	    
	strScan(istr,"year",s1);
	sscanf(s1,"%d",&year);
	if (year <1998 || year >2100)
		year = 0;       	    
	
	fflush(stdout);
	
	printf("Content-type: text/html\n\n");	
	
	fflush(stdout);
	
	printf("<HTML><HEAD><TITLE>names</TITLE></HEAD>");
	printf("<BODY>\n");
	
	printf("new members = %d<p>\n",newm);
	printf("date = %04d%02d%02d\n",year,month,day);	


	fflush(stdout);
}



/*This takes the *str1, the input from a form
				 *str2, the string name
	and puts the transferred string into *str3.
	It returns the converted string length or 0.*/

int strScan(const char *str1,const char *str2, char *str3)
{
	int i, n2, n3 = 0;
	n2 = strlen(str2);
	
	for (i = 0; i < strlen(str1); i++) {
		if (strncmp(str1+i,str2,n2)==0) {
			while (*(str1+i+n2+1+n3) != '&') {
				*(str3+n3)=*(str1+i+n2+1+n3++);
			}
			*(str3+n3) = '\0';
			fixAscii(str3);
			return(strlen(str3));
		}
	}
	return(0);
}


/*This takes a string with formatting characters and
converts to normal ascii.  The function returns the 
number of removed characters (2 per converted character)*/

int fixAscii(char *str)
{
	int n, i, j=0;
	
	n = strlen(str);
        
	for (i = 0; i < n-j; i++) {
	
		switch (*(str+i+j))	{
			
			case '+':
				*(str+i) = ' ';
				break;

			case '%':
				{
					char s[3];
					s[0] = *(str+i+j+1);
					s[1] = *(str+i+j+2);
					s[2] = 0;
					*(str+i) = htoi(s);
					j += 2;
				}
				break;
				
			default:
				 *(str+i) = *(str+i+j);
			}
	}
		
	*(str+i)='\0';
	return(j); 
}


/*This converts a hex string to int */

int htoi(char *s)
{
	char *digits = "0123456789ABCDEF";

	if (islower(s[0])) s[0] = toupper(s[0]);
	if (islower(s[1])) s[1] = toupper(s[1]);

	return 16 * (strchr(digits, s[0]) - strchr(digits, '0')) 
        + (strchr(digits, s[1]) - strchr(digits, '0'));
}

long theDate(char *str)
{
	struct tm *ltime;
	time_t now;
	long tsec=0;
	
	time(&now);
	ltime = localtime(&now);
	sprintf(str, "%02d/%02d/%02d\0", 
		ltime->tm_mon+1, ltime->tm_mday, ltime->tm_year);

	tsec += ltime->tm_sec+60*ltime->tm_min+3600*ltime->tm_hour;
	tsec += 86400*ltime->tm_yday+31536000*(ltime->tm_year-96);
	return (tsec);
}

/*This strips off initial and final white space from a string*/
void cleanStr(char *astr)  
{
	char t1[MAXCHAR];
	int i;
	int n;
	
	i=0;
	while ( isspace(*(astr+i)) )
		i++;
	strcpy(t1,astr+i);
	strcpy(astr,t1);
	n = strlen(astr);
	for (i=0;i<n;i++)  {
	*(t1+i)=*(astr+n-i-1);
	}
	*(t1+i)='\0';
	strcpy(astr,t1);
	
	i=0;
	while ( isspace(*(astr+i)) )
		i++;
	strcpy(t1,astr+i);
	strcpy(astr,t1);
	n = strlen(astr);
	for (i=0;i<n;i++)  {
	*(t1+i)=*(astr+n-i-1);
	}
	*(t1+i)='\0';
	strcpy(astr,t1);
}
