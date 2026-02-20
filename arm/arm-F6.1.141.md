## F6.1.141 VMOVL

Vector Move Long takes each element in a doubleword vector, sign or zero-extends them to twice their original length, and places the results in a quadword vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMOVL{<c>}{<q>}.<dt> <Qd>, <Dm>
```

## Decode for this encoding

```
"VSHLL"; HighestSetBitNZ(imm3H);
```

```
if imm3H == '000' then SEE "Related encodings"; if ! imm3H IN {'001', '010', '100'} then SEE if Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant boolean unsigned = (U == '1');
```

T1

<!-- image -->

## Encoding

```
VMOVL{<c>}{<q>}.<dt> <Qd>, <Dm>
```

## Decode for this encoding

```
"VSHLL"; HighestSetBitNZ(imm3H);
```

```
if imm3H == '000' then SEE "Related encodings"; if ! imm3H IN {'001', '010', '100'} then SEE if Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant boolean unsigned = (U == '1');
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

L

L

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operand, encoded in 'U:imm3H':

|   U |   imm3H | <dt>   |
|-----|---------|--------|
|   0 |     001 | S8     |
|   0 |     010 | S16    |
|   0 |     100 | S32    |
|   1 |     001 | U8     |
|   1 |     010 | U16    |
|   1 |     100 | U32    |

&lt;q&gt;

&lt;dt&gt;

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 constant bits(esize) op1elt = Elem[Din[m],e,esize]; constant integer result = if unsigned then UInt(op1elt) else SInt(op1elt); Elem[Q[d>>1],e,2*esize] = result<2*esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.