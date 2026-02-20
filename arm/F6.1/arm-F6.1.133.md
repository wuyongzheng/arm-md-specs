## F6.1.133 VMOV (between general-purpose register and half-precision)

Copy 16 bits of a general-purpose register to or from a 32-bit SIMD&amp;FP register

Copy 16 bits of a general-purpose register to or from a 32-bit SIMD&amp;FP register. This instruction transfers the value held in the bottom 16 bits of a 32-bit SIMD&amp;FP register to the bottom 16 bits of a general-purpose register, or the value held in the bottom 16 bits of a general-purpose register to the bottom 16 bits of a 32-bit SIMD&amp;FP register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

## A1

(FEAT\_FP16)

<!-- image -->

## Encoding for the From general-purpose register variant

```
Applies when (op == 0) VMOV{<c>}{<q>}.F16 <Sn>,
```

```
<Rt>
```

## Encoding for the To general-purpose register variant

```
Applies when (op == 1) VMOV{<c>}{<q>}.F16 <Rt>,
```

```
<Sn>
```

## Decode for all variants of this encoding

```
UNDEFINED;
```

```
if !IsFeatureImplemented(FEAT_FP16) then if cond != '1110' then UNPREDICTABLE; constant boolean to_arm_register = (op == '1'); constant integer t = UInt(Rt); constant integer n = UInt(Vn:N); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If cond != '1110' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

```
T1 (FEAT_FP16)
```

<!-- image -->

## Encoding for the From general-purpose register variant

```
Applies when (op == 0) VMOV{<c>}{<q>}.F16 <Sn>,
```

```
<Rt>
```

## Encoding for the To general-purpose register variant

Applies when

```
(op == 1) VMOV{<c>}{<q>}.F16 <Rt>,
```

```
<Sn>
```

## Decode for all variants of this encoding

```
UNDEFINED;
```

```
if !IsFeatureImplemented(FEAT_FP16) then if InITBlock() then UNPREDICTABLE; constant boolean to_arm_register = (op == '1'); constant integer t = UInt(Rt); constant integer n = UInt(Vn:N); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If InITBlock() , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as if it passes the Condition code check.
- The instruction executes as NOP. This means it behaves as if it fails the Condition code check.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

```
<c> See Standard assembler syntax fields. <q> See Standard assembler syntax fields. <Sn> Is the 32-bit name of the SIMD&FP register to be transferred, encoded in the 'Vn:N' field. <Rt>
```

Is the general-purpose register that &lt;Sn&gt; will be transferred to or from, encoded in the 'Rt' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); if to_arm_register then R[t] = Zeros(16) : else S[n] = Zeros(16) :
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.

```
S[n]<15:0>; R[t]<15:0>;
```