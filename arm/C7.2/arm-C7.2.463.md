## C7.2.463 ZIP2

Zip vectors (secondary)

This instruction reads adjacent vector elements from the upper half of two source SIMD&amp;FP registers as pairs, interleaves the pairs and places them into a vector, and writes the vector to the destination SIMD&amp;FP register. The first pair from the first source register is placed into the two lowest vector elements, with subsequent pairs taken alternately from each source register.

Note

Figure C7-10 ZIP1 and ZIP2 with the arrangement specifier 8B

<!-- image -->

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Advanced SIMD

(FEAT\_AdvSIMD)

<!-- image -->

## Encoding

```
ZIP2 <Vd>.<T>, <Vn>.<T>, <Vm>.<T>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AdvSIMD) then EndOfDecode(Decode_UNDEF); if size:Q == '110' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize; constant integer part = UInt(op); constant integer pairs = elements DIV 2;
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
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; bits(datasize) result; constant integer base = part * pairs; for p = 0 to pairs-1 Elem[result, 2*p+0, esize] = Elem[operand1, base+p, esize]; Elem[result, 2*p+1, esize] = Elem[operand2, base+p, esize]; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

&lt;T&gt;

&lt;Vn&gt;

## Chapter C8 SVE Instruction Descriptions

This chapter describes the SVE instructions. It contains the following sections:

- About the SVE instructions.
- Alphabetical list of SVE instructions.
