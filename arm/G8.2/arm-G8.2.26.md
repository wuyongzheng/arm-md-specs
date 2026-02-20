## G8.2.26 CFPRCTX, Control Flow Prediction Restriction by Context

The CFPRCTX characteristics are:

## Purpose

Control Flow Prediction Restriction by Context applies to all Control Flow Prediction Resources that predict execution based on information gathered within the target execution context or contexts.

Control flow predictions determined by the actions of code in the target execution context or contexts appearing in program order before the instruction cannot exploitatively control speculative execution occurring after the instruction is complete and synchronized.

This instruction is guaranteed to be complete following a DSB that covers both read and write behavior on the same PE as executed the original restriction instruction, and a subsequent context synchronization event is required to ensure that the effect of the completion of the instructions is synchronized to the current execution.

Note

This instruction does not require the invalidation of prediction structures so long as the behavior described for completion of this instruction is met by the implementation.

Onsomeimplementations the instruction is likely to take a significant number of cycles to execute. This instruction is expected to be used very rarely, such as on the roll-over of an ASID or VMID, but should not be used on every context switch.

## Configuration

This system instruction is present only when FEAT\_AA32 is implemented and FEAT\_SPECRES is implemented. Otherwise, direct accesses to CFPRCTX are UNDEFINED.

## Attributes

CFPRCTX is a 32-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [31:28]

Reserved, RES0.

## GVMID, bit [27]

Execution of this instruction applies to all VMIDs or a specified VMID.

| GVMID   | Meaning                                                              |
|---------|----------------------------------------------------------------------|
| 0b0     | Applies to specified VMIDfor an EL0 or EL1 target execution context. |
| 0b1     | Applies to all VMIDs for an EL0 or EL1 target execution context.     |

For target execution contexts other than EL0 or EL1, this field is RES0.

If the instruction is executed at EL0 or EL1, this field has an Effective value of 0.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## NS, bit [26]

Security State.

| NS   | Meaning           |
|------|-------------------|
| 0b0  | Secure state.     |
| 0b1  | Non-secure state. |

If the instruction is executed in Non-secure state, this field has an Effective value of 1.

## EL, bits [25:24]

Exception Level. Indicates the Exception level of the target execution context.

| EL   | Meaning   | Applies when            |
|------|-----------|-------------------------|
| 0b00 | EL0.      |                         |
| 0b01 | EL1       |                         |
| 0b10 | EL2       | FEAT_EL2 is implemented |
| 0b11 | EL3       | FEAT_EL3 is implemented |

If the instruction is executed at an Exception level lower than the specified level, or is specified to apply to a combination of Exception level and Security state that is not implemented, this instruction is treated as a NOP.

## VMID, bits [23:16]

Only applies when bit[27] is 0 and the target execution context is either:

- EL1.
- EL0 when EL2 is using AArch32 or the Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

Otherwise this field is RES0.

When the instruction is executed at EL1, this field is treated as the current VMID.

When the instruction is executed at EL0, this field is treated as the current VMID if any of the following are true:

- EL2 is using AArch32.
- The Effective value of HCR\_EL2.{E2H, TGE} is not {1, 1}.

When the instruction is executed at EL0 and the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field is ignored.

If EL2 is not implemented or not enabled for the target Security state, this field is RES0.

## Bits [15:9]

Reserved, RES0.

## GASID, bit [8]

Execution of this instruction applies to all ASIDs or a specified ASID.

| GASID   | Meaning                                                        |
|---------|----------------------------------------------------------------|
| 0b0     | Applies to specified ASID for an EL0 target execution context. |
| 0b1     | Applies to all ASIDs for an EL0 target execution context.      |

For target execution contexts other than EL0, this field is RES0.

If the instruction is executed at EL0, this field is treated as 0.

## ASID, bits [7:0]

Only applies for an EL0 target execution context and when bit[8] is 0.

Otherwise, this field is RES0.

When the instruction is executed at EL0, this field is treated as the current ASID.

## Executing CFPRCTX

Accesses to this instruction use the following encodings in the System instruction encoding space:

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0111 | 0b0011 | 0b100  |

```
if !(IsFeatureImplemented(FEAT_AA32) && IsFeatureImplemented(FEAT_SPECRES)) then UNDEFINED; elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1) && !ELIsInHost(EL0) && ↪ → SCTLR_EL1.EnRCTX == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch64.AArch32SystemAccessTrap(EL1, 0x03); elsif IsFeatureImplemented(FEAT_AA32EL1) && ELUsingAArch32(EL1) && SCTLR.EnRCTX == '0' then if EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && HCR_EL2.TGE ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HCR.TGE == ↪ → '1' then AArch32.TakeHypTrapException(0x00); else UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2)) && ↪ → !ELIsInHost(EL0) && HSTR_EL2.T7 == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2)) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && (IsFeatureImplemented(FEAT_AA64EL1) && !ELUsingAArch32(EL1)) && ↪ → !ELIsInHost(EL0) && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGITR_EL2.CFPRCTX == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif ELIsInHost(EL0) && SCTLR_EL2.EnRCTX == '0' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); else AArch32.RestrictPrediction(R[t], RestrictType_ControlFlow);
```

```
elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T7 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T7 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else AArch32.RestrictPrediction(R[t], RestrictType_ControlFlow); elsif PSTATE.EL == EL2 then AArch32.RestrictPrediction(R[t], RestrictType_ControlFlow); elsif PSTATE.EL == EL3 then AArch32.RestrictPrediction(R[t], RestrictType_ControlFlow);
```