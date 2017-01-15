
%option noyywrap
%option nounput
%option noinput

%{
#include <stdio.h>
#include <stdlib.h>
#include "y.tab.h"

%}

%%
[0-9]+      yylval.vrednost = atoi(yytext); return NUM;
[+*()]      return yytext[0];
[\n\t ]     ;
.           fprintf(stderr,"nepoznata lexema %s\n",yytext); exit(EXIT_FAILURE);

%%
