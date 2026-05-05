## C7.2.341 SQRDMULH (by element)

Signed saturating rounding doubling multiply returning high half (by element)

This instruction multiplies each vector element in the first source SIMD&amp;FP register by the specified vector element of the second source SIMD&amp;FP register, doubles the results, places the most significant half of the final results into a vector, and writes the vector to the destination SIMD&amp;FP register.

The results are rounded. For truncated results, see SQDMULH.

If any of the results overflows, they are saturated. If saturation occurs, the cumulative saturation bit FPSR.QC is set.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQRDMULH <V><d>, <V><n>, V<m>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer idxdsize = 64 << UInt(H); integer index; bit Rmhi; case size of when '01' index = UInt(H:L:M); Rmhi = '0'; when '10' index = UInt(H:L); Rmhi = M; otherwise EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1; constant boolean round = TRUE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SQRDMULH <Vd>.<T>, <Vn>.<T>, V<m>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer idxdsize = 64 << UInt(H); integer index; bit Rmhi; case size of when '01' index = UInt(H:L:M); Rmhi = '0'; when '10' index = UInt(H:L); Rmhi = M; otherwise EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean round = TRUE;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'size':

&lt;d&gt;

&lt;n&gt;

&lt;m&gt;

|   size | <V>      |
|--------|----------|
|     00 | RESERVED |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is the number of the second SIMD&amp;FP source register, encoded in 'size:M:Rm':

|   size | <m>          |
|--------|--------------|
|     00 | RESERVED     |
|     01 | UInt('0':Rm) |
|     10 | UInt(M:Rm)   |

## &lt;Ts&gt;

Is an element size specifier, encoded in 'size':

## &lt;index&gt;

Is the element index, encoded in 'size:H:L:M':

## &lt;Vd&gt;

&lt;T&gt;

## &lt;Vn&gt;

Restricted to 0-15 when element size &lt;Ts&gt; is H.

|   size | <m>      |
|--------|----------|
|     11 | RESERVED |

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

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | x   | RESERVED |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(idxdsize) operand2 = V[m, idxdsize]; bits(datasize) result; integer element1; integer element2; integer product; boolean sat; element2 = SInt(Elem[operand2, index, esize]); for e = 0 to elements-1 element1 = SInt(Elem[operand1, e, esize]); product = 2 * element1 * element2; product = RShr(product, esize, round); // The following only saturates if element1 and element2 (Elem[result, e, esize], sat) = SignedSatQ(product, esize); if sat then FPSR.QC = '1'; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
equal -(2^(esize-1))
```
