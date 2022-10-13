#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <ctype.h>
#include <string.h>
#include <pthread.h>

void* capitalize(void **str){
    char *t = (char *)*str;
    char *opt[strlen(t)+1];

    for(int i=0; t[i]!='\0'; i++){
        //opt[i] = toupper(p[i]);
        int ascii = toascii(t[i]);
        if(ascii < 123 && ascii > 97){
            ascii -= 32;
            opt[i] = (char *)ascii;
        } else {
            opt[i] = t[i];
        }
    }
    opt[strlen(t)] = '\0';

    //*str = opt;

    printf("thread_finish\n");
    return ((void*)opt);
}

int main(void) {
    char *p = "helloABC123,world";
    void *result;
    printf("thread waiting...\n");

    pthread_t thread;
    pthread_create(&thread, NULL, capitalize, &p);
    pthread_join(thread, &result);
    puts(result);

    //capitalize();
    for(int i=0; p[i]!='\0'; i++){printf("%c", p[i]);}
    printf ("\nfinish\n");
}


