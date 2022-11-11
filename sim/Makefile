TESTS += bit_full_adder
TESTS += four_bits
TESTS += multiplier
TESTS += asic_multiplier

.PHONY: $(TESTS)

.PHONY: all clean
all: $(TESTS)

$(TESTS):
	@cd $@ && $(MAKE)

clean:
	$(foreach TEST, $(TESTS), $(MAKE) -C $(TEST))