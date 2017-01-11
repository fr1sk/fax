/**********************************
* count chars and new lines
* stop on EOF
***********************************/

%option noyywrap

%{
    int charCount = 0;
    int lineCount = 0;
%}

%%
\n {
    charCount++;
    lineCount++;
}

. {
    charCount++;
}
%%

int main(){
    yylex();
    printf("num of characters: %d\nnum of lines: %d", charCount, lineCount);
    return 0;
}
