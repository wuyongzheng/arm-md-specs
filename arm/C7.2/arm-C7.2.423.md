## C7.2.423 UMINP

Unsigned minimum pairwise

This instruction creates a vector by concatenating the vector elements of the first source SIMD&amp;FP register after the vector elements of the second source SIMD&amp;FP register, reads each pair of adjacent vector elements in the two source SIMD&amp;FP registers, writes the smallest of each pair of unsigned integer values into a vector, and writes the vector to the destination SIMD&amp;FP register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Three registers of the same type (FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
UMINP <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size == '11' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size | Q   | <T>      |
|--------|-----|----------|
|     00 | 0   | 8B       |
|     00 | 1   | 16B      |
|     01 | 0   | 4H       |
|     01 | 1   | 8H       |
|     10 | 0   | 2S       |
|     10 | 1   | 4S       |
|     11 | x   | RESERVED |

<!-- image -->

&lt;T&gt;

&lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; constant bits(2*datasize) concat = operand2:operand1; integer element1; integer element2; integer min; for e = 0 to elements-1 element1 = UInt(Elem[concat, 2*e, esize]); element2 = UInt(Elem[concat, (2*e)+1, esize]); min = Min(element1, element2); Elem[result, e, esize] = min<esize-1:0>; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.
