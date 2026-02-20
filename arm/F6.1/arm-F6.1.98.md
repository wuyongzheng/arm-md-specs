## F6.1.98 VINS

Vector move Insertion. This instruction copies the lower 16 bits of the 32-bit source SIMD&amp;FP register into the upper 16 bits of the 32-bit destination SIMD&amp;FP register, while preserving the values in the remaining bits.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_FP16)

<!-- image -->

## Encoding

```
VINS{<q>}.F16 <Sd>, <Sm>
```

## Decode for this encoding

```
if !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if FPSCR.Len != '000' || FPSCR.Stride != '00' then constant integer d = UInt(Vd:D); constant integer m = UInt(Vm:M);
```

T1

(FEAT\_FP16)

<!-- image -->

## Encoding

```
VINS{<q>}.F16 <Sd>, <Sm>
```

## Decode for this encoding

```
if InITBlock() then UNPREDICTABLE; if !IsFeatureImplemented(FEAT_FP16) then UNDEFINED; if FPSCR.Len != '000' || FPSCR.Stride != '00' then UNDEFINED; constant integer d = UInt(Vd:D); constant integer m = UInt(Vm:M);
```

```
UNDEFINED;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

## Assembler Symbols

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Sd&gt;

Is the 32-bit name of the SIMD&amp;FP destination register, encoded in the 'Vd:D' field.

## &lt;Sm&gt;

Is the 32-bit name of the SIMD&amp;FP source register, encoded in the 'Vm:M' field.

## Operation

```
EncodingSpecificOperations();
```

```
if ConditionPassed() then CheckVFPEnabled(TRUE); S[d]<31:16> = H[m];
```