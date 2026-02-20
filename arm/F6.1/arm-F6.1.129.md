## F6.1.129 VMLSL (integer)

Vector Multiply Subtract Long (integer)

Vector Multiply Subtract Long multiplies corresponding elements in two vectors, and subtract the products from the corresponding elements of the destination vector. The destination vector element is twice as long as the elements that are multiplied.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
encodings";
```

```
if size == '11' then SEE "Related if Vd<0> == '1' then UNDEFINED; constant boolean add = (op == '0'); constant boolean long_destination = TRUE; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = 1;
```

T1

<!-- image -->

## Encoding

```
VMLSL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
encodings";
```

```
if size == '11' then SEE "Related if Vd<0> == '1' then UNDEFINED; constant boolean add = (op == '0'); constant boolean long_destination = TRUE; constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = 1;
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'U:size':

|   U |   size | <dt>   |
|-----|--------|--------|
|   0 |     00 | S8     |
|   0 |     01 | S16    |
|   0 |     10 | S32    |
|   1 |     00 | U8     |
|   1 |     01 | U16    |
|   1 |     10 | U32    |

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;q&gt;

&lt;dt&gt;

## &lt;Qd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1
```

```
for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[n+r],e,esize]; constant bits(esize) op2elt = Elem[Din[m+r],e,esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer product = element1 * element2; constant integer addend = if add then product else -product; if long_destination then Elem[Q[d>>1],e,2*esize] = Elem[Qin[d>>1],e,2*esize] + addend; else Elem[D[d+r],e,esize] = Elem[Din[d+r],e,esize] + addend;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.