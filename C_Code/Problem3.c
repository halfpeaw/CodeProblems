/*
 * Problem3.c
 *
 *  Created on: Jan 15, 2012
 *      Author: halfpeaw
 */


#include <stdio.h>
#include <stdlib.h>
#include <math.h>




void primeList3(long *array, int *counter, long limit) {
	const int FALSE =  0;
	const int TRUE  = 1;
	int flag = 0;
	//float compareSqrt = 0.0;
	int size = 48;
	long val = 3;
	realloc(array, size*sizeof(long));
	array[0] = 1;
	array[1] = 2;
	array[2] = 3;
	*counter = 3;
	while (val < limit) {
		flag = TRUE;
		val += 2;
		//compareSqrt = sqrt((float)val);
		for (int i = 2; i < *counter; i++ ) {
			/*if ((float)val > compareSqrt) {
				printf("Sqrt Break %i\n",val);
				break;
			}*/
			if (val % array[i] == 0) {
				flag = FALSE;
				break;
			}
		}
		if (flag == 1) {
			printf("SIZE: %d, Counter: %d\n", size, *counter); fflush(stdout);
			if (*counter >= size) {
				size = size * 2;
				printf("New Size: %d\n", size); fflush(stdout);
				realloc(array, size*sizeof(long));
			}
			array[*counter] = val;
			printf("Display: %i\n", array[*counter]);
			*counter = *counter + 1;
		}
	}
	printf("exit\n");

}

void ReduceLimit(long *array, int *counter, unsigned long long limit) {
	const int FALSE = 0;
	const int TRUE = 1;
	int flag = 0;
	int size = 48;
	long val = 1;
	realloc(array, size*sizeof(long));
	array[0] = 1;
	array[1] = 2;
	*counter = 2;
	while (limit % 2 == 0) {
		limit = limit / 2;
		printf("2 New Val: %q, divisor: 2\n",limit);
	}

	while (val < limit) {
		flag = 1;
		val += 2;
		//compareSqrt = sqrt((float)val);
		for (int i = 2; i < *counter; i++ ) {
			/*if ((float)val > compareSqrt) {
				printf("Sqrt Break %i\n",val);
				break;
			}*/
			while (limit % val == 0) {
				limit = limit / (long long)val;
				printf("New Val: %llu, divisor: %llu\n",limit,val);
			}
			if (val % array[i] == 0) {
				flag = 0;
				break;
			}
		}
		if (flag == TRUE) {
			//printf("SIZE: %d, Counter: %d\n", size, *counter); fflush(stdout);
			if (*counter >= size) {
				size = size * 2;
				//printf("New Size: %d\n", size); fflush(stdout);
				realloc(array, size*sizeof(long));
			}
			array[*counter] = val;
			//printf("Display: %i\n", array[*counter]);
			*counter = *counter + 1;
		}
	}
	printf("SIZE: %d, Counter: %d\n", size, *counter); fflush(stdout);
	for (int i = 0; i < *counter; i++ ) {
			printf("%i ",array[i]);
	}
	printf("exit\n");

}



void problem3(void) {

	printf("What is the largest prime factor of 600851475143?\n"); fflush(stdout);
	long *array;
	int *counter;
	array=(long *) malloc(1000*sizeof(long));
	counter = calloc(sizeof(int),0);
	*counter = 0;
	ReduceLimit(array, counter,600851475143);

	/*for (int i = 0; i < *counter; i++ ) {
		printf("%i ",array[i]);
	}*/
	free(array);
}



