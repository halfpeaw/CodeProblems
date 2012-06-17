/*
 * problem47.c
 *
 *  Created on: Jan 21, 2012
 *      Author: halfpeaw
 */

#include <stdlib.h>
#include <math.h>
#include <stdio.h>

int problem47Prime(int *counter) {
	const int FALSE = 0;
	const int TRUE = 1;
	int flag = 0;
	int numInARow = 0;
	int numDividers = 0;
	int size = 20000;
	long val = 3;
	long *array;
	array = (long*)malloc(size*sizeof(long));
	array[0] = 2;
	array[1] = 3;
	*counter = 2;
	while (*counter < size) {
		flag = TRUE;
		val+=1;
		//compareSqrt = sqrt((float)val);
		for (int i = 0; i < *counter; i++ ) {
			if (val % array[i] == 0) {
				numDividers +=1;
				flag = FALSE;
			}
		}
		//Is a number not prime and had 4 prime dividers
		if (flag == FALSE && numDividers == 4) {
			//printf("Val: %d",val);
			numInARow += 1;
			if (numInARow == 3) {
				//printf("3 in a row!: %d, counter %d\n",val,*counter);

			}
			if (numInARow == 4) {
				return val;
			}
		} else {
			numInARow = 0;
		}
		//Reset num dividers
		numDividers = 0;
		if (flag == TRUE) {
			//printf("SIZE: %d, Counter: %d\n", size, *counter); fflush(stdout);
			if (*counter >= size) {
				printf("Shouldn't happen\n");
				return 0;
			}
			array[*counter] = val;
			//printf("%i: %i\n", *counter, array[*counter]);
			*counter = *counter + 1;
		}
	}
	return 0;
	printf("exit\n");

}


void problem47(void) {
	printf("Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?\n");
	int *counter;
	counter = calloc(sizeof(int),0);
	*counter = 0;
	int result = problem47Prime(counter);
	printf("Result: %d, %d, %d, %d\n",result-3,result-2,result-1,result);
	//free(array);

}

