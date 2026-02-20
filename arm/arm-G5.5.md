## G5.5 The VMSAv8-32 Long-descriptor translation table format

The VMSAv8-32 Long-descriptor translation table format supports the assignment of memory attributes to memory Pages, at a granularity of 4KB, across the complete input address range. It also supports the assignment of memory attributes to blocks of memory, where a block can be 2MB or 1GB.

Note

- Although the VMSAv8-32 Long-descriptor format is limited to three levels of address lookup, its design and naming conventions support extension to additional levels, to support a larger input address range.
- Similarly, while the VMSAv8-32 implementation limits the output address range to 40 bits, its design supports extension to a larger output address range.

Figure G5-2 shows the different address translation stages. The Long-descriptor translation table format:

- Is used for:
- -The Non-secure EL2 stage 1 translation.
- -The Non-secure PL1&amp;0 stage 2 translation.
- Can be used for the Secure and Non-secure PL1&amp;0 translations.

When used for a stage 1 translation, the translation tables support an input address of up to 32 bits, corresponding to the VA address range of the PE.

When used for a stage 2 translation, the translation tables support an input address range of up to 40 bits, to support the translation from IPA to PA. If the input address for the stage 2 translation is a 32-bit address, then this address is zero-extended to 40 bits.

Note

When the Short-descriptor translation table format is used for the Non-secure stage 1 translations, this generates 32-bit IPAs. These are zero-extended to 40 bits to provide the input address for the stage 2 translation.

Overview of VMSAv8-32 address translation using Long-descriptor translation tables summarizes address translation from AArch32 state when using the Long-descriptor format translation tables.

The following sections then describe the format of the descriptors in the Long-descriptor format translation tables:

- VMSAv8-32 Long-descriptor Translation Table format descriptors.
- Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors.
- Control of Secure or Non-secure memory access, VMSAv8-32 Long-descriptor format.

The following sections then describe this translation table format:

- Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format.
- VMSAv8-32 Long-descriptor translation table format address lookup levels.
- Translation table walks, when using the VMSAv8-32 Long-descriptor translation table format.
- The algorithm for finding the translation table entries, VMSAv8-32 Long-descriptor format.

## G5.5.1 Overview of VMSAv8-32 address translation using Long-descriptor translation tables

Figure G5-8 gives a general view of VMSAv8-32 stage 1 address translation when using the Long-descriptor translation table format.

Figure G5-8 General view of VMSAv8-32 stage 1 address translation using Long-descriptor format

<!-- image -->

Figure G5-9 gives a general view of VMSAv8-32 stage 2 address translation. Stage 2 translation always uses the Long-descriptor translation table format.

Figure G5-9 General view of VMSAv8-32 stage 2 address translation, Long-descriptor translation table format

<!-- image -->

Use of concatenated translation tables for the initial stage 2 lookup describes how using concatenated level 2 tables means lookup can start at level 2, as referred to in Figure G5-9.

## G5.5.2 VMSAv8-32 Long-descriptor Translation Table format descriptors

As described in VMSAv8-32 Long-descriptor translation table format address lookup levels, the Long-descriptor translation table format provides up to three levels of address lookup. A translation table walk starts either at level 1 or level 2 of the address lookup.

In general, a descriptor is one of:

- An invalid or fault entry.
- Atable entry, that points to the next-level translation table.
- Ablock entry, that defines the memory properties for the access.
- Areserved format.

Bit[1] of the descriptor indicates the descriptor type, and bit[0] indicates whether the descriptor is valid.

The following sections describe the Long-descriptor Translation Table descriptor formats:

- VMSAv8-32 Long-descriptor level 1 and level 2 descriptor formats.
- VMSAv8-32 Long-descriptor translation table level 3 descriptor formats.

Information returned by a translation table lookup describes the classification of the non-address fields in the descriptors between address map control , access controls , and region attributes .

## G5.5.2.1 VMSAv8-32 Long-descriptor level 1 and level 2 descriptor formats

In the Long-descriptor translation tables, the formats of the level 1 and level 2 descriptors differ only in the size of the block of memory addressed by the Block descriptor. A block entry:

- In a level 1 table describes the mapping of the associated 1GB input address range.
- In a level 2 table describes the mapping of the associated 2MB input address range.

Figure G5-10 shows the Long-descriptor level 1 and level 2 descriptor formats:

<!-- image -->

Figure G5-10 VMSAv8-32 Long-descriptor level 1and level 2 descriptor formats

## G5.5.2.1.1 Descriptor encodings, Long-descriptor level 1 and level 2 formats

Descriptor bit[0] identifies whether the descriptor is valid, and is 1 for a valid descriptor. If a lookup returns an invalid descriptor, the associated input address is unmapped, and any attempt to access it generates a Translation fault.

Descriptor bit[1] identifies the descriptor type, and is encoded as:

- 0, Block

The descriptor gives the base address of a block of memory, and the attributes for that memory region.

- 1, Table The descriptor gives the address of the next level of translation table, and for a stage 1 translation, some attributes for that translation.

The other fields in the valid descriptors are:

## Block descriptor

Gives the base address and attributes of a block of memory:

- For a level 1 Block descriptor, bits[39:30] are bits[39:30] of the output address that specifies a 1GB block of memory.

## Table descriptor

- 1, Page
- For a level 2 Block descriptor, bits[39:21] are bits[39:21] of the output address that specifies a 2MBblock of memory.

In both cases, if bits[47:40] of the descriptor are not zero then a translation that uses the descriptor will generate an Address size fault, see Address size fault.

Bits[63:52, 11:2] provide attributes for the target memory block, see Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors. The position and contents of these bits is identical in the level 2 Block descriptor and in the level 3 Page descriptor.

Bits[39:m] are bits[39:m] of the address of the required next-level table. Bits[m-1:0] of the table address are zero:

- For a level 1 Table descriptor, this is the address of a level 2 table.
- For a level 2 Table descriptor, this is the address of a level 3 table.

In both cases, if bits[47:40] of the descriptor are not zero then a translation that uses the descriptor will generate an Address size fault, see Address size fault.

For a stage 1 translation only, bits[63:59] provide attributes for the next-level lookup, see Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors.

If the translation table defines the Non-secure PL1&amp;0 stage 1 translations, then the output address in the descriptor is the IPA of the target block or table. Otherwise, it is the PA of the target block or table.

## G5.5.2.2 VMSAv8-32 Long-descriptor translation table level 3 descriptor formats

Each entry in a level 3 table describes the mapping of the associated 4KB input address range.

Figure G5-11 shows the Long-descriptor level 3 descriptor formats.

<!-- image -->

Figure G5-11 VMSAv8-32 Long-descriptor level 3 descriptor formats

Descriptor bit[0] identifies whether the descriptor is valid, and is 1 for a valid descriptor. If a lookup returns an invalid descriptor, the associated input address is unmapped, and any attempt to access it generates a Translation fault.

Descriptor bit[1] identifies the descriptor type, and is encoded as:

## 0, Reserved, invalid

Behaves identically to encodings with bit[0] set to 0.

This encoding must not be used in level 3 translation tables.

Gives the address and attributes of a 4KB page of memory.

At this level, the only valid format is the Page descriptor. The other fields in the Page descriptor are:

## Page descriptor

Bits[39:12] are bits[39:12] of the output address for a page of memory.

If bits[47:40] of the descriptor are not zero, then a translation that uses the descriptor will generate an Address size fault, see Address size fault.

Bits[63:52, 11:2] provide attributes for the target memory page, see Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors. The position and contents of these bits are identical in the level 1 Block descriptor and in the level 2 Block descriptor.

If the translation table defines the Non-secure PL1&amp;0 stage 1 translations, then the output address in the descriptor is the IPA of the target page. Otherwise, it is the PA of the target page.

## G5.5.3 Attribute fields in VMSAv8-32 Long-descriptor translation table format descriptors

The memory attributes in the VMSAv8-32 Long-descriptor translation tables are based on those in the Short-descriptor translation table format, with some extensions. Memory region attributes describes these attributes. In the Long-descriptor translation table format:

- Table entries for stage 1 translations define attributes for the next level of lookup, see Next-level attributes in VMSAv8-32 Long-descriptor stage 1 Table descriptors.

The hierarchical permissions in the translation tables, APTable, XNTable, and PXNTable, permit subtrees of the translation tables to be used by different agents. Not all operating systems use this functionality, and so FEAT\_AA32HPD adds a facility to disable these bits.

This ability to disable hierarchical permissions bits has no effect on the NSTable bit.

- Block and Page entries define memory attributes for the target block or page of memory. Stage 1 and stage 2 translations have some differences in these attributes, see:
- -Attribute fields in VMSAv8-32 Long-descriptor stage 1 Block and Page descriptors.
- -Attribute fields in VMSAv8-32 Long-descriptor stage 2 Block and Page descriptors.

## G5.5.3.1 Next-level attributes in VMSAv8-32 Long-descriptor stage 1 Table descriptors

In a Table descriptor for a stage 1 translation, bits[63:59] of the descriptor define the following attributes for the next-level translation table access:

- NSTable, bit[63] For memory accesses from Secure state, specifies the Security state for subsequent levels of lookup, see Hierarchical control of Secure or Non-secure memory accesses, Long-descriptor format.

For memory accesses from Non-secure state, this bit is ignored.

- APTable, bits[62:61] Access permissions limit for subsequent levels of lookup, see Hierarchical control of access permissions, Long-descriptor format.

APTable[0] is reserved, SBZ, in the Non-secure EL2 stage 1 translation tables.

From Armv8.2, when FEAT\_AA32HPD is implemented, this field can be disabled.

When the value of TTBCR2.HPD0 or TTBCR2.HPD1 is 1, and the value of TTBCR.T2E is also 1:

- The value of the corresponding APTable field is IGNORED by hardware, allowing the field to be used by software.
- The behavior of the system is as if the value of the corresponding APTable field is 0, that is to say, the APTable field has an Effective value of 0.
- XNTable, bit[60] XNlimit for subsequent levels of lookup, see Hierarchical control of instruction fetching, Long-descriptor format.

From Armv8.2, when FEAT\_AA32HPD is implemented, this field can be disabled.

When the value of TTBCR2.HPD0 or TTBCR2.HPD1 is 1, and the value of TTBCR.T2E is also 1:

- The value of the corresponding XNTable field is IGNORED by hardware, allowing the field to be used by software.
- The behavior of the system is as if the value of the corresponding XNTable field is 0, that is to say, the XNTable field has an Effective value of 0.

PXNTable, bit[59] PXNlimit for subsequent levels of lookup, see Hierarchical control of instruction fetching, Long-descriptor format.

This bit is RES0 in the Non-secure EL2 stage 1 translation tables.

From Armv8.2, when FEAT\_AA32HPD is implemented, this field can be disabled.

When the value of TTBCR2.HPD0 or TTBCR2.HPD1 is 1 and the value of TTBCR.T2E is also 1:

- The value of the corresponding PXNTable field is ignored by hardware, allowing the field to be used by software.
- The behavior of the system is as if the value of the corresponding PXNTable field is 0, that is to say, the PXNTable field has an Effective value of 0.

## G5.5.3.2 Attribute fields in VMSAv8-32 Long-descriptor stage 1 Block and Page descriptors

In Block and Page descriptors, the memory attributes are split into an upper block and a lower block as shown for a stage 1 translation:

<!-- image -->

† IGNORED if FEAT\_HPDS2 is not implemented.

‡ RES0 for a translation regime that cannot apply to execution at EL0.

For a stage 1 descriptor, the attributes are:

## PBHA, bits[62:59]

Page-based hardware attributes bits.

These bits are IGNORED when FEAT\_HPDS2 is not implemented.

When FEAT\_HPDS2 is implemented, the HTCR and the TTBCR2 registers both contain a control bit for each PBHA bit in the translation tables that they control. When the value of that control bit is 1, and the value of the corresponding Hierarchical permission disables bit is 1, hardware can use that PBHA bit for IMPLEMENTATION DEFINED purposes. When the PBHA bit is used for IMPLEMENTATION DEFINED purposes, the value of 0 in the PBHA bit is a safe default setting that gives the same behavior as when the PBHA bit is not used for IMPLEMENTATION DEFINED purposes.

The control bits for this feature are:

For a Non-secure EL2 translation regime:

## HTCR.HWUnn

Controls whether Block or Page descriptor bit[nn] can be used by hardware.

These controls apply only when the value of HTCR.HPD is 1.

## For a PL1&amp;0 translation regime:

## TTBCR2.HWU1nn

For the translation tables indicated by TTBR1, controls whether Block or Page descriptor bit[nn] can be used by hardware.

These controls apply only when the value of TTBCR2.HPD1 is 1 and the value of TTBCR.T2E is 1.

## TTBCR2.HWU0nn

For the translation tables indicated by TTBR0, controls whether Block or Page descriptor bit[nn] can be used by hardware.

These controls apply only when the value of TTBCR2.HPD0 is 1 and the value of TTBCR.T2E is 1.

Implementation of FEAT\_HPDS2 requires the implementation of FEAT\_AA32HPD, which provides the Hierarchical permission disables bits. If FEAT\_AA32HPD is implemented but FEAT\_HPDS2 is not implemented, then the control bits are RAZ/WI but other aspects of FEAT\_AA32HPD functionality are implemented. If neither feature is implemented, then:

- The control bits are RAZ/WI.
- The FEAT\_AA32HPD identification registers indicate that the functionality is not supported, see FEAT\_AA32HPD.
- The TTBCR2 register encoding is treated as unallocated.
- XN, bit[54] The Execute-never field, see Access permissions for instruction execution.
- PXN, bit[53] The Privileged execute-never field, see Access permissions for instruction execution.

This bit is RES0 in the Non-secure EL2 stage 1 translation tables.

## Contiguous, bit[52]

Indicates that 16 adjacent translation table entries point to contiguous memory regions, see Contiguous bit.

nG, bit[11]

The not global bit. Determines how the translation is marked in the TLB, see Global and process-specific translation table entries.

This bit is RES0 in the Non-secure EL2 stage 1 translation tables.

- AF, bit[10] The Access flag, see The Access flag.
- SH, bits[9:8] Shareability field, see Memory region attributes.

## AP[2:1], bits[7:6]

Access Permissions bits, see Memory access control.

Note

For consistency with the Short-descriptor translation table formats, the Long-descriptor format defines AP[2:1] as the Access Permissions bits, and does not define an AP[0] bit.

AP[1] is RES1 in the Non-secure EL2 stage 1 translation tables.

- NS, bit[5] Non-secure bit. For memory accesses from Secure state, specifies whether the output address is in Secure or Non-secure memory, see Control of Secure or Non-secure memory access, VMSAv8-32 Long-descriptor format.

For memory accesses from Non-secure state, this bit is RES0 and is ignored by the PE.

## AttrIndx[2:0], bits[4:2]

Stage 1 memory attributes index field, for the indicated Memory Attribute Indirection Register, see VMSAv8-32 Long-descriptor format memory region attributes.

The definition of IGNORED means the architecture guarantees that the PE makes no use of the field, see IGNORED. For more information about these fields, see Other fields in the Long-descriptor translation table format descriptors.

## G5.5.3.3 Attribute fields in VMSAv8-32 Long-descriptor stage 2 Block and Page descriptors

In Block and Page descriptors, the memory attributes are split into an upper block and a lower block as shown for a stage 2 translation:

<!-- image -->

- ‡ Bit[53] is RES0 if FEAT\_XNX is not implemented.
- † Bits [62:60] are IGNORED and reserved for use by System MMU if FEAT\_HPDS2 is not implemented. Bits [59] is IGNORED if FEAT\_HPDS2 is not implemented.

For a stage 2 descriptor, the attributes are:

## PBHA[3:1], bits[62:60]

Page-based hardware attributes bits.

These bits are IGNORED and reserved for System MMU use when FEAT\_HPDS2 is not implemented.

When FEAT\_HPDS2 is implemented, VTCR\_EL2 has a control bit for each PBHA bit in the EL1&amp;0 stage 2 translation tables:

- When the value of that control bit is 1, hardware can use the corresponding PBHA bit for IMPLEMENTATION DEFINED purposes. When the PBHA bit is used for IMPLEMENTATION DEFINED purposes, the value of 0 in the PBHA bit is a safe default setting that gives the same behavior as when the PBHA bit is not used for IMPLEMENTATION DEFINED purposes.
- When the value of that control bit is 0, the corresponding PBHA bit is IGNORED and reserved for System MMU use.

## PBHA[0], bit[59]

Page-based hardware attributes bit.

This bit is IGNORED when FEAT\_HPDS2 is not implemented.

When FEAT\_HPDS2 is implemented, VTCR\_EL2 has a control bit for this bit in the EL1&amp;0 stage 2 translation tables:

- When the value of that control bit is 1, hardware can use this bit for IMPLEMENTATION DEFINED purposes. When the PBHA bit is used for IMPLEMENTATION DEFINED purposes, the value of 0 in the PBHA bit is a safe default setting that gives the same behavior as when the PBHA bit is not used for IMPLEMENTATION DEFINED purposes.
- When the value of that control bit is 0, this bit is IGNORED.

## XN[1:0], bits[54:53]

The stage 2 Execute-never field, see Access permissions for instruction execution.

If FEAT\_XNX is not implemented, bit[53] is RES0.

## Contiguous, bit[52]

Indicates that 16 adjacent translation table entries point to contiguous memory regions, see Contiguous bit.

AF, bit[10]

The Access flag, see The Access flag.

SH, bits[9:8]

Shareability field, see EL2 control of Non-secure memory region attributes.

S2AP, bits[7:6]

Stage 2 Access Permissions bits, see Hyp mode control of Non-secure access permissions.

Note

In the original VMSAv7-32 Long-descriptor attribute definition, this field was called HAP[2:1], for consistency with the AP[2:1] field in the stage 1 descriptors and despite there being no HAP[0] bit. VMSAv8-32 renames the field for greater clarity.

## MemAttr, bits[5:2]

Stage 2 memory attributes, see EL2 control of Non-secure memory region attributes.

The definition of IGNORED means the architecture guarantees that the PE makes no use of the field, see IGNORED. For more information about these fields, see Other fields in the Long-descriptor translation table format descriptors.

## G5.5.4 Control of Secure or Non-secure memory access, VMSAv8-32 Long-descriptor format

Access to the Secure or Non-secure PA map describes how the NS bit in the translation table entries:

- For accesses from Secure state, determines whether the access is to Secure or Non-secure memory.
- Is ignored by accesses from Non-secure state.

In the Long-descriptor format:

- The NS bit relates only to the memory block or page at the output address defined by the descriptor.
- The descriptors also include an NSTable bit, see Hierarchical control of Secure or Non-secure memory accesses, Long-descriptor format.

The NS and NSTable bits are valid only for memory accesses from Secure state. Memory accesses from Non-secure state ignore the values of these bits.

## G5.5.4.1 Hierarchical control of Secure or Non-secure memory accesses, Long-descriptor format

For Long-descriptor Format Table descriptors for stage 1 translations, the descriptor includes an NSTable bit, which indicates whether the table identified in the descriptor is in Secure or Non-secure memory. For accesses from Secure state, the meaning of the NSTable bit is:

- NSTable == 0 The defined table address is in the Secure PA map. In the descriptors in that translation table, NS bits and NSTable bits have their defined meanings.
- NSTable == 1 The defined table address is in the Non-secure PA map. Because this table is fetched from the Non-secure address map, the NS and NSTable bits in the descriptors in this table must be ignored. This means that, for this table:
- The value of the NS bit in any Block or Page descriptor is ignored. The block or page address refers to Non-secure memory.
- The value of the NSTable bit in any Table descriptor is ignored, and the table address refers to Non-secure memory. When this table is accessed, the NS bit in any Block or Page descriptor is ignored, and all descriptors in the table refer to Non-secure memory.

In addition, an entry fetched in Secure state is treated as non-global if it is read from Non-secure memory. That is, these entries must be treated as if nG==1, regardless of the value of the nG bit. For more information about the nG bit, see Global and process-specific translation table entries.

The effect of NSTable applies to later entries in the translation table walk, and so its effects can be held in one or more TLB entries. Therefore, a change to NSTable requires coarse-grained invalidation of the TLB to ensure that the effect of the change is visible to subsequent memory transactions.

Note

- When using the Long-descriptor Format, Table descriptors are defined only for the level 1 and level 2 of lookup.
- Stage 2 translations are performed only for operations in Non-secure state, that can access only the Non-secure address map. Therefore, the stage 2 descriptors do not include NS or NSTable bits.

## G5.5.5 Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format

As described in Determining the translation table base address in the VMSAv8-32 translation regimes, two sets of translation tables can be defined for each of the PL1&amp;0 stage 1 translations, and TTBR0 and TTBR1 hold the base addresses for the two sets of tables. The Long-descriptor translation table format provides more flexibility in defining the boundary between using TTBR0 and using TTBR1. When a PL1&amp;0 stage 1 address translation is enabled, TTBR0 is always used. If TTBR1 is also used then:

- TTBR1 is used for the top part of the input address range.
- TTBR0 is used for the bottom part of the input address range.

The TTBCR.T0SZ and TTBCR.T1SZ size fields control the use of TTBR0 and TTBR1, as Table G5-2 shows.

## Table G5-2 Use of TTBR0 and TTBR1, Long-descriptor format

| TTBCR   |       | Input address range using:    |                                           |
|---------|-------|-------------------------------|-------------------------------------------|
| 0b000   | 0b000 | All addresses                 | Not used                                  |
| M a     | 0b000 | Zero to (2 (32- M ) -1)       | 2 32- M to maximum input address          |
| 0b000   | N a   | Zero to (2 32 -2 (32- N ) -1) | 2 32 -2 (32- N ) to maximum input address |
| M a     | N a   | Zero to (2 (32- M ) -1)       | 2 32 -2 (32- N ) to maximum input address |

For stage 1 translations, the input address is always a V A, and the maximum possible V A is (2 32 -1).

When address translation is using the Long-descriptor translation table format:

- Figure G5-12 shows how, when TTBCR.T1SZ is zero, the value of TTBCR.T0SZ controls the boundary between VAs that are translated using TTBR0, and V As that are translated using TTBR1.

Figure G5-12 Control of TTBR boundary, when TTBCR.T1SZ is zero

<!-- image -->

- Figure G5-13 shows how, when TTBCR.T1SZ is nonzero, the values of TTBCR.T0SZ and TTBCR.T1SZ control the boundaries between V As that are translated using TTBR0, and V As that are translated using TTBR1.

Figure G5-13 Control of TTBR boundaries, when TTBCR.T1SZ is nonzero

<!-- image -->

When T0SZ and T1SZ are both nonzero:

- -If both fields are set to 0b001 , the boundary between the two regions is 0x8000\_0000 . This is identical to having T0SZ set to 0b000 and T1SZ set to 0b001 .
- -Otherwise, the TTBR0 and TTBR1 regions are non-contiguous. In this case, any attempt to access an address that is in that gap between the TTBR0 and TTBR1 regions generates a Translation fault.

Note

The handling of the Contiguous bit can mean that the boundary between the translation regions defined by the TCR\_EL1.TnSZ values and the region for which an access generates a Translation fault is wider than shown in Figure G5-13. That is, if the descriptor for an access to the region shown as generating a fault has the Contiguous bit set to 1, the access might not generate a fault. Possible errors in programming the translation table registers describes this possibility.

When using the Long-descriptor translation table format:

- The TTBCR contains fields that define memory region attributes for the translation table walk, for each TTBR. These are the SH0, ORGN0, IRGN0, SH1, ORGN1, and IRGN1 bits.

- TTBR0 and TTBR1 each contain an ASID field, and the TTBCR.A1 field selects which ASID to use.

For this translation table format, VMSAv8-32 Long-descriptor translation table format address lookup levels summarizes the lookup levels, and Translation table walks, when using the VMSAv8-32 Long-descriptor translation table format describes the possible translations.

## G5.5.5.1 Possible errors in programming the translation table registers

In all the descriptions in this subsection, the size of the input address supported for a PL1&amp;0 stage 1 translation refers to the size specified by a TTBCR.TxSZ field.

Note

For a PL1&amp;0 stage 1 translation, the input address range can be split so that the lower addresses are translated by TTBR0 and the higher addresses are translated by TTBR1. In this case, each of input address sizes specified by TTBCR.{T0SZ, T1SZ} is smaller than the total address size supported by the stage of translation.

The following are possible errors in the programming of TTBR0, TTBR1, and TTBCR. For the translation of a particular address at a particular stage of translation, either:

- The block size being used to translate the address is larger than the size of the input address supported at a stage of translation used in performing the required translation. This can occur only for the PL1&amp;0 stage 1 translations, and only when either TTBCR.T0SZ or TTBCR.T1SZ is zero, meaning there is no gap between the address range translated by TTBR0 and the range translated by TTBR1. In this case, this programming error occurs if a block translated from the region that has TxSZ set to zero straddles the boundary between the two address ranges. Example G5-2 shows an example of this mis-programming.
- The address range translated by a set of blocks marked as contiguous, by use of the contiguous bit, is larger than the size of the input address supported at a stage of translation used in performing the required translation.

## Example G5-2 Error in programming the translation table registers

If TTBCR.T0SZ is programmed to 0 and TTBCR.T1SZ is programmed to 7, this means:

- TTBR0 translates addresses in the range 0x0000\_0000 -0xFDFF\_FFFF .
- TTBR1 translates addresses in the range 0xFE00\_0000 -0xFFFF\_FFFF .

The translation table indicated by TTBR0 might be programmed with a block entry for a 1GB region starting at 0xC000\_0000 . This covers the address range 0xC000\_0000 -0xFFFF\_FFFF , that overlaps the TTBR1 address range. This means this block size is larger than the input address size supported for translations using TTBR0, and therefore this is a programming error.

To understand why this must be a programming error, consider a memory access to address 0xFFFF\_0000 . According to the TTBCR.{T0SZ, T1SZ} values, this must be translated using TTBR1. However, the access matches a TLB entry for the translation, using TTBR0, of the block at 0xC000\_0000 . Hardware is not required to detect that the access to 0xFFFF\_0000 is being translated incorrectly.

In these cases, an implementation might use one of the following approaches:

- Treat such a block as causing a Translation fault, even though the block is valid, and the address accessed within that block is within the size of the input address supported at a stage of translation. The block might be a block within a contiguous set of blocks.
- Treat such a block as not causing a Translation fault, even though the address accessed within that block is outside the size of the input address supported at a stage of translation, provided that both of the following apply:
- -The block is valid.
- -At least one address within the block, or contiguous set of blocks, is within the size of the input address supported at a stage of translation.

The block might be a block within a contiguous set of blocks.

Additional constraints apply to programming the VTCR, see Determining the required initial lookup level for stage 2 translations.

## G5.5.6 VMSAv8-32 Long-descriptor translation table format address lookup levels

As stated at the start of this section, because the Long-descriptor translation table format is used for the Non-secure PL1&amp;0 stage 2 translations, the format must support input addresses of up to 40 bits.

Table G5-3 summarizes the properties of the different levels of address lookup when using this format.

Table G5-3 Properties of the three levels of address lookup with VMSAv8-32 Long-descriptor translation tables

| Level   | Input address   |                     | Output address a   | Output address a   | Number of entries   |
|---------|-----------------|---------------------|--------------------|--------------------|---------------------|
|         | Size            | Address range b     | Size               | Address range      |                     |
| First   | Up to 512GB     | Up to Address[38:0] | 1GB                | Address[39:30]     | Up to 512           |
| Second  | Up to 1GB       | Up to Address[29:0] | 2MB                | Address[39:21]     | Up to 512           |
| Third   | 2MB             | Address[20:0]       | 4KB                | Address[39:12]     | 512                 |

b. Input address range for the translation table. See Use of concatenated level 1 translation tables for details of support for additional bits of address at a given level, including possible support of a 40-bit input address range for stage 2 translations at level 1. For stage 1 translations at level 1 the input address range is limited to the V A size of [31:0].

For level 1 and level 2 tables, reducing the input address range reduces the number of addresses in the table and therefore reduces the table size. The appropriate Translation Table Control Register specifies the input address range.

Stage 1 translations require an input address range of up to 32 bits, corresponding to V A[31:0]. For these translations:

- For a memory access from a mode other than Hyp mode, the Secure or Non-secure TTBR0 or TTBR1 holds the translation table base address, and the Secure or Non-secure TTBCR is the control register.
- For a memory access from Hyp mode, HTTBR holds the translation table base address, and HTCR is the control register.

Note

For translations controlled by TTBR0 and TTBR1, if neither TTBR has an input address range larger than 1GB, then translation starts at level 2. Together, TTBR0 and TTBR1 can still cover the 32-bit V A input address range.

Stage 2 translations require an input address range of up to 40 bits, corresponding to IPA[39:0], and the supported input address size is configurable in the range 25-40 bits. Table G5-3 indicates a requirement for the translation mechanism to support a 39-bit input address range, Address[38:0]. Use of concatenated translation tables for the initial stage 2 lookup describes how a 40-bit IPA address range is supported. For stage 2 translations:

- VTTBR holds the translation table base address, and VTCR is the control register.
- If a supplied input address is larger than the configured input address size, a Translation fault is generated.

## G5.5.6.1 Use of concatenated translation tables for the initial stage 2 lookup

If a stage 2 translation would require 16 entries or fewer in its top-level translation table, that stage of translation can, instead, be configured so that:

- It requires the corresponding number of concatenated translation tables at the next translation level, aligned to the size of the block of concatenated translation tables.
- The stage 2 translation starts at that next translation level.

Note

Stage 2 translations always use the Long-descriptor translation table format.

This use of concatenated translation tables is:

- Required when the stage 2 translation supports a 40-bit input address range, see Use of concatenated level 1 translation tables.
- Supported for a stage 2 translation with an input address range of 31-34 bits, see Use of concatenated level 2 translation tables.

The use of concatenated translation tables requires the software that is defining the translation to:

- Define the concatenated translation tables with the required overall alignment.
- Program VTTBR to hold the address of the first of the concatenated translation tables.
- Program VTCR to indicate the required input address range and initial lookup level.

Note

The use of concatenated translation tables avoids the overhead of an additional level of translation.

## G5.5.6.1.1 Use of concatenated level 1 translation tables

The Long-descriptor format translation tables provide 9 bits of address resolution at each level of lookup. However, a 40-bit input address range with a translation granularity of 4KB requires a total of 28 bits of address resolution. Therefore, a stage 2 translation that supports a 40-bit input address range requires two concatenated level 1 translation tables, together aligned to 8KB, where:

- The table at the address with PA[12:0]== 0b0\_0000\_0000\_0000 defines the translations for input addresses with bit[39]==0.
- The table at the address with PA[12:0]== 0b1\_0000\_0000\_0000 defines the translations for input addresses with bit[39]==1.
- The 8KB alignment requirement means that both tables have the same value for PA[39:13].

## G5.5.6.1.2 Use of concatenated level 2 translation tables

Astage 2 translation with an input address range of 31-34 bits can start the translation either:

- With a level 1 lookup, accessing a level 1 translation table with 2-16 entries.
- With a level 2 lookup, accessing a set of concatenated level 2 translation tables.

Table G5-4 shows these options, for each of the input address ranges that can use this scheme.

Note

Because these are stage 2 translations, the input address range is an IPA range.

## Table G5-4 Possible uses of concatenated translation tables for level 2 lookup

| Input address range   | Input address range   | Lookup starts at level 1   | Lookup starts at level 2      | a                  |
|-----------------------|-----------------------|----------------------------|-------------------------------|--------------------|
| IPA range             | Size                  | Required level 1 entries   | Number of concatenated tables | Required alignment |
| IPA[30:0]             | 2 31 bytes            | 2                          | 2                             | 8KB                |
| IPA[31:0]             | 2 32 bytes            | 4                          | 4                             | 16KB               |
| IPA[32:0]             | 2 33 bytes            | 8                          | 8                             | 32KB               |
| IPA[33:0]             | 2 34 bytes            | 16                         | 16                            | 64KB               |

See also Determining the required initial lookup level for stage 2 translations.

## G5.5.7 Translation table walks, when using the VMSAv8-32 Long-descriptor translation table format

Figure G5-2 shows the possible address translations. If a stage of translation is controlled from an Exception level that is using AArch32, the input and output address constraints and the registers that control the translation are as follows:

## Stage 1 translations

For all stage 1 translations:

- The input address range is up to 32 bits, as determined by either:
- -TTBCR.T0SZ or TTBCR.T1SZ, for a PL1&amp;0 stage 1 translation.
- -HTCR.T0SZ, for an EL2 stage 1 translation.
- The output address range is 40 bits.

The stage 1 translations are:

## Non-secure PL1&amp;0 stage 1 translation

The stage 1 translation for memory accesses from Non-secure modes other than Hyp mode. This translates a V A to an IPA. For this translation, when Non-secure EL1 is using AArch32:

- Non-secure TTBR0 or TTBR1 holds the translation table base address.
- Non-secure TTBCR determines which TTBR is used.

## Non-secure EL2 stage 1 translation

The stage 1 translation for memory accesses from Hyp mode, translates a V A to a PA. For this translation, when EL2 is using AArch32, HTTBR holds the translation table base address.

## Secure PL1&amp;0 stage 1 translation

The stage 1 translation for memory accesses from Secure modes, translates a V A to a PA. For this translation, when the Secure PL1 modes are using AArch32:

- Secure TTBR0 or TTBR1 holds the translation table base address.
- Secure TTBCR determines which TTBR is used.

## Stage 2 translation

## Non-secure PL1&amp;0 stage 2 translation

The stage 2 translation for memory accesses from Non-secure modes other than Hyp mode, and translates an IPA to a PA. For this translation, when EL2 is using AArch32:

- The input address range is 40 bits, and VTCR.T0SZ determines the input address size.
- The output address range depends on the implemented memory system, and is up to 40 bits.
- VTTBR holds the translation table base address.
- VTCRspecifies the required input address range, and whether the initial lookup is at level 1 or at level 2.

The descriptions of the VMSAv8-32 translation stages state that the maximum output address size is 40 bits. However, the register and Long-descriptor Format descriptor fields that hold these addresses are 48 bits wide. If bits[47:40] of an output address are not all zero, then the address generates an Address size fault.

The Long-descriptor translation table format provides up to three levels of address lookup, as described in VMSAv8-32 Long-descriptor translation table format address lookup levels, and the initial lookup, in which the MMU reads the translation table base address, is at either level 1 or level 2. The following determines the level of the initial lookup:

- For a stage 1 translation, the required input address range. For more information, see Determining the required initial lookup level for stage 1 translations.
- For a stage 2 translation, the level specified by the VTCR.SL0 field. For more information, see Determining the required initial lookup level for stage 2 translations.

Note

For a stage 2 translation, the size of the required input address range constrains the VTCR.SL0 value.

Figure G5-14 shows how the descriptor address for the initial lookup for a translation using the Long-descriptor translation table format is determined from the input address and the TTBR value. This figure shows the lookup for a translation that starts with a level 1 lookup, that translates bits[39:30] of the input address, zero extended if necessary.

Figure G5-14 VMSAv8-32 Long-descriptor initial lookup, starting at level 1

<!-- image -->

If bits[47:40] of the TTBR are not zero then the initial lookup will generate an Address size fault, see Address size fault. For a translation that starts with a level 1 lookup, as shown in Figure G5-14:

## For a stage 1 translation

n is in the range 4-5 and:

- For a memory access from Hyp mode:
- -HTTBR is the TTBR.
- -n =5-(HTCR.T0SZ).
- For other accesses:
- -The Secure or Non-secure instance of TTBR0 or TTBR1 is the TTBR.
- -n =(5-TTBCR.T x SZ), where x is 0 when using TTBR0, and 1 when using TTBR1.

## For a stage 2 translation

n is in the range 4-13 and:

- VTTBR is the TTBR.
- n =5-(VTCR.T0SZ).

For a translation that starts with a level 2 lookup, the descriptor address is obtained in the same way, except that bits[( n +17):21] of the input address provide bits[( n -1):3] of the descriptor address, where:

## For a stage 1 translation

n is in the range 7-12. As Determining the required initial lookup level for stage 1 translations shows, for a stage 1 translation to start with a level 2 lookup, the corresponding T0SZ or T1SZ field must be 2 or more. This means:

- For a memory access from Hyp mode, n =14-HTCR.T0SZ.
- For other memory accesses, n =14-(TTBCR.T x SZ), where x is 0 when using TTBR0, and 1 when using TTBR1.

## For a stage 2 translation

n is in the range 7-16. For a stage 2 translation to start with a level 2 lookup, VTCR.SL0 is 0b00 , and n =14-(VTCR.T0SZ).

The following sections describe how the level of the initial lookup is determined:

- Determining the required initial lookup level for stage 1 translations.
- Determining the required initial lookup level for stage 2 translations.

Address translation examples using the VMSAv8-32 Long descriptor translation table format shows examples of full translation flows, to an entry for a 4KB memory page, for lookups starting at level 1 and lookups starting at level 2.

## G5.5.7.1 Determining the required initial lookup level for stage 1 translations

For a stage 1 translation, the required input address range, indicated by a T0SZ or T1SZ field in a translation table control register, determines the initial lookup level. The size of this input address region is 2 (32-T x SZ) bytes, and if this size is:

- Less than or equal to 2 30 bytes, the required start is at level 2, and translation requires two levels of table to map to 4KB pages. This corresponds to a T x SZ value of 2 or more.
- More than 2 30 bytes, the required start is at level 1, and translation requires three levels of table to map to 4KB pages. This corresponds to a T x SZ value that is less than 2.

For the PL1&amp;0 stage 1 translations, the TTBCR:

- Splits the 32-bit V A input address range between TTBR0 and TTBR1, see Selecting between TTBR0 and TTBR1, VMSAv8-32 Long-descriptor translation table format.
- Holds the input address range sizes for TTBR0 and TTBR1, in the TTBCR.T0SZ and TTBCR.T1SZ fields.

For the EL2 stage 1 translations, HTCR.T0SZ indicates the size of the required input address range. For example, if this field is 0b000 , it indicates a 32-bit V A input address range, and translation lookup must start at level 1.

## G5.5.7.2 Determining the required initial lookup level for stage 2 translations

For a PL1&amp;0 stage 2 translation, the output address range from the PL1&amp;0 stage 1 translations determines the required input address range for the stage 2 translation.

VTCR.SL0 indicates the starting level for the lookup. The permitted SL0 values are:

| 0b00   | Stage 2 translation lookup must start at level 2.   |
|--------|-----------------------------------------------------|
| 0b01   | Stage 2 translation lookup must start at level 1.   |

In addition, VTCR.T0SZ must indicate the required input address range. The size of the input address region is 2 (32-T0SZ) bytes.

Note

VTCR.T0SZ holds a four-bit signed integer value, meaning it supports values from -8 to 7. This is different from the other translation control registers, where T n SZ holds a three-bit unsigned integer, supporting values from 0 to 7.

The programming of VTCR must follow the constraints shown in Table G5-5, otherwise any attempt to perform a translation table walk that uses the stage 2 address translation generates a stage 2 level 1 Translation Fault. The table also shows how the VTCR.SL0 and VTCR.T0SZ values determine the VTTBR.BADDR field width.

Note

If VTCR.SL0 is programmed to a reserved value then the constraints shown in Table G5-5 are not met, and a translation table walk that uses stage 2 translation generates a stage 2 level 1 Translation fault.

Table G5-5 Input address range constraints on programming VTCR

| VTCR.SL0   | VTCR.T0SZ   | Input address range, R   | Initial lookup level   | BADDR[39:x] width a   |
|------------|-------------|--------------------------|------------------------|-----------------------|
| 0b00       | 2 to 7      | R ≤ 2 30 bytes           | Level 2                | [39:12] to [39:7]     |
| 0b00       | -2 to 1     | 2 30 <R ≤ 2 34 bytes     | Level 2                | [39:16] to [39:13]    |
| 0b01       | -2 to 1     |                          | Level 1                | [39:7] to [39:4]      |
| 0b01       | -8 to -3    | 2 34 <R                  | Level 1                | [39:13] to [39:8]     |

In addition, VTCR.S must be programmed to the value of T0SZ[3], otherwise behavior is CONSTRAINED UNPREDICTABLE with the resulting behavior being that VTCR.T0SZ is treated as an UNKNOWN value.

Note

VTCR.T0SZ being treated as an UNKNOWN value results in a stage 2 level 1 Translation Fault if that UNKNOWN value is not consistent with the programmed value of VTCR.SL0.

CONSTRAINED UNPREDICTABLE behaviors associated with the VTCR describes these CONSTRAINED UNPREDICTABLE behaviors.

Where necessary, the initial lookup level provides multiple concatenated translation tables, as described in Use of concatenated level 2 translation tables. This section also gives more information about the alternatives, shown in Table G5-5, when R is in the range 2 31 - 2 34 .

## G5.5.8 The algorithm for finding the translation table entries, VMSAv8-32 Long-descriptor format

This section gives the algorithm for finding the translation table entry that corresponds to a given IA, for each required level of lookup. The algorithm encodes the descriptions of address translation given earlier in this section. The VMSAv8-32 Long-descriptor format uses a 4KB translation granule.

The description uses the following terms:

BaseAddr

IA

The base address for the level of lookup, as defined by:

- For the initial lookup level, the TTBR.BADDR base address field in the appropriate TTBR, see the description of T n SZ.
- Otherwise, the translation table address returned by the previous level of lookup.

The supplied IA for this stage of translation.

T n SZ The translation table size for this stage of translation:

For PL1&amp;0 stage 1 Either:

- TTBCR.T0SZ if the translation is using TTBR0.
- TTBCR.T1SZ if the translation is using TTBR1.

For PL1&amp;0 stage 2 VTCR.T0SZ. The translation uses VTTBR.

SL0

For EL2 stage 1 HTCR.T0SZ. The translation uses HTTBR.

VTCR.SL0. Applies to the Non-secure PL1&amp;0 stage 2 translation only.

Table G5-6 shows the Translation Table descriptor address, for each level of lookup. The table shows only architecturally-valid programming of the TCR. See also Possible errors in programming the translation table registers.

## Table G5-6 Translation table entry addresses, VMSAv8-32 using Long-descriptor format

| Lookup level   | Entry address and conditions Stage 1 translation                                           | Stage 2 translation                                                                                                        | General conditions   |
|----------------|--------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|----------------------|
| One            | BaseAddr[39: x ]:IA[ y :30]: 0b000 if a 0 ≤ T n SZ ≤ 1 then x = (5 - T n SZ)               | BaseAddr[39: x ]:IA[ y :30]: 0b000 if SL0 b == 1 then if a -8 ≤ T0SZ ≤ 1 then x = (5 - T0SZ)                               | y = ( x + 26)        |
| Two            | BaseAddr[39: x ]:IA[ y :21]: 0b000 if a 2 ≤ T n SZ ≤ 7 then x = (14 - T n SZ) else c x =12 | BaseAddr[39: x ]:IA[ y :21]: 0b000 if SL0 == 0 then if a -2 ≤ T0SZ ≤ 7 then x = (14 - T0SZ) elsif c SL0 b == 1 then x = 12 | y = ( x + 17)        |
| Three          | BaseAddr[39:12]:IA[20:12]: 0b000                                                           | BaseAddr[39:12]:IA[20:12]: 0b000                                                                                           | -                    |