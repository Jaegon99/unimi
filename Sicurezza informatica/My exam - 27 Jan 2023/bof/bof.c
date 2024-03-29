#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdint.h>

int security_check = 0 ;

int disable_security_check() {
security_check = 0 ;
}
int enable_security_check() {return 1;}


void print_function(char *src){

        int canary;
        char dst[120] ;

	int x = rand() ;
		
	printf("\n\ncanary: %p\n", &canary);
	printf("dst: %d\n", dst);
	printf("x: %d\n\n", x);

	canary = x ;
	printf("dst is at %08x, now checking security\n", &dst);
        if (security_check)
	{
               strncpy(dst, src, 119);
	       dst[120] ='\0' ;
	       printf("%s\n", dst) ;	
	}

     else
	{
                strcpy(dst, src);
		printf("canary is: %d\n", canary);
		printf("x is: %d\n\n", x);
		
		if (canary != x) exit(0) ;
		else printf("Canary is correct\n");
	}

}



int main(int argc, char *argv[]){

 
 int (*fp)() = NULL;
 char str[270] ;
 short check =0; 
 int i ;
 char index = 0;

	printf("\n fp:%p",&fp);       
 	printf("\n str:%p",str);       
 	printf("\n check:%p",&check);       
 	printf("\n i:%p",&i);       
 	printf("\n index:%p",&index);     

	security_check = enable_security_check() ;

	for(i = 0; i < 282; i++) {
	  str[i] = getchar();
	  if(str[i] == 10) break;
	}
	str[i] = 0;
	
	if (fp != NULL){
					printf("%p\n", fp) ;
	       	fp() ;
		printf("Security Check:%d\n", security_check) ;
	}

	/* print function name */
	print_function(str) ;

 	printf("Never return from main\n") ;	
	exit(0) ;
}
