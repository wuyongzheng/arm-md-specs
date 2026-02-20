## F6.1.35 VBIC (register)

Vector Bitwise Bit Clear (register) performs a bitwise AND between a register value and the complement of a register value, and places the result in the destination register.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VBIC{<c>}{<q>}{.<dt>} {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when
```

```
(Q == 1) VBIC{<c>}{<q>}{.<dt>} {<Qd>, }<Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VBIC{<c>}{<q>}{.<dt>} {<Dd>, }<Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VBIC{<c>}{<q>}{.<dt>} {<Qd>, }<Qn>, <Qm>
```

```
UNDEFINED;
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

An optional data type. It is ignored by assemblers, and does not affect the encoding.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); for r = 0 to regs-1 D[d+r] = D[n+r]
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

```
AND NOT(D[m+r]);
```