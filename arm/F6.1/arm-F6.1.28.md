## F6.1.28 VADD (integer)

Vector Add (integer) adds corresponding elements in two vectors, and places the results in the destination vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VADD{&lt;c&gt;}{&lt;q&gt;}.&lt;dt&gt;

{&lt;Dd&gt;, }&lt;Dn&gt;,

&lt;Dm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VADD{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VADD{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VADD{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     00 | I8     |
|     01 | I16    |
|     10 | I32    |
|     11 | I64    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 for e = 0 to elements-1 Elem[D[d+r],e,esize] = Elem[D[n+r],e,esize] + Elem[D[m+r],e,esize];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.