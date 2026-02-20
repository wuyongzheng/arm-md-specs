## C8.2.289 INSR (SIMD&amp;FP scalar)

Insert SIMD&amp;FP scalar register in shifted vector

This instruction shifts the destination vector left by one element, and then places a copy of the SIMD&amp;FP scalar register in element 0 of the destination vector. This instruction is unpredicated.

## SVE

(FEAT\_SVE || FEAT\_SME)

<!-- image -->

## Encoding

```
INSR <Zdn>.<T>, <V><m>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) && !IsFeatureImplemented(FEAT_SME) then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer dn = UInt(Zdn); constant integer m = UInt(Vm);
```

## Assembler Symbols

## &lt;Zdn&gt;

Is the name of the source and destination scalable vector register, encoded in the 'Zdn' field.

<!-- image -->

&lt;T&gt;

&lt;V&gt;

Is the size specifier, encoded in 'size':

Is a width specifier, encoded in 'size':

|   size | <T>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |

&lt;m&gt;

```
esize]; src;
```

|   size | <V>   |
|--------|-------|
|     10 | S     |
|     11 | D     |

Is the number [0-31] of the source SIMD&amp;FP register, encoded in the 'Vm' field.

## Operation

```
CheckSVEEnabled(); constant integer VL = CurrentVL; constant bits(VL) dest = Z[dn, VL]; constant bits(esize) src = V[m, Z[dn, VL] = dest<(VL-esize)-1:0> :
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.