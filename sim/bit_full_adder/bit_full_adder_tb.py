# -*- coding: utf-8 -*-
import cocotb
from cocotb.triggers import Timer
from cocotb.regression import TestFactory

PERIOD = 10

@cocotb.test()
async def sum_1bit_test(dut):

  dut.i_a_bit.value = 0
  dut.i_b_bit.value = 0
  dut.i_carryin.value = 0

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 0
  assert dut.o_carryout.value == 0

  dut.i_a_bit.value = 0
  dut.i_b_bit.value = 0
  dut.i_carryin.value = 1

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 1
  assert dut.o_carryout.value == 0

  dut.i_a_bit.value = 1
  dut.i_b_bit.value = 0
  dut.i_carryin.value = 1

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 0
  assert dut.o_carryout.value == 1

  dut.i_a_bit.value = 0
  dut.i_b_bit.value = 1
  dut.i_carryin.value = 1

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 0
  assert dut.o_carryout.value == 1

  dut.i_a_bit.value = 1
  dut.i_b_bit.value = 1
  dut.i_carryin.value = 0

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 0
  assert dut.o_carryout.value == 1

  dut.i_a_bit.value = 1
  dut.i_b_bit.value = 0
  dut.i_carryin.value = 0

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 1
  assert dut.o_carryout.value == 0

  dut.i_a_bit.value = 0
  dut.i_b_bit.value = 1
  dut.i_carryin.value = 0

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 1
  assert dut.o_carryout.value == 0

  dut.i_a_bit.value = 1
  dut.i_b_bit.value = 1
  dut.i_carryin.value = 1

  await Timer(20*PERIOD, units='ns')
  assert dut.o_sum_bit.value == 1
  assert dut.o_carryout.value == 1

# Register the test.
factory = TestFactory(sum_1bit_test)
factory.generate_tests()
    