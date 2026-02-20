## F6.1.59 VCVT (between half-precision and single-precision, Advanced SIMD)

Vector Convert between half-precision and single-precision converts each element in a vector from single-precision to half-precision floating-point, or from half-precision to single-precision, and places the results in a second vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the Half-precision to single-precision variant

```
Applies when (op == 1) VCVT{<c>}{<q>}.F32.F16 <Qd>,
```

```
<Dm>
```

## Encoding for the Single-precision to half-precision variant

```
Applies when (op == 0) VCVT{<c>}{<q>}.F16.F32 <Dd>, <Qm>
```

## Decode for all variants of this encoding

```
if size != '01' then UNDEFINED; if op == '1' && Vd<0> == '1' then UNDEFINED; if op == '0' && Vm<0> == '1' then UNDEFINED; constant boolean half_to_single = (op == '1'); constant integer esize = 16; constant integer elements = 4; constant integer m = UInt(M:Vm); constant integer d = UInt(D:Vd);
```

T1

<!-- image -->

## Encoding for the Half-precision to single-precision variant

```
Applies when (op == 1) VCVT{<c>}{<q>}.F32.F16 <Qd>,
```

```
<Dm>
```

## Encoding for the Single-precision to half-precision variant

Applies when

```
(op == 0) VCVT{<c>}{<q>}.F16.F32 <Dd>,
```

```
<Qm>
```

## Decode for all variants of this encoding

```
'1');
```

```
if size != '01' then UNDEFINED; if op == '1' && Vd<0> == '1' then UNDEFINED; if op == '0' && Vm<0> == '1' then UNDEFINED; constant boolean half_to_single = (op == constant integer esize = 16; constant integer elements = 4; constant integer m = UInt(M:Vm); constant integer d = UInt(D:Vd);
```

## Assembler Symbols

&lt;c&gt;

For the 'A1 Half-precision to single-precision' and 'A1 Single-precision to half-precision' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 Half-precision to single-precision' and 'T1 Single-precision to half-precision' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;q&gt;

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Dd&gt;

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for e = 0 to elements-1 if half_to_single then Elem[Q[d>>1],e,32] = FPConvert(Elem[Din[m],e,16], fpcr, 32); else Elem[D[d],e,16] = FPConvert(Elem[Qin[m>>1],e,32], fpcr, 16);
```