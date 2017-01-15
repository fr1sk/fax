%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
extern int yylex();
char imena[26];
void yyerror(char *s);
void postavi(char c, float value);
%}


%union {
    char c;
    float f;
}
%nonassoc '<' '>' EQ NEQ GEQ LEQ
%left '+' '-' '*' '/'
%token print EQ NEQ GEQ LEQ
%token <c> ime
%token <f> vrednost
%type <f> e
%start program

%%
program :   program naredba ';'         {;}
        |   naredba ';'                 {;}
        ;

naredba :   print '(' e ')'             {printf("%.2f",$3);}
        |   ime '=' e                   {postavi($1,$3);}
        |   e '>' e                     {if($1>$3) printf("tacno!");else printf("netacno");}
        |   e '<' e                     {if($1<$3) printf("tacno!");else printf("netacno");}
        |   e EQ e                      {if($1==$3) printf("tacno!");else printf("netacno");}
        |   e NEQ e                     {if($1!=$3) printf("tacno!");else printf("netacno");}
        |   e LEQ e                     {if($1<=$3) printf("tacno!");else printf("netacno");}
        |   e GEQ e                     {if($1>=$3) printf("tacno!");else printf("netacno");}
        ;

e       :   e '+' e                     {$$ = $1 + $3;}
        |   e '-' e                     {$$ = $1 - $3;}
        |   e '*' e                     {$$ = $1 * $3;}
        |   e '/' e                     {if($3==0) yyerror("deljenje 0 nije moguce"); $$ = $1 / $3;}
        |   '('e')'                     {$$ = $2;}
        |   '-'e                        {$$ = -$2;}
        |   vrednost                    {$$ = $1;}
        |   ime                         {$$ = imena[$1-'a'];}
        ;

%%

void yyerror(char *s){
    fprintf(stderr, "nepoznato: %s\n", s);
    exit(EXIT_FAILURE);
}

void postavi(char c,float value){
    imena[c-'a']=value;
}

int main(){
    yyparse();
    return 0;
}
