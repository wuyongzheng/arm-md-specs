## A1.6 The Arm memory model

The Arm memory model supports:

- Generating an exception on an unaligned memory access.
- Restricting access by applications to specified areas of memory.
- Translating virtual addresses (VAs) provided by executing instructions to physical addresses (PAs).
- Altering the interpretation of multi-byte data between big-endian and little-endian.
- Controlling the order of accesses to memory.
- Controlling caches and address translation structures.
- Synchronizing access to shared memory by multiple PEs.
- Barriers that control and prevent speculative access to memory.

VA support depends on the Execution state, as follows:

## AArch64 state

## AArch32 state

Supports 32-bit virtual addressing, with the Translation Control Register determining the supported V A range. For execution at EL1 and EL0, system software can split the V A range into two subranges, each with its own translation controls.

The supported PA space is IMPLEMENTATION DEFINED, and can be discovered by system software.

Regardless of the Execution state, the Virtual Memory System Architecture (VMSA) can translate VAs to blocks or pages of memory anywhere within the supported PA space.

For more information, see:

## For execution in AArch64 state

- The AArch64 Application Level Memory Model.
- The AArch64 System Level Memory Model.
- The AArch64 Virtual Memory System Architecture.

## For execution in AArch32 state

- The AArch32 Application Level Memory Model.
- The AArch32 System Level Memory Model.
- The AArch32 Virtual Memory System Architecture.

Supports 64-bit virtual addressing, with the Translation Control Register determining the supported V A range. Execution at EL1 and EL0 supports two independent VA ranges, each with its own translation controls.