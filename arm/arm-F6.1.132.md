## F6.1.132 VMOV (between two general-purpose registers and a doubleword floating-point register)

Copy two general-purpose registers to or from a SIMD&amp;FP register copies two words from two general-purpose registers into a doubleword register in the Advanced SIMD and floating-point register file, or from a doubleword register in the Advanced SIMD and floating-point register file to two general-purpose registers.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the From general-purpose registers variant

Applies when

```
<Dm>, <Rt>, <Rt2>
```

```
(op == 0) VMOV{<c>}{<q>}
```

## Encoding for the To general-purpose registers variant

```
Applies when (op == 1) VMOV{<c>}{<q>} <Rt>, <Rt2>, <Dm>
```

## Decode for all variants of this encoding

```
constant boolean to_arm_registers = (op == '1'); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer m = UInt(M:Vm); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 then UNPREDICTABLE; if to_arm_registers && t == t2 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If to\_arm\_registers &amp;&amp; t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

T1

<!-- image -->

## Encoding for the From general-purpose registers variant

```
Applies when (op == 0) VMOV{<c>}{<q>}
```

```
<Dm>, <Rt>, <Rt2>
```

## Encoding for the To general-purpose registers variant

Applies when (op ==

```
1) VMOV{<c>}{<q>} <Rt>, <Rt2>, <Dm>
```

## Decode for all variants of this encoding

```
constant boolean to_arm_registers = (op == '1'); constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer m = UInt(M:Vm); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 || t2 == 15 then UNPREDICTABLE; if to_arm_registers && t == t2 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If to\_arm\_registers &amp;&amp; t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VMOV (between two general-purpose registers and a doubleword floating-point register).

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Dm&gt;

Is the 64-bit name of the SIMD&amp;FP register to be transferred, encoded in the 'M:Vm' field.

## &lt;Rt&gt;

Is the first general-purpose register that &lt;Dm&gt; [31:0] will be transferred to or from, encoded in the 'Rt' field.

## &lt;Rt2&gt;

Is the second general-purpose register that &lt;Dm&gt; [63:32] will be transferred to or from, encoded in the 'Rt2' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); CheckVFPEnabled(TRUE); if to_arm_registers then R[t] = D[m]<31:0>; R[t2] = D[m]<63:32>; else D[m]<31:0> = R[t]; D[m]<63:32> = R[t2];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.