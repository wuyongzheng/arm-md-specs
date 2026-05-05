## C7.2.243 MOV (element)

Move vector element to another vector element

This instruction copies the vector element of the source SIMD&amp;FP register to the specified vector element of the destination SIMD&amp;FP register.

This instruction can insert data into individual elements within a SIMD&amp;FP register without clearing the remaining bits to zero.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of INS (element). This means:

- The encodings in this description are named to match the encodings of INS (element).
- The description of INS (element) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

| MOV              | <Vd>.<Ts>[<index1>], <Vn>.<Ts>[<index2>]   |
|------------------|--------------------------------------------|
| is equivalent to | is equivalent to                           |
| INS              | <Vd>.<Ts>[<index1>], <Vn>.<Ts>[<index2>]   |

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

## &lt;index1&gt;

Is the destination element index encoded in 'imm5':

## &lt;Vn&gt;

| imm5   | <index1>        |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;index2&gt;

Is the source element index encoded in 'imm5:imm4':

| imm5   | <index2>        |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm4)      |
| xxx10  | UInt(imm4<3:1>) |
| xx100  | UInt(imm4<3:2>) |
| x1000  | UInt(imm4<3>)   |

Unspecified bits in 'imm4' are ignored but should be set to zero by an assembler.

## Operation

The description of INS (element) gives the operational pseudocode for this instruction.

## Operational Information

The description of INS (element) gives the operational information for this instruction.
