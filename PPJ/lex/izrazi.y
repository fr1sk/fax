%{
#include <stdio.h>
#include <stdlib.h>
extern int yylex();
int yyerror(char *s){
    fprintf(stderr, "%s\n", s);
    exit(EXIT_FAILURE);
}

%}

//redefinisemo tip vrednosti, po defaultu je int, moze vise
%union {
    int vrednost;
}

//token gde cuvamo vrednost i tip. zadajemo u kom polju
//unije ce se nalaziti i dobija i taj tip
%token <vrednost> NUM

//neterminali - ako su istog tipa moze u istom redu
%type <vrednost> e t f

//funkcija (aksioma) gramatike
%start pocetak

%%
pocetak: e      {printf("vrednost izraza je %d\n",$1);}

e: e '+' t      {$$=$1+$3;}
|        t      {$$=$1;}


t: t '*' f      {$$=$1*$3;}
|        t      ;

f: '(' f ')'    {$$=$2;}
|       NUM     {$$=$1;}

%%


int main(){
    if(yyparse()==0){
        printf("Uparen je aritmeticki izraz\n");
    return 0;
    }
}
