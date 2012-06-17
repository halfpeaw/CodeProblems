/*
 * problem9.c
 *
 *  Created on: Jan 22, 2012
 *      Author: halfpeaw
 */


#include <stdlib.h>
#include <math.h>
#include <stdio.h>


void problem9(void) {
	printf("There exists exactly one Pythagorean triplet for which a + b + c = 1000. Find the product abc.\n");
	const int MAX = 1000;
	long c = 1;
	for (long b = 1; b < MAX; b++) {
		for (long a = 1; a < MAX; a++) {
			c = pow(a,2) + pow(b,2);
			c = sqrt(c);
			if (pow(c,2) == pow(a,2) + pow(b,2)) {
				if (c+a+b == 1000) {
					printf("a: %d, b: %d, c: %d\n",a,b,c);
					printf("Product: %d\n",a*b*c);
					return;
				}
			}
		}
	}

}
