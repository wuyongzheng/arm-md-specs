## B2.1 About the Arm memory model

The Arm architecture is a weakly ordered memory architecture that permits the observation and completion of memory accesses in a different order from the program order. The following sections of this chapter provide the complete definition of the memory model.

This section contains:

- Address space.
- Memory type overview.
- SVE memory model.
- SMEmemory model.

## B2.1.1 Address space

Address calculations are performed using 64-bit registers.

However, supervisory software can configure the top eight address bits for use as a tag, as described in Address tagging. If this is done, address bits[63:56]:

- Are not considered when determining whether the address is valid.
- Are never propagated to the Program Counter.

Supervisory software determines the valid address range. Attempting to access an address that is not valid generates an MMUfault.

Simple sequential execution of instructions might overflow the valid address range. For more information, see Virtual address space overflow.

Memory accesses use the Mem[] function. This function makes an access of the required type. If supervisory software configures the top eight address bits for use as a tag, the top eight address bits are ignored.

The AccessType defines the different access types and attributes.

Note

- The AArch64 System Level Memory Model and The AArch64 Virtual Memory System Architecture include descriptions of memory system features that are transparent to the application, including memory access, address translation, memory maintenance instructions, and alignment checking and the associated fault handling. These chapters also include pseudocode descriptions of these operations.
- For information on the pseudocode that relates to memory accesses, see Basic memory access, Unaligned memory access, and Aligned memory access.

## B2.1.2 Memory type overview

The Arm architecture provides the following mutually-exclusive memory types:

- Normal

This is generally used for the majority of memory operations, both read/write and read-only operations.

Device

The Arm architecture forbids Speculative reads of any type of Device memory. This means Device memory types are suitable attributes for read-sensitive Locations.

Locations of the memory map that are assigned to peripherals are usually assigned the Device memory attribute.

Device memory has additional attributes that have the following effects:

- They prevent aggregation of reads and writes, maintaining the number and size of the specified memory accesses. See Gathering.
- They preserve the access order and synchronization requirements for accesses to a single peripheral. See Reordering.

- They indicate whether a write can be acknowledged other than at the end point. See Early Write Acknowledgement.

For more information on Normal memory and Device memory, see Memory types and attributes.

Note

Earlier versions of the Arm architecture defined a single Device memory type and a Strongly-ordered memory type. A Note in Device memory describes how these memory types map onto the Armv8 memory types.

## B2.1.3 SVE memory model

- ICZFSY

SVE predicated memory operations have a vector element size and a memory element access size. The vector element size specifies the data that is read from and written to the vector. The memory element access size specifies the amount of data that is read from and written to the memory.

- ITJQJF The vector element size and the memory element access size do not need to have the same value.
- ILGGHH For each memory element, there is an associated element address.

SVE also affects behavior in the following areas:

- Requirements for single-copy atomicity.
- SVE memory ordering relaxations.
- Load or Store of Single or Multiple registers.
- Endianness in SVE operations.
- SVE loads and stores that access Device memory.

## B2.1.4 SME memory model

RBQSCG

SMEload/store memory accesses are subject to the same rules that govern SVE load/store memory accesses.

- IWWVYJ When the PE is in Streaming SVE mode , there are relaxations for Advanced SIMD&amp;FP instructions in the following

areas:

- Streaming SVE mode memory ordering relaxations.
- Streaming SVE mode loads and stores that access Device memory.