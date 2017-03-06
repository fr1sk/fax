//usage: ./mkdir imeDir 775
//              imeDira dozvole
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//kada define u vise redova razdvajamo sa \

#define osAssert(cond, msg) \
        osErrorFatal(cond, msg, __LINE__, __FILE__);

void osErrorFatal(bool cond,
                  const char *msg,
                  int lineNum,
                  const char *fname){
                    if(!cond){
                        perror(msg); //moja poruka: sistemska poruka
                        fprintf(stderr, "%s:%d\n", fname, lineNum);
                        exit(EXIT_FAILURE);
                    }
                  }

/*
prima putanju do fajla
path, access[0775]
*/

//koristimo mkdir
int main(int argc, char **argv){
    osAssert(3==argc, "Wrong num of cmd num\n");
    //int fd; //file descriptor
    //strtol prebacuje borjeve iz jedne u drugu osnovu
    //drugi argument sluzi za detekciju greske ako npr u stringu nemamo nikakav br
    char *endptr = NULL;
    long access = strtol(argv[2], &endptr, 8);
    osAssert(!*endptr, "Argument not a number");
    osAssert(-1 != mkdir(argv[1], access), "Mkdir failed");
    return 0;
}
