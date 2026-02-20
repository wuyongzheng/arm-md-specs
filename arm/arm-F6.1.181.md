## F6.1.181 VQRDMULH

Vector Saturating Rounding Doubling Multiply Returning High Half multiplies corresponding elements in two vectors, doubles the results, and places the most significant half of the final results in the destination vector. The results are rounded. For truncated results see VQDMULH.

The second operand can be a scalar instead of a vector. For more information about scalars see Advanced SIMD scalars.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

```
VQRDMULH{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMULH{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if size == '00' || size == '11' then UNDEFINED; constant boolean scalar_form = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2; constant integer index = integer UNKNOWN;
```

A2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
VQRDMULH{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm[x]>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMULH{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VQRDMULH{<c>}{<q>}.<dt> {<Dd>, }<Dn>,
```

```
<Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMULH{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if size == '00' || size == '11' then UNDEFINED; constant boolean scalar_form = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2; constant integer index = integer UNKNOWN;
```

```
UNDEFINED;
```

T2

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VQRDMULH{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm[x]>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMULH{<c>}{<q>}.<dt> {<Qd>, }<Qn>,
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector', 'A1 64-bit SIMD vector', 'A2 128-bit SIMD vector', and 'A2 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector', 'T1 64-bit SIMD vector', 'T2 128-bit SIMD vector', and 'T2 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     01 | S16    |
|     10 | S32    |

```
<Dm[x]>
```

<!-- image -->

&lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;Dm[x]&gt;

Is the 64-bit name of the second SIMD&amp;FP source register holding the scalar. If &lt;dt&gt; is S16 , Dm is restricted to D0-D7. Dm is encoded in 'Vm&lt;2:0&gt;', and x is encoded in 'M:Vm&lt;3&gt;'. If &lt;dt&gt; is S32 , Dm is restricted to D0-D15. Dm is encoded in 'Vm', and x is encoded in 'M'.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); integer op2; constant boolean round = TRUE; if scalar_form then op2 = SInt(Elem[D[m],index,esize]); for r = 0 to regs-1 for e = 0 to elements-1 constant integer op1 = SInt(Elem[D[n+r],e,esize]); if !scalar_form then op2 = SInt(Elem[D[m+r],e,esize]); constant integer rdmulh = RShr(2*op1*op2, esize, round); bits(esize) result; boolean sat; (result, sat) = SignedSatQ(rdmulh, esize); Elem[D[d+r],e,esize] = result; if sat then FPSCR.QC = '1';
```

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.