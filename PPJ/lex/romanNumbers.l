%option noyywrap

%{
    int value = 0;
%}

hiljade M+
stotine C+|CD|DC*|CM
desetice X+|XL|LX*|XC
jedinice I+|IV|VI*|IX

%%


%%

int main(){
    yylex();
    return 0;
}
