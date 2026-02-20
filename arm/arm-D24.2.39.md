## D24.2.39 CPTR\_EL3, Architectural Feature Trap Register (EL3)

The CPTR\_EL3 characteristics are:

## Purpose

Controls trapping to EL3 of accesses to CPACR, CPACR\_EL1, HCPTR, CPTR\_EL2, trace, Activity Monitor, SME, Streaming SVE, SVE, and Advanced SIMD and floating-point functionality.

## Configuration

This register is present only when EL3 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to CPTR\_EL3 are UNDEFINED.

## Attributes

CPTR\_EL3 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## TCPAC, bit [31]

Traps all of the following to EL3, from both Execution states and any Security state.

- EL2 accesses to CPTR\_EL2, reported using EC syndrome value 0x18 , or HCPTR, reported using EC syndrome value 0x03 .
- EL2 and EL1 accesses to CPACR\_EL1 reported using EC syndrome value 0x18 , or CPACR reported using EC syndrome value 0x03 .

When CPTR\_EL3.TCPAC is:

| TCPAC   | Meaning                                                                                                                                                   |
|---------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0     | This control does not cause any instructions to be trapped.                                                                                               |
| 0b1     | EL2 accesses to the CPTR_EL2 or HCPTR, and EL2 and EL1 accesses to the CPACR_EL1 or CPACR, are trapped to EL3, unless they are trapped by CPTR_EL2.TCPAC. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

TAM, bit [30]

## When FEAT\_AMUv1 is implemented:

Trap Activity Monitor access. Traps EL2, EL1, and EL0 accesses to all Activity Monitor registers to EL3. Accesses to the Activity Monitors registers are trapped as follows:

- In AArch64 state, the following registers are trapped to EL3 and reported using EC syndrome value 0x18 :
- AMUSERENR\_EL0, AMCFGR\_EL0, AMCGCR\_EL0, AMCNTENCLR0\_EL0, AMCNTENCLR1\_EL0, AMCNTENSET0\_EL0, AMCNTENSET1\_EL0, AMCR\_EL0, AMEVCNTR0&lt;n&gt;\_EL0, AMEVCNTR1&lt;n&gt;\_EL0, AMEVTYPER0&lt;n&gt;\_EL0, and AMEVTYPER1&lt;n&gt;\_EL0.
- In AArch32 state, accesses with MRC or MCR to the following registers reported using EC syndrome value 0x03 :
- AMUSERENR, AMCFGR, AMCGCR, AMCNTENCLR0, AMCNTENCLR1, AMCNTENSET0, AMCNTENSET1, AMCR, AMEVTYPER0&lt;n&gt;, and AMEVTYPER1&lt;n&gt;.
- In AArch32 state, accesses with MRRC or MCRR to the following registers, reported using EC syndrome value 0x04 :
- AMEVCNTR0&lt;n&gt;, AMEVCNTR1&lt;n&gt;.

| TAM   | Meaning                                                                           |
|-------|-----------------------------------------------------------------------------------|
| 0b0   | Accesses from EL2, EL1, and EL0 to Activity Monitor registers are not trapped.    |
| 0b1   | Accesses from EL2, EL1, and EL0 to Activity Monitor registers are trapped to EL3. |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [29:21]

Reserved, RES0.

## TTA, bit [20]

## When System register access to the trace unit registers is implemented:

Traps System register accesses. Accesses to the trace registers, from all Exception levels, any Security state, and both Execution states are trapped to EL3 as follows:

- In AArch64 state, Trace registers with op0=2, op1=1, and CRn&lt; 0b1000 are trapped to EL3 and reported using EC syndrome value 0x18 .
- In AArch32 state, accesses using MCR or MRC to the Trace registers with cpnum=14, opc1=1, and CRn&lt; 0b1000 are reported using EC syndrome value 0x05 .

| TTA   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | This control does not cause any instructions to be trapped. |

| TTA   | Meaning                                                                                                                                    |
|-------|--------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1   | Any System register access to the trace registers is trapped to EL3, unless it is trapped by CPACR.TRCDIS, CPACR_EL1.TTA, or CPTR_EL2.TTA. |

Note

The ETMv4 architecture and ETE do not permit EL0 to access the trace registers. If the trace unit implements FEAT\_ETMv4 or FEAT\_ETE, EL0 accesses to the trace registers are UNDEFINED, and any resulting exception is higher priority than this trap exception. EL3 does not provide traps on trace register accesses through the Memory-mapped interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, no side-effects occur before the exception is taken, see 'Configurable instruction controls'.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bits [19:13]

Reserved, RES0.

## ESM, bit [12]

## When FEAT\_SME is implemented:

Traps execution of SME instructions, SVE instructions when FEAT\_SVE is not implemented or the PE is in Streaming SVE mode, and instructions that directly access the SMCR\_EL1, SMCR\_EL2, SMCR\_EL3, SMPRI\_EL1, SMPRIMAP\_EL2, or SVCR System registers, from all Exception levels and any Security state, to EL3.

When instructions that directly access the SVCR System register are trapped with reference to this control, the MSR SVCRSM , MSR SVCRZA , and MSR SVCRSMZA instructions are also trapped.

When direct accesses to SMPRI\_EL1 and SMPRIMAP\_EL2 are trapped, the exception is reported using EC syndrome value 0x18 . Otherwise, the exception is reported using EC syndrome value 0x1D , with an ISS code of 0x0000000 .

This field does not affect whether Streaming SVE or SME register values are valid.

Atrap taken as a result of CPTR\_EL3.ESM has precedence over a trap taken as a result of CPTR\_EL3.TFP.

| ESM   | Meaning                                                                                    |
|-------|--------------------------------------------------------------------------------------------|
| 0b0   | This control causes execution of these instructions at all Exception levels to be trapped. |
| 0b1   | This control does not cause execution of any instructions to be trapped.                   |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

## Bit [11]

Reserved, RES0.

## TFP, bit [10]

Traps execution of instructions which access the Advanced SIMD and floating-point functionality, from all Exception levels, any Security state, and both Execution states, to EL3.

This includes the following registers, all reported using EC syndrome value 0x07 :

- FPCR, FPSR, FPEXC32\_EL2, and any of the SIMD and floating-point registers V0-V31, including their views as D0-D31 registers or S0-S31 registers.
- If FEAT\_FPMR is implemented, FPMR.
- MVFR0, MVFR1, MVFR2, FPSCR, FPEXC, and any of the SIMD and floating-point registers Q0-Q15, including their views as D0-D31 registers or S0-S31 registers.
- VMSRaccesses to FPSID.

Permitted VMSR accesses to FPSID are ignored, but for the purposes of this trap the architecture defines a VMSR access to the FPSID from EL1 or higher as an access to a SIMD and floating-point register.

Traps execution at all Exception levels of SME and SVE instructions to EL3 from any Security state. The exception is reported using EC syndrome value 0x07 .

Atrap taken as a result of CPTR\_EL3.ESM has precedence over a trap taken as a result of CPTR\_EL3.TFP.

Atrap taken as a result of CPTR\_EL3.EZ has precedence over a trap taken as a result of CPTR\_EL3.TFP.

| TFP   | Meaning                                                                                    |
|-------|--------------------------------------------------------------------------------------------|
| 0b0   | This control does not cause execution of any instructions to be trapped.                   |
| 0b1   | This control causes execution of these instructions at all Exception levels to be trapped. |

## Note

FPEXC32\_EL2 is not accessible from EL0 using AArch64.

FPSID, MVFR0, MVFR1, and FPEXC are not accessible from EL0 using AArch32.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bit [9]

Reserved, RES0.

## EZ, bit [8]

## When FEAT\_SVE is implemented:

Traps execution of SVE instructions when the PE is not in Streaming SVE mode, and instructions that directly access the ZCR\_EL3, ZCR\_EL2, or ZCR\_EL1 System registers, from all Exception levels and any Security state, to EL3.

The exception is reported using EC syndrome value 0x19 .

Atrap taken as a result of CPTR\_EL3.EZ has precedence over a trap taken as a result of CPTR\_EL3.TFP.

| EZ   | Meaning                                                                                    |
|------|--------------------------------------------------------------------------------------------|
| 0b0  | This control causes execution of these instructions at all Exception levels to be trapped. |
| 0b1  | This control does not cause execution of any instructions to be trapped.                   |

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Otherwise:

Reserved, RES0.

Bits [7:0]

Reserved, RES0.

## Accessing CPTR\_EL3

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, CPTR\_EL3

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then X[t, 64] = CPTR_EL3;
```

MSR CPTR\_EL3, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b110 | 0b0001 | 0b0001 | 0b010 |

```
if !(HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then CPTR_EL3 = X[t, 64];
```