set ::env(DESIGN_NAME) asic_multiplier
set ::env(VERILOG_FILES) "\
    $::env(DESIGN_DIR)/bit_full_adder.v \
    $::env(DESIGN_DIR)/n_bit_adder.v \
    $::env(DESIGN_DIR)/seg7.v \
    $::env(DESIGN_DIR)/multiplier.v \
    $::env(DESIGN_DIR)/asic_multiplier.v"
