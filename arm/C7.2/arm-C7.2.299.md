## C7.2.299 SHLL, SHLL2

Shift left long (by element size)

This instruction reads each vector element in the lower or upper half of the source SIMD&amp;FP register, left shifts each result by the element size, writes the final result to a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the source vector elements.

The SHLL instruction extracts vector elements from the lower half of the source register. The SHLL2 instruction extracts vector elements from the upper half of the source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SHLL{2} <Vd>.<Ta>, <Vn>.<Tb>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
constant integer d = UInt(Rd); constant integer n = UInt(Rn); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = esize;
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

## &lt;Ta&gt;

## &lt;Vn&gt;

## &lt;Tb&gt;

Is an arrangement specifier, encoded in 'size':

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = Vpart[n, part, datasize]; bits(2*datasize) result; integer element; for e = 0 to elements-1 element = SInt(Elem[operand, e, esize]) << shift;
```

|   size | <Ta>     |
|--------|----------|
|     00 | 8H       |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

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

## &lt;shift&gt;

Is the left shift amount, which must be equal to the source element width in bits, encoded in 'size':

|   size | <shift>   |
|--------|-----------|
|     00 | 8         |
|     01 | 16        |
|     10 | 32        |
|     11 | RESERVED  |

```
Elem[result, e, 2*esize] = element<2*esize-1:0>; V[d, 2*datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
