/********************************************
* check if all brackets are closed/opened
*********************************************/

%option noyywrap

%{
    int opened = 0;
%}

%%
"{" {ECHO;opened++;}
"}" {ECHO;opened--;}
\n {ECHO;}
. {ECHO;}
%%

int main(){
    yylex();
    if(opened==0){
        printf("Sve zagrade su lepo uparene.\n");
    }
    else if(opened>0){
        printf("ima %d vise otvorenih.\n",opened);
    } else {
        printf("ima %d vise zatvorenih.\n",abs(opened));
    }
    return 0;
}
