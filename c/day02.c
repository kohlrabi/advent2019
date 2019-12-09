#include <stdio.h>

#define SIZE 1024

int run_program(int *a)
{
	int i;

	for(i=0;; i+=4) {
		switch(a[i]) {
			case 1:
				a[a[i+3]] = a[a[i+1]] + a[a[i+2]];
				break;
			case 2:
				a[a[i+3]] = a[a[i+1]] * a[a[i+2]];
				break;
			case 99:
				return 0;
			default:
				return -1;
		}
	}
}

int part1(int *a)
{
	a[1] = 12;
	a[2] = 2;

	run_program(a);

	return a[0];
}


int main(int argc, char **argv)
{
	int i, m, a[SIZE];

	i = 0;
	for(i=0; scanf("%d,", &m) != EOF; i++) {
		a[i] = m;
	}

	printf("part1: %d\n", part1(a));

	return 0;
}
