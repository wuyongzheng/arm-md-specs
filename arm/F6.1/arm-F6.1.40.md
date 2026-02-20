## F6.1.40 VCEQ (immediate #0)

Vector Compare Equal to Zero takes each element in a vector, and compares it with zero. If it is equal to zero, the corresponding element in the destination vector is set to all ones. Otherwise, it is set to all zeros.

The operand vector elements are the same type, and are integers or floating-point numbers. The result vector elements are fields the same size as the operand vector elements.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCEQ{<c>}{<q>}.<dt> {<Dd>, }<Dm>, #0
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qm>, #0
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if F == '1' && size == '00' then UNDEFINED; if F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean floating_point = (F == '1'); constant integer esize = 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize; constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCEQ{<c>}{<q>}.<dt> {<Dd>, }<Dm>, #0
```

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

```
VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qm>, #0
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if F == '1' && size == '00' then UNDEFINED; if F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if F == '1' && size == '01' && InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean floating_point = (F == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If F == '1' &amp;&amp; size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

- &lt;dt&gt; Is the data type for the elements of the operands, encoded in 'F:size':

|   F |   size | <dt>   |
|-----|--------|--------|
|   0 |     00 | I8     |
|   0 |     01 | I16    |
|   0 |     10 | I32    |
|   1 |     01 | F16    |
|   1 |     10 | F32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;q&gt;

&lt;Dd&gt;

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 boolean test_passed; if floating_point then constant bits(esize) zero = FPZero('0', esize); test_passed = FPCompareEQ(Elem[D[m+r],e,esize], zero, StandardFPCR()); else test_passed = (Elem[D[m+r],e,esize] == Zeros(esize)); Elem[D[d+r],e,esize] = if test_passed then Ones(esize) else Zeros(esize);
```