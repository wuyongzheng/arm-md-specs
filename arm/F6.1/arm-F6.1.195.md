## F6.1.195 VREV16

Vector Reverse in halfwords reverses the order of 8-bit elements in each halfword of the vector, and places the result in the corresponding destination vector.

There is no distinction between data types, other than size.

## VREV16.8, doubleword

Figure F6-6 VREV16 doubleword operation

<!-- image -->

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when
```

```
(Q == 0) VREV16{<c>}{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VREV16{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if UInt(op)+UInt(size) >= 3 then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer container_size = 64 >> UInt(op); constant integer containers = 64 DIV container_size; constant integer elements_per_container = container_size DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VREV16{<c>}{<q>}.<dt>
```

```
<Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when
```

```
(Q == 1) VREV16{<c>}{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if UInt(op)+UInt(size) >= 3 then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer esize = 8 << UInt(size); constant integer container_size = 64 >> UInt(op); constant integer containers = 64 DIV container_size; constant integer elements_per_container = container_size DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

<!-- image -->

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the operand, encoded in 'size':

| size   | <dt>     |
|--------|----------|
| 00     | 8        |
| 01     | RESERVED |
| 1x     | RESERVED |

<!-- image -->

&lt;dt&gt;

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

&lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

&lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(64) result; integer element; integer rev_element; for r = 0 to regs-1 element = 0; for c = 0 to containers-1 rev_element = (element + elements_per_container) -1; for e = 0 to elements_per_container-1 Elem[result, rev_element, esize] = Elem[D[m+r], element, esize]; element = element + 1; rev_element = rev_element - 1; D[d+r] = result;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.