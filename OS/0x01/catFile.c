//program koj simulira CAT comandu
//read(int fd, void *buf, size_t count);
//fd - handler
//buf - bilo koj tip cita
//count - broj koliko cita


//USAGE: ./catfile 1.txt
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>

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


void osCatFile(int fd){
    char buf[BUFF_SZ];
    ssize_t bytesRead;

    //sizeof bez zagrada radi za ne pokazivace
    while((bytesRead = read(fd, buf, sizeof buf)) > 0){
        //ssize_t write(int fd, const void *buf, size_t count);
        //postoje defineovane konstante koje odgovaraju file deskriptorima
        //STDIN_FILENO  0
        //STDERR_FILENO 1
        //STDOUT_FILENO 2
        osAssert(-1 != write(STDOUT_FILENO, buf, bytesRead), "Write failed");
    }
    osAssert(-1 != bytesRead, "read failed");
}

int main(int argc, char **argv){
    osAssert(2==argc, "Wrong num of cmd num\n");
    int fd; //file descriptor
    osAssert(osOpenFile(argv[1],"r", &fd), "Opening failed");
    osCatFile(fd);
    close(fd);
    return 0;
}
