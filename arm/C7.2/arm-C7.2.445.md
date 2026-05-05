## C7.2.445 URSQRTE

Unsigned reciprocal square root estimate

This instruction reads each vector element from the source SIMD&amp;FP register, calculates an approximate inverse square root for each value, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register. All the values in this instruction are unsigned integer values.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
URSQRTE <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); if sz == '1' then EndOfDecode(Decode_UNDEF); constant integer esize = 32; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'sz:Q':

|   sz | Q   | <T>      |
|------|-----|----------|
|    0 | 0   | 2S       |
|    0 | 1   | 4S       |
|    1 | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;T&gt;

&lt;Vn&gt;

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; bits(32) element; for e = 0 to elements-1 element = Elem[operand, e, 32]; Elem[result, e, 32] = V[d, datasize] = result;
```

```
UnsignedRSqrtEstimate(element);
```
