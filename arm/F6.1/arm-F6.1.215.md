## F6.1.215 VRSHRN

Vector Rounding Shift Right and Narrow takes each element in a vector, right shifts them by an immediate value, and places the rounded results in the destination vector. For truncated results, see VSHRN.

The operand elements can be 16-bit, 32-bit, or 64-bit integers. There is no distinction between signed and unsigned integers. The destination elements are half the size of the source elements.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VRSHRN{<c>}{<q>}.I<size> <Dd>, <Qm>, #<imm>
```

## Decode for this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = (esize << 1) -UInt(imm6); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VRSHRN{<c>}{<q>}.I<size> <Dd>, <Qm>, #<imm>
```

## Decode for this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << HighestSetBitNZ(imm6<5:3>); constant integer elements = 64 DIV esize; constant integer shift_amount = (esize << 1) -UInt(imm6); constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;size&gt;

Is the data size for the elements of the vectors, encoded in 'imm6':

| imm6   |   <size> |
|--------|----------|
| 001xxx |       16 |
| 01xxxx |       32 |
| 1xxxxx |       64 |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## &lt;imm&gt;

Is an immediate value, in the range 1 to &lt;size&gt; /2, encoded in the 'imm6' field as &lt;size&gt; /2 &lt;imm&gt; .

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant boolean round = TRUE; for e = 0 to elements-1 constant integer result = RShr(UInt(Elem[Qin[m>>1],e,2*esize]), shift_amount, round); Elem[D[d],e,esize] = result<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

## &lt;Dd&gt;