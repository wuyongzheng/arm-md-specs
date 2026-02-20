## F6.1.165 VPMAX (floating-point)

Vector Pairwise Maximum (floating-point)

Vector Pairwise Maximum compares adjacent pairs of elements in two doubleword vectors, and copies the larger of each pair into the corresponding element in the destination doubleword vector.

Depending on settings in the CPACR, NSACR, and HCPTR registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VPMAX{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Decode for this encoding

```
if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then constant boolean maximum = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

T1

<!-- image -->

## Encoding

```
VPMAX{<c>}{<q>}.<dt> {<Dd>, }<Dn>, <Dm>
```

## Decode for this encoding

```
if sz == '1' && !IsFeatureImplemented(FEAT_FP16) then if sz == '1' && InITBlock() then UNPREDICTABLE; constant boolean maximum = (op == '0'); constant integer esize = 32 >> UInt(sz); constant integer elements = 64 DIV esize; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

```
UNDEFINED;
```

## CONSTRAINED UNPREDICTABLE behavior

If sz == '1' &amp;&amp; InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;c&gt;

For the 'A1' variant: see Standard assembler syntax fields. This encoding must be unconditional.

For the 'T1' variant: see Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the data type for the elements of the vectors, encoded in 'sz':

|   sz | <dt>   |
|------|--------|
|    0 | F32    |
|    1 | F16    |

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field.

&lt;q&gt;

&lt;dt&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckAdvSIMDEnabled(); bits(64) dest; constant FPCR_Type fpcr = StandardFPCR(); constant integer h = elements DIV 2; for e = 0 to h-1 bits(esize) op1elt = Elem[D[n],2*e,esize]; bits(esize) op2elt = Elem[D[n],2*e+1,esize]; Elem[dest,e,esize] = (if maximum then FPMax(op1elt, op2elt, fpcr) else FPMin(op1elt, op2elt, fpcr)); op1elt = Elem[D[m],2*e,esize]; op2elt = Elem[D[m],2*e+1,esize]; Elem[dest,e+h,esize] = (if maximum then FPMax(op1elt, op2elt, fpcr) else FPMin(op1elt, op2elt, fpcr)); D[d] = dest;
```