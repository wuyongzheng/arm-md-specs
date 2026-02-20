## F6.1.179 VQRDMLAH

Vector Saturating Rounding Doubling Multiply Accumulate Returning High Half. This instruction multiplies the vector elements of the first source SIMD&amp;FP register with either the corresponding vector elements of the second source SIMD&amp;FP register or the value of a vector element of the second source SIMD&amp;FP register, without saturating the multiply results, doubles the results, and accumulates the most significant half of the final results with the vector elements of the destination SIMD&amp;FP register. The results are rounded.

If any of the results overflow, they are saturated. The cumulative saturation bit, FPSCR.QC, is set if saturation occurs. For details see Pseudocode details of saturation.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

(FEAT\_RDM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VQRDMLAH{<q>}.<dt> <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMLAH{<q>}.<dt> <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then if size == '00' || size == '11' then UNDEFINED; constant boolean add = TRUE; constant boolean scalar_form = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2; constant integer index = integer UNKNOWN;
```

```
UNDEFINED;
```

A2

(FEAT\_RDM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VQRDMLAH{<q>}.<dt> <Dd>, <Dn>, <Dm[x]>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMLAH{<q>}.<dt>
```

```
<Qd>, <Qn>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then UNDEFINED; if size == '11' then SEE "Related encodings"; if size == '00' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean add = TRUE; constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

T1

(FEAT\_RDM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VQRDMLAH{<q>}.<dt> <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VQRDMLAH{<q>}.<dt> <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then UNDEFINED; if InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; if size == '00' || size == '11' then UNDEFINED; constant boolean add = TRUE; constant boolean scalar_form = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2; constant integer index = integer UNKNOWN;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

T2

(FEAT\_RDM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
<Dd>, <Dn>, <Dm[x]>
```

```
(Q == 0) VQRDMLAH{<q>}.<dt>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VQRDMLAH{<q>}.<dt> <Qd>, <Qn>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_RDM) then UNDEFINED; if InITBlock() then UNPREDICTABLE; if size == '11' then SEE "Related encodings"; if size == '00' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean add = TRUE; constant boolean scalar_form = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     01 | S16    |
|     10 | S32    |

Is the 64-bit name of the SIMD&amp;FP register holding the accumulate vector, encoded in the 'D:Vd' field.

<!-- image -->

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;Dm[x]&gt;

Is the 64-bit name of the second SIMD&amp;FP source register holding the scalar. If &lt;dt&gt; is S16 , Dm is restricted to D0-D7. Dm is encoded in 'Vm&lt;2:0&gt;', and x is encoded in 'M:Vm&lt;3&gt;'. If &lt;dt&gt; is S32 , Dm is restricted to D0-D15. Dm is encoded in 'Vm', and x is encoded in 'M'.

Is the 128-bit name of the SIMD&amp;FP register holding the accumulate vector, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); integer operand2; constant boolean round = TRUE; if scalar_form then operand2 = SInt(Elem[D[m],index,esize]); for r = 0 to regs-1 for e = 0 to elements-1 constant integer operand1 = SInt(Elem[D[n+r],e,esize]); constant integer operand3 = SInt(Elem[D[d+r],e,esize]) << esize; if !scalar_form then operand2 = SInt(Elem[D[m+r],e,esize]); constant integer rdmlah = RShr(operand3 + 2*(operand1*operand2), esize, bits(esize) result; boolean sat; (result, sat) = SignedSatQ(rdmlah, esize); Elem[D[d+r],e,esize] = result; if sat then FPSCR.QC = '1';
```

```
round);
```