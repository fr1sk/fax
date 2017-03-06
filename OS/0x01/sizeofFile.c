//racuna velicinu fajla
//sistemsi poziv lseak
//off_t lseek(int fd, off_t offset, int whence);
//vraca trenutnu udaljenost od pocetka fajla
//fajl niz bajtova a ne kao studenti sa fona xD
//fajl sadrzi referentne tacne
    //seek_end - krajfajla
    //seek_set - pocetakfajla
    //seek_cur - nasa trenutna pozicija

//USAGE: ./sizeof 1.txt
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>
#include <stdint.h>
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




off_t osFsize(int fd){
    off_t currPos = lseek(fd, 0, SEEK_CUR);
    osAssert(-1 != currPos, "Getting curr pos failed");
    off_t fsize = lseek(fd, 0 ,SEEK_END);
    osAssert(-1 != fsize, "Getting file size failed");
    osAssert(-1 != lseek(fd,currPos, SEEK_SET), "Restore failed");
    return fsize;


}


    int main(int argc, char **argv){
        osAssert(2==argc, "Wrong num of cmd num\n");
        int fd; //file descriptor - handler
        osAssert(osOpenFile(argv[1],"r", &fd), "Opening failed");
        printf("filesize: %jd", (intmax_t)osFsize(fd));
        close(fd);
        return 0;
    }

//int32_t
//uint64_t
//intmax_t -- najveci int
