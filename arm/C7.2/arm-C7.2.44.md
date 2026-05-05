## C7.2.44 EXT

Extract vector from pair of vectors

This instruction extracts the lowest vector elements from the second source SIMD&amp;FP register and the highest vector elements from the first source SIMD&amp;FP register, concatenates the results into a vector, and writes the vector to the destination SIMD&amp;FP register vector. The index value specifies the lowest vector element to extract from the first source register, and consecutive elements are extracted from the first, then second, source registers until the destination vector is filled.

Figure C7-1 EXT doubleword operation for Q = 0 and imm4&lt;2:0&gt; = 3

<!-- image -->

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
EXT
```

```
<Vd>.<T>, <Vn>.<T>, <Vm>.<T>, #<index>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if Q == '0' && imm4<3> == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 64 << UInt(Q); constant integer position = 8 * UInt(imm4);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;T&gt;

## &lt;Vn&gt;

Is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;index&gt;

Is the lowest numbered byte element to be extracted, encoded in 'Q:imm4':

|   Q | imm4<3>   | <index>         |
|-----|-----------|-----------------|
|   0 | 0         | UInt(imm4<2:0>) |
|   0 | 1         | RESERVED        |
|   1 | x         | UInt(imm4)      |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) hi = V[m, datasize]; constant bits(datasize) lo = V[n, datasize]; constant bits(datasize*2) concat = hi : lo; V[d, datasize] = concat<(position+datasize)-1:position>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
