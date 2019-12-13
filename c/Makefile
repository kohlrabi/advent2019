.PHONY: all clean

CFLAGS=-Wall -O3

BINS=`ls *.c | sed 's/\.c//'`


all:
	make $(BINS)

clean:
	rm -f $(BINS)

run: all
	@echo
	@for i in $(BINS); do \
		echo "$$i"; \
		echo "----------------"; \
		./$$i < ../input/$$i.input; \
		echo; \
	done;
