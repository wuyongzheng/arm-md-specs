## F6.1.73 VCVTP (Advanced SIMD)

Vector Convert floating-point to integer with Round towards +Infinity converts each element in a vector from floating-point to integer using the Round towards +Infinity rounding mode, and places the results in a second vector.

The operand vector elements are floating-point numbers.

The result vector elements are integers, and the same size as the operand vector elements. Signed and unsigned integers are distinct.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

```
Applies when
```

```
(Q == 0) VCVTP{<q>}.<dt>.<dt2> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCVTP{<q>}.<dt>.<dt2> <Qd>,
```

```
<Qm>
```

## Decode for all variants of this encoding

```
if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if size IN {'00', '11'} then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then constant FPRounding rounding = FPDecodeRM(RM); constant boolean unsigned = (op == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

T1

<!-- image -->

## Encoding for the 64-bit SIMD vector variant

Applies when (Q == 0)

```
UNDEFINED;
```

```
VCVTP{<q>}.<dt>.<dt2> <Dd>, <Dm>
```

## Encoding for the 128-bit SIMD vector variant

```
Applies when (Q == 1) VCVTP{<q>}.<dt>.<dt2> <Qd>, <Qm>
```

## Decode for all variants of this encoding

```
if InITBlock() then UNPREDICTABLE; if Q == '1' && (Vd<0> == '1' || Vm<0> == '1') then UNDEFINED; if size IN {'00', '11'} then UNDEFINED; if size == '01' && !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; constant FPRounding rounding = FPDecodeRM(RM); constant boolean unsigned = (op == '1'); constant integer esize = 8 << UInt(size); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer m = UInt(M:Vm); constant integer regs = if Q == '0' then 1 else 2;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

Is the data type for the elements of the destination, encoded in 'op:size':

|   op |   size | <dt>   |
|------|--------|--------|
|    0 |     01 | S16    |
|    0 |     10 | S32    |
|    1 |     01 | U16    |
|    1 |     10 | U32    |

&lt;dt2&gt;

Is the data type for the elements of the source vector, encoded in 'size':

&lt;dt&gt;

## &lt;Dd&gt;

|   size | <dt2>   |
|--------|---------|
|     01 | F16     |
|     10 | F32     |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## &lt;Qd&gt;

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

## &lt;Qm&gt;

Is the 128-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
EncodingSpecificOperations(); CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); for r = 0 to regs-1 for e = 0 to elements-1 Elem[D[d+r],e,esize] = FPToFixed(Elem[D[m+r],e,esize],
```

```
0, unsigned, fpcr, rounding, esize);
```