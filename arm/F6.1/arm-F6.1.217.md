## F6.1.217 VRSQRTE

Vector Reciprocal Square Root Estimate finds an approximate reciprocal square root of each element in a vector, and places the results in a second vector.

The operand and result elements are the same type, and can be floating-point numbers or unsigned integers.

For details of the operation performed by this instruction see Floating-point reciprocal estimate and step.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRSQRTE{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VRSQRTE{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if (size == '01' && (!IsFeatureImplemented(FEAT_FP16) || F == '0')) || size IN {'00', '11'} then UNDEFINED; constant boolean floating_point = (F == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRSQRTE{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VRSQRTE{<c>}{<q>}.<dt>
```

```
<Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if size == '01' && (!IsFeatureImplemented(FEAT_FP16) || F == '0') then UNDEFINED; if size IN {'00', '11'} then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean floating_point = (F == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'F:size':

|   F |   size | <dt>   |
|-----|--------|--------|
|   0 |     10 | U32    |
|   1 |     01 | F16    |
|   1 |     10 | F32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

Newton-Raphson iteration

For details of the operation performed and how it can be used in a Newton-Raphson iteration to calculate the reciprocal of the square root of a number, see Floating-point reciprocal estimate and step.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 if floating_point then Elem[D[d+r],e,esize] = FPRSqrtEstimate(Elem[D[m+r],e,esize], fpcr); else Elem[D[d+r],e,esize] = UnsignedRSqrtEstimate(Elem[D[m+r],e,esize]);
```