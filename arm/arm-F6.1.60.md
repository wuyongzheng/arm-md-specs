## F6.1.60 VCVT (between floating-point and integer, Advanced SIMD)

Vector Convert between floating-point and integer converts each element in a vector from floating-point to integer, or from integer to floating-point, and places the results in a second vector.

The vector elements are the same type, and are floating-point numbers or integers. Signed and unsigned integers are distinct.

The floating-point to integer operation uses the Round towards Zero rounding mode. The integer to floating-point operation uses the Round to Nearest rounding mode.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when

(Q == 0)

```
VCVT{<c>}{<q>}.<dt1>.<dt2> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
(Q == 1) VCVT{<c>}{<q>}.<dt1>.<dt2>
```

```
<Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if size IN {'00', '11'} then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then constant boolean to_integer = (op<1> == '1'); constant boolean unsigned = (op<0> == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
UNDEFINED;
```

```
VCVT{<c>}{<q>}.<dt1>.<dt2> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

Applies when

```
VCVT{<c>}{<q>}.<dt1>.<dt2>
```

```
(Q == 1) <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if size IN {'00', '11'} then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if size == '01' && InITBlock() then UNPREDICTABLE; constant boolean to_integer = (op<1> == '1'); constant boolean unsigned = (op<0> == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If size == '01' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1 128-bit SIMD vector' and 'A1 64-bit SIMD vector' variants: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1 128-bit SIMD vector' and 'T1 64-bit SIMD vector' variants: see Standard assembler syntax fields.

See Standard assembler syntax fields.

&lt;dt1&gt;

Is the data type for the elements of the destination vector, encoded in 'size:op':

|   size | op   | <dt1>   |
|--------|------|---------|
|     01 | 0x   | F16     |
|     01 | 10   | S16     |
|     01 | 11   | U16     |
|     10 | 0x   | F32     |
|     10 | 10   | S32     |
|     10 | 11   | U32     |

<!-- image -->

## &lt;dt2&gt;

Is the data type for the elements of the source vector, encoded in 'size:op':

|   size | op   | <dt2>   |
|--------|------|---------|
|     01 | 00   | S16     |
|     01 | 01   | U16     |
|     01 | 1x   | F16     |
|     10 | 00   | S32     |
|     10 | 01   | U32     |
|     10 | 1x   | F32     |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); bits(esize) result; for r = 0 to regs-1 for e = 0 to elements-1 constant bits(esize) operand1 = Elem[D[m+r],e,esize]; if to_integer then result = FPToFixed(operand1, 0, unsigned, fpcr, FPRounding_ZERO, esize); else result = FixedToFP(operand1, 0, unsigned, fpcr, FPRounding_TIEEVEN, esize); Elem[D[d+r],e,esize] = result;
```

## &lt;Dd&gt;