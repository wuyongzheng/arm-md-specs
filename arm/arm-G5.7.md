## G5.7 Memory region attributes

In addition to an output address, a translation table entry that refers to a page or region of memory includes fields that define properties of that target memory region. Information returned by a translation table lookup describes the classification of those fields as address map control, access control, and memory attribute fields. The memory region attribute fields control the memory type, Cacheability, and Shareability of the region.

The following sections describe the assignment of memory region attributes for stage 1 translations:

- Overview of memory region attributes for stage 1 translations.
- Short-descriptor format memory region attributes, without TEX remap.
- Short-descriptor format memory region attributes, with TEX remap.
- VMSAv8-32 Long-descriptor format memory region attributes.

For an implementation that is operating in Secure state, or in Hyp mode, these assignments define the memory attributes of the accessed region.

For an implementation that is operating in a Non-secure PL1 or EL0 mode, the Non-secure PL1&amp;0 stage 2 translation can modify the memory attributes assigned by the stage 1 translation. EL2 control of Non-secure memory region attributes describes these stage 2 assignments.

## G5.7.1 Overview of memory region attributes for stage 1 translations

The description of the memory region attributes in a Translation descriptor divides into:

## Memory type and attributes

These are described either:

- Directly, by bits in the Translation Table descriptor.
- Indirectly, by registers referenced by bits in the Table descriptor. This is described as remapping the memory type and attribute description.

The Short-descriptor translation table format can use either of these approaches, selected by the SCTLR.TRE bit:

- TRE==0

Remap disabled. The TEX[2:0], C, and B bits in the Translation Table descriptor define the memory region attributes. Short-descriptor format memory region attributes, without TEX remap describes this encoding.

Note

With the Short-descriptor format, remapping is called TEX remap , and the SCTLR.TRE bit is the TEX remap enabled bit.

The description of the TRE == 0 encoding includes information about the encoding in previous versions of the architecture.

- TRE==1 Remap enabled. The TEX[0], C, and B bits in the Translation Table descriptor are index bits to the remap registers, that define the memory region attributes:
- The Primary Region Remap Register, PRRR.
- The Normal Memory Remap Register, NMRR.

Short-descriptor format memory region attributes, with TEX remap describes this encoding scheme.

This scheme reassigns Translation Table descriptor bits TEX[2:1] for use as bits managed by the operating system.

The Long-descriptor translation table format always uses remapping. This means that when the value of TTBCR.EAE is 1, enabling use of the Long-descriptor translation table format, SCTLR.TRE is RES1.

VMSAv8-32 Long-descriptor format memory region attributes describes this encoding.

## Shareability

In the Short-descriptor translation table format, the S bit in the Translation Table descriptor is used in determining the Shareability of the region. How the S bit is interpreted depends on whether TEX remap is enabled, see:

- Shareability and the S bit, without TEX remap.
- Determining the Shareability, with TEX remap.

In the Long-descriptor translation table format, the SH[1:0] field in the Translation Table descriptor encodes the Shareability of the region, see Shareability, Long-descriptor format.

Note

Shareability is one of Non-shareable, Inner Shareable, and Outer Shareable. However, when using the Short-descriptor translation table format without TEX remap, VMSAv8-32 does not support any distinction between Inner Shareable and Outer Shareable memory, and a memory region is either Non-shareable or Outer Shareable.

## G5.7.1.1 Stage 1 definition of the XS attribute

When FEAT\_XS is implemented, all stage 1 memory types defined in the MAIR0, MAIR1, HMAIR0, HMAIR1, PRRR, and NMRR registers, or the TTBCR or HTCR registers, or in the translation tables, have the XS attribute set to 1, unless they are Inner Write-Back Cacheable, Outer Write-back Cacheable, which have the XS attribute set to 0. This includes any memory types that are treated as Write-Back Cacheable as a result of IMPLEMENTATION DEFINED choices in the architecture.

## G5.7.2 Short-descriptor format memory region attributes, without TEX remap

When using the Short-descriptor translation table formats, TEX remap is disabled when the value of SCTLR.TRE is 0.

Note

- The Short-descriptor format scheme without TEX remap is the scheme used in VMSAv6.
- The B (Bufferable), C (Cacheable), and TEX (Type extension) bit names are inherited from earlier versions of the architecture. These names no longer adequately describe the function of the B, C, and TEX bits.

Table G5-12 shows the C, B, and TEX[2:0] encodings when TEX remap is disabled. In the Page Shareability column, an entry of S bit indicates that the S bit in the Translation Table descriptor determines the Shareability, see Shareability and the S bit, without TEX remap.

## Table G5-12 TEX, C, and B encodings when TRE == 0

| TEX[2:0]   | C   |   B | Description                                                    | Memory type            | Page Shareability      |
|------------|-----|-----|----------------------------------------------------------------|------------------------|------------------------|
| 000        | 0   |   0 | Device-nGnRnE                                                  | Device-nGnRnE          | Outer Shareable        |
|            |     |   1 | Device-nGnRE a                                                 | Device-nGnRE           | Outer Shareable a      |
|            | 1   |   0 | Outer and Inner Write-Through, Read-Allocate No Write-Allocate | Normal                 | S bit                  |
|            |     |   1 | Outer and Inner Write-Back, Read-Allocate No Write-Allocate    | Normal                 | S bit                  |
| 001        | 0   |   0 | Outer and Inner Non-cacheable                                  | Normal                 | Outer Shareable b      |
|            |     |   1 | Reserved                                                       | -                      | -                      |
|            | 1   |   0 | IMPLEMENTATION DEFINED                                         | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED |
|            |     |   1 | Outer and Inner Write-Back, Read-Allocate Write-Allocate       | Normal                 | S bit                  |
| 010        | 0   |   0 | Device-nGnRE a                                                 | Device-nGnRE           | Outer Shareable a      |
|            |     |   1 | Reserved                                                       | -                      | -                      |

| TEX[2:0]   | C   | B   | Description       | Memory type                  | Page Shareability   |
|------------|-----|-----|-------------------|------------------------------|---------------------|
|            | 1   | x   | Reserved          | -                            | -                   |
| 011        | x   | x   | Reserved          | -                            | -                   |
| 1BB        | A   | A   | Cacheable memory: | attribute c attribute Normal | S bit               |

b. In Armv8, Normal Inner Non-cacheable, Outer Non-cacheable memory is always Outer Shareable. This is a change from previous versions of the architecture, where the S bit determined the Shareability. For compatibility with Armv7 software should set S to 1.

c. For more information, see Cacheability attributes, without TEX remap.

See Memory types and attributes for an explanation of Normal memory, and the types of Device memory, and of the Shareability attribute.

## G5.7.2.1 Cacheability attributes, without TEX remap

When the value of TEX[2] is 0, the same Cacheability attribute applies to Inner Cacheable and Outer Cacheable memory regions, and the {TEX[1:0], C, B} values identify this attribute, as Table G5-12 shows.

When the value of TEX[2] is 1, the memory described by the translation table entry is cacheable, and the rest of the encoding defines the Inner Cacheability and Outer Cacheability attributes:

TEX[1:0]

Define the Outer Cacheability attribute.

- C, B

Define the Inner Cacheability attribute.

The translation table entries use the same encoding for the Outer and Inner Cacheability attributes, as Table G5-13 shows.

Table G5-13 Inner and Outer Cacheability attribute encoding

|   Encoding | Cacheability attribute                         |
|------------|------------------------------------------------|
|         00 | Non-cacheable                                  |
|         01 | Write-Back, Read-Allocate Write-Allocate       |
|         10 | Write-Through, Read Allocate No Write-Allocate |
|         11 | Write-Back, Read Allocate No Write-Allocate    |

## G5.7.2.2 Shareability and the S bit, without TEX remap

The Short-descriptor format translation table entries include an S bit. This bit:

- Is ignored if the entry refers to any type of Device memory, or to Normal memory that is Inner Non-cacheable, Outer Non-cacheable.
- For Normal memory that is not Inner Non-cacheable, Outer Non-cacheable, determines whether the memory region is Outer Shareable or Non-shareable:

| S == 0   | Normal memory region is Non-shareable.   |
|----------|------------------------------------------|
| S == 1   | Normal memory region is Outer Shareable. |

Without TEX remapping there is no distinction between Inner Shareable and Outer Shareable memory, meaning the S bit determines whether the region is Non-shareable or Outer Shareable.

## G5.7.3 Short-descriptor format memory region attributes, with TEX remap

When using the Short-descriptor translation table formats, TEX remap is enabled when the value of SCTLR.TRE is 1. In this configuration:

- The software that defines the translation tables must program the PRRR and NMRR to define seven possible memory region attributes.
- The TEX[0], C, and B bits of the Translation Table descriptors define the memory region attributes, by indexing PRRR and NMRR.
- Hardware makes no use of TEX[2:1], see The OS managed translation table bits.

## When TEX remap is enabled:

- For seven of the eight possible combinations of the TEX[0], C and B bits, fields in the PRRR and NMRR define the region attributes, as described in this section.
- The meaning of the eighth combination for the TEX[0], C and B bits is IMPLEMENTATION DEFINED.
- If the TEX[0], C and B bits determine that the region is a Device memory type, or is Normal Inner Non-cacheable, Outer Non-cacheable, then the region is Outer Shareable. Otherwise, the Shareability is determined by the combination of:
- -The S bit from the Translation Table descriptor.
- -The value of the PRRR.NS0 or PRRR.NS1 bit.
- -The value of the appropriate PRRR.NOS n bit, as shown in Table G5-14.

For more information, see Determining the Shareability, with TEX remap.

For each of the possible encodings of the TEX[0], C, and B bits in a translation table entry, Table G5-14 shows which fields of the PRRR and NMRR registers describe the memory region attributes.

Table G5-14 TEX, C, and B encodings when TRE == 1

| Encoding   |    |    | Memory type a          | Cache attributes a, b :   |                        | Outer Shareable attribute a, c   |
|------------|----|----|------------------------|---------------------------|------------------------|----------------------------------|
| TEX[0]     | C  | B  |                        | Inner cacheability        | Outer cacheability     |                                  |
| 0          | 0  | 0  | PRRR.TR0               | NMRR.IR0                  | NMRR.OR0               | NOT(PRRR.NOS0)                   |
|            |    | 1  | PRRR.TR1               | NMRR.IR1                  | NMRR.OR1               | NOT(PRRR.NOS1)                   |
|            | 1  | 0  | PRRR.TR2               | NMRR.IR2                  | NMRR.OR2               | NOT(PRRR.NOS2)                   |
|            |    | 1  | PRRR.TR3               | NMRR.IR3                  | NMRR.OR3               | NOT(PRRR.NOS3)                   |
| 1          | 0  | 0  | PRRR.TR4               | NMRR.IR4                  | NMRR.OR4               | NOT(PRRR.NOS4)                   |
|            |    | 1  | PRRR.TR5               | NMRR.IR5                  | NMRR.OR5               | NOT(PRRR.NOS5)                   |
|            | 1  | 0  | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED    | IMPLEMENTATION DEFINED | IMPLEMENTATION DEFINED           |
|            |    | 1  | PRRR.TR7               | NMRR.IR7                  | NMRR.OR7               | NOT(PRRR.NOS7)                   |

- c. Applies only if both of the following apply:
- The memory type for the region is mapped as Normal memory that is not Inner Non-cacheable and Outer Non-cacheable.
- The region is not Non-shareable.

See Determining the Shareability, with TEX remap.

As Table G5-14 shows, when TEX remap is enabled, for a given set of {TEX[0], C, B} bits from a Translation Table descriptor:

1. The primary mapping, to memory type, is given by the PRRR.TR n field as shown in the Memory type column.
2. For any region that the PRRR.TR n maps as Normal memory, NMRR.IR n determines the Inner cacheability attribute, and NMRR.OR n determines the Outer cacheability attribute.
3. For a region that PRRR.TR n maps as Normal memory, if NMRR.{IR n , OR n } do not map the region as Inner Non-cacheable, Outer Non-cacheable, PRRR.{NS0, NS1} and PRRR.NOS n are used to determine the Shareability of the region, see Determining the Shareability, with TEX remap.

The TEX remap registers and the SCTLR.TRE bit are banked between the Secure and Non-secure Security states. For more information, see The effect of EL3 on TEX remap.

The TEX remap registers must be static during normal operation. In particular, when the remap registers are changed:

- It is IMPLEMENTATION DEFINED when the changes take effect.
- It is CONSTRAINED UNPREDICTABLE whether the TLB caches the effect of the TEX remap on translation tables, see CONSTRAINED UNPREDICTABLE behaviors due to caching of System register control or data values.

The software sequence to ensure the synchronization of changes to the TEX remap registers is:

1. Execute a DSB instruction. This ensures any memory accesses using the old mapping have completed.
2. Write the TEX remap registers or SCTLR.TRE bit.
3. Execute an ISB instruction. This ensures synchronization of the register updates.
4. Invalidate the entire TLB.
5. Execute a DSB instruction. This ensures completion of the entire TLB operation.
6. Clean and invalidate all caches. This removes any cached information associated with the old mapping.
7. Execute a DSB instruction. This ensures completion of the cache maintenance.
8. Execute an ISB instruction. This ensures instruction synchronization.

This extends the standard rules for the synchronization of changes to System registers described in Synchronization of changes to AArch32 System registers, and provides implementation freedom as to whether or not the effect of the TEX remap is cached.

## G5.7.3.1 Determining the Shareability, with TEX remap

The memory type of a region, as indicated in the Memory type column of Table G5-14, provides the first level of control of the Shareability of the region:

- If the memory is any type of Device memory, then the region is Outer Shareable, and any Shareability attributes in the Translation Table descriptor and PRRR for that region are ignored. This applies also to a Normal memory region that the NMRR attributes identify as Inner Non-cacheable and Outer Non-cacheable,
- If using the Short descriptor translation table format then the Shareability of the region is determined using the value of the S bit in the Translation Table descriptor to index one of the PRRR.{NS1. NS0} bits, as described in this section.

Table G5-15 shows how the translation table S bit indexes into the PRRR:

## Table G5-15 Determining the Shareability attribute, with TEX remap

| Memory type                                               | Remapping when S == 0   | Remapping when S == 1   |
|-----------------------------------------------------------|-------------------------|-------------------------|
| Device or Normal Inner Non-cacheable, Outer Non-cacheable | Outer Shareable         | Outer Shareable         |
| Normal, not Inner Non-cacheable, Outer Non-cacheable      | PRRR.NS0                | PRRR.NS1                |

For a Normal memory region that is not Inner Non-cacheable, Outer Non-cacheable, the appropriate bit of the PRRR indicates whether the region is Non-shareable, as follows:

PRRR.NS n == 0 Non-shareable.

PRRR.{NOS7:NOS0} are ignored.

- PRRR.NS n == 1 The appropriate PRRR.NOS m field, as shown in Table G5-14, indicates whether the region is Inner Shareable or Outer Shareable:

PRRR.NOS m == 0 Region is Outer Shareable.

PRRR.NOS m == 1 Region is Inner Shareable.

Note

This means that TEX remapping can map a translation table entry with S == 0 as shareable memory.

## G5.7.3.2 SCTLR.TRE, SCTLR.M, and the effect of the TEX remap registers

When TEX remap is disabled, because the value of the SCTLR.TRE bit is 0:

- The effect of the PRRR and NMRR registers can be IMPLEMENTATION DEFINED.
- The interpretation of the fields of the PRRR and NMRR registers can differ from the description given earlier in this section. One implication of this is that the implementation can provide an IMPLEMENTATION DEFINED mechanism to interpret the PRRR.{NOS7:NOS0} fields.

VMSAv8-32 requires that the effect of these registers is limited to remapping the attributes of memory locations. These registers must not change whether any cache hardware or stages of address translation are enabled. The mechanism by which the TEX remap registers have an effect when the value of the SCTLR.TRE bit is 0 is IMPLEMENTATION DEFINED. The AArch32 architecture requires that from reset, if the IMPLEMENTATION DEFINED mechanism has not been invoked:

- If the PL1&amp;0 stage 1 address translation is enabled and is using the Short-descriptor format translation tables, the architecturally-defined behavior of the TEX[2:0], C, and B bits must apply, without reference to the TEX remap functionality. In other words, memory attribute assignment must comply with the scheme described in Short-descriptor format memory region attributes, without TEX remap.
- If the PL1&amp;0 stage 1 address translation is disabled, then the architecturally-defined behavior of VMSAv8-32 with address translation disabled must apply, without reference to the TEX remap functionality. See The effects of disabling address translation stages on VMSAv8-32 behavior.

Possible mechanisms for enabling the IMPLEMENTATION DEFINED effect of the TEX remap registers when the value of SCTLR.TRE is 0 include:

- Acontrol bit in the ACTLR, or in an IMPLEMENTATION DEFINED System register.
- Changing the behavior when the PRRR and NMRR registers are changed from their IMPLEMENTATION DEFINED reset values.

In addition, if the stage of address translation is disabled and the value of the SCTLR.TRE bit is 1, the architecturally-defined behavior of the VMSAv8-32 with the stage of address translation disabled must apply without reference to the TEX remap functionality.

In an implementation that includes EL3, the IMPLEMENTATION DEFINED effect of these registers must only take effect in the Security state of the registers. See also The effect of EL3 on TEX remap.

## G5.7.3.3 The OS managed translation table bits

When TEX remap is enabled, the TEX[2:1] bits in the Translation Table descriptors are available as two bits that can be managed by the operating system. In VMSAv8-32, as long as the SCTLR.TRE bit is set to 1, the values of the TEX[2:1] bits are IGNORED by the PE. Software can write any value to these bits in the translation tables.

## G5.7.3.4 The effect of EL3 on TEX remap

In an implementation that includes EL3, when EL3 is using AArch32, the TEX remap registers are banked between the Secure and Non-secure Security states. When EL3 is using AArch32, write accesses to the Secure register for the current security state apply to all PL1&amp;0 stage 1 translation table lookups in that state. The SCTLR.TRE bit is banked in the Secure and Non-secure copies of the register, and the appropriate version of this bit determines whether TEX remap is applied to translation table lookups in the current security state.

Write accesses to the Secure copies of the TEX remap registers are disabled when the CP15SDISABLE input is asserted HIGH, meaning the MCR operations to access these registers are UNDEFINED. For more information, see The CP15SDISABLE and CP15SDISABLE2 input signals.

## G5.7.4 VMSAv8-32 Long-descriptor format memory region attributes

When a PE is using the VMSAv8-32 Long-descriptor translation table format, the AttrIndx[2:0] field in a block or page Translation Table descriptor for a stage 1 translation indicates the 8-bit field, in the appropriate MAIR register, that specifies the attributes for the corresponding memory region, as follows:

- AttrIndx[2] indicates the MAIR register to be used:

AttrIndx[2] == 0 Use MAIR0.

AttrIndx[2] == 1 Use MAIR1.

- AttrIndx[2:0] indicates the required Attr field, Attr n , where n = AttrIndx[2:0].

Each AttrIndx field defines, for the corresponding memory region:

- The memory type, Normal or a type of Device memory.
- For Normal memory:
- -The Inner cacheability and Outer cacheability attributes, each of which is one of Non-cacheable, Write-Through Cacheable, or Write-Back Cacheable.
- -For Write-Through Cacheable and Write-Back Cacheable regions, the Read-Allocate and Write-Allocate policy hints, each of which is Allocate or No allocate .

For more information about the AttrIndx[2:0] descriptor field, see Attribute fields in VMSAv8-32 Long-descriptor stage 1 Block and Page descriptors.

## G5.7.4.1 Shareability, Long-descriptor format

When a PE is using the Long-descriptor translation table format, the SH[1:0] field in a Block or Page Translation Table descriptor specifies the Shareability attributes of the corresponding memory region, if the MAIR entry for that region identifies it as Normal memory that is not both Inner Non-cacheable and Outer Non-cacheable. Table G5-16 shows the encoding of this field.

Table G5-16 SH[1:0] field encoding for Normal memory, Long-descriptor format

|   SH[1:0] | Normal memory                                                                                                                                            |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|        00 | Non-shareable.                                                                                                                                           |
|        01 | Reserved, CONSTRAINED UNPREDICTABLE, see Reserved values in System and memory-mapped registers and translation table entries for the permitted behavior. |
|        10 | Outer Shareable.                                                                                                                                         |
|        11 | Inner Shareable.                                                                                                                                         |

See Combining the Shareability attribute for constraints on the Shareability attributes of a Normal memory region that is Inner Non-cacheable, Outer Non-cacheable.

For any type of Device memory, and for Normal Inner Non-cacheable, Outer Non-cacheable memory, the value of the SH[1:0] field of the Translation Table descriptor is ignored.

## G5.7.4.2 Other fields in the Long-descriptor translation table format descriptors

The following subsections describe the other fields in the Translation Table Block and Page descriptors when a PE is using the Long-descriptor translation table format:

- Contiguous bit.
- IGNORED fields.
- Field reserved for software use.

## G5.7.4.2.1 Contiguous bit

The Long-descriptor Translation Table Format descriptors contain a Contiguous bit. Setting this bit to 1 indicates that 16 adjacent translation table entries point to a contiguous output address range . These 16 entries must be aligned in the translation table so that the top five bits of their input addresses, that index their position in the translation table, are the same. For example, to use this bit for a block of 16 entries in the level 3 translation table, bits[20:16] of the input addresses for the 16 entries must be the same.

The contiguous output address range must be aligned to size of 16 translation table entries at the same translation table level.

Use of this bit means that the TLB can cache a single entry to cover the 16 translation table entries.

This bit acts as a hint. The architecture does not require a PE to cache TLB entries in this way. To avoid TLB coherency issues, any TLB maintenance by address must not assume any optimization of the TLB tables that might result from use of this bit.

Note

The use of the contiguous bit is similar to the approach used, in the Short-descriptor translation table format, for optimized caching of Large Pages and Supersections in the TLB. However, an important difference in the contiguous bit capability is that TLB maintenance must be performed based on the size of the underlying translation table entries, to avoid TLB coherency issues. That is, any use of the contiguous bit has no effect on the minimum size of entry that must be invalidated from the TLB.

## G5.7.4.2.2 IGNORED fields

In the VMSAv8-32 translation table long-descriptor format, the following fields are defined as IGNORED, meaning the architecture guarantees that a PE makes no use of these fields:

- In the stage 1 and stage 2 Table descriptors, bits[58:52] and bits[11:2].
- In the stage 1 and stage 2 Block and Page descriptors, bit[63] and bits[58:55].
- In the stage 1 and stage 2 Block and Page descriptors in an implementation that does not include FEAT\_HPDS2, bits[62:59].

## Of these fields:

- In the stage 1 and stage 2 Block and Page descriptors, bits[58:55] are reserved for software use, see Field reserved for software use.
- In the stage 2 Block and Page descriptors:
- -Bit[63] is reserved for use by a System MMU.
- -In an implementation that does not include FEAT\_HPDS2, bits[62:59] are reserved for use by a System MMU.

## G5.7.4.2.3 Field reserved for software use

The architecture reserves a 4-bit IGNORED field in the Block and Translation Table descriptors, bits[58:55], for software use. In considering migration from using the Short-descriptor format to the Long-descriptor format, this field is an extension of the Short-descriptor field described in The OS managed translation table bits.

Note

The definition of IGNORED means there is no need to invalidate the TLB if these bits are changed.

## G5.7.5 EL2 control of Non-secure memory region attributes

Software executing at EL2 controls two sets of translation tables, both of which use the Long-descriptor translation table format. These are:

- The translation tables that control Non-secure EL2 stage 1 translations. These map V As to PAs, and when EL2 is using AArch32 they are indicated and controlled by the HTTBR and HTCR.
- These translations have exactly the same memory region attribute controls as any other stage 1 translations, as
- described in VMSAv8-32 Long-descriptor format memory region attributes.
- The translation tables that control Non-secure PL1&amp;0 stage 2 translations. These map the IPAs from the stage 1 translation onto PAs, and are indicated and when EL2 is using AArch32 they are controlled by the VTTBR and VTCR.

The descriptors in the virtualization translation tables define level 2 memory region attributes, that are combined with the attributes defined in the stage 1 translation. This section describes this combining of attributes.

VMSAv8-32 Long-descriptor Translation Table format descriptors describes the format of the entries in these tables.

Note

In a virtualization implementation, a hypervisor might usefully:

- Reduce the permitted Cacheability of a region.
- Increase the required Shareability of a region.

The combining of attributes from stage 1 and stage 2 translations supports both of these options.

In the stage 2 Translation Table descriptors for memory regions and pages, the MemAttr[3:0] and SH[1:0] fields describe the stage 2 memory region attributes:

- The definition of the stage 2 SH[1:0] field is identical to the same field for a stage 1 translation, see Shareability, Long-descriptor format.
- MemAttr[3:2] give a top-level definition of the memory type, and of the cacheability of a Normal memory region, as Table G5-17 shows:

Table G5-17 Long-descriptor MemAttr[3:2] encoding, stage 2 translation

|   MemAttr[3:2] | Memory type                                           | Cacheability                  |
|----------------|-------------------------------------------------------|-------------------------------|
|             00 | Device, of type determined by MemAttr[1:0]            | Not applicable                |
|             01 | Normal, Inner cacheability determined by MemAttr[1:0] | Outer Non-cacheable           |
|             10 |                                                       | Outer Write-Through Cacheable |
|             11 |                                                       | Outer Write-Back Cacheable    |

The encoding of MemAttr[1:0] depends on the Memory type indicated by MemAttr[3:2]:

- When MemAttr[3:2] == 0b00 , indicating a type of Device memory, Table G5-18 shows the encoding of MemAttr[1:0]:

## Table G5-18 MemAttr[1:0] encoding for the types of Device memory

|   MemAttr[1:0] | Meaning when MemAttr[3:2] == 0b00   |
|----------------|-------------------------------------|
|             00 | Region is Device-nGnRnE memory      |
|             01 | Region is Device-nGnRE memory       |

|   MemAttr[1:0] | Meaning when MemAttr[3:2] == 0b00   |
|----------------|-------------------------------------|
|             10 | Region is Device-nGRE memory        |
|             11 | Region is Device-GRE memory         |

- When MemAttr[3:2] != 0b00 , indicating Normal memory, Table G5-19 shows the encoding of MemAttr[1:0]:

## Table G5-19 MemAttr[1:0] encoding for Normal memory

|   MemAttr[1:0] | Meaning when MemAttr[3:2] != 0b00                                                                                                                        |
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------|
|             00 | Reserved, CONSTRAINED UNPREDICTABLE, See Reserved values in System and memory-mapped registers and translation table entries for the permitted behavior. |
|             01 | Inner Non-cacheable.                                                                                                                                     |
|             10 | Inner Write-Through Cacheable.                                                                                                                           |
|             11 | Inner Write-Back Cacheable.                                                                                                                              |

Note

The stage 2 translation does not assign any allocation hints.

The following sections describe how the memory type attributes assigned at stage 2 of the translation are combined with those assigned at stage 1:

- Combining the memory type attribute.
- Combining the Cacheability attribute.
- Combining the Shareability attribute.

## Note

- The following stage 2 translation table attribute settings leave the stage 1 settings unchanged:
- -MemAttr[3:2] == 0b11 , Normal memory, Outer Write-Back Cacheable.
- -MemAttr[1:0] == 0b11 , Inner Write-Back Cacheable.
- In addition to the attribute combinations described in this section, Access permissions for instruction execution describes how the stage 1 and stage 2 execute-never permission fields are combined, so that a region is executenever if it is defined as execute-never in at least one stage of translation.

## G5.7.5.1 Combining the memory type attribute

Table G5-20 shows how the stage 1 and stage 2 memory type assignments are combined:

## Table G5-20 Combining the stage 1 and stage 2 memory type assignments

| Assignment in stage 1   | Assignment in stage 2   | Resultant type   |
|-------------------------|-------------------------|------------------|
| Device-nGnRnE           | Any                     | Device-nGnRnE    |
| Device-nGnRE            | Device-nGnRnE           | Device-nGnRnE    |
|                         | Not Device-nGnRnE       | Device-nGnRE     |

| Assignment in stage 1   | Assignment in stage 2               | Resultant type                  |
|-------------------------|-------------------------------------|---------------------------------|
| Device-nGRE             | Device-nGnRnE                       | Device-nGnRnE                   |
| Device-nGRE             | Device-nGnRE                        | Device-nGnRE                    |
| Device-nGRE             | Not (Device-nGnRnE or Device-nGnRE) | Device-nGRE                     |
| Device-GRE              | Device-nGnRnE                       | Device-nGnRnE                   |
| Device-GRE              | Device-nGnRE                        | Device-nGnRE                    |
| Device-GRE              | Device-nGRE                         | Device-nGRE                     |
| Device-GRE              | Device-GRE or Normal                | Device-GRE                      |
| Normal                  | Any type of Device                  | Device type assigned at stage 2 |
| Normal                  | Normal                              | Normal                          |

See Combining the Shareability attribute for information about the Shareability of:

- Aregion for which the resultant type is any Device type.
- Aregion with a resultant type of Normal for which the resultant cacheability, described in Combining the Cacheability attribute, is Inner Non-cacheable, Outer Non-cacheable.

The combining of the memory type attribute means a translation table walk for a stage 1 translation can be made to a type of Device memory. If this occurs, then:

- If the value of HCR.PTW is 0, then the translation table walk occurs as if it is to Normal Non-cacheable memory. This means it can be done speculatively.
- If the value of HCR.PTW is 1, then the memory access generates a stage 2 Permission fault.

## G5.7.5.2 Combining the Cacheability attribute

For a Normal memory region, Table G5-21 shows how the stage 1 and stage 2 Cacheability assignments are combined. This combination applies, independently, for the Inner Cacheability and Outer Cacheability attributes:

Table G5-21 Combining the stage 1 and stage 2 cacheability assignments

| Assignment in stage 1                 | Assignment in stage 2                 | Resultant cacheability   |
|---------------------------------------|---------------------------------------|--------------------------|
| Non-cacheable                         | Any                                   | Non-cacheable            |
| Any                                   | Non-cacheable                         | Non-cacheable            |
| Write-Through Cacheable               | Write-Through or Write-Back Cacheable | Write-Through Cacheable  |
| Write-Through or Write-Back Cacheable | Write-Through Cacheable               | Write-Through Cacheable  |
| Write-Back Cacheable                  | Write-Back Cacheable                  | Write-Back Cacheable     |

Note

Only Normal memory has a Cacheability attribute.

## G5.7.5.3 Combining the Shareability attribute

In the following cases, a memory region is treated as Outer Shareable, regardless of any shareability assignments at either stage of translation:

- The resultant memory type attribute, described in Combining the memory type attribute, is any type of Device memory.

- The resultant memory type attribute is Normal memory, and the resultant Cacheability, described in Combining the Cacheability attribute, is Inner Non-cacheable Outer Non-cacheable.

For a memory region with a resultant memory type attribute of Normal that is not Inner Non-cacheable Outer Non-cacheable, Table G5-22 shows how the stage 1 and stage 2 shareability assignments are combined:

Table G5-22 Combining the stage 1 and stage 2 Shareability assignments

| Assignment in stage 1   | Assignment in stage 2   | Resultant Shareability   |
|-------------------------|-------------------------|--------------------------|
| Outer Shareable         | Any                     | Outer Shareable          |
| Inner Shareable         | Outer Shareable         | Outer Shareable          |
| Inner Shareable         | Inner Shareable         | Inner Shareable          |
| Inner Shareable         | Non-shareable           | Inner Shareable          |
| Non-shareable           | Outer Shareable         | Outer Shareable          |
| Non-shareable           | Inner Shareable         | Inner Shareable          |
| Non-shareable           | Non-shareable           | Non-shareable            |