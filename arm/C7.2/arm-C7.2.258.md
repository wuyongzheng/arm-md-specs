## C7.2.258 PMULL, PMULL2

Polynomial multiply long

This instruction multiplies corresponding elements in the lower or upper half of the vectors of the two source SIMD&amp;FP registers, places the results in a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the elements that are multiplied.

For information about multiplying polynomials, see Polynomial arithmetic over {0, 1}.

The PMULL instruction extracts each source vector from the lower half of each source register. The PMULL2 instruction extracts each source vector from the upper half of each source register.

The PMULL and PMULL2 variants that operate on 64-bit source elements are defined only when FEAT\_PMULL is implemented.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers, not all the same type (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
PMULL{2} <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.<Tb>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '01' || size == '10' then EndOfDecode(Decode_UNDEF); if size == '11' && !IsFeatureImplemented(FEAT_PMULL) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize;
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

&lt;Ta&gt;

## &lt;Vn&gt;

&lt;Tb&gt;

Is an arrangement specifier, encoded in 'size':

|   size | <Ta>     |
|--------|----------|
|     00 | 8H       |
|     01 | RESERVED |
|     10 | RESERVED |
|     11 | 1Q       |

The '1Q' arrangement is only allocated in an implementation that includes the Cryptographic Extension, and is otherwise RESERVED.

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <Tb>     |
|--------|-----|----------|
|     00 | 0   | 8B       |
|     00 | 1   | 16B      |
|     01 | x   | RESERVED |
|     10 | x   | RESERVED |
|     11 | 0   | 1D       |
|     11 | 1   | 2D       |

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = Vpart[n, part, datasize]; constant bits(datasize) operand2 = Vpart[m, part, datasize]; bits(2*datasize) result; bits(esize) element1; bits(esize) element2; for e = 0 to elements-1 element1 = Elem[operand1, e, esize]; element2 = Elem[operand2, e, esize]; Elem[result, e, 2*esize] = PolynomialMult(element1, element2); V[d, 2*datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
