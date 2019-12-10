.PHONY: all clean

CFLAGS=-Wall -O3

all:
	make `ls *.c | sed 's/\.c//'`

clean:
	rm `ls *.c | sed 's/\.c//'`

run: all
	@echo
	@for i in `ls *.c | sed 's/\.c//'`; do \
		echo "$$i"; \
		echo "----------------"; \
		./$$i < ../input/$$i.input; \
		echo; \
	done;
