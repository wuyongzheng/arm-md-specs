## F6.1.168 VPMIN (integer)

Vector Pairwise Minimum (integer)

Vector Pairwise Minimum compares adjacent pairs of elements in two doubleword vectors, and copies the smaller of each pair into the corresponding element in the destination doubleword vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VPMIN{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then UNDEFINED; constant boolean maximum = (op == '0'); constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VPMIN{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then UNDEFINED; constant boolean maximum = (op == '0'); constant boolean unsigned = (U == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

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

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(64) dest; constant integer h = elements DIV 2; for e = 0 to h-1 bits(esize) op1elt = Elem[D[n],2*e,esize]; bits(esize) op2elt = Elem[D[n],2*e+1,esize]; integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); integer result = if maximum then Max(element1, element2) else Min(element1, element2); Elem[dest,e,esize] = result<esize-1:0>; op1elt = Elem[D[m],2*e,esize]; op2elt = Elem[D[m],2*e+1,esize]; element1 = if unsigned then UInt(op1elt) else SInt(op1elt); element2 = if unsigned then UInt(op2elt) else SInt(op2elt); result = if maximum then Max(element1, element2) else Min(element1, element2); Elem[dest,e+h,esize] = result<esize-1:0>; D[d] = dest;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.