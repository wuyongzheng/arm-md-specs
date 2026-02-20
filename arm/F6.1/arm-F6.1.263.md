## F6.1.263 VUZP (alias)

Vector Unzip de-interleaves the elements of two vectors.

This is a pseudo-instruction of VTRN. This means:

- The encodings in this description are named to match the encodings of VTRN.
- The assembler syntax is used only for assembly, and is not used on disassembly.
- The description of VTRN gives the operational pseudocode, any CONSTRAINED UNPREDICTABLE behavior, and any operational information for this instruction.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

<!-- image -->

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
VUZP{<c>}{<q>}.32 <Dd>, <Dm>
```

## is equivalent to

```
VTRN{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Assembler Symbols

<!-- image -->

For the 'A1 64-bit SIMD vector' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 64-bit SIMD vector' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

The description of VTRN gives the operational pseudocode for this instruction.

## Operational Information

The description of VTRN gives the operational information for this instruction.