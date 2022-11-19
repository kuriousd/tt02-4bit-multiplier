# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

# gate level simulation requires some extra setup
COMPILE_ARGS    += -DGL_TEST
COMPILE_ARGS    += -DFUNCTIONAL
COMPILE_ARGS    += -DUSE_POWER_PINS
COMPILE_ARGS    += -DSIM
COMPILE_ARGS    += -DUNIT_DELAY=#1
VERILOG_SOURCES += $(PDK_ROOT)/sky130B/libs.ref/sky130_fd_sc_hd/verilog/primitives.v
VERILOG_SOURCES += $(PDK_ROOT)/sky130B/libs.ref/sky130_fd_sc_hd/verilog/sky130_fd_sc_hd.v

# copy the gatelevel verilog from /runs/wokwi/results/final/verilog/gl/ and commit to this directory
VERILOG_SOURCES += $(PWD)/gate_level_tb.v 
VERILOG_SOURCES += $(PWD)/asic_multiplier_wrapper_gl.v

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = gate_level_tb

# MODULE is the basename of the Python test file
MODULE = gate_level_tb

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim