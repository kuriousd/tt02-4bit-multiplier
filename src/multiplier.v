//-------------------------------------------------------------------
// Title       : multiplier.v
// Author      : Fernando Dominguez Pousa
// Created     : 30/10/2022
// Description : N_BITS bit multiplier. Result 2*N_BITS
//-------------------------------------------------------------------

/*******************************************************************/
/*                            INCLUDES                             */
/*******************************************************************/

// `include "bit_full_adder.v"

module multiplier
  #(parameter N_BITS = 4)
    (
      input [N_BITS-1:0] i_a,
      input [N_BITS-1:0] i_b,
      output [2*N_BITS-1:0] o_mult
    );

wire [N_BITS-1:0] first_row ;
wire [N_BITS-1:0] second_row;
wire [N_BITS-1:0] third_row ;
wire [N_BITS-1:0] fourth_row;

wire [N_BITS-1:0] first_sum    ;
wire [N_BITS-1:0] first_result;

wire [N_BITS-1:0] second_sum    ;
wire [N_BITS-1:0] second_result;

wire [N_BITS-1:0] third_sum;

wire first_cout ;
wire second_cout;
wire third_cout ;

assign first_row  = {1'b0, i_a[3] & i_b[0], i_a[2] & i_b[0], i_a[1] & i_b[0]};
assign second_row = {i_a[3] & i_b[1], i_a[2] & i_b[1], i_a[1] & i_b[1], i_a[0] & i_b[1]};
assign third_row  = {i_a[3] & i_b[2], i_a[2] & i_b[2], i_a[1] & i_b[2], i_a[0] & i_b[2]};
assign fourth_row = {i_a[3] & i_b[3], i_a[2] & i_b[3], i_a[1] & i_b[3], i_a[0] & i_b[3]};

assign first_result  = {first_cout, first_sum[N_BITS-1:1]};
assign second_result = {second_cout, second_sum[N_BITS-1:1]};

assign o_mult = {third_cout, third_sum, second_sum[0], first_sum[0], i_a[0] & i_b[0]};

n_bit_adder first_adder
  (
    .i_a(first_row),
    .i_b(second_row),
    .i_carryin(1'b0),
    .o_sum(first_sum),
    .o_carryout(first_cout)
  );

n_bit_adder second_adder
  (
    .i_a(first_result),
    .i_b(third_row),
    .i_carryin(1'b0),
    .o_sum(second_sum),
    .o_carryout(second_cout)
  );

n_bit_adder third_adder
  (
    .i_a(second_result),
    .i_b(fourth_row),
    .i_carryin(1'b0),
    .o_sum(third_sum),
    .o_carryout(third_cout)
  );

endmodule
