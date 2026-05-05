## C7.2.407 UADDLP

Unsigned add long pairwise

This instruction adds pairs of adjacent unsigned integer values from the vector in the source SIMD&amp;FP register, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the source vector elements.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UADDLP <Vd>.<Ta>, <Vn>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV (2 * esize);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <Ta>     |
|--------|-----|----------|
|     00 | 0   | 4H       |
|     00 | 1   | 8H       |
|     01 | 0   | 2S       |
|     01 | 1   | 4S       |
|     10 | 0   | 1D       |
|     10 | 1   | 2D       |
|     11 | x   | RESERVED |

&lt;Ta&gt;

&lt;Vn&gt;

&lt;Tb&gt;

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

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

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = bits(datasize) result; bits(2*esize) sum; integer op1; integer op2; for e = 0 to elements-1 op1 = UInt(Elem[operand, 2*e+0, esize]); op2 = UInt(Elem[operand, 2*e+1, esize]); sum = (op1+op2)<2*esize-1:0>; Elem[result, e, 2*esize] = sum; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
V[n, datasize];
```
