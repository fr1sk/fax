/*****************************
* convert c code to colorful sintax html page
******************************/


%option noyywrap

%{
    void printChar(char c);
    void printString(char *s);
%}

DIGIT [0-9]
ID [a-zA-Z_][a-zA-Z0-9_]
WHITE [\t\n ]

%%
{DIGIT}+                    fprintf(yyout, "<span style='color:blue;'>%s</span>", yytext);
{DIGIT}+\.{DIGIT}*          fprintf(yyout, "<span style='color:blue;'>%s</span>", yytext);
if|else|switch|case|while|for|do|break|continue|int|char|double|float|short|unsigned|long|void|struct|union|static|extern|typedef|return|register {
    fprintf(yyout, "<B>%s</B>", yytext);
}
^{WHITE}*#(.|\\\n)*\n {
    fprintf(yyout, "<span style='color:green;'>");
    printString(yytext);
    fprintf(yyout, "</span>");
}
{ID}                        fprintf(yyout, "<span style='color:black;'>%s</span>", yytext);
"/*"([^*]|"*"*[^/*])*"*"*"/"  {
      fprintf(yyout, "<span style=\"color:grey;\">");
      printString(yytext);
      fprintf(yyout, "</span>\n");
    }
\"([^\\\"]|\\.)*\"  {

      fprintf(yyout, "<span style=\"color:red;\">");
      printString(yytext);
      fprintf(yyout, "</span>");
    }
'([^\\']|\\.)' {

    fprintf(yyout , "<span style=\"color:violet;\"> ");
    printString(yytext);
    fprintf(yyout, "</span>");}

.|\n                        ECHO;

%%
void printChar(char c){
    if(c=='<')
        fprintf(yyout, "&lt;");
    else if(c=='>')
        fprintf(yyout, "&gt;");
    else if(c=='&')
        fprintf(yyout, "&amp;");
    else
        fprintf(yyout, "%c",c);
}

void printString(char *s){
    int i;
    for(i=0; s[i]!='\0'; i++){
        printChar(s[i]);
    }
}


int main(int argc, char **argv){
    if(argc>1 && (yyin = fopen(argv[1],"r"))!=NULL);
    else yyin = stdin;
    if(argc>2 && (yyout = fopen(argv[2],"w"))!=NULL);
    else yyout = stdout;

    //print html
    fprintf(yyout, "<html>\n");
    if(argc>1){
        fprintf(yyout,"<head>\n\t<title>%s</title>\n", argv[1]);
    }
    fprintf(yyout, "<body>\n\t<pre>\n");
    yylex();
    fprintf(yyout, "\t</pre>\n</body>\n</html>");

    fclose(yyin);
    fclose(yyout);
    return 0;
}
