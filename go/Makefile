.PHONY: all

BUILD=go build

RUN=go run

BINS=`ls *.go | sed 's/\.go//'`


all:
	@for i in $(BINS); do \
		$(BUILD) $$i.go; \
	done;

clean:
	rm $(BINS)

run:
	@echo
	@for i in $(BINS); do \
		echo "$$i"; \
		echo "----------------"; \
		$(RUN) $$i.go < ../input/$$i.input; \
		echo; \
	done;



