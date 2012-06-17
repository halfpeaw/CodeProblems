/*
 * problem48.c
 *
 *  Created on: Jan 21, 2012
 *      Author: halfpeaw
 */
#include <stdlib.h>
#include <math.h>
#include <stdio.h>

void problem48(void) {

	printf("Find the last 10 digits of sum(1^1, 2^2,3^2, ... ,1000^1000\n");
	const long long MAX = 10000000000LL;
	int limit = 1000;
	long long summation = 0;
	long long multiVal = 1;
	for (long i = 1; i <= limit; i++) {
		multiVal = 1;
		for (long val = 1; val <= i; val++) {
			multiVal = multiVal * i;
			if (multiVal > MAX) {
				multiVal = multiVal % MAX;
				if (multiVal == 0) {
					printf("I think something is amiss: %d^%d\n",i,val);
					break;
				}
			}
		}
		//printf("Multival: %llu\n",multiVal);
		summation = summation + multiVal;
		if (summation > MAX) {
			//printf("Reset, summation: %llu\n",summation);
			summation = summation % MAX;

		}
	}
	printf("Problem48 Result: %llu\n",summation);
	//9110846700

}

