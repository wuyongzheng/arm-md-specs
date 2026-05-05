## C7.2.421 UMAXV

Unsigned maximum across vector

This instruction compares all the vector elements in the source SIMD&amp;FP register, and writes the largest of the values as a scalar to the destination SIMD&amp;FP register. All the values in this instruction are unsigned integer values.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UMAXV <V><d>, <Vn>.<T>
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

<!-- image -->

&lt;Vn&gt;

|   size | <V>      |
|--------|----------|
|     00 | B        |
|     01 | H        |
|     10 | S        |
|     11 | RESERVED |

Is the number of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;T&gt;

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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(esize) opelt = Elem[operand, 0, esize]; integer max = if unsigned then UInt(opelt) else SInt(opelt); for e = 1 to elements-1 opelt = Elem[operand, e, esize]; constant integer element = if unsigned then UInt(opelt) else SInt(opelt); max = Max(max, element); V[d, esize] = max<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
