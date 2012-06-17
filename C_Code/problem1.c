/*
 * problem1.c
 *
 *  Created on: Feb 1, 2012
 *      Author: halfpeaw
 */
#include <stdio.h>
void problem1(void) {
	const int va11 = 3;
	const int val2 = 5;
	const int TOTAL = 1000;
	int sum = 0;
	for (int i = 0; i < TOTAL; i++ ) {
		if (i % va11 == 0 || i % val2 == 0) {
			sum = i + sum;
			printf("Sum: %d\n",i);
		}
	}
	printf("Sum: %d\n",sum);
}
