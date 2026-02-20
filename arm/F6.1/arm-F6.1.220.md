## F6.1.220 VRSUBHN

Vector Rounding Subtract and Narrow, returning High Half subtracts the elements of one quadword vector from the corresponding elements of another quadword vector, takes the most significant half of each result, and places the final results in a doubleword vector. The results are rounded. For truncated results, see VSUBHN.

The operand elements can be 16-bit, 32-bit, or 64-bit integers. There is no distinction between signed and unsigned integers.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VRSUBHN{<c>}{<q>}.<dt> <Dd>, <Qn>, <Qm>
```

## Decode for this encoding

```
UNDEFINED;
```

```
if size == '11' then SEE "Related encodings"; if Vn<0> == '1' || Vm<0> == '1' then constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VRSUBHN{<c>}{<q>}.<dt> <Dd>, <Qn>, <Qm>
```

## Decode for this encoding

```
UNDEFINED;
```

```
if size == '11' then SEE "Related encodings"; if Vn<0> == '1' || Vm<0> == '1' then constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

Related encodings: See Advanced SIMD data-processing for the T32 instruction set, or Advanced SIMD data-processing for the A32 instruction set.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operands, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     00 | I16    |
|     01 | I32    |
|     10 | I64    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant boolean round = TRUE; for e = 0 to elements-1 constant integer result = (RShr(UInt(Elem[Qin[n>>1],e,2*esize] Elem[Qin[m>>1],e,2*esize]), esize, round)); Elem[D[d],e,esize] = result<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.