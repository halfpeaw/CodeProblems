/*
 * problem7.c
 *
 *  Created on: Jan 21, 2012
 *      Author: halfpeaw
 */
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void problem7PrimeList(long *array, int *counter) {
	const int FALSE = 0;
	const int TRUE = 1;
	int flag = 0;
	//float compareSqrt = 0.0;
	int size = 10002;
	long val = 3;
	realloc(array, size*sizeof(long));
	array[0] = 2;
	array[1] = 3;
	*counter = 2;
	while (*counter < size) {
		flag = TRUE;
		val += 2;
		//compareSqrt = sqrt((float)val);
		for (int i = 1; i < *counter; i++ ) {
			/*if ((float)val > compareSqrt) {
				printf("Sqrt Break %i\n",val);
				break;
			}*/
			if (val % array[i] == 0) {
				flag = FALSE;
				break;
			}
		}
		if (flag == TRUE) {
			//printf("SIZE: %d, Counter: %d\n", size, *counter); fflush(stdout);
			if (*counter >= size) {
				printf("Shouldn't happen\n");
				return;
				//size = size * 2;
				//printf("New Size: %d\n", size); fflush(stdout);
				//realloc(array, size*sizeof(long));
			}
			array[*counter] = val;
			printf("%i: %i\n", *counter, array[*counter]);
			*counter = *counter + 1;
		}
	}
	printf("exit\n");

}

void problem7(void) {
	printf("What is the 10 001st prime number?\n");
	int *counter;
	long *array;
	counter = calloc(sizeof(int),0);
	array=(long *) malloc(1*sizeof(long));
	*counter = 0;
	problem7PrimeList(array, counter);
	free(array);
}
