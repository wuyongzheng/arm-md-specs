## F6.1.87 VFMAB, VFMAT (BFloat16, vector)

BFloat16 floating-point widening multiply-add long (vector)

The Bfloat16 floating-point widening multiply-add long instruction widens the even-numbered (bottom) or odd-numbered (top) 16-bit elements in the first and second source vectors from Bfloat16 to single-precision format. The instruction then multiplies and adds these values to the overlapping single-precision elements of the destination vector.

Unlike other BFloat16 multiplication instructions, this performs a fused multiply-add, without intermediate rounding that uses the Round to Nearest rounding mode and can generate a floating-point exception that causes cumulative exception bits in the FPSCR to be set.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VFMA<bt>{<q>}.BF16 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
UNDEFINED;
```

```
if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
```

## T1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VFMA<bt>{<q>}.BF16 <Qd>, <Qn>, <Qm>
```

## Decode for this encoding

```
UNDEFINED;
```

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32BF16) then UNDEFINED; if Vd<0> == '1' || Vn<0> == '1' || Vm<0> == '1' then constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(M:Vm); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
```

## Assembler Symbols

&lt;bt&gt;

Is the bottom or top element specifier, encoded in 'Q':

|   Q | <bt>   |
|-----|--------|
|   0 | B      |
|   1 | T      |

&lt;q&gt;

- &lt;Qd&gt;
- &lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

- &lt;Qm&gt;

Is the 128-bit name of the second SIMD&amp;FP source register, encoded in the 'M:Vm' field as &lt;Qm&gt;*2.

## Operation

```
CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(128) operand1 = Q[n>>1]; constant bits(128) operand2 = Q[m>>1]; constant bits(128) operand3 = Q[d>>1]; bits(128) result; for e = 0 to elements-1 constant bits(32) element1 = Elem[operand1, 2 * e + sel, 16] : Zeros(16); constant bits(32) element2 = Elem[operand2, 2 * e + sel, 16] : Zeros(16); constant bits(32) addend = Elem[operand3, e, 32]; Elem[result, e, 32] = FPMulAdd(addend, element1, element2, fpcr); Q[d>>1] = result;
```

See Standard assembler syntax fields.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.