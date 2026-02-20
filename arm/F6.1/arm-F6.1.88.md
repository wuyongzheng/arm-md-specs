## F6.1.88 VFMAB, VFMAT (BFloat16, by scalar)

BFloat16 floating-point widening multiply-add long (by scalar)

The BFloat16 floating-point widening multiply-add long instruction widens the even-numbered (bottom) or odd-numbered (top) 16-bit elements in the first source vector, and an indexed element in the second source vector from Bfloat16 to single-precision format. The instruction then multiplies and adds these values to the overlapping single-precision elements of the destination vector.

Unlike other BFloat16 multiplication instructions, this performs a fused multiply-add, without intermediate rounding that uses the Round to Nearest rounding mode and can generate a floating-point exception that causes cumulative exception bits in the FPSCR to be set.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VFMA<bt>{<q>}.BF16 <Qd>, <Qn>, <Dm>[<index>]
```

## Decode for this encoding

```
UNDEFINED;
```

```
if !IsFeatureImplemented(FEAT_AA32BF16) then if Vd<0> == '1' || Vn<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(Vm<2:0>); constant integer i = UInt(M:Vm<3>); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
```

## T1

(FEAT\_AA32BF16)

<!-- image -->

## Encoding

```
VFMA<bt>{<q>}.BF16 <Qd>, <Qn>, <Dm>[<index>]
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_AA32BF16) then if Vd<0> == '1' || Vn<0> == '1' then UNDEFINED; constant integer d = UInt(D:Vd); constant integer n = UInt(N:Vn); constant integer m = UInt(Vm<2:0>); constant integer i = UInt(M:Vm<3>); constant integer elements = 128 DIV 32; constant integer sel = UInt(Q);
```

## Assembler Symbols

&lt;bt&gt;

Is the bottom or top element specifier, encoded in 'Q':

|   Q | <bt>   |
|-----|--------|
|   0 | B      |
|   1 | T      |

&lt;q&gt;

## &lt;Qd&gt;

&lt;Qn&gt;

Is the 128-bit name of the first SIMD&amp;FP source register, encoded in the 'N:Vn' field as &lt;Qn&gt;*2.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register, encoded in the 'Vm&lt;2:0&gt;' field.

## &lt;index&gt;

Is the element index in the range 0 to 3, encoded in the 'M:Vm&lt;3&gt;' field.

## Operation

```
CheckAdvSIMDEnabled(); constant FPCR_Type fpcr = StandardFPCR(); constant bits(128) operand1 = Q[n>>1]; constant bits(64) operand2 = D[m]; constant bits(128) operand3 = Q[d>>1]; bits(128) result; constant bits(32) element2 = Elem[operand2, i, 16] : Zeros(16); for e = 0 to elements-1 constant bits(32) element1 = Elem[operand1, 2 * e + sel, 16] : constant bits(32) addend = Elem[operand3, e, 32]; Elem[result, e, 32] = FPMulAdd(addend, element1, element2, fpcr); Q[d>>1] = result;
```

See Standard assembler syntax fields.

Is the 128-bit name of the SIMD&amp;FP destination register, encoded in the 'D:Vd' field as &lt;Qd&gt;*2.

```
UNDEFINED;
```

```
Zeros(16);
```