# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer

from cocotb.binary import BinaryValue

import random
import sum_model

PERIOD = 10

@cocotb.test()
async def sum_4bit_test(dut):

  for i in range(10):

      a = random.randint(0, 15)
      b = random.randint(0, 15)
      cin = random.randint(0, 1)

      dut.i_a.value = a
      dut.i_b.value = b
      dut.i_carryin.value = cin

      await Timer(2, units="ns")

      carry, sum = sum_model.four_bits_adder(a, b, cin)

      assert (dut.o_sum.value ==  sum), "Expected sum = {exp} Actual sum = {actual}".format(
          exp=sum, actual=dut.o_sum.value
      )

      assert (dut.o_carryout.value ==  carry), "Expected sum = {exp} Actual sum = {actual}".format(
          exp=sum, actual=dut.o_sum.value
      )
