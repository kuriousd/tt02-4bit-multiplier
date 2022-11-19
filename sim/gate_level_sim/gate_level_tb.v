//-------------------------------------------------------------------
// Title       : gate_level.v
// Author      : Fernando Dominguez Pousa
// Created     : 12/11/2022
// Description : Wrapper to fulfill TT02 interface requirements
//-------------------------------------------------------------------

`default_nettype none
`timescale 1ns/1ps

module gate_level_tb (
    input        clk        ,
    input        reset      ,
    input  [2:0] i_factor_a ,
    input  [2:0] i_factor_b ,
    output [6:0] o_segments ,
    output       o_lsb_digit
);

    // wire up the inputs and outputs
    wire [7:0] inputs  = {i_factor_b, i_factor_a, reset, clk};
    wire [7:0] outputs;                                       ;

    assign o_segments  = outputs[6:0];
    assign o_lsb_digit = outputs[7];


    // instantiate the DUT
    asic_multiplier_wrapper asic_multiplier_wrapper (
        `ifdef GL_TEST
        .vccd1 (1'b1   ),
        .vssd1 (1'b0   ),
        `endif
        
        .io_in (inputs ),
        .io_out(outputs)
    );

    // this part dumps the trace to a vcd file that can be viewed with GTKWave
    initial begin
        $dumpfile ("gate_level_tb.vcd");
        $dumpvars (0, gate_level_tb);
        #1;
    end

endmodule