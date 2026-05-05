## C7.2.108 FCVTZU (vector, fixed-point)

Floating-point convert to unsigned fixed-point, rounding toward zero (vector)

This instruction converts a scalar or each element in a vector from floating-point to fixed-point unsigned integer using the Round towards Zero rounding mode, and writes the result to the general-purpose destination register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTZU <V><d>, <V><n>, #<fbits>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh IN {'000x'} || (immh IN {'001x'} && !IsFeatureImplemented(FEAT_FP16)) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = if immh IN {'1xxx'} then 64 else if immh IN {'01xx'} then 32 else 16; constant integer datasize = esize; constant integer elements = 1; constant integer fracbits = (esize * 2) UInt(immh:immb); constant boolean unsigned = TRUE; constant FPRounding rounding = FPRounding_ZERO;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
FCVTZU <Vd>.<T>, <Vn>.<T>, #<fbits>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh IN {'000x'} || (immh IN {'001x'} && !IsFeatureImplemented(FEAT_FP16)) then EndOfDecode(Decode_UNDEF); if immh<3>:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = if immh IN {'1xxx'} then 64 else if immh IN {'01xx'} then 32 else 16; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer fracbits = (esize * 2) UInt(immh:immb); constant boolean unsigned = TRUE; constant FPRounding rounding = FPRounding_ZERO;
```

## Assembler Symbols

&lt;V&gt;

Is a width specifier, encoded in 'immh':

| immh   | <V>      | Architectural Feature   |
|--------|----------|-------------------------|
| 0001   | RESERVED | -                       |
| 001x   | H        | FEAT_FP16               |
| 01xx   | S        | -                       |
| 1xxx   | D        | -                       |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;d&gt;

&lt;n&gt;

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;fbits&gt;

For the 'Scalar' variant: is the number of fractional bits, in the range 1 to the operand width, encoded in 'immh:immb':

| immh   | <fbits>               |
|--------|-----------------------|
| 0001   | RESERVED              |
| 001x   | 32 - UInt(immh:immb)  |
| 01xx   | 64 - UInt(immh:immb)  |
| 1xxx   | 128 - UInt(immh:immb) |

For the 'Vector' variant: is the number of fractional bits, in the range 1 to the element width, encoded in 'immh:immb':

## &lt;Vd&gt;

&lt;T&gt;

| immh   | <fbits>               |
|--------|-----------------------|
| 0001   | RESERVED              |
| 001x   | 32 - UInt(immh:immb)  |
| 01xx   | 64 - UInt(immh:immb)  |
| 1xxx   | 128 - UInt(immh:immb) |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'immh:Q':

| immh   | Q   | <T>      | Architectural Feature   |
|--------|-----|----------|-------------------------|
| 0001   | x   | RESERVED | -                       |
| 001x   | 0   | 4H       | FEAT_FP16               |
| 001x   | 1   | 8H       | FEAT_FP16               |
| 01xx   | 0   | 2S       | -                       |
| 01xx   | 1   | 4S       | -                       |
| 1xxx   | 0   | RESERVED | -                       |
| 1xxx   | 1   | 2D       | -                       |

## &lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; constant boolean merge = elements == 1 && IsMerging(FPCR); bits(128) result = if merge then V[d, 128] else Zeros(128); bits(esize) element; for e = 0 to elements-1 element = Elem[operand, e, esize]; Elem[result, e, esize] = FPToFixed(element, fracbits, unsigned, FPCR, rounding, esize); V[d, 128] = result;
```
