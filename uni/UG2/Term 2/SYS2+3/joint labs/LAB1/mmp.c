#include<stdio.h>
#include <stdlib.h>

int main(void)
{
  int c, d, p, q, m, n, k, tot = 0;
  int fst[10][10], sec[10][10], mul[10][10];
  int  maxd = 3;
 for (c = 0; c < maxd; c++){
 	 m = c+1;
	 n = c+1;
 	 p = c+1;
 	 q = c+1;

//printf(" Insert your matrix elements : \n ");
  for (c = 0; c < m; c++){
    for (d = 0; d < n; d++){
	fst[c][d] = rand()%100 + 1;
	printf("%d \t", fst[c][d]);
	}
	printf("\n");
	}
   //printf(" Please insert the number of rows and columns for second matrix\n");

  if (n != p)
    printf(" Your given matrices cannot be multiplied with each other. \n ");
  else
  {
    //printf(" Insert your elements for second matrix \n ");
    for (c = 0; c < p; c++){
      for (d = 0; d < q; d++){
        sec[c][d] = rand()%100 + 1;
	printf("%d \t", sec[c][d]);
	}
	printf("\n");
	}

    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++) {
        for (k = 0; k < p; k++) {
          tot = tot + fst[c][k] * sec[k][d];
        }
        mul[c][d] = tot;
        tot = 0;
      }
    }
 
    printf("\n The result of matrix multiplication or product of the matrices is: \n "); 
    for (c = 0; c < m; c++) {
      for (d = 0; d < q; d++)
        printf("%d \t", mul[c][d] );
      printf(" \n ");
    }
  }
}
  return 0;
}
