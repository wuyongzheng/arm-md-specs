## F6.1.144 VMRS

Move SIMD&amp;FP Special register to general-purpose register moves the value of an Advanced SIMD and floating-point System register to a general-purpose register. When the specified System register is the FPSCR, a form of the instruction transfers the FPSCR.{N, Z, C, V} condition flags to the APSR.{N, Z, C, V} condition flags.

Depending on settings in the CPACR, NSACR, HCPTR, and FPEXC registers, and the Security state and PE mode in which the instruction is executed, an attempt to execute the instruction might be UNDEFINED, or trapped to Hyp mode. For more information see Enabling Advanced SIMD and floating-point support.

When these settings permit the execution of Advanced SIMD and floating-point instructions, if the specified floating-point System register is not the FPSCR, the instruction is UNDEFINED if executed in User mode.

In an implementation that includes EL2, when HCR.TID0 is set to 1, any VMRS access to FPSID from a Non-secure EL1 mode that would be permitted if HCR.TID0 was set to 0 generates a Hyp Trap exception. For more information, see EL2 configurable controls.

For simplicity, the VMRS pseudocode does not show the possible trap to Hyp mode.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
VMRS{<c>}{<q>} <Rt>, <spec_reg>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); if ! reg IN {'000x', '0101', '011x', '1000'} then // Armv8-A removes UNPREDICTABLE for R13 if t == 15 && reg != '0001' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If ! reg IN {'000x', '0101', '011x', '1000'} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction transfers an UNKNOWN value to the specified target register. When the Rt field holds the value 0b1111 , the specified target register is the APSR.{N, Z, C, V} bits, and these bits become UNKNOWN. Otherwise, the specified target register is the register specified by the Rt field, R0 - R14.

T1

<!-- image -->

## Encoding

```
UNPREDICTABLE;
```

```
VMRS{<c>}{<q>} <Rt>, <spec_reg>
```

## Decode for this encoding

```
constant integer t = UInt(Rt); if ! reg IN {'000x', '0101', '011x', '1000'} then // Armv8-A removes UNPREDICTABLE for R13 if t == 15 && reg != '0001' then UNPREDICTABLE;
```

## CONSTRAINED UNPREDICTABLE behavior

If ! reg IN {'000x', '0101', '011x', '1000'} , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .
- The instruction transfers an UNKNOWN value to the specified target register. When the Rt field holds the value 0b1111 , the specified target register is the APSR.{N, Z, C, V} bits, and these bits become UNKNOWN. Otherwise, the specified target register is the register specified by the Rt field, R0 - R14.

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

## Assembler Symbols

&lt;c&gt;

See Standard assembler syntax fields.

See Standard assembler syntax fields.

Is the general-purpose destination register, encoded in the 'Rt' field. Is one of:

R0-R14 General-purpose register.

APSR\_nzcv Permitted only when &lt;spec\_reg&gt; is FPSCR . Encoded as 0b1111 . The instruction transfers the FPSCR.{N, Z, C, V} condition flags to the APSR.{N, Z, C, V} condition flags.

## &lt;spec\_reg&gt;

Is the source Advanced SIMD and floating-point System register, encoded in 'reg':

| reg   | <spec_reg>    |
|-------|---------------|
| 0000  | FPSID         |
| 0001  | FPSCR         |
| 001x  | UNPREDICTABLE |
| 0100  | UNPREDICTABLE |
| 0101  | MVFR2         |
| 0110  | MVFR1         |
| 0111  | MVFR0         |
| 1000  | FPEXC         |

&lt;q&gt;

## &lt;Rt&gt;

```
UNPREDICTABLE;
```

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if reg == '0001' then // FPSCR CheckVFPEnabled(TRUE); if t == 15 then PSTATE.<N,Z,C,V> = FPSR.<N,Z,C,V>; else R[t] = FPSCR; elsif PSTATE.EL == EL0 then UNDEFINED; // Non-FPSCR registers accessible only at PL1 or above else CheckVFPEnabled(FALSE); // Non-FPSCR registers are not affected by FPEXC.EN AArch32.CheckAdvSIMDOrFPRegisterTraps(reg); case reg of when '0000' R[t] = FPSID; when '0101' R[t] = MVFR2; when '0110' R[t] = MVFR1; when '0111' R[t] = MVFR0; when '1000' R[t] = FPEXC; otherwise Unreachable(); // Dealt with above or in encoding-specific pseudocode
```

| reg   | <spec_reg>    |
|-------|---------------|
| 1001  | UNPREDICTABLE |
| 101x  | UNPREDICTABLE |
| 11xx  | UNPREDICTABLE |