%option noyywrap
%option noinput
%option nounput

%{
#include <stdio.h>
#include <stdlib.h>
#include "calcAnin.tab.h"
%}

%%
[0-9]+(\.[0-9]+)?([eE][0-9]+)?              {yylval.f = atof(yytext);return vrednost;}
[\t\s ]                                     {;}
[+\-*/<>=();]                               {return *yytext;}
"=="                                        {return EQ;}
"!="                                        {return NEQ;}
">="                                        {return GEQ;}
"<="                                        {return LEQ;}
print                                       {return print;}
[a-z]                                       {yylval.c = yytext[0]; return ime;}
.                                           {//yyerror(yytext[0]);
                                                fprintf(stderr, "greska: %s", yytext);
                                                exit(EXIT_FAILURE);
                                            }
%%
