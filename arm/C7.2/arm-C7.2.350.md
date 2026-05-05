## C7.2.350 SQSHRUN, SQSHRUN2

Signed saturating shift right unsigned narrow (immediate)

This instruction reads each signed integer value in the vector of the source SIMD&amp;FP register, right shifts each value by an immediate value, saturates the result to an unsigned integer value that is half the original width, places the final result into a vector, and writes the vector to the destination SIMD&amp;FP register. The results are truncated. For rounded results, see SQRSHRUN.

The SQSHRUN instruction writes the vector to the lower half of the destination register and clears the upper half. The SQSHRUN2 instruction writes the vector to the upper half of the destination register without affecting the other bits of the register.

If saturation occurs, the cumulative saturation bit FPSR.QC is set.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSHRUN <Vb><d>, <Va><n>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh == '0000' then EndOfDecode(Decode_UNDEF); if immh<3> == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh<2:0>); constant integer datasize = esize; constant integer elements = 1; constant integer part = 0; constant integer shift = (2 * esize) UInt(immh:immb); constant boolean round = FALSE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQSHRUN{2} <Vd>.<Tb>, <Vn>.<Ta>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if immh<3> == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh<2:0>); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = (2 * esize) UInt(immh:immb); constant boolean round = FALSE;
```

## Assembler Symbols

&lt;Vb&gt;

Is the destination width specifier, encoded in 'immh':

| immh   | <Vb>     |
|--------|----------|
| 0001   | B        |
| 001x   | H        |
| 01xx   | S        |
| 1xxx   | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the source width specifier, encoded in 'immh':

&lt;d&gt;

&lt;Va&gt;

<!-- image -->

&lt;n&gt;

| immh   | <Va>     |
|--------|----------|
| 0001   | H        |
| 001x   | S        |
| 01xx   | D        |
| 1xxx   | RESERVED |

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the 'Scalar' variant: is the right shift amount, in the range 1 to the destination operand width in bits, encoded in 'immh:immb':

2

## &lt;Vd&gt;

## &lt;Tb&gt;

| immh   | <shift>              |
|--------|----------------------|
| 0001   | 16 - UInt(immh:immb) |
| 001x   | 32 - UInt(immh:immb) |
| 01xx   | 64 - UInt(immh:immb) |
| 1xxx   | RESERVED             |

For the 'Vector' variant: is the right shift amount, in the range 1 to the destination element width in bits, encoded in 'immh:immb':

| immh   | <shift>              |
|--------|----------------------|
| 0001   | 16 - UInt(immh:immb) |
| 001x   | 32 - UInt(immh:immb) |
| 01xx   | 64 - UInt(immh:immb) |
| 1xxx   | RESERVED             |

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'immh:Q':

| immh   |   Q | <Tb>   |
|--------|-----|--------|
| 0001   |   0 | 8B     |
| 0001   |   1 | 16B    |
| 001x   |   0 | 4H     |
| 001x   |   1 | 8H     |
| 01xx   |   0 | 2S     |
| 01xx   |   1 | 4S     |

&lt;Vn&gt;

&lt;Ta&gt;

Is an arrangement specifier, encoded in 'immh':

| immh   | <Ta>     |
|--------|----------|
| 0001   | 8H       |
| 001x   | 4S       |
| 01xx   | 2D       |
| 1xxx   | RESERVED |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize*2) operand = V[n, datasize*2]; bits(datasize) result; integer element; boolean sat; for e = 0 to elements-1 element = RShr(SInt(Elem[operand, e, 2*esize]), shift, round); (Elem[result, e, esize], sat) = UnsignedSatQ(element, esize); if sat then FPSR.QC = '1'; Vpart[d, part, datasize] = result;
```

| immh   | Q   | <Tb>     |
|--------|-----|----------|
| 1xxx   | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.
