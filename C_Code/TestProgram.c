/*
 ============================================================================
 Name        : TestProgram.c
 Author      : 
 Version     :
 Copyright   : Your copyright notice
 Description : Hello World in C, Ansi-style
 ============================================================================
 */

#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ARRAYSIZE 10;


void primeFactors(long target, long* array, int* counter) {
	const int FALSE =  0;
	const int TRUE  = 1;
	int flag = 0;
	//float compareSqrt = 0.0;
	long val = 1;
	int size = ARRAYSIZE;
	//counter = calloc(sizeof(int),0);
	//array  = malloc( size*sizeof(long));

	*counter = 0;
	while (target % 2 == 0) {
		target = target / 2;
		//yeah yeah i know this could happen multiple times, I didn't want to write extra code...
		*counter = 1;
		array[0]=2;
	}
	while (val < target) {
		flag = TRUE;
		val += 2;
		//compareSqrt = sqrt((float)val);
		//Could actual start at 0
		for (int i = 0; i < *counter; i++ ) {
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
				size = size * 2;
				//printf("New Size: %d\n", size); fflush(stdout);
				realloc(array, size*sizeof(long));
			}
			if (target % val == 0 ) {
				while (target % val == 0) {
					target = target / val;
				}
				array[*counter] = val;
				//printf("Display: %i\n", array[*counter]);
				*counter = *counter + 1;
			}
		}
	}
}

void primeComponentList(long target, long* result, int* size) {
	long * array;
	int * counter;
	int x = 0;
	array  = malloc( 1000*sizeof(long));
	counter  = malloc( 1*sizeof(long));
	//primeFactors(target, array, counter);
	printf("counter: %d\n",*counter);
	for (int i = 0; i < *counter; i++) {
		while (target % array[i] == 0) {
			target = target / array[i];
			printf("::%d,target: %d, size: %d!\n",array[i],target,x);
			result[x] = array[i];
			x++;
		}
	}
	*size = x;
}






int main(void) {
	printf("Euler Problem\n");
	fflush(stdout);
	//problem3();
	//problem4();
	//problem6();
	//problem7();
	//problem8();
	//problem9();
	//problem10();
	//problem12();
	//problem47();
	//problem48();
	problem383();
	/*
	long * array;
	int * counter;
	long target;
	int ArraySize = ARRAYSIZE;

	array  = malloc( ArraySize*sizeof(long));
	counter  = malloc( 1*sizeof(long));
	target = 3072;
	primeFactors(target, array, counter);
	printf("\n");
	for (int i = 0; i < *counter; i++) {
		fflush(stdout);
		printf("%d, ",array[i]);
	}
	printf("\n");
	target = 76576500;
	array  = malloc( 1000*sizeof(long));
	counter  = malloc( 1*sizeof(long));
	primeComponentList(target, array, counter);
	printf("\n");
	for (int i = 0; i < *counter; i++) {
		fflush(stdout);
		printf("%d, ",array[i]);
	}

	printf("\n");
	printf("Finish Euler Problem\n");
	fflush(stdout);*/
	//return EXIT_SUCCESS;
}

