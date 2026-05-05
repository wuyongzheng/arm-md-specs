## C5.5.9 TLBI ALLE3OS, TLBI ALLE3OSNXS, TLB Invalidate All, EL3, Outer Shareable

The TLBI ALLE3OS, TLBI ALLE3OSNXS characteristics are:

## Purpose

If EL3 is implemented, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is a stage 1 translation table entry, from any level of the translation table walk.
- The entry would be required to translate an address using the EL3 translation regime.

The invalidation applies to all PEs in the same Outer Shareable shareability domain as the PE that executes this System instruction.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_TLBIOS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBI ALLE3OS, TLBI ALLE3OSNXS are UNDEFINED.

## Attributes

TLBI ALLE3OS, TLBI ALLE3OSNXS is a 64-bit System instruction.

## Field descriptions

This instruction has no applicable fields.

The value in the register specified by &lt;Xt&gt; is ignored.

## Executing TLBI ALLE3OS, TLBI ALLE3OSNXS

The Rt field should be set to 0b11111 . If the Rt field is not set to 0b11111 , it is CONSTRAINED UNPREDICTABLE whether:

- The instruction is UNDEFINED.
- The instruction behaves as if the Rt field is set to 0b11111 .

This system instruction is an alias of the SYS instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBI ALLE3OS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1000 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_TLBIOS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL3) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL3), Regime_EL3, Broadcast_OSH, TLBI_AllAttr, X[t, 64]);
```

When FEAT\_XS is implemented TLBI ALLE3OSNXS{, &lt;Xt&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1001 | 0b0001 | 0b000 |

```
if !(IsFeatureImplemented(FEAT_TLBIOS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL3) then return; else AArch64.TLBI_ALL(SecurityStateAtEL(EL3), Regime_EL3, Broadcast_OSH, TLBI_ExcludeXS, X[t, ↪ → 64]);
```
