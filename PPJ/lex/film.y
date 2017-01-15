%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>

extern int yylex();
void yyerror(char *s);
int PoredjenjeGodina(const void *a, const void *b);
int PoredjenjeOcena(const void *a, const void *b);
int PoredjenjeNaziva(const void *a, const void *b);

typedef struct{
    char *naslov;
    char *reziser;
    int godina;
    float ocena;
} FILM;

FILM spisak[] = NULL;
int alocirano = 0;
int brFilmova = 0;


%}


%union
%token
%type
%nonassoc
%left
%start program

%%
program :   {}


%%

void yyerror(char *s){
    fprintf(stderr, "greska rodjaci: %s\n", s);
    exit(EXIT_FAILURE);
}

int PoredjenjeGodina(const void *a, const void *b){
    FILM prvi = *(FILM*)a;
    FILM drugi = *(FILM*)b;
    return prvi.godina - drugi.godina;

}
int PoredjenjeOcena(const void *a, const void *b){
    FILM prvi = *(FILM*)a;
    FILM drugi = *(FILM*)b;
    return prvi.ocena - drugi.ocena;

}
int PoredjenjeNaziva(const void *a, const void *b){
    FILM prvi = *(FILM*)a;
    FILM drugi = *(FILM*)b;
    return strcmp(prvi.naziv, drugi.naziv);

}

int main(){
    yyparse();
    return 0;
}
