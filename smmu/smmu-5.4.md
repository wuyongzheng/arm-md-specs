## 5.4 CD, Context Descriptor

The CD characteristics are:

Configuration structure for stage 1 translation containing the base address of the translation tables and information for the translation regime for each of the lower and higher V A ranges.

CD is a 64-byte structure.

## Purpose

## Attributes

## Field descriptions

<!-- image -->

The CD structure contains stage 1 translation table pointers and associated fields (such as ASID and table walk attributes). Translation tables might be interpreted as VMSAv8-32 LPAE, VMSAv8-64 or VMSAv9-128 formats (as controlled by the AA64 field).

Invalid or contradictory CD configurations are marked ILLEGAL. A transaction that attempts to translate through a CD containing ILLEGAL configuration is terminated with an abort and a C\_BAD\_CD event is recorded in the Event queue appropriate to the Security state of the transaction, as determined by SEC\_SID.

Note: In accordance with Armv8-A [2], the interpretation of the translation table descriptor permissions is a function of the translation table format (from CD.AA64) and the Exception level to which the tables correspond (as determined by the STE StreamWorld).

## T0SZ, bits [5:0]

Size of VA region covered by TTB0.

This field is equivalent to TCR\_ELx.T0SZ in the A-profile architecture[2].

If CD.AA64 selects VMSAv8-32 LPAE:

- This field is 3 bits ([2:0]) and bits [5:3] are IGNORED.
- The input region size is calculated the same as in AArch32 TTBCR in the A-profile architecture[2].
- The valid range of values is 0 to 7 inclusive.
- -Note: All 3-bit values are valid, therefore it is not possible to use an out of range value when CD.AA64 selects VMSAv8-32 LPAE.

If CD.AA64 selects VMSAv8-64:

- This field is 6 bits and the region size is calculated the same as for TCR\_ELx.T0SZ in the A-profile architecture[2].
- If SMMU\_IDR3.STT == 0, the maximum valid value is 39.
- If SMMU\_IDR3.STT == 1, the maximum valid value is:
- -48, if the corresponding CD.TGx selects a 4KB or 16KB granule.
- -47, if the corresponding CD.TGx selects a 64KB granule.
- If SMMU\_IDR5.VAX indicates support for 52-bit VAs and either of the following also hold, the minimum permitted value is 12:
- -The corresponding CD.TGx selects a 64KB granule size.
- -CD.DS == 1 and the corresponding CD.TGx selects a 4KB or 16KB granule size. Otherwise, the minimum valid value is 16.

If CD.AA64 selects VMSAv9-128:

- The maximum valid value is:
- -48, if CD.TGx selects a 4KB or 16KB granule.
- -47, if CD.TGx selects a 64KB granule.
- The minimum valid value is:
- -8, if SMMU\_IDR5.VAX indicates support for 56-bit VAs and StreamWorld is EL3.
- -9, if SMMU\_IDR5.VAX indicates support for 56-bit VAs and StreamWorld is EL1 or any-EL2-E2H.
- -12, if SMMU\_IDR5.VAX indicates support for 52-bit VAs.
- -16, if SMMU\_IDR5.VAX indicates support for 48-bit VAs.

Note: VMSAv9-128 is not supported for StreamWorld any-EL2.

In implementations of SMMUv3.1 and later, a CD is treated as ILLEGAL if it contains a TxSZ value outside the range of these maximum and minimum values.

In SMMUv3.0 implementations, a fetch of a CD containing an out of range value is CONSTRAINED UNPREDICTABLE and has one of the following behaviors:

- The CD becomes ILLEGAL.

- The CD is not ILLEGAL and the Effective value used by the translation is 39 if the programmed value is greater than 39, or 16 if the programmed value is less than 16.

IGNORED if the Effective value of CD.EPD0 == 1.

## TG0, bits [7:6]

TTB0 Translation Granule size, if CD.AA64 selects VMSAv8-64 or VMSAv9-128.

This field is equivalent to TCR\_ELx.TG0 in the A-profile architecture[2].

| TG0   | Meaning   |
|-------|-----------|
| 0b00  | 4KB       |
| 0b01  | 64KB      |
| 0b10  | 16KB      |
| 0b11  | Reserved  |

This field must only select a granule supported by the SMMU, as indicated by SMMU\_IDR5. Use of an unsupported size or Reserved value is ILLEGAL, except this field is IGNORED if the effective value of CD.EPD0 == 1.

Note: The different encoding of CD.TG1 to this field is consistent with the Translation System in the A-profile architecture[2].

If CD.AA64 selects VMSAv8-32 LPAE, this field and CD.TG1 are IGNORED.

## IR0, bits [9:8]

Inner region Cacheability for TTB0 access.

| IR0   | Meaning                                                |
|-------|--------------------------------------------------------|
| 0b00  | Non-cacheable                                          |
| 0b01  | Write-back Cacheable, Read-Allocate, Write-Allocate    |
| 0b10  | Write-through Cacheable, Read-Allocate                 |
| 0b11  | Write-back Cacheable, Read-Allocate, no Write-Allocate |

The only time that translation table entries are written by the SMMU is when HTTU is in use, and because the read effect of the atomic update might cause read allocation of the affected translation table entry into a data cache, it is IMPLEMENTATION DEFINED as to whether 0b01 and 0b11 differ.

Many memory systems might require use of Normal Write-back Cacheable memory for the atomic updates of translation table entries to occur correctly.

If HTTU is enabled and this field is configured to 0b00 or 0b10 , then it is IMPLEMENTATION DEFINED which of the following behaviors occurs for hardware updates of Access flag and dirty state:

- The hardware update occurs correctly as an atomic read-modify-write operation.
- The hardware update occurs, but the read-modify-write operation is not guaranteed to be atomic.
- The hardware update is attempted but fails and generates an F\_WALK\_EABT event.

Arm recommends that software uses 0b01 or 0b11 when HTTU is enabled for this translation table unless the behavior of an implementation is otherwise known.

This field is IGNORED if the effective value of CD.EPD0 == 1.

## OR0, bits [11:10]

Outer region Cacheability for TTB0 access.

| OR0   | Meaning                                                |
|-------|--------------------------------------------------------|
| 0b00  | Non-cacheable                                          |
| 0b01  | Write-back Cacheable, Read-Allocate, Write-Allocate    |
| 0b10  | Write-through Cacheable, Read-Allocate                 |
| 0b11  | Write-back Cacheable, Read-Allocate, no Write-Allocate |

The behavior of this field is otherwise the same as for CD.IR0.

## SH0, bits [13:12]

Shareability for TTB0 access.

| SH0   | Meaning                     |
|-------|-----------------------------|
| 0b00  | Non-shareable               |
| 0b01  | Reserved (behaves as 0b00 ) |
| 0b10  | Outer Shareable             |
| 0b11  | Inner Shareable             |

Note: If both CD.IR0 and CD.OR0 are configured to 0b00 , selecting normal Non-cacheable access, the Shareability of TTB0 access is taken to be OSH regardless of the value of this field.

IGNORED if the effective value of CD.EPD0 == 1.

## EPD0, bit [14]

TTB0 translation table walk disable.

| EPD0   | Meaning                                                                                                                                                                             |
|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | Perform translation table walks using TTB0.                                                                                                                                         |
| 0b1    | A TLB miss on an address that is translated using TTB0 causes a Translation fault. No translation table walk is performed. CD.T0SZ/CD.TG0/CD.IR0/CD.OR0/CD.SH0/CD.TTB0 are IGNORED. |

Consistent with translation in the A-profile architecture[2], this field and CD.EPD1 are IGNORED (and their effective value is 0) if this CD is located from an STE with StreamWorld of any-EL2 or EL3. It is only possible for an EL1 (Secure, Non-secure or Realm) or any-EL2-E2H stream to disable translation table walk using this field or CD.EPD1.

## ENDI, bit [15]

Translation table endianness.

| ENDI   | Meaning       |
|--------|---------------|
| 0b0    | Little Endian |
| 0b1    | Big Endian    |

If the effective values of both CD.EPD0 and CD.EPD1 are 1, this field is IGNORED. Otherwise:

If SMMU\_IDR0.TTENDIAN == 0b10 , it is ILLEGAL to set this field to 1.

If SMMU\_IDR0.TTENDIAN == 0b11 , it is ILLEGAL to set this field to 0.

## T1SZ, bits [21:16]

VA region size covered by TTB1.

This field is equivalent to TCR\_ELx.T1SZ in the A-profile architecture[2].

This field has the same encoding as CD.T0SZ.

IGNORED if the effective value of CD.EPD1 == 1. If StreamWorld == any-EL2 or EL3, this field is RES0.

## TG1, bits [23:22]

TTB1 Translation Granule size.

This field is equivalent to TCR\_ELx.TG1 in the A-profile architecture[2].

| TG1   | Meaning   |
|-------|-----------|
| 0b00  | Reserved  |
| 0b01  | 16KB      |
| 0b10  | 4KB       |
| 0b11  | 64KB      |

This field must only select a granule supported by the SMMU, as indicated by SMMU\_IDR5. Use of an unsupported size or Reserved value is ILLEGAL, except this field is IGNORED if the effective value of CD.EPD1 == 1.

Note: The different encoding of this field to CD.TG0 is consistent with the Translation System in the A-profile architecture[2].

If StreamWorld == any-EL2 or EL3 this field is RES0, otherwise if CD.AA64 selects VMSAv8-32 LPAE, CD.TG0 and this field are IGNORED.

## IR1, bits [25:24]

Inner region Cacheability for TTB1 access.

Same encoding as CD.IR0.

IGNORED if the effective value of CD.EPD1 == 1. If StreamWorld == any-EL2 or EL3 this field is RES0.

## OR1, bits [27:26]

Outer region Cacheability for TTB1 access.

Same encoding as CD.OR0.

IGNORED if the effective value of CD.EPD1 == 1. If StreamWorld == any-EL2 or EL3 this field is RES0.

## SH1, bits [29:28]

Shareability for TTB1 access.

Same encoding as CD.SH0.

IGNORED if the effective value of CD.EPD1 == 1. If StreamWorld == any-EL2 or EL3 this field is RES0.

## EPD1, bit [30]

TTB1 translation table walk disable.

Same encoding as CD.EPD0.

Affects CD.T1SZ/CD.TG1/CD.IR1/CD.OR1/CD.SH1/CD.TTB1.

CD Valid.

| V   | Meaning                                                       |
|-----|---------------------------------------------------------------|
| 0b0 | Invalid - use of the CD by an incoming transaction is ILLEGAL |
| 0b1 | Valid                                                         |

If this field is 0, the entire rest of the structure is IGNORED. An incoming transaction causing a CD with this field configured to 0 to be located from a valid STE is terminated with an abort and a C\_BAD\_CD event is recorded.

## IPS, bits [34:32]

Intermediate Physical address Size.

This field is equivalent to TCR\_ELx.PS in the A-profile architecture[2].

| IPS   | Meaning                                                                                                                                                 |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b000 | 32 bits                                                                                                                                                 |
| 0b001 | 36 bits                                                                                                                                                 |
| 0b010 | 40 bits                                                                                                                                                 |
| 0b011 | 42 bits                                                                                                                                                 |
| 0b100 | 44 bits                                                                                                                                                 |
| 0b101 | 48 bits                                                                                                                                                 |
| 0b110 | In SMMUv3.0 implementations, this value is Reserved and behaves as 0b101 . In implementations of SMMUv3.1 and later, this value selects 52 bits of IPA. |

## V, bit [31]

| IPS   | Meaning                                                                                                                                                                                                                                           |
|-------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b111 | In SMMUv3.0 implementations, this value is Reserved and behaves as 0b101 . In implementations of SMMUv3.1 to SMMUv3.3, this value is Reserved and behaves as 0b110 . In implementations of SMMUv3.4 and later, this value selects 56 bits of IPA. |

Software must not rely on the behavior of Reserved values.

Addresses output from the stage 1 translation table walks through either TTBx table base are range-checked against the effective value of this field, causing a stage 1 Address Size fault if out of range. This means that if the output address of any stage 1 translation has non-zero bits above eff\_IPS , where eff\_IPS is the effective number of IPA bits, an F\_ADDR\_SIZE is recorded. See section 3.4 Address sizes .

This check applies to stage 1 next-level table addresses in Table descriptors, as well as stage 1 output addresses in Block and Page descriptors.

If CD.AA64 selects VMSAv8-32 LPAE, IPS is IGNORED and effective stage 1 output address size of 40 bits is always used. This reflects the 40-bit IPA used in VMSAv8-32 LPAE translations. An Address Size fault occurs if the output address bits [47:40] of a VMSAv8-32 LPAE stage 1 translation table descriptor are programmed as non-zero.

If CD.AA64 selects VMSAv8-64 or VMSAv9-128:

- The effective stage 1 output address size is given by:
- eff\_IPS = MIN(CD.IPS, SMMU\_IDR5.OAS);

The effective IPS size is capped to the OAS.

- Setting this field to any value greater than the cap behaves as though this field equals the cap size. Software must not rely on this behavior.

In SMMUv3.0 addresses are limited to 48 bits.

If CD.AA64 selects VMSAv8-64, an address of 52 bits in size can only be represented in a descriptor when:

- A 64KB granule is in use for that translation table.
- CD.DS == 1.

An address of 56 bits in size can be represented in a descriptor when CD.AA64 selects VMSAv9-128.

Note: In configurations where the effective IPS is larger than the address output from the descriptor, output bits above the address are treated as zero and no Address Size fault can occur.

## AFFD, bit [35]

Access Flag Fault Disable.

When HTTU is not in use because HA == 0 or HTTU is not supported, this flag determines the behavior on access of a stage 1 page whose descriptor has AF == 0:

| AFFD   | Meaning                                                                         |
|--------|---------------------------------------------------------------------------------|
| 0b0    | An Access flag fault occurs (behavior controlled by ARS bits)                   |
| 0b1    | An Access flag fault never occurs. The TTD.AF bit is considered to be always 1. |

If HA == 1, this flag is IGNORED.

Note: Because AFFD == 1 causes a TTD.AF bit to be considered to be 1, a resulting TLB entry will contain AF == 1.

## WXN, bit [36]

Write Execute Never.

This flag controls overall permission of an instruction read to any writable page located using TTB{0,1}:

| WXN   | Meaning                                                     |
|-------|-------------------------------------------------------------|
| 0b0   | Instruction read is allowed as normal                       |
| 0b1   | Instruction read to writable page raises a Permission fault |

## UWXN, bit [37]

Unprivileged Write Execute Never.

This flag controls overall permission of a privileged instruction read to a page marked writable for user privilege that is located through TTB{0,1}:

| UWXN   | Meaning                                                                    |
|--------|----------------------------------------------------------------------------|
| 0b0    | Instruction read is allowed as normal                                      |
| 0b1    | Instruction read from user-writable page raises a stage 1 Permission Fault |

In configurations for which all accesses are considered privileged, for example StreamWorld == any-EL2 or StreamWorld == EL3, this field has no effect and is IGNORED.

If CD.AA64 selects VMSAv9-128, this field is RES0.

If CD.AA64 selects VMSAv8-64, this field is IGNORED.

Note: In VMSAv8-64, all EL0-writable regions are treated as being PXN.

## TBI0, bit [38]

Top Byte Ignore for TTB0.

TBIx affects generation of a Translation fault for addresses having V A[63:56] dissimilar to a sign-extension of VA[55] in the same way as TBI in the A-profile architecture[2].

Note: Refer to section 3.9.1 ATS Interface for additional considerations for use of TBI with PCIe ATS.

## TBI1, bit [39]

Top Byte Ignore for TTB1.

If StreamWorld == any-EL2 or EL3 this field is RES0.

## PAN, bit [40]

Privileged Access Never.

When 1, this field disables data read or data write access by privileged transactions to a virtual address where unprivileged access to the virtual address is permitted at stage 1.

Note: See the A-profile architecture[2] for information on PAN.

Note: When HADx is used, the APTable bits do not affect the permission of a translation.

Privileged transactions are those configured through an STE with STE.PRIVCFG == Privileged, or an STE with STE.PRIVCFG == 'Use Incoming' and marked as Privileged by the client device.

This field is IGNORED when StreamWorld == any-EL2 or StreamWorld == EL3 and PAN is effectively 0.

## AA64, bit [41]

Translation table format for both TTB0 and TTB1.

| AA64   | Meaning                                | Applies when          |
|--------|----------------------------------------|-----------------------|
| 0b0    | Use VMSAv8-32 LPAE descriptor formats. | SMMU_IDR0.TTF[0] == 1 |
| 0b0    | Use VMSAv9-128 descriptor formats.     | SMMU_IDR5.D128 == 1   |
| 0b1    | Use VMSAv8-64 descriptor formats.      |                       |

Note: This is consistent with the A-profile architecture[2], where use of 128-bit descriptors is supported for EL2&amp;0 translation regimes but not for EL2 translation regimes.

The behaviour of this field if SMMU\_IDR5.D128 == 1 is equivalent to TCR(2)\_ELx.D128 in the A-profile architecture[2], with reversed polarity.

It is ILLEGAL to select VMSAv8-32 LPAE tables when either:

- VMSAv8-32 LPAE tables are not supported (SMMU\_IDR0.TTF[0] == 0)
- StreamWorld == any-EL2-E2H or S-EL2 or EL3.

It is ILLEGAL to select VMSAv8-64 tables when either:

- VMSAv8-64 tables are not supported (SMMU\_IDR0.TTF[1] == 0)
- Stage 2 translates (STE.Config == 0b11x ) and STE.S2AA64 selects VMSAv8-32.
- -Note: Consistent with the VMSA in the A-profile architecture[2], a 64-bit stage 1 is not supported on a 32-bit stage 2.

Note: When VMSAv8-64 is selected, the IPS field selects a variable output address size, the translation granule can be altered, HTTU can be enabled and page permissions are interpreted differently, see the other fields for details.

It is ILLEGAL to select VMSAv9-128 tables if any of the following are true:

- StreamWorld is EL2. Configuring stage 1 to use VMSAv9-128 tables is permitted if StreamWorld is EL2-E2H in the SMMU, as configured in SMMU\_(*\_)CR2.E2H and STE.{Config, STRW}.
- STE.S1PIE is 0.

This field is permitted to be cached in a TLB.

## HD, bit [42]

Hardware Translation Table Update of Dirty flags for CD.TTB0 and CD.TTB1.

See definition of HA.

## HA, bit [43]

Hardware Translation Table Update of Access flags for CD.TTB0 and CD.TTB1.

When combined with CD.HD as {HD, HA}:

- 0b00 : HTTU disabled.
- 0b01 : Update of Access flag enabled.
- 0b10 : Reserved. If CD.HD == 1 is not ILLEGAL, behaves as though this field is 0 and CD.HD is 0.
- 0b11 : Update of Access flag and dirty state of the page enabled.

These flags are IGNORED if CD.AA64 selects VMSAv8-32 LPAE.

Otherwise:

- It is ILLEGAL to set HA if SMMU\_IDR0.HTTU == 0b00 .
- It is ILLEGAL to set HD if SMMU\_IDR0.HTTU == 0b00 or 0b01 .

Note: If HTTU is enabled when ORx or IRx indicate Non-cacheable memory, behavior is IMPLEMENTATION DEFINED, see 3.15 Coherency considerations and memory access types . Some systems might only be able to perform atomic updates using normal cacheable memory. Incompatible attributes might cause HTTU not to be performed but system integrity must be maintained as a CD might be under control of a malicious VM.

Stage 1 fault behavior.

See section 5.5 Fault configuration (A, R, S bits) for a description of fault configuration.

Stage 1 fault behavior.

See section 5.5 Fault configuration (A, R, S bits) for a description of fault configuration.

Stage 1 fault behavior.

See section 5.5 Fault configuration (A, R, S bits) for a description of fault configuration.

## ASET, bit [47]

ASID Set.

Selects type for ASID, between sets shared and non-shared with PE ASIDs. This flag affects broadcast TLB invalidation participation and the scope within which Global TLB entries are matched:

| ASET   | Meaning                                                                                                                                                                                                                                                                                                                    |
|--------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | ASID in shared set: This ASID, and address space described by CD.TTB0 and CD.TTB1, are shared with that of a process on the PE. All matching broadcast invalidation messages will invalidate TLB entries created from this context (where supported and globally enabled), keeping SMMUand PE address spaces synchronized. |
| 0b1    | ASID in non-shared set: TLB entries created from this context are not expected to be invalidated by some broadcast invalidations as described in section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .                                                                                   |

## S, bit [44]

## R, bit [45]

## A, bit [46]

## Bit [65]

For invalidation by ASID scope such entries require SMMU invalidation commands to be issued. This ASID represents an SMMU-local address space, not shared with PE processes, therefore broadcast invalidation from a coincidentally matching ASID is irrelevant to this address space. Use of ASET == 1 might avoid over-invalidation and improve performance.

Note: All other broadcast TLB invalidations, except for those listed here, are expected to affect matching TLB entries created when ASET == 1. For example, TLBI VMALLE1IS must invalidate all TLB entries matching a given VMID, regardless of ASET.

ASET must be included in any Global cached translations inserted using a CD reached through an STE with StreamWorld == NS-EL1 or Secure or any-EL2-E2H. In these StreamWorlds, ASET is also intended (but not required) to be included in non-Global translations to allow them to opt-out of broadcast invalidation.

Changes to a the ASET of a CD or the ASID, or both, are not automatically reflected in cached translations. Arm recommends that these are subjected to separate TLB maintenance.

ASET is permitted to be included in cached translations inserted using a CD reached through an STE with StreamWorld == any EL2 or EL3.

## ASID, bits [63:48]

Address Space Identifier.

See ASET field. Tag for TLB entries inserted due to translations from this CD, differentiating them from translations with the same V A from different address spaces.

ASID must tag all cached translations inserted using this CD through an STE with StreamWorld == NS-EL1 or Secure or any-EL2-E2H.

This field is IGNORED if StreamWorld == any-EL2 or EL3. Otherwise, when an implementation supports only 8-bit ASIDs (SMMU\_IDR0.ASID16 == 0), it is ILLEGAL for ASID[15:8] to be non-zero.

If 16-bit ASIDs are supported by an implementation, the full ASID[15:0] value is used regardless of CD.AA64. Arm expects that legacy/AArch32 software using 8-bit ASIDs will write zero-extended 8-bit values in the ASID field in this case.

## NSCFG0, bit [64]

Non-secure attribute for the memory associated with the starting-level translation table to which CD.TTB0 points.

| NSCFG0   | Meaning                                                              |
|----------|----------------------------------------------------------------------|
| 0b0      | Starting-level descriptor of CD.TTB0 is fetched using NS == 0 access |
| 0b1      | Starting-level descriptor of CD.TTB0 is fetched using NS == 1 access |

This field is used only when the CD is reached from a Secure STE and is otherwise IGNORED.

## When SMMU\_IDR5.D128 == 1:

## DisCH0, bit [65]

Disable the Contiguous bit for the initial level of walk for CD.TTB0.

This field is equivalent to TCR(2)\_ELx.DisCH0 in the A-profile architecture[2].

| DisCH0   | Meaning                                                                                       |
|----------|-----------------------------------------------------------------------------------------------|
| 0b0      | No effect on the Contiguous bit.                                                              |
| 0b1      | The Contiguous bit in Block or Page descriptors at the initial level of walk is treated as 0. |

The interpretation of this field only applies if CD.AA64 selects VMSAv9-128.

If CD.EPD0 is 1, this field is IGNORED.

This field is permitted to be cached in a TLB.

## Otherwise:

## HAD0, bit [65]

Hierarchical Attribute Disable for the CD.TTB0 region.

| HAD0   | Meaning                               |
|--------|---------------------------------------|
| 0b0    | Hierarchical attributes are enabled.  |
| 0b1    | Hierarchical attributes are disabled. |

The presence of this feature can be determined from SMMU\_IDR3.HAD; if SMMU\_IDR3.HAD == 0, this field and CD.HAD1 are IGNORED. Otherwise:

When this field is 1, the APTable, PXNTable and XNTable/UXNTable fields of table descriptors walked through CD.TTB0 become IGNORED, might be used by software for any purpose and do not affect translation. When StreamWorld == any-EL2 or EL3, this effect includes the APTable[0] and PXNTable bits which are otherwise Reserved by VMSA in these translation regimes.

This field and CD.HAD1 are supported for both VMSAv8-32 LPAE and VMSAv8-64 translation tables.

## E0PD0, bit [66]

Disable unprivileged access to addresses translated by CD.TTB0.

When an access is prevented by the E0PD mechanism, the event is reported as a Translation Fault, F\_TRANSLATION.

This field is equivalent to TCR\_ELx.E0PD0 in the A-profile architecture[2].

Note: Consistent with FEAT\_E0PD in the A-profile architecture[2], Arm expects that the fault should take the same time to generate, whether the address is present in the TLB or not, to mitigate attacks that use fault timing.

E0PD only applies to VMSAv8-64 translation regimes with StreamWorld configured as EL1, Secure or any-EL2-E2H.

| E0PD0   | Meaning                                                                                              |
|---------|------------------------------------------------------------------------------------------------------|
| 0b0     | Unprivileged access to any address translated by CD.TTB0 will not generate a fault by this mechanism |
| 0b1     | Unprivileged access to any address translated by CD.TTB0 will generate a Translation fault           |

If SMMU\_IDR3.E0PD == 0 this field is RES0.

If CD.AA64 selects VMSAv8-32 LPAE or if StreamWorld is EL3 or any-EL2, this field is RES0.

This field is permitted to be cached in a TLB.

## HAFT, bit [67]

Enable hardware update of Access flag in Table descriptors.

| HAFT   | Meaning                |
|--------|------------------------|
| 0b0    | Stage 1 HAFT disabled. |
| 0b1    | Stage 1 HAFT enabled.  |

If CD.HA is 0 and not IGNORED, it is ILLEGAL to set this field to 1 and this results in C\_BAD\_CD.

This field is permitted to be cached in a TLB.

If SMMU\_IDR0.HTTU != 0b11 this field is RES0.

## TTB0, bits [119:68]

In SMMUv3.1 and later, if CD.AA64 selects VMSAv9-128, then bits[119:68] represent the address of the TT0 base, bits[55:4]. Otherwise:

- In SMMUv3.1 and later:
- -Bits[115:68] represent the address of the TT0 base, bits[51:4].
- -Bits[119:116] are RES0.
- In SMMUv3.0:
- -Bits[111:68] represent the address of the TT0 base, bits[47:4].
- -Bits[119:112] are RES0.

Address bits above and below the field range are implied as zero.

Bits [(x-1):0] are treated as if all the bits are zero, where x is defined by the required alignment of the translation table as given by the VMSA in the A-profile architecture[2].

Note: The SMMU effectively aligns the value in this field before use.

If CD.AA64 selects VMSAv8-64, then a 64-byte minimum alignment on starting-level translation table addresses is imposed when the effective IPS value indicates 52-bit output. In this case bits [5:0] are treated as zero.

If CD.AA64 selects VMSAv9-128, then a 32-byte minimum alignment on starting-level translation table addresses is imposed regardless of the effective IPS value. In this case bits [4:0] are treated as zero.

If the effective value of CD.EPD0 == 1, this field is IGNORED. Otherwise, it is ILLEGAL for the address in this field to be outside the range described by the CD's effective IPS value. In addition, it is ILLEGAL for the address in this field to be outside of a 48-bit range when CD.DS == 0, CD.AA64 selects VMSAv8-64 and CD.TG0 selects a granule smaller than 64KB.

## Bits [121:120]

Reserved, RES0.

## PnCH, bit [122]

Stage 1 Protected attribute enable.

This field is equivalent to TCR(2)\_ELx.PnCH in the A-profile architecture[2].

| PnCH   | Meaning                       |
|--------|-------------------------------|
| 0b0    | Protected attribute disabled. |
| 0b1    | Protected attribute enabled.  |

If CD.AA64 selects VMSAv9-128, then this field is RES0. If VMSAv9-128 is selected, the functionality of this field is implicitly enabled, however, the Contiguous bit disable property of this field does not apply. If CD.AA64 selects VMSAv8-32 LPAE, then this field is RES0.

If SMMU\_IDR3.THE == 0 this field is RES0.

See also:

- 3.27.1 Protected attribute .
- 3.27.2 AssuredOnly permission checks .

This field is permitted to be cached in a TLB.

## EPAN, bit [123]

Control for Enhanced PAN mechanism.

| EPAN   | Meaning                                                                                                                                                                                                                                                                                                                                          |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0    | When CD.PAN == 1, a privileged data access to a page with stage 1 unprivileged data access permission generates F_PERMISSION as a result of the Privileged Access Never mechanism.                                                                                                                                                               |
| 0b1    | When CD.PAN == 1, a privileged data access to a page with stage 1 unprivileged data or stage 1 unprivileged instruction access permission generates F_PERMISSION as a result of the Privileged Access Never mechanism. Any data access, including speculative accesses, that is prevented by CD.PAN == 1 will not cause allocation into a cache. |

If any of the following are true this field is RES0:

- CD.AA64 selects VMSAv8-32 LPAE.
- StreamWorld is any-EL2 or EL3.
- Stage 1 permission indirection is enabled. Note: If stage 1 permission indirection is enabled, and CD.PAN is 1, the PAN check behaves as though this field is also 1. See section 3.26.1 Stage 1 permission indirections .

If SMMU\_IDR3.EPAN == 0 this field is RES0.

This field is permitted to be cached in a TLB.

## HWU059, bit [124]

If SMMU\_IDR3.PBHA == 1 and CD.HAD0 == 1, this field controls the interpretation of bit [59] of the stage 1 translation table final-level (page or block) descriptor pointed at by CD.TTB0:

| HWU059   | Meaning                                                                        |
|----------|--------------------------------------------------------------------------------|
| 0b0      | Bit [59] is not interpreted by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1      | Bit [59] has IMPLEMENTATION DEFINED hardware use.                              |

## Bit [129]

This field is IGNORED when PBHA are not supported (SMMU\_IDR3.PBHA == 0) or when CD.HAD0 == 0. If CD.AA64 selects VMSAv9-128, this field is RES0.

In SMMUv3.0 this field is RES0.

## HWU060, bit [125]

Similar to CD.HWU059, but affecting descriptor bit [60].

## Bits [127:126]

## When SMMU\_IDR5.D128 == 1:

## SKL0, bits [127:126]

Skip Level configuration for initial lookup for stage 1 translations using TTB0.

This field is equivalent to TTBR0\_ELx.SKL in the A-profile architecture[2].

| SKL0   | Meaning        |
|--------|----------------|
| 0b00   | Skip 0 levels. |
| 0b01   | Skip 1 level.  |
| 0b10   | Skip 2 levels. |
| 0b11   | Skip 3 levels. |

The interpretation of this field only applies if CD.AA64 selects VMSAv9-128.

If CD.EPD0 is 1, this field is IGNORED.

This field is permitted to be cached in a TLB.

## Otherwise:

## HWU0&lt;x&gt;, bits [127:126]

HWU062 and HWU061.

Similar to CD.HWU059, but affecting descriptor bits [62, 61].

## NSCFG1, bit [128]

Non-secure attribute for the memory associated with the starting-level translation table to which CD.TTB1 points. See CD.NSCFG0.

If StreamWorld == any-EL2 or EL3 this field is RES0.

## When SMMU\_IDR5.D128 == 1:

## DisCH1, bit [129]

Disable the Contiguous bit for the initial level of walk for CD.TTB1.

This field is equivalent to TCR(2)\_ELx.DisCH1 in the A-profile architecture[2].

| DisCH1   | Meaning                                                                                       |
|----------|-----------------------------------------------------------------------------------------------|
| 0b0      | No effect on the Contiguous bit.                                                              |
| 0b1      | The Contiguous bit in Block or Page descriptors at the initial level of walk is treated as 0. |

The interpretation of this field only applies if CD.AA64 selects VMSAv9-128.

If StreamWorld is EL3 or any-EL2, this field is RES0.

If CD.EPD1 is 1, this field is IGNORED.

This field is permitted to be cached in a TLB.

## Otherwise:

## HAD1, bit [129]

Hierarchical Attribute Disable for the CD.TTB1 region.

| HAD1   | Meaning                              |
|--------|--------------------------------------|
| 0b0    | Hierarchical attributes are enabled  |
| 0b1    | Hierarchical attributes are disabled |

If SMMU\_IDR3.HAD == 1, this field is RES0 if StreamWorld == any-EL2 or EL3.

## E0PD1, bit [130]

Disable unprivileged access to addresses translated by CD.TTB1.

When an access is prevented by the E0PD mechanism, the event is reported as a Translation Fault, F\_TRANSLATION.

This field is equivalent to TCR\_ELx.E0PD1 in the A-profile architecture[2].

Note: Consistent with FEAT\_E0PD in the A-profile architecture[2], Arm expects that the fault should take the same time to generate, whether the address is present in the TLB or not, to mitigate attacks that use fault timing.

E0PD only applies to VMSAv8-64 translation regimes with StreamWorld configured as EL1, Secure or any-EL2-E2H.

| E0PD1   | Meaning                                                                                              |
|---------|------------------------------------------------------------------------------------------------------|
| 0b0     | Unprivileged access to any address translated by CD.TTB1 will not generate a fault by this mechanism |
| 0b1     | Unprivileged access to any address translated by CD.TTB1 will generate a Translation fault           |

If SMMU\_IDR3.E0PD == 0 this field is RES0.

If CD.AA64 selects VMSAv8-32 LPAE or if StreamWorld is EL3 or any-EL2, this field is RES0.

This field is permitted to be cached in a TLB.

## AIE, bit [131]

Enable stage 1 attribute extension.

| AIE   | Meaning                                  |
|-------|------------------------------------------|
| 0b0   | Stage 1 attribute extension is disabled. |
| 0b1   | Stage 1 attribute extension is enabled.  |

If SMMU\_IDR3.AIE is 0, this field is RES0.

For more information see CD.{MAIR0, MAIR1}.

This field is permitted to be cached in a TLB.

## TTB1, bits [183:132]

In SMMUv3.1 and later, if CD.AA64 selects VMSAv9-128, then bits[183:132] represent the address of the TT1 base, bits[55:4]. Otherwise:

- In SMMUv3.1 and later:
- -Bits[179:132] represent the address of the TT1 base, bits[51:4].
- -Bits[183:180] are RES0.
- In SMMUv3.0:
- -Bits[175:132] represent the address of the TT1 base, bits[47:4].
- -Bits[183:176] are RES0.

Address bits above and below the field range are implied as zero.

See the notes below about when CD.TTB1 might be valid.

Bits [(x-1):0] are treated as if all the bits are zero, where x is defined by the required alignment of the translation table as given by the VMSA in the A-profile architecture[2].

Note: The SMMU effectively aligns the value in this field before use.

If CD.AA64 selects VMSAv8-64, then a 64-byte minimum alignment on starting-level translation table addresses is imposed when the effective IPS value indicates 52-bit output. In this case bits [5:0] are treated as zero.

If CD.AA64 selects VMSAv8-128, then a 32-byte minimum alignment on starting-level translation table addresses is imposed regardless of the effective IPS value. In this case bits [4:0] are treated as zero.

If StreamWorld == any-EL2 or EL3 this field is RES0, otherwise if the effective value of CD.EPD1 == 1, this field is IGNORED. Otherwise, it is ILLEGAL for the address in this field to be outside the range described by the effective IPS value of the CD. In addition, it is ILLEGAL for the address in this field to be outside of a 48-bit range when CD.DS == 0, CD.AA64 selects VMSAv8-64 and CD.TG1 selects a granule smaller than 64KB.

## Bits [185:184]

Reserved, RES0.

## DS, bit [186]

Enable 52-bit input and output address size when using 4KB and 16KB granules.

| DS   | Meaning                                                         |
|------|-----------------------------------------------------------------|
| 0b0  | 52-bit address sizes when using 4KB and 16KB granules disabled. |

## PIE, bit [187]

Stage 1 permission indirection enable.

This field is equivalent to TCR(2)\_ELx.PIE in the A-profile architecture[2].

| PIE   | Meaning                                                              |
|-------|----------------------------------------------------------------------|
| 0b0   | Use permissions directly from stage 1 translation table descriptors. |
| 0b1   | Use stage 1 Indirect Permission Scheme.                              |

If any of the following conditions are true this field is RES0:

- SMMU\_IDR3.S1PI is 0.
- STE.S1PIE is 0.
- CD.AA64 selects VMSAv9-128. Stage 1 permission indirection is implicitly enabled.
- CD.AA64 selects VMSAv8-32. Stage 1 permission indirection is not supported.

This field is permitted to be cached in a TLB.

## HWU159, bit [188]

If SMMU\_IDR3.PBHA == 1 and CD.HAD1 == 1, this field controls the interpretation of bit [59] of the Stage 1 translation table final-level (page or block) descriptor pointed at by CD.TTB1:

| HWU159   | Meaning                                                                        |
|----------|--------------------------------------------------------------------------------|
| 0b0      | Bit [59] is not interpreted by hardware for an IMPLEMENTATION DEFINED purpose. |
| 0b1      | Bit [59] has IMPLEMENTATION DEFINED hardware usage.                            |

This field is IGNORED when PBHA are not supported (SMMU\_IDR3.PBHA == 0) or when CD.HAD1 == 0.

| DS   | Meaning                                                        |
|------|----------------------------------------------------------------|
| 0b1  | 52-bit address sizes when using 4KB and 16KB granules enabled. |

This field affects both the input and output address sizes, as follows:

- The effect of this field on the interpretation of stage 1 translation table descriptors is the same as for the TCR\_ELx.DS bit as specified in FEAT\_LPA2 in the A-profile architecture[2].
- The effect of this field on the determination of whether the CD.TxSZ fields are configured to out-of-range values is the same as for the TCR\_ELx.DS bit specified in FEAT\_LPA2 in the A-profile architecture[2].

If this field is 1 and CD.TGx selects 4KB or 16KB, then the Shareability attribute for a Cacheable location translated by tables pointed to by CD.TTBx is taken from CD.SHx.

If any of the following are true this field is RES0:

- SMMU\_IDR5.DS == 0.
- CD.AA64 selects VMSAv9-128.
- CD.AA64 selects VMSAv8-32 LPAE.
- StreamWorld == EL1 or EL2-E2H, and both CD.TG0 and CD.TG1 select 64KB.
- StreamWorld == EL2 or EL3, and CD.TG0 selects 64KB.

In SMMUv3.0 this field is RES0.

## HWU160, bit [189]

Similar to CD.HWU159, but affecting descriptor bit [60].

## Bits [191:190]

## When SMMU\_IDR5.D128 == 1:

## SKL1, bits [191:190]

Skip Level configuration for initial lookup for stage 1 translations using TTB1.

This field is equivalent to TTBR1\_ELx.SKL in the A-profile architecture[2].

| SKL1   | Meaning        |
|--------|----------------|
| 0b00   | Skip 0 levels. |
| 0b01   | Skip 1 level.  |
| 0b10   | Skip 2 levels. |
| 0b11   | Skip 3 levels. |

The interpretation of this field only applies if CD.AA64 selects VMSAv9-128.

Otherwise behaves the same as CD.SKL0, but for translations using TTB1.

If StreamWorld is EL3 or any-EL2, this field is RES0.

If CD.EPD1 is 1, this field is IGNORED.

This field is permitted to be cached in a TLB.

## Otherwise:

## HWU1&lt;x&gt;, bits [191:190]

HWU162 and HWU161.

Similar to HWU159, but affecting descriptor bits [62, 61].

## MAIR0, bits [223:192]

Memory Attribute Indirection Register 0, bits[31:0].

## MAIR1, bits [255:224]

Memory Attribute Indirection Register 1, bits[31:0].

Equivalent to the A-profile architecture[2] Memory Attribute Indirection Registers, the MAIR0 and MAIR1 fields are indexed by AttrIndx in descriptors fetched from TTB0 &amp; TTB1 and contain attributes encoded in the same way as in Arm VMSAv8-64 MAIR registers with the following exceptions:

All encodings defined as UNPREDICTABLE in VMSAv8-64 are Reserved in this architecture, and behave as follows:

| Attr<n>[3:0]           | If Attr<n>[7:4] == 0b0000          | If Attr<n>[7:4] != 0b0000                              |
|------------------------|------------------------------------|--------------------------------------------------------|
| 0b0000                 | Same as VMSAv8-64                  | Reserved, behaves as Normal-iWT Transient withRW= 0b11 |
| 0b00RW where RW!= 0b00 | Reserved, behaves as Device-nGnRnE | Same as VMSAv8-64                                      |
| 0b01RW where RW!= 0b00 | Reserved, behaves as Device-nGnRE  | Same as VMSAv8-64                                      |
| 0b10RW where RW!= 0b00 | Reserved, behaves as Device-nGRE   | Same as VMSAv8-64                                      |
| 0b11RW where RW!= 0b00 | Reserved, behaves as Device-GRE    | Same as VMSAv8-64                                      |

Note: The encoding 0b11110000 , 'Tagged Normal Memory' in the A-profile architecture[2] is not supported in SMMUv3.

MAIR, as referenced in the table below, is the concatenation of {CD.MAIR1, CD.MAIR0} as a 64-bit value. If SMMU\_IDR3.AIE is 0 or CD.AIE is 0, then MAIR is indexed by AttrIndx[2:0] from stage 1 Block or Page descriptors. If SMMU\_IDR3.AIE is 1 and CD.AIE is 1 then MAIR is indexed by AttrIndx[3:0] as follows:

| AttrIndx[3:0]   | MAIR output          |
|-----------------|----------------------|
| 7 >= x >= 0     | Bits [(8*x)+7 : 8*x] |
| x>7             | Bits [63:56]         |

Consistent with the A-profile architecture[2], AttrIndx[3] is derived as follows:

- If CD.AA64 selects VMSAv8-64, then AttrIndx[3] is bit [59] of Block and Page descriptors.
- If CD.AA64 selects VMSAv9-128, then AttrIndx[3] is bit [5] of Block and Page descriptors.

## AMAIR0, bits [287:256]

Auxiliary Memory Attribute Indirection Register 0, bits[31:0].

## AMAIR1, bits [319:288]

Auxiliary Memory Attribute Indirection Register 1, bits[31:0].

Equivalent to PE Auxiliary Memory Attribute Indirection Registers. The content of the AMAIR{1,0} fields is IMPLEMENTATION DEFINED and might enable extended functionality.

If software has no IMPLEMENTATION SPECIFIC knowledge it must set the AMAIR{1,0} fields to zero. An implementation must remain compatible with generic driver software by maintaining correct behavior when the AMAIR is set to zero.

If SMMU\_IDR3.AIE is 0 or CD.AIE is 0, then in a typical implementation, the AMAIR{1,0} fields are split into eight one-byte fields indexed by the AttrIndx[2:0] field from stage 1 Block or Page descriptors but this is not required. If SMMU\_IDR3.AIE is 1 and CD.AIE is 1 then AMAIR is indexed by AttrIndx[3:0] from stage 1 Block or Page descriptors as follows: Note: AMAIR, as referenced in the table below, is the concatenation of {CD.AMAIR1, CD.AMAIR0} as a 64-bit value.

| AttrIndx[3:0]   | AMAIR output         |
|-----------------|----------------------|
| 7 >= x >= 0     | Bits [(8*x)+7 : 8*x] |
| x>7             | Bits [63:56]         |

Consistent with the A-profile architecture[2], AttrIndx[3] is derived as follows:

- If CD.AA64 selects VMSAv8-64, then AttrIndx[3] is bit [59] of Block and Page descriptors.
- If CD.AA64 selects VMSAv9-128, then AttrIndx[3] is bit [5] of Block and Page descriptors.

## IMPLEMENTATION DEFINED, bits [351:320]

IMPLEMENTATION DEFINED, for example QoS, allocation, or transient hints for translation table access.

## PARTID, bits [367:352]

MPAM Partition ID.

If MPAM is not supported in the corresponding Security state, or if STE.S1MPAM == 0, this field is RES0. Otherwise:

When STE.Config == 0b111 and STE.S1MPAM == 1, PARTID[4:0] is the 5-bit virtual PARTID used for client transactions. Bits [15:5] are RES0. The virtual ID is translated to a physical ID using the VMS.PARTID\_MAP structure.

When STE.Config == 0b101 and STE.S1MPAM == 1, this field is the physical PARTID used for client transactions. In this configuration, this field is interpreted as having an UNKNOWN value if it is configured with a value greater than the corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX.

The corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX is chosen as follows:

- For a Non-secure Stream, then SMMU\_MPAMIDR.PMG\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0 or STE.MPAM\_NS == 0, then SMMU\_S\_MPAMIDR.PMG\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and STE.MPAM\_NS == 1, then SMMU\_MPAMIDR.PMG\_MAX.

See Chapter 17 Memory System Resource Partitioning and Monitoring for more information on use of this field.

## PMG, bits [375:368]

MPAM Performance Monitor Group.

If MPAM is not supported in the corresponding Security state or if STE.S1MPAM == 0, this field is RES0.

This field is interpreted as having an UNKNOWN value if it is configured with a value greater than the corresponding SMMU\_(*\_)MPAMIDR.PMG\_MAX.

The corresponding SMMU\_(*\_)MPAMIDR.PMG\_MAX is chosen as follows:

- For a Non-secure Stream, then SMMU\_MPAMIDR.PMG\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0 or STE.MPAM\_NS == 0, then SMMU\_S\_MPAMIDR.PMG\_MAX.
- For a Secure Stream, if SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1 and STE.MPAM\_NS == 1, then SMMU\_MPAMIDR.PMG\_MAX.

See Chapter 17 Memory System Resource Partitioning and Monitoring for more information on use of this field.

## Bits [383:376]

Reserved, RES0.

## PIIU&lt;p&gt; , bits [3p+386:3p+384], for p = 15 to 0

The set of 16 stage 1 Unprivileged base permission interpretations.

This field is indexed by the PIIndex value derived from a stage 1 Block or Page descriptor, as PIIU[(PIIndex*3)+2 : PIIndex*3], to give a permission interpretation.

| PIIU<p>   | Meaning             |
|-----------|---------------------|
| 0b000     | No Access.          |
| 0b001     | Read-only.          |
| 0b010     | Execute-only.       |
| 0b011     | Read-execute.       |
| 0b101     | Read-write.         |
| 0b111     | Read-write-execute. |

All other values are reserved, and treated as C\_BAD\_CD.

If StreamWorld is EL3 or any-EL2, this field is RES0.

Note: The encoding of this field is different from the encoding of the Perm field in the PIRE0\_ELx registers in the A-profile architecture[2].

If stage 1 permission indirection is disabled, this field is RES0.

This field is permitted to be cached in a TLB.

## Bits [447:432]

Reserved, RES0.

## PIIP&lt;p&gt; , bits [3p+450:3p+448], for p = 15 to 0

The set of 16 stage 1 Privileged base permission interpretations.

This field is indexed by the PIIndex value derived from a stage 1 Block or Page descriptor, as PIIP[(PIIndex*3)+2 : PIIndex*3], to give a permission interpretation.

| PIIP<p>   | Meaning             |
|-----------|---------------------|
| 0b000     | No Access.          |
| 0b001     | Read-only.          |
| 0b010     | Execute-only.       |
| 0b011     | Read-execute.       |
| 0b101     | Read-write.         |
| 0b111     | Read-write-execute. |

All other values are reserved, and treated as C\_BAD\_CD.

If PIIP[x] grants Privileged execute permission, and CD.PIIU[x] is not RES0 and grants Unprivileged write permission, this is ILLEGAL and results in C\_BAD\_CD.

Note: The encoding of this field is different from the encoding of the Perm field in the PIR\_ELx registers in the A-profile architecture[2].

If stage 1 permission indirection is disabled, this field is RES0.

This field is permitted to be cached in a TLB.

## Bits [511:496]

Reserved, RES0.

## 5.4.1 CD notes

Note: Consistent with Armv8.1 [2] PE translation, translation table descriptor bits APTable, PXNTable and UXNTable control hierarchical permission attributes for lower levels of translation table walks. Not all systems use this feature, so the CD Hierarchical Attribute Disable flags allow translation table walks using TTB0 and TTB1 to be performed ignoring these bits. Software is then free to use the APTable, PXNTable and UXNTable fields for other purposes.

When a CD is used from a stream configured with StreamWorld == any-EL2 or EL3 (but not any-EL2-E2H):

- Only one translation table is supported (TTB0) and TTB1 is unreachable.
- ASID is IGNORED.

When TTB1 is unreachable:

- The following fields become RES0:

TTB1, TBI[1], TG1, SH1, OR1, IR1, T1SZ, HAD1, NSCFG1.

- T0SZ must cover the required VA input space

A CD must only be configured to be located through a set of multiple STEs when all STEs in the set configure an identical Exception level (given by the STE StreamWorld).

Note: For example, one STE configuring a stream as NS-EL2 and another STE configuring a stream as NS-EL1 must not both share the same CD as, in this configuration, TTB1 is both enabled and unused depending on the StreamID that locates the CD. Similarly, a CD with AA64 == 0 is ILLEGAL if reached from an STE with StreamWorld == any-EL2-E2H but not if reached from an STE with StreamWorld == NS-EL1 or Secure.

The legality of a CD is, in part, affected by following properties of the STE used to locate the CD:

- StreamWorld.
- S1STALLD.
- AA64 and Config[1] (to detect VMSAv8-32 LPAE stage 2 translation).

When a CD is reached from an STE whose state causes the CD to be considered ILLEGAL, C\_BAD\_CD is raised and the transaction causing the configuration lookup is terminated with an abort.

When using the Direct Permission Scheme at stage 1, the interpretation of the lower bit of the translation table descriptor AP[2:1] field changes depending on the translation regime under which the table is walked, Translation tables located from STEs with StreamWorld == any-EL2 or EL3 are under EL2 or EL3 AArch64 state ownership and, consistent with Armv8-A PEs, the AP[1] bit (of AP[2:1]) is ignored and treated as 1, see section 13.4.1 Stage 1 page permissions .

Depending on the presentation of an address to the SMMU, TTB1 might never be selected in some implementations, see section 3.4.1 Input address size and Virtual Address size for details.

In Armv8-A, an inconsistency between TTBRx and IPS is reported as an Address Size fault. A CD TTBx address outside the range of IPS makes the CD ILLEGAL, recording a C\_BAD\_CD error.

ACDorL1CDthat is successfully fetched might be cached in any state, therefore any modification, commissioning or decommissioning of a CD must be followed by a CMD\_CFGI\_CD command to make the modification visible to the SMMU. A failed fetch (F\_CD\_FETCH, or a stage 2 fault where CLASS == CD) does not cause a CD or L1CD to be cached.

The translation table walks performed from TTB0 or TTB1 are always performed in IPA space if stage 2 translations are enabled (STE.Config == 0b11x ). If stage 2 translations are not enabled (or if the SMMU does not implement stage 2), translation table walks are always performed in PA space. CDs are fetched from IPA space if stage 2 translations are enabled, otherwise they are fetched from PA space.

Note: This enables a hypervisor to point directly to guest-managed CD structures and translation tables.

The following CD fields are permitted to be cached as part of a translation or TLB entry, and alteration requires invalidation of any TLB entry that might have cached these fields, in addition to CD structure cache invalidation:

- HAD{0,1}.
- AFFD.
- ASID+ASET (affect tagging of TLB entries, so a change may not require old entries to be invalidated).
- MAIR.
- AMAIR.
- EPD{0,1}.
- TTB{0,1}.
- T{0,1}SZ.
- OR{0,1}.
- IR{0,1}.
- SH{0,1}.
- ENDI.
- TG{0,1}.
- HA, HD.
- WXN, UWXN.
- AA64.
- TBI.
- IPS.
- NSCFG{0,1}.
- PAN.
- EPAN.
- PnCH.
- PIE.
- PIIP.
- PIIU.
- DisCH0.
- DisCH1.
- SKL0.
- SKL1.
- AIE.
- HAFT.

Alteration of the remaining fields of the CD does not require an explicit invalidation of any structure other than the CD itself:

## • A,R,S

The PARTID and PMG fields are not permitted to be cached in a TLB entry and these fields are permitted to differ between CDs having the same ASID value within the same VMID.

Note: Changes to IMPLEMENTATION DEFINED fields might have IMPLEMENTATION DEFINED invalidation requirements.

When cached in an SMMU, a CD is uniquely identified by the tuple {StreamID, SubstreamID} including the qualification of StreamID by SEC\_SID. This means that:

- Multiple CDs are distinguished by StreamID, so CDs located from the same SubstreamID index but through different StreamIDs are considered separate and can contain different configuration:
- -Note: Different devices (StreamIDs) might therefore use the same SubstreamID value to associate transactions with different process address spaces in an OS. The SubstreamID namespace is local to the StreamID.
- A common CD (or CD table) shared by different STEs is permitted to be cached as multiple entries that are specific to each possible {StreamID, SubstreamID} combination.

- -A change to such a CD requires invalidation of the CD cache. When CMD\_CFGI\_CD(\_ALL) is used, it must be issued multiple times for every {StreamID, SubstreamID} combination that the CD is reachable from.
- -Note: The SMMU might prefetch a reachable structure, so even if a CD was not accessed by a transaction with a particular StreamID, it might have been prefetched through the STE of that stream, so must still be invalidated using that StreamID.

It might arise that multiple CDs represent the same address space (therefore TLB entries), as identified by a combination of Security state, StreamWorld or translation regime, VMID tag (if relevant) and ASID tag (if relevant). This can happen in any of the following (non-exhaustive list of) cases:

- Several STEs with StreamWorld == Secure each point to their own CD that contains a common ASID value
- -Secure translation regime differentiates address spaces by ASID (but not VMID).
- Several STEs with StreamWorld == NS-EL1 contain a common VMID. Each STE points to its own CD that contains a common ASID value:
- -NS-EL1 differentiates address spaces by ASID and VMID.
- An STE with StreamWorld == any-EL2 points to a table of more than one CD.
- -EL2 has no ASIDs, therefore multiple CDs represent the same (single) set of translations.
- An STE with StreamWorld == any-EL2-E2H points to a CD table where some entries use the same ASID value:
- -EL2-E2H differentiates address spaces by ASID only.

If multiple CDs exist in the same translation regime representing the same address space, any of these CDs can insert TLB entries matching lookup in that address space. All such CDs are considered interchangeable by the SMMUand must contain identical configuration for fields that are permitted to be cacheable as part of a TLB entry.

Note: The EL2 and EL3 translation regimes do not differentiate address spaces by ASID, therefore all CDs referenced from STEs having StreamWorld any-EL2 or EL3 must be identical for fields permitted to be cacheable in a TLB. This includes tables of multiple CDs referenced from one STE, or CDs referenced one to one from an STE. It is not expected that SubstreamIDs (therefore a CD table with multiple entries) will be used with STEs configured for any-EL2 or EL3 StreamWorlds.

If a software error causes two CDs representing the same address space to differ, the result of a TLB lookup for that address space is UNPREDICTABLE. The SMMU must not allow such an error to provide device access to memory locations outside of the Security state of the stream, or that would not otherwise have been accessible given a stage 2 configuration, if present.

Note: Fields permitted to be cached as part of a TLB entry modify the properties of the TLB entry. A difference in CD configuration can cause TLB entries to be cached with different properties in the same address space. It would be UNPREDICTABLE as to which CD inserted a given TLB entry, therefore the properties returned by a general TLB lookup become UNPREDICTABLE.

## 5.4.1.1 EPDx behavior

The CD EPD0 and EPD1 fields disable translation configuration related to TTB0 and TTB1, respectively. Validity checks are not performed on fields that are disabled or IGNORED by CD.EPDx.

This table shows interaction of CD.TxSZ with EPDx and incoming addresses that select TTB0 or TTB1 translation configuration:

| Virtual Address (VMSAv8-64 example shown)   |   Effective EPD0 |   Effective EPD1 | T0SZ        | T1SZ        | Result                                                               |
|---------------------------------------------|------------------|------------------|-------------|-------------|----------------------------------------------------------------------|
| 0xFFFFXXXXXXXXXXXX                          |                0 |                0 | Valid       | Valid       | Translates through TTB1                                              |
| 0x0000XXXXXXXXXXXX                          |                0 |                0 | Valid       | Valid       | Translates through TTB0                                              |
| 0xFFFFXXXXXXXXXXXX                          |                0 |                0 | X           | Invalid (1) | C_BAD_CD                                                             |
| 0x0000XXXXXXXXXXXX                          |                0 |                0 | X           | Invalid (1) | C_BAD_CD                                                             |
| 0xFFFFXXXXXXXXXXXX                          |                0 |                0 | Invalid (1) | X           | C_BAD_CD                                                             |
| 0x0000XXXXXXXXXXXX                          |                0 |                0 | Invalid (1) | X           | C_BAD_CD                                                             |
| 0xFFFFXXXXXXXXXXXX                          |                0 |                1 | Valid       | X           | TLB miss causes F_TRANSLATION (translation through TTB1 is disabled) |
| 0x0000XXXXXXXXXXXX                          |                0 |                1 | Valid       | X           | Translates through TTB0                                              |
| 0xFFFFXXXXXXXXXXXX                          |                0 |                1 | Invalid (1) | X           | C_BAD_CD                                                             |
| 0x0000XXXXXXXXXXXX                          |                0 |                1 | Invalid (1) | X           | C_BAD_CD                                                             |
| 0xFFFFXXXXXXXXXXXX                          |                1 |                0 | X           | Valid       | Translates through TTB1                                              |
| 0x0000XXXXXXXXXXXX                          |                1 |                0 | X           | Valid       | TLB miss causes F_TRANSLATION (translation through TTB1 is disabled) |
| 0xFFFFXXXXXXXXXXXX                          |                1 |                0 | X           | Invalid (1) | C_BAD_CD                                                             |
| 0x0000XXXXXXXXXXXX                          |                1 |                0 | X           | Invalid (1) | C_BAD_CD                                                             |

- The high-order bits or bits of the V A determine whether TTB0 or TTB1 is selected, according to the A-profile architecture[2].
- In the cases marked (1) , TxSZ is shown as being an invalid value and the SMMU treating this as making the CD ILLEGAL, for the purposes of illustration. See CD.T0SZ, this is one of the CONSTRAINED UNPREDICTABLE behaviors for an out-of-range TxSZ.
- EPDx == 1 causes TxSZ to be IGNORED and an invalid TxSZ value (or an invalid TTBx or TGx value) does not lead to C\_BAD\_CD.
- When EPDx == 1, a translation table walk through TTBx causes F\_TRANSLATION.
- -Note: The A-profile architecture[2] allows a TLB hit to occur for an input address associated with an EPD bit set to 1, but the translation table walk is disabled upon miss.

## 5.4.2 Validity of CD

The following function indicates whether a CD is considered valid or ILLEGAL, for the purposes of determining a configuration error (C\_BAD\_CD). Subsequent checks must be performed as part of the translation process and further faults might arise, but these are unrelated to the validity of configuration structures.

```
// CdIllegal() // =========== // Returns TRUE if CD is considered ILLEGAL // Returns FALSE otherwise boolean CdIllegal(STE_t STE, CD_t CD, bits (2) SEC_SID) // Intermediate values SecurityState sec_sid = DecodeSecSid(SEC_SID); STE_StreamWorld ste_streamworld = SteStreamWorld(STE.STRW, SEC_SID); boolean n_transl_cfg0 = EffectiveCDEPD0(CD.EPD0, ste_streamworld); boolean n_transl_cfg1 = EffectiveCDEPD1(CD.EPD1, ste_streamworld); TGx tg0 = TG0(CD.TG0); TGx tg1 = TG1(CD.TG1); integer ipa_range = CalcPARange(CD.IPS, CD.AA64); boolean using_vmsa32 = SMMU_IDR5.D128 == '0' && CD.AA64 == '0'; boolean using_vmsa64 = CD.AA64 == '1'; boolean using_vmsa128 = SMMU_IDR5.D128 == '1' && CD.AA64 == '0'; bits (2) stall_model; case sec_sid of when SS_NonSecure stall_model = EffectiveSMMU_IDR0_STALL_MODEL(); when SS_Secure stall_model = SMMU_S_IDR0.STALL_MODEL; when SS_Realm stall_model = SMMU_R_IDR0.STALL_MODEL; boolean constr_unpred_TxSZ_or_illegal; if SMMU_AIDR.ArchMajorRev == '0000' && SMMU_AIDR.ArchMinorRev == '0000' then constr_unpred_TxSZ_or_illegal = ConstrainUnpredictableBool(Unpredictable_CD_TxSZ); else // In SMMUv3.1 and later, these cases are always ILLEGAL constr_unpred_TxSZ_or_illegal = TRUE; if CD.V == '0' then // CD is ILLEGAL if not valid return TRUE; if STE.S1STALLD == '1' && CD.S == '1' then // Stalls disabled for the stream but enabled for the CD return TRUE; if SMMU_IDR0.TERM_MODEL == '1' && CD.A == '0' then // Terminating a transaction with RAZ/WI behavior is not supported, // CD.A must be 1. return TRUE; if stall_model == '01' && CD.S == '1' then // Stall is not supported, but CD.S ==1 return TRUE; if stall_model == '10' && CD.S == '0' then // Stall is forced, but CD.S == 0 return TRUE; // Check CD.ENDI if (!n_transl_cfg0 || !n_transl_cfg1) && // CD.ENDI is not IGNORED ((SMMU_IDR0.TTENDIAN == '10' && CD.ENDI == '1') || (SMMU_IDR0.TTENDIAN == '11' && CD.ENDI == '0')) then // Endianess of CD doesn't match system supported endianess return TRUE; // Check CD.AA64 // AArch32 tables not supported by system or the above StreamWorlds if using_vmsa32 && ((SMMU_IDR0.TTF == 'x0') || ste_streamworld IN {STE_StreamWorld_EL3, STE_StreamWorld_any_EL2_E2H}) then return TRUE;
```

```
// VMSAv8-32 LPAE tables are not supported for S-EL2 StreamWorld if sec_sid == SS_Secure && ste_streamworld == STE_StreamWorld_any_EL2 && using_vmsa32 then assert SMMU_S_IDR1.SEL2 == '1'; return TRUE; // AArch64 tables not supported by system or the STE if using_vmsa64 && ((SMMU_IDR0.TTF == '0x') || (STE.Config == '11x' && STE.S2AA64 == '0' && SMMU_IDR5.D128 == '0')) then return TRUE; // Check CD.HA, CD.HD, CD.HAFT if !using_vmsa32 && // The following conditions are ILLEGAL when VMSAv8-64 or // when VMSAv9-128 are used. // No flag updates supported, but CD wants to update flag (((CD.HA == '1' || CD.HD == '1') && (SMMU_IDR0.HTTU == '00')) || // Only access flag update suppported, but CD updates dirty flag (CD.HD == '1' && SMMU_IDR0.HTTU == '01') || // Hardware update of AF in Table descriptors is supported and enabled, // but update of AF in leaf descriptors is not enabled (SMMU_IDR0.HTTU == '11' && CD.HAFT == '1' && CD.HA == '0')) then return TRUE; // Check CD.ASID. // While in one of the following SteamWorlds, // and the system only supports 8-bit ASIDs, if the CD.ASID field // is non-zero for the 8 MSBs, the CD is ILLEGAL if ste_streamworld IN { STE_StreamWorld_NS_EL1, STE_StreamWorld_Secure, STE_StreamWorld_Realm_EL1, STE_StreamWorld_any_EL2_E2H } && SMMU_IDR0.ASID16 == '0' && CD.ASID<15:8> != '00000000' then return TRUE; // Check CD.TxSZ if (!using_vmsa32 && constr_unpred_TxSZ_or_illegal) && ((!n_transl_cfg0 && CDTxSZInvalid(ste_streamworld, using_vmsa128, CD.DS, CD.T0SZ, tg0)) || (!n_transl_cfg1 && CDTxSZInvalid(ste_streamworld, using_vmsa128, CD.DS, CD.T1SZ, tg1))) then return TRUE; // Check CD.TTBx if !n_transl_cfg0 && ((!using_vmsa32 && !GranuleSupported(tg0)) || CDTTBxOutOfRange(CD.TTB0, CDTTBxValidRange(using_vmsa128, CD.DS, tg0, ipa_range))) ↪ → then return TRUE; if !n_transl_cfg1 && ((!using_vmsa32 && !GranuleSupported(tg1)) || CDTTBxOutOfRange(CD.TTB1, CDTTBxValidRange(using_vmsa128, CD.DS, tg1, ipa_range))) ↪ → then return TRUE; // Check VMSAv9-128 if using_vmsa128 then if STE.S1PIE == '0' then // CD uses VMSAv9-128, but STE disables use of permission indirection return TRUE; if ste_streamworld == STE_StreamWorld_any_EL2 then // CD uses VMSAv9-128, but STE selects Stream World EL2 return TRUE; if ((!n_transl_cfg0 && CDSLInvalidD128(CD.SKL0, CD.T0SZ, tg0)) || (!n_transl_cfg1 && CDSLInvalidD128(CD.SKL1, CD.T1SZ, tg1))) then // CD configured the start level of translation to an invalid value
```

```
return TRUE; // Check CD.{PIIP,PIIU} (permission indirection) if ((using_vmsa64 && SMMU_IDR3.S1PI == '1' && STE.S1PIE == '1' && CD.PIE == '1') || using_vmsa128) then for i = 0 to 15 if CD.PIIP<(i*3)+:3> IN { '100','110' } then // Stage 1 permission indirection is enabled, // but PIIP contains a Reserved encoding return TRUE; // If the stream world supports unprivileged transactions, check PIIU if ste_streamworld IN { STE_StreamWorld_any_EL2_E2H, STE_StreamWorld_NS_EL1, STE_StreamWorld_Realm_EL1, STE_StreamWorld_Secure } then if CD.PIIU<(i*3)+:3> IN { '100','110' } then // Stage 1 permission indirection is enabled, // but PIIU contains a Reserved encoding return TRUE; if CD.PIIP<(i*3)+:3> == 'x1x' && CD.PIIU<(i*3)+:3> == '1xx' then // Permitting execution by privileged transactions while also permitting // writes by unprivileged transactions is ILLEGAL return TRUE; // CD is not ILLEGAL return FALSE; // CDTxSZInvalid() // =============== // Returns TRUE if TxSZ is outside the valid range // when stage 1 is using VMSAv8-64 or VMSAv9-128 // Returns FALSE otherwise boolean CDTxSZInvalid(STE_StreamWorld ste_streamworld, boolean using_vmsa128, bit DS, bits (6) TxSZ, TGx TG) integer txsz_min, txsz_max; integer txsz = UInt(TxSZ); // Find txsz_max if SMMU_IDR3.STT == '1' && TG IN {TGx_4KB, TGx_16KB} then // Small translation table supported txsz_max = 48; elsif SMMU_IDR3.STT == '1' then // Small translation table supported but TG NOT IN {4KB, 16KB} txsz_max = 47; else // Small translation table not supported txsz_max = 39; // find txsz_min if SMMU_IDR5.VAX == '10' then if using_vmsa128 then // VMSAv9-128 can use up to 56-bit VAs if ste_streamworld == STE_StreamWorld_EL3 then txsz_min = 8; else txsz_min = 9; elsif TG == TGx_64KB || (SMMU_IDR5.DS == '1' && DS == '1') then // VMSAv8-64 can use up to 52-bit VAs in certain configurations txsz_min = 12; else // Other VMSAv8-64 configurations can only use up to 48-bit VAs txsz_min = 16; elsif SMMU_IDR5.VAX == '01' then if TG == TGx_64KB || (SMMU_IDR5.DS == '1' && DS == '1') || using_vmsa128 then // VMSAv8-64 can use up to 52-bit VAs in certain configurations // VMSAv9-128 can use up to 56-bit VAs, but only 52-bit VAs are implemented
```

```
txsz_min = 12; else // Other VMSAv8-64 configurations can only use up to 48-bit VAs txsz_min = 16; else // Only 48-bit VAs are implemented txsz_min = 16; return (txsz < txsz_min || txsz > txsz_max); // CDSLInvalidD128() // ================= // Returns TRUE if start level is invalid when using VMSAv9-128 // Returns FALSE otherwise boolean CDSLInvalidD128( bits (2) SKL, bits (6) TxSZ, TGx TG) integer iasize = 64 - UInt(TxSZ); integer granulebits = TGSize(TG); integer stride = granulebits - 4; integer startlevel = 3 - (((iasize-1) - granulebits) DIV stride); return startlevel + UInt(SKL) > 3;
```