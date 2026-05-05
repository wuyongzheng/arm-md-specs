## C7.2.456 USUBW, USUBW2

Unsigned subtract wide

This instruction subtracts each vector element in the lower or upper half of the second source SIMD&amp;FP register from the corresponding vector element in the first source SIMD&amp;FP register, places the result in a vector, and writes the vector to the SIMD&amp;FP destination register. All the values in this instruction are unsigned integer values.

The vector elements of the destination register and the first source register are twice as long as the vector elements of the second source register.

The USUBW instruction extracts vector elements from the lower half of the second source register. The USUBW2 instruction extracts vector elements from the upper half of the second source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers, not all the same type (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
USUBW{2} <Vd>.<Ta>, <Vn>.<Ta>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

<!-- image -->

## &lt;Ta&gt;

## &lt;Vn&gt;

Is an arrangement specifier, encoded in 'size':

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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(2*datasize) operand1 = V[n, 2*datasize]; constant bits(datasize) operand2 = bits(2*datasize) result; integer element1; integer element2; integer sum; for e = 0 to elements-1 element1 = UInt(Elem[operand1, e, 2*esize]); element2 = UInt(Elem[operand2, e, esize]); sum = element1 - element2; Elem[result, e, 2*esize] = sum<2*esize-1:0>; V[d, 2*datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   size | <Ta>     |
|--------|----------|
|     00 | 8H       |
|     01 | 4S       |
|     10 | 2D       |
|     11 | RESERVED |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Tb&gt;

```
Vpart[m, part, datasize];
```
