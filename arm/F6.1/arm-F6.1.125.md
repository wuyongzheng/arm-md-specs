## F6.1.125 VMLAL (by scalar)

Vector Multiply Accumulate Long (by scalar)

Vector Multiply Accumulate Long multiplies elements of a vector by a scalar, and adds the products to corresponding elements of the destination vector. The destination vector elements are twice as long as the elements that are multiplied.

For more information about scalars see Advanced SIMD scalars.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMLAL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm[x]>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean add = (op == '0'); constant boolean floating_point = FALSE; constant boolean long_destination = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = 1; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

T1

<!-- image -->

## Encoding

```
VMLAL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm[x]>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if size == '00' || Vd<0> == '1' then UNDEFINED; constant boolean unsigned = (U == '1'); constant boolean add = (op == '0'); constant boolean floating_point = FALSE; constant boolean long_destination = TRUE; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer regs = 1; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer m = if size == '01' then UInt(Vm<2:0>) else UInt(Vm); constant integer index = if size == '01' then UInt(M:Vm<3>) else UInt(M);
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

```
<c> For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional. For the 'T1' variant: see Standard assembler syntax fields. <q> See Standard assembler syntax fields. <dt>
```

Is the data type for the scalar and the elements of the operand vector, encoded in 'U:size':

|   U |   size | <dt>   |
|-----|--------|--------|
|   0 |     01 | S16    |
|   0 |     10 | S32    |
|   1 |     01 | U16    |
|   1 |     10 | U32    |

Is the 128-bit name of the SIMD&amp;FP register holding the accumulate vector, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm[x]&gt;

Is the 64-bit name of the second SIMD&amp;FP source register holding the scalar. If &lt;dt&gt; is S16 or U16 , Dm is restricted to D0-D7. Dm is encoded in 'Vm&lt;2:0&gt;', and x is encoded in 'M:Vm&lt;3&gt;'. If &lt;dt&gt; is S32 or U32 , Dm is restricted to D0-D15. Dm is encoded in 'Vm', and x is encoded in 'M'.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(esize) op2elt = Elem[Din[m],index,esize]; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; if floating_point then constant bits(esize) fp_addend = (if add then FPMul(op1elt, op2elt, fpcr) else FPNeg(FPMul(op1elt, op2elt, fpcr), fpcr)); Elem[D[d+r],e,esize] = FPAdd(Elem[Din[d+r],e,esize], fp_addend, fpcr); else constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer addend = if add then element1*element2 else -element1*element2; if long_destination then Elem[Q[d>>1],e,2*esize] = Elem[Qin[d>>1],e,2*esize] + addend; else Elem[D[d+r],e,esize] = Elem[Din[d+r],e,esize] + addend;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.