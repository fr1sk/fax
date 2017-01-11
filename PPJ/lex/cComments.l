

%option noyywrap
%x commentState

%{
int numOfLines = 0;

%}

%%
"/"+\*                      BEGIN(commentState);
<commentState>[^*\n]*       ;
<commentState>"*"*          ;
<commentState>\n            numOfLines++;
<commentState>\*+"/"        BEGIN(INITIAL);
\n                          numOfLines++;ECHO;
.                           ECHO;
%%

int main(void){
    yylex();
    printf("\n\nbroj linija je %d\n\n", numOfLines);
    return 0;
}
