## I1.3 Access requirements for reserved and unallocated registers

This section describes the access requirements for reserved and unallocated memory-mapped components.

The following information relates to certain types of reserved accesses:

- Reads and writes of unallocated locations. These accesses are reserved for the architecture.
- Reads and writes of locations for features that are not implemented, including:
- -OPTIONAL features that are not implemented.
- -Breakpoints and watchpoints that are not implemented.
- -Performance Monitors counters that are not implemented.
- -CTI triggers that are not implemented.
- -Error records that are not implemented.

These accesses are reserved.

- Reads of WO locations. These accesses are reserved for the architecture.
- Writes to RO locations. These accesses are reserved for the architecture.

Reserved accesses are normally RAZ/WI. However, software must not rely on this property as the behavior of reserved values might change in a future revision of the architecture. Software must treat reserved accesses as RES0.

## Chapter I2 System Level Implementation of the Generic Timer

This chapter defines the system level implementation of the Generic Timer. It contains the following sections:

- About the Generic Timer specification.
- Memory-mapped counter module.
- Memory-mapped timer components.

## Note

- Generic Timer memory-mapped register descriptions describes the System level Generic Timer registers. These registers are memory-mapped.
- Additional Information for Implementations of the Generic Timer gives additional information, that does not form part of the architectural definition of a system level implementation of the Generic Timer.
- The Generic Timer in AArch64 state gives a general description of the AArch64 state view of the Generic Timer, and describes the AArch64 System register interface to the Generic Timer.
- The Generic Timer in AArch32 state gives a general description of the AArch32 state view of the Generic Timer, and describes the AArch32 System register interface to the Generic Timer.