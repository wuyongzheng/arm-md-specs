## G4.2 Address space

The architecture is designed to support a wide range of applications with different memory requirements. It supports a range of Physical Address (PA) sizes, and provides associated control and identification mechanisms. For more information, see About VMSA v8-32.

## G4.2.1 Address space overflow or underflow

This subsection describes address space overflow or underflow:

## G4.2.1.1 Instruction address space overflow

When a PE performs a normal, sequential execution of instructions, it calculates:

(address\_of\_current\_instruction) + (size\_of\_executed\_instruction)

This calculation is performed after each instruction to determine which instruction to execute next.

If the address calculation performed after executing an A32 or T32 instruction overflows 0xFFFF\_FFFF , the Program Counter becomes UNKNOWN.

If the PE executes an instruction for which the instruction address, size, and alignment mean that it contains the bytes 0xFFFF\_FFFF and 0x0000\_0000 , the bytes that apparently from 0x0000\_0000 onwards come from an UNKNOWN address.

## G4.2.1.2 Data address space overflow and underflow

If the PE executes a load or store instruction for which the computed address, total access size, and alignment mean that it accesses bytes 0xFFFF\_FFFF and 0x0000\_0000 , then the bytes that apparently come from 0x0000\_0000 onwards come from UNKNOWN addresses.