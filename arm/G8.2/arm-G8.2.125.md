## G8.2.125 RVBAR, Reset Vector Base Address Register

The RVBAR characteristics are:

## Purpose

If EL3 is not implemented, contains the IMPLEMENTATION DEFINED address that execution starts from after reset when executing in AArch32 state.

## Configuration

This register is implemented only if the highest Exception level implemented is capable of using AArch32, and is not EL3.

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to RVBAR are UNDEFINED.

## Attributes

RVBARis a 32-bit register.

## Field descriptions

<!-- image -->

## ResetAddress, bits [31:1]

Bits [31:1] of the IMPLEMENTATION DEFINED address that execution starts from after reset when executing in 32-bit state.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Bit [0]

Reserved, RES1.

## Accessing RVBAR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b1100 | 0b0000 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if IsHighestEL(EL1) then R[t] = RVBAR;
```

```
elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T12 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T12 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif IsFeatureImplemented(FEAT_AA64EL3) && !ELUsingAArch32(EL3) && ↪ → IsCurrentSecurityState(SS_Secure) then AArch64.AArch32SystemAccessTrap(EL3, 0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then if IsHighestEL(EL2) then R[t] = RVBAR; else UNDEFINED; elsif PSTATE.EL == EL3 then R[t] = MVBAR;
```