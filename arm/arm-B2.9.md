## B2.9 Endian support

General description of endianness in the Arm architecture describes the relationship between endianness and memory addressing in the Arm architecture.

The following subsections then describe the endianness schemes supported by the architecture:

- Instruction endianness.
- Data endianness.
- Endianness of memory-mapped peripherals.

## B2.9.1 General description of endianness in the Arm architecture

This section describes only memory addressing and the effects of endianness for data elements up to quadwords of 128 bits. However, this description can be extended to apply to larger data elements.

For an address A, Figure B2-2 shows, for big-endian and little-endian memory systems, the relationship between:

- The quadword at address A.
- The doubleword at address A and A+8.
- The words at addresses A, A+4, A+8, and A+12.
- The halfwords at addresses A, A+2, A+4, A+6, A+8, A+10, A+12, and A+14.
- The bytes at addresses A, A+1, A+2, A+3, A+4, A+5, A+6, A+7, A+8, A+9, A+10, A+11, A+12, A+13, A+14, and A+15.

The terms in Figure B2-2 have the following definitions:

| B_A    | Byte at address A.      |
|--------|-------------------------|
| HW_A   | Halfword at address A.  |
| MSByte | Most significant byte.  |
| LSByte | Least significant byte. |

<!-- image -->

Figure B2-2 Endianness relationships

The big-endian and little-endian mapping schemes determine the order in which the bytes of a quadword, doubleword, word, or halfword are interpreted. For example, a load of a word from address 0x1000 always results in an access to the bytes at memory locations 0x1000 , 0x1001 , 0x1002 , and 0x1003 . The endianness mapping scheme determines the significance of these 4 bytes.

## B2.9.2 Instruction endianness

A64 instructions have a fixed length of 32 bits and are always little-endian.

## B2.9.3 Data endianness

SCTLR\_EL1.E0E, configurable at EL1 or higher, determines the data endianness for execution at EL0. When the Effective value of HCR\_EL2.{E2H,TGE} is {1, 1}, the control is from SCTLR\_EL2.E0E.

The data size used for endianness conversions:

- Is the size of the data value that is loaded or stored for SIMD and floating-point register and general-purpose register loads and stores.
- Is the size of the data element that is loaded or stored for SIMD element and data structure loads and stores. For more information, see Endianness in SIMD operations.

Note

This means the Armv8 architecture introduces a requirement for 128-bit endian conversions.

## B2.9.3.1 Instructions to reverse bytes in a general-purpose register, a SIMD and floating-point register, or an SVE scalable vector register

An application or device driver might have to interface to memory-mapped peripheral registers or shared memory structures that are not the same endianness as the internal data structures. Similarly, the endianness of the operating system might not match that of the peripheral registers or shared memory. In these cases, the PE requires an efficient method to transform explicitly the endianness of the data.

Table B2-2 shows the instructions that provide this functionality:

## Table B2-2 Byte reversal instructions

| Function                                                  | Instructions     | Notes                                          |
|-----------------------------------------------------------|------------------|------------------------------------------------|
| Reverse bytes in 32-bit word or words a                   | REV32            | For use with general-purpose registers         |
| Reverse bytes in whole register                           | REV              | For use with general-purpose registers         |
| Reverse bytes in 16-bit halfwords                         | REV16            | For use with general-purpose registers         |
| Reverse elements in doublewords, vector                   | REV64            | For use with SIMD and floating-point registers |
| Reverse elements in words, vector                         | REV32            | For use with SIMD and floating-point registers |
| Reverse elements in halfwords, vector                     | REV16            | For use with SIMD and floating-point registers |
| Reverse bytes/halfwords/words within elements, predicated | REVB, REVH, REVW | For use with SVE scalable vector registers     |

## B2.9.3.2 Endianness in SIMD operations

SIMD element load/store instructions transfer vectors of elements between memory and the SIMD and floating-point register file. An instruction specifies both the length of the transfer and the size of the data elements being transferred. This information is used to load and store data correctly in both big-endian and little-endian systems.

| For example:      |
|-------------------|
| LD1 {V0.4H}, [X1] |

This loads a 64-bit register with four 16-bit values. The four elements appear in the register in array order, with the lowest indexed element fetched from the lowest address. The order of bytes in the elements depends on the endianness configuration, as shown in Figure B2-3. Therefore, the order of the elements in the registers is the same regardless of the endianness configuration.

<!-- image -->

Figure B2-3 SIMD byte order example

The BigEndian() pseudocode function determines the current endianness of the data.

The BigEndianReverse() pseudocode function reverses the endianness of a bitstring.

The BigEndian() and BigEndianReverse() ' functions are defined in A-profile Architecture Pseudocode.

## B2.9.3.3 Endianness in SVE operations

| R VDGQK   | Rules on byte and element order of SIMD load and store instructions apply to SVE load and store instructions.                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I RFQJP   | Additional rules apply to the data endianness of memory accesses performed by SVE load and store instructions.                                                                                                                |
| R CNKCL   | For predicated SVE vector element and structure load and store instructions, an endianness conversion is performed using the memory element access size. The size of the vector element is not used in endianness conversion. |
| R QHXPL   | For unpredicated SVE vector register load and store instructions, the vector byte elements are transferred in increasing element number order without any endianness conversion.                                              |
| R RWLXY   | For unpredicated SVE predicate register load and store instructions, each 8 bits from the predicate are transferred as a byte in increasing element number order without any endianness conversion.                           |
| R YGSBQ   | When an SVE load instruction is executed, endianness conversion occurs before any sign-extension or zero-extension into a vector element.                                                                                     |
| R KYRQW   | When an SVE store instruction is executed, endianness conversion occurs after any truncation from the vector element to the memory element access size.                                                                       |

## B2.9.4 Endianness of memory-mapped peripherals

All memory-mapped peripherals defined in the Arm architecture must be little-endian.

Peripherals to which this requirement applies include:

- Memory-mapped register interfaces to a debugger, or to a Cross Trigger Interface, see About the External Debug Registers.
- The memory-mapped register interface to the system level implementation of the Generic Timer, see System Level Implementation of the Generic Timer.
- Amemory-mapped register interface to the Performance Monitors, see Recommended External Interface to the Performance Monitors.
- Amemory-mapped register interface to the Activity Monitors, see Recommended External Interface to the Activity Monitors.
- Amemory-mapped register interface to the Memory System Resource Partitioning and Monitoring architecture (MPAM), see the Arm® Memory System Resource Partitioning and Monitoring (MPAM) System Component Specification (ARM IHI 0099).
- Memory-mapped register interfaces to an Arm Generic Interface Controller, see the ARM ® Generic Interrupt Controller Architecture Specification, GIC architecture version 3 and version 4.
- The memory-mapped register interface to an Arm trace component. See, for example, the Arm ® Embedded Trace Macrocell Architecture Specification, ETMv4.