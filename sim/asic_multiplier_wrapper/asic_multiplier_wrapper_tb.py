# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer

import asic_multiplier_models

PERIOD = 10

async def generate_clock(dut):
    """Generate clock pulses."""

    for cycle in range(161250):
        dut.io_in[0].value = 0
        await Timer(200, units="us")
        dut.io_in[0].value = 1
        await Timer(200, units="us")

@cocotb.test()
async def asic_multiplier_test(dut):

  await cocotb.start(generate_clock(dut))  # run the clock "in the background"

  # Set the reset
  dut.io_in[1].value = 1

  await Timer(500, units="us")

  dut.io_in[1].value = 0

  await Timer(100, units="us")

  a = 7
  b = 7

  dut.io_in[2].value = 1
  dut.io_in[3].value = 1
  dut.io_in[4].value = 1
  dut.io_in[5].value = 1
  dut.io_in[6].value = 1
  dut.io_in[7].value = 1

  await Timer(501, units="ms")

  mult = a * b

  output = dut.io_out.value
  o_segments = (output & 0x7F)
  o_lsb_digit = (output & 0x80) >> 7

  segment_lsb = asic_multiplier_models.seven_segs_to_number(o_segments)

  assert (o_lsb_digit == 1), "LED showing LSB nibble is not HIGH"

  await Timer(500, units="ms")

  output = dut.io_out.value
  o_segments = (output & 0x7F)
  o_lsb_digit = (output & 0x80) >> 7

  segment_msb = asic_multiplier_models.seven_segs_to_number(o_segments)
  seg_result = asic_multiplier_models.digits_to_number(segment_msb, segment_lsb)

  assert (o_lsb_digit == 0), "LED showing MSB nibble is not LOW"

  assert (mult ==  seg_result), "A = {A} B = {B}  Expected mult = {exp} Actual mult = {actual}".format(
      A=a, B=b, exp=mult, actual=seg_result
  )
    
