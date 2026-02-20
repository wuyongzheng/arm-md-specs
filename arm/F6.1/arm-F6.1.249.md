## F6.1.249 VSUBL

Vector Subtract Long subtracts the elements of one doubleword vector from the corresponding elements of another doubleword vector, and places the results in a quadword vector. Before subtracting, it sign-extends or zero-extends the elements of both operands.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VSUBL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if Vd<0> == '1' || (op == '1' && Vn<0> == '1') then constant boolean unsigned = (U == '1'); constant boolean is_vsubw = (op == '1'); constant integer esize = 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize;
```

T1

<!-- image -->

## Encoding

```
VSUBL{<c>}{<q>}.<dt> <Qd>, <Dn>, <Dm>
```

## Decode for this encoding

```
if size == '11' then SEE "Related encodings"; if Vd<0> == '1' || (op == '1' && Vn<0> == '1') then constant boolean unsigned = (U == '1'); constant boolean is_vsubw = (op == '1'); constant integer esize = 8 << UInt(size); constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 64 DIV esize;
```

```
UNDEFINED;
```

```
UNDEFINED;
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the second operand vector, encoded in 'U:size':

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

&lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 integer element1; if is_vsubw then constant bits(2*esize) op1elt = Elem[Qin[n>>1],e,2*esize]; element1 = if unsigned then UInt(op1elt) else SInt(op1elt); else constant bits(esize) op1elt = Elem[Din[n],e,esize]; element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant bits(esize) op2elt = Elem[Din[m],e,esize]; constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer result = element1 -element2; Elem[Q[d>>1],e,2*esize] = result<2*esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.