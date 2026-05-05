## C7.2.328 SQDMLAL, SQDMLAL2 (by element)

Signed saturating doubling multiply-add long (by element)

This instruction multiplies each vector element in the lower or upper half of the first source SIMD&amp;FP register by the specified vector element of the second source SIMD&amp;FP register, doubles the results, and accumulates the final results with the vector elements of the destination SIMD&amp;FP register. The destination vector elements are twice as long as the elements that are multiplied.

If overflow occurs with any of the results, those results are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

The SQDMLAL instruction extracts vector elements from the lower half of the first source register. The SQDMLAL2 instruction extracts vector elements from the upper half of the first source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQDMLAL <Va><d>, <Vb><n>, V<m>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer idxdsize = 64 << UInt(H); integer index; bit Rmhi; case size of when '01' index = UInt(H:L:M); Rmhi = '0'; when '10' index = UInt(H:L); Rmhi = M; otherwise EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant integer part = 0;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQDMLAL{2} <Vd>.<Ta>, <Vn>.<Tb>, V<m>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer idxdsize = 64 << UInt(H); integer index; bit Rmhi; case size of when '01' index = UInt(H:L:M); Rmhi = '0'; when '10' index = UInt(H:L); Rmhi = M; otherwise EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Va&gt;

Is the destination width specifier, encoded in 'size':

&lt;d&gt;

&lt;Vb&gt;

<!-- image -->

&lt;n&gt;

|   size | <Va>     |
|--------|----------|
|     00 | RESERVED |
|     01 | S        |
|     10 | D        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the source width specifier, encoded in 'size':

|   size | <Vb>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;m&gt;

## &lt;Ts&gt;

Is an element size specifier, encoded in 'size':

## &lt;index&gt;

Is the element index, encoded in 'size:H:L:M':

2

Is the number of the second SIMD&amp;FP source register, encoded in 'size:M:Rm':

|   size | <m>          |
|--------|--------------|
|     00 | RESERVED     |
|     01 | UInt('0':Rm) |
|     10 | UInt(M:Rm)   |
|     11 | RESERVED     |

|   size | <Ts>     |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

|   size | <index>     |
|--------|-------------|
|     00 | RESERVED    |
|     01 | UInt(H:L:M) |
|     10 | UInt(H:L)   |
|     11 | RESERVED    |

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Restricted to 0-15 when element size &lt;Ts&gt; is H.

&lt;Vd&gt;

&lt;Ta&gt;

&lt;Vn&gt;

&lt;Tb&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size':

|   size | <Ta>     |
|--------|----------|
|     00 | RESERVED |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <Tb>     |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = Vpart[n, part, datasize]; constant bits(idxdsize) operand2 = V[m, idxdsize]; constant bits(2*datasize) operand3 = V[d, 2*datasize]; bits(2*datasize) result; integer element1; integer element2; bits(2*esize) product; integer accum; boolean sat1; boolean sat2; element2 = SInt(Elem[operand2, index, esize]); for e = 0 to elements-1 element1 = SInt(Elem[operand1, e, esize]); (product, sat1) = SignedSatQ(2 * element1 * element2, 2 * esize); accum = SInt(Elem[operand3, e, 2*esize]) + SInt(product); (Elem[result, e, 2*esize], sat2) = SignedSatQ(accum, 2 * esize); if sat1 || sat2 then FPSR.QC = '1'; V[d, 2*datasize] = result;
```
