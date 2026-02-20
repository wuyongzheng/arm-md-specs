## F6.1.24 VACGT

Vector Absolute Compare Greater Than takes the absolute value of each element in a vector, and compares it with the absolute value of the corresponding element of a second vector. If the first is greater than the second, the corresponding element in the destination vector is set to all ones. Otherwise, it is set to all zeros.

The operands and result can be quadword or doubleword vectors. They must all be the same size.

The operand vector elements are floating-point numbers. The result vector elements are the same size as the operand vector elements.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instruction V ACLT.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

```
VACGT{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VACGT{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant boolean or_equal = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

```
UNDEFINED;
```

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VACGT{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VACGT{<c>}{<q>}.<dt> {<Qd>, }<Qn>,
```

```
(Q == 1) <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if sz == '1' && InITBlock() then UNPREDICTABLE; constant boolean or_equal = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If sz == '1' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

<!-- image -->

<!-- image -->

<!-- image -->

```
<Dn> Is the 64-bit name of the first SIMD&FP source register, encoded in the 'N:Vn' field. <Dm> Is the 64-bit name of the second SIMD&FP source register, encoded in the 'M:Vm' field. <Qd> Is the 128-bit name of the SIMD&FP destination register, encoded in the 'D:Vd' field as <Qd>*2. <Qn> Is the 128-bit name of the first SIMD&FP source register, encoded in the 'N:Vn' field as <Qn>*2. <Qm> Is the 128-bit name of the second SIMD&FP source register, encoded in the 'M:Vm' field as <Qm>*2.
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1 = FPAbs(Elem[D[n+r],e,esize], fpcr); constant bits(esize) op2 = FPAbs(Elem[D[m+r],e,esize], fpcr); boolean test_passed; if or_equal then test_passed = FPCompareGE(op1, op2, fpcr); else test_passed = FPCompareGT(op1, op2, fpcr); Elem[D[d+r],e,esize] = if test_passed then Ones(esize) else
```

```
Zeros(esize);
```