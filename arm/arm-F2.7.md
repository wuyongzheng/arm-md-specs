## F2.7 Load/store multiple instructions

Load Multiple instructions load from memory a subset, or possibly all, of the general-purpose registers and the PC.

Store Multiple instructions store to memory a subset, or possibly all, of the general-purpose registers.

The memory locations are consecutive word-aligned words. The addresses used are obtained from a base register, and can be either above or below the value in the base register. The base register can optionally be updated by the total size of the data transferred.

Table F2-13 summarizes the load/store multiple instructions in the T32 and A32 instruction sets.

Table F2-13 Load/store multiple instructions

| Instruction                                           | See              |
|-------------------------------------------------------|------------------|
| Load Multiple, Increment After or Full Descending     | LDM, LDMIA,LDMFD |
| Load Multiple, Decrement After or Full Ascending a    | LDMDA,LDMFA      |
| Load Multiple, Decrement Before or Empty Ascending    | LDMDB,LDMEA      |
| Load Multiple, Increment Before or Empty Descending a | LDMIB,LDMED      |
| Pop multiple registers off the stack b                | POP              |
| Push multiple registers onto the stack c              | PUSH             |
| Store Multiple, Increment After or Empty Ascending    | STM, STMIA,STMEA |
| Store Multiple, Decrement After or Empty Descending a | STMDA,STMED      |
| Store Multiple, Decrement Before or Full Descending   | STMDB,STMFD      |
| Store Multiple, Increment Before or Full Ascending a  | STMIB, STMFA     |

When executing at EL1, variants of the LDM and STM instructions load and store User mode registers. Another system level variant of the LDM instruction performs an exception return.

## F2.7.1 Loads to the PC

The LDM , LDMDA , LDMDB , LDMIB , and POP instructions can load a value into the PC. The value loaded is treated as an interworking address, as described by the LoadWritePC() pseudocode function in Pseudocode description of operations on the AArch32 general-purpose registers and the PC.