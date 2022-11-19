ifneq ($(GATES),yes)
TESTS += bit_full_adder
TESTS += four_bits
TESTS += multiplier
TESTS += asic_multiplier
TESTS += asic_multiplier_wrapper
else
TESTS += gate_level_sim
endif

.PHONY: $(TESTS)

.PHONY: all clean
all: $(TESTS)

$(TESTS):
	@cd $@ && $(MAKE)

clean:
	$(foreach TEST, $(TESTS), $(MAKE) -C $(TEST))