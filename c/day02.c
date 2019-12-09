#include <stdio.h>
#include <string.h>

#define SIZE 1024

/* available opcodes */
enum opcodes {
	OP_ADD = 1,
	OP_MUL = 2,
	OP_FIN = 99
};

int run_program(int *a)
{
	int i;
	const int oplen = 4;

	for(i=0;; i+=oplen) {
		switch(a[i]) {
			case OP_ADD:
				a[a[i+3]] = a[a[i+1]] + a[a[i+2]];
				break;
			case OP_MUL:
				a[a[i+3]] = a[a[i+1]] * a[a[i+2]];
				break;
			case OP_FIN:
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

int part2(int *a, int *b)
{
	int noun, verb;
	const int magic = 19690720;

	for(noun=0; noun<100; noun++) {
		for(verb=0; verb<100; verb++) {
			a[1] = noun;
			a[2] = verb;
			run_program(a);
			if(a[0] == magic) {
				return 100 * noun + verb;
			}
			/* restore initial state from backup */
			memcpy(a, b, SIZE * sizeof(int));
		}
	}
	return -1;
}


int main(int argc, char **argv)
{
	int i, m, a[SIZE], b[SIZE];

	i = 0;
	for(i=0; scanf("%d,", &m) != EOF; i++) {
		a[i] = m;
	}

	/* make backup of a in b */
	memcpy(b, a, SIZE * sizeof(int));

	printf("part1: %d\n", part1(a));
	
	/* restore backup for part 2 */
	memcpy(a, b, SIZE * sizeof(int));

	printf("part2: %d\n", part2(a, b));

	return 0;
}
