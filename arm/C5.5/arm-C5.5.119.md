## C5.5.119 TLBIP RVALE3, TLBIP RVALE3NXS, TLB Range Invalidate by VA, Last level, EL3

The TLBIP RVALE3, TLBIP RVALE3NXS characteristics are:

## Purpose

If EL3 is implemented, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry, from the final level of the translation table walk up to the level indicated in the TTL hint.
- A64-bit stage 1 translation table entry, from the final level of the translation table walk, if TTL is 0b00 .
- The entry would be used to translate any of the V As in the specified address range using the EL3 translation regime.
- The entry is within the address range determined by the formula [BaseADDR &lt;= VA &lt; BaseADDR + ((NUM +1)*2 (5*SCALE +1) * Translation\_Granule\_Size)].

The invalidation applies to the PE that executes this System instruction.

For 128-bit translation table entry, the range of addresses invalidated is UNPREDICTABLE when Block or Page size corresponding to TTL and TG, for the translation system is not aligned.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP RV ALE3, TLBIP RVALE3NXS are UNDEFINED.

## Attributes

TLBIP RVALE3, TLBIP RVALE3NXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

Bits [127:108]

Reserved, RES0.

## BaseADDR[55:12], bits [107:64]

The starting address for the range of the maintenance instructions. This field is BaseADDR[55:12] for all translation granules.

## Bits [63:48]

Reserved, RES0.

## TG, bits [47:46]

Translation granule size.

| TG   | Meaning                  |
|------|--------------------------|
| 0b00 | Reserved.                |
| 0b01 | 4K translation granule.  |
| 0b10 | 16K translation granule. |
| 0b11 | 64K translation granule. |

The instruction takes a translation granule size for the translations that are being invalidated. If the translations used a different translation granule size than the one being specified, then the architecture does not require that the instruction invalidates any entries.

## SCALE, bits [45:44]

The exponent element of the calculation that is used to produce the upper range.

## NUM,bits [43:39]

The base element of the calculation that is used to produce the upper range.

## TTL, bits [38:37]

TTL Level hint. The TTL hint is only guaranteed to invalidate:

- Non-leaf-level entries in the range up to but not including the level described by the TTL hint.
- Leaf-level entries in the range that match the level described by the TTL hint.

| TTL   | Meaning                                                                            |
|-------|------------------------------------------------------------------------------------|
| 0b00  | The entries in the range can be using any level for the translation table entries. |
| 0b01  | The TTL hint indicates level 1.                                                    |
| 0b10  | The TTL hint indicates level 2.                                                    |
| 0b11  | The TTL hint indicates level 3.                                                    |

## Bits [36:0]

Reserved, RES0.

## Executing TLBIP RVALE3, TLBIP RVALE3NXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBIP RVALE3{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1000 | 0b0110 | 0b101 |

if !(IsFeatureImplemented(FEAT\_D128) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT\_RME) &amp;&amp; !ValidSecurityStateAtEL(EL3) then return; else AArch64.TLBIP\_RVA(SecurityStateAtEL(EL3), Regime\_EL3, VMID\_NONE, Broadcast\_NSH, TLBILevel\_Last, ↪ → TLBI\_AllAttr, X[t, t2, 128]);

TLBIP RVALE3NXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1001 | 0b0110 | 0b101 |

```
if !(IsFeatureImplemented(FEAT_D128) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif !IsFeatureImplemented(FEAT_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT_RME) && !ValidSecurityStateAtEL(EL3) then return; else AArch64.TLBIP_RVA(SecurityStateAtEL(EL3), Regime_EL3, VMID_NONE, Broadcast_NSH, TLBILevel_Last, ↪ → TLBI_ExcludeXS, X[t, t2, 128]);
```
