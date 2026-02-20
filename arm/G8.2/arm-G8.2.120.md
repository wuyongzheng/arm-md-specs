## G8.2.120 NSACR, Non-Secure Access Control Register

The NSACR characteristics are:

## Purpose

When EL3 is implemented and can use AArch32, defines the Non-secure access permissions to Trace, Advanced SIMD and floating-point functionality. Also includes IMPLEMENTATION DEFINED bits that can define Non-secure access permissions for IMPLEMENTATION DEFINED functionality.

## Configuration

Note

In AArch64 state, the NSACR controls are replaced by controls in CPTR\_EL3.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to NSACR are UNDEFINED.

## Attributes

NSACRis a 32-bit register.

## Field descriptions

<!-- image -->

If EL3 is implemented and is using AArch64 then:

- Any read of the NSACR from Non-secure EL2 or Non-secure EL1 returns a value of 0x00000C00 .
- Any read or write to NSACR from Secure EL1 is trapped as an exception to EL3.

If EL3 is not implemented, then any read of the NSACR from EL2 or EL1 returns a value of 0x00000C00 .

## Bits [31:21]

Reserved, RES0.

## NSTRCDIS, bit [20]

Disables Non-secure System register accesses to all implemented trace registers.

| NSTRCDIS   | Meaning                                                                                                |
|------------|--------------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on:                                                                         |
|            | • System register access to implemented trace registers. • The behavior of CPACR.TRCDIS and HCPTR.TTA. |

| NSTRCDIS   | Meaning                                                                                                                                              |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1        | Non-secure System register accesses to all implemented trace registers are disabled, meaning:                                                        |
|            | • CPACR.TRCDIS behaves as RAO/WI in Non-secure state, regardless of its actual value. • HCPTR.TTA behaves as RAO/WI, regardless of its actual value. |

The implementation of this field must correspond to the implementation of the CPACR.TRCDIS field:

- If CPACR.TRCDIS is RAZ/WI, this field is RAZ/WI.
- If CPACR.TRCDIS is RW, this field is RW.

## Note

- FEAT\_ETMv4 and FEAT\_ETE do not permit EL0 to access the trace registers. EL0 accesses to the trace registers are UNDEFINED.
- The Arm architecture does not provide Non-secure access controls on trace register accesses through the optional memory-mapped external debug interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, any side-effects that are normally associated with the access do not occur before the exception is taken.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Bit [19]

Reserved, RES0.

## IMPLEMENTATIONDEFINED, bits [18:16]

IMPLEMENTATION DEFINED.

## NSASEDIS, bit [15]

Disables Non-secure access to the Advanced SIMD functionality.

| NSASEDIS   | Meaning                                                                                                                                                                                                                          |
|------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0        | This control has no effect on: • Non-secure access to Advanced SIMD functionality. • The behavior of CPACR.ASEDIS and HCPTR.TASE.                                                                                                |
| 0b1        | Non-secure access to the Advanced SIMD functionality is disabled, meaning: • CPACR.ASEDIS behaves as RAO/WI in Non-secure state, regardless of its actual value. • HCPTR.TASE behaves as RAO/WI, regardless of its actual value. |

The implementation of this field must correspond to the implementation of the CPACR.ASEDIS field:

- If CPACR.ASEDIS is RES0, this field is RES0. If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0.
- If CPACR.ASEDIS is RAZ/WI, this field is RAZ/WI.
- If CPACR.ASEDIS is RW, this field is RW.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3, this field resets to '0' .

## Bits [14:12]

Reserved, RES0.

## cp11, bit [11]

The value of this field is ignored. If this field is programmed with a different value to the cp10 field then this field is UNKNOWN on a direct read of the NSACR.

If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## cp10, bit [10]

Enable Non-secure access to the Advanced SIMD and floating-point features. Possible values of the fields are:

| cp10   | Meaning                                                                                                                                                                                                                                                                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Advanced SIMD and floating-point features can be accessed only from Secure state. Any attempt to access this functionality from Non-secure state is UNDEFINED. When the PE is in Non-secure state: • The CPACR.{cp11, cp10} fields ignore writes and read as 0b00 , access denied. • The HCPTR.{TCP11, TCP10} fields behave as RAO/WI, regardless of their actual values. |
| 0b1    | Advanced SIMD and floating-point features can be accessed from both Security states.                                                                                                                                                                                                                                                                                      |

If Non-secure access to the Advanced SIMD and floating-point functionality is enabled, the CPACR must be checked to determine the level of access that is permitted.

The Advanced SIMD and floating-point features controlled by these fields are:

- Execution of any floating-point or Advanced SIMD instruction.
- Any access to the Advanced SIMD and floating-point registers D0-D31 and their views as S0-S31 and Q0-Q15.
- Any access to the FPSCR, FPSID, MVFR0, MVFR1, MVFR2, or FPEXC System registers.

If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [9:0]

Reserved, RES0.

## Accessing NSACR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); elsif !HaveEL(EL3) || (IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.NS == ↪ → '1') then R[t] = Zeros(20):'1100':Zeros(8); else R[t] = NSACR; elsif PSTATE.EL == EL2 then if !HaveEL(EL3) || (IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && SCR_EL3.NS == '1') ↪ → then R[t] = Zeros(20):'1100':Zeros(8); else R[t] = NSACR; elsif PSTATE.EL == EL3 then R[t] = NSACR;
```

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0001 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else UNDEFINED;
```

```
elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if CP15SDISABLE2 == HIGH then UNDEFINED; else NSACR = R[t];
```