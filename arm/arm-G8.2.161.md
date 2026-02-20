## G8.2.161 TLBTR, TLB Type Register

The TLBTR characteristics are:

## Purpose

Provides information about the TLB implementation. The register must define whether the implementation provides separate instruction and data TLBs, or a unified TLB. Normally, the IMPLEMENTATION DEFINED information in this register includes the number of lockable entries in the TLB.

## Configuration

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to TLBTR are UNDEFINED.

## Attributes

TLBTR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31                     | 1 0   |
|------------------------|-------|
| IMPLEMENTATION DEFINED | nU    |

## IMPLEMENTATIONDEFINED, bits [31:1]

IMPLEMENTATION DEFINED.

## nU, bit [0]

Not Unified TLB. Indicates whether the implementation has a unified TLB.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| nU   | Meaning                             |
|------|-------------------------------------|
| 0b0  | Unified TLB.                        |
| 0b1  | Separate Instruction and Data TLBs. |

Access to this field is RO.

## Accessing TLBTR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b011  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID1 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID1 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = TLBTR; elsif PSTATE.EL == EL2 then R[t] = TLBTR; elsif PSTATE.EL == EL3 then R[t] = TLBTR;
```