## D24.2.38 CPTR\_EL2, Architectural Feature Trap Register (EL2)

The CPTR\_EL2 characteristics are:

## Purpose

Controls trapping to EL2 of accesses to CPACR, CPACR\_EL1, trace, Activity Monitor, SME, Streaming SVE, SVE, and Advanced SIMD and floating-point functionality.

## Configuration

If EL2 is not implemented, this register is RES0 from EL3.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register CPTR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register HCPTR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to CPTR\_EL2 are UNDEFINED.

## Attributes

CPTR\_EL2 is a 64-bit register.

## Field descriptions

When ELIsInHost(EL2):

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

In AArch64 state, traps accesses to CPACR\_EL1 from EL1 to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x18 .

In AArch32 state, traps accesses to CPACR from EL1 to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x03 .

| TCPAC   | Meaning                                                                                                    |
|---------|------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                |
| 0b1     | EL1 accesses to CPACR_EL1 and CPACR are trapped to EL2, when EL2 is enabled in the current Security state. |

When the Effective value of HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

Note

CPACR\_EL1 and CPACR are not accessible at EL0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TAM, bit [30]

## When FEAT\_AMUv1 is implemented:

Trap Activity Monitor access. Traps EL1 and EL0 accesses to all Activity Monitor registers to EL2, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x18 :
- AMUSERENR\_EL0, AMCFGR\_EL0, AMCGCR\_EL0, AMCNTENCLR0\_EL0, AMCNTENCLR1\_EL0, AMCNTENSET0\_EL0, AMCNTENSET1\_EL0, AMCR\_EL0, AMEVCNTR0&lt;n&gt;\_EL0, AMEVCNTR1&lt;n&gt;\_EL0, AMEVTYPER0&lt;n&gt;\_EL0, and AMEVTYPER1&lt;n&gt;\_EL0.
- In AArch32 state, MRC or MCR accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 :
- AMUSERENR, AMCFGR, AMCGCR, AMCNTENCLR0, AMCNTENCLR1, AMCNTENSET0, AMCNTENSET1, AMCR, AMEVTYPER0&lt;n&gt;, and AMEVTYPER1&lt;n&gt;.
- In AArch32 state, MRRC or MCRR accesses to AMEVCNTR0&lt;n&gt; and AMEVCNTR1&lt;n&gt;, are trapped to EL2, reported using EC syndrome value 0x04 .

| TAM   | Meaning                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses from EL1 and EL0 to Activity Monitor registers are not trapped.                                                       |
| 0b1   | Accesses from EL1 and EL0 to Activity Monitor registers are trapped to EL2, when EL2 is enabled in the current Security state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## E0POE, bit [29]

## When FEAT\_S1POE is implemented:

Enable access to POR\_EL0.

Traps EL0 accesses to POR\_EL0 to EL2, from AArch64 state only. The exception is reported using EC syndrome value 0x18 .

| E0POE   | Meaning                                                     |
|---------|-------------------------------------------------------------|
| 0b0     | This control causes EL0 access to POR_EL0 to be trapped.    |
| 0b1     | This control does not cause any instructions to be trapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## TTA, bit [28]

## When System register access to the trace unit registers is implemented:

Traps System register accesses to all implemented trace registers from both Execution states to EL2, when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to trace registers with op0=2, op1=1, and CRn&lt; 0b1000 are trapped to EL2, reported using EC syndrome value 0x18 .
- In AArch32 state, MRC or MCR accesses to trace registers with cpnum=14, opc1=1, and CRn&lt; 0b1000 are trapped to EL2, reported using EC syndrome value 0x05 .

| TTA   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                                                                                                                                                                                                          |
| 0b1   | Any attempt at EL0, EL1 or EL2, to execute a System register access to an implemented trace register is trapped to EL2, when EL2 is enabled in the current Security state, unless HCR_EL2.TGE is 0 and it is trapped by CPACR.NSTRCDIS or CPACR_EL1.TTA. When HCR_EL2.TGE is 1, any attempt at EL0 or EL2 to execute a System register access to an implemented trace register is trapped to EL2, when EL2 is enabled in the current Security state. |

## Note

The ETMv4 architecture and ETE do not permit EL0 to access the trace registers. If the trace unit implements FEAT\_ETMv4 or ETE, EL0 accesses to the trace registers are UNDEFINED, and any resulting exception is higher priority than an exception that would be generated because the value of CPTR\_EL2.TTA is 1. EL2 does not provide traps on trace register accesses through the optional Memory-mapped interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, any side-effects that are normally associated with the access do not occur before the exception is taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [27:26]

Reserved, RES0.

SMEN, bits [25:24]

## When FEAT\_SME is implemented:

Traps execution at EL2, EL1, and EL0 of SME instructions, SVE instructions when FEAT\_SVE is not implemented or the PE is in Streaming SVE mode, and instructions that directly access the SVCR, SMCR\_EL1, or SMCR\_EL2 System registers to EL2, when EL2 is enabled in the current Security state.

When instructions that directly access the SVCR System register are trapped with reference to this control, the MSR SVCRSM , MSR SVCRZA , and MSR SVCRSMZA instructions are also trapped.

The exception is reported using EC syndrome value 0x1D , with an ISS code of 0x0000000 .

This field does not affect whether Streaming SVE or SME register values are valid.

Atrap taken as a result of CPTR\_EL2.SMEN has precedence over a trap taken as a result of CPTR\_EL2.FPEN.

| SMEN   | Meaning                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped.                                                                                                                                                                                 |
| 0b01   | When HCR_EL2.TGE is 0, this control does not cause execution of any instructions to be trapped. When HCR_EL2.TGE is 1, this control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL2 to be trapped. |
| 0b10   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped.                                                                                                                                                                                 |
| 0b11   | This control does not cause execution of any instructions to be trapped.                                                                                                                                                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [23:22]

Reserved, RES0.

## FPEN, bits [21:20]

Traps execution at EL2, EL1, and EL0 of instructions that access the Advanced SIMD and floating-point registers from both Execution states to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x07 .

Traps execution at EL2, EL1, and EL0 of SME and SVE instructions to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x07 .

When FEAT\_FPMR is implemented, traps execution at EL2, EL1, and EL0 of instructions that access FPMR to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x07

Atrap taken as a result of CPTR\_EL2.SMEN has precedence over a trap taken as a result of CPTR\_EL2.FPEN.

Atrap taken as a result of CPTR\_EL2.ZEN has precedence over a trap taken as a result of CPTR\_EL2.FPEN.

| FPEN   | Meaning                                                                                 |
|--------|-----------------------------------------------------------------------------------------|
| 0b00   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped. |

| FPEN   | Meaning                                                                                                                                                                                                                                                                 |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b01   | When HCR_EL2.TGE is 0, this control does not cause execution of any instructions to be trapped. When HCR_EL2.TGE is 1, this control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL2 to be trapped. |
| 0b10   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped.                                                                                                                                                                                 |
| 0b11   | This control does not cause execution of any instructions to be trapped.                                                                                                                                                                                                |

Writes to MVFR0, MVFR1, and MVFR2 from EL1 or higher are CONSTRAINED UNPREDICTABLE and whether these accesses can be trapped by this control depends on implemented CONSTRAINED UNPREDICTABLE behavior.

## Note

- Attempts to write to the FPSID count as use of the registers for accesses from EL1 or higher.
- Accesses from EL0 to FPSID, MVFR0, MVFR1, MVFR2, and FPEXC are UNDEFINED, and any resulting exception is higher priority than an exception that would be generated because the value of CPTR\_EL2.FPEN is not 0b11 .

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [19:18]

Reserved, RES0.

## ZEN, bits [17:16]

## When FEAT\_SVE is implemented:

Traps execution at EL2, EL1, and EL0 of SVE instructions when the PE is not in Streaming SVE mode, and instructions that directly access the ZCR\_EL1 or ZCR\_EL2 System registers to EL2, when EL2 is enabled in the current Security state.

The exception is reported using EC syndrome value 0x19 .

Atrap taken as a result of CPTR\_EL2.ZEN has precedence over a trap taken as a result of CPTR\_EL2.FPEN.

| ZEN   | Meaning                                                                                                                                                                                                                                                                 |
|-------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00  | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped.                                                                                                                                                                                 |
| 0b01  | When HCR_EL2.TGE is 0, this control does not cause execution of any instructions to be trapped. When HCR_EL2.TGE is 1, this control causes execution of these instructions at EL0 to be trapped, but does not cause execution of any instructions at EL2 to be trapped. |
| 0b10  | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped.                                                                                                                                                                                 |
| 0b11  | This control does not cause execution of any instructions to be trapped.                                                                                                                                                                                                |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [15:0]

Reserved, RES0.

## Otherwise:

<!-- image -->

This format applies in all Armv8.0 implementations.

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

In AArch64 state, traps accesses to CPACR\_EL1 from EL1 to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x18 .

In AArch32 state, traps accesses to CPACR from EL1 to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x03 .

| TCPAC   | Meaning                                                                                                                              |
|---------|--------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                          |
| 0b1     | EL1 accesses to the following registers are trapped to EL2, when EL2 is enabled in the current Security state: • CPACR_EL1. • CPACR. |

When HCR\_EL2.TGE is 1, this control does not cause any instructions to be trapped.

| Note                                           |
|------------------------------------------------|
| CPACR_EL1 and CPACR are not accessible at EL0. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## TAM, bit [30]

## When FEAT\_AMUv1 is implemented:

Trap Activity Monitor access. Traps EL1 and EL0 accesses to all Activity Monitor registers to EL2, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x18 :
- AMUSERENR\_EL0, AMCFGR\_EL0, AMCGCR\_EL0, AMCNTENCLR0\_EL0, AMCNTENCLR1\_EL0, AMCNTENSET0\_EL0, AMCNTENSET1\_EL0, AMCR\_EL0, AMEVCNTR0&lt;n&gt;\_EL0, AMEVCNTR1&lt;n&gt;\_EL0, AMEVTYPER0&lt;n&gt;\_EL0, and AMEVTYPER1&lt;n&gt;\_EL0.

- In AArch32 state, MCR or MRC accesses to the following registers are trapped to EL2 and reported using EC syndrome value 0x03 :
- AMUSERENR, AMCFGR, AMCGCR, AMCNTENCLR0, AMCNTENCLR1, AMCNTENSET0, AMCNTENSET1, AMCR, AMEVTYPER0&lt;n&gt;, and AMEVTYPER1&lt;n&gt;.
- In AArch32 state, MCRR or MRRC accesses to AMEVCNTR0&lt;n&gt; and AMEVCNTR1&lt;n&gt;, are trapped to EL2, reported using EC syndrome value 0x04 .

| TAM   | Meaning                                                                                                                        |
|-------|--------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | Accesses from EL1 and EL0 to Activity Monitor registers are not trapped.                                                       |
| 0b1   | Accesses from EL1 and EL0 to Activity Monitor registers are trapped to EL2, when EL2 is enabled in the current Security state. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [29:21]

Reserved, RES0.

## TTA, bit [20]

## When System register access to the trace unit registers is implemented:

Traps System register accesses to all implemented trace registers from both Execution states to EL2, when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to trace registers with op0=2, op1=1, and CRn&lt; 0b1000 are trapped to EL2, reported using EC syndrome value 0x18 .
- In AArch32 state, MRC or MCR accesses to trace registers with cpnum=14, opc1=1, and CRn&lt; 0b1000 are trapped to EL2, reported using EC syndrome value 0x05 .

| TTA   | Meaning                                                                                                                                                                                                                                                             |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped.                                                                                                                                                                                                         |
| 0b1   | Any attempt at EL0, EL1, or EL2, to execute a System register access to an implemented trace register is trapped to EL2, when EL2 is enabled in the current Security state, unless it is trapped by one of the following controls: • CPACR_EL1.TTA. • CPACR.TRCDIS. |

Note

- FEAT\_ETMv4 and FEAT\_ETE do not permit EL0 to access the trace registers. EL0 accesses to the trace System registers are UNDEFINED, and any resulting exception is higher priority than an exception that would be generated because the value of CPTR\_EL2.TTA is 1.
- EL2 does not provide traps on trace register accesses through the optional memory-mapped interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, any side-effects that are normally associated with the access do not occur before the exception is taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:14]

Reserved, RES0.

## Bit [13]

Reserved, RES1.

## TSM, bit [12]

## When FEAT\_SME is implemented:

Traps execution at EL2, EL1, and EL0 of SME instructions, SVE instructions when FEAT\_SVE is not implemented or the PE is in Streaming SVE mode, and instructions that directly access the SVCR, SMCR\_EL1, or SMCR\_EL2 System registers to EL2, when EL2 is enabled in the current Security state.

When instructions that directly access the SVCR System register are trapped with reference to this control, the MSR SVCRSM , MSR SVCRZA , and MSR SVCRSMZA instructions are also trapped.

The exception is reported using EC syndrome value 0x1D , with an ISS code of 0x0000000 .

This field does not affect whether Streaming SVE or SME register values are valid.

Atrap taken as a result of CPTR\_EL2.TSM has precedence over a trap taken as a result of CPTR\_EL2.TFP.

| TSM   | Meaning                                                                                 |
|-------|-----------------------------------------------------------------------------------------|
| 0b0   | This control does not cause execution of any instructions to be trapped.                |
| 0b1   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

## Bit [11]

Reserved, RES0.

## TFP, bit [10]

Traps execution of instructions which access the Advanced SIMD and floating-point functionality, from both Execution states to EL2, when EL2 is enabled in the current Security state, as follows:

- In AArch64 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x07 :
- FPCR, FPSR, FPEXC32\_EL2, and any of the SIMD and floating-point registers V0-V31, including their views as D0-D31 registers or S0-31 registers.

- If FEAT\_FPMR is implemented, FPMR.
- In AArch32 state, accesses to the following registers are trapped to EL2, reported using EC syndrome value 0x07 :
- MVFR0, MVFR1, MVFR2, FPSCR, FPEXC, and any of the SIMD and floating-point registers Q0-15, including their views as D0-D31 registers or S0-31 registers. For the purposes of this trap, the architecture defines a VMSR access to FPSID from EL1 or higher as an access to a SIMD and floating-point register. Otherwise, permitted VMSR accesses to FPSID are ignored.

Traps execution at the same Exception levels of SME and SVE instructions to EL2, when EL2 is enabled in the current Security state. The exception is reported using EC syndrome value 0x07 .

Atrap taken as a result of CPTR\_EL2.TSM has precedence over a trap taken as a result of CPTR\_EL2.TFP.

Atrap taken as a result of CPTR\_EL2.TZ has precedence over a trap taken as a result of CPTR\_EL2.TFP.

| TFP   | Meaning                                                                                 |
|-------|-----------------------------------------------------------------------------------------|
| 0b0   | This control does not cause execution of any instructions to be trapped.                |
| 0b1   | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped. |

## Note

FPEXC32\_EL2 is not accessible from EL0 using AArch64.

FPSID, MVFR0, MVFR1, and FPEXC are not accessible from EL0 using AArch32.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES1.

## TZ, bit [8]

## When FEAT\_SVE is implemented:

Traps execution at EL2, EL1, and EL0 of SVE instructions when the PE is not in Streaming SVE mode, and instructions that directly access the ZCR\_EL2 or ZCR\_EL1 System registers to EL2, when EL2 is enabled in the current Security state.

The exception is reported using EC syndrome value 0x19 .

Atrap taken as a result of CPTR\_EL2.TZ has precedence over a trap taken as a result of CPTR\_EL2.TFP.

| TZ   | Meaning                                                                                 |
|------|-----------------------------------------------------------------------------------------|
| 0b0  | This control does not cause execution of any instructions to be trapped.                |
| 0b1  | This control causes execution of these instructions at EL2, EL1, and EL0 to be trapped. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES1.

Bits [7:0]

Reserved, RES1.

## Accessing CPTR\_EL2

When the Effective value of HCR\_EL2.E2H is 1, without explicit synchronization, accesses from EL2 using the accessor name CPTR\_EL2 or CPACR\_EL1 are not guaranteed to be ordered with respect to accesses using the other accessor name.

If FEAT\_SRMASK is implemented, accesses to CPTR\_EL2 are masked by CPTRMASK\_EL2.

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CPTR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = CPTR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = CPTR_EL2;
```

MSR CPTR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0001 | 0b0001 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else if IsFeatureImplemented(FEAT_SRMASK) then CPTR_EL2 = (X[t, 64] AND NOT EffectiveCPTRMASK_EL2()) OR (CPTR_EL2 AND ↪ → EffectiveCPTRMASK_EL2()); else CPTR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then CPTR_EL2 = X[t, 64];
```

When FEAT\_VHE is implemented MRS &lt;Xt&gt;, CPACR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGRTR_EL2.CPACR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then X[t, 64] = NVMem[0x100]; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then X[t, 64] = CPTR_EL2; else X[t, 64] = CPACR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = CPACR_EL1;
```

When FEAT\_VHE is implemented MSR CPACR\_EL1, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0001 | 0b0000 | 0b010 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && CPTR_EL2.TCPAC == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') ↪ → && HFGWTR_EL2.CPACR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif EffectiveHCR_EL2_NVx() IN {'111'} then NVMem[0x100] = X[t, 64]; else if IsFeatureImplemented(FEAT_SRMASK) then CPACR_EL1 = (X[t, 64] AND NOT EffectiveCPACRMASK_EL1()) OR (CPACR_EL1 AND ↪ → EffectiveCPACRMASK_EL1()); else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && CPTR_EL3.TCPAC == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_SRMASK) then CPTR_EL2 = (X[t, 64] AND NOT EffectiveCPTRMASK_EL2()) OR (CPTR_EL2 AND ↪ → EffectiveCPTRMASK_EL2()); else CPTR_EL2 = X[t, 64]; else CPACR_EL1 = X[t, 64]; elsif PSTATE.EL == EL3 then CPACR_EL1 = X[t, 64];
```