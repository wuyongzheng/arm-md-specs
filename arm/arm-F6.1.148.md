## F6.1.148 VMUL (by scalar)

Vector Multiply (by scalar)

Vector Multiply multiplies each element in a vector by a scalar, and places the results in a second vector.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VMUL{<c>}{<q>}.<dt>
```

```
{<Dd>, }<Dn>, <Dm>[<index>]
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1)
```

```
VMUL{<c>}{<q>}.<dt> {<Qd>, }<Qn>, <Dm>[<index>]
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || (F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = FALSE; // "Don't care" value: TRUE produces same functionality constant boolean floating_point = (F == '1'); constant boolean long_destination = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

T1

<!-- image -->

size

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VMUL{<c>}{<q>}.<dt>
```

```
{<Dd>, }<Dn>, <Dm>[<index>]
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VMUL{<c>}{<q>}.<dt>
```

```
(Q == 1) {<Qd>, }<Qn>, <Dm>[<index>]
```

## Decode for all variants of this encoding

```
if size == '11' then SEE "Related encodings"; if F == '1' && size == '01' && InITBlock() then UNPREDICTABLE; if size == '00' || (F == '1' && size == '01' && !IsFeatureImplemented(FEAT_FP16)) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1') then UNDEFINED; constant boolean unsigned = FALSE; // "Don't care" value: TRUE produces same functionality constant boolean floating_point = (F == '1'); constant boolean long_destination = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = if Q == '0' then 1 else 2; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
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

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register. When &lt;dt&gt; is I16 or F16, this is encoded in the 'Vm&lt;2:0&gt;' field. Otherwise it is encoded in the 'Vm' field.

## &lt;index&gt;

Is the element index. When &lt;dt&gt; is I16 or F16, this is in the range 0 to 3 and is encoded in the 'M:Vm&lt;3&gt;' field. Otherwise it is in the range 0 to 1 and is encoded in the 'M' field.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(esize) op2elt = Elem[Din[m],index,esize]; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; if floating_point then Elem[D[d+r],e,esize] = FPMul(op1elt, op2elt, fpcr); else constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); if long_destination then Elem[Q[d>>1],e,2*esize] = (element1 * element2)<2*esize-1:0>; else Elem[D[d+r],e,esize] = (element1 * element2)<esize-1:0>;
```

|   F |   size | <dt>   |
|-----|--------|--------|
|   0 |     01 | I16    |
|   0 |     10 | I32    |
|   1 |     01 | F16    |
|   1 |     10 | F32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.