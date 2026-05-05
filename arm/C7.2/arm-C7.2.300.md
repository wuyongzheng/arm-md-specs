## C7.2.300 SHRN, SHRN2

Shift right narrow (immediate)

This instruction reads each unsigned integer value from the source SIMD&amp;FP register, right shifts each result by an immediate value, puts the final result into a vector, and writes the vector to the lower or upper half of the destination SIMD&amp;FP register. The destination vector elements are half as long as the source vector elements. The results are truncated. For rounded results, see RSHRN.

The SHRN instruction writes the vector to the lower half of the destination register and clears the upper half. The SHRN2 instruction writes the vector to the upper half of the destination register without affecting the other bits of the register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SHRN{2} <Vd>.<Tb>, <Vn>.<Ta>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if immh<3> == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh<2:0>); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = (2 * esize) UInt(immh:immb); constant boolean round = FALSE;
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

## &lt;Tb&gt;

## &lt;Vn&gt;

## &lt;Ta&gt;

Is an arrangement specifier, encoded in 'immh':

| immh   | <Ta>     |
|--------|----------|
| 0001   | 8H       |
| 001x   | 4S       |
| 01xx   | 2D       |
| 1xxx   | RESERVED |

Is an arrangement specifier, encoded in 'immh:Q':

| immh   | Q   | <Tb>     |
|--------|-----|----------|
| 0001   | 0   | 8B       |
| 0001   | 1   | 16B      |
| 001x   | 0   | 4H       |
| 001x   | 1   | 8H       |
| 01xx   | 0   | 2S       |
| 01xx   | 1   | 4S       |
| 1xxx   | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;shift&gt;

Is the right shift amount, in the range 1 to the destination element width in bits, encoded in 'immh:immb':

| immh   | <shift>              |
|--------|----------------------|
| 0001   | 16 - UInt(immh:immb) |
| 001x   | 32 - UInt(immh:immb) |
| 01xx   | 64 - UInt(immh:immb) |
| 1xxx   | RESERVED             |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize*2) operand = V[n, datasize*2]; bits(datasize) result; integer element; for e = 0 to elements-1 element = RShr(UInt(Elem[operand, e, 2*esize]), shift, round);
```

```
Elem[result, e, esize] = element<esize-1:0>; Vpart[d, part, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
