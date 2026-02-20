## F6.1.81 VDUP (general-purpose register)

Duplicate general-purpose register to vector duplicates an element from a general-purpose register into every element of the destination vector.

The destination vector elements can be 8-bit, 16-bit, or 32-bit fields. The source element is the least significant 8, 16, or 32 bits of the general-purpose register. There is no distinction between data types.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VDUP{<c>}{<q>}.<size> <Dd>, <Rt>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VDUP{<c>}{<q>}.<size> <Qd>, <Rt>
```

## Decode for all variants of this encoding

```
if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer t = UInt(Rt); constant integer regs = if Q == '0' then 1 else if B:E == '11' then UNDEFINED; constant integer esize = 32 >> UInt(B:E); constant integer elements = 64 DIV esize; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VDUP{<c>}{<q>}.<size> <Dd>,
```

```
<Rt>
```

```
2;
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VDUP{<c>}{<q>}.<size> <Qd>,
```

```
<Rt>
```

## Decode for all variants of this encoding

```
if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer t = UInt(Rt); constant integer regs = if Q == '0' then 1 else if B:E == '11' then UNDEFINED; constant integer esize = 32 >> UInt(B:E); constant integer elements = 64 DIV esize; // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

```
2;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields. Arm strongly recommends that any VDUP instruction is unconditional, see Conditional execution.

See Standard assembler syntax fields.

&lt;size&gt;

The data size for the elements of the destination vector. It must be one of:

```
8 Encoded as [b, e] = 0b10 . 16 Encoded as [b, e] = 0b01 . 32 Encoded as [b, e] = 0b00 .
```

The destination vector for a doubleword operation.

The Arm source register.

&lt;q&gt;

&lt;Dd&gt;

&lt;Rt&gt;

&lt;Qd&gt;

The destination vector for a quadword operation.

## Operation

```
if ConditionPassed() then R[t]<esize-1:0>;
```

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant bits(esize) scalar = for r = 0 to regs-1 for e = 0 to elements-1 Elem[D[d+r],e,esize] = scalar;
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.