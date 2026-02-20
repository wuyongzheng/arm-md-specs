## F6.1.41 VCEQ (register)

Vector Compare Equal takes each element in a vector, and compares it with the corresponding element of a second vector. If they are equal, the corresponding element in the destination vector is set to all ones. Otherwise, it is set to all zeros.

The operand vector elements are the same type, and are integers or floating-point numbers. The result vector elements are fields the same size as the operand vector elements.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VCEQ{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

{&lt;Dd&gt;, }&lt;Dn&gt;,

&lt;Dm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if size == '11' then UNDEFINED; constant boolean int_operation = TRUE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

A2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCEQ{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant boolean int_operation = FALSE; constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VCEQ{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

{&lt;Dd&gt;, }&lt;Dn&gt;,

&lt;Dm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if size == '11' then UNDEFINED; constant boolean int_operation = TRUE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

T2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VCEQ{<c>}{<q>}.<dt> {<Dd>, }<Dn>,
```

```
<Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

```
VCEQ{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if sz == '1' && InITBlock() then UNPREDICTABLE; constant boolean int_operation = FALSE; constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If sz == '1' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A2 128-bit SIMD vector', and 'A2 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 128-bit SIMD vector', and 'T2 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'T1 128-bit SIMD vector', and 'T1 64-bit SIMD vector' variants: is the data type for the elements of the vectors, encoded in 'size':

<!-- image -->

&lt;dt&gt;

## &lt;Dd&gt;

- &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

- &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

- &lt;Qd&gt;
- &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

- &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[D[n+r],e,esize]; constant bits(esize) op2elt = Elem[D[m+r],e,esize]; boolean test_passed; if int_operation then test_passed = (op1elt == op2elt); else test_passed = FPCompareEQ(op1elt, op2elt, StandardFPCR()); Elem[D[d+r],e,esize] = if test_passed then Ones(esize) else Zeros(esize);
```

|   size | <dt>   |
|--------|--------|
|     00 | I8     |
|     01 | I16    |
|     10 | I32    |

For the 'A2 128-bit SIMD vector', 'A2 64-bit SIMD vector', 'T2 128-bit SIMD vector', and 'T2 64-bit SIMD vector' variants: is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.