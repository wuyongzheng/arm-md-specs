## D8.7 Other descriptor fields

## D8.7.1 The Contiguous bit

ILYNXC

The Contiguous bit identifies a descriptor as belonging to a group of adjacent translation table entries that point to a contiguous OA range.

RSKQHL

RHMQXG

RCBXXM

If the Effective value of the Contiguous bit in a Block descriptor or Page descriptor is 1, and the descriptor would otherwise be permitted to be cached in a TLB, then all of the following apply:

- The entry is permitted to be cached in a TLB as though it is one of a number of adjacent translation table entries that point to a contiguous OA range with consistent attributes and permissions.
- Software is required to ensure that all of the adjacent translation table entries for the contiguous region point to a contiguous OA range with consistent attributes and permissions.

For VMSAv8-64 translation system, the Contiguous bit is RES0 and has an Effective value of 0 in all of the following Block descriptors:

- For the 4KB translation granule, if the Effective value of TCR\_ELx.DS or VTCR\_EL2.DS is 1, then the Contiguous bit is RES0 in the level 0 Block descriptor of that translation regime.
- For the 16KB translation granule, if the Effective value of TCR\_ELx.DS or VTCR\_EL2.DS is 1, then the Contiguous bit is RES0 in the level 1 Block descriptor of that translation regime.
- For the 64KB translation granules, if FEAT\_LPA is implemented, then the Contiguous bit is RES0 in a level 1 Block descriptor.

For a lookup level in a translation granule using the VMSAv8-64 translation system, if the Effective value of the Contiguous bit is 1, then the entry is permitted to be cached in a TLB as though all of the properties shown in the following table apply:

## Table D8-104 Permitted properties of caching a translation in a TLB when Effective value of Contiguous bit is 1, VMSAv8-64 translation system

| Translation granule   |   Block or Page lookup level |   Number of adjacent translation table entries | Alignment boundary of adjacent translation table entries within the translation table   | Alignment of contiguous OA range   |
|-----------------------|------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------|
| 4KB                   |                            1 |                                             16 | 128 bytes                                                                               | 16GB                               |
| 4KB                   |                            2 |                                             16 | 128 bytes                                                                               | 32MB                               |
| 4KB                   |                            3 |                                             16 | 128 bytes                                                                               | 64KB                               |
| 16KB                  |                            2 |                                             32 | 256 bytes                                                                               | 1GB                                |
| 16KB                  |                            3 |                                            128 | 1KB                                                                                     | 2MB                                |
| 64KB                  |                            2 |                                             32 | 256 bytes                                                                               | 16GB                               |
| 64KB                  |                            3 |                                             32 | 256 bytes                                                                               | 2MB                                |

RRLJBB

RCMKCR

For the VMSAv9-128 translation system, the Contiguous bit is RES0 and has an Effective value of 0 in all of the following Block descriptors:

- For the 4KB translation granule, the level 0 Block descriptor of that translation regime.
- For the 64KB translation granule, the level 1 Block descriptor of that translation regime.

For a lookup level in a translation granule using the VMSAv9-128 translation system, if the Effective value of the Contiguous bit is 1, then the entry is permitted to be cached in a TLB as though all of the properties shown in the following table apply:

## Table D8-105 Permitted properties of caching a translation in a TLB when Effective value of Contiguous bit is 1, VMSAv9-128 translation system

| Translation granule   |   Block or Page lookup level |   Number of adjacent translation table entries | Alignment boundary of adjacent translation table entries within the translation table   | Alignment of contiguous OA range   |
|-----------------------|------------------------------|------------------------------------------------|-----------------------------------------------------------------------------------------|------------------------------------|
| 4KB                   |                            1 |                                              4 | 64 bytes                                                                                | 1GB                                |
| 4KB                   |                            2 |                                             16 | 256 bytes                                                                               | 16MB                               |
| 4KB                   |                            3 |                                             16 | 256 bytes                                                                               | 64KB                               |
| 16KB                  |                            1 |                                              4 | 64 bytes                                                                                | 64GB                               |
| 16KB                  |                            2 |                                             16 | 256 bytes                                                                               | 256MB                              |
| 16KB                  |                            3 |                                             64 | 1KB                                                                                     | 1MB                                |
| 64KB                  |                            2 |                                             64 | 1KB                                                                                     | 16GB                               |
| 64KB                  |                            3 |                                             16 | 256 bytes                                                                               | 1MB                                |

RJDLPG

For the initial lookup table in a translation regime that uses the VMSAv9-128 translation system, the following table shows how the Disable Contiguous bit , DisCH n , is determined:

## Table D8-106 Determination of DisCHn for the initial lookup table

| Translation Regime   | VA Range (VA[55])   | DisCH           |
|----------------------|---------------------|-----------------|
| EL1&0                | Lower (0)           | TCR2_EL1.DisCH0 |
|                      | Upper (1)           | TCR2_EL1.DisCH1 |
| EL2&0                | Lower (0)           | TCR2_EL2.DisCH0 |
|                      | Upper (1)           | TCR2_EL2.DisCH1 |
| EL3                  | -                   | TCR_EL3.DisCH0  |

RWSVXT

For a translation regime that uses the VMSAv9-128 translation system, if the corresponding DisCH n field is 1, then the Effective value of the Contiguous bit in the initial lookup table Block and Page descriptors is 0.

RBBRTL

IVNXYF

For the VMSAv9-128 translation system, if the DisCH field in the next level table descriptor is 1, then the Effective value of the Contiguous bit in the stage 1 next level Block and Page descriptors is 0.

The architecture does not require descriptors with the Contiguous bit set to 1 to be cached as a single TLB entry for the contiguous region. To avoid TLB coherency issues, software is required to perform TLB maintenance on the entire address region that results from using the Contiguous bit.

ICQTNL If the Effective value of the Contiguous bit is 1, then hardware updates to the AF and dirty state can cause members in a group of contiguous translation table entries to have different AF, AP[2], and S2AP[1] values.

For more information, see Use of the Contiguous bit with hardware updates to the translation tables.

## D8.7.1.1 Misprogramming the Contiguous bit

RQTRPM For all descriptors within the range indicated by one or more descriptors that have the Contiguous bit set to 1, if one or more of the contiguous translation table entries does not have the Contiguous bit set to 1, then this is misprogramming of the Contiguous bit, and a TLB might contain overlapping entries.

RNGLXZ

For a TLB lookup in a contiguous region mapped by translation table entries that have the Contiguous bit misprogrammed, that TLB lookup is permitted to produce one of the following:

IHQWXX

- An OA, access permissions, and memory attributes that are consistent with any of the programmed translation table values.
- If BBM support levels 1 and 2 are not implemented, then an OA, access permissions, or memory attributes that are inconsistent with any of the programmed translation table values. For more information, see Support levels for changing table or block size.
- ATLBconflict abort.

RJQQTC For a TLB lookup in a contiguous region mapped by translation table entries that have consistent values for the Contiguous bit, but have the OA, attributes, or permissions misprogrammed, that TLB lookup is permitted to produce an OA, access permissions, and memory attributes that are consistent with any one of the programmed translation table values.

IPGVGZ The Contiguous bit is present only in valid Block and Page translation table descriptors, and therefore neither of the following configurations are considered as misprogramming of the Contiguous bit:

- Acontiguous range of descriptors that are each either invalid, or valid with Contiguous set to 1.
- Acontiguous range of descriptors that are each either invalid, or valid with Contiguous set to 0.

## D8.7.1.2 Architectural guarantees when the Contiguous bit is misprogrammed

RMWFWF If the Contiguous bit is misprogrammed, then the architecture guarantees all of the following:

- If physical memory regions are inaccessible through translation tables programmed at EL1 when the Contiguous bit is not misprogrammed, then they remain inaccessible to software executing at EL1 or EL0.
- If memory attributes and permissions are unattainable through translation tables programmed at EL1 when the Contiguous bit is not misprogrammed, then they remain unattainable to software executing at EL1 or EL0.
- Software executing in Non-secure state cannot access Secure, Realm, or Root physical memory.
- Software executing in Secure state cannot access Realm or Root physical memory.
- Software executing in Realm state cannot access Secure or Root physical memory.

RXFDVL The PE is required to generate an Address Size fault on accesses to addresses above the configured OA size, even in the case where the Contiguous bit is used to mark a set of Block descriptors as contiguous, such that the OA region translated by that contiguous set of descriptors exceeds the configured OA size.

- IJHQPP An implementation is permitted to ignore the Contiguous bit and treat it as 0 to ensure that OA range checking is done.

## D8.7.1.3 Implementation options when the Contiguous bit is misprogrammed

If software does all of the following, it is considered a programming error:

- The Contiguous bit is used to mark a set of translation table entries as contiguous.
- The address range translated by the set of translation table entries is larger than the IA size configured for the translation stage as determined by the TCR\_ELx.T n SZ field.

RWMNPV If the Contiguous bit is used to mark a set of translation table entries as contiguous and if the address range translated by the translation table entries is larger than the IA size supported by the translation stage, as defined by the TCR\_ELx.T n SZ field, then an implementation is permitted, but not required to, do one or more of the following:

- Generate a Translation fault.
- When all of the following apply, an implementation is permitted to not generate a Translation fault:
- -Atranslation table entry within a contiguous set of translation table entries is accessed.
- -The translation table entry is valid.

## D8.7.2 Page Based Hardware attributes

| I RHDNL   | The PBHAbits can be used for IMPLEMENTATION DEFINED purposes.                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XCJVR   | All statements in this section require implementation of FEAT_HPDS2.                                                                                                                                                  |
| R JVMMH   | For a stage 1 translation that uses TTBR0_ELx, if all of the following apply, then hardware can use the PBHAbit in the corresponding Block descriptor or Page descriptor bit[nn] for IMPLEMENTATION DEFINED purposes: |

- The corresponding TCR\_ELx.HWU nn bit, HWU62, HWU61, HWU60, or HWU59, is 1.
- TCR\_ELx.HPD0 is 1.

| R QSTMZ   | For a stage 1 translation that uses TTBR1_ELx, if all of the following apply, then hardware can use the PBHAbit in the corresponding Block descriptor or Page descriptor bit[nn] for IMPLEMENTATION DEFINED purposes: • The corresponding TCR_ELx.HWU1 nn bit, HWU162, HWU161, HWU160, or HWU159, is 1.                                                                                                                                                                                                                                                         |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R BHQKX   | For a stage 2 translation, if the value of VTCR_EL2.HWU nn is 1, then hardware can use the PBHAbit in the corresponding Block descriptor or Page descriptor bit[nn] for IMPLEMENTATION DEFINED purposes.                                                                                                                                                                                                                                                                                                                                                        |
| R VDFPM   | If the PBHAbit is used for IMPLEMENTATION DEFINED purposes, then setting the PBHAbit to 0 has the same behavior as when the PBHAbit is not used for IMPLEMENTATION DEFINED purposes.                                                                                                                                                                                                                                                                                                                                                                            |
| R PFZRK   | If the Effective value of TCR_ELx.HWU{0, 1} nn is 0, then the PBHAbit in the corresponding Block descriptor or Page descriptor bit[nn] is IGNORED.                                                                                                                                                                                                                                                                                                                                                                                                              |
| R TDLFM   | For any translation stage, if Overlay permissions are enabled, or for stage 1 translations, the Attribute Index Extension is enabled, then all of the following apply: • The Effective value of PBHA[3:0] is 0b0000 . • For stage 1 translations, the Effective value of the corresponding TCR_ELx.HWU nn bits are 0. • For stage 2 translations, the Effective value of the corresponding VTCR_EL2.HWU nn bits are 0. For more information, see Stage 1 Overlay permissions, Stage 2 Overlay permissions, and Stage 1 memory type and Cacheability attributes. |
| I TKJCZ   | The VMSAv9-128 translation system does not support the PBHAfields, and the TCR_ELx.HWU{0, 1} nn fields are RES0.                                                                                                                                                                                                                                                                                                                                                                                                                                                |

## D8.7.3 Table and Block entry

| R DFJNG   | All statements in this section require implementation of FEAT_BBML1.                                                                                                                                                                                                                                                                          |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I PJZBK   | The nT bit is supported in the following descriptors: • VMSAv8-64 Block descriptors. • VMSAv9-128 descriptors, when the SKL field in that descriptor is not 0.                                                                                                                                                                                |
| I XPRKH   | Setting the nT bit in a Table descriptor or Block descriptor guarantees that, when changing the table or block size, accesses translated by the translation table entry do not break coherency, ordering guarantees or uniprocessor semantics, or fail to clear the Exclusives monitors.                                                      |
| R MRRPW   | When using a Table descriptor or Block descriptor with the nT bit set to 1, all of the following apply: • It is IMPLEMENTATION DEFINED whether a Translation fault is generated. • If a Translation fault is not generated, a TLB conflict abort can be generated. For more information, see Support levels for changing table or block size. |
| I DXRJK   | If the nT bit in a Table descriptor or Block descriptor is 1, then the translation performance can be significantly impacted.                                                                                                                                                                                                                 |

## D8.7.4 XS attribute modifier

| I PMZTD   | The XS attribute indicates that an access to the memory region could take a long time to complete. Variants of DSB instructions and TLB maintenance instructions that do not depend on the completion of memory accesses with the XS attribute set to 1 are defined.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R DNHCL   | All statements in this section require implementation of FEAT_XS.                                                                                                                                                                                                      |
| R FQWJG   | For a stage 2 translation, the FnXS bit in a Block descriptor and Page descriptor has all of the following properties:                                                                                                                                                 |

RTDMCS

IZXKSJ

ISQFSD

IMTRQS

- If the FnXS bit is 0, then the XS attribute of the resultant memory translation is not modified.
- If the FnXS bit is 1, then the XS attribute of the resultant memory translation is set to 0.

For stage 2 translations, if the resultant memory attributes are Normal Inner Write-back, Outer Write-back Cacheable, then the XS attribute is set to 0 on the resultant memory translation.

If FEAT\_XS is implemented and the stage 1 memory type defined by the MAIR\_ELx or TCR\_ELx registers is one of the following, then the XS attribute is set to 0, otherwise the XS attribute is set to 1:

- Device memory types that use the MAIR\_ELx.Attr&lt; n &gt; encoding 0b0000dd01 .
- For Normal memory, one of the following:
- -Inner Write-Back Cacheable, Outer Write-back Cacheable memory types defined in the MAIR\_ELx or TCR\_ELx registers, including any memory types that are treated as Write-Back Cacheable as a result of IMPLEMENTATION DEFINED choices in the architecture.
- -Inner Write-through Cacheable and Outer Write-through Cacheable memory types that use the MAIR\_ELx.Attr&lt; n &gt; encoding 0b10100000 .
- -Inner Non-cacheable, Outer Non-cacheable memory types that use the MAIR\_ELx.Attr&lt; n &gt; encoding 0b01000000 .

The stage 2 impact of the FnXS bit applies for stage 1 translations in the EL1&amp;0 translation regime from AArch32 or AArch64.

For more information, see:

- Enabling and disabling the caching of memory accesses.
- Stage 1 memory type and Cacheability attributes.
- Stage 2 memory type and Cacheability attributes when FWB is enabled.