//testbench for and gate

module tb;

    reg A, B;  //input assigned to register

    wire out; //output assigned to net

    //instantiate dut

    and_gate dut(out,A,B);

    initial

    begin

        A = 0; B = 0;#10

        $display("A=%b B=%b Output=%b",A,B,out);

        A = 0; B = 1;#10

        $display("A=%b B=%b Output=%b",A,B,out);

        A = 1; B = 0;#10

        $display("A=%b B=%b Output=%b",A,B,out);

        A = 1; B = 1;#10

        $display("A=%b B=%b Output=%b",A,B,out);

        $finish;

    end

endmodule