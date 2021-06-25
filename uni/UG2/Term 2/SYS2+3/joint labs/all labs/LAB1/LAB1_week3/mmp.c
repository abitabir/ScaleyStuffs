#include <stdio.h>
#include <stdlib.h>
#include <time.h>


#define START(X) clock_t X = clock()
#define STOP(X) printf("%s\t%gs", (#X), (double)(clock() - (X)) / CLOCKS_PER_SEC)

int main(int argc, char *argv[])
{
  int c, d, m1_max_col, m1_max_row, m2_max_col, m2_max_row, k, tot, i = 0;
  char *endptr;
  char *ptr = argv[1]; 
  int maxd = 3;
  //argp_parse (0, argc, argv, 0, 0, 0);
START(program);
  maxd = strtol(ptr, &endptr, 10 );
  int fst[maxd][maxd], sec[maxd][maxd], mul[maxd][maxd];
  printf(" MatrixSize\t%d\n ", maxd); 
 for (i = 0; i < maxd; i++){
 	 m1_max_col = m1_max_row = m2_max_col = m2_max_row = i+1 ;
	

//printf(" Insert your matrix elements : \n ");

  for (c = 0; c < m1_max_col; c++){
    for (d = 0; d < m1_max_row; d++){
	  fst[c][d] = rand()%100 + 1;
	  //printf("%d\t", fst[c][d]);
	  }
	  //printf("\n");
	}
 
   //printf(" Please insert the number of rows and columns for second matrix\n");

  if (m1_max_row  != m2_max_col)
   ;
    //printf(" Your given matrices cannot be multiplied with each other. \n ");
  else
  {
    //printf(" Insert your elements for second matrix \n ");
    for (c = 0; c < m2_max_col; c++){
      for (d = 0; d < m2_max_row; d++){
        sec[c][d] = rand()%100 + 1;
	//printf("%d \t", sec[c][d]);
	}
	//printf("\n");
	}

    for (c = 0; c < m1_max_col; c++) {
      for (d = 0; d < m2_max_row; d++) {
        for (k = 0; k < m2_max_col; k++) {
          tot = tot + fst[c][k] * sec[k][d];
        }
        mul[c][d] = tot;
        tot = 0;
      }
    }
 
    //printf("\n The result of matrix multiplication or product of the matrices is: \n "); 
    for (c = 0; c < m1_max_col; c++) {
      for (d = 0; d < m2_max_row; d++)
      ;
       // printf("%d \t", mul[c][d] );
      //printf(" \n ");
    }
  }
} 
STOP(program); 
  return 0;
}
