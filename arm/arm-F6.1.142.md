## F6.1.142 VMOVN

Vector Move and Narrow copies the least significant half of each element of a quadword vector into the corresponding elements of a doubleword vector.

The operand vector elements can be any one of 16-bit, 32-bit, or 64-bit integers. There is no distinction between signed and unsigned integers.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

This instruction is used by the pseudo-instructions VRSHRN (zero) and VSHRN (zero).

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMOVN{<c>}{<q>}.<dt> <Dd>, <Qm>
```

## Decode for this encoding

```
UInt(size); esize;
```

```
if size == '11' then UNDEFINED; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << constant integer elements = 64 DIV constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VMOVN{<c>}{<q>}.<dt> <Dd>, <Qm>
```

## Decode for this encoding

```
if size == '11' then UNDEFINED; if Vm<0> == '1' then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operand, encoded in 'size':

|   size | <dt>     |
|--------|----------|
|     00 | I16      |
|     01 | I32      |
|     10 | I64      |
|     11 | RESERVED |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for e = 0 to elements-1 Elem[D[d],e,esize] = Elem[Qin[m>>1],e,2*esize]<esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;