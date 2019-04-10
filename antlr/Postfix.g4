grammar Postfix;

DIGIT: [0-9];
NL:   '\r'? '\n' ;

prog:   (   expr NL* {print()}
        )*
        EOF
    ;
expr: term rest;
rest: '+' term {print('+', end='')} rest
	| '-' term {print('-', end='')} rest
	|
	;
term: DIGIT {print($DIGIT.int, end='')} ;
