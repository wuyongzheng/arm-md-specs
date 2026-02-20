## D9.6 GPT formats

| R QKHMJ   | The in-memory structure that describes the association of physical granules with PA spaces is the Granule Protection Table (GPT).                                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I PZSYC   | For implementations that choose to do so for area or performance reasons, the architecture permits caching of GPT information in a TLB.                                                 |
| R JLXZV   | Asuccessful GPT lookup resolves an input PA to the GPI for that address.                                                                                                                |
| R TRVSY   | AGPTdescriptor is one of a Table, Block, Contiguous, or Granules descriptor.                                                                                                            |
| R JXNXP   | AGPTdescriptor is eight bytes.                                                                                                                                                          |
| R BQHPD   | All structures in the GPT are little-endian.                                                                                                                                            |
| I KFVNY   | All GPT entries are naturally-aligned in memory.                                                                                                                                        |
| R VXNGT   | The GPT has two levels of lookup.                                                                                                                                                       |
| R TRCQY   | All valid entries in a level 0 GPT are GPT Block or GPT Table descriptors.                                                                                                              |
| R TXFXH   | Alevel 0 GPT entry that is not a GPT Block or GPT Table descriptor is invalid.                                                                                                          |
| R DCTFM   | All valid entries in a level 1 GPT are GPT Contiguous or GPT Granules descriptors.                                                                                                      |
| R TPBZN   | Alevel 1 GPT entry that is not a GPT Contiguous or GPT Granules descriptor is invalid.                                                                                                  |
| R XNKFZ   | AGPTentry is invalid if any of the following are true: • Afield in the entry is configured with an encoding marked as reserved. • Abit location in the entry marked as RES0 is nonzero. |
| I VRKNJ   | If FEAT_RME_GDI is implemented, the check of validity on level 1 GPT entries is performed on pairs of entries. See GPC faults.                                                          |
| I XJKRS   | This is to increase the probability of detecting errors relating to a loss of integrity of the memory holding the GPT.                                                                  |

## D9.6.1 GPT Table descriptor

RRCTBJ

AGPTTable descriptor contains a pointer to the base address of a next-level table, and fields describing properties relating to the remaining levels of walk.

IHKPQF

The following figure shows the level 0 GPT Table descriptor format:

## Level 0 GPT Table descriptor

Figure D9-2 Level 0 GPT Table descriptor format

<!-- image -->

RKCDQS

GPT Table descriptor bits[63:56] are RES0.

RLHVFM

GPT Table descriptor bits[55:52] are bits [55:52] of the next-level table address, if FEAT\_RME\_GPC3 is implemented and GPCCR\_EL3.PPS is configured to 56 bits, and are otherwise RES0.

RNWCYC

GPT Table descriptor bits[51:12] are bits [51:12] of the next-level table address.

RSFPYD

GPT Table descriptor bits[11:4] are RES0.

RGPPXX

GPT level 0 entry bits[3:0] are 0b0011 , indicating the entry is a GPT Table descriptor.

RDBTFW

The alignment of the next-level table address depends on the value of GPCCR\_EL3.PGS as follows: Descriptor bits [s-p-2:12] are RES0, where:

- s is derived from GPCCR\_EL3.L0GPTSZ as follows:
- p is derived from GPCCR\_EL3.PGS as follows:

| GPCCR_EL3.L0GPTSZ   | Size indicated   |   s |
|---------------------|------------------|-----|
| 0b0000              | 1GB              |  30 |
| 0b0100              | 16GB             |  34 |
| 0b0110              | 64GB             |  36 |
| 0b1001              | 512GB            |  39 |

| GPCCR_EL3.PGS   | Size indicated   |   p |
|-----------------|------------------|-----|
| 0b00            | 4KB              |  12 |
| 0b10            | 16KB             |  14 |
| 0b01            | 64KB             |  16 |

IBFKHR

Level 1 tables are aligned to their size in memory. The size of level 1 tables is determined by GPCCR\_EL3.PGS and GPCCR\_EL3.L0GPTSZ.

## D9.6.2 GPT Block descriptor

INKQNF

The following figure shows the level 0 GPT Block descriptor format:

<!-- image -->

Figure D9-3 Level 0 GPT Block descriptor format

| R PHBLQ   | GPT Block descriptor bits[63:8] are RES0.                                                                                                                                                                                                               |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FZGCP   | GPT Block descriptor bits[7:4] are the GPI value. For more information, see GPI field encoding in GPT descriptors.                                                                                                                                      |
| R FGPWN   | GPT level 0 entry bits[3:0] are 0b0001 , indicating the entry is a GPT Block descriptor.                                                                                                                                                                |
| R PLSSK   | GPT information from a level 0 GPT Block descriptor is permitted to be cached in a TLB as though the block is a contiguous region of granules, each of the size configured in GPCCR_EL3.PGS.                                                            |
| R YNKWN   | If the range encoded in the SIZE field of the invalidation covers the full address range of the Block, as advertised in GPCCR_EL3.L0GPTSZ, a TLBI RPA* operation is only required to invalidate cached information from a level 0 GPT Block descriptor. |
| R GXNNL   | When GPT configuration is changed between the two following structures, Granule protection checks continue to be made correctly, even if a TLBI is not issued:                                                                                          |

RGQPWL

- Alevel 0 GPT Block descriptor indicating a GPI value for a region.
- Alevel 0 GPT Table descriptor pointing at a level 1 table of Contiguous or Granules descriptors that have the same GPI value as the level 0 Block descriptor.

When a level 0 Table descriptor is replaced with a level 0 Block descriptor, the hardware may continue to access the level 1 Table until completion of a non-Last-level TLBI by PA, targeting at least the full address range of the level 0 descriptor. This means that the memory containing the level 1 Table cannot be reclaimed for other uses until completion of that TLBI by PA operation.

## D9.6.3 GPT Granules descriptor

INRSQJ

The following figure shows the level 1 GPT Granules descriptor format:

## Level 1 GPT Granules descriptor

| 63   | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 32 36 35   | 28 31   | 27   | 24 23   | 20 19   | 16 15   | 12 11   | 8 7   | 4 3   | 0   |
|------|---------|---------|---------|---------|---------|---------|------------|---------|------|---------|---------|---------|---------|-------|-------|-----|
| GPI  | GPI     | GPI     | GPI     | GPI     | GPI     | GPI     | GPI        | GPI     | GPI  | GPI     | GPI     | GPI     | GPI     | GPI   |       | GPI |

## Figure D9-4 Level 1 GPT Granules descriptor format

RHJWQH

An 8-byte GPT Granules descriptor contains the GPI values for 16 physical granules. For more information, see GPI field encoding in GPT descriptors.

RQDCZJ

The following table describes how the GPI values within one Granules descriptor are indexed:

| GPCCR_EL3.PGS   | Size indicated   | Within Granules descriptor   |
|-----------------|------------------|------------------------------|
| 0b00            | 4KB              | i = PA[15:12]                |
| 0b10            | 16KB             | i = PA[17:14]                |
| 0b01            | 64KB             | i = PA[19:16]                |

The GPI value to use is descriptor bits [(4* i ) + 3 : (4* i )].

GPT level 1 entry bits[3:0] are a valid GPI encoding, indicating the entry is a GPT Granules descriptor. For more information, see GPI field encoding in GPT descriptors.

## D9.6.4 GPT Contiguous descriptor

ISPSCW

The following figure shows the level 1 GPT Contiguous descriptor format:

## Level 1 GPT Contiguous descriptor

Figure D9-5 Level 1 GPT Contiguous descriptor format

<!-- image -->

| 63   |      | 10 9   | 8 7   | 3      |
|------|------|--------|-------|--------|
|      | RES0 | Contig | GPI   | 0b0001 |

RMVVWZ

GPT Contiguous descriptor bits[63:10] are RES0.

RJCXJC

GPT Contiguous descriptor bits[9:8] are the Contig field.

RJLQNJ

GPT Contiguous descriptor bits[7:4] are the GPI value. For more information, see GPI field encoding in GPT descriptors.

RBSSVP

GPT level 1 entry bits[3:0] are 0b0001 , indicating the entry is a GPT Contiguous descriptor.

RBFCGF

The following table describes the Contig field encoding:

| Value   | Meaning   |
|---------|-----------|
| 0b00    | Reserved  |
| 0b01    | 2MB       |
| 0b10    | 32MB      |
| 0b11    | 512MB     |

RMNZWK

Information from a GPT Contiguous descriptor is permitted to be cached in a TLB or a table walk cache for an input address range up to the size indicated by the Contig field.

RCZJSQ Contiguous regions are naturally-aligned.

- IQJZQH For example, if the Contig field in the Contiguous descriptor for address 0x8000\_4000 indicates a 2MB contiguous region, the region is 0x8000\_0000 to 0x801F\_FFFF .

RRQBNP GPT entries marked for contiguity are permitted, but not required, to be cached as block entries.

RSSKBB TLB Invalidation of GPT information is only guaranteed by TLB maintenance of the full contiguous range.

- IKBTDW For example, this might be done by executing a TLBI RPALOS, &lt;Xt&gt; instruction covering the full range of the contiguous GPT region.
- INZJDP This requirement on TLBI scope is intended to be the same as the behavior of the Contiguous bit in the VMSA. For more information, see The Contiguous bit.
- RSPLJH If any of the GPI values in GPT descriptors within the range specified by a Contig field differ from each other, then the GPT Contiguous descriptor has been misprogrammed .
- RSMQTZ For an access to a memory location within the range specified by the Contig field, if a GPT Contiguous descriptor has been misprogrammed, then in the absence of other faulting conditions it is CONSTRAINED UNPREDICTABLE whether one of the following occurs:
- The access succeeds as though its PA space is permitted by a programmed GPI value in the range.
- The access experiences a GPF consistent with the access not being permitted by one of the GPI values configured for the range.
- RNNHCF If a GPT Contiguous descriptor has the Contig field configured to one value, and other GPT Granules descriptors or Contiguous descriptors within the range indicated by that Contig field are all configured with the same GPI values, then in the absence of both misprogramming and faulting conditions, accesses to that range are correctly checked against the GPI value programmed for the range.

IJMVJS This behavior is intended to be the same as FEAT\_BBML2 behavior, but with the option of TLB Conflict aborts removed.

For more information, see Support levels for changing table or block size.

IRQFBR For more information, see:

- GPC faults
- GPT caching and invalidation

## D9.6.5 GPI field encoding in GPT descriptors

RGYQGW

The following table describes the GPI field encoding:

| Value     | Meaning                                                                                                                                                        |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000    | No accesses permitted.                                                                                                                                         |
| 0b0100    | Accesses permitted to System Agent PA space only. This encoding is reserved if GPCCR_EL3.SA is 0.                                                              |
| 0b0101    | Accesses permitted to Non-secure Protected PA space only. This encoding is reserved if GPCCR_EL3.NSP is 0.                                                     |
| 0b0110    | No accesses permitted. This encoding is reserved if GPCCR_EL3.NA6 is 0.                                                                                        |
| 0b0111    | No accesses permitted. This encoding is reserved if GPCCR_EL3.NA7 is 0.                                                                                        |
| 0b1000    | Accesses permitted to Secure PA space only. This encoding is reserved if FEAT_SEL2 is not implemented.                                                         |
| 0b1001    | Accesses permitted to Non-secure PA space only                                                                                                                 |
| 0b1010    | Accesses permitted to Root PA space only                                                                                                                       |
| 0b1011    | Accesses permitted to Realm PA space only                                                                                                                      |
| 0b1101    | Accesses permitted to Non-secure PA space only, by Non-secure or Root Security states. This encoding is reserved if the Effective value of GPCCR_EL3.NSO is 0. |
| 0b1111    | All accesses permitted                                                                                                                                         |
| Otherwise | Reserved                                                                                                                                                       |

| I XKBXW   | Since a PE is not permitted to access memory within the NSP or the SA PA spaces, GPI encodings 0b0100 to 0b0111 are effectively 'No access permitted' for PEs. These encodings are specified in the PE to allow it to distinguish between valid table entries with known encodings and invalid table entries that contain reserved encodings.   |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I YDVBY   | The GPI encoding All accesses permitted might be used for mapping peripherals that perform register banking based on the PA space of an access.                                                                                                                                                                                                 |
| I LJQWQ   | The 0b1101 GPI field encoding extends the GPC to distinguish between different Security states when checking access to the Non-secure PA space.                                                                                                                                                                                                 |