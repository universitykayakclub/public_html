/* kdebug.c: HTML forms parsing program

   started with (C) Copyright Sky Coyote, 1995.
   Modified by Kelly Bruland
   
   compile with:  cc -o kdebug.cgi kdebug.c
                  chmod 701 kdebug.cgi  */

#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <strings.h>
#define MAXC 10000
#define LW 60

int htoi(char *);

main()
{
	int i, j, n;
	char c, istr[MAXC];


	printf("Content-type: text/plain\n\n");

	n = 0;
	if (getenv("CONTENT_LENGTH"))
		n = atoi(getenv("CONTENT_LENGTH"));

	j = 0;    
	for (i = 0; (i < n) && (i < MAXC) ; i ++)
	{
		j++;
		
		if (j == LW)
		{
			j = 0;
			putchar('\n');
		}
		
		istr[i] = getchar();
		putchar(istr[i]);
	}
	
	putchar('\n');
	putchar('\n');

	for (i = 0; (i < n) && (i < MAXC) ; i ++)	
		{
		int is_eq = 0;
        
		c = istr[i];
        
		switch (c)
			{
			case '&':
				c = '\n';
				break;

			case '+':
				c = ' ';
				break;
             
			case '%':
				{
				char s[3];
				s[0] = istr[++i];
				s[1] = istr[++i];
				s[2] = 0;
				c = htoi(s);
				}
				break;

			case '=':
				c = ':';
				is_eq = 1;
				break;
          	}
        
		putchar(c);

		if (is_eq) putchar(' ');
		}
        
	putchar('\n');
	putchar('\n');


	if (getenv("AUTH_TYPE"))
		printf("AUTH_TYPE = %s\n",getenv("AUTH_TYPE"));
		
	if (getenv("CONTENT_LENGTH"))
		printf("CONTENT_LENGTH = %s\n",getenv("CONTENT_LENGTH"));

	if (getenv("CONTENT_TYPE"))
		printf("CONTENT_TYPE = %s\n",getenv("CONTENT_TYPE"));		
					
	if (getenv("DOCUMENT_ROOT"))
		printf("DOCUMENT_ROOT = %s\n",getenv("DOCUMENT_ROOT"));
	
	if (getenv("GATEWAY_INTERFACE"))
		printf("GATEWAY_INTERFACE = %s\n",getenv("GATEWAY_INTERFACE"));		

	if (getenv("HTTP_ACCEPT"))
		printf("HTTP_ACCEPT = %s\n",getenv("HTTP_ACCEPT"));

	if (getenv("HTTP_CONNECTION"))
		printf("HTTP_CONNECTION = %s\n",getenv("HTTP_CONNECTION"));

	if (getenv("HTTP_HOST"))
		printf("HTTP_HOST = %s\n",getenv("HTTP_HOST"));

	if (getenv("HTTP_REFERER"))
		printf("HTTP_REFERER = %s\n",getenv("HTTP_REFERER"));
		
	if (getenv("HTTP_USER_AGENT"))
		printf("HTTP_USER_AGENT = %s\n",getenv("HTTP_USER_AGENT"));

	if (getenv("PATH"))
		printf("PATH = %s\n",getenv("PATH"));
		
	if (getenv("PATH_INFO"))
		printf("PATH_INFO = %s\n",getenv("PATH_INFO"));

	if (getenv("PATH_TRANSLATED"))
		printf("PATH_TRANSLATED = %s\n",getenv("PATH_TRANSLATED"));

	if (getenv("REMOTE_ADDR"))
		printf("REMOTE_ADDR = %s\n",getenv("REMOTE_ADDR"));		

	if (getenv("REMOTE_HOST"))
		printf("REMOTE_HOST = %s\n",getenv("REMOTE_HOST"));		

	if (getenv("REMOTE_USER"))
		printf("REMOTE_USER = %s\n",getenv("REMOTE_USER"));
		
	if (getenv("REQUEST_METHOD"))
		printf("REQUEST_METHOD = %s\n",getenv("REQUEST_METHOD"));		

	if (getenv("SCRIPT_FILENAME"))
		printf("SCRIPT_FILENAME = %s\n",getenv("SCRIPT_FILENAME"));		

	if (getenv("SCRIPT_NAME"))
		printf("SCRIPT_NAME = %s\n",getenv("SCRIPT_NAME"));		

	if (getenv("SERVER_ADMIN"))
		printf("SERVER_ADMIN = %s\n",getenv("SERVER_ADMIN"));		

	if (getenv("SERVER_NAME"))
		printf("SERVER_NAME = %s\n",getenv("SERVER_NAME"));		

	if (getenv("SERVER_PORT"))
		printf("SERVER_PORT = %s\n",getenv("SERVER_PORT"));		

	if (getenv("SERVER_PROTOCOL"))
		printf("SERVER_PROTOCOL = %s\n",getenv("SERVER_PROTOCOL"));		

	if (getenv("SERVER_SOFTWARE"))
		printf("SERVER_SOFTWARE = %s\n",getenv("SERVER_SOFTWARE"));		

	if (getenv("QUERY_STRING"))
		printf("QUERY_STRING = %s\n",getenv("QUERY_STRING"));		

	fflush(stdout);
}





/* convert hex string to int */

int htoi(char *s)
{
	char *digits = "0123456789ABCDEF";

	if (islower(s[0])) s[0] = toupper(s[0]);
	if (islower(s[1])) s[1] = toupper(s[1]);

	return 16 * (strchr(digits, s[0]) - strchr(digits, '0')) 
		+ (strchr(digits, s[1]) - strchr(digits, '0'));
}
