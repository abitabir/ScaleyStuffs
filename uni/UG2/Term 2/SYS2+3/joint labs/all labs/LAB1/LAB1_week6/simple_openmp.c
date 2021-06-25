#include <omp.h> //In mac-os if you have erron finiding this - may install using brew install libomp
#include <stdio.h>
int main(int argc, char *argv[])
{
/* sequential code */
#pragma omp parallel
{
printf("I am a parallel region.");
}
/* sequential code */
return 0;
}