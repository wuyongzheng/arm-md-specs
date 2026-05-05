## C7.2.59 FCCMPE

Floating-point conditional signaling compare (scalar)

This instruction compares the two SIMD&amp;FP source register values and writes the result to the PSTATE.{N, Z, C, V} flags. If the condition does not pass, then the PSTATE.{N, Z, C, V} flags are set to the flag bit specifier.

This instruction raises an Invalid Operation floating-point exception if either or both of the operands is any type of NaN.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

```
(FEAT_FP16) Applies when (ftype == 11)
```

```
FCCMPE <Hn>, <Hm>, #<nzcv>, <cond>
```

## Encoding for the Single-precision variant

```
(FEAT_FP) Applies when (ftype == 00) FCCMPE <Sn>, <Sm>, #<nzcv>, <cond>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FCCMPE <Dn>, <Dm>, #<nzcv>, <cond>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer datasize = 8 << UInt(ftype EOR '10'); constant bits(4) condition = cond; bits(4) flags = nzcv;
```

## Assembler Symbols

&lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

&lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;nzcv&gt;

Is the flag bit specifier, an immediate in the range 0 to 15, giving the alternative state for the 4-bit NZCV condition flags, encoded in the 'nzcv' field.

## &lt;cond&gt;

Is one of the standard conditions, encoded in the standard way, and encoded in 'cond':

|   cond | <cond>   |
|--------|----------|
|   0000 | EQ       |
|   0001 | NE       |
|   0010 | CS       |
|   0011 | CC       |
|   0100 | MI       |
|   0101 | PL       |
|   0110 | VS       |
|   0111 | VC       |
|   1000 | HI       |
|   1001 | LS       |
|   1010 | GE       |
|   1011 | LT       |
|   1100 | GT       |
|   1101 | LE       |
|   1110 | AL       |
|   1111 | NV       |

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'Rn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Rm' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(datasize) operand1 = V[n, datasize]; constant bits(datasize) operand2 = V[m, datasize]; if ConditionHolds(condition) then constant boolean signal_all_nans = TRUE; flags = FPCompare(operand1, operand2, signal_all_nans,
```

## &lt;Sn&gt;

```
FPCR);
```

PSTATE.&lt;N,Z,C,V&gt; = flags;

## Operational Information

The IEEE 754 standard specifies that the result of a comparison is precisely one of &lt;, ==, &gt; or unordered. If either or both of the operands is a NaN, they are unordered, and all three of (Operand1 &lt; Operand2), (Operand1 == Operand2) and (Operand1 &gt; Operand2) are false. An unordered comparison sets the PSTATE condition flags to N=0, Z=0, C=1, and V=1.

If FEAT\_SME is implemented and the PE is in Streaming SVE mode, then any subsequent instruction which is dependent on the NZCV condition flags written by this instruction might be significantly delayed.
