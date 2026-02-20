## D8.3 Translation table descriptor formats

RHJXKZ

RJXLYN

RKHVQT

RRWMFF

If an address translation stage is controlled by an Exception level that is using AArch64, then the translation table uses one of the following:

- For the VMSAv8-64 translation system, 64-bit descriptors.
- For the VMSAv9-128 translation system, 128-bit descriptors.

Atranslation descriptor has one of the following formats:

- An invalid descriptor format.
- ATable descriptor format that points to the next-level translation table.
- ABlock descriptor or Page descriptor format that defines the memory access properties.
- Areserved format.

The value of descriptor bit[0] determines one of the following:

- If descriptor bit[0] is 0, then the descriptor is invalid.
- If descriptor bit[0] is 1, then the descriptor is valid.

For 64-bit descriptors used by the VMSAv8-64 translation system, if descriptor bit[0] is 1, then the descriptor type is determined by one of the following values of descriptor bit[1]:

- For lookup levels less than lookup level 3, one of the following:
- -If bit[1] is 0, then the descriptor is a Block descriptor.
- -If bit[1] is 1, then the descriptor is a Table descriptor.
- For lookup level 3, one of the following:
- -If bit[1] is 0, then the descriptor is reserved, and treated as invalid.
- -If bit[1] is 1, then the descriptor is a Page descriptor.

## Table D8-48 Determination of descriptor type, VMSAv8-64 translation system

| Descriptor   | Descriptor   | type                         | Condition             |
|--------------|--------------|------------------------------|-----------------------|
| 0            | -            | Invalid                      | -                     |
| 1            | 0            | Block                        | Lookup level is not 3 |
|              |              | Reserved, treated as invalid | Lookup level is 3     |
|              | 1            | Table                        | Lookup level is not 3 |
|              |              | Page                         | Lookup level is 3     |

RBPTPZ

For 128-bit descriptors used by the VMSAv9-128 translation system, if descriptor bit[0] is 1, then the descriptor type is determined by the sum of the current lookup level and the descriptor SKL field in descriptor bits[110:109], as follows:

- If the sum is less than 3, then one of the following:
- -If a table of the resulting size is permitted, then a Table descriptor.
- -If a table of the resulting size is not permitted, then an Invalid descriptor.
- If the sum is equal to 3, then one of the following:
- -If a block of the resulting size is permitted at the resulting level, then a Block or Page descriptor.
- -If a block of the resulting size is not permitted at the resulting level, then an Invalid descriptor.
- If the sum is greater than 3, then an Invalid descriptor.

RFRLRB

RPGHRP

ITWKLX

Table D8-49 Determination of descriptor type, VMSAv9-128 translation system

| Descriptor bit[0]   | Current lookup level + descriptor SKL field   | Descriptor type   | Condition                   |
|---------------------|-----------------------------------------------|-------------------|-----------------------------|
| 0                   | -                                             | Invalid           | -                           |
| 1                   | Less than 3                                   | Table             | Table size is permitted     |
|                     |                                               | Invalid           | Table size is not permitted |
|                     | Equal to 3                                    | Block or Page     | Block size is permitted     |
|                     |                                               | Invalid           | Block size is not permitted |
|                     | Greater than 3                                | Invalid           | -                           |

RCQGPJ For Table descriptors, if the Effective value of the SKL field is 0, then the next-level table address is one of the following:

- For a level -2 Table descriptor, the base address of a level -1 table.
- For a level -1 Table descriptor, the base address of a level 0 table.
- For a level 0 Table descriptor, the base address of a level 1 table.
- For a level 1 Table descriptor, the base address of a level 2 table.
- For a level 2 Table descriptor, the base address of a level 3 table.

For Table descriptors, the next-level table address is one of the following:

- For the EL1&amp;0 stage 1 translation regimes, if EL2 is enabled, then the IPA of the target table.
- For all other translation regimes, the PA of the target table.

## D8.3.1 VMSAv8-64 descriptor formats

## D8.3.1.1 VMSAv8-64 Table descriptor format

Throughout this section, if an address translation stage is not specified, then references to the Effective value of TCR\_ELx.DS also apply to VTCR\_EL2.DS.

The following figure shows all of following stage 1 and stage 2 VMSAv8-64 Table descriptor formats:

- 4KB, 16KB, and 64KB granules using a 48-bit next-level table address.
- If the Effective value of TCR\_ELx.DS is 1, the 4KB and 16KB granules using a 52-bit next-level table address.
- If FEAT\_LPA is implemented, the 64KB granule using a 52-bit next-level table address.

<!-- image -->

With the 4KB granule size m is 12 ‡ , with the 16KB granule size m is 14, and with the 64KB granule size m is 16. ‡ When m is 12, the RES0 field shown for bits[( m -1):12] is absent.

## Figure D8-12 VMSAv8-64 Table descriptor formats

ILZSBS For a stage 1 translation, the following figure shows the next-level attribute fields in a VMSAv8-64 Table descriptor. For a stage 2 translation, all of the following apply:

- Bit[63] is RES0.
- Bits[62:59] are one of the following:
- -If stage 2 Indirect permissions are disabled, then RES0.
- -If stage 2 Indirect permissions are enabled, then IGNORED.
- Bits[58:51] are IGNORED.

RYWCCT

Figure D8-13 Stage 1 next-level attribute fields in a VMSAv8-64 Table descriptor

<!-- image -->

For stage 1 translations, the following table defines the fields in the VMSAv8-64 Table descriptor. In this table, NLTA is the next level table address.

## Table D8-50 Stage 1 VMSAv8-64 Table descriptor fields

| Bit position   | Field   | Condition                               |
|----------------|---------|-----------------------------------------|
| [63]           | RES0    | The Security state is not Secure state. |

| Bit position   | Field                    | Condition                                                                                                                                                                                                                                                                                                           |
|----------------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | NSTable                  | Secure state. See Hierarchical control of Secure or Non-secure memory accesses.                                                                                                                                                                                                                                     |
| [62:61]        | APTable[1:0]             | Hierarchical permissions are enabled. See Hierarchical control of data access Direct permissions. For EL1&0 translations, if the Effective value of HCR_EL2.{NV, NV1} is {1, 1}, then APTable[0] is treated as 0 regardless of the actual value. See Additional behavior when HCR_EL2.NV is 1 and HCR_EL2.NV1 is 1. |
| [60]           | XNTable                  | Hierarchical permissions are enabled and the translation regime supports a single privilege level. See Hierarchical control of instruction execution for Direct permissions.                                                                                                                                        |
| [60]           | UXNTable                 | Hierarchical permissions are enabled and the translation regime supports two privilege levels. See Hierarchical control of instruction execution for Direct permissions.                                                                                                                                            |
| [60]           | PXNTable                 | Hierarchical permissions are enabled, the EL1&0 translation regime, and the Effective value of HCR_EL2.{NV, NV1} is {1, 1}. See Hierarchical control of instruction execution for Direct permissions.                                                                                                               |
| [59]           | RES0                     | Hierarchical permissions are enabled and one of the following applies: • The translation regime supports a single privilege level. • The EL1&0 translation regime and the Effective value of HCR_EL2.{NV, NV1} is {1, 1}.                                                                                           |
| [58:53]        | IGNORED                  | -                                                                                                                                                                                                                                                                                                                   |
| [52]           | IGNORED                  | The Effective value of PnCH is 0.                                                                                                                                                                                                                                                                                   |
| [52]           | Protected                | The Effective value of PnCH is 1. See Stage 1 Protected Attribute.                                                                                                                                                                                                                                                  |
| [51]           | IGNORED                  | -                                                                                                                                                                                                                                                                                                                   |
| [50]           | RES0                     | -                                                                                                                                                                                                                                                                                                                   |
| [49:48]        | RES0                     | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0, or the 64KB translation granule is used.                                                                                                                                                                                   |
| [49:48]        | NLTA[49:48]              | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                                                                                                                                                                            |
| [47:12]        | NLTA[47:12]              | The 4KB translation granule is used.                                                                                                                                                                                                                                                                                |
| [47:12]        | NLTA[47:14]              | The 16KB translation granule is used. Descriptor bits [13:12] are RES0.                                                                                                                                                                                                                                             |
| [47:12]        | NLTA[47:16]              | The 64KB translation granule is used and FEAT_LPA is not implemented. Descriptor bits [15:12] are RES0.                                                                                                                                                                                                             |
| [47:12]        | NLTA[47:16]: NLTA[51:48] | The 64KB translation granule is used and FEAT_LPA is implemented.                                                                                                                                                                                                                                                   |
| [11]           | IGNORED                  | -                                                                                                                                                                                                                                                                                                                   |
| [10]           | IGNORED                  | Hardware managed Table descriptor Access flag is not enabled.                                                                                                                                                                                                                                                       |
| [10]           | Access flag (AF)         | Hardware managed Table descriptor Access flag is enabled. See Hardware management of the Table descriptor Access Flag.                                                                                                                                                                                              |
| [9:8]          | IGNORED                  | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0, or the 64KB translation granule is used.                                                                                                                                                                                   |
| [9:8]          | NLTA[51:50]              | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                                                                                                                                                                            |
| [7:2]          | IGNORED                  | -                                                                                                                                                                                                                                                                                                                   |

| Bit position   | Field            | Condition                                      |
|----------------|------------------|------------------------------------------------|
| [1]            | Table descriptor | 1, for lookup levels less than lookup level 3. |
| [0]            | Valid descriptor | 1.                                             |

| I LPCPS   | For stage 1 translations in the EL3 translation regime, the removal of NSTable in Root state is a change from the behavior of EL3 in Secure state.       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XFNBW   | For stage 2 translations, the following table defines the fields in the VMSAv8-64 Table descriptor. In this table, NLTA is the next level table address. |

## Table D8-51 Stage 2 VMSAv8-64 Table descriptor fields

| Bit position   | Field                    | Condition                                                                                                                          |
|----------------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------|
| [63]           | RES0                     | -                                                                                                                                  |
| [62:59]        | RES0                     | Stage 2 Indirect permissions are disabled.                                                                                         |
| [62:59]        | IGNORED                  | Stage 2 Indirect permissions are enabled. See Stage 2 Indirect permissions.                                                        |
| [58:51]        | IGNORED                  | -                                                                                                                                  |
| [50]           | RES0                     | -                                                                                                                                  |
| [49:48]        | RES0                     | The 4KB or 16KB translation granule is used, and the Effective value of VTCR_EL2.DS is 0, or the 64KB translation granule is used. |
| [49:48]        | NLTA[49:48]              | The 4KB or 16KB translation granule is used, and the Effective value of VTCR_EL2.DS is 1.                                          |
| [47:12]        | NLTA[47:12]              | The 4KB translation granule is used.                                                                                               |
| [47:12]        | NLTA[47:14]              | The 16KB translation granule is used. Descriptor bits [13:12] are RES0.                                                            |
| [47:12]        | NLTA[47:16]              | The 64KB translation granule is used and FEAT_LPA is not implemented. Descriptor bits [15:12] are RES0.                            |
| [47:12]        | NLTA[47:16]: NLTA[51:48] | The 64KB translation granule is used and FEAT_LPA is implemented.                                                                  |
| [11]           | IGNORED                  | -                                                                                                                                  |
| [10]           | IGNORED                  | Hardware managed Table descriptor Access flag is not enabled.                                                                      |
| [10]           | Access flag (AF)         | Hardware managed Table descriptor Access flag is enabled. See Hardware management of the Table descriptor Access Flag.             |
| [9:8]          | IGNORED                  | The 4KB or 16KB translation granule is used, and the Effective value of VTCR_EL2.DS is 0, or the 64KB translation granule is used. |
| [9:8]          | NLTA[51:50]              | The 4KB or 16KB translation granule is used, and the Effective value of VTCR_EL2.DS is 1.                                          |
| [7:2]          | IGNORED                  | -                                                                                                                                  |
| [1]            | Table descriptor         | 1, for lookup levels less than lookup level 3.                                                                                     |
| [0]            | Valid descriptor         | 1.                                                                                                                                 |

## D8.3.1.2 VMSAv8-64 Block descriptor and Page descriptor formats

RWLDSK

Throughout this section, if an address translation stage is not specified, then references to the Effective value of TCR\_ELx.DS also apply to VTCR\_EL2.DS.

IGBPDK

The following figure shows all of the following VMSAv8-64 Block descriptor formats:

- 4KB, 16KB, and 64KB granules using a 48-bit OA.

IWNCLB

- If the Effective value of TCR\_ELx.DS is 1, the 4KB and 16KB granules using a 52-bit OA.
- If FEAT\_LPA is supported, the 64KB granule using a 52-bit OA.

Figure D8-14 VMSAv8-64 Block descriptor formats

<!-- image -->

The following figure shows all of the following VMSAv8-64 Page descriptor formats:

- 4KB, 16KB, and 64KB granules using a 48-bit OA.
- If the Effective value of TCR\_ELx.DS is 1, the 4KB and 16KB granules using a 52-bit OA.
- If FEAT\_LPA is supported, the 64KB granule using a 52-bit OA.

Figure D8-15 VMSAv8-64 Page descriptor formats

<!-- image -->

IGLMLD For a stage 1 translation, the following figure shows the attribute fields in VMSAv8-64 Block descriptors and Page descriptors, split into upper attributes and lower attributes.

Figure D8-16 Stage 1 attribute fields in VMSAv8-64 Block and Page descriptors

<!-- image -->

For stage 1 translations, the following table defines the fields in the VMSAv8-64 Block and Page descriptors. In this table, OAB is the OA base that is appended to the IA supplied to the translation stage to produce the final OA supplied by the translation stage.

RJJNHR

## Table D8-52 Stage 1 VMSAv8-64 Block and Page descriptor fields

| Bit position   | Field                            | Condition                                                                                                                                                                                                                                                                                              |
|----------------|----------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [63]           | IGNORED                          | Secure state.                                                                                                                                                                                                                                                                                          |
| [63]           | Reserved for software use        | Non-secure state, or the Realm EL1&0 translation regime.                                                                                                                                                                                                                                               |
| [63]           | Alternate MECID (AMEC)           | Realm EL2 or Realm EL2&0 translation regimes, and the descriptor NS field is 0. See Memory Encryption Contexts extension.                                                                                                                                                                              |
| [63]           | RES0                             | Realm EL2 or Realm EL2&0 translation regimes, and the descriptor NS field is 1.                                                                                                                                                                                                                        |
| [62:60]        | IGNORED                          | Both of the following apply: • FEAT_HPDS2 is not implemented or PBHAis not enabled by the corresponding TCR_ELx.HWU nn control bit. • FEAT_S1POE is not implemented or stage 1 Overlay permissions are not enabled.                                                                                    |
| [62:60]        | PBHA[3:1]                        | FEAT_HPDS2 is implemented and the PBHAbit is enabled by the corresponding TCR_ELx.HWU nn control bit. See Page Based Hardware attributes.                                                                                                                                                              |
| [62:60]        | POIndex[2:0]                     | Stage 1 Overlay permissions enabled. See Stage 1 Overlay permissions.                                                                                                                                                                                                                                  |
| [59]           | IGNORED                          | Both of the following apply: • FEAT_HPDS2 is not implemented or PBHAis not enabled by the corresponding TCR_ELx.HWU nn control bit. • FEAT_AIE is not implemented or the stage 1 Attribute Index Extension is not enabled.                                                                             |
| [59]           | PBHA[0]                          | FEAT_HPDS2 is implemented and the PBHAbit is enabled by the corresponding TCR_ELx.HWU nn control bit. See Page Based Hardware attributes.                                                                                                                                                              |
| [59]           | AttrIndx[3]                      | FEAT_AIE is enabled. See Stage 1 memory type and Cacheability attributes.                                                                                                                                                                                                                              |
| [58:55]        | Reserved for software use        | -                                                                                                                                                                                                                                                                                                      |
| [54]           | Execute-never (XN)               | The translation regime supports a single privilege level. See Stage 1 instruction execution using Direct permissions.                                                                                                                                                                                  |
| [54]           | Unprivileged Execute-never (UXN) | The translation regime supports two privilege levels. See Stage 1 instruction execution using Direct permissions.                                                                                                                                                                                      |
| [54]           | Privileged Execute-never (PXN)   | The EL1&0 translation regime and the Effective value of HCR_EL2.{NV, NV1} is {1, 1}. The Effective value of UXNis 0. See Stage 1 instruction execution using Direct permissions and Additional behavior when HCR_EL2.NV is 1 and HCR_EL2.NV1 is 1.                                                     |
| [54]           | PIIndex[3]                       | Stage 1 Indirect permissions enabled, regardless of other feature settings. See Stage 1 Indirect permissions.                                                                                                                                                                                          |
| [53]           | RES0                             | One of the following: • The translation regime supports a single privilege level. • The EL1&0 translation regime and the Effective value of HCR_EL2.{NV, NV1} is {1, 1}. See Stage 1 instruction execution using Direct permissions and Additional behavior when HCR_EL2.NV is 1 and HCR_EL2.NV1 is 1. |
| [53]           | PXN                              | The translation regime supports two privilege levels. See Stage 1 instruction execution using Direct permissions.                                                                                                                                                                                      |

| Bit position   | Field                    | Condition                                                                                                                                                 |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | PIIndex[2]               | Stage 1 Indirect permissions enabled, regardless of other feature settings. See Stage 1 Indirect permissions.                                             |
| [52]           | Contiguous               | The Effective value of PnCH is 0. See The Contiguous bit.                                                                                                 |
|                | Protected                | The Effective value of PnCH is 1. See Stage 1 Protected Attribute.                                                                                        |
| [51]           | Dirty bit modifier (DBM) | Stage 1 Indirect permissions are disabled. See Hardware management of the dirty state.                                                                    |
|                | PIIndex[1]               | Stage 1 Indirect permissions are enabled. See Stage 1 Indirect permissions.                                                                               |
| [50]           | RES0                     | FEAT_BTI is not implemented.                                                                                                                              |
|                | Guarded Page (GP)        | FEAT_BTI is implemented. See PSTATE.BTYPE.                                                                                                                |
| [49:48]        | RES0                     | One of the following: • The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0. • The 64KB translation granule is used.  |
|                | OAB[49:48]               | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                  |
| Block[47:17]   | OAB[47:39]               | The 4KB translation granule, the Effective value of TCR_ELx.DS is 1, and the descriptor is a level 0 Block descriptor. Descriptor bits [38:17] are RES0.  |
|                | OAB[47:30]               | The 4KB translation granule and the descriptor is a level 1 Block descriptor. Descriptor bits [29:17] are RES0.                                           |
|                | OAB[47:21]               | The 4KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [20:17] are RES0.                                           |
|                | OAB[47:36]               | The 16KB translation granule, the Effective value of TCR_ELx.DS is 1, and the descriptor is a level 1 Block descriptor. Descriptor bits [35:17] are RES0. |
|                | OAB[47:25]               | The 16KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [24:17] are RES0.                                          |
|                | OAB[47:42]               | The 64KB translation granule, FEAT_LPA is implemented, and the descriptor is a level 1 Block descriptor. Descriptor bits [41:17] are RES0.                |
|                | OAB[47:29]               | The 64KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [28:17] are RES0.                                          |
| Block[16]      | RES0                     | FEAT_BBML1 is not implemented.                                                                                                                            |
|                | nT                       | FEAT_BBML1 is implemented. See Table and Block entry.                                                                                                     |
| Block[15:12]   | RES0                     | One of the following: • FEAT_LPA is not implemented. • FEAT_LPA is implemented, and the 4KB or 16KB translation granule is used.                          |
|                | OAB[51:48]               | FEAT_LPA is implemented and the 64KB translation granule is used.                                                                                         |
| Page[47:12]    | OAB[47:12]               | The 4KB translation granule is used.                                                                                                                      |
|                | OAB[47:14]               | The 16KB translation granule is used. Descriptor bits [13:12] are RES0.                                                                                   |
|                | OAB[47:16]               | The 64KB translation granule and FEAT_LPA is not implemented. Descriptor bits [15:12] are RES0.                                                           |

| Bit position   | Field                  | Condition                                                                                                                                                                                     |
|----------------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | OAB[47:16]: OAB[51:48] | The 64KB translation granule and FEAT_LPA is implemented.                                                                                                                                     |
| [11]           | RES0                   | The translation regime supports a single privilege level and the Security state is not Root state.                                                                                            |
| [11]           | NSE                    | Root state. See Controlling memory access Security state.                                                                                                                                     |
| [11]           | Not global (nG)        | The translation regime supports two privilege levels. See Global and process-specific translation table entries.                                                                              |
| [11]           | IGNORED                | The Effective value of TCR2_ELx.FNGy is 1, where y is {0, 1}. SeeR KDVGW in Use of ASIDs and VMIDs to reduce TLB maintenance requirements.                                                    |
| [10]           | Access flag (AF)       | - See The Access flag.                                                                                                                                                                        |
| [9:8]          | Shareability (SH[1:0]) | One of the following: • The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0. • The 64KB translation granule is used. See Stage 1 Shareability attributes. |
| [9:8]          | OAB[51:50]             | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                                                      |
| [7]            | AP[2]                  | Stage 1 Indirect permissions are disabled. See Stage 1 data accesses using Direct permissions.                                                                                                |
| [7]            | nDirty                 | Stage 1 Indirect permissions are enabled. See The dirty state.                                                                                                                                |
| [6]            | RES1                   | Stage 1 Indirect permissions are disabled and the translation regime supports a single privilege level.                                                                                       |
| [6]            | AP[1]                  | Stage 1 Indirect permissions are disabled and the translation regime supports two privilege levels. See Stage 1 data accesses using Direct permissions.                                       |
| [6]            | PIIndex[0]             | Stage 1 Indirect permissions are enabled. See Stage 1 Indirect permissions.                                                                                                                   |
| [5]            | RES0                   | The access is from Non-secure state, or from Realm state using the EL1&0 translation regime.                                                                                                  |
| [5]            | NS                     | The access is from Secure state, from Realm state using the EL2 or EL2&0 translation regimes, or from Root state.                                                                             |
| [4:2]          | AttrIndx[2:0]          | See Stage 1 memory type and Cacheability attributes.                                                                                                                                          |
| [1]            | Block descriptor       | 0, for lookup levels less than lookup level 3.                                                                                                                                                |
| [1]            | Page descriptor        | 1, for lookup level 3.                                                                                                                                                                        |
| [0]            | Valid descriptor       | 1.                                                                                                                                                                                            |

IBJRZD

For a stage 2 translation, the following figure shows the attribute fields in VMSAv8-64 Block descriptors and Page descriptors, split into upper attributes and lower attributes.

RDMBGN

Figure D8-17 Stage 2 attribute fields in VMSAv8-64 Block and Page descriptors

<!-- image -->

For stage 2 translations, the following table defines the fields in the VMSAv8-64 Block and Page descriptors. In this table, OAB is the OA base that is appended to the IA supplied to the translation stage to produce the final OA supplied by the translation stage.

## Table D8-53 Stage 2 VMSAv8-64 Block and Page descriptor fields

| Bit position   | Field                           | Condition                                                                                                                                                          |
|----------------|---------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [63]           | RES0                            | One of the following: • Non-secure or Secure state. • Realm state and the descriptor NS field is 1.                                                                |
| [63]           | Alternate MECID (AMEC)          | Realm state and the descriptor NS field is 0. See Memory Encryption Contexts extension.                                                                            |
| [62:60]        | Reserved for use by a SystemMMU | One of the following: • FEAT_HPDS2 is not implemented. • FEAT_HPDS2 is implemented and the PBHAbit is not enabled by the corresponding TCR_ELx.HWU nn control bit. |
| [62:60]        | PBHA[3:1]                       | FEAT_HPDS2 is implemented and the PBHAbit is enabled by the corresponding TCR_ELx.HWU nn control bit. See Page Based Hardware attributes.                          |
| [62:60]        | POIndex[3:1]                    | Stage 2 Overlay permissions enabled, regardless of other feature settings. See Stage 2 Overlay permissions.                                                        |
| [59]           | IGNORED                         | FEAT_HPDS2 is implemented and the PBHAbit is enabled by the corresponding TCR_ELx.HWU nn control bit. See Page Based Hardware attributes.                          |
| [59]           | PBHA[0]                         | FEAT_HPDS2 is implemented and PBHAbit is enabled by the corresponding TCR_ELx.HWU nn control bit. See Page Based Hardware attributes.                              |
| [59]           | POIndex[0]                      | Stage 2 Overlay permissions enabled, regardless of other feature settings. See Stage 2 Overlay permissions.                                                        |
| [58]           | Reserved for software use       | VTCR_EL2.AssuredOnly is 0.                                                                                                                                         |
| [58]           | AssuredOnly                     | VTCR_EL2.AssuredOnly is 1. See Assured translation.                                                                                                                |
| [57:56]        | Reserved for software use       | -                                                                                                                                                                  |

| Bit position   | Field                    | Condition                                                                                                                                                 |
|----------------|--------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|
| [55]           | Non-secure (NS)          | Realm state. See Controlling memory access Security state.                                                                                                |
|                | IGNORED                  | Security state other than Realm state.                                                                                                                    |
| [54]           | Execute-never (XN)       | FEAT_XNX is not implemented. See Stage 2 instruction execution using Direct permissions.                                                                  |
|                | XN[1]                    | FEAT_XNX is implemented. See Stage 2 instruction execution using Direct permissions.                                                                      |
|                | PIIndex[3]               | Stage 2 Indirect permissions enabled, regardless of other feature settings. See Stage 2 Indirect permissions.                                             |
| [53]           | RES0                     | FEAT_XNX is not implemented.                                                                                                                              |
|                | XN[0]                    | FEAT_XNX is implemented. See Stage 2 instruction execution using Direct permissions.                                                                      |
|                | PIIndex[2]               | Stage 2 Indirect permissions enabled, regardless of other feature settings. See Stage 2 Indirect permissions.                                             |
| [52]           | Contiguous               | -                                                                                                                                                         |
| [51]           | Dirty bit modifier (DBM) | Stage 2 Indirect permissions are disabled. See Hardware management of the dirty state.                                                                    |
|                | PIIndex[1]               | Stage 2 Indirect permissions are enabled. See Stage 2 Indirect permissions.                                                                               |
| [50]           | RES0                     | -                                                                                                                                                         |
| [49:48]        | RES0                     | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0, or the 64KB translation granule.                                 |
|                | OAB[49:48]               | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                  |
| Block[47:17]   | OAB[47:39]               | The 4KB translation granule, the Effective value of TCR_ELx.DS is 1, and the descriptor is a level 0 Block descriptor. Descriptor bits [38:17] are RES0.  |
|                | OAB[47:30]               | The 4KB translation granule and the descriptor is a level 1 Block descriptor. Descriptor bits [29:17] are RES0.                                           |
|                | OAB[47:21]               | The 4KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [20:17] are RES0.                                           |
|                | OAB[47:36]               | The 16KB translation granule, the Effective value of TCR_ELx.DS is 1, and the descriptor is a level 1 Block descriptor. Descriptor bits [35:17] are RES0. |
|                | OAB[47:25]               | The 16KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [24:17] are RES0.                                          |
|                | OAB[47:42]               | The 64KB translation granule, FEAT_LPA is implemented, and the descriptor is a level 1 Block descriptor. Descriptor bits [41:17] are RES0.                |
|                | OAB[47:29]               | The 64KB translation granule and the descriptor is a level 2 Block descriptor. Descriptor bits [28:17] are RES0.                                          |
| Block[16]      | RES0                     | FEAT_BBML1 is not implemented.                                                                                                                            |
|                | nT                       | FEAT_BBML1 is implemented. See Table and Block entry.                                                                                                     |
| Block[15:12]   | RES0                     | One of the following:                                                                                                                                     |
|                |                          | • FEAT_LPA is not implemented. • FEAT_LPA is implemented, and the 4KB or 16KB translation granule is used.                                                |

| Bit position   | Field                  | Condition                                                                                                                                                   |
|----------------|------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|
|                | OAB[51:48]             | FEAT_LPA is implemented and the 64KB translation granule is used.                                                                                           |
| Page[47:12]    | OAB[47:12]             | The 4KB translation granule is used.                                                                                                                        |
| Page[47:12]    | OAB[47:14]             | The 16KB translation granule is used. Descriptor bits [13:12] are RES0.                                                                                     |
| Page[47:12]    | OAB[47:16]             | The 64KB translation granule and FEAT_LPA is not implemented. Descriptor bits [15:12] are RES0.                                                             |
| Page[47:12]    | OAB[47:16]: OAB[51:48] | The 64KB translation granule and FEAT_LPA is implemented.                                                                                                   |
| [11]           | RES0                   | FEAT_XS is not implemented.                                                                                                                                 |
| [11]           | FnXS                   | FEAT_XS is implemented. See XS attribute modifier.                                                                                                          |
| [10]           | Access flag (AF)       | - See The Access flag.                                                                                                                                      |
| [9:8]          | Shareability (SH[1:0]) | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 0, the 64KB translation granule. See Stage 2 Shareability attributes. |
| [9:8]          | OAB[51:50]             | The 4KB or 16KB translation granule is used, and the Effective value of TCR_ELx.DS is 1.                                                                    |
| [7]            | S2AP[1]                | Stage 2 Indirect permissions are disabled. See Stage 2 data accesses using Direct permissions.                                                              |
| [7]            | Dirty                  | Stage 2 Indirect permissions are enabled. See The dirty state.                                                                                              |
| [6]            | S2AP[0]                | Stage 2 Indirect permissions are disabled. See Stage 2 data accesses using Direct permissions.                                                              |
| [6]            | PIIndex[0]             | Stage 2 Indirect permissions are enabled. See Stage 2 Indirect permissions.                                                                                 |
| [5]            | RES0                   | The Effective value of HCR_EL2.FWB is 1.                                                                                                                    |
| [5]            | MemAttr[3]             | The Effective value of HCR_EL2.FWB is 0. See Stage 2 memory type and Cacheability attributes when FWBis disabled.                                           |
| [4:2]          | MemAttr[2:0]           | - See Stage 2 memory type and Cacheability attributes when FWBis disabled and Stage 2 memory type and Cacheability attributes when FWBis enabled.           |
| [1]            | Block descriptor       | 0, for lookup levels less than lookup level 3.                                                                                                              |
| [1]            | Page descriptor        | 1, for lookup level 3.                                                                                                                                      |
| [0]            | Valid descriptor       | 1.                                                                                                                                                          |

IGKSKW

The VMSAv8-64 Block descriptor and Page descriptor format defines the data Access Permissions bits, AP[2:1], and does not define an AP[0] bit.

## D8.3.1.3 VMSAv8-64 Invalid descriptor format

RVRYZC For stage 1 translations, the following table defines the fields in the VMSAv8-64 Invalid descriptor. IGNORED fields are available for software use.

IBCKNF

RFHFQV

## Table D8-54 Stage 1 VMSAv8-64 Invalid descriptor fields

| Bit position   | Field              | Condition                                                          |
|----------------|--------------------|--------------------------------------------------------------------|
| [63:53]        | IGNORED            | -                                                                  |
| [52]           | IGNORED            | The Effective value of PnCH is 0.                                  |
|                | Protected          | The Effective value of PnCH is 1. See Stage 1 Protected Attribute. |
| [51:1]         | IGNORED            | -                                                                  |
| [0]            | Invalid descriptor | 0.                                                                 |

RJYLCV

For stage 2 translations, the following table defines the fields in the VMSAv8-64 Invalid descriptor. IGNORED fields are available for software use.

## Table D8-55 Stage 2 VMSAv8-64 Invalid descriptor fields

| Bit position   | Field              | Condition   |
|----------------|--------------------|-------------|
| [63:1]         | IGNORED            | -           |
| [0]            | Invalid descriptor | 0.          |

## D8.3.2 VMSAv9-128 descriptor formats

## D8.3.2.1 VMSAv9-128 Table descriptor format

For stage 1 translations, the following figure shows the format of the VMSAv9-128 Table descriptor.

Figure D8-18 Stage 1 VMSAv9-128 Table descriptor

<!-- image -->

For stage 1 translations, the following table defines the fields in the VMSAv9-128 Table descriptor. In this table, NLTA is the next level table address.

| Bit position   | Field                          | Condition                                                                                                              |
|----------------|--------------------------------|------------------------------------------------------------------------------------------------------------------------|
| [127]          | RES0                           | The Security state is not Secure state.                                                                                |
| [127]          | NSTable                        | Secure state. See Hierarchical control of Secure or Non-secure memory accesses.                                        |
| [126:125]      | RES0                           | -                                                                                                                      |
| [124:121]      | RES0                           | Stage 1 Overlay permissions disabled.                                                                                  |
| [124:121]      | IGNORED                        | Stage 1 Overlay permissions enabled. See Stage 1 Overlay permissions.                                                  |
| [120:119]      | RES0                           | -                                                                                                                      |
| [118:115]      | IGNORED                        | -                                                                                                                      |
| [114]          | RES0                           | FEAT_THE is not implemented.                                                                                           |
| [114]          | Protected                      | FEAT_THE is implemented. See Stage 1 Protected Attribute.                                                              |
| [113]          | IGNORED                        | -                                                                                                                      |
| [112]          | Disable contiguous bit (DisCH) | - See The Contiguous bit.                                                                                              |
| [111]          | IGNORED                        | -                                                                                                                      |
| [110:109]      | Skip level (SKL)               | - See Translation using the VMSAv9-128 translation system, and to determine the descriptor type, Table D8-49.          |
| [108:101]      | RES0                           | -                                                                                                                      |
| [100:91]       | Software usage                 | -                                                                                                                      |
| [90:56]        | RES0                           | -                                                                                                                      |
| [55:12]        | NLTA[55:12]                    | 4KB translation granule.                                                                                               |
| [55:12]        | NLTA[55:14]                    | 16KB translation granule. Descriptor bits [13:12] are RES0.                                                            |
| [55:12]        | NLTA[55:16]                    | 64KB translation granule. Descriptor bits [15:12] are RES0.                                                            |
| [11]           | RES0                           | The translation regime supports a single privilege level and the Security state is not Root state.                     |
| [11]           | IGNORED                        | The translation regime supports two privilege levels or the Security state is Root state.                              |
| [10]           | IGNORED                        | Hardware managed Table descriptor Access flag is not enabled.                                                          |
| [10]           | Access flag (AF)               | Hardware managed Table descriptor Access flag is enabled. See Hardware management of the Table descriptor Access Flag. |
| [9:7]          | IGNORED                        | -                                                                                                                      |
| [6]            | RES0                           | SKL is 0b00 .                                                                                                          |
| [6]            | nT                             | SKL is not 0b00 . See Table and Block entry.                                                                           |
| [5:2]          | IGNORED                        | -                                                                                                                      |
| [1]            | RES0                           | -                                                                                                                      |
| [0]            | Valid descriptor               | 1.                                                                                                                     |

ITKQXW

For stage 2 translations, the following figure shows the format of the VMSAv9-128 Table descriptor.

RMYLYC

Figure D8-19 Stage 2 VMSAv9-128 Table descriptor

<!-- image -->

For stage 2 translations, the following table defines the fields in the VMSAv9-128 Table descriptor. In this table, NLTA is the next level table address.

## Table D8-57 Stage 2 VMSAv9-128 Table descriptor fields

| Bit position   | Field            | Condition                                                                                                     |
|----------------|------------------|---------------------------------------------------------------------------------------------------------------|
| [127]          | IGNORED          | Realm EL1&0 translation regime.                                                                               |
| [127]          | RES0             | Translation regime is not the Realm EL1&0 translation regime.                                                 |
| [126:125]      | RES0             | -                                                                                                             |
| [124:121]      | RES0             | Stage 2 Overlay permissions disabled.                                                                         |
| [124:121]      | IGNORED          | Stage 2 Overlay permissions enabled. See Stage 2 Overlay permissions.                                         |
| [120:119]      | RES0             | -                                                                                                             |
| [118:115]      | IGNORED          | -                                                                                                             |
| [114]          | RES0             | FEAT_THE is not implemented.                                                                                  |
| [114]          | IGNORED          | FEAT_THE is implemented.                                                                                      |
| [113:112]      | RES0             | -                                                                                                             |
| [111]          | IGNORED          | -                                                                                                             |
| [110:109]      | Skip level (SKL) | - See Translation using the VMSAv9-128 translation system, and to determine the descriptor type, Table D8-49. |
| [108:101]      | RES0             | -                                                                                                             |
| [100:91]       | Software usage   | -                                                                                                             |
| [90:56]        | RES0             | -                                                                                                             |
| [55:12]        | NLTA[55:12]      | 4KB translation granule.                                                                                      |
| [55:12]        | NLTA[55:14]      | 16KB translation granule. Descriptor bits [13:12] are RES0.                                                   |
| [55:12]        | NLTA[55:16]      | 64KB translation granule. Descriptor bits [15:12] are RES0.                                                   |
| [11]           | IGNORED          | -                                                                                                             |
| [10]           | IGNORED          | Hardware managed Table descriptor Access flag is not enabled.                                                 |

| Bit position   | Field            | Condition                                                                                                              |
|----------------|------------------|------------------------------------------------------------------------------------------------------------------------|
|                | Access flag (AF) | Hardware managed Table descriptor Access flag is enabled. See Hardware management of the Table descriptor Access Flag. |
| [9:7]          | IGNORED          | -                                                                                                                      |
| [6]            | RES0             | SKL is 0b00 .                                                                                                          |
|                | nT               | SKL is not 0b00 . See Block translation entry.                                                                         |
| [5:2]          | IGNORED          | -                                                                                                                      |
| [1]            | RES0             | -                                                                                                                      |
| [0]            | Valid descriptor | 1.                                                                                                                     |

## D8.3.2.2 VMSAv9-128 Block descriptor and Page descriptor formats

For stage 1 translations, the following figure shows the format of the VMSAv9-128 Block and Page descriptor.

Figure D8-20 Stage 1 VMSAv9-128 Block and Page descriptor

<!-- image -->

For stage 1 translations, the following table defines the fields in the VMSAv9-128 Block and Page descriptor. In this table, OAB is the OA base that is appended to the IA supplied to the translation stage to produce the final OA supplied by the translation stage.

## Table D8-58 Stage 1 VMSAv9-128 Block and Page descriptor fields

| Bit position   | Field   | Condition                                                                                                         |
|----------------|---------|-------------------------------------------------------------------------------------------------------------------|
| [127]          | RES0    | The access is from Non-secure state, or from Realm state using the EL1&0 translation regime.                      |
|                | NS      | The access is from Secure state, from Realm state using the EL2 or EL2&0 translation regimes, or from Root state. |
| [126:125]      | RES0    | -                                                                                                                 |
| [124:121]      | RES0    | Stage 1 Overlay permissions disabled.                                                                             |

IYCWMS

RFPNKM

| Bit position   | Field                  | Condition                                                                                                                                  |
|----------------|------------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
|                | POIndex[3:0]           | Stage 1 Overlay permissions enabled. See Stage 1 Overlay permissions.                                                                      |
| [120:119]      | RES0                   | -                                                                                                                                          |
| [118:115]      | PIIndex[3:0]           | -                                                                                                                                          |
| [114]          | RES0                   | FEAT_THE is not implemented.                                                                                                               |
|                | Protected              | FEAT_THE is implemented. See Stage 1 Protected Attribute.                                                                                  |
| [113]          | Guarded Page (GP)      | - See PSTATE.BTYPE.                                                                                                                        |
| [112]          | IGNORED                | -                                                                                                                                          |
| [111]          | Contiguous             | - See The Contiguous bit.                                                                                                                  |
| [110:109]      | Skip level (SKL)       | - See Translation using the VMSAv9-128 translation system, and to determine the descriptor type, Table D8-49.                              |
| [108:101]      | RES0                   | -                                                                                                                                          |
| [100:91]       | Software usage         | -                                                                                                                                          |
| [90:56]        | RES0                   | -                                                                                                                                          |
| [55:12]        | OAB[55:12]             | 4KB translation granule.                                                                                                                   |
|                | OAB[55:14]             | 16KB translation granule. Descriptor bits [13:12] are RES0.                                                                                |
|                | OAB[55:16]             | 64KB translation granule. Descriptor bits [15:12] are RES0.                                                                                |
| [11]           | RES0                   | The translation regime supports a single privilege level and the Security state is not Root state.                                         |
|                | NSE                    | Root state. See Controlling memory access Security state.                                                                                  |
|                | Not global (nG)        | The translation regime supports two privilege levels. See Global and process-specific translation table entries.                           |
|                | IGNORED                | The Effective value of TCR2_ELx.FNGy is 1, where y is {0, 1}. SeeR KDVGW in Use of ASIDs and VMIDs to reduce TLB maintenance requirements. |
| [10]           | Access flag (AF)       | - See The Access flag.                                                                                                                     |
| [9:8]          | Shareability (SH[1:0]) | - See Stage 1 Shareability attributes.                                                                                                     |
| [7]            | nDirty                 | - See The dirty state.                                                                                                                     |
| [6]            | RES0                   | SKL is 0b00 .                                                                                                                              |
|                | nT                     | SKL is not 0b00 . See Block translation entry.                                                                                             |
| [5]            | IGNORED                | FEAT_AIE is not implemented or not enabled.                                                                                                |
|                | AttrIndx[3]            | FEAT_AIE is implemented and enabled. See Stage 1 memory type and Cacheability attributes.                                                  |
| [4:2]          | AttrIndx[2:0]          | - See Stage 1 memory type and Cacheability attributes.                                                                                     |
| [1]            | RES0                   | -                                                                                                                                          |
| [0]            | Valid descriptor       | 1.                                                                                                                                         |

ILFZDC

RNQYBF

For stage 2 translations, the following figure shows the format of the VMSAv9-128 Block and Page descriptor. In this table, OAB is the OA base that is appended to the IA supplied to the translation stage to produce the final OA supplied by the translation stage.

Figure D8-21 Stage 2 VMSAv9-128 Block and Page descriptor

<!-- image -->

For stage 2 translations, the following table defines the fields in the VMSAv9-128 Block and Page descriptors:

## Table D8-59 Stage 2 VMSAv9-128 Block and Page descriptor fields

| Bit position   | Field            | Condition                                                                                                     |
|----------------|------------------|---------------------------------------------------------------------------------------------------------------|
| [127]          | RES0             | The access is not from the Realm EL1&0 translation regime.                                                    |
| [127]          | NS               | The access is from the Realm EL1&0 translation regime.                                                        |
| [126:125]      | RES0             | -                                                                                                             |
| [124:121]      | RES0             | Stage 2 Overlay permissions disabled.                                                                         |
| [124:121]      | POIndex[3:0]     | Stage 2 Overlay permissions enabled. See Stage 2 Overlay permissions.                                         |
| [120:119]      | RES0             | -                                                                                                             |
| [118:115]      | PIIndex[3:0]     | -                                                                                                             |
| [114]          | RES0             | FEAT_THE is not implemented.                                                                                  |
| [114]          | AssuredOnly      | FEAT_THE is implemented. See Assured translation.                                                             |
| [113:112]      | RES0             | -                                                                                                             |
| [111]          | Contiguous       | - See The Contiguous bit.                                                                                     |
| [110:109]      | Skip level (SKL) | - See Translation using the VMSAv9-128 translation system, and to determine the descriptor type, Table D8-49. |
| [108:101]      | RES0             | -                                                                                                             |
| [100:91]       | Software usage   | -                                                                                                             |
| [90:56]        | RES0             | -                                                                                                             |
| [55:12]        | OAB[55:12]       | 4KB translation granule.                                                                                      |

| Bit position   | Field                  | Condition                                                                                                                                         |
|----------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
|                | OAB[55:14]             | 16KB translation granule. Descriptor bits [13:12] are RES0.                                                                                       |
|                | OAB[55:16]             | 64KB translation granule. Descriptor bits [15:12] are RES0.                                                                                       |
| [11]           | FnXS                   | - See XS attribute modifier.                                                                                                                      |
| [10]           | Access flag (AF)       | - See The Access flag.                                                                                                                            |
| [9:8]          | Shareability (SH[1:0]) | - See Stage 1 Shareability attributes.                                                                                                            |
| [7]            | Dirty                  | - See The dirty state.                                                                                                                            |
| [6]            | RES0                   | SKL is 0b00 .                                                                                                                                     |
|                | nT                     | SKL is not 0b00 . See Block translation entry.                                                                                                    |
| [5]            | RES0                   | The Effective value of HCR_EL2.FWB is 1.                                                                                                          |
|                | MemAttr[3]             | The Effective value of HCR_EL2.FWB is 0. See Stage 2 memory type and Cacheability attributes when FWBis disabled.                                 |
| [4:2]          | MemAttr[2:0]           | - See Stage 2 memory type and Cacheability attributes when FWBis disabled and Stage 2 memory type and Cacheability attributes when FWBis enabled. |
| [1]            | RES0                   | -                                                                                                                                                 |
| [0]            | Invalid descriptor     | 0.                                                                                                                                                |
|                | Valid descriptor       | 1.                                                                                                                                                |

## D8.3.2.3 VMSAv9-128 Invalid descriptor format

For the VMSAv9-128 translation system, the following table defines the fields in the Invalid descriptor. IGNORED fields are available for software use.

## Table D8-60 VMSAv9-128 Invalid descriptor fields

| Bit position   | Field              | Condition                                                     |
|----------------|--------------------|---------------------------------------------------------------|
| [127:115]      | IGNORED            | -                                                             |
| [114]          | Protected          | Stage 1 and FEAT_THE is implemented. See Assured translation. |
|                | IGNORED            | Stage 2 or FEAT_THE is not implemented.                       |
| [113:1]        | IGNORED            | -                                                             |
| [0]            | Invalid descriptor | 0.                                                            |

RJRLVJ