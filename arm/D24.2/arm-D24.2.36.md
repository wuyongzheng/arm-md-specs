## D24.2.36 CPACR\_EL1, Architectural Feature Access Control Register

The CPACR\_EL1 characteristics are:

## Purpose

Controls access to trace, SME, Streaming SVE, SVE, and Advanced SIMD and floating-point functionality.

## Configuration

AArch64 System register CPACR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register CPACR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CPACR\_EL1 are UNDEFINED.

## Attributes

CPACR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

## When FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TAM, bit [30]

## When FEAT\_AMUv1 is implemented and FEAT\_NV2p1 is implemented:

Reserved for software use in nested virtualization.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0POE, bit [29]

## When FEAT\_S1POE is implemented:

Enable access to POR\_EL0.

Traps EL0 accesses to POR\_EL0, from AArch64 state only to EL1, or to EL2 when it is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1. The exception is reported using EC syndrome value 0x18 .

| E0POE   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0     | This control causes EL0 access to POR_EL0 to be trapped.    |
| 0b1     | This control does not cause any instructions to be trapped. |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field has no effect on execution at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTA, bit [28]

## When System register access to the trace unit registers is implemented:

Traps EL0 and EL1 System register accesses to all implemented trace registers from both Execution states to EL1, or to EL2 when it is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, accesses to trace registers are trapped, reported using EC syndrome value 0x18 .
- In AArch32 state, MRC and MCR accesses to trace registers are trapped, reported using EC syndrome value 0x05 .
- In AArch32 state, MRRC and MCRR accesses to trace registers are trapped, reported using EC syndrome value 0x0C .

| TTA   | Meaning                                                                                                    |
|-------|------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                |
| 0b1   | This control causes EL0 and EL1 System register accesses to all implemented trace registers to be trapped. |

## Note

- The ETMv4 architecture and ETE do not permit EL0 to access the trace registers. If the trace unit implements FEAT\_ETMv4 or FEAT\_ETE, EL0 accesses to the trace registers are UNDEFINED, and any resulting exception is higher priority than an exception that would be generated because the value of CPACR\_EL1.TTA is 1.
- The Arm architecture does not provide traps on trace register accesses through the optional memorymapped interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, any side-effects that are normally associated with the access do not occur before the exception is taken.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field has no effect on execution at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [27:26]

Reserved, RES0.

## SMEN, bits [25:24]

## When FEAT\_SME is implemented:

Traps execution at EL1 and EL0 of SME instructions, SVE instructions when FEAT\_SVE is not implemented or the PE is in Streaming SVE mode, and instructions that directly access the SVCR or SMCR\_EL1 System registers to EL1, or to EL2 when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1.

When instructions that directly access the SVCR System register are trapped with reference to this control, the MSR SVCRSM , MSR SVCRZA , and MSR SVCRSMZA instructions are also trapped.

The exception is reported using EC syndrome value 0x1D , with an ISS code of 0x0000000 .

This field does not affect whether Streaming SVE or SME register values are valid.

Atrap taken as a result of CPACR\_EL1.SMEN has precedence over a trap taken as a result of CPACR\_EL1.FPEN.

| SMEN   | Meaning                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | This control causes execution of these instructions at EL1 and EL0 to be trapped.                                                                |
| 0b01   | This control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL1 to be trapped. |
| 0b10   | This control causes execution of these instructions at EL1 and EL0 to be trapped.                                                                |
| 0b11   | This control does not cause execution of any instructions to be trapped.                                                                         |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field has no effect on execution at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [23:22]

Reserved, RES0.

## FPEN, bits [21:20]

Traps execution at EL1 and EL0 of instructions that access the Advanced SIMD and floating-point registers from both Execution states to EL1, reported using EC syndrome value 0x07 , or to EL2 reported using EC syndrome value 0x00 when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1, as follows:

- In AArch64 state, accesses to FPMR, FPCR, FPSR, and any of the SIMD and floating-point registers V0-V31, including their views as D0-D31 registers or S0-31 registers.

- In AArch32 state, FPSCR, and any of the SIMD and floating-point registers Q0-15, including their views as D0-D31 registers or S0-31 registers.

Traps execution at EL1 and EL0 of SME and SVE instructions to EL1, or to EL2 when EL2 is implemented and enabled for the current Security state and HCR\_EL2.TGE is 1. The exception is reported using EC syndrome value 0x07 .

Atrap taken as a result of CPACR\_EL1.SMEN has precedence over a trap taken as a result of CPACR\_EL1.FPEN.

Atrap taken as a result of CPACR\_EL1.ZEN has precedence over a trap taken as a result of CPACR\_EL1.FPEN.

| FPEN   | Meaning                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | This control causes execution of these instructions at EL1 and EL0 to be trapped.                                                                |
| 0b01   | This control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL1 to be trapped. |
| 0b10   | This control causes execution of these instructions at EL1 and EL0 to be trapped.                                                                |
| 0b11   | This control does not cause execution of any instructions to be trapped.                                                                         |

Writes to MVFR0, MVFR1, and MVFR2 from EL1 or higher are CONSTRAINED UNPREDICTABLE and whether these accesses can be trapped by this control depends on implemented CONSTRAINED UNPREDICTABLE behavior.

## Note

- Attempts to write to the FPSID count as use of the registers for accesses from EL1 or higher.
- Accesses from EL0 to FPSID, MVFR0, MVFR1, MVFR2, and FPEXC are UNDEFINED, and any resulting exception is higher priority than an exception that would be generated because the value of CPACR\_EL1.FPEN is not 0b11 .

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field has no effect on execution at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:18]

Reserved, RES0.

## ZEN, bits [17:16]

## When FEAT\_SVE is implemented:

Traps execution at EL1 and EL0 of SVE instructions when the PE is not in Streaming SVE mode, and instructions that directly access the ZCR\_EL1 System register to EL1, or to EL2 when EL2 is implemented and enabled in the current Security state and HCR\_EL2.TGE is 1.

The exception is reported using EC syndrome value 0x19 .

Atrap taken as a result of CPACR\_EL1.ZEN has precedence over a trap taken as a result of CPACR\_EL1.FPEN.

| ZEN   | Meaning                                                                           |
|-------|-----------------------------------------------------------------------------------|
| 0b00  | This control causes execution of these instructions at EL1 and EL0 to be trapped. |

| ZEN   | Meaning                                                                                                                                          |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b01  | This control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL1 to be trapped. |
| 0b10  | This control causes execution of these instructions at EL1 and EL0 to be trapped.                                                                |
| 0b11  | This control does not cause execution of any instructions to be trapped.                                                                         |

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, this field has no effect on execution at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:0]

Reserved, RES0.

## Accessing CPACR\_EL1

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL3 using the accessor name CPACR\_EL1 or CPACR\_EL12 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to CPACR\_EL1 are masked by CPACRMASK\_EL1.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CPACR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.CPACR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x100]; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then
```

```
UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = CPTR_EL2; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CPACR_EL1;
```

MSR CPACR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGWTR_EL2.CPACR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x100] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then CPACR_EL1 = (X[t, 64] AND NOT EffectiveCPACRMASK_EL1()) OR (CPACR_EL1 AND ↪ → EffectiveCPACRMASK_EL1()); else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then CPTR_EL2 = (X[t, 64] AND NOT EffectiveCPTRMASK_EL2()) OR (CPTR_EL2 AND ↪ → EffectiveCPTRMASK_EL2()); else CPTR_EL2 = X[t, 64]; else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then
```

```
CPACR_EL1 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CPACR\_EL12

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then X[t, 64] = NVMem[0x100]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CPACR_EL1; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then X[t, 64] = CPACR_EL1; else UNDEFINED;
```

When FEAT\_VHE is implemented MSR CPACR\_EL12, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b101 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() == '101' then NVMem[0x100] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then
```

```
if ELIsInHost(EL2) then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else CPACR_EL1 = X[t, 64]; else UNDEFINED; elsif PSTATE.EL == EL3 then if ELIsInHost(EL2) then CPACR_EL1 = X[t, 64]; else UNDEFINED;
```

When FEAT\_SRMASK is implemented MRS &lt;Xt&gt;, CPACRALIAS\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGRTR2_EL2.nCPACRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x100]; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = CPTR_EL2; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CPACR_EL1;
```

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0100 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT2) && ((HaveEL(EL3) && SCR_EL3.FGTEn2 == ↪ → '0') || HFGWTR2_EL2.nCPACRALIAS_EL1 == '0') then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x100] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then CPACR_EL1 = (X[t, 64] AND NOT EffectiveCPACRMASK_EL1()) OR (CPACR_EL1 AND ↪ → EffectiveCPACRMASK_EL1()); else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then CPTR_EL2 = (X[t, 64] AND NOT EffectiveCPTRMASK_EL2()) OR (CPTR_EL2 AND ↪ → EffectiveCPTRMASK_EL2()); else CPTR_EL2 = X[t, 64]; else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CPACR_EL1 = X[t, 64];
```