## C7.2.263 REV32 (vector)

Reverse elements in 32-bit words (vector)

This instruction reverses the order of 8-bit or 16-bit elements in each word of the vector in the source SIMD&amp;FP register, places the results into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
REV32 <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer csize = 64 >> UInt(o0:U); constant integer esize = 8 << UInt(size); if csize <= esize then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer datasize = 64 << UInt(Q); constant integer containers = datasize DIV csize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

| size   | Q   | <T>      |
|--------|-----|----------|
| 00     | 0   | 8B       |
| 00     | 1   | 16B      |
| 01     | 0   | 4H       |
| 01     | 1   | 8H       |
| 1x     | x   | RESERVED |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

<!-- image -->

&lt;T&gt;

&lt;Vn&gt;

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = V[n, datasize]; bits(datasize) result; for c = 0 to containers-1 constant bits(csize) container = Elem[operand, c, Elem[result, c, csize] = Reverse(container, esize); V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
csize];
```
