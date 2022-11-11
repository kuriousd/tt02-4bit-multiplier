//-------------------------------------------------------------------
// Title       : bit_full_adder.v
// Author      : Fernando Dominguez Pousa
// Created     : 30/10/2022
// Description : One bit adder with carries
//-------------------------------------------------------------------

module bit_full_adder (
  input  i_a_bit   ,
  input  i_b_bit   ,
  input  i_carryin ,
  output o_sum_bit ,
  output o_carryout
);

  wire w_sum_ab ;
  wire w_carry_1;
  wire w_carry_2;

  assign w_sum_ab  = i_a_bit ^ i_b_bit;
  assign w_carry_1 = i_a_bit & i_b_bit;
  assign w_carry_2 = w_sum_ab & i_carryin;

  assign o_sum_bit  = w_sum_ab ^ i_carryin;
  assign o_carryout = w_carry_1 | w_carry_2;

endmodule
