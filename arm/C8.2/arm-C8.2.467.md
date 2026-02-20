## C8.2.467 MOV (SIMD&amp;FP scalar, unpredicated)

Move indexed element or SIMD&amp;FP scalar to vector (unpredicated)

This instruction unconditionally broadcasts the SIMD&amp;FP scalar into each element of the destination vector. This instruction is unpredicated.

This is an alias of DUP (indexed). This means:

- The encodings in this description are named to match the encodings of DUP (indexed).
- The description of DUP (indexed) gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

MOV

&lt;Zd&gt;.&lt;T&gt;, &lt;V&gt;&lt;n&gt;

is equivalent to

DUP

&lt;Zd&gt;.&lt;T&gt;, &lt;Zn&gt;.&lt;T&gt;[0]

and is the preferred disassembly when BitCount(imm2 :: tsz) == 1 .

## Encoding

| MOV              | <Zd>.<T>, <Zn>.<T>[<imm>]   |
|------------------|-----------------------------|
| is equivalent to | is equivalent to            |
| DUP              | <Zd>.<T>, <Zn>.<T>[<imm>]   |

and is the preferred disassembly when BitCount(imm2 :: tsz) &gt; 1 .

## Assembler Symbols

## &lt;Zd&gt;

Is the name of the destination scalable vector register, encoded in the 'Zd' field.

Is the size specifier, encoded in 'tsz':

## &lt;T&gt;

| tsz   | <T>      |
|-------|----------|
| 00000 | RESERVED |
| xxxx1 | B        |
| xxx10 | H        |
| xx100 | S        |

&lt;V&gt;

&lt;n&gt;

## &lt;Zn&gt;

Is the name of the source scalable vector register, encoded in the 'Zn' field.

## &lt;imm&gt;

Is the immediate index, in the range 0 to one less than the number of elements in 512 bits, encoded in 'imm2:tsz'.

## Operation

The description of DUP (indexed) gives the operational pseudocode for this instruction.

## Operational Information

The description of DUP (indexed) gives the operational information for this instruction.

Is a width specifier, encoded in 'tsz':

| tsz   | <T>   |
|-------|-------|
| x1000 | D     |
| 10000 | Q     |

| tsz   | <V>      |
|-------|----------|
| 00000 | RESERVED |
| xxxx1 | B        |
| xxx10 | H        |
| xx100 | S        |
| x1000 | D        |
| 10000 | Q        |

Is the number [0-31] of the source SIMD&amp;FP register, encoded in the 'Zn' field.