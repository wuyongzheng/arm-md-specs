## C7.2.36 CMLE (zero)

Compare signed less than or equal to zero (vector)

This instruction reads each vector element in the source SIMD&amp;FP register and if the signed integer value is less than or equal to zero sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to one, otherwise sets every bit of the corresponding vector element in the destination SIMD&amp;FP register to zero.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
CMLE D<d>, D<n>, #0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size != '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = esize; constant integer elements = 1;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
CMLE <Vd>.<T>, <Vn>.<T>, #0
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;n&gt;

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

- &lt;Vd&gt; Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;T&gt;

&lt;Vn&gt;

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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; integer element; for e = 0 to elements-1 element = SInt(Elem[operand, e, esize]); Elem[result, e, esize] = if element <= 0 then Ones(esize) else Zeros(esize); V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
