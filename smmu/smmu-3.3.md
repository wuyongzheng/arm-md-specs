## 3.3 Data structures and translation procedure

The SMMU uses a set of data structures in memory to locate translation data. Registers hold the base addresses of the initial root structure, the Stream table. An STE contains stage 2 translation table base pointers, and also locates stage 1 configuration structures, which contain translation table base pointers. A Context Descriptor (CD) represents stage 1 translation, and a Stream Table Entry represents stage 2 translation.

Therefore, there are two distinct groups of structures used by the SMMU:

- Configuration structures, which map from the StreamID of a transaction (a device originator identifier) to the translation table base pointers, configuration, and context under which the translation tables are accessed.
- Translation table structures that are used to perform the V A to IPA and IPA to PA translation of addresses for stage 1 and stage 2, respectively.

The procedure for translation of an incoming transaction is to first locate configuration appropriate for that transaction, identified by its StreamID and, optionally, SubstreamID, and then to use that configuration to locate translations for the address used.

The first step in dealing with an incoming transaction is to locate the STE, which tells the SMMU what other configuration it requires.

Conceptually, an STE describes configuration for a client device in terms of whether it is subject to stage 1 or stage 2 translation or both. Multiple devices can be associated with a single Virtual Machine, so multiple STEs can share common stage 2 translation tables. Similarly, multiple devices (strictly, streams) might share common stage 1 configuration, therefore multiple STEs could share common CDs.

## 3.3.1 Stream table lookup

The StreamID of an incoming transaction locates an STE. Two formats of Stream table are supported. The format is set by the Stream table base registers. The incoming StreamID is range-checked against the programmed table size, and a transaction is terminated if its StreamID would otherwise select an entry outside the configured Stream table extent (or outside a level 2 span). See SMMU\_STRTAB\_BASE\_CFG and C\_BAD\_STREAMID.

The StreamID of an incoming transaction might be qualified by SEC\_SID, and this determines which Stream table, or cached copies of that Stream table, is used for lookup. See section 3.10.1 StreamID Security state (SEC\_SID) .

## 3.3.1.1 Linear Stream table

Figure 3.1: Linear Stream table

<!-- image -->

A linear Stream table is a contiguous array of STEs, indexed from 0 by StreamID. The size is configurable as a 2 n multiple of STE size up to the maximum number of StreamID bits supported in hardware by the SMMU. The linear Stream table format is supported by all SMMU implementations.

## 3.3.1.2 2-level Stream table

Figure 3.2: Example Two level Stream table with SPLIT == 8

<!-- image -->

A 2-level Stream table is a structure consisting of one top-level table that contains descriptors that point to multiple second-level tables that contain linear arrays of STEs. The span of StreamIDs covered by the entire structure is configurable up to the maximum number supported by the SMMU but the second-level tables do not have to be fully populated and might vary in size. This saves memory and avoids the requirement of large physically-contiguous allocations for very large StreamID spaces.

The top-level table is indexed by StreamID[n:x], where n is the uppermost StreamID bit covered, and x is a configurable Split point given by SMMU\_(*\_)STRTAB\_BASE\_CFG.SPLIT. The second-level tables are indexed by up to StreamID[x - 1:0], depending on the span of each table.

Support for the 2-level Stream table format is discoverable using the SMMU\_IDR0.ST\_LEVEL field. Where 2-level Stream tables are supported, split points of 6 bits, 8 bits and 10 bits can be used. Implementations support either a linear Stream table format, or both linear and 2-level formats.

SMMUs supporting more than 64 StreamIDs (6 bits of StreamID) must also support two-level Stream tables.

Note: Implementations supporting fewer than 64 StreamIDs might support two-level Stream tables, but doing so is not useful as all streams would fit within a single second-level table.

Note: This rule means that an implementation supports two-level tables when the maximum size of linear Stream table would be too big to fit in a 4KB page.

The top-level descriptors contain a pointer to the second-level table along with the StreamID span that the table represents. Each descriptor can also be marked as invalid.

This example top-level table is depicted in Figure 3.2, where the split point is set to 8:

|   Level 1 index | Valid   | Level 2 pointer   | Span of Level 2   |   Value of L1STD.Span |
|-----------------|---------|-------------------|-------------------|-----------------------|
|               0 | Y       | 0x1000            | 2 8               |                     9 |
|               1 | Y       | 0x2F20            | 2 2               |                     3 |
|               2 | N       | -                 | -                 |                     0 |

|   Level 1 index | Valid   | Level 2 pointer   | Span of Level 2   |   Value of L1STD.Span |
|-----------------|---------|-------------------|-------------------|-----------------------|
|               3 | Y       | 0x4000            | 2 0               |                     1 |

In this example:

- StreamIDs 0-1023 (4 x 8-bit level 2 tables) are represented, though not all are valid.
- StreamIDs 0-255 are configured by the array of STEs at 0x1000 (each of which separately enables the relevant StreamID).
- StreamIDs 256-259 are configured by the array of STEs at 0x2F20 .
- StreamIDs 512-767 are all invalid.
- The STE of StreamID 768 is at 0x4000 .

A two-level table with a split point of 8 can reduce the memory usage compared to a large and sparse linear table used with PCIe. If the full 256 PCIe bus numbers are supported, the RequesterID or StreamID space is 16-bits. However, because there is usually one PCIe bus for each physical link and potentially one device for each bus, in the worst case a valid StreamID might only appear once every 256 StreamIDs.

Alternatively, a split point of 6 provides 64 bottom-level STEs, enabling use of a 4KB page for each bottom-level table.

Note: Depending on the size of the StreamID space, the L1 Stream table might require allocation of a region of physically-contiguous memory greater than a single granule. This table shows some example sizes for the amount of memory occupied by L1 and L2 Stream tables:

|   SIDSIZE |   SPLIT | L1 table size   | L2 table size   |
|-----------|---------|-----------------|-----------------|
|        16 |       6 | 8KB             | 4KB             |
|        16 |       8 | 2KB             | 16KB            |
|        16 |      10 | 512B            | 64KB            |
|        24 |       6 | 2MB             | 4KB             |
|        24 |       8 | 512KB           | 16KB            |
|        24 |      10 | 128KB           | 64KB            |

## 3.3.2 StreamIDs to Context Descriptors

The STE contains the configuration for each stream indicating:

- Whether traffic from the device is enabled.
- Whether it is subject to stage 1 translation.
- Whether it is subject to stage 2 translation, and the relevant translation tables.
- Which data structures locate translation tables for stage 1.

If stage 1 is used, the STE indicates the address of one or more CDs in memory using the STE.S1ContextPtr field.

The CD associates the StreamID with stage 1 translation table base pointers (to translate V A into IPA), per-stream configuration, and ASID. If substreams are in use, multiple CDs indicate multiple stage 1 translations, one for each substream. Transactions provided with a SubstreamID are terminated when stage 1 translation is not enabled.

If stage 2 is used, the STE contains the stage 2 translation table base pointer (to translate IPA to PA) and VMID. If multiple devices are associated with a particular virtual machine, meaning they share stage 2 translation tables, then multiple STEs might map to one stage 2 translation table.

Note: Arm expects that, where hypervisor software is present, the Stream table and stage 2 translation table are managed by the hypervisor and the CDs and stage 1 translation tables associated with devices under guest control are managed by the guest OS. Additionally, the hypervisor can make use of separate hypervisor stage 1 translations for its own internal purposes. Where a hypervisor is not used, a bare-metal OS manages the Stream table and CDs. For more information, see section 3.6 Structure and queue ownership .

When a SubstreamID is supplied with a transaction and the configuration enables substreams, the SubstreamID indexes the CDs to select a stage 1 translation context. In this configuration, if a SubstreamID is not supplied, behavior depends on the STE.S1DSS flag:

- When STE.S1DSS == 0b00 , all traffic is expected to have a SubstreamID and the lack of SubstreamID is an error. A transaction without a SubstreamID is aborted and an event recorded.
- When STE.S1DSS == 0b01 , a transaction without a SubstreamID is accepted but is treated exactly as if its configuration were stage 1-bypass. The stage 1 translations are enabled only for transactions with SubstreamIDs.
- When STE.S1DSS == 0b10 , a transaction without a SubstreamID is accepted and uses the CD of Substream 0. Under this configuration, transactions that arrive with SubstreamID 0 are aborted and an event recorded.

When stage 1 is used, the STE.S1ContextPtr field gives the address of one of the following, configured by STE.S1Fmt and STE.S1CDMax:

- A single CD.
- The start address of a single-level table of CDs.
- -The table is a contiguous array of CDs indexed by the SubstreamID.
- The start address of a first-level, L1, table of L1CDs.
- -Each L1CD.L2Ptr in the L1 table can be configured with the address of a linear level two, L2, table of CDs.
- -The L1 table is a contiguous array of L1CDs indexed by upper bits of SubstreamID. The L2 table is a contiguous array of CDs indexed by lower bits of SubstreamID. The ranges of SubstreamID bits that are used for the L1 and L2 indices are configured by STE.S1Fmt.

The S1ContextPtr and L2Ptr addresses are IPAs when both stage 1 and stage 2 are used and PAs when only stage 1 is used. S1ContextPtr is not used when stage 1 is not used.

The ASID and VMID values provided by the CD and STE structures tag TLB entries created from translation lookups performed through configuration from the CD and STEs. These tags are used on lookup to differentiate translation address spaces between different streams, or to match entries for invalidation on receipt of broadcast TLB maintenance operations. Implementations might also use these tags to efficiently allow sharing of identical translation tables between different streams.

3.3. Data structures and translation procedure

Figure 3.3: Configuration structure example

<!-- image -->

Figure 3.3 shows an example configuration in which a StreamID selects an STE from a linear Stream table, the STE points to a translation table for stage 2 and points to a single CD for stage 1 configuration, and then the CD points to translation tables for stage 1.

Figure 3.4: Multiple Context Descriptors for Substreams

<!-- image -->

Figure 3.4 shows a configuration in which an STE points to an array of several CDs. An incoming SubstreamID selects one of the CDs and therefore the SubstreamID determines which stage 1 translations are used by a transaction.

Figure 3.5: Multi-level Stream and CD tables

<!-- image -->

Figure 3.5 shows a more complex layout in which a multi-level Stream table is used. Two of the STEs point to a single CD, or a flat array of CDs, whereas the third STE points to a multi-level CD table. With multiple levels, many streams and many substreams might be supported without large physically-contiguous tables.

Figure 3.6: Translation stages and addresses

<!-- image -->

An incoming transaction is dealt with in the following logical steps:

1. If the SMMU is globally disabled (for example when it has just come out of reset with SMMU\_CR0.SMMUEN == 0), the transaction passes through the SMMU without any address modification. Global attributes, such as memory type or Shareability, might be applied from the SMMU\_GBPA register of the SMMU. Or, the SMMU\_GBPA register might be configured to abort all transactions.
2. If the global bypass described in (1) does not apply, the configuration is determined:
- a) An STE is located.
- b) If the STE enables stage 2 translation, the STE contains the stage 2 translation table base.
- c) If the STE enables stage 1 translation, a CD is located. If stage 2 translation is also enabled by the STE, the CD is fetched from IPA space which uses the stage 2 translations. Otherwise, the CD is fetched from PA space.
3. Translations are performed, if the configuration is valid.
- a) If stage 1 is configured to translate, the CD contains a translation table base which is walked. This might require stage 2 translations, if stage 2 is enabled for the STE. Otherwise, stage 1 bypasses translation and the input address is provided directly to stage 2.
- b) If stage 2 is configured to translate, the STE contains a translation table base that performs a nested walk of a stage 1 translation table if enabled, or a normal walk of an incoming IPA. Otherwise, stage 2 bypasses translation and the stage 2 input address is provided as the output address.

4. A transaction with a valid configuration that does not experience a fault on translation has the output address (and memory attributes, as appropriate) applied and is forwarded.

Note: This sequence illustrates the path of a transaction on a Non-secure stream. If Secure state is supported, the path of a transaction on a Secure stream is similar, except SMMU\_S\_CR0.SMMUEN and SMMU\_S\_GBPA control bypass.

An implementation might cache data as required for any of these steps. Section 16.2 Caching describes caching of configuration and translation structures.

Furthermore, events might occur at several stages in the process that prevent the transaction from progressing any further. If a transaction fails to locate valid configuration or is of an unsupported type, it is terminated with an abort, and an event might be recorded. If the transaction progresses as far as translation, faults can arise at either stage of translation. The configuration that is specific to the CD and STEs that are used determines whether the transaction is terminated or whether it is stalled, pending software fault resolution, see section 3.12 Fault models, recording and reporting .

The two translation stages are described using the V A to IPA and IPA to PA stages of the Armv8-A Virtualization terminology.

Note: Some systems refer to the SMMU input as a Bus Address (BA). The term VA emphasizes that the input address to the SMMU can potentially be from the same virtual address space as a PE process (using VAs).

Unless otherwise specified, translation tables and their configuration fields act exactly the same way as their equivalents specified in the Armv8-A Translation System for PEs [2].

If an SMMU does not implement one of the two stages of translation, it behaves as though that stage is configured to permanently bypass translation. Other restrictions are also relevant, for example it is not valid to configure a non-present stage to translate. An SMMU must support at least one stage of translation.

## 3.3.3 Configuration and Translation lookup

Figure 3.7: Configuration and translation lookup sequence

<!-- image -->

Figure 3.7 illustrates the concepts that are used in this specification when referring to a configuration lookup and translation lookup.

As described in 3.3.2 StreamIDs to Context Descriptors above, an incoming transaction is first subject to a

configuration lookup, and the SMMU determines how to begin to translate the transaction. This involves locating the appropriate STE then, if required, a CD.

The configuration lookup stage does not depend on the input address and is a function of the:

- SMMUglobal register configuration.
- Incoming transaction StreamID.
- Incoming transaction SubstreamID (if supplied).

The result of the configuration lookup is the stream or substream-specific configuration that locates the translation, including:

- Stage 1 translation table base pointers, ASID, and properties modifying the interpretation or walk of the translation tables (such as translation granule).
- Stage 2 translation table base pointer, VMID and properties modifying the interpretation or walk of the translation table.
- Stream-specific properties, such as the StreamWorld (the Exception Level, or translation regime, in PE terms) to which the stream is assigned.

The translation lookup stage logically works the same way as a PE memory address translation system. The output is the final physical address provided to the system, which is a function of the:

- Input address
- StreamWorld (Stream Security state and Exception level), ASID and VMID (which are provided from the previous step).

Figure 3.7 shows a PE-style TLB used in the translation lookup step. Arm expects the SMMU to use a TLB to cache translations instead of performing translation table walks for each transaction, but this is not mandatory.

Note: For clarity, Figure 3.7 does not show error reporting paths or CD fetch through stage 2 translation (which would also access the TLB or translation table walk facilities). An implementation might choose to flatten or combine some of the steps shown, while maintaining the same behavior.

A cached translation is associated with a StreamWorld that denotes its translation regime. StreamWorld is directly equivalent to an Exception level on a PE.

The StreamWorld of a translation is determined by the configuration that inserts that translation. The StreamWorld of a cached translation is determined from the combination of the Security state of an STE, its STE.Config field, its STE.STRW field, and the corresponding SMMU\_(*\_)CR2.E2H configuration. See the STE.STRW field in section 5.2 Stream Table Entry.

In addition to insertion into a TLB, the StreamWorld affects TLB lookups, and the scope of different types of TLB invalidations. An SMMU implementation is not required to distinguish between cached translations inserted for EL2 versus EL2-E2H.

For the behavior of TLB invalidations, see section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance .

A translation is associated with one of the following StreamWorlds:

| StreamWorld   | Properties equivalent to                                                                |
|---------------|-----------------------------------------------------------------------------------------|
| NS-EL1        | Non-secure EL1&0                                                                        |
| NS-EL2        | Non-secure EL2. This is when E2H is not used, and translations do not have an ASID tag. |
| NS-EL2-E2H    | Non-secure EL2&0. This is when E2H is used, and translations have an ASID tag.          |
| S-EL2         | Secure EL2. This is when E2H is not used, and translations do not have an ASID tag.     |
| S-EL2-E2H     | Secure EL2&0. This is when E2H is used, and translations have an ASID tag.              |
| Secure        | Either:                                                                                 |

| StreamWorld   | Properties equivalent to                                                                                                                                                                                                           |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| EL3           | - Secure EL1&0 when EL3 is running in AArch64 state. EL3 has a separate translation This regime has an ASID and, if Secure stage 2 is supported, a VMID. EL3 when EL3 is running in AArch64 state and FEAT_RME is not implemented. |
| Realm-EL1     | Realm EL1&0.                                                                                                                                                                                                                       |
| Realm-EL2     | Realm EL2. This is when E2H is not used, and translations do not have an ASID tag.                                                                                                                                                 |
| Realm-EL2-E2H | Realm EL2&0. This is when E2H is used, and translations have an ASID tag.                                                                                                                                                          |

Note: StreamWorld can differentiate multiple translation regimes in the SMMU that are associated with different bodies of software at different Exception levels. For example, a Secure Monitor EL3 translation for address 0x1000 is different to (and unaffected by) a Non-secure hypervisor EL2 translation for address 0x1000 , as are NS-EL1 translations for address 0x1000 . Arm expects that the StreamWorld configured for a stream in the SMMU will match the Exception level of the software that controls the stream or device.

The term any-EL2 is used to describe behaviors common to NS-EL2, S-EL2, and Realm-EL2.

The term any-EL2-E2H is used to describe behaviors common to NS-EL2-E2H, S-EL2-E2H, and Realm-EL2-E2H StreamWorlds.

In the same way as in an Armv8-A MMU, a translation is architecturally unique if it is identified by a unique set of {StreamWorld, VMID, ASID, Address} input parameters.

For example, the following are unique and can all co-exist in a translation cache:

- Entries with the same address, but different ASIDs.
- Entries with the same address and ASID, but different VMIDs.
- Entries with the same address and ASID but a different StreamWorld.

Architecturally, a translation is not uniquely identified by a StreamID and SubstreamID. This results in two properties:

- A translation is not required to be unique for a set of transaction input parameters (StreamID, SubstreamID).
- -Two streams can be configured to use the same translation configuration and the resulting ASID/VMID from their configuration lookup will identify a single set of shared translation cache entries.
- Multiple StreamID/SubstreamID configurations that result in identical ASID/VMID/StreamWorld configuration must maintain the same configuration where configuration can affect TLB lookup.
- -For example, two streams configured for a stage 1, NS-EL1 with ASID == 3 must both use the same translation table base addresses and translation granule.

When translating an address, any-EL2 and EL3 regimes use only one translation table. CD.TTB1 is unused in these configurations. All other StreamWorlds use both translation tables, and therefore CD.TTB0 and CD.TTB1 are both required.

Only some stage 1 translation table formats are valid in each StreamWorld, consistent with the PE. Valid combinations are described in the CD.AA64 description. Selecting an inconsistent combination of StreamWorld and CD.AA64 (for example, using VMSAv8-32 LPAE translation tables to represent a VMSAv8-64 EL3 translation regime) causes the CD to be ILLEGAL.

Secure stage 1 permits VMSAv8-32 LPAE, VMSAv8-64 and VMSAv9-128 translation tables. Secure stage 2 is not supported for VMSAv8-32 LPAE translation tables.

In this specification, the term TLB is used to mean the concept of a translation cache, indexed by StreamWorld/VMID/ASID and VA.

SMMUcache maintenance commands therefore fall into two groups:

- Configuration cache maintenance, acting upon StreamIDs and SubstreamIDs.
- Translation cache maintenance (or TLB maintenance), acting on addresses, ASIDs, VMIDs and StreamWorld.

The second set of commands directly matches broadcast TLB maintenance operations that might be available from PEs in some systems. The StreamWorld tag determines how TLB entries respond to incoming broadcast TLB invalidations and TLB invalidation SMMU commands, see section 3.17 TLB tagging, VMIDs, ASIDs and participation in broadcast TLB maintenance for details.

## 3.3.4 Transaction attributes: incoming, two-stage translation and overrides

In addition to an address, size and read/write attributes, an incoming transaction might be presented to the SMMU with other attributes, such as an access type (for example Device, WB-cached Normal memory), Shareability (for example Outer Shareable), cache allocation hints, and permissions-related attributes, instruction/data, privileged/unprivileged, Secure/Non-secure. Some of these attributes are used to check the access against the page permissions that are determined from the translation tables. After passing through the SMMU, a transaction presented to the system might also have a set of attributes, which might have been affected by the SMMU.

Depending on the StreamWorld configuration, these attributes can be configured differently. For example, the format of access permissions in a stage 1 translation table descriptor is affected when located from a configuration with StreamWorld == any-EL2 or StreamWorld == EL3, consistent with the Armv8 Translation System [2]. Specifically, the AP[1] bit (of the AP[2:1] field) is ignored and treated as if it were 1 because privilege checks are ignored for EL2 and EL3 (VMSAv8-64 and VMSAv9-128) translations. However, any-EL2-E2H translations maintain privileged/non-privileged checks in the same manner as EL1.

The details of how input attributes affect the attributes output into the system, in combination with translation table attributes and other configuration, is described in detail in Chapter 13 Attribute Transformation .

The input attributes are conceptually provided from the system, either conveyed from a client device that defines the transaction attributes in a device-specific way, or set in a system-specific way by the interconnect before the transaction is input to the SMMU.

As an overview:

- Permission-related attributes (instruction/data, privileged/unprivileged) and read/write properties are used for checking against translation table permissions, which might deny the access. The permission-related attributes input into the SMMU might be overridden on a per-device basis before the permission checks are performed, using the INSTCFG, PRIVCFG, and NSCFG STE fields. See section 13.5 Summary of attribute/permission configuration fields for information about output attributes.

Note: The overrides might be useful if a device is not able to express a particular kind of traffic.

- Other attributes (memory type, Shareability, cache hints) are intended to have an effect on the memory system rather than the SMMU, for example, control cache lookup for the transaction. The attributes output into the memory system are a function of the attributes specified by the translation table descriptors (at stage 1, stage 2, or stage 1 and stage 2) used to translate the input address. The SMMU might convey attributes input from a device through this process, so that the device might influence the final transaction access, and input attributes might be overridden on a per-device basis using the MTCFG/MemAttr, SHCFG, ALLOCCFG STE fields. The input attribute, modified by these fields, is primarily useful for setting the resulting output access attribute when both stage 1 and stage 2 translation is bypassed (no translation table descriptors to determine attribute) but can also be useful for stage 2-only configurations in which a device stream might have finer knowledge about the required access behavior than the general virtual machine-global stage 2 translation tables.

The STE attribute and permission override fields, MTCFG/MemAttr, SHCFG, ALLOCCFG, INSTCFG, PRIVCFG, and NSCFG, allow an incoming value to be used or, for each field, a specific override value to be selected. For example, INSTCFG can configure a stream as Always Data, replacing an incoming INST property that might be in either state. However, in SMMU implementations that are closely-coupled to, or embedded in, a device, the incoming attribute can always be considered to be the most appropriate. When an SMMU and device guarantee

3.3.

that the incoming attributes are correct, it is permissible for an SMMU to always use the incoming value for each attribute value. See SMMU\_IDR1.ATTR\_TYPES\_OVR and SMMU\_IDR1.ATTR\_PERMS\_OVR for more information. For an SMMU that cannot guarantee that these attributes are always provided correctly from the client device, for example a discrete SMMU design, Arm strongly recommends supporting overrides of incoming attributes.

## 3.3.5 Translation table descriptors

The A-profile architecture[2] defines bits [63:60] of stage 2 Block and Page descriptors as being Reserved for use by a System MMU. In SMMUv3.1 and later, these bits are Reserved, RES0.

Note: When PBHA is enabled for a bit in this range, bits [62:60] are affected by the PBHA mechanism. When PBHA is not enabled, the previous definition applies.