## C7.2.168 FNMSUB

Floating-point negated fused multiply-subtract (scalar)

This instruction multiplies the values of the first two SIMD&amp;FP source registers, subtracts the value of the third SIMD&amp;FP source register, and writes the result to the destination SIMD&amp;FP register.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

<!-- image -->

## Encoding for the Half-precision variant

(FEAT\_FP16) Applies when (ftype == 11)

```
FNMSUB <Hd>, <Hn>, <Hm>, <Ha>
```

## Encoding for the Single-precision variant

(FEAT\_FP) Applies when (ftype == 00)

```
FNMSUB <Sd>, <Sn>, <Sm>, <Sa>
```

## Encoding for the Double-precision variant

```
(FEAT_FP) Applies when (ftype == 01)
```

```
FNMSUB <Dd>, <Dn>, <Dm>, <Da>
```

## Decode for all variants of this encoding

```
if !IsFeatureImplemented(FEAT_FP) then EndOfDecode(Decode_UNDEF); if ftype == '10' then EndOfDecode(Decode_UNDEF); if ftype == '11' && !IsFeatureImplemented(FEAT_FP16) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn); constant integer m = UInt(Rm); constant integer a = UInt(Ra); constant integer esize = 8 << UInt(ftype EOR '10');
```

## Assembler Symbols

## &lt;Hd&gt;

Is the 16-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

## &lt;Hn&gt;

Is the 16-bit name of the first SIMD&amp;FP source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Hm&gt;

Is the 16-bit name of the second SIMD&amp;FP source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Ha&gt;

## &lt;Sd&gt;

## &lt;Sn&gt;

Is the 32-bit name of the first SIMD&amp;FP source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Sm&gt;

Is the 32-bit name of the second SIMD&amp;FP source register holding the multiplier, encoded in the 'Rm' field.

&lt;Sa&gt;

## &lt;Dd&gt;

## &lt;Dn&gt;

Is the 64-bit name of the first SIMD&amp;FP source register holding the multiplicand, encoded in the 'Rn' field.

## &lt;Dm&gt;

Is the 64-bit name of the second SIMD&amp;FP source register holding the multiplier, encoded in the 'Rm' field.

## &lt;Da&gt;

Is the 64-bit name of the third SIMD&amp;FP source register holding the minuend, encoded in the 'Ra' field.

## Operation

```
AArch64.CheckFPEnabled(); constant bits(esize) addend = FPNeg(V[a, esize], FPCR); constant bits(esize) operand1 = V[n, esize]; constant bits(esize) operand2 = V[m, esize]; bits(128) result = if IsMerging(FPCR) then V[a, 128] else Zeros(128); Elem[result, 0, esize] = FPMulAdd(addend, operand1, operand2, FPCR); V[d, 128] = result;
```

Is the 16-bit name of the third SIMD&amp;FP source register holding the minuend, encoded in the 'Ra' field.

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.

Is the 32-bit name of the third SIMD&amp;FP source register holding the minuend, encoded in the 'Ra' field.

Is the 64-bit name of the SIMD&amp;FP destination register, encoded in the 'Rd' field.
