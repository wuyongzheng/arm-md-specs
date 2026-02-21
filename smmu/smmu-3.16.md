## 3.16 Embedded Implementations

Some implementations might support the use of on-chip or internal storage for one or more of the Stream table structures, the Command queue, or the Event queue. This manifests itself as register base pointers and properties that are hard-wired to point to the on-chip storage. Such queues and structures are of a fixed size and configuration and in all cases are discoverable by system software. Software must not assume that it is necessary to allocate tables in RAM and set up pointers. It must initially probe for an existing configuration. SMMU\_IDR1.TABLES\_PRESET and SMMU\_IDR1.QUEUES\_PRESET indicate that the Stream table base address and queue base addresses are hardwired to indicate pre-existing storage for the tables or queues, or both. When SMMU\_IDR1.REL is set, the base addresses are given relative to the start of the SMMU register memory map, rather than as absolute addresses.

An implementation using internal storage for configuration and queues is not required to access this storage through the coherency domain of the PEs. Data accesses from the PE require manual cache maintenance or use of a non-cached memory type for these addresses.

For an implementation using internal storage for configuration and queues, it is required that all address regions for those configuration structures and queues do not overlap. This requirement applies both within the same physical address space, and across Non-secure and Secure PA spaces.

## 3.16.1 Changes to structure and queue storage behavior when fixed/preset

Non-preset tables/queues are stored in normal memory. When an Embedded Implementation (EI) contains a preset structure or queue in internal storage it is not required that all bits of all structures/queue entries are accessible exactly as they would be in normal memory. For example, an implementation might not provide storage for fields in structures and queues that would not be used by architected behavior.

## 3.16.1.1 Event Queue and PRI Queue

All entries in an embedded Event queue or PRI queue, that is where SMMU\_IDR1.QUEUES\_PRESET == 1, are permitted to have read-only/write-ignored behavior with respect to software accesses.

## 3.16.1.2 Command Queue

Entries in an embedded Command queue, that is where SMMU\_IDR1.QUEUES\_PRESET == 1, are readable and writable, but are not required to provide storage outside of the union of all defined fields for all implemented commands. In addition, referring to the Command encodings in Chapter 4 Commands , storage is not required to be provided for:

- Reserved and undefined fields.
- High-order bits of StreamID fields beyond the implemented range of StreamIDs.
- High-order bits of SubstreamID fields beyond the implemented range of SubstreamIDs (including the entire field if SubstreamIDs are not implemented).
- SSV fields, if SubstreamIDs are not implemented.
- STAG bits that are always generated as '0' to software.

Note: An implementation might choose to use fewer than 16 bits of STAG when communicating stalled faults to software.

- SSec, if only Non-secure state is supported.
- CMD\_SYNC MSIData, MSIAddress and MSIWriteAttributes if MSIs are not supported by the Security state of the Command queue.
- ASID[15:8] if SMMU\_IDR0.ASID16 == 0, or VMID[15:8] if SMMU\_IDR0.VMID16 == 0.
- CMD\_CFGI\_STE Leaf parameter (embedded Stream tables are single-level).
- Fields in any command type that gives rise to CERROR\_ILL.

A bit that is not stored due to these rules has RAZ/WI behavior.

Note: An implementation determines the set of required storage bits from IMPLEMENTATION SPECIFIC configuration options and values.

Software must not assume that it can write an arbitrary 16-byte sequence to a Command queue entry and read back the sequence unmodified. However, functional fields that form valid command parameters must be readable by software for debug and read-modify-write construction of commands (the queue is not considered write-only).

## 3.16.1.3 Stream Table Entry

Entries in an embedded Stream table are freely read/write accessible, but storage is not required to be provided for:

- Undefined fields.
- Reserved/ RES0 fields.
- Fields that are IGNORED in all possible configurations that an implementation supports.
- Fields permitted to have RAZ/WI behavior.

As an example, storage is not required for STE.S1ContextPtr on an SMMU that has an embedded Stream table but does not support stage 1.

Note: Fields Reserved for software use do not alter SMMU function but must be stored in their entirety.