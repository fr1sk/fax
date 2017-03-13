//komanda ll

//USAGE: ./fileinfo putanja(fajl)
#define _XOPEN_SOURCE 700
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
#include <grp.h>
#include <time.h>
//stdint treba za maxint_t

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

    struct stat finfo;
    osAssert(-1 != stat(argv[1], &finfo), "getting finfo failed");

    //print file type
    if(S_ISREG(finfo.st_mode)){
        printf("-");
    } else if(S_ISDIR(finfo.st_mode)){
        printf("d");
    } else if(S_ISCHR(finfo.st_mode)){
        printf("c");
    } else if(S_ISBLK(finfo.st_mode)){
        printf("b");
    } else if(S_ISLNK(finfo.st_mode)){
        printf("l");
    } else if(S_ISSOCK(finfo.st_mode)){
        printf("s");
    } else if(S_ISFIFO(finfo.st_mode)){
        printf("p");
    }
    //privilegije
    // if (finfo.st_mode & S_IRUSR){
    //     printf("r");
    // }
    // printf("\n");
    printf("%c", finfo.st_mode & S_IRUSR ? 'r' : '-');
    printf("%c", finfo.st_mode & S_IWUSR ? 'w' : '-');
    printf("%c", finfo.st_mode & S_IXUSR ? 'x' : '-');
    printf("%c", finfo.st_mode & S_IRGRP ? 'r' : '-');
    printf("%c", finfo.st_mode & S_IWGRP ? 'w' : '-');
    printf("%c", finfo.st_mode & S_IXGRP ? 'x' : '-');
    printf("%c", finfo.st_mode & S_IROTH ? 'r' : '-');
    printf("%c", finfo.st_mode & S_IWOTH ? 'w' : '-');
    printf("%c", finfo.st_mode & S_IXOTH ? 'x' : '-');

    //get number of hardlinks
    printf(" %jd", (intmax_t)finfo.st_nlink);

    //get username
    struct passwd *pUserInfo = getpwuid(finfo.st_uid);
    osAssert(NULL != pUserInfo, "Failed to get user info");
    printf(" %s",pUserInfo->pw_name);

    //get group name
    struct group *pGrpInfo = getgrgid(finfo.st_gid);
    osAssert(NULL != pGrpInfo, "Failed to get grp info");
    printf(" %s", pGrpInfo->gr_name);

    //get file size
    printf(" %jd", (intmax_t)finfo.st_size);

    //get time string
    char *ctimeStr = ctime(&finfo.st_mtime);
    ctimeStr[strlen(ctimeStr)-1] = 0;
    printf(" %s",ctimeStr);

    printf(" %s", argv[1]);
return 0;
}
