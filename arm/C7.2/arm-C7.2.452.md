## C7.2.452 USMMLA (vector)

Unsigned and signed 8-bit integer matrix multiply-accumulate to 32-bit integer (vector)

This instruction multiplies the 2x8 matrix of unsigned 8-bit integer values in the first source vector by the 8x2 matrix of signed 8-bit integer values in the second source vector. The resulting 2x2 32-bit integer matrix product is destructively added to the 32-bit integer matrix accumulator in the destination vector. This is equivalent to performing an 8-way dot product per destination element.

From Armv8.2 to Armv8.5, this is an OPTIONAL instruction. From Armv8.6 it is mandatory for implementations that include Advanced SIMD to support it. ID\_AA64ISAR1\_EL1.I8MM indicates whether this instruction is supported.

## Vector

(FEAT\_I8MM)

<!-- image -->

## Encoding

```
USMMLA <Vd>.4S, <Vn>.16B, <Vm>.16B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_I8MM) then constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant boolean op1_unsigned = TRUE; constant boolean op2_unsigned = FALSE;
```

## Assembler Symbols

&lt;Vd&gt;

Is the name of the SIMD&amp;FP third source and destination register, encoded in the 'Rd' field.

## &lt;Vn&gt;

Is the name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Vm&gt;

Is the name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(128) operand1 = V[n, 128]; constant bits(128) operand2 = V[m, 128]; constant bits(128) addend = V[d, 128]; V[d, 128] = MatMulAdd(addend, operand1, operand2, op1_unsigned, op2_unsigned);
```

## Operational Information

Arm expects that the USMMLA (vector) instruction will deliver a peak integer multiply throughput that is at least as high as can be achieved using two USDOT (vector) instructions, with a goal that it should have significantly higher throughput.

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

```
EndOfDecode(Decode_UNDEF);
```
