## F6.1.63 VCVT (between floating-point and fixed-point, Advanced SIMD)

Vector Convert between floating-point and fixed-point converts each element in a vector from floating-point to fixed-point, or from fixed-point to floating-point, and places the results in a second vector.

The vector elements are the same type, and are floating-point numbers or integers. Signed and unsigned integers are distinct.

The floating-point to fixed-point operation uses the Round towards Zero rounding mode. The fixed-point to floating-point operation uses the Round to Nearest rounding mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCVT{<c>}{<q>}.<dt1>.<dt2>
```

```
<Dd>, <Dm>, #<fbits>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCVT{<c>}{<q>}.<dt1>.<dt2> <Qd>, <Qm>, #<fbits>
```

## Decode for all variants of this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if op<1> == '0' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if op<1> == '0' && imm6 == '10xxxx' then UNDEFINED; if imm6 == '0xxxxx' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean to_fixed = (op<0> == '1'); constant integer frac_bits = 64 -UInt(imm6); constant boolean unsigned = (U == '1'); constant integer esize = 16 << UInt(op<1>); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VCVT{<c>}{<q>}.<dt1>.<dt2>
```

```
<Dd>, <Dm>, #<fbits>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when
```

```
(Q == 1)
```

```
VCVT{<c>}{<q>}.<dt1>.<dt2>
```

```
<Qd>, <Qm>, #<fbits>
```

## Decode for all variants of this encoding

```
if imm6 == '000xxx' then SEE "Related encodings"; if op<1> == '0' && !IsFeatureImplemented(FEAT_FP16) then if op<1> == '0' && imm6 == '10xxxx' then UNDEFINED; if imm6 == '0xxxxx' then UNDEFINED; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; constant boolean to_fixed = (op<0> == '1'); constant integer frac_bits = 64 -UInt(imm6); constant boolean unsigned = (U == '1'); constant integer esize = 16 << UInt(op<1>); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

```
UNDEFINED;
```

Related encodings: See Advanced SIMD one register and modified immediate for the T32 instruction set, or Advanced SIMD one register and modified immediate for the A32 instruction set.

## Assembler Symbols

<!-- image -->

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

- &lt;dt1&gt; Is the data type for the elements of the destination vector, encoded in 'op:U':

|   op | U   | <dt1>   |
|------|-----|---------|
|   00 | x   | F16     |
|   01 | 0   | S16     |
|   01 | 1   | U16     |
|   10 | x   | F32     |
|   11 | 0   | S32     |
|   11 | 1   | U32     |

<!-- image -->

## &lt;dt2&gt;

Is the data type for the elements of the source vector, encoded in 'op:U':

|   op | U   | <dt2>   |
|------|-----|---------|
|   00 | 0   | S16     |
|   00 | 1   | U16     |
|   01 | x   | F16     |
|   10 | 0   | S32     |
|   10 | 1   | U32     |
|   11 | x   | F32     |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;fbits&gt;

The number of fraction bits in the fixed point number, in the range 1 to 32 for 32-bit elements, or in the range 1 to 16 for 16-bit elements:

- (64 &lt;fbits&gt; ) is encoded in imm6.

An assembler can permit an &lt;fbits&gt; value of 0. This is encoded as floating-point to integer or integer to floating-point instruction, see VCVT (between floating-point and integer, Advanced SIMD).

## &lt;Dd&gt;

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(esize) result; constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) operand1 = Elem[D[m+r],e,esize]; if to_fixed then result = FPToFixed(operand1, frac_bits, unsigned, fpcr, FPRounding_ZERO, esize); else result = FixedToFP(operand1, frac_bits, unsigned, fpcr, FPRounding_TIEEVEN, esize); Elem[D[d+r],e,esize] = result;
```