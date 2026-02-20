## G8.2.154 TLBIMVAH, TLB Invalidate by VA, Hyp mode

The TLBIMVAH characteristics are:

## Purpose

If EL2 is implemented, invalidate all cached copies of translation table entries from TLBs that are from any level of the translation table walk that would be required for the Non-secure EL2 translation regime and used to translate the specified address.

The invalidation only applies to the PE that executes this System instruction.

## Configuration

This system instruction is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to TLBIMVAH are UNDEFINED.

## Attributes

TLBIMVAH is a 32-bit System instruction.

## Field descriptions

<!-- image -->

## VA, bits [31:12]

Virtual address to match. Any TLB entries that match the ASID value and V A value will be affected by this System instruction.

## Bits [11:0]

Reserved, RES0.

## Executing TLBIMVAH

If this instruction is executed in a Secure privileged mode other than Monitor mode, then the behavior is CONSTRAINED UNPREDICTABLE, and one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP.
- The instruction executes as if it had been executed in Monitor mode.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1000 | 0b0111 | 0b001  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T8 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T8 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch32.TLBI_VA(SecurityStateAtEL(EL2), Regime_EL2, VMID_NONE, Broadcast_NSH, TLBILevel_Any, ↪ → TLBI_AllAttr, R[t]); elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then UNDEFINED; else AArch32.TLBI_VA(SS_NonSecure, Regime_EL2, VMID[], Broadcast_NSH, TLBILevel_Any, TLBI_AllAttr, ↪ → R[t]);
```