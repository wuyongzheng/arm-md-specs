## C7.2.119 FJCVTZS

Floating-point Javascript convert to signed fixed-point, rounding toward zero

This instruction converts the double-precision floating-point value in the SIMD&amp;FP source register to a 32-bit signed integer using the Round towards Zero rounding mode, and writes the result to the general-purpose destination register. If the result is too large to be represented as a signed 32-bit integer, then the result is the integer modulo 2 32 , as held in a 32-bit signed integer.

This instruction can generate a floating-point exception. Depending on the settings in FPCR, the exception results in either a flag being set in FPSR or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on the settings in the CPACR\_EL1, CPTR\_EL2, and CPTR\_EL3 registers, and the current Security state and Exception level, an attempt to execute the instruction might be trapped.

## Double-precision to 32-bit

(FEAT\_JSCVT)

<!-- image -->

## Encoding

```
FJCVTZS <Wd>, <Dn>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_JSCVT) then EndOfDecode(Decode_UNDEF); constant integer d = UInt(Rd); constant integer n = UInt(Rn);
```

## Assembler Symbols

&lt;Wd&gt;

Is the 32-bit name of the general-purpose destination register, encoded in the 'Rd' field.

## &lt;Dn&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'Rn' field.

## Operation

```
AArch64.CheckFPAdvSIMDEnabled(); constant bits(64) fltval = V[n, 64]; bits(32) intval; bit z; (intval, z) = FPToFixedJS(fltval, FPCR); X[d, 32] = intval; PSTATE.<N,Z,C,V> = '0':z:'00';
```
