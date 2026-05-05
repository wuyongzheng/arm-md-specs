## C7.2.39 CNT

Population count per byte

This instruction counts the number of bits that have a value of one in each vector element in the source SIMD&amp;FP register, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
CNT <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size != '00' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV 8;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

| size   | Q   | <T>      |
|--------|-----|----------|
| 00     | 0   | 8B       |
| 00     | 1   | 16B      |
| 01     | x   | RESERVED |
| 1x     | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

&lt;T&gt;

&lt;Vn&gt;

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; for e = 0 to elements-1 constant integer count = Elem[result, e, esize] = count<esize-1:0>; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
BitCount(Elem[operand, e, esize]);
```
