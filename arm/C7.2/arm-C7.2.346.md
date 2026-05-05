## C7.2.346 SQSHL (immediate)

Signed saturating shift left (immediate)

This instruction reads each vector element in the source SIMD&amp;FP register, shifts each result by an immediate value, places the final result in a vector, and writes the vector to the destination SIMD&amp;FP register. The results are truncated. For rounded results, see UQRSHL.

If overflow occurs with any of the results, those results are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSHL <V><d>, <V><n>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh == '0000' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh); constant integer datasize = esize; constant integer elements = 1; constant integer shift = UInt(immh:immb) esize; constant boolean src_unsigned = FALSE; constant boolean dst_unsigned = FALSE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSHL <Vd>.<T>, <Vn>.<T>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if immh<3>:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = UInt(immh:immb) esize; constant boolean src_unsigned = FALSE; constant boolean dst_unsigned = FALSE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'immh':

&lt;d&gt;

&lt;n&gt;

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the 'Scalar' variant: is the left shift amount, in the range 0 to the operand width in bits minus 1, encoded in 'immh:immb':

| immh   | <shift>              |
|--------|----------------------|
| 0001   | UInt(immh:immb) - 8  |
| 001x   | UInt(immh:immb) - 16 |
| 01xx   | UInt(immh:immb) - 32 |
| 1xxx   | UInt(immh:immb) - 64 |

For the 'Vector' variant: is the left shift amount, in the range 0 to the element width in bits minus 1, encoded in 'immh:immb':

| immh   | <V>   |
|--------|-------|
| 0001   | B     |
| 001x   | H     |
| 01xx   | S     |
| 1xxx   | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

<!-- image -->

&lt;T&gt;

&lt;Vn&gt;

| immh   | <shift>              |
|--------|----------------------|
| 0001   | UInt(immh:immb) - 8  |
| 001x   | UInt(immh:immb) - 16 |
| 01xx   | UInt(immh:immb) - 32 |
| 1xxx   | UInt(immh:immb) - 64 |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'immh:Q':

| immh   |   Q | <T>      |
|--------|-----|----------|
| 0001   |   0 | 8B       |
| 0001   |   1 | 16B      |
| 001x   |   0 | 4H       |
| 001x   |   1 | 8H       |
| 01xx   |   0 | 2S       |
| 01xx   |   1 | 4S       |
| 1xxx   |   0 | RESERVED |
| 1xxx   |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; boolean sat; for e = 0 to elements-1 constant bits(esize) opelt = Elem[operand, e, esize]; constant integer element = if src_unsigned then UInt(opelt) else SInt(opelt); (Elem[result, e, esize], sat) = SatQ(element << shift, esize, dst_unsigned); if sat then FPSR.QC = '1'; V[d, datasize] = result;
```
