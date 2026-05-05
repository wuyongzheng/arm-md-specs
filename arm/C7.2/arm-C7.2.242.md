## C7.2.242 MOV (scalar)

Move vector element to scalar

This instruction duplicates the specified vector element in the SIMD&amp;FP source register into a scalar, and writes the result to the SIMD&amp;FP destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This is an alias of DUP (element). This means:

- The encodings in this description are named to match the encodings of DUP (element).
- The description of DUP (element) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

MOV

&lt;V&gt;&lt;d&gt;, &lt;Vn&gt;.&lt;T&gt;[&lt;index&gt;]

is equivalent to

DUP

&lt;V&gt;&lt;d&gt;, &lt;Vn&gt;.&lt;T&gt;[&lt;index&gt;]

and is always the preferred disassembly.

## Assembler Symbols

<!-- image -->

&lt;V&gt;

Is the destination width specifier, encoded in 'imm5':

| imm5   | <V>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

&lt;Vn&gt;

&lt;T&gt;

Is the element width specifier, encoded in 'imm5':

## &lt;index&gt;

Is the element index encoded in 'imm5':

## Operation

The description of DUP (element) gives the operational pseudocode for this instruction.

## Operational Information

The description of DUP (element) gives the operational information for this instruction.

| imm5   | <T>      |
|--------|----------|
| x0000  | RESERVED |
| xxxx1  | B        |
| xxx10  | H        |
| xx100  | S        |
| x1000  | D        |

| imm5   | <index>         |
|--------|-----------------|
| x0000  | RESERVED        |
| xxxx1  | UInt(imm5<4:1>) |
| xxx10  | UInt(imm5<4:2>) |
| xx100  | UInt(imm5<4:3>) |
| x1000  | UInt(imm5<4>)   |
