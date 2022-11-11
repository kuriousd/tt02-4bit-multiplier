
`default_nettype none

module asic_multiplier #(parameter MAX_COUNT = 1250) (
    input        clk        , // external clock is 2500Hz
    input        reset      ,
    input  [2:0] i_factor_a ,
    input  [2:0] i_factor_b ,
    output [6:0] o_segments ,
    output       o_lsb_digit
);

    integer product   ;
    wire [6:0] seven_segs;

    assign o_segments  = seven_segs;
    assign o_lsb_digit = r_lsb_led;

    // 12 bits to count up to 2500
    reg [11:0] r_counter  ;
    reg [ 3:0] r_fact_a   ;
    reg [ 3:0] r_fact_b   ;
    reg [ 3:0] r_digit    ;
    reg        r_lsb_digit;
    reg        r_lsb_led  ;
    reg        r_trigger  ;

    always @(posedge clk) begin
        // if reset, set r_counter to 0
        if (reset) begin
            r_lsb_digit <= 0;
            r_counter   <= 0;
            r_lsb_led   <= 0;
            r_fact_a   <= 0;
            r_fact_b   <= 0;
            r_trigger   <= 0;

        end else begin
            // if up to 16e6
            if (r_counter == MAX_COUNT) begin
                // reset
                r_counter <= 0;
                r_trigger <= 1;

                // Create the multiplication factors
                r_fact_a <= {1'b0, i_factor_a};
                r_fact_b <= {1'b0, i_factor_b};

                // toggle between msb and lsb r_digit
                r_lsb_digit <= ~r_lsb_digit;

            end else begin
                // increment r_counter
                r_counter <= r_counter + 1'b1;
                // register the product and lsb led
                r_lsb_led <= r_lsb_digit;

                // To remove
                r_trigger <= 0; 

                if (r_lsb_digit == 1)
                    r_digit <= product[3:0];
                else
                    r_digit <= product[7:4];

            end

        end
    end

    // Instantiate the multiplier
    multiplier multiplier_8bits (
        .i_a   (r_fact_a),
        .i_b   (r_fact_b),
        .o_mult(product )
    );


    // Instantiate segment display
    seg7 seg7_display (
        .number  (r_digit   ),
        .segments(seven_segs)
    );

    `ifdef COCOTB_SIM
    initial begin
        $dumpfile ("asic_multiplier.vcd");
        $dumpvars (0, clk);
        $dumpvars (1, reset);
        $dumpvars (2, i_factor_a);
        $dumpvars (3, i_factor_b);
        $dumpvars (4, o_segments);
        $dumpvars (5, o_lsb_digit);
        $dumpvars (6, product);
        $dumpvars (7, r_digit);
        $dumpvars (8, r_counter);
        $dumpvars (9, r_trigger);
        $dumpvars (10, r_lsb_digit);
        #1;
    end
    `endif

endmodule