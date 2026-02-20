## F6.1.139 VMOV (between two general-purpose registers and two single-precision registers)

Copy two general-purpose registers to a pair of 32-bit SIMD&amp;FP registers transfers the contents of two consecutively numbered single-precision Floating-point registers to two general-purpose registers, or the contents of two general-purpose registers to a pair of single-precision Floating-point registers. The general-purpose registers do not have to be contiguous.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding for the From general-purpose registers variant

```
Applies when (op == 0) VMOV{<c>}{<q>} <Sm>, <Sm1>, <Rt>,
```

```
<Rt2>
```

## Encoding for the To general-purpose registers variant

```
Applies when (op == 1) VMOV{<c>}{<q>} <Rt>, <Rt2>, <Sm>, <Sm1>
```

## Decode for all variants of this encoding

```
UNPREDICTABLE;
```

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer m = UInt(Vm:M); constant integer m2 = m + 1; constant boolean to_arm_registers = (op == '1'); if t == 15 || t2 == 15 || m == 31 then if to_arm_registers && t == t2 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If to\_arm\_registers &amp;&amp; t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

If m == 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the single-precision registers become UNKNOWN for a move to the single-precision register. The general-purpose registers listed in the instruction become UNKNOWN for a move from the single-precision registers. This behavior does not affect any other general-purpose registers.

T1

<!-- image -->

## Encoding for the From general-purpose registers variant

```
Applies when (op == 0) VMOV{<c>}{<q>} <Sm>, <Sm1>, <Rt>, <Rt2>
```

## Encoding for the To general-purpose registers variant

Applies when (op ==

```
1) VMOV{<c>}{<q>} <Rt>, <Rt2>, <Sm>, <Sm1>
```

## Decode for all variants of this encoding

```
UNPREDICTABLE;
```

```
constant integer t = UInt(Rt); constant integer t2 = UInt(Rt2); constant integer m = UInt(Vm:M); constant integer m2 = m + 1; constant boolean to_arm_registers = (op == '1'); if t == 15 || t2 == 15 || m == 31 then if to_arm_registers && t == t2 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If to\_arm\_registers &amp;&amp; t == t2 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The value in the destination register is UNKNOWN.

If m == 31 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- One or more of the single-precision registers become UNKNOWN for a move to the single-precision register. The general-purpose registers listed in the instruction become UNKNOWN for a move from the single-precision registers. This behavior does not affect any other general-purpose registers.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors, and particularly VMOV (between two general-purpose registers and two single-precision registers).

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

&lt;q&gt;

See Standard assembler syntax fields.

## &lt;Sm&gt;

Is the 32-bit name of the first SIMD&amp;FP register to be transferred, encoded in the 'Vm:M' field.

## &lt;Sm1&gt;

Is the 32-bit name of the second SIMD&amp;FP register to be transferred. This is the next SIMD&amp;FP register after &lt;Sm&gt; .

## &lt;Rt&gt;

Is the first general-purpose register that &lt;Sm&gt; will be transferred to or from, encoded in the 'Rt' field.

## &lt;Rt2&gt;

Is the second general-purpose register that &lt;Sm1&gt; will be transferred to or from, encoded in the 'Rt2' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations();
```

```
CheckVFPEnabled(TRUE); if to_arm_registers then R[t] = S[m]; R[t2] = S[m2]; else S[m] = R[t]; S[m2] = R[t2];
```

## Operational Information

This instruction is a data-independent-time instruction as described in About the DIT bit.