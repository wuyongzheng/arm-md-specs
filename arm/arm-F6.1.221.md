## F6.1.221 VSDOT (vector)

Dot Product vector form with signed integers. This instruction performs the dot product of the four 8-bit elements in each 32-bit element of the first source register with the four 8-bit elements of the corresponding 32-bit element in the second source register, accumulating the result into the corresponding 32-bit element of the destination register.

In Armv8.2 and Armv8.3, this is an OPTIONAL instruction. From Armv8.4 it is mandatory for all implementations to support it.

```
Note ID_ISAR6.DP indicates whether this instruction is supported.
```

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_DotProd)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0)
```

```
VSDOT{<q>}.S8 <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VSDOT{<q>}.S8 <Qd>, <Qn>,
```

```
<Qm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_DotProd) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean signed = U=='0'; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 32; constant integer regs = if Q == '1' then 2 else 1;
```

T1

(FEAT\_DotProd)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
VSDOT{<q>}.S8 <Dd>, <Dn>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VSDOT{<q>}.S8 <Qd>, <Qn>,
```

```
(Q == 1) <Qm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_DotProd) then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean signed = U=='0'; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer esize = 32; constant integer regs = if Q == '1' then 2 else 1;
```

## Assembler Symbols

## &lt;q&gt;

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

- &lt;Qd&gt;

## &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
bits(64) operand1; bits(64) operand2; bits(64) result; CheckAdvSIMDEnabled(); for r = 0 to regs-1 operand1 = D[n+r]; operand2 = D[m+r]; result = D[d+r]; integer element1, for e = 0 to 1 integer res = 0;
```

```
element2; for i = 0 to 3
```

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

```
if signed then element1 = SInt(Elem[operand1, 4 * e + i, esize DIV 4]); element2 = SInt(Elem[operand2, 4 * e + i, esize DIV 4]); else element1 = UInt(Elem[operand1, 4 * e + i, esize DIV 4]); element2 = UInt(Elem[operand2, 4 * e + i, esize DIV 4]); res = res + element1 * element2; Elem[result, e, esize] = Elem[result, e, esize] + res; D[d+r] = result;
```