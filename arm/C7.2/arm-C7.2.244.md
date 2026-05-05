## C7.2.244 MOV (from general)

Move general-purpose register to a vector element

This instruction copies the contents of the source general-purpose register to the specified vector element in the destination SIMD&amp;FP register.

This instruction can insert data into individual elements within a SIMD&amp;FP register without clearing the remaining bits to zero.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of INS (general). This means:

- The encodings in this description are named to match the encodings of INS (general).
- The description of INS (general) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

| MOV              | <Vd>.<Ts>[<index>], <R><n>   |
|------------------|------------------------------|
| is equivalent to | is equivalent to             |
| INS              | <Vd>.<Ts>[<index>], <R><n>   |

and is always the preferred disassembly.

## Assembler Symbols

## &lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an element size specifier, encoded in 'imm5':

## &lt;Ts&gt;

| imm5   | <Ts>     |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

## &lt;index&gt;

Is the element index encoded in 'imm5':

<!-- image -->

<!-- image -->

Is the number [0-30] of the general-purpose source register or ZR (31), encoded in the 'Rn' field.

## Operation

The description of INS (general) gives the operational pseudocode for this instruction.

## Operational Information

The description of INS (general) gives the operational information for this instruction.

| imm5   | <index>         |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |

Is the width specifier for the general-purpose source register, encoded in 'imm5':

| imm5   | <R>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | W        |
| xxx10  | W        |
| xx100  | W        |
| x1000  | X        |
