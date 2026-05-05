## C7.2.447 USDOT (by element)

Dot product with unsigned and signed integers (vector, by element)

This instruction performs the dot product of the four unsigned 8-bit integer values in each 32-bit element of the first source register with the four signed 8-bit integer values in an indexed 32-bit element of the second source register, accumulating the result into the corresponding 32-bit element of the destination register.

From Armv8.2 to Armv8.5, this is an OPTIONAL instruction. From Armv8.6 it is mandatory for implementations that include Advanced SIMD to support it. ID\_AA64ISAR1\_EL1.I8MM indicates whether this instruction is supported.

## Vector

(FEAT\_I8MM)

<!-- image -->

## Encoding

```
USDOT <Vd>.<Ta>, <Vn>.<Tb>, <Vm>.4B[<index>]
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_I8MM) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt(M:Rm); constant integer d = UInt(Rd); constant integer i = UInt(H:L); constant integer datasize = 64 << UInt(Q); constant integer elements = datasize DIV 32;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP third source and destination register, encoded in the 'Rd' field.

Is an arrangement specifier, encoded in 'Q':

&lt;Ta&gt;

&lt;Vn&gt;

<!-- image -->

|   Q | <Ta>   |
|-----|--------|
|   0 | 2S     |
|   1 | 4S     |

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

Is an arrangement specifier, encoded in 'Q':

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'M:Rm' fields.

## &lt;index&gt;

Is the immediate index of a 32-bit group of four 8-bit values, in the range 0 to 3, encoded in the 'H:L' fields.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(128) operand2 = V[m, 128]; constant bits(datasize) operand3 = V[d, datasize]; bits(datasize) result; for e = 0 to elements-1 bits(32) res = Elem[operand3, e, 32]; for b = 0 to 3 constant integer element1 = UInt(Elem[operand1, 4 * e + b, 8]); constant integer element2 = SInt(Elem[operand2, 4 * i + b, 8]); res = res + element1 * element2; Elem[result, e, 32] = res; V[d, datasize] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

|   Q | <Tb>   |
|-----|--------|
|   0 | 8B     |
|   1 | 16B    |
