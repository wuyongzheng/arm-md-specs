## C5.5.6 TLBI ALLE2OS, TLBI ALLE2OSNXS, TLB Invalidate All, EL2, Outer Shareable

The TLBI ALLE2OS, TLBI ALLE2OSNXS characteristics are:

## Purpose

If EL2 is implemented and enabled in the current Security state, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is a stage 1 translation table entry, from any level of the translation table walk.
- If FEAT\_RME is implemented, one of the following applies:
- SCR\_EL3.{NSE, NS} is {0, 0} and the entry would be required to translate any address using the Secure EL2&amp;0 or EL2 translation regime.
- SCR\_EL3.{NSE, NS} is {0, 1} and the entry would be required to translate any address using the Non-secure EL2&amp;0 or EL2 translation regime.
- SCR\_EL3.{NSE, NS} is {1, 1} and the entry would be required to translate any address using the Realm EL2&amp;0 or EL2 translation regime.
- If FEAT\_RME is not implemented, one of the following applies:
- SCR\_EL3.NS is 0 and the entry would be required to translate any address using the Secure EL2&amp;0 or EL2 translation regime.
- SCR\_EL3.NS is 1 and the entry would be required to translate any address using the Non-secure EL2&amp;0 or EL2 translation regime.

The invalidation applies to all PEs in the same Outer Shareable shareability domain as the PE that executes this System instruction.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_TLBIOS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBI ALLE2OS, TLBI ALLE2OSNXS are UNDEFINED.

## Attributes

TLBI ALLE2OS, TLBI ALLE2OSNXS is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing TLBI ALLE2OS, TLBI ALLE2OSNXS

The Rt field should be set to 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBI ALLE2OS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1000 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_TLBIOS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL20, Broadcast_OSH, TLBI_AllAttr, X[t, 64]); else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL2, Broadcast_OSH, TLBI_AllAttr, X[t, 64]); elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL20, Broadcast_OSH, TLBI_AllAttr, X[t, 64]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL2, Broadcast_OSH, TLBI_AllAttr, X[t, 64]);
```

When FEAT\_XS is implemented TLBI ALLE2OSNXS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b100 | 0b1001 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_TLBIOS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if ELIsInHost(EL2) then AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL20, Broadcast_OSH, TLBI_ExcludeXS, X[t, ↪ → 64]); else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL2, Broadcast_OSH, TLBI_ExcludeXS, X[t, ↪ → 64]);
```

```
elsif PSTATE.EL == EL3 then if !EL2Enabled() then UNDEFINED; elsif ELIsInHost(EL2) then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL20, Broadcast_OSH, TLBI_ExcludeXS, ↪ → X[t, 64]); else if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL2) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL2), Regime_EL2, Broadcast_OSH, TLBI_ExcludeXS, ↪ → X[t, 64]);
```
