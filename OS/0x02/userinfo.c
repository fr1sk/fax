//izbacuje info za username korisnika koji je zadat kao arg
//korisino fju getpwnam

//USAGE: ./usrinfo imeusera

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
    osAssert(2==argc, "Wrong num of cmd num\n");

    struct passwd *pUserInfo = getpwnam(argv[1]);
    osAssert(NULL != pUserInfo, "Unknown user");

    printf("UNAME: %s\n"
           "UID: %jd\n"
           "GID: %jd\n"
           "GECKOS: %s\n"
           "HOME DIR: %s\n"
           "LOGIN SHELL: %s\n",
           pUserInfo->pw_name,
           (intmax_t)pUserInfo -> pw_uid,
           (intmax_t)pUserInfo -> pw_gid,
           pUserInfo -> pw_gecos,
           pUserInfo -> pw_dir,
           pUserInfo -> pw_shell
       );

    return 0;
}
