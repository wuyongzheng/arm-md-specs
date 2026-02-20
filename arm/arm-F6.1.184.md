## F6.1.184 VQRSHRN (zero)

Vector Saturating Rounding Shift Right, Narrow takes each element in a quadword vector of integers, right shifts them by an immediate value, and places the signed rounded results in a doubleword vector.

This is a pseudo-instruction of VQMOVN, VQMOVUN. This means:

- The encodings in this description are named to match the encodings of VQMOVN, VQMOVUN.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of VQMOVN, VQMOVUN gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Signed result variant

<!-- image -->

T1

<!-- image -->

## Encoding for the Signed result variant

```
VQRSHRN{<c>}{<q>}.<dt> <Dd>, <Qm>, #0
```

## is equivalent to

```
VQMOVN{<c>}{<q>}.<dt> <Dd>, <Qm>
```

## Assembler Symbols

<!-- image -->

For the 'A1 Signed result' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Signed result' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

&lt;dt&gt;

## &lt;Dd&gt;

Is the data type for the elements of the operand, encoded in 'op:size':

| op   |   size | <dt>     |
|------|--------|----------|
| 10   |     00 | S16      |
| 10   |     01 | S32      |
| 10   |     10 | S64      |
| 1x   |     11 | RESERVED |
| 11   |     00 | U16      |
| 11   |     01 | U32      |
| 11   |     10 | U64      |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

The description of VQMOVN, VQMOVUN gives the operational pseudocode for this instruction.