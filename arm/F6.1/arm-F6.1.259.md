## F6.1.259 VUSDOT (vector)

Dot Product vector form with mixed-sign integers. This instruction performs the dot product of the four unsigned 8-bit integer values in each 32-bit element of the first source register with the four signed 8-bit integer values in the corresponding 32-bit element of the second source register, accumulating the result into the corresponding 32-bit element of the destination register.

From Armv8.2, this is an OPTIONAL instruction. ID\_ISAR6.I8MM indicates whether this instruction is supported in the T32 and A32 instruction sets.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_AA32I8MM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

VUSDOT{&lt;q&gt;}.S8

&lt;Dd&gt;, &lt;Dn&gt;, &lt;Dm&gt;

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VUSDOT{<q>}.S8
```

```
<Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_AA32I8MM) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '1' then 2 else 1;
```

T1

(FEAT\_AA32I8MM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VUSDOT{<q>}.S8 <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when (Q == 1)

```
VUSDOT{<q>}.S8 <Qd>, <Qn>, <Qm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32I8MM) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer regs = if Q == '1' then 2 else 1;
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP third source and destination register, encoded in the 'D:Vd' field.

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
CheckAdvSIMDEnabled(); bits(64) operand1; bits(64) operand2; bits(64) result; for r = 0 to regs-1 operand1 = Din[n+r]; operand2 = Din[m+r]; result = Din[d+r]; for e = 0 to 1 bits(32) res = Elem[result, e, 32]; for b = 0 to 3 constant integer element1 = UInt(Elem[operand1, 4 * e + b, 8]); constant integer element2 = SInt(Elem[operand2, 4 * e + b, 8]); res = res + element1 * element2; Elem[result, e, 32] = res; D[d+r] = result;
```

Is the 128-bit name of the SIMD&amp;FP third source and destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.