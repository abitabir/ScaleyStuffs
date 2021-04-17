#include<stdio.h>
#include"myprint.h"
/*
including the header file - a 'helper' file containing
definitions of various C functions and associated variables.
stdio.h is the default header file that comes with the C compiler.
add headers according to the fucntions you want to use in your code.
double quotes inform compiler to start searching for header files
from your own current directory.
*/

int main() /* simple main function, takes in no values, output is of type int */
{
    printf("Hello SYS2+4 students!\nXDDD"); // printf is a function being called, statement in parameter printed
    // myprint(10);  // causes error probably a functioned defined in some scope
    return 0;
}
/*
int myprint(int x)
{
    printf("This is my printing func\n"); // need to seperate lines out between each compiler
    return 0;
}
*/
