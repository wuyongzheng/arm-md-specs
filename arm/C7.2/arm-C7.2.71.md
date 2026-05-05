## C7.2.71 FCMPE

Floating-point signaling compare (scalar)

This instruction compares the two SIMD&amp;FP source register values, or the first SIMD&amp;FP source register value and zero. It writes the result to the PSTATE.{N, Z, C, V} flags.

This instruction raises an Invalid Operation floating-point exception if either or both of the operands is any type of NaN.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11 && opc == 10)
```

```
FCMPE <Hn>, <Hm>
```

## Encoding for the Half-precision, zero variant

```
(FEAT_FP16) Applies when (ftype == 11 && Rm == (00000) && opc == 11)
```

```
FCMPE <Hn>, #0.0
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00 && opc == 10)
```

```
FCMPE <Sn>, <Sm>
```

## Encoding for the Single-precision, zero variant

```
(FEAT_FP) Applies when (ftype == 00 && Rm == (00000) && opc == 11)
```

```
FCMPE <Sn>, #0.0
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01 && opc == 10)
```

```
FCMPE <Dn>, <Dm>
```

## Encoding for the Double-precision, zero variant

```
(FEAT_FP) Applies when (ftype == 01 && Rm == (00000) && opc == 11)
```

```
FCMPE <Dn>, #0.0
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt(Rm); // ignored when opc<0> == '1' constant integer datasize = 8 << UInt(ftype EOR '10'); constant boolean signal_all_nans = TRUE; constant boolean cmp_with_zero = (opc<0> == '1');
```

## Assembler Symbols

## &lt;Hn&gt;

For the 'Half-precision' variant: is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

For the 'Half-precision, zero' variant: is the 16-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

For the 'Single-precision' variant: is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

For the 'Single-precision, zero' variant: is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

For the 'Double-precision' variant: is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

For the 'Double-precision, zero' variant: is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = if cmp_with_zero then FPZero('0', datasize) else V[m, datasize]; PSTATE.<N,Z,C,V> = FPCompare(operand1, operand2, signal_all_nans, FPCR);
```

## &lt;Sn&gt;

## &lt;Dn&gt;

## Operational Information

The IEEE 754 standard specifies that the result of a comparison is precisely one of &lt;, ==, &gt; or unordered. If either or both of the operands is a NaN, they are unordered, and all three of (Operand1 &lt; Operand2), (Operand1 == Operand2) and (Operand1 &gt; Operand2) are false. An unordered comparison sets the PSTATE condition flags to N=0, Z=0, C=1, and V=1.

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.
