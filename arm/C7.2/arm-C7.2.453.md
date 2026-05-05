## C7.2.453 USQADD

Unsigned saturating accumulate of signed value

This instruction adds the signed integer values of the vector elements in the source SIMD&amp;FP register to corresponding unsigned integer values of the vector elements in the destination SIMD&amp;FP register, and accumulates the resulting unsigned integer values with the vector elements of the destination SIMD&amp;FP register.

If overflow occurs with any of the results, those results are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
USQADD <V><d>, <V><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant boolean unsigned = TRUE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
USQADD <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean unsigned = TRUE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

&lt;d&gt;

&lt;n&gt;

&lt;Vd&gt;

&lt;T&gt;

&lt;Vn&gt;

|   size | <V>   |
|--------|-------|
|     00 | B     |
|     01 | H     |
|     10 | S     |
|     11 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>      |
|--------|-----|----------|
|     00 |   0 | 8B       |
|     00 |   1 | 16B      |
|     01 |   0 | 4H       |
|     01 |   1 | 8H       |
|     10 |   0 | 2S       |
|     10 |   1 | 4S       |
|     11 |   0 | RESERVED |
|     11 |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; constant bits(datasize) operand2 = V[d, datasize]; integer op1; integer op2; boolean sat; for e = 0 to elements-1 op1 = SInt(Elem[operand, e, esize]); op2 = UInt(Elem[operand2, e, esize]); (Elem[result, e, esize], sat) = SatQ(op1 + op2, if sat then FPSR.QC = '1'; V[d, datasize] = result;
```

```
esize, unsigned);
```
