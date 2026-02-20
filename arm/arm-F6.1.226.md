## F6.1.226 VSHLL

Vector Shift Left Long takes each element in a doubleword vector, left shifts them by an immediate value, and places the results in a quadword vector.

The operand elements can be:

- 8-bit, 16-bit, or 32-bit signed integers.
- 8-bit, 16-bit, or 32-bit unsigned integers.
- 8-bit, 16-bit, or 32-bit untyped integers, maximum shift only.

The result elements are twice the length of the operand elements.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1 and A2) and T32 (T1 and T2).

A1

<!-- image -->

## Encoding

```
VSHLL{<c>}{<q>}.<type><size> <Qd>, <Dm>, #<imm>
```

## Decode for this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if imm6 IN {'001000', '010000', '100000'} then SEE if Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(imm6) esize; constant boolean unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

A2

<!-- image -->

## Encoding

```
VSHLL{<c>}{<q>}.<type><size> <Qd>, <Dm>, #<imm>
```

```
"VMOVL";
```

## Decode for this encoding

```
if size == '11' || Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer shift_amount = esize; constant boolean unsigned = FALSE; // Or TRUE without change of functionality constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VSHLL{<c>}{<q>}.<type><size> <Qd>, <Dm>, #<imm>
```

## Decode for this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if imm6 IN {'001000', '010000', '100000'} then SEE if Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = UInt(imm6) esize; constant boolean unsigned = (U == '1'); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T2

<!-- image -->

## Encoding

```
VSHLL{<c>}{<q>}.<type><size> <Qd>, <Dm>, #<imm>
```

## Decode for this encoding

```
if size == '11' || Vd<0> == '1' then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer shift_amount = esize; constant boolean unsigned = FALSE; // Or TRUE without change of functionality constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

```
"VMOVL";
```

## Assembler Symbols

&lt;c&gt;

For the 'A1' and 'A2' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' and 'T2' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

## &lt;size&gt;

The data size for the elements of the operand. The following table shows the permitted values and their encodings:

|   <size> | Encoding T1/A1               | Encoding T2/A2         |
|----------|------------------------------|------------------------|
|        8 | Encoded as imm6<5:3> = 0b001 | Encoded as size = 0b00 |
|       16 | Encoded as imm6<5:4> = 0b01  | Encoded as size = 0b01 |
|       32 | Encoded as imm6<5> = 1       | Encoded as size = 0b10 |

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;imm&gt;

The immediate value. &lt;imm&gt; must lie in the range 1 to &lt;size&gt; , and:

- If &lt;size&gt; == &lt;imm&gt; , the encoding is T2/A2.
- Otherwise, the encoding is T1/A1, and:
- If &lt;size&gt; == 8, &lt;imm&gt; is encoded in imm6&lt;2:0&gt;.
- If &lt;size&gt; == 16, &lt;imm&gt; is encoded in imm6&lt;3:0&gt;.
- If &lt;size&gt; == 32, &lt;imm&gt; is encoded in imm6&lt;4:0&gt;.

&lt;q&gt;

## &lt;type&gt;

The data type for the elements of the operand. It must be one of:

- S Signed. In encoding T1/A1, encoded as U = 0.
- U Unsigned. In encoding T1/A1, encoded as U = 1.
- I Untyped integer, Available only in encoding T2/A2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 constant bits(esize) opelt = Elem[Din[m],e,esize]; constant integer element = if unsigned then UInt(opelt) else SInt(opelt); constant integer result = element << shift_amount; Elem[Q[d>>1],e,2*esize] = result<2*esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.