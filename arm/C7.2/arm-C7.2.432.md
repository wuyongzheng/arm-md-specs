## C7.2.432 UMULL, UMULL2 (vector)

Unsigned multiply long (vector)

This instruction multiplies corresponding vector elements in the lower or upper half of the two source SIMD&amp;FP registers, places the result in a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the elements that are multiplied. All the values in this instruction are unsigned integer values.

The UMULL instruction extracts each source vector from the lower half of each source register. The UMULL2 instruction extracts each source vector from the upper half of each source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers, not all the same type

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UMULL{2} <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

- 2 Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the

registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vd&gt;

&lt;Ta&gt;

&lt;Vn&gt;

&lt;Tb&gt;

Is an arrangement specifier, encoded in 'size':

|   size | <Ta>     |
|--------|----------|
|     00 | 8H       |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

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

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = Vpart[n, part, datasize]; constant bits(datasize) operand2 = Vpart[m, part, datasize]; bits(2*datasize) result; integer element1; integer element2; for e = 0 to elements-1 element1 = UInt(Elem[operand1, e, esize]); element2 = UInt(Elem[operand2, e, esize]); Elem[result, e, 2*esize] = (element1 * element2)<2*esize-1:0>; V[d, 2*datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
