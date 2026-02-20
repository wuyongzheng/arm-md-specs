## F6.1.150 VMULL (by scalar)

Vector Multiply Long (by scalar)

Vector Multiply Long multiplies each element in a vector by a scalar, and places the results in a second vector. The destination vector elements are twice as long as the elements that are multiplied.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMULL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>[<index>]
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean long_destination = TRUE; constant boolean floating_point = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = 1; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

T1

<!-- image -->

## Encoding

```
VMULL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>[<index>]
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean long_destination = TRUE; constant boolean floating_point = FALSE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = 1; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the scalar and the elements of the operand vector, encoded in 'U:size':

|   U |   size | <dt>   |
|-----|--------|--------|
|   0 |     01 | S16    |
|   0 |     10 | S32    |
|   1 |     01 | U16    |
|   1 |     10 | U32    |

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;q&gt;

&lt;dt&gt;

&lt;Qd&gt;

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm&lt;2:0&gt;' field when &lt;dt&gt; is S16 or U16, otherwise the 'Vm' field.

## &lt;index&gt;

Is the element index in the range 0 to 3, encoded in the 'M:Vm&lt;3&gt;' field when &lt;dt&gt; is S16 or U16, otherwise in range 0 to 1, encoded in the 'M' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(esize) op2elt = Elem[Din[m],index,esize]; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; if floating_point then Elem[D[d+r],e,esize] = FPMul(op1elt, op2elt, fpcr); else constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); if long_destination then Elem[Q[d>>1],e,2*esize] = (element1 * element2)<2*esize-1:0>; else Elem[D[d+r],e,esize] = (element1 * element2)<esize-1:0>;
```