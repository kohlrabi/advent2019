.PHONY: all clean

CFLAGS=-Wall -O3
LDLIBS=-lm

all:
	make `ls *.c | sed 's/\.c//'`

clean:
	rm `ls *.c | sed 's/\.c//'`
