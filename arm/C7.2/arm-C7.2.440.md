## C7.2.440 UQXTN, UQXTN2

Unsigned saturating extract narrow

This instruction reads each vector element from the source SIMD&amp;FP register, saturates each value to half the original width, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register. All the values in this instruction are unsigned integer values.

If saturation occurs, the cumulative saturation bit FPSR.QC is set.

The UQXTN instruction writes the vector to the lower half of the destination register and clears the upper half. The UQXTN2 instruction writes the vector to the upper half of the destination register without affecting the other bits of the register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UQXTN <Vb><d>, <Va><n>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer part = 0; constant integer elements = 1; constant boolean unsigned = TRUE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

UQXTN{2}

&lt;Vd&gt;.&lt;Tb&gt;, &lt;Vn&gt;.&lt;Ta&gt;

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize; constant boolean unsigned = TRUE;
```

## Assembler Symbols

## &lt;Vb&gt;

Is the destination width specifier, encoded in 'size':

&lt;d&gt;

&lt;Va&gt;

&lt;n&gt;

2

|   size | <Vb>     |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the source width specifier, encoded in 'size':

|   size | <Va>     |
|--------|----------|
|     00 | H        |
|     01 | S        |
|     10 | D        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

&lt;Vd&gt;

&lt;Tb&gt;

## &lt;Vn&gt;

## &lt;Ta&gt;

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(2*datasize) operand = V[n, 2*datasize]; bits(datasize) result; bits(2*esize) element; boolean sat; for e = 0 to elements-1 element = Elem[operand, e, 2*esize]; (Elem[result, e, esize], sat) = if sat then FPSR.QC = '1'; Vpart[d, part, datasize] = result;
```

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <Tb>     |
|--------|-----|----------|
|     00 | 0   | 8B       |
|     00 | 1   | 16B      |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'size':

|   size | <Ta>     |
|--------|----------|
|     00 | 8H       |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

```
SatQ(UInt(element), esize, unsigned);
```
