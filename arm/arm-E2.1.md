## E2.1 About the Arm memory model

The Arm architecture is a weakly ordered memory architecture that permits the observation and completion of memory accesses in a different order from the program order. The following sections of this chapter provide the complete definition of the memory model, this introduction is not intended to contradict the definition found in those sections. In general, the basic principles of the memory model are:

- To provide a memory model that has similar weaknesses to those found in the memory models used by high-level programming languages such as C or Java. For example, by permitting independent memory accesses to be reordered as seen by other observers.
- To avoid the requirement for multi-copy atomicity in the majority of memory types.
- The provision of instructions and memory barriers to compensate for the lack of multi-copy atomicity in the cases where it would be needed.
- The use of address, data, and control dependencies in the creation of order so as to avoid having excessive numbers of barriers or other explicit instructions in common situations where some order is required by the programmer or the compiler.

This section contains:

- Address space.
- Memory type overview.

## E2.1.1 Address space

Address calculations are performed using 32-bit registers. Supervisory software determines the valid address range.

Attempting to access an address that is not valid generates an MMU fault.

Address calculations are performed modulo 2 32 .

The result of an address calculation is UNKNOWN if it overflows or underflows the 32-bit address range A[31:0].

Memory accesses use the MemA[] , MemO[] , MemU[] , and MemU\_unpriv[] pseudocode functions:

- The MemA[] function makes an aligned access of the required type.
- The MemO[] function makes an ordered access of the required type.
- The MemU[] function makes an unaligned access of the required type
- The MemU\_unpriv[] function makes an unaligned, unprivileged access of the required type.

Each of these functions calls Mem\_with\_type[] function, which specifies the required access. This calls AArch32.MemSingle[] , which performs an atomic, little-endian read of size bytes.

The AccessDescriptor type defines the different access types and attributes.

Note

- The AArch32 System Level Memory Model and The AArch32 Virtual Memory System Architecture include descriptions of memory system features that are transparent to the application, including memory access, address translation, memory maintenance instructions, and alignment checking and the associated fault handling. These chapters also reference pseudocode descriptions of these operations.
- For references to the pseudocode that relates to memory accesses, see Basic memory access, Unaligned memory access, and Aligned memory access.

## E2.1.2 Memory type overview

The architecture provides the following mutually-exclusive memory types:

Normal

This is generally used for the majority of memory operations, both read/write and read-only operations.

## Device

The Arm architecture forbids speculative reads of any type of Device memory. This means Device memory types are suitable attributes for read-sensitive locations.

Locations of the memory map that are assigned to peripherals are usually assigned the Device memory attribute.

Device memory has additional attributes that have the following effects:

- They prevent aggregation of reads and writes, maintaining the number and size of the specified memory accesses. See Gathering.
- They preserve the access order and synchronization requirements, both for accesses to a single peripheral and where there is a synchronization requirement on the observability of one or more memory write and read accesses. See Reordering
- They indicate whether a write can be acknowledged other than at the end point. See Early Write Acknowledgement.

For more information on Normal memory and Device memory, see Memory types and attributes.

Note

Earlier versions of the Arm architecture defined a single Device memory type and a Strongly-ordered memory type. A Note in Device memory describes how these memory types map onto the memory types used from the introduction of Armv8.