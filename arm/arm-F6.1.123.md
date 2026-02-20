## F6.1.123 VMLA (by scalar)

Vector Multiply Accumulate (by scalar)

Vector Multiply Accumulate multiplies elements of a vector by a scalar, and adds the products to corresponding elements of the destination vector.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VMLA{<c>}{<q>}.<dt> <Dd>,
```

```
<Dn>, <Dm[x]>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when
```

```
(Q == 1) VMLA{<c>}{<q>}.<dt> <Qd>, <Qn>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || (F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = FALSE; // "Don't care" value: TRUE produces same functionality constant boolean add = (op == '0'); constant boolean floating_point = (F == '1'); constant boolean long_destination = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
VMLA{<c>}{<q>}.<dt> <Dd>,
```

```
(Q == 0) <Dn>, <Dm[x]>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VMLA{<c>}{<q>}.<dt> <Qd>,
```

```
(Q == 1) <Qn>, <Dm[x]>
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || (F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if F == '1' && size == '01' && InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = FALSE; // "Don't care" value: TRUE produces same functionality constant boolean add = (op == '0'); constant boolean floating_point = (F == '1'); constant boolean long_destination = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

## CONSTRAINED UNPREDICTABLE behavior

If F == '1' &amp;&amp; size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the scalar and the elements of the operand vector, encoded in 'F:size':

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm[x]&gt;

Is the 64-bit name of the second SIMD&amp;FP source register holding the scalar. If &lt;dt&gt; is I16 or F16 , Dm is restricted to D0-D7. Dm is encoded in 'Vm&lt;2:0&gt;', and x is encoded in 'M:Vm&lt;3&gt;'. If &lt;dt&gt; is I32 or F32 , Dm is restricted to D0-D15. Dm is encoded in 'Vm', and x is encoded in 'M'.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(esize) op2elt = Elem[Din[m],index,esize]; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; if floating_point then constant bits(esize) fp_addend = (if add then FPMul(op1elt, op2elt, fpcr) else FPNeg(FPMul(op1elt, op2elt, fpcr), fpcr)); Elem[D[d+r],e,esize] = FPAdd(Elem[Din[d+r],e,esize], fp_addend, fpcr); else constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer addend = if add then element1*element2 else -element1*element2; if long_destination then Elem[Q[d>>1],e,2*esize] = Elem[Qin[d>>1],e,2*esize] + addend; else Elem[D[d+r],e,esize] = Elem[Din[d+r],e,esize] + addend;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

|   F |   size | <dt>   |
|-----|--------|--------|
|   0 |     01 | I16    |
|   0 |     10 | I32    |
|   1 |     01 | F16    |
|   1 |     10 | F32    |

Is the 64-bit name of the SIMD&amp;FP register holding the accumulate vector, encoded in the 'D:Vd' field.

Is the 128-bit name of the SIMD&amp;FP register holding the accumulate vector, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.