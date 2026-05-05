## C7.2.298 SHL

Shift left (immediate)

This instruction reads each value from a vector, left shifts each result by an immediate value, writes the final result to a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

It has encodings from 2 classes: Scalar and Vector

## Scalar

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SHL D<d>, D<n>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh<3> != '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << 3; constant integer datasize = esize; constant integer elements = 1; constant integer shift = UInt(immh:immb) esize;
```

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SHL <Vd>.<T>, <Vn>.<T>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh<3>:Q == '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = UInt(immh:immb) esize;
```

## Assembler Symbols

&lt;d&gt;

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->

Is the number of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;shift&gt;

For the 'Scalar' variant: is the left shift amount, in the range 0 to 63, encoded as UInt('immh:immb') - 64 .

For the 'Vector' variant: is the left shift amount, in the range 0 to the element width in bits minus 1, encoded in 'immh:immb':

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

## &lt;Vd&gt;

&lt;T&gt;

&lt;Vn&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; for e = 0 to elements-1 Elem[result, e, esize] = LSL(Elem[operand, e, esize], shift); V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

immh

Q

&lt;T&gt;
