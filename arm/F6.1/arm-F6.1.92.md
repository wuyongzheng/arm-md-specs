## F6.1.92 VFMSL (vector)

Vector Floating-point Multiply-Subtract Long from accumulator (vector). This instruction negates the values in the vector of one SIMD&amp;FP register, multiplies these with the corresponding values in another vector, and accumulates the product to the corresponding vector element of the destination SIMD&amp;FP register. The instruction does not round the result of the multiply before the accumulation.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

In Armv8.2 and Armv8.3, this is an OPTIONAL instruction. From Armv8.4 it is mandatory for all implementations to support it.

Note

ID\_ISAR6.FHM indicates whether this instruction is supported.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

(FEAT\_FHM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VFMSL{<q>}.F16
```

```
<Dd>, <Sn>, <Sm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VFMSL{<q>}.F16
```

```
<Qd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FHM) then UNDEFINED; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = if Q == '1' then UInt(N:Vn) else constant integer m = if Q == '1' then UInt(M:Vm) else constant integer esize = 32; constant integer datasize = 32 << UInt(Q); constant boolean sub_op = S == '1'; constant integer regs = if Q == '0' then 1 else 2;
```

```
UInt(Vn:N); UInt(Vm:M);
```

T1

(FEAT\_FHM)

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

```
(Q == 0)
```

```
VFMSL{<q>}.F16 <Dd>, <Sn>, <Sm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VFMSL{<q>}.F16 <Qd>, <Dn>, <Dm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_FHM) then UNDEFINED; if Q == '1' && Vd<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = if Q == '1' then UInt(N:Vn) else constant integer m = if Q == '1' then UInt(M:Vm) else constant integer esize = 32; constant integer regs = 1 << UInt(Q); constant integer datasize = 32 << UInt(Q); constant boolean sub_op = S == '1';
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;Dd&gt;

&lt;Sn&gt;

Is the 32-bit name of the first SIMD&amp;FP source register, encoded in the 'Vn:N' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm:M' field.

&lt;Qd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

```
UInt(Vn:N); UInt(Vm:M);
```

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## Operation

```
CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); bits(datasize) operand1; bits(datasize) operand2; bits(64) operand3; bits(64) result; bits(esize DIV 2) element1; bits(esize DIV 2) element2; if Q=='0' then operand1 = S[n]<datasize-1:0>; operand2 = S[m]<datasize-1:0>; else operand1 = D[n]<datasize-1:0>; operand2 = D[m]<datasize-1:0>; for r = 0 to regs-1 operand3 = D[d+r]; for e = 0 to 1 element1 = Elem[operand1, 2*r+e, esize DIV 2]; element2 = Elem[operand2, 2*r+e, esize DIV 2]; if sub_op then element1 = FPNeg(element1, fpcr); Elem[result, e, esize] = FPMulAddH(Elem[operand3, e, esize], element1, element2, fpcr); D[d+r] = result;
```