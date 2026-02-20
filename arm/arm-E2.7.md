## E2.7 Endian support

General description of endianness in the Arm architecture describes the relationship between endianness and memory addressing in the Arm architecture.

The following subsections then describe the endianness schemes supported by the architecture:

- Instruction endianness.
- Data endianness.
- Endianness of memory-mapped peripherals.

## E2.7.1 General description of endianness in the Arm architecture

This section only describes memory addressing and the effects of endianness for data elements up to doubleword of 64 bits. However, this description can be extended to apply to larger data elements.

For an address A, Figure E2-2 shows, for big-endian and little-endian memory systems, the relationship between:

- The doubleword at address A.
- The words at addresses A and A+4.
- The halfwords at addresses A, A+2, A+4, and A+6.
- The bytes at addresses A, A+1, A+2, A+3, A+4, A+5, A+6, and A+7.

The terms in Figure E2-2 have the following definitions:

MSByte

Most significant byte.

LSByte

Least significant byte.

Figure E2-2 Endianness relationships in AArch32 state

<!-- image -->

<!-- image -->

## E2.7.2 Instruction endianness

The mapping of instruction memory is always little-endian.

## E2.7.3 Data endianness

The size of the data value that is loaded or stored is the size that is used for the purpose of endian conversion for floating-point, Advanced SIMD, and general-purpose register loads and stores.

Table E2-4 shows the element sizes of all the load/store instructions, for all instruction sets.

Table E2-4 Element size of load/store instructions

| Instructions                                                         | Element size   |
|----------------------------------------------------------------------|----------------|
| LDRB , LDREXB , LDRBT , LDRSB , LDRSBT , STRB , STREXB , STRBT , TBB | Byte           |
| LDRH , LDREXH , LDRHT , LDRSH , LDRSHT , STRH , STREXH , STRHT , TBH | Halfword       |
| LDR , LDRT , LDREX , STR , STRT , STREX                              | Word           |
| LDRD , LDREXD , STRD , STREXD                                        | Word           |
| All forms of LDM , PUSH , POP , RFE , SRS , all forms of STM ,       | Word           |
| LDC , STC                                                            | Word           |

| Instructions                                                                        | Element size                             |
|-------------------------------------------------------------------------------------|------------------------------------------|
| Forms of VLDM , VLDR , VPOP , VPUSH , VSTM , VSTR that transfer 32-bit Si registers | Word                                     |
| Forms of VLDM , VLDR , VPOP , VPUSH , VSTM , VSTR that transfer 64-bit Di registers | Doubleword                               |
| VLD1 , VLD2 , VLD3 , VLD4 , VST1 , VST2 , VST3 , VST4                               | Element size of the Advanced SIMD access |

CPSR.E determines the data endianness.

The data size used for endianness conversions:

- Is the size of the data value that is loaded or stored for Advanced SIMD and floating-point register and general-purpose register loads and stores.
- Is the size of the data element that is loaded or stored for Advanced SIMD element and data structure loads and stores. For more information, see Endianness in Advanced SIMD.

## E2.7.3.1 Instructions to reverse bytes in registers

An application or device driver might have to interface to memory-mapped peripheral registers or shared memory structures that are not the same endianness as the internal data structures. Similarly, the endianness of the operating system might not match that of the peripheral registers or shared memory. In these cases, the PE requires an efficient method to transform explicitly the endianness of the data.

Table E2-5 shows the instructions that provide this functionality in the T32 and A32 instruction sets.

## Table E2-5 Byte reversal instructions

| Function                                  | T32/A32 instruction   | Notes                                                               |
|-------------------------------------------|-----------------------|---------------------------------------------------------------------|
| Reverse bytes in whole register           | REV                   | For use with general purpose registers                              |
| Reverse bytes in 16-bit halfwords         | REV16                 | For use with general purpose registers                              |
| Reverse bytes in halfword and sign-extend | REVSH                 | For use with general purpose registers                              |
| Reverse elements in doublewords, vector   | VREV64                | For use with registers in the SIMD and floating-point register file |
| Reverse elements in words, vector         | VREV32                | For use with registers in the SIMD and floating-point register file |
| Reverse elements in halfwords, vector     | VREV16                | For use with registers in the SIMD and floating-point register file |

## E2.7.3.2 Endianness in Advanced SIMD

Advanced SIMD element load/store instructions transfer vectors of elements between memory and the SIMD and floating-point register file. An instruction specifies both the length of the transfer and the size of the data elements being transferred. This information is used by the PE to load and store data correctly in both big-endian and little-endian systems.

Consider, for example, the A32 or T32 instruction:

```
VLD1.16 {D0}, [R1]
```

This loads a 64-bit register with four 16-bit values. The four elements appear in the register in array order, with the lowest indexed element fetched from the lowest address. The order of bytes in the elements depends on the endianness configuration, as shown in Figure E2-3. Therefore, the order of the elements in the registers is the same regardless of the endianness configuration.

Figure E2-3 Advanced SIMD byte order example for AArch32 state

<!-- image -->

For information about the alignment of Advanced SIMD instructions, see Alignment support.

The BigEndian() pseudocode function determines the current endianness of the data.

The BigEndianReverse() pseudocode function reverses the endianness of a bitstring.

The BigEndian() and BigEndianReverse() functions are defined in A-profile Architecture Pseudocode.

## E2.7.4 Endianness of memory-mapped peripherals

All memory-mapped peripherals defined in the Arm architecture must be little-endian.

Peripherals to which this requirement applies include:

- Memory-mapped register interfaces to a debugger, or to a cross-trigger interface, see About the External Debug Registers.
- The memory-mapped register interface to the system level implementation of the Generic Timer, see System Level Implementation of the Generic Timer.
- Amemory-mapped register interface to the Performance Monitors, see Recommended External Interface to the Performance Monitors.
- Amemory-mapped register interface to the Activity Monitors, see Recommended External Interface to the Activity Monitors.
- Memory-mapped register interfaces to an Arm Generic Interface Controller, see the ARM ® Generic Interrupt Controller Architecture Specification, GIC architecture version 3 and version 4.
- The memory-mapped register interface to an Arm trace component. See, for example, the Arm ® Embedded Trace Macrocell Architecture Specification, ETMv4.