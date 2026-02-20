## F6.1.201 VRINTM (Advanced SIMD)

Vector Round floating-point to integer towards -Infinity rounds a vector of floating-point values to integral floating-point values of the same size, using the Round towards -Infinity rounding mode. A zero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRINTM{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VRINTM{<q>}.<dt>
```

```
<Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if op<2> != op<0> then SEE "Related encodings"; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if (size == '01' && !IsFeatureImplemented(FEAT_FP16)) || size IN {'00', '11'} then UNDEFINED; // Rounding encoded differently from other VCVT and VRINT instructions constant FPRounding rounding = FPDecodeRM(op<2>:NOT(op<1>)); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRINTM{<q>}.<dt>
```

```
<Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1)
```

```
VRINTM{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if op<2> != op<0> then SEE "Related encodings"; if InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if (size == '01' && !IsFeatureImplemented(FEAT_FP16)) || size IN {'00', '11'} then UNDEFINED; // Rounding encoded differently from other VCVT and VRINT instructions constant FPRounding rounding = FPDecodeRM(op<2>:NOT(op<1>)); constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

Related encodings: See Advanced SIMD two registers misc for the T32 instruction set, or Advanced SIMD two registers misc for the A32 instruction set.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'size':

|   size | <dt>   |
|--------|--------|
|     01 | F16    |
|     10 | F32    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

&lt;dt&gt;

## &lt;Dd&gt;

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) operand1 = Elem[D[m+r],e,esize]; constant bits(esize) result = FPRoundInt(operand1, fpcr, rounding, Elem[D[d+r],e,esize] = result;
```

```
exact);
```