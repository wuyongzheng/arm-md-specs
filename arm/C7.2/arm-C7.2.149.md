## C7.2.149 FMLS (by element)

Floating-point fused multiply-subtract from accumulator (by element)

This instruction multiplies the vector elements in the first source SIMD&amp;FP register by the specified value in the second source SIMD&amp;FP register, and subtracts the results from the vector elements of the destination SIMD&amp;FP register. All the values in this instruction are floating-point values.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 4 classes: Scalar, half-precision, Scalar, single-precision and double-precision, Vector, half-precision, and Vector, single-precision and double-precision

## Scalar, half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FMLS
```

```
<Hd>, <Hn>, <Vm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer idxdsize = 64 << UInt(H); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Rd); constant integer index = UInt(H:L:M); constant integer esize = 16; constant integer datasize = esize; constant integer elements = 1;
```

Scalar, single-precision and double-precision

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FMLS <V><d>, <V><n>, <Vm>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer idxdsize = 64 << UInt(H); integer index; constant bit Rmhi = M; case sz:L of when '0x' index = UInt(H:L); when '10' index = UInt(H); when '11' EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 32 << UInt(sz); constant integer datasize = esize; constant integer elements = 1;
```

## Vector, half-precision

(FEAT\_AdvSIMD &amp;&amp; FEAT\_FP16)

<!-- image -->

## Encoding

```
FMLS <Vd>.<T>, <Vn>.<T>, <Vm>.H[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) || !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer idxdsize = 64 << UInt(H); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer d = UInt(Rd); constant integer index = UInt(H:L:M); constant integer esize = 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

Vector, single-precision and double-precision (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FMLS <Vd>.<T>, <Vn>.<T>, <Vm>.<Ts>[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if sz:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer idxdsize = 64 << UInt(H); integer index; constant bit Rmhi = M; case sz:L of when '0x' index = UInt(H:L); when '10' index = UInt(H); when '11' EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rmhi:Rm); constant integer esize = 32 << UInt(sz); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

For the 'Scalar, half-precision' and 'Vector, half-precision' variants: is the name of the second SIMD&amp;FP source register, in the range V0 to V15, encoded in the 'Rm' field.

For the 'Scalar, single-precision and double-precision' and 'Vector, single-precision and double-precision' variants: is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;index&gt;

For the 'Scalar, half-precision' and 'Vector, half-precision' variants: is the element index, in the range 0 to 7, encoded in the 'H:L:M' fields.

For the 'Scalar, single-precision and double-precision' and 'Vector, single-precision and double-precision' variants: is the element index, encoded in 'sz:L:H':

|   sz | L   | <index>   |
|------|-----|-----------|
|    0 | x   | UInt(H:L) |
|    1 | 0   | UInt(H)   |
|    1 | 1   | RESERVED  |

Is a width specifier, encoded in 'sz':

&lt;V&gt;

- &lt;d&gt;
- &lt;n&gt;

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

- &lt;Ts&gt; Is an element size specifier, encoded in 'sz':

&lt;Vn&gt;

|   sz | <V>   |
|------|-------|
|    0 | S     |
|    1 | D     |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

|   sz | <Ts>   |
|------|--------|
|    0 | S      |
|    1 | D      |

- &lt;Vd&gt; Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
- &lt;T&gt; For the 'Vector, half-precision' variant: is an arrangement specifier, encoded in 'Q':

|   Q | <T>   |
|-----|-------|
|   0 | 4H    |
|   1 | 8H    |

For the 'Vector, single-precision and double-precision' variant: is an arrangement specifier, encoded in 'Q:sz':

|   Q |   sz | <T>      |
|-----|------|----------|
|   0 |    0 | 2S       |
|   0 |    1 | RESERVED |
|   1 |    0 | 4S       |
|   1 |    1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(idxdsize) operand2 = V[m, idxdsize]; constant bits(datasize) operand3 = V[d, datasize]; bits(esize) element1; constant bits(esize) element2 = Elem[operand2, index, esize]; constant boolean merge = elements == 1 && IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); for e = 0 to elements-1 element1 = FPNeg(Elem[operand1, e, esize], FPCR); Elem[result, e, esize] = FPMulAdd(Elem[operand3, e, esize], element1, element2, FPCR); V[d, 128] = result;
```
