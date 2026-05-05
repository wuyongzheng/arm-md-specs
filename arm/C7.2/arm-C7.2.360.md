## C7.2.360 SSHLL, SSHLL2

Signed shift left long (immediate)

This instruction reads each vector element from the source SIMD&amp;FP register, left shifts each vector element by the specified shift amount, places the result into a vector, and writes the vector to the destination SIMD&amp;FP register. The destination vector elements are twice as long as the source vector elements. All the values in this instruction are signed integer values.

The SSHLL instruction extracts vector elements from the lower half of the source register. The SSHLL2 instruction extracts vector elements from the upper half of the source register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias SXTL, SXTL2.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
SSHLL{2} <Vd>.<Ta>, <Vn>.<Tb>, #<shift>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if immh<3> == '1' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << HighestSetBitNZ(immh<2:0>); constant integer datasize = 64; constant integer part = UInt(Q); constant integer elements = datasize DIV esize; constant integer shift = UInt(immh:immb) esize; constant boolean unsigned = FALSE;
```

## Assembler Symbols

2

Is the second and upper half specifier. If present it causes the operation to be performed on the upper 64 bits of the registers holding the narrower elements, and is encoded in 'Q':

|   Q | 2         |
|-----|-----------|
|   0 | [absent]  |
|   1 | [present] |

&lt;Vd&gt;

&lt;Ta&gt;

## &lt;Vn&gt;

## &lt;Tb&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'immh':

## Alias Conditions

| immh   | <Ta>     |
|--------|----------|
| 0001   | 8H       |
| 001x   | 4S       |
| 01xx   | 2D       |
| 1xxx   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

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

## &lt;shift&gt;

Is the left shift amount, in the range 0 to the source element width in bits minus 1, encoded in 'immh:immb':

| immh   | <shift>              |
|--------|----------------------|
| 0001   | UInt(immh:immb) - 8  |
| 001x   | UInt(immh:immb) - 16 |
| 01xx   | UInt(immh:immb) - 32 |
| 1xxx   | RESERVED             |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = Vpart[n, part, datasize]; bits(datasize*2) result; for e = 0 to elements-1 constant bits(esize) opelt = Elem[operand, e, esize]; constant integer element = if unsigned then UInt(opelt) else SInt(opelt); Elem[result, e, 2*esize] = (element << shift)<2*esize-1:0>; V[d, datasize*2] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

| Alias       | Is preferred when                    |
|-------------|--------------------------------------|
| SXTL, SXTL2 | immb == '000' && BitCount(immh) == 1 |
