## C5.5.144 TLBIP VALE3IS, TLBIP VALE3ISNXS, TLB Invalidate Pair by VA, Last level, EL3, Inner Shareable

The TLBIP VALE3IS, TLBIP VALE3ISNXS characteristics are:

## Purpose

If EL3 is implemented, invalidates cached copies of translation table entries from TLBs that meet all the following requirements:

- The entry is one of the following:
- A128-bit stage 1 translation table entry, from the final level of the translation table walk.
- A64-bit stage 1 translation table entry, from the final level of the translation table walk, if TTL[3:2] is 0b00 .
- The entry would be used to translate the specified V A using the EL3 translation regime.

The invalidation applies to all PEs in the same Inner Shareable shareability domain as the PE that executes this System instruction.

If FEAT\_XS is implemented, the nXS variant of this System instruction is defined.

It is IMPLEMENTATION SPECIFIC whether the TLBI System instruction with the nXS qualifier invalidates TLB entries with the XS attribute set to 1.

The TLBI System instruction without the nXS qualifier waits for all memory accesses using in-scope old translation information to complete before it is considered complete.

The TLBI System instruction with the nXS qualifier is considered complete when the subset of these memory accesses with XS attribute set to 0 are complete.

## Configuration

This system instruction is present only when FEAT\_D128 is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to TLBIP V ALE3IS, TLBIP VALE3ISNXS are UNDEFINED.

## Attributes

TLBIP VALE3IS, TLBIP VALE3ISNXS is a 128-bit System instruction.

## Field descriptions

<!-- image -->

| 127   | 108       | 107       | 96   |
|-------|-----------|-----------|------|
| RES0  |           | VA[55:12] |      |
| 95    |           |           | 64   |
|       | VA[55:12] |           |      |
| 63    | 48 47     | 44 43     | 32   |
| RES0  | TTL       | RES0      |      |
| 31    |           |           | 0    |
| RES0  | RES0      | RES0      | RES0 |

## Bits [127:108]

Reserved, RES0.

## VA[55:12], bits [107:64]

Bits[55:12] of the virtual address to match. Any appropriate TLB entries that match the ASID value (if appropriate) and V A will be affected by this System instruction.

The treatment of the low-order bits of this field depends on the translation granule size, as follows:

- Where a 4KB translation granule is being used, all bits are valid and used for the invalidation.
- Where a 16KB translation granule is being used, bits [1:0] of this field are RES0 and ignored when the instruction is executed, because V A[13:12] have no effect on the operation of the instruction.
- Where a 64KB translation granule is being used, bits [3:0] of this field are RES0 and ignored when the instruction is executed, because V A[15:12] have no effect on the operation of the instruction.

## Bits [63:48]

Reserved, RES0.

## TTL, bits [47:44]

## When FEAT\_TTL is implemented:

Translation Table Level. Indicates the level of the translation table walk that holds the leaf entry for the address being invalidated.

| TTL    | Meaning                                                                                                                                                                                                   |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b00xx | No information supplied as to the translation table level. Hardware must assume that the entry can be from any level. In this case, TTL<1:0> is RES0.                                                     |
| 0b01xx | The entry comes from a 4KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Level 0. 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3.                                  |
| 0b10xx | The entry comes from a 16KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |
| 0b11xx | The entry comes from a 64KB translation granule. The level of walk for the leaf level 0bxx is encoded as: 0b00 : Reserved. Treat as if TTL<3:2> is 0b00 . 0b01 : Level 1. 0b10 : Level 2. 0b11 : Level 3. |

If an incorrect value of the TTL field is specified for the entry being invalidated by the instruction, then no entries are required by the architecture to be invalidated from the TLB.

## Otherwise:

Reserved, RES0.

## Bits [43:0]

Reserved, RES0.

## Executing TLBIP VALE3IS, TLBIP VALE3ISNXS

This system instruction is an alias of the SYSP instruction.

Accesses to this instruction use the following encodings in the System instruction encoding space:

TLBIP VALE3IS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1000 | 0b0011 | 0b101 |

if !(IsFeatureImplemented(FEAT\_D128) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED;

elsif PSTATE.EL == EL0 then

UNDEFINED;

elsif PSTATE.EL == EL1 then

UNDEFINED;

elsif PSTATE.EL == EL2 then

UNDEFINED;

elsif PSTATE.EL == EL3 then

if IsFeatureImplemented(FEAT\_RME) &amp;&amp; !ValidSecurityStateAtEL(EL3) then

return;

else

AArch64.TLBIP\_VA(SecurityStateAtEL(EL3), Regime\_EL3, VMID\_NONE, Broadcast\_ISH, TLBILevel\_Last, ↪ → TLBI\_AllAttr, X[t, t2, 128]);

TLBIP VALE3ISNXS{, &lt;Xt&gt;, &lt;Xt2&gt;}

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b01  | 0b110 | 0b1001 | 0b0011 | 0b101 |

if !(IsFeatureImplemented(FEAT\_D128) &amp;&amp; IsFeatureImplemented(FEAT\_AA64)) then

UNDEFINED; elsif !IsFeatureImplemented(FEAT\_XS) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then UNDEFINED; elsif PSTATE.EL == EL2 then UNDEFINED; elsif PSTATE.EL == EL3 then if IsFeatureImplemented(FEAT\_RME) &amp;&amp; !ValidSecurityStateAtEL(EL3) then return; else AArch64.TLBIP\_VA(SecurityStateAtEL(EL3), Regime\_EL3, VMID\_NONE, Broadcast\_ISH, TLBILevel\_Last, ↪ → TLBI\_ExcludeXS, X[t, t2, 128]);
