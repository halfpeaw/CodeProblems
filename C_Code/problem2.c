/*
 * problem2.c
 *
 *  Created on: Feb 1, 2012
 *      Author: halfpeaw
 */
#include <stdio.h>

void problem2(void) {
	const int TOTAL = 4000000;
	const int VAL = 2;
	int first = 1;
	int second = 2;
	long sum = second;
	for (int i = 3; i < TOTAL; i = first + second ) {
		first = second;
		second = i;
		printf("Fib: %d\n", i);
		if (i % VAL == 0) {
			sum = i + sum;
			printf("Sum: %d\n",i);
		}
	}
	printf("Sum: %d\n",sum);
}
