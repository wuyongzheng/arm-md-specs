## F6.1.145 VMSR

Move general-purpose register to SIMD&amp;FP Special register moves the value of a general-purpose register to a floating-point System register.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

When these settings permit the execution of Advanced SIMD and floating-point instructions:

- If the specified floating-point System register is FPSID or FPEXC, the instruction is UNDEFINED if executed in User mode.
- If the specified floating-point System register is the FPSID and the instruction is executed in a mode other than User mode, the instruction is ignored.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMSR{<c>}{<q>} <spec_reg>, <Rt>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); if reg != '000x' && reg != '1000' then constant Constraint c = ConstrainUnpredictable(Unpredictable_VMSR); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If reg != '000x' &amp;&amp; reg != '1000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction transfers the value in the general-purpose register to one of the allocated registers accessible using VMSR at the same Exception level.

T1

<!-- image -->

## Encoding

```
VMSR{<c>}{<q>} <spec_reg>, <Rt>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); if reg != '000x' && reg != '1000' then constant Constraint c = ConstrainUnpredictable(Unpredictable_VMSR); assert c IN {Constraint_UNDEF, Constraint_NOP}; case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); // Armv8-A removes UNPREDICTABLE for R13 if t == 15 then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If reg != '000x' &amp;&amp; reg != '1000' , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction transfers the value in the general-purpose register to one of the allocated registers accessible using VMSR at the same Exception level.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

<!-- image -->

See Standard assembler syntax fields.

## &lt;spec\_reg&gt;

Is the destination Advanced SIMD and floating-point System register, encoded in 'reg':

|   reg | <spec_reg>   |
|-------|--------------|
|  0000 | FPSID        |
|  0001 | FPSCR        |

## &lt;Rt&gt;

| reg   | <spec_reg>    |
|-------|---------------|
| 001x  | UNPREDICTABLE |
| 01xx  | UNPREDICTABLE |
| 1000  | FPEXC         |
| 1001  | UNPREDICTABLE |
| 101x  | UNPREDICTABLE |
| 11xx  | UNPREDICTABLE |

Is the general-purpose source register, encoded in the 'Rt' field.

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if reg == '0001' then // FPSCR CheckVFPEnabled(TRUE); FPSCR = R[t]; elsif PSTATE.EL == EL0 then UNDEFINED; // Non-FPSCR registers accessible only at PL1 or above else CheckVFPEnabled(FALSE); // Non-FPSCR registers are not affected by FPEXC.EN case reg of when '0000' // VMSR access to FPSID is ignored when '1000' FPEXC = R[t]; otherwise Unreachable(); // Dealt with above or in encoding-specific pseudocode
```