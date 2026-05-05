## C5.5.81 TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS, TLB Invalidate by VMID, All at Stage 1 and 2, EL1, Inner Shareable

The TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS characteristics are:

## Purpose

Invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is a stage 1 or stage 2 translation table entry, from any level of the translation table walk.
- If FEAT\_RME is implemented, one of the following applies:
- If SCR\_EL3.{NSE, NS} is {0, 0}, then:
- The entry would be required to translate an address using the Secure EL1&amp;0 translation regime.
- If FEAT\_SEL2 is implemented and enabled, the entry would be used with the current VMID.
- If SCR\_EL3.{NSE, NS} is {0, 1}, then:
- The entry would be required to translate an address using the Non-secure EL1&amp;0 translation regime.
- If Non-secure EL2 is implemented, the entry would be used with the current VMID.
- If SCR\_EL3.{NSE, NS} is {1, 1}, then:
- The entry would be required to translate an address using the Realm EL1&amp;0 translation regime.
- The entry would be used with the current VMID.
- If FEAT\_RME is not implemented, one of the following applies:
- If SCR\_EL3.NS is 0, then:
- The entry would be required to translate an address using the Secure EL1&amp;0 translation regime.
- If FEAT\_SEL2 is implemented and enabled, the entry would be used with the current VMID.
- If SCR\_EL3.NS is 1, then:
- The entry would be required to translate an address using the Non-secure EL1&amp;0 translation regime.
- If Non-secure EL2 is implemented, the entry would be used with the current VMID.

The invalidation applies to all PEs in the same Inner Shareable shareability domain as the PE that executes this System instruction.

Note

From Armv8.4, when a TLB maintenance instruction is generated to the Secure EL1&amp;0 translation regime and is defined to pass a VMID argument, or would be defined to pass a VMID argument if SCR\_EL3.EEL2==1, then:

- APEwith SCR\_EL3.EEL2==1 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==0.
- APEwith SCR\_EL3.EEL2==0 is not architecturally required to invalidate any entries in the Secure EL1&amp;0 translation of a PE in the same required shareability domain with SCR\_EL3.EEL2==1.
- APEisarchitecturally required to invalidate all relevant entries in the Secure EL1&amp;0 translation of a System MMUinthe same required shareability domain with a VMID of 0.

Note

For the EL1&amp;0 translation regimes, the invalidation applies to both global entries and non-global entries with any ASID.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS are UNDEFINED.

## Attributes

TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing TLBI VMALLS12E1IS, TLBI VMALLS12E1ISNXS

The Rt field should be set to 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBI VMALLS12E1IS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1000 | 0b0011 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.TLBI_VMALLS12(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, TLBI_AllAttr, X[t, ↪ → 64]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID_NONE, Broadcast_ISH, TLBI_AllAttr, ↪ → X[t, 64]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBI_VMALLS12(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, ↪ → TLBI_AllAttr, X[t, 64]);
```

When FEAT\_XS is implemented TLBI VMALLS12E1ISNXS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1001 | 0b0011 | 0b110 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then
```

```
UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then AArch64.TLBI_VMALLS12(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, ↪ → TLBI_ExcludeXS, X[t, 64]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then AArch64.TLBI_VMALL(SecurityStateAtEL(EL1), Regime_EL10, VMID_NONE, Broadcast_ISH, ↪ → TLBI_ExcludeXS, X[t, 64]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL1) then return; else AArch64.TLBI_VMALLS12(SecurityStateAtEL(EL1), Regime_EL10, VMID[], Broadcast_ISH, ↪ → TLBI_ExcludeXS, X[t, 64]);
```
