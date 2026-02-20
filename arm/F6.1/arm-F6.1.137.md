## F6.1.137 VMOV (between general-purpose register and single-precision)

Copy a general-purpose register to or from a 32-bit SIMD&amp;FP register. This instruction transfers the value held in a 32-bit SIMD&amp;FP register to a general-purpose register, or the value held in a general-purpose register to a 32-bit SIMD&amp;FP register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the From general-purpose register variant

```
Applies when (op == 0) VMOV{<c>}{<q>}
```

```
<Sn>, <Rt>
```

## Encoding for the To general-purpose register variant

```
Applies when (op == 1) VMOV{<c>}{<q>} <Rt>, <Sn>
```

## Decode for all variants of this encoding

```
== '1');
```

```
constant boolean to_arm_register = (op constant integer t = UInt(Rt); constant integer n = UInt(Vn:N); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

T1

<!-- image -->

## Encoding for the From general-purpose register variant

```
Applies when (op == 0) VMOV{<c>}{<q>}
```

```
<Sn>, <Rt>
```

## Encoding for the To general-purpose register variant

```
Applies when (op == 1) VMOV{<c>}{<q>} <Rt>, <Sn>
```

## Decode for all variants of this encoding

```
== '1');
```

```
constant boolean to_arm_register = (op constant integer t = UInt(Rt); constant integer n = UInt(Vn:N); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the 32-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'Vn:N' field.

&lt;q&gt;

&lt;Sn&gt;

&lt;Rt&gt;

Is the general-purpose register that &lt;Sn&gt; will be transferred to or from, encoded in the 'Rt' field.

## Operation

```
EncodingSpecificOperations();
```

```
if ConditionPassed() then CheckVFPEnabled(TRUE); if to_arm_register then R[t] = S[n]; else S[n] = R[t];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.