%{
#include <stdio.h>
#include <stdlib.h>
void yyerror(char *s);
extern int yylex();
%}

%union {float f;}
%token <f> NUM
%type <f> E T F


//nonterminals levo, karakteri u singlequote
%%
S   :   E               {fprintf(stdout, "%f\n", $1);}
    ;

E   :   E '+' T         {$$ = $1 + $3;}
    |   E '-' T         {$$ = $1 - $3;}
    |   T               {$$ = $1;}
    ;

T   :   T '*' F         {$$ = $1 + $3;}
    |   T '/' F         {$$ = $1 + $3;}
    |   F               {$$ = $1;}
    ;

F   :   '(' E ')'       {$$ = $2;};
    |   '-' F           {$$ = -$2;}
    |   NUM             {$$ = $1;}
    ;



%%

void yyerror(char *s){
    fprintf(stderr, "%s\n", s);
    exit(EXIT_FAILURE);
}

int main(){
    yyparse();
    return 0;
}
