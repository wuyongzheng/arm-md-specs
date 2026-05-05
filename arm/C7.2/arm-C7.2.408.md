## C7.2.408 UADDLV

Unsigned sum long across vector

This instruction adds every vector element in the source SIMD&amp;FP register together, and writes the scalar result to the destination SIMD&amp;FP register. The destination scalar is twice as long as the source vector elements. All the values in this instruction are unsigned integer values.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UADDLV <V><d>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF);
```

```
if size:Q == '100' then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant boolean unsigned = TRUE;
```

## Assembler Symbols

<!-- image -->

&lt;V&gt;

Is the destination width specifier, encoded in 'size':

<!-- image -->

|   size | <V>      |
|--------|----------|
|     00 | H        |
|     01 | S        |
|     10 | D        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

&lt;Vn&gt;

<!-- image -->

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | 0   | 8B       |
|     00 | 1   | 16B      |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | RESERVED |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(esize) opelt = Elem[operand, 0, esize]; integer sum = if unsigned then UInt(opelt) else SInt(opelt); for e = 1 to elements-1 opelt = Elem[operand, e, esize]; constant integer element = if unsigned then UInt(opelt) else SInt(opelt); sum = sum + element; V[d, 2*esize] = sum<2*esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
