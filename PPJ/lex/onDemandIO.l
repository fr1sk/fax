/*************************************
* ondemand lexer updated
**************************************/

%option noyywrap

%{
    #define floatConst 1
    #define intConst 2
%}

%%
[+-]?[0-9]+                                return intConst;
[+-]?[0-9]+\.[0-9]*([Ee][+-]?[0-9]+)?      return floatConst;
\n                       ;
.                        ;
%%

int main(int argc, char **argv){
    if(argc>1 && (yyin = fopen(argv[1],"r"))!=NULL);
    else yyin=stdin;
    if(argc>2 && (yyout = fopen(argv[2],"w"))!=NULL);
    else yyout=stdout;

    int token;
    while(token=yylex()){
        switch(token){
            case floatConst:
                printf("float const %s\n", yytext);
                break;
            case intConst:
                printf("int const %s\n", yytext);
                break;
        }
    }
    return 0;
}
