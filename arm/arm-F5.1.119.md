## F5.1.119 MRS (Banked register)

Move Banked or Special register to general-purpose register

Move to Register from Banked or Special register moves the value from the Banked general-purpose register or Saved Program Status Registers (SPSRs) of the specified mode, or the value of ELR\_hyp, to a general-purpose register.

MRS (Banked register) is UNPREDICTABLE if executed in User mode.

When EL3 is using AArch64, if an MRS (Banked register) instruction that is executed in a Secure EL1 mode would access SPSR\_mon, SP\_mon, or LR\_mon, it is trapped to EL3.

The effect of using an MRS (Banked register) instruction with a register argument that is not valid for the current mode is UNPREDICTABLE. For more information see Usage restrictions on the Banked register transfer instructions.

It has encodings from the following instruction sets: A32 (A1) and T32 (T1).

A1

<!-- image -->

## Encoding

```
MRS{<c>}{<q>} <Rd>, <banked_reg>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean read_spsr = (R == if d == 15 then UNPREDICTABLE; constant bits(5) SYSm = M:M1;
```

T1

<!-- image -->

## Encoding

```
MRS{<c>}{<q>} <Rd>, <banked_reg>
```

## Decode for this encoding

```
constant integer d = UInt(Rd); constant boolean read_spsr = (R == '1'); // Armv8-A removes UNPREDICTABLE for R13 if d == 15 then UNPREDICTABLE; constant bits(5) SYSm = M:M1;
```

For more information about the CONSTRAINED UNPREDICTABLE behavior of this instruction, see Architectural Constraints on UNPREDICTABLE behaviors.

```
'1');
```

## Assembler Symbols

<!-- image -->

See Standard assembler syntax fields.

See Standard assembler syntax fields.

<!-- image -->

## &lt;Rd&gt;

Is the general-purpose destination register, encoded in the 'Rd' field.

## &lt;banked\_reg&gt;

Is the name of the banked register to be transferred to or from, encoded in 'R:M:M1':

|   R |   M | M1   | <banked_reg>   |
|-----|-----|------|----------------|
|   0 |   0 | 0000 | R8_usr         |
|   0 |   0 | 0001 | R9_usr         |
|   0 |   0 | 0010 | R10_usr        |
|   0 |   0 | 0011 | R11_usr        |
|   0 |   0 | 0100 | R12_usr        |
|   0 |   0 | 0101 | SP_usr         |
|   0 |   0 | 0110 | LR_usr         |
|   0 |   0 | 0111 | UNPREDICTABLE  |
|   0 |   0 | 1000 | R8_fiq         |
|   0 |   0 | 1001 | R9_fiq         |
|   0 |   0 | 1010 | R10_fiq        |
|   0 |   0 | 1011 | R11_fiq        |
|   0 |   0 | 1100 | R12_fiq        |
|   0 |   0 | 1101 | SP_fiq         |
|   0 |   0 | 1110 | LR_fiq         |
|   0 |   0 | 1111 | UNPREDICTABLE  |
|   0 |   1 | 0000 | LR_irq         |
|   0 |   1 | 0001 | SP_irq         |
|   0 |   1 | 0010 | LR_svc         |
|   0 |   1 | 0011 | SP_svc         |
|   0 |   1 | 0100 | LR_abt         |
|   0 |   1 | 0101 | SP_abt         |
|   0 |   1 | 0110 | LR_und         |
|   0 |   1 | 0111 | SP_und         |
|   0 |   1 | 10xx | UNPREDICTABLE  |
|   0 |   1 | 1100 | LR_mon         |
|   0 |   1 | 1101 | SP_mon         |

|   R |   M | M1   | <banked_reg>   |
|-----|-----|------|----------------|
|   0 |   1 | 1110 | ELR_hyp        |
|   0 |   1 | 1111 | SP_hyp         |
|   1 |   0 | 0xxx | UNPREDICTABLE  |
|   1 |   0 | 10xx | UNPREDICTABLE  |
|   1 |   0 | 110x | UNPREDICTABLE  |
|   1 |   0 | 1110 | SPSR_fiq       |
|   1 |   0 | 1111 | UNPREDICTABLE  |
|   1 |   1 | 0000 | SPSR_irq       |
|   1 |   1 | 0001 | UNPREDICTABLE  |
|   1 |   1 | 0010 | SPSR_svc       |
|   1 |   1 | 0011 | UNPREDICTABLE  |
|   1 |   1 | 0100 | SPSR_abt       |
|   1 |   1 | 0101 | UNPREDICTABLE  |
|   1 |   1 | 0110 | SPSR_und       |
|   1 |   1 | 0111 | UNPREDICTABLE  |
|   1 |   1 | 10xx | UNPREDICTABLE  |
|   1 |   1 | 1100 | SPSR_mon       |
|   1 |   1 | 1101 | UNPREDICTABLE  |
|   1 |   1 | 1110 | SPSR_hyp       |
|   1 |   1 | 1111 | UNPREDICTABLE  |

## Operation

```
if ConditionPassed() then EncodingSpecificOperations(); if PSTATE.EL == EL0 then constant Constraint c = ConstrainUnpredictable(Unpredictable_BankedRegister); case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); when Constraint_UNKNOWN R[d] = bits(32) UNKNOWN; else constant bits(5) mode = PSTATE.M; if read_spsr then // Check for CONSTRAINED UNPREDICTABLE cases boolean valid; Constraint c = Constraint_NONE; (valid, c) = SPSRaccessValid(SYSm, mode); if valid then case SYSm of when '01110' R[d] = SPSR_fiq<31:0>; when '10000' R[d] = SPSR_irq<31:0>; when '10010' R[d] = SPSR_svc<31:0>; when '10100' R[d] = SPSR_abt<31:0>; when '10110' R[d] = SPSR_und<31:0>; when '11100' if !ELUsingAArch32(EL3) then AArch64.MonitorModeTrap(); R[d] = SPSR_mon;
```

```
when '11110' R[d] = SPSR_hyp<31:0>; else case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); when Constraint_UNKNOWN R[d] = bits(32) UNKNOWN; when Constraint_ANYREG R[d] = ReadAnyAllocatedSPSR(); else // Check for CONSTRAINED UNPREDICTABLE cases boolean valid; Constraint c = Constraint_NONE; (valid, c) = BankedRegisterAccessValid(SYSm, mode); if valid then case SYSm of when '00xxx' // Access the User mode registers constant integer m = UInt(SYSm<2:0>) + 8; R[d] = Rmode[m,M32_User]; when '01xxx' // Access the FIQ mode registers constant integer m = UInt(SYSm<2:0>) + 8; R[d] = Rmode[m,M32_FIQ]; when '1000x' // Access the IRQ mode registers // LR when SYSm<0> == 0, otherwise SP constant integer m = 14 -UInt(SYSm<0>); R[d] = Rmode[m,M32_IRQ]; when '1001x' // Access the Supervisor mode registers // LR when SYSm<0> == 0, otherwise SP constant integer m = 14 -UInt(SYSm<0>); R[d] = Rmode[m,M32_Svc]; when '1010x' // Access the Abort mode registers // LR when SYSm<0> == 0, otherwise SP constant integer m = 14 -UInt(SYSm<0>); R[d] = Rmode[m,M32_Abort]; when '1011x' // Access the Undefined mode registers // LR when SYSm<0> == 0, otherwise SP constant integer m = 14 -UInt(SYSm<0>); R[d] = Rmode[m,M32_Undef]; when '1110x' // Access Monitor registers if !ELUsingAArch32(EL3) then AArch64.MonitorModeTrap(); // LR when SYSm<0> == 0, otherwise SP constant integer m = 14 -UInt(SYSm<0>); R[d] = Rmode[m,M32_Monitor]; when '11110' // Access ELR_hyp register R[d] = ELR_hyp; when '11111' // Access SP_hyp register R[d] = Rmode[13,M32_Hyp]; else case c of when Constraint_UNDEF UNDEFINED; when Constraint_NOP ExecuteAsNOP(); when Constraint_UNKNOWN R[d] = bits(32) UNKNOWN; when Constraint_ANYREG R[d] = ReadAnyAllocatedRegister();
```

## CONSTRAINED UNPREDICTABLE behavior

If PSTATE.EL == EL0 , then one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction executes as NOP .