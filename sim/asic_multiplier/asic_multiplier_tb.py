# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer, ClockCycles

import asic_multiplier_models

PERIOD = 10

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(161250):
        dut.clk.value = 0
        await Timer(200, units="us")
        dut.clk.value = 1
        await Timer(200, units="us")

@cocotb.test()
async def asic_multiplier_test(dut):

  await cocotb.start(generate_clock(dut))  # run the clock "in the background"

  # Set the reset
  dut.reset.value = 1

  await Timer(500, units="us")

  dut.reset.value = 0

  await Timer(100, units="us")

  for i in range(8):
    for j in range(8):
      a = i
      b = j


      dut.i_factor_a.value = a
      dut.i_factor_b.value = b

      await ClockCycles(dut.clk, 1253)

      mult = a * b
      segment_lsb = asic_multiplier_models.seven_segs_to_number(dut.o_segments.value)

      assert (dut.o_lsb_digit == 1), "LED showing LSB nibble is not HIGH"

      await ClockCycles(dut.clk, 1253)

      segment_msb = asic_multiplier_models.seven_segs_to_number(dut.o_segments.value)
      seg_result = asic_multiplier_models.digits_to_number(segment_msb, segment_lsb)

      assert (dut.o_lsb_digit == 0), "LED showing MSB nibble is not LOW"

      assert (mult ==  seg_result), "A = {A} B = {B}  Expected mult = {exp} Actual mult = {actual}".format(
          A=a, B=b, exp=mult, actual=seg_result
      )
    
