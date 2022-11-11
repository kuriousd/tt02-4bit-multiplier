//-------------------------------------------------------------------
// Title       : n_bit_adder.v
// Author      : Fernando Dominguez Pousa
// Created     : 30/10/2022
// Description : N_BITS bit adder with carries
//-------------------------------------------------------------------

// `include "bit_full_adder.v"

module n_bit_adder
  #(parameter N_BITS = 4)
    (
      input [N_BITS-1:0] i_a,
      input [N_BITS-1:0] i_b,
      input i_carryin,
      output [N_BITS-1:0] o_sum,
      output o_carryout
    );

wire [N_BITS:0] w_carry;

assign w_carry[0] = i_carryin;
assign o_carryout = w_carry[N_BITS];

genvar i;
// Generate the required adder with N_BITS width specified
generate
  for(i=0; i<N_BITS; i=i+1)
    begin
      bit_full_adder adder_inst
        (
          .i_a_bit(i_a[i]),
          .i_b_bit(i_b[i]),
          .i_carryin(w_carry[i]),
          .o_sum_bit(o_sum[i]),
          .o_carryout(w_carry[i+1])
        );
    end
endgenerate

endmodule
