## G8.2.33 CPACR, Architectural Feature Access Control Register

The CPACR characteristics are:

## Purpose

Controls access to trace, and to Advanced SIMD and floating-point functionality from EL0, EL1, and EL3.

In an implementation that includes EL2, the CPACR has no effect on instructions executed at EL2.

## Configuration

Bits in the NSACR control Non-secure access to the CPACR fields. See the field descriptions for more information.

## Note

In the register field descriptions, controls are described as applying at specified Privilege levels. This is because, in Secure state, a PL1 control:

- Applies to execution in a Secure EL3 mode when EL3 is using AArch32.
- Applies to execution in a Secure EL1 mode when EL3 is using AArch64.

See 'Security state, Exception levels, and AArch32 execution privilege'.

AArch32 System register CPACR bits [31:0] are architecturally mapped to AArch64 System register CPACR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to CPACR are UNDEFINED.

## Attributes

CPACR is a 32-bit register.

## Field descriptions

<!-- image -->

## ASEDIS, bit [31]

Disables PL0 and PL1 execution of Advanced SIMD instructions.

| ASEDIS   | Meaning                                                                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0      | This control permits execution of Advanced SIMD instructions at PL0 and PL1.                                                                                 |
| 0b1      | All instruction encodings that are Advanced SIMD instruction encodings, but are not also floating-point instruction encodings, are UNDEFINED at PL0 and PL1. |

If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0. Otherwise, it is IMPLEMENTATION DEFINED whether this field is implemented as a RW field. If it is not implemented as a RW field, it is RAZ/WI.

If EL3 is implemented and is using AArch32, and the value of NSACR.NSASEDIS is 1, this field behaves as RAO/WI in Non-secure state, regardless of its actual value. This applies even if the field is implemented as RAZ/WI.

For the list of instructions affected by this field, see 'Controls of Advanced SIMD operation that do not apply to floating-point operation'.

See the description of CPACR.cp10 for a list of other controls that can disable or trap execution of Advanced SIMD instructions in AArch32 state.

The reset behavior of this field is:

- On a Warm reset, this field resets to '0' .

## Bits [30:29]

Reserved, RES0.

## TRCDIS, bit [28]

Traps PL0 and PL1 System register accesses to all implemented trace registers to Undefined mode.

| TRCDIS   | Meaning                                                                                                |
|----------|--------------------------------------------------------------------------------------------------------|
| 0b0      | This control has no effect on PL0 and PL1 System register accesses to trace registers.                 |
| 0b1      | PL0 and PL1 System register accesses to all implemented trace registers are trapped to Undefined mode. |

If the implementation does not include a trace unit, or does not include a System register interface to the trace unit registers, this field is RES0. Otherwise, it is IMPLEMENTATION DEFINED whether this field is implemented as a RW field. If it is not implemented as a RW field, it is RAZ/WI.

If EL3 is implemented and is using AArch32, and the value of NSACR.NSTRCDIS is 1, this field behaves as RAO/WI in Non-secure state, regardless of its actual value. This applies even if the field is implemented as RAZ/WI.

## Note

- FEAT\_ETMv4 and FEAT\_ETE do not permit EL0 to access the trace registers. EL0 accesses to the trace System registers are UNDEFINED.
- The Arm architecture does not provide traps on trace register accesses through the optional memory-mapped external debug interface.

System register accesses to the trace registers can have side-effects. When a System register access is trapped, any side-effects that are normally associated with the access do not occur before the exception is taken.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [27:24]

Reserved, RES0.

## cp11, bits [23:22]

The value of this field is ignored. If this field is programmed with a different value to the cp10 field then this field is UNKNOWN on a direct read of the CPACR.

If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0.

In Non-secure state, if EL3 is implemented and is using AArch32, when the value of NSACR.cp10 is 0, this field behaves as RAZ/WI, regardless of its actual value.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

When EL3 is implemented, EL3 is using AArch32, !IsCurrentSecurityState(SS\_Secure), and NSACR.cp10 == '0', access to this field is RAZ/WI.

## cp10, bits [21:20]

Defines the access rights for the Advanced SIMD and floating-point functionality. Possible values of the field are:

| cp10   | Meaning                                                                                                                   |
|--------|---------------------------------------------------------------------------------------------------------------------------|
| 0b00   | PL0 and PL1 accesses to Advanced SIMD and floating-point registers or instructions are UNDEFINED.                         |
| 0b01   | PL0 accesses to Advanced SIMD and floating-point registers or instructions are UNDEFINED.                                 |
| 0b10   | Reserved. The effect of programming this field to this value is CONSTRAINED UNPREDICTABLE choice between:                 |
|        | • The value of this field is treated as 0b00 , 0b01 , or 0b11 for all purposes other than reading the value of the field. |
|        | • PL1 accesses to floating-point and Advanced SIMD regsiters or instructions are UNDEFINED.                               |
| 0b11   | This control permits full access to the Advanced SIMD and floating-point functionality from PL0 and PL1.                  |

The Advanced SIMD and floating-point features controlled by these fields are:

- Execution of any floating-point or Advanced SIMD instruction.
- Any access to the Advanced SIMD and floating-point registers D0-D31 and their views as S0-S31 and Q0-Q15.
- Any access to the FPSCR, FPSID, MVFR0, MVFR1, MVFR2, or FPEXC System registers.

Note

The CPACR has no effect on Advanced SIMD and floating-point accesses from PL2. These can be disabled by the HCPTR.TCP10 field.

If the implementation does not include Advanced SIMD and floating-point functionality, this field is RES0.

In Non-secure state, if EL3 is implemented and is using AArch32, when the value of NSACR.cp10 is 0, this field behaves as RAZ/WI, regardless of its actual value.

Execution of Advanced SIMD and floating-point instructions in AArch32 state can be disabled or trapped by the following controls:

- CPACR.cp10, or, if executing at EL0, CPACR\_EL1.FPEN.
- FPEXC.EN.
- If executing in Non-secure state:
- HCPTR.TCP10, or if EL2 is using AArch64, CPTR\_EL2.TFP.
- NSACR.cp10, or if EL3 is using AArch64, CPTR\_EL3.TFP.
- For Advanced SIMD instructions only:
- CPACR.ASEDIS.
- If executing in Non-secure state, HCPTR.TASE and NSACR.NSASEDIS.

See the descriptions of the controls for more information.

The reset behavior of this field is:

- On a Warm reset, this field resets to '00' .

When EL3 is implemented, EL3 is using AArch32, !IsCurrentSecurityState(SS\_Secure), and NSACR.cp10 == '0', access to this field is RAZ/WI.

## Bits [19:0]

Reserved, RES0.

## Accessing CPACR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TCPAC ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TCPAC == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = CPACR; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else R[t] = CPACR; elsif PSTATE.EL == EL3 then R[t] = CPACR;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0001 | 0b0000 | 0b010  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && CPTR_EL2.TCPAC ↪ → == '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCPTR.TCPAC == ↪ → '1' then AArch32.TakeHypTrapException(0x03); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else CPACR = R[t]; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_AA64EL3) && ↪ → !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == '1' then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && CPTR_EL3.TCPAC == ↪ → '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.AArch32SystemAccessTrap(EL3, 0x03); else CPACR = R[t]; elsif PSTATE.EL == EL3 then CPACR = R[t];
```