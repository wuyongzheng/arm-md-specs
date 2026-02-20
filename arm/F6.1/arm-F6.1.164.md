## F6.1.164 VPADDL

Vector Pairwise Add Long adds adjacent pairs of elements of two vectors, and places the results in the destination vector.

The vectors can be doubleword or quadword. The operand elements can be 8-bit, 16-bit, or 32-bit integers. The result elements are twice the length of the operand elements.

Figure F6-4 VPADDL doubleword operation for data type S16

<!-- image -->

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VPADDL{<c>}{<q>}.<dt>
```

```
<Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VPADDL{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant boolean unsigned = (op == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
VPADDL{<c>}{<q>}.<dt>
```

```
<Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VPADDL{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if size == '11' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then constant boolean unsigned = (op == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

<!-- image -->

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'op:size':

| op   |   size | <dt>     |
|------|--------|----------|
| 0    |     00 | S8       |
| 0    |     01 | S16      |
| 0    |     10 | S32      |
| x    |     11 | RESERVED |
| 1    |     00 | U8       |
| 1    |     01 | U16      |

<!-- image -->

<!-- image -->

```
UNDEFINED;
```

## &lt;Dd&gt;

|   op |   size | <dt>   |
|------|--------|--------|
|    1 |     10 | U32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant integer h = elements DIV 2; for r = 0 to regs-1 for e = 0 to h-1 constant bits(esize) op1elt = Elem[D[m+r],2*e,esize]; constant bits(esize) op2elt = Elem[D[m+r],2*e+1,esize]; constant integer element1 = if unsigned then UInt(op1elt) else SInt(op1elt); constant integer element2 = if unsigned then UInt(op2elt) else SInt(op2elt); constant integer result = element1 + element2; Elem[D[d+r],e,2*esize] = result<2*esize-1:0>;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.