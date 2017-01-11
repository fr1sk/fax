/********************************************
* ignore all pascal comments
*********************************************/

%option noyywrap
%option noinput
%option nounput

%%
"{"[^}]*"}"         ;
"(*"[^)]*"*)"       ;
.               ECHO;

%%

int main(){
    yylex();
    return 0;
}
