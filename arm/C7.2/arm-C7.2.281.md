## C7.2.281 SDOT (by element)

Dot product signed arithmetic (vector, by element)

This instruction performs the dot product of the four 8-bit elements in each 32-bit element of the first source register with the four 8-bit elements of an indexed 32-bit element in the second source register, accumulating the result into the corresponding 32-bit element of the destination register.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

In Armv8.2 and Armv8.3, this is an OPTIONAL instruction. From Armv8.4 it is mandatory for all implementations to support it.

Note

ID\_AA64ISAR0\_EL1.DP indicates whether this instruction is supported.

## Vector

(FEAT\_DotProd)

<!-- image -->

## Encoding

```
SDOT <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.4B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_DotProd) then EndOfDecode(Decode_UNDEF);
```

```
if size != '10' then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(M:Rm); constant integer index = UInt(H:L); constant integer esize = 8 << UInt(size); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV esize;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP third source and destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Ta&gt;

|   Q | <Ta>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

## &lt;Vn&gt;

&lt;Tb&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;index&gt;

Is the element index, encoded in the 'H:L' fields.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(128) operand2 = V[m, 128]; bits(datasize) result = V[d, datasize]; for e = 0 to elements-1 integer res = 0; integer element1, element2; for i = 0 to 3 element1 = SInt(Elem[operand1, 4 * e + i, esize DIV 4]); element2 = SInt(Elem[operand2, 4 * index + i, esize res = res + element1 * element2; Elem[result, e, esize] = Elem[result, e, esize] + res; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   Q | <Tb>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |

```
DIV 4]);
```
