//izbacuje listu svih usera i podatke o njima

//USAGE: ./listusers
#define _XOPEN_SOURCE 700
//neka od bibl ima if define i tamo pita da li je > 500 i zato mora pre definises
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

void osPrintUser(const struct passwd *pUserInfo){
    printf("########################################\n");
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

}



int main(int argc, char **argv){
    osUnusedVar(argc); //isto ova 2
    (void)argv;

    struct passwd *pUserInfo = NULL;
    setpwent();
    while((pUserInfo = getpwent())){ //u slucaju da bude NULL bice false i nece uci u while
        osPrintUser(pUserInfo);
    }
    endpwent();
    osAssert(NULL != pUserInfo, "Unknown user");


    return 0;
}

//void cast kaze kompajleru ja necu ovu promenjivu da koristim
