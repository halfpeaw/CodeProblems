/*
 * problem10.c
 *
 *  Created on: Jan 22, 2012
 *      Author: halfpeaw
 */

#include <stdlib.h>
#include <math.h>
#include <stdio.h>


void problem10PrimeList() {
	const int FALSE = 0;
	const int TRUE = 1;
	long *array;
	array=(long *) malloc(250000*sizeof(long));
	int flag = 0;
	long counter;
	long long summation = 5;
	//float compareSqrt = 0.0;
	long size = 2000000;
	long val = 5;
	array[0] = 2;
	array[1] = 3;
	counter = 2;

	while (val < size) {
		flag = TRUE;
		//compareSqrt = sqrt((float)val);
		for (int i = 1; i < counter; i++ ) {
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
			if (counter >= size) {
				printf("Shouldn't happen\n");
				return;
			}
			array[counter] = val;
			summation += (long long)val;
			printf("%i: %i\n", counter, array[counter]);
			printf("Summation: %llu\n",summation);
			counter +=1;
		}
		val += 2;
	}
	printf("Summation: %llu\n",summation);
	printf("exit\n");
}

void problem10(void) {
	printf("Find the sum of all the primes below two million.\n");
	problem10PrimeList();
}
