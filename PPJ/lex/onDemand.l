/*************************************
* find fload and int constants
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

int main(){
    int token;
    while(token=yylex()){
        switch(token){
            case floatConst:
                printf("float konstanta: %s\n",yytext);
                break;
            case intConst:
                printf("int konstanta: %s\n",yytext);
                break;
        }
    }
    return 0;
}
