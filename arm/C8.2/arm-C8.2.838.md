## C8.2.838 UMMLA

Unsigned 8-bit integer matrix multiply-accumulate to 32-bit integer

This instruction multiplies the 2 × 8 matrix of unsigned 8-bit integer values held in each 128-bit segment of the first source vector by the 8 × 2 matrix of unsigned 8-bit integer values in the corresponding segment of the second source vector. The resulting 2 × 2 widened 32-bit integer matrix product is then destructively added to the 32-bit integer matrix accumulator held in the corresponding segment of the addend and destination vector. This is equivalent to performing an 8-way dot product per destination element.

This instruction is unpredicated.

ID\_AA64ZFR0\_EL1.I8MM indicates whether this instruction is implemented.

This instruction is illegal when executed in Streaming SVE mode, unless FEAT\_SME\_FA64 is implemented and enabled.

## SVE

(FEAT\_SVE &amp;&amp; FEAT\_I8MM)

<!-- image -->

## Encoding

```
UMMLA <Zda>.S, <Zn>.B,
```

```
<Zm>.B
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_SVE) || !IsFeatureImplemented(FEAT_I8MM) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Zn); constant integer m = UInt(Zm); constant integer da = UInt(Zda); constant boolean op1_unsigned = TRUE; constant boolean op2_unsigned = TRUE;
```

## Assembler Symbols

## &lt;Zda&gt;

Is the name of the third source and destination scalable vector register, encoded in the 'Zda' field.

## &lt;Zn&gt;

Is the name of the first source scalable vector register, encoded in the 'Zn' field.

## &lt;Zm&gt;

Is the name of the second source scalable vector register, encoded in the 'Zm' field.

## Operation

```
CheckNonStreamingSVEEnabled(); constant integer VL = CurrentVL; constant integer segments = VL DIV constant bits(VL) operand1 = Z[n, VL]; constant bits(VL) operand2 = Z[m, VL]; constant bits(VL) operand3 =
```

```
128; Z[da, VL]; bits(VL) result = Zeros(VL);
```

```
bits(128) op1, op2; bits(128) res, addend; for s = 0 to segments-1 op1 = Elem[operand1, s, 128]; op2 = Elem[operand2, s, 128]; addend = Elem[operand3, s, 128]; res = MatMulAdd(addend, op1, op2, op1_unsigned, Elem[result, s, 128] = res; Z[da, VL] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About PSTATE.DIT.

This instruction might be immediately preceded in program order by a MOVPRFX instruction. The MOVPRFX must conform to all of the following requirements, otherwise the behavior of the MOVPRFX and this instruction is CONSTRAINED UNPREDICTABLE:

- The MOVPRFX must be unpredicated.
- The MOVPRFX must specify the same destination register as this instruction.
- The destination register must not refer to architectural register state referenced by any other source operand register of this instruction.

```
op2_unsigned);
```