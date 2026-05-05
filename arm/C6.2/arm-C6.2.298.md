## C6.2.298 NOP

## No operation

This instruction does nothing, other than advance the value of the program counter by 4. This instruction can be used for instruction alignment purposes.

Note

The timing effects of including a NOP instruction in a program are not guaranteed. It can increase execution time, leave it unchanged, or even reduce it. Therefore, NOP instructions are not suitable for timing loops.

<!-- image -->

<!-- image -->

## Encoding

NOP

## Decode for this encoding

// Empty.

## Operation

return; // Do nothing
