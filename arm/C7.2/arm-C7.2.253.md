## C7.2.253 NOT

Bitwise NOT (vector)

This instruction reads each vector element from the source SIMD&amp;FP register, places the inverse of each value into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

This instruction is used by the alias MVN.

## Vector

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
NOT <Vd>.<T>, <Vn>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer esize = 8; constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV 8;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

<!-- image -->

<!-- image -->

|   Q | <T>   |
|-----|-------|
|   0 | 8B    |
|   1 | 16B   |

Is the name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Alias Conditions

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand = bits(datasize) result; bits(esize) element; for e = 0 to elements-1 element = Elem[operand, e, esize]; Elem[result, e, esize] = NOT(element); V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
V[n, datasize];
```

| Alias   | Is preferred when   |
|---------|---------------------|
| MVN     | Unconditionally     |
