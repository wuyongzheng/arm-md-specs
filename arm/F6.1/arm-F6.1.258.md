## F6.1.258 VUMMLA

Widening 8-bit unsigned integer matrix multiply-accumulate into 2x2 matrix

The widening integer matrix multiply-accumulate instruction multiplies the 2x8 matrix of unsigned 8-bit integer values held in the first source vector by the 8x2 matrix of unsigned 8-bit integer values in the second source vector. The resulting 2x2 32-bit integer matrix product is destructively added to the 32-bit integer matrix accumulator held in the destination vector. This is equivalent to performing an 8-way dot product per destination element.

From Armv8.2, this is an OPTIONAL instruction. ID\_ISAR6.I8MM indicates whether this instruction is supported in the T32 and A32 instruction sets.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_AA32I8MM)

<!-- image -->

## Encoding

```
VUMMLA{<q>}.U8 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_AA32I8MM) then UNDEFINED; boolean op1_unsigned; boolean op2_unsigned; case B:U of when '00' op1_unsigned = FALSE; op2_unsigned = FALSE; when '01' op1_unsigned = TRUE; op2_unsigned = TRUE; when '10' op1_unsigned = TRUE; op2_unsigned = FALSE; when '11' UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

## T1

(FEAT\_AA32I8MM)

<!-- image -->

## Encoding

```
VUMMLA{<q>}.U8 <Qd>, <Qn>, <Qm>
```

```
UNDEFINED;
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32I8MM) then UNDEFINED; boolean op1_unsigned; boolean op2_unsigned; case B:U of when '00' op1_unsigned = FALSE; op2_unsigned = FALSE; when '01' op1_unsigned = TRUE; op2_unsigned = TRUE; when '10' op1_unsigned = TRUE; op2_unsigned = FALSE; when '11' UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the 128-bit name of the SIMD&amp;FP third source and destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
CheckAdvSIMDEnabled(); constant bits(128) operand1 = Q[n>>1]; constant bits(128) operand2 = Q[m>>1]; constant bits(128) addend = Q[d>>1]; Q[d>>1] = MatMulAdd(addend, operand1, operand2, op1_unsigned, op2_unsigned);
```

```
UNDEFINED;
```