## C7.2.361 SSHR

Signed shift right (immediate)

This instruction reads each vector element in the source SIMD&amp;FP register, right shifts each result by an immediate value, places the final result into a vector, and writes the vector to the destination SIMD&amp;FP register. All the values in this instruction are signed integer values. The results are truncated. For rounded results, see SRSHR.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SSHR D<d>, D<n>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if immh<3> != '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << 3; constant integer datasize = esize; constant integer elements = 1; constant integer shift = (esize * 2) -UInt(immh:immb); constant boolean unsigned = FALSE; constant boolean round = FALSE;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SSHR <Vd>.<T>, <Vn>.<T>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if immh<3>:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = (esize * 2) -UInt(immh:immb); constant boolean unsigned = FALSE; constant boolean round = FALSE;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;n&gt;

Is the number of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the 'Scalar' variant: is the right shift amount, in the range 1 to 64, encoded as 128 - UInt('immh:immb') .

For the 'Vector' variant: is the right shift amount, in the range 1 to the element width in bits, encoded in 'immh:immb':

| immh   | <shift>               |
|--------|-----------------------|
| 0001   | 16 - UInt(immh:immb)  |
| 001x   | 32 - UInt(immh:immb)  |
| 01xx   | 64 - UInt(immh:immb)  |
| 1xxx   | 128 - UInt(immh:immb) |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'immh:Q':

| immh   |   Q | <T>   |
|--------|-----|-------|
| 0001   |   0 | 8B    |
| 0001   |   1 | 16B   |
| 001x   |   0 | 4H    |
| 001x   |   1 | 8H    |
| 01xx   |   0 | 2S    |

## &lt;Vd&gt;

&lt;T&gt;

&lt;Vn&gt;

| immh   |   Q | <T>      |
|--------|-----|----------|
| 01xx   |   1 | 4S       |
| 1xxx   |   0 | RESERVED |
| 1xxx   |   1 | 2D       |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; integer element; for e = 0 to elements-1 constant bits(esize) opelt = Elem[operand, e, esize]; if unsigned then element = RShr(UInt(opelt), shift, round); else element = RShr(SInt(opelt), shift, round); Elem[result, e, esize] = element<esize-1:0>; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
