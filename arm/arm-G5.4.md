## G5.4 The VMSAv8-32 Short-descriptor translation table format

The Short-descriptor translation table format supports a memory map based on memory sections or pages:

| Supersections   | Consist of 16MB blocks of memory. Support for Supersections is optional, except that an implementation that supports more than 32 bits of PA must also support Supersections to provide access to the entire PA space.   |
|-----------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Sections        | Consist of 1MBblocks of memory.                                                                                                                                                                                          |
| Large pages     | Consist of 64KB blocks of memory.                                                                                                                                                                                        |
| Small pages     | Consist of 4KB blocks of memory.                                                                                                                                                                                         |

Supersections, Sections, and Large pages map large regions of memory using only a single TLB entry.

Note

- Whether a VMSAv8-32 implementation of the Short-descriptor format translation tables supports supersections is IMPLEMENTATION DEFINED.
- The EL2 translation regime cannot use the Short-descriptor translation table format.

When using the Short-descriptor translation table format, two levels of translation tables are held in memory:

## Level 1 table

## Level 2 tables

Holds level 1 descriptors that contain the base address and

- Translation properties for a Section and Supersection.
- Translation properties and pointers to a level 2 table for a Large page or a Small page.

Hold level 2 descriptors that contain the base address and translation properties for a Small page or a Large page. With the Short-descriptor format, level 2 tables can be referred to as translation tables .

Alevel 2 table requires 1KB of memory.

In the translation tables, in general, a descriptor is one of:

- An invalid or fault entry.
- Atranslation table entry, that points to a next-level translation table.
- Apage or section entry, that defines the memory properties for the access.
- Areserved format.

Bits[1:0] of the descriptor give the primary indication of the descriptor type.

Figure G5-3 gives a general view of address translation when using the Short-descriptor translation table format.

Figure G5-3 General view of address translation using VMSAv8-32 Short-descriptor format translation tables

<!-- image -->

Additional requirements for Short-descriptor format translation tables describes why, when using the Short-descriptor format, Supersection and Large page entries must be repeated 16 times, as shown in Figure G5-3.

VMSAv8-32 Short-descriptor Translation Table format descriptors, Memory attributes in the VMSAv8-32 Short-descriptor Translation Table format descriptors, and Control of Secure or Non-secure memory access, VMSAv8-32 Short-descriptor format describe the format of the descriptors in the Short-descriptor format translation tables.

The following sections then describe the use of this translation table format:

- Selecting between TTBR0 and TTBR1, VMSAv8-32 Short-descriptor translation table format.
- Translation table walks, when using the VMSAv8-32 Short-descriptor translation table format.

## G5.4.1 VMSAv8-32 Short-descriptor Translation Table format descriptors

The following sections describe the formats of the entries in the Short-descriptor Translation Tables:

- Short-descriptor Translation Table level 1 descriptor formats.
- Short-descriptor Translation Table level 2 descriptor formats.

For more information about level 2 translation tables, see Additional requirements for Short-descriptor format translation tables.

Note

Previous versions of the Arm Architecture Reference Manual , and some other documentation, describes the AP[2] bit in the translation table entries as the APX bit.

Information returned by a translation table lookup describes the classification of the non-address fields in the descriptors as address map control, access control, or attribute fields.

## G5.4.1.1 Short-descriptor Translation Table level 1 descriptor formats

Each entry in the level 1 table describes the mapping of the associated 1MB V A range.

Figure G5-4 shows the possible level 1 descriptor formats.

Figure G5-4 VMSAv8-32 Short-descriptor level 1 descriptor formats

<!-- image -->

Descriptor bits[1:0] identify the descriptor type. The encoding of these bits is:

## 0b00 , Invalid entry

The associated VA is unmapped, and any attempt to access it generates a Translation fault.

Bits[31:2] of the descriptor are IGNORED, see IGNORED. This means software can use these bits for its own purposes.

## 0b01 , Translation table

The descriptor gives the address of a level 2 translation table, that specifies the mapping of the associated 1MByte VA range.

## 0b10 , Section or Supersection

The descriptor gives the base address of the Section or Supersection. Bit[18] determines whether the entry describes a Section or a Supersection.

This encoding also defines the PXN field as 0.

## 0b11 , Section or Supersection, if the implementation supports the PXN attribute

This encoding is identical to 0b10 , except that it defines the PXN field as 1.

Note

A VMSAv8-32 implementation can use the Short-descriptor translation table format for the PL1&amp;0 stage 1 translations, by setting TTBCR.EAE to 0.

The address information in the level 1 descriptors is:

Translation table Bits[31:10] of the descriptor are bits[31:10] of the address of a translation table.

Section

Bits[31:20] of the descriptor are bits[31:20] of the address of the Section.

Supersection

Bits[31:24] of the descriptor are bits[31:24] of the address of the Supersection.

Optionally, bits[8:5, 23:20] of the descriptor are bits[39:32] of the extended Supersection address.

For the Non-secure PL1&amp;0 translation tables, the address in the descriptor is the IPA of the translation table, Section, or Supersection. Otherwise, the address is the PA of the translation table, Section, or Supersection.

For descriptions of the other fields in the descriptors, see Memory attributes in the VMSAv8-32 Short-descriptor Translation Table format descriptors.

## G5.4.1.2 Short-descriptor Translation Table level 2 descriptor formats

Figure G5-5 shows the possible formats of a level 2 descriptor.

Figure G5-5 Short-descriptor level 2 descriptor formats

<!-- image -->

Descriptor bits[1:0] identify the descriptor type. The encoding of these bits is:

## 0b00 , Invalid entry

The associated VA is unmapped, and attempting to access it generates a Translation fault.

Bits[31:2] of the descriptor are IGNORED, see IGNORED. This means software can use these bits for its own purposes.

## 0b01 , Large page

The descriptor gives the base address and properties of the Large page.

## 0b1x , Small page

The descriptor gives the base address and properties of the Small page.

In this descriptor format, bit[0] of the descriptor is the XN field.

The address information in the level 2 descriptors is:

Large page

Bits[31:16] of the descriptor are bits[31:16] of the address of the Large page.

## Small page

Bits[31:12] of the descriptor are bits[31:12] of the address of the Small page.

For the Non-secure PL1&amp;0 translation tables, the address in the descriptor is the IPA of the translation table, Section, or Supersection. Otherwise, the address is the PA of the translation table, Section, or Supersection.

For descriptions of the other fields in the descriptors, see Memory attributes in the VMSAv8-32 Short-descriptor Translation Table format descriptors.

## G5.4.1.3 Additional requirements for Short-descriptor format translation tables

When using Supersection or Large Page descriptors in the Short-descriptor translation table format, the input address field that defines the Supersection or Large Page descriptor address overlaps the table address field. In each case, the size of the overlap is 4 bits. The following diagrams show these overlaps:

- Figure K8-14 for the level 1 translation table entry for a Supersection.
- Figure K8-16 for the level 2 translation table entry for a Large page.

Considering the case of using Large Page descriptors in a level 2 translation table, this overlap means that for any specific Large page, the bottom four bits of the level 2 translation table entry might take any value from 0b0000 to 0b1111 . Therefore, each of these 16 index values must point to a separate copy of the same descriptor.

This means that each Large page or Supersection descriptor must:

- Occur first on a sixteen-word boundary.
- Be repeated in 16 consecutive memory locations.

## G5.4.2 Memory attributes in the VMSAv8-32 Short-descriptor Translation Table format descriptors

This section describes the descriptor fields other than the descriptor type field and the address field:

| TEX[2:0], C,B   |                                                                                                                                                                                                                                                                       |
|-----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| XNbit           | The Execute-never field, see Access permissions for instruction execution.                                                                                                                                                                                            |
|                 | described in the corresponding translation table are Privileged execute-never. Non-secure bit. Specifies whether the translated PA is in the Secure or Non-secure address map, see Control of Secure or Non-secure memory access, VMSAv8-32 Short-descriptor format.  |
| NS bit          | This bit is not present in level 2 descriptors. The value of the NS bit in a level 1 descriptor for a translation table applies to all entries in the corresponding level 2 translation table.                                                                        |
| Domain          | Domain field, see Domains, Short-descriptor format only. This field is not present in a Supersection entry. Memory described by Supersections is in domain 0. This bit is not present in level 2 descriptors. The value of the Domain field in the level 1 descriptor |
| An              | for translation table applies to all entries in the corresponding level 2 translation table. IMPLEMENTATIONDEFINEDbit                                                                                                                                                 |
|                 | This bit is not present in level 2 descriptors.                                                                                                                                                                                                                       |

S bit nGbit

AP[0] can be configured as the Access flag , see The Access flag.

These bits are not present in a descriptor for a translation table.

Shareable bit. Used in determining the Shareability of the addressed region, see Memory region attributes.

Note

Thenamingofthis bit as the Shareable bit is carried forward from early versions of the Arm architecture. This name is no longer an adequate description of the interpretation of the bit.

This bit is not present in a descriptor for a translation table.

The not global bit. If a lookup using this descriptor is cached in a TLB, determines whether the TLB

entry applies to all ASID values, or only to the current ASID value. See Global and process-specific translation table entries.

This bit is not present in a descriptor for a translation table.

Bit[18], when bits[1:0] indicate a Section or Supersection descriptor

0

Descriptor is for a Section.

- 1

Descriptor is for a Supersection.

## G5.4.3 Control of Secure or Non-secure memory access, VMSAv8-32 Short-descriptor format

Access to the Secure or Non-secure PA map describes how the NS bit in the translation table entries:

- For accesses from Secure state, determines whether the access is to Secure or Non-secure memory.
- Is ignored by accesses from Non-secure state.

In the Short-descriptor translation table format, the NS bit is defined only in the level 1 translation tables. This means that, in a level 1 descriptor for a translation table, the NS bit defines the PA map, Secure or Non-secure, for all of the Large pages and Small pages of memory described by that table.

The NS bit of a level 1 descriptor for a translation table has no effect on the PA map in which that translation table is held. As stated in Secure and Non-secure address spaces, the PA of that translation table is in:

- The Secure address map if the translation table walk is in Secure state.
- The Non-secure address map if the translation table walk is in Non-secure state.

This means the granularity of the Secure and Non-secure memory maps is 1MB. However, in these memory maps, table entries can define physical memory regions with a granularity of 4KB.

## G5.4.4 Selecting between TTBR0 and TTBR1, VMSAv8-32 Short-descriptor translation table format

As described in Determining the translation table base address in the VMSAv8-32 translation regimes, two sets of translation tables can be defined for each of the PL1&amp;0 stage 1 translations, and TTBR0 and TTBR1 hold the base addresses for the two sets of tables. When using the Short-descriptor translation table format, the value of TTBCR.N indicates the number of most significant bits of the input V A that determine whether TTBR0 or TTBR1 holds the required translation table base address, as follows:

- If N == 0 then use TTBR0. Setting TTBCR.N to zero disables use of a second set of translation tables.
- If N &gt; 0 then:
- -If bits[31:32-N] of the input V A are all zero, then use TTBR0.
- -Otherwise use TTBR1.

Table G5-1 shows how the value of N determines the lowest address translated using TTBR1, and the size of the level 1 translation table addressed by TTBR0.

Table G5-1 Effect of TTBCR.N on address translation, Short-descriptor format

| TTBCR.N   | First address translated with TTBR1   | TTBR0 table Size   | Index range   |
|-----------|---------------------------------------|--------------------|---------------|
| 0b000     | TTBR1 not used                        | 16KB               | VA[31:20]     |
| 0b001     | 0x8000_0000                           | 8KB                | VA[30:20]     |
| 0b010     | 0x4000_0000                           | 4KB                | VA[29:20]     |
| 0b011     | 0x2000_0000                           | 2KB                | VA[28:20]     |
| 0b100     | 0x1000_0000                           | 1KB                | VA[27:20]     |
| 0b101     | 0x0800_0000                           | 512 bytes          | VA[26:20]     |
| 0b110     | 0x0400_0000                           | 256 bytes          | VA[25:20]     |
| 0b111     | 0x0200_0000                           | 128 bytes          | VA[24:20]     |

Whenever TTBCR.N is nonzero, the size of the translation table addressed by TTBR1 is 16KB.

Figure G5-6 shows how the value of TTBCR.N controls the boundary between VAs that are translated using TTBR0, and VAs that are translated using TTBR1.

Figure G5-6 How TTBCR.N controls the boundary between the TTBRs, Short-descriptor format

<!-- image -->

In the selected TTBR, bits RGN, S, and IRGN[1:0] define the memory region attributes for the translation table walk.

Translation table walks, when using the VMSAv8-32 Short-descriptor translation table format describes the translation.

## G5.4.5 Translation table walks, when using the VMSAv8-32 Short-descriptor translation table format

When using the Short-descriptor translation table format, and a memory access requires a translation table walk:

- Asection-mapped access only requires a read of the level 1 translation table.
- Apage-mapped access also requires a read of the level 2 translation table.

Reading a level 1 translation table describes how either TTBR1 or TTBR0 is used, with the accessed V A, to determine the address of the level 1 descriptor.

Reading a level 1 translation table shows the output address as A[39:0]:

- For a Non-secure PL1&amp;0 stage 1 translation, this is the IPA of the required descriptor. A Non-secure PL1&amp;0 stage 2 translation of this address is performed to obtain the PA of the descriptor.
- Otherwise, this address is the PA of the required descriptor.

The full translation flow for Sections, Supersections, Small pages and Large pages then shows the complete translation flow for each valid memory access.

## G5.4.5.1 Reading a level 1 translation table

When performing a fetch based on TTBR0:

- The address bits taken from TTBR0 vary between bits[31:14] and bits[31:7].
- The address bits taken from the V A, that is the input address for the translation, vary between bits[31:20] and bits[24:20].

The width of the TTBR0 and VA fields depend on the value of TTBCR.N, as Figure G5-7 shows.

When performing a fetch based on TTBR1, Bits TTBR1[31:14] are concatenated with bits[31:20] of the VA. This makes the fetch equivalent to that shown in Figure G5-7, with N==0.

Note

See The address and Properties fields shown in the translation flows for more information about the Properties label used in this and other figures.

Figure G5-7 Accessing level 1 translation table based on TTBR0, Short-descriptor format

<!-- image -->

Regardless of which register is used as the base for the fetch, the resulting output address selects a four-byte translation table entry that is one of:

- Alevel 1 descriptor for a Section or Supersection.

- Adescriptor for a translation table , that points to a level 2 translation table. In this case:
- -Asecond fetch is performed to retrieve a level 2 descriptor.
- -The descriptor also contains some attributes for the access, see Figure G5-4.
- Afaulting entry.

## G5.4.5.2 The full translation flow for Sections, Supersections, Small pages and Large pages

In a translation table walk, only the initial lookup uses the translation table base address from the appropriate TTBR. Subsequent lookups use a combination of address information from:

- The Table descriptor read in the previous lookup.
- The input address.

Address translation examples using the VMSAv8-32 Short descriptor translation table format shows the full translation flow for each of the memory section and page options. As described in VMSAv8-32 Short-descriptor Translation Table format descriptors, these options are:

Supersection

A16 MB memory region, see Translation flow for a Supersection.

Section

A1MBmemoryregion, see Translation flow for a Section.

Large page

A64 KB memory region, described by the combination of:

- Alevel 1 translation table entry that indicates the address of a level 2 translation table.
- Alevel 2 descriptor that indicates a Large page.

See Translation flow for a Large page.

Small page A4KBmemory region, described by the combination of:

- Alevel 1 translation table entry that indicates the address of a level 2 translation table.
- Alevel 2 descriptor that indicates a Small page.

See Translation flow for a Small page.