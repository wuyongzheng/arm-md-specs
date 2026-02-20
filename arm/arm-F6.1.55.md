## F6.1.55 VCMPE

Vector Compare, raising Invalid Operation on NaN compares two floating-point registers, or one floating-point register and zero. It writes the result to the FPSCR flags. These are normally transferred to the PSTATE.{N, Z, C, V} Condition flags by a subsequent VMRS instruction.

This instruction raises an Invalid Operation floating-point exception if either or both of the operands is any type of NaN.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

## A1

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(size == 01)
```

```
(FEAT_FP16) Applies when VCMPE{<c>}{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCMPE{<c>}{<q>}.F32
```

```
<Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VCMPE{<c>}{<q>}.F64
```

```
<Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean quiet_nan_exc = (E == '1'); constant boolean with_zero = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

A2

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when

```
VCMPE{<c>}{<q>}.F16
```

```
(size == 01) <Sd>, #0.0
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCMPE{<c>}{<q>}.F32 <Sd>, #0.0
```

## Encoding for the Double-precision scalar variant

Applies when (size ==

```
11) VCMPE{<c>}{<q>}.F64 <Dd>, #0.0
```

## Decode for all variants of this encoding

```
if size == '00' || (size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if size == '01' && cond != '1110' then UNPREDICTABLE; constant boolean quiet_nan_exc = (E == '1'); constant boolean with_zero = TRUE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = integer UNKNOWN;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T1

<!-- image -->

## Encoding for the Half-precision scalar variant

(FEAT\_FP16) Applies when (size == 01)

```
VCMPE{<c>}{<q>}.F16 <Sd>, <Sm>
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCMPE{<c>}{<q>}.F32 <Sd>, <Sm>
```

## Encoding for the Double-precision scalar variant

```
Applies when (size == 11) VCMPE{<c>}{<q>}.F64
```

```
<Dd>, <Dm>
```

## Decode for all variants of this encoding

```
if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean quiet_nan_exc = (E == '1'); constant boolean with_zero = FALSE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = if size == '11' then UInt(M:Vm) else UInt(Vm:M);
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T2

<!-- image -->

## Encoding for the Half-precision scalar variant

```
(FEAT_FP16) Applies when (size == 01) VCMPE{<c>}{<q>}.F16 <Sd>, #0.0
```

## Encoding for the Single-precision scalar variant

```
Applies when (size == 10) VCMPE{<c>}{<q>}.F32 <Sd>, #0.0
```

## Encoding for the Double-precision scalar variant

Applies when

```
(size == 11) VCMPE{<c>}{<q>}.F64 <Dd>, #0.0
```

## Decode for all variants of this encoding

```
if size == '00' then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean quiet_nan_exc = (E == '1'); constant boolean with_zero = TRUE; constant integer esize = 8 << UInt(size); constant integer d = if size == '11' then UInt(D:Vd) else UInt(Vd:D); constant integer m = integer UNKNOWN;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant FPCR_Type fpcr = EffectiveFPCR(); bits(4) nzcv; case esize of when 16 constant bits(16) op16 = if with_zero then FPZero('0', 16) else H[m]; nzcv = FPCompare(H[d], op16, quiet_nan_exc, fpcr); when 32 constant bits(32) op32 = if with_zero then FPZero('0', 32) else S[m]; nzcv = FPCompare(S[d], op32, quiet_nan_exc, fpcr); when 64 constant bits(64) op64 = if with_zero then FPZero('0', 64) else D[m]; nzcv = FPCompare(D[d], op64, quiet_nan_exc, fpcr);
```

FPSCR&lt;31:28&gt; = nzcv; // FPSCR.&lt;N,Z,C,V&gt; set to nzcv

## Operational Information

The IEEE 754 standard specifies that the result of a comparison is precisely one of &lt;, ==, &gt; or unordered. If either or both of the operands is a NaN, they are unordered, and all three of (Operand1 &lt; Operand2), (Operand1 == Operand2) and (Operand1 &gt; Operand2) are false. An unordered comparison sets the FPSCR condition flags to N=0, Z=0, C=1, and V=1.