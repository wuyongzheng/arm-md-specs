## C8.2.288 INSR (scalar)

Insert general-purpose register in shifted vector

This instruction shifts the destination vector left by one element, and then places a copy of the least-significant bits of the general-purpose register in element 0 of the destination vector. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INSR <Zdn>.<T>, <R><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn); constant integer m = UInt(Rm);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

&lt;T&gt;

<!-- image -->

Is the size specifier, encoded in 'size':

Is a width specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

|   size | <R>   |
|--------|-------|
|     00 | W     |
|     01 | W     |

&lt;m&gt;

Is the number [0-30] of the source general-purpose register or the name ZR (31), encoded in the 'Rm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) dest = Z[dn, VL]; constant bits(esize) src = X[m, esize]; Z[dn, VL] = dest<(VL-esize)-1:0> : src;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

|   size | <R>   |
|--------|-------|
|     10 | W     |
|     11 | X     |