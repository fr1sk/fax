//Usage: ./rmdir -f imefajla
//       ./rmdir -d imeFoldera
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

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

//brisemo fajlove - koristimo UNLINK sistemski poziv
//2 fajla koji su isti fajl na disku - hard link - REFERENCE COUNTING tehnika - broji broj referenci na objekat
int main(int argc, char **argv){
    osAssert(3==argc, "Wrong num of cmd num\n");
    int fd; //file descriptor
    //
    if(!strcmp("-f", argv[1])){
        osAssert(-1 != unlink(argv[2]), "removing file failed");
    } else {
        osAssert(-1 != rmdir(argv[2]), "removing directory failed");
    }
    return 0;
}
