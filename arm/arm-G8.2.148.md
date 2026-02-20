## G8.2.148 TLBIIPAS2LIS, TLB Invalidate by Intermediate Physical Address, Stage 2, Last level, Inner Shareable

The TLBIIPAS2LIS characteristics are:

## Purpose

If EL2 is implemented, invalidate all cached copies of translation table entries from TLBs that meet the following requirements:

- The entry is a stage 2 only translation table entry, from the final level of the translation table walk.
- SCR.NS is 1.
- The entry would be used for the specified IPA.
- The entry would be used with the current VMID.
- The entry would be required for the PL1&amp;0 translation regime.

The invalidation is not required to apply to caching structures that combine stage 1 and stage 2 translation table entries.

The invalidation applies to all PEs in the same Inner Shareable shareability domain as the PE that executes this System instruction.

## Configuration

Note

This System instruction is not implemented in architecture versions before Armv8.

This system instruction is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to TLBIIPAS2LIS are UNDEFINED.

## Attributes

TLBIIPAS2LIS is a 32-bit System instruction.

## Field descriptions

<!-- image -->

## Bits [31:28]

Reserved, RES0.

## IPA[39:12], bits [27:0]

Bits[39:12] of the intermediate physical address to match.

## Executing TLBIIPAS2LIS

If this instruction is executed in a Secure privileged mode other than Monitor mode, then the behavior is CONSTRAINED UNPREDICTABLE, and one of the following behaviors must occur:

- The instruction is UNDEFINED.
- The instruction is treated as a NOP.
- The instruction executes as if it had been executed in Monitor mode.

Accesses to this instruction use the following encodings in the System instruction encoding space:

MCR{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b1000 | 0b0000 | 0b101  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T8 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T8 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch32.TLBI_IPAS2(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, R[t]); elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then UNDEFINED; elsif SCR.NS == '0' then return; else AArch32.TLBI_IPAS2(SS_NonSecure, Regime_EL10, VMID_NONE, Broadcast_ISH, TLBILevel_Last, ↪ → TLBI_AllAttr, R[t]);
```