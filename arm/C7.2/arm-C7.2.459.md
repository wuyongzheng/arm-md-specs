## C7.2.459 UZP2

Unzip vectors (secondary)

This instruction reads corresponding odd-numbered vector elements from the two source SIMD&amp;FP registers, places the result from the first source register into consecutive elements in the lower half of a vector, and the result from the second source register into consecutive elements in the upper half of a vector, and writes the vector to the destination SIMD&amp;FP register.

Note

Figure C7-8 UZP1 and UZP2 with the arrangement specifier 8B

<!-- image -->

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding

```
UZP2 <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer part = UInt(op);
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'size:Q':

|   size |   Q | <T>      |
|--------|-----|----------|
|     00 |   0 | 8B       |
|     00 |   1 | 16B      |
|     01 |   0 | 4H       |
|     01 |   1 | 8H       |
|     10 |   0 | 2S       |
|     10 |   1 | 4S       |
|     11 |   0 | RESERVED |
|     11 |   1 | 2D       |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operandl = V[n, datasize]; constant bits(datasize) operandh = V[m, datasize]; bits(datasize) result; constant bits(datasize*2) zipped = operandh:operandl; for e = 0 to elements-1 Elem[result, e, esize] = Elem[zipped, 2*e+part, esize]; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

&lt;T&gt;

&lt;Vn&gt;
