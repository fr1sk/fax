//usage: ./mkfile imefajla.txt a+
//                imeFajla     flagovi
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

//kada define u vise redova razdvajamo sa "\"

#define osAssert(cond, msg) osErrorFatal(cond, msg, __LINE__, __FILE__)

void osErrorFatal(bool cond, const char *msg, int lineNum, const char *fname){
    if(!cond){
        perror(msg); //moja poruka: sistemska poruka
        fprintf(stderr, "%s:%d\n", fname, lineNum);
        exit(EXIT_FAILURE);
    }
  }

/*
prima putanju do fajla
path, r,w,a,r+,w+,a+
*/
bool osOpenFile(const char *path, const char *access, int *fd){
    static const mode_t mod = 0644; //koristise za OS programiranje, svi su integeri, to je u sustini typedefovan tip
                                    // da uvek bude uptodate
    int flags = 0;
    if('r' == access[0]){
        if('+'==access[1]){
            flags |= O_RDWR;
        } else {
            flags |= O_RDONLY;
        }
    } else if('w' == access[0]){
        flags |= O_CREAT;
        flags |= O_TRUNC;
        if('+'==access[1]){
            flags |= O_RDWR;
        } else {
            flags |= O_WRONLY;
        }
    } else {    //flag - a
        flags |= O_CREAT;
        flags |= O_APPEND;
        if('+'==access[1]){
            flags |= O_RDWR;
        } else {
            flags |= O_WRONLY;
        }
    }

    //ako open fail vraca -1
    return -1 != (*fd = open(path,flags,mod));
}

int main(int argc, char **argv){
    // if(3!=argc){
    //     fprintf(stderr, "wrong cmd args num\n");
    //     exit(EXIT_FAILURE);
    // }
    osAssert(3==argc, "Wrong num of cmd");
    //osErrorFatal(3==argc, "Wrong num of cmd", __FILE__, __LINE__);
    int fd; //file descriptor
    osAssert(osOpenFile(argv[1],argv[2], &fd), "Opening failed");
    close(fd);
    return 0;
}
