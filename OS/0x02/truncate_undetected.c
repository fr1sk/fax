//USAGE: ./trunc_undetected
#define osUnusedVar(x) ((void)x)
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>
#include <sys/types.h>
#include <pwd.h>
#include <utime.h>




#define BUFF_SZ (4096)
//std int treba za maxint_t

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




int main(int argc, char **argv){

    osAssert(2 == argc, "Wrong cmd args");

    //get old times
    struct stat finfo;
    osAssert(-1 != stat(argv[1], &finfo), "getting old time failed");

    //trunate file
    int fd = open(argv[1], O_WRONLY | O_TRUNC);
    osAssert(-1 != fd, "trunc failed");
    close(fd);

    //restore old times
    //koristimo fju UTIME
    struct utimbuf oldTimes = {
        .actime=finfo.st_atime,
        .modtime = finfo.st_mtime
    };
    osAssert(-1 != utime(argv[1], &oldTimes), "setting old time failed")
    return 0;
}

//void cast kaze kompajleru ja necu ovu promenjivu da koristim
