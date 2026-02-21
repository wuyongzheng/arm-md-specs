## Chapter 5

## Data structure formats

All SMMU configuration data structures, that is Stream Table Entries and Context Descriptors, are little-endian. Translation table data might be configured for access in either endianness on some implementations, see CD.ENDI, STE.S2ENDI and SMMU\_IDR0.TTENDIAN.

All non-specified fields are RES0, Reserved, and software must set them to zero. An implementation either:

- Detects non-zero values in non-specified fields and considers the structure invalid.
- Ignores the Reserved field entirely.

All specified fields are required to be checked against the defined structure validity rules in each of the STE and CD sections.

A configuration or programming error or invalid use of any of the fields in these structures might cause the whole structure to be deemed invalid, where specified. Any transaction from a device that causes the use of an invalid structure will report an abort back to the device and will log an error event, the nature of which is specific to the nature of the misconfiguration.

A structure is used when it is indicated by an STE (or in the case of an STE itself, when an incoming transaction selects it from the Stream table, by StreamID).

The memory attribute set by SMMU\_(*\_)CR1.TABLE\_{SH,OC,IC} is used when fetching the following structures:

- Level 1 Stream Table Descriptor.
- Stream Table Entry.
- Virtual Machine Structure.

The attribute set by STE.{S1CIR,S1COR,S1CSH} is used when fetching a Level 1 Context Descriptor and Context Descriptor.

See section 3.21.3 Configuration structures and configuration invalidation completion for information on structure access, caching and invalidation rules.

See section 16.2 Caching for implementation notes on caching and interactions between structures.