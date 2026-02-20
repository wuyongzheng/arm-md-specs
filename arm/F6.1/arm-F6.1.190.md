## F6.1.190 VQSHRUN (zero)

Vector Saturating Shift Right, Narrow takes each element in a quadword vector of integers, right shifts them by an immediate value, and places the unsigned truncated results in a doubleword vector.

This is a pseudo-instruction of VQMOVN, VQMOVUN. This means:

- The encodings in this description are named to match the encodings of VQMOVN, VQMOVUN.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of VQMOVN, VQMOVUN gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Unsigned result variant

<!-- image -->

T1

<!-- image -->

## Encoding for the Unsigned result variant

```
VQSHRUN{<c>}{<q>}.<dt> <Dd>, <Qm>, #0
```

## is equivalent to

```
VQMOVUN{<c>}{<q>}.<dt> <Dd>, <Qm>
```

## Assembler Symbols

<!-- image -->

For the 'A1 Unsigned result' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Unsigned result' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

<!-- image -->

## &lt;Dd&gt;

Is the data type for the elements of the operand, encoded in 'size':

|   size | <dt>     |
|--------|----------|
|     00 | S16      |
|     01 | S32      |
|     10 | S64      |
|     11 | RESERVED |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

The description of VQMOVN, VQMOVUN gives the operational pseudocode for this instruction.