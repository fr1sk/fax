%option noyywrap
%option noinput
%option nounput

%{
#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include "y.tab.h"

%}

%%
"print"         {return print;}
"exit"          {return exit_command;}
[a-zA-Z]        {yylval.id=yytext[0];return identifier;}
[0-9]+          {yylval.num = atoi(yytext);return number;}
[-+=;]          {return yytext[0];}
[\n\t ]         ;
.               {ECHO;yyerror("unexpected character");}


%%


//int yywrap (void) {return 1;}
