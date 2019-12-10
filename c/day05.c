#include <stdio.h>
#include <string.h>

#define SIZE (1024*1024*20)

/* available opcodes */
enum opcodes {
	OP_ADD = 1,
	OP_MUL = 2,
	OP_INP = 3,
	OP_OUT = 4,
	OP_JNZ = 5,
	OP_JEZ = 6,
	OP_SLT = 7,
	OP_SEQ = 8,
	OP_FIN = 99
};

int run_program(int *a, int input)
{
	int i, j;
	int oplen = 4;
	int output = -1;
	int op;
	int mode;
	int ops[2];

	for(i=0;; i+=oplen) {
		/* extract opcode */
		op = a[i] % 100;
		/* extract mode flags
		 * 0: position mode
		 * 1: immediate mode
		 *
		 * we only need to extract the first two mode flags,
		 * the third parameter is always positional
		 */
		for(j=0; j<2; j++) {
			mode = j == 0 ? (a[i] / 100) % 10 : (a[i] / 1000) % 10;
			if(mode) {
				ops[j] = a[i+j+1];
			}
			else {
				ops[j] = a[a[i+j+1]];
			}
		}
		/* run program */
		switch(op) {
			case OP_ADD:
				a[a[i+3]] = ops[0] + ops[1];
				oplen = 4;
				break;
			case OP_MUL:
				a[a[i+3]] = ops[0] * ops[1];
				oplen = 4;
				break;
			case OP_INP:
				a[a[i+1]] = input;
				oplen = 2;
				break;
			case OP_OUT:
				output = ops[0];
				oplen = 2;
				break;
			case OP_JNZ:
				oplen = 3;
				if(ops[0]) {
					i = ops[1];
					oplen = 0;
				}
				break;
			case OP_JEZ:
				oplen = 3;
				if(!ops[0]) {
					i = ops[1];
					oplen = 0;
				}
				break;
			case OP_SLT:
				a[a[i+3]] = ops[0] < ops[1] ? 1 : 0;
				oplen = 4;
				break;
			case OP_SEQ:
				a[a[i+3]] = ops[0] == ops[1] ? 1 : 0;
				oplen = 4;
				break;
			case OP_FIN:
				return output;
			default:
				return -1;
		}
	}
}

int part1(int a[SIZE])
{
	return run_program(a, 1);
}

int part2(int a[SIZE])
{
	return run_program(a, 5);
}

int main(int argc, char **argv)
{
	int i, m;
	static int a[SIZE];
	static int b[SIZE];

	i = 0;
	for(i=0; scanf("%d,", &m) != EOF; i++) {
		a[i] = m;
	}

	/* make backup of a in b */
	memcpy(b, a, SIZE * sizeof(int));

	printf("part1: %d\n", part1(a));
	
	/* restore backup for part 2 */
	memcpy(a, b, SIZE * sizeof(int));
	
	printf("part2: %d\n", part2(a));

	return 0;
}
