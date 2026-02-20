## F6.1.99 VJCVT

Javascript Convert to signed fixed-point, rounding toward Zero. This instruction converts the double-precision floating-point value in the SIMD&amp;FP source register to a 32-bit signed integer using the Round towards Zero rounding mode, and writes the result to the SIMD&amp;FP destination register. If the result is too large to be accommodated as a signed 32-bit integer, then the result is the integer modulo 2 32 , as held in a 32-bit signed integer.

This instruction can generate a floating-point exception. Depending on the settings in FPSCR, the exception results in either a flag being set or a synchronous exception being generated. For more information, see Floating-point exceptions and exception traps.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_JSCVT)

<!-- image -->

## Encoding

```
VJCVT{<q>}.S32.F64 <Sd>, <Dm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_JSCVT) then if cond != '1110' then UNPREDICTABLE; constant integer d = UInt(Vd:D); constant integer m = UInt(M:Vm);
```

## T1

(FEAT\_JSCVT)

<!-- image -->

## Encoding

```
VJCVT{<q>}.S32.F64 <Sd>, <Dm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_JSCVT) then UNDEFINED; if InITBlock() then UNPREDICTABLE; constant integer d = UInt(Vd:D); constant integer m = UInt(M:Vm);
```

```
UNDEFINED;
```

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP source register, encoded in the 'M:Vm' field.

## Operation

```
EncodingSpecificOperations(); CheckVFPEnabled(TRUE); constant bits(64) fltval = D[m]; bits(32) intval; bit Z; (intval, Z) = FPSCR<31:28> = '0':Z:'00'; S[d] = intval;
```

```
FPToFixedJS(fltval, EffectiveFPCR());
```