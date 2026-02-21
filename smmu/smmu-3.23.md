## 3.23 Memory Tagging Extension

MTE introduces a new MAIR field encoding, 0xf0 . This encoding is Reserved in SMMUv3, in the CD.MAIR0 and CD.MAIR1 fields.

All SMMU-originated accesses are Tag Unchecked accesses. The SMMU does not write Allocation Tags .

The terms Tag Unchecked and Allocation Tag are defined in [2].

## 3.23.1 SMMU support for FEAT\_MTE\_PERM

If SMMU\_IDR3.MTEPERM is 1, then stage 2 MemAttr encodings that have the NoTagAccess attribute introduced by FEAT\_MTE\_PERM in [2] are treated as both:

- Not having the NoTagAccess attribute in the SMMU.
- Having the same memory type and Cacheability attributes as in FEAT\_MTE\_PERM in [2].

The resulting encodings are:

|   STE.S2FWB | Stage 2 MemAttr[3:0]   | SMMUinterpretation                                            |
|-------------|------------------------|---------------------------------------------------------------|
|           0 | 0b0100                 | Normal Inner Write-Back Cacheable, Outer Write-Back Cacheable |
|           1 | 0b1111                 | Same as 0b0111 .                                              |
|           1 | 0b1110                 | Same as 0b0110 .                                              |
|           1 | 0b1101                 | Reserved.                                                     |
|           1 | 0b1100                 | Reserved.                                                     |
|           1 | 0b10xx                 | Reserved.                                                     |

Note: The stage 2 MemAttr behavior for the SMMU specified here is consistent with all accesses not having the Tagged attribute at stage 2.