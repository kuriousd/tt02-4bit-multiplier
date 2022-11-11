# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer

import mult_model

PERIOD = 10

@cocotb.test()
async def mult_4bit_test(dut):

  for i in range(16):
    for j in range(16):
      a = i
      b = j

      dut.i_a.value = a
      dut.i_b.value = b

      await Timer(2, units="ns")

      mult = mult_model.four_bits_multiplier(a, b)

      assert (dut.o_mult.value ==  mult), "A = {A} B = {B}  Expected mult = {exp} Actual mult = {actual}".format(
          A=a, B=b, exp=mult, actual=dut.o_mult.value
      )
