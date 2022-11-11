# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/../../src/bit_full_adder.v
VERILOG_SOURCES += $(PWD)/../../src/n_bit_adder.v
VERILOG_SOURCES += $(PWD)/../../src/multiplier.v
VERILOG_SOURCES += $(PWD)/../../src/seg7.v
VERILOG_SOURCES += $(PWD)/../../src/asic_multiplier.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = asic_multiplier

# MODULE is the basename of the Python test file
MODULE = asic_multiplier_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim