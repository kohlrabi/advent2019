#include <stdio.h>
#include <string.h>
#include <math.h>

#define SIZE (1024*1024*10)

/* available opcodes */
enum ops {
	OP_ADD = 1,
	OP_MUL = 2,
	OP_INP = 3,
	OP_OUT = 4,
	OP_FIN = 99
};

int run_program(int *a, int input)
{
	int i, j;
	int oplen = 4;
	int output;
	int op;
	int mode;
	int ops[2];

	for(i=0;; i+=oplen) {
		/* extract opcode */
		op = a[i] % 100;
		/* extract mode flags
		 * 0: position mode
		 * 1: immediate mode
		 */
		for(j=1; j<3; j++) {
			mode = (int)(a[i]/pow(10, j+1)) % (int)pow(10, j);
			if(mode) {
				ops[j-1] = a[i+j];
			}
			else {
				ops[j-1] = a[a[i+j]];
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
				if(output && a[i+2] != OP_FIN) {
					return -1;
				}
				oplen = 2;
				break;
			case OP_FIN:
				return output;
			default:
				return -1;
		}
	}
}

int part1(int a[SIZE*2])
{
	return run_program(a, 1);
}

int main(int argc, char **argv)
{
	int i, m;
	static int a[SIZE*2];

	i = 0;
	for(i=0; scanf("%d,", &m) != EOF; i++) {
		a[i] = m;
	}

	memcpy(a+SIZE, a, SIZE * sizeof(int));

	printf("part1: %d\n", part1(a));

	return 0;
}
