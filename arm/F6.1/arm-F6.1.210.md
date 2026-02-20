## F6.1.210 VRINTZ (Advanced SIMD)

Vector round floating-point to integer towards Zero rounds a vector of floating-point values to integral floating-point values of the same size, using the Round towards Zero rounding mode. A zero input gives a zero result with the same sign, an infinite input gives an infinite result with the same sign, and a NaN is propagated as for normal arithmetic.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRINTZ{<q>}.<dt>
```

```
<Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VRINTZ{<q>}.<dt>
```

```
<Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if (size == '01' && !IsFeatureImplemented(FEAT_FP16)) || size IN {'00', '11'} then UNDEFINED; constant FPRounding rounding = FPRounding_ZERO; constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when (Q == 0) VRINTZ{<q>}.<dt> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VRINTZ{<q>}.<dt> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if (size == '01' && !IsFeatureImplemented(FEAT_FP16)) || size IN {'00', '11'} then UNDEFINED; constant FPRounding rounding = FPRounding_ZERO; constant boolean exact = FALSE; constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2; if InITBlock() then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

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

&lt;Qd&gt;

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