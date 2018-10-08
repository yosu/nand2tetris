load Decode.hdl,
output-file Decode.out,
compare-to Decode.cmp,
output-list instruction%B1.16.1
            i%B1.1.1
            value%B1.15.1
            a%B1.1.1
            zx%B2.1.1
            nx%B2.1.1
            zy%B2.1.1
            ny%B2.1.1
            f%B1.1.1
            no%B2.1.1
            da%B2.1.1
            dd%B2.1.1
            dm%B2.1.1
            jl%B2.1.1
            je%B2.1.1
            jg%B2.1.1;

set instruction %B0000000000000000,
eval,
output;

set instruction %B0100000000000001,
eval,
output;

set instruction %B0111111111111111,
eval,
output;

set instruction %B1000000000000000,
eval,
output;

set instruction %B1110000000000000,
eval,
output;

set instruction %B1001010101010101,
eval,
output;

set instruction %B1000101010101010,
eval,
output;

// Test for c instruction part
set instruction %B1000100000000000,
eval,
output;

set instruction %B1000010000000000,
eval,
output;

set instruction %B1000001000000000,
eval,
output;

set instruction %B1000000100000000,
eval,
output;

set instruction %B1000000010000000,
eval,
output;

set instruction %B1000000001000000,
eval,
output;

// Test for dest part
set instruction %B1000000000100000,
eval,
output;

set instruction %B1000000000010000,
eval,
output;

set instruction %B1000000000001000,
eval,
output;

// Test for jump part
set instruction %B1000000000000100,
eval,
output;

set instruction %B1000000000000010,
eval,
output;

set instruction %B1000000000000001,
eval,
output;
