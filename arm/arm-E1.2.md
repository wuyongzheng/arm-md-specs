## E1.2 The Application level programmers' model in AArch32 state

The following sections give more information about the application level programmers' model in AArch32 state:

- Instruction sets, arithmetic operations, and register files.
- Core data types and arithmetic in AArch32 state.
- The general-purpose registers, and the PC, in AArch32 state.
- Process state, PSTATE.
- Jazelle support.

## E1.2.1 Instruction sets, arithmetic operations, and register files

The T32 and A32 instruction sets both provide a wide range of integer arithmetic and logical operations, that operate on a register file of sixteen 32-bit registers, that are comprised of the AArch32 general-purpose registers and the PC. As described in The general-purpose registers, and the PC, in AArch32 state, these registers include the registers SP (R13) and LR (R14), which have specialized uses. Core data types and arithmetic in AArch32 state gives more information about these operations.

In addition, an implementation that implements the T32 and A32 instruction sets includes both:

- Scalar floating-point instructions.
- The Advanced SIMD vector instructions.

Floating-point and vector instructions operate on a separate common register file, described in The SIMD and floating-point register file. Advanced SIMD and floating-point instructions gives more information about these instructions.

## E1.2.2 Core data types and arithmetic in AArch32 state

When executing in AArch32 state, a PE supports the following data types in memory:

Byte

8 bits.

Halfword

16 bits.

Word

32 bits.

Doubleword

64 bits.

PE registers are 32 bits in size. The instruction sets provide instructions that use the following data types for data held in registers:

- 32-bit pointers.
- Unsigned or signed 32-bit integers.
- Unsigned 16-bit or 8-bit integers, held in zero-extended form.
- Signed 16-bit or 8-bit integers, held in sign-extended form.
- Two 16-bit integers packed into a register.
- Four 8-bit integers packed into a register.
- Unsigned or signed 64-bit integers held in two registers.

Load and store operations can transfer bytes, halfwords, or words to and from memory. Loads of bytes or halfwords zero-extend or sign-extend the data as it is loaded, as specified in the appropriate load instruction.

The instruction sets include load and store operations that transfer two or more words to and from memory. Software can load and store doublewords using these instructions.

Note

For information about the atomicity of memory accesses, see Atomicity in the Arm architecture.

When any of the data types is described as unsigned , the N-bit data value represents a non-negative integer in the range 0 to 2 N -1, using normal binary format.

When any of these types is described as signed , the N-bit data value represents an integer in the range -2 (N-1) to +2 (N-1) -1, using two's complement format.

The instructions that operate on packed halfwords or bytes include some multiply instructions that use only one of two halfwords, and SIMD instructions that perform parallel addition or subtraction on all of the halfwords or bytes.

Note

These SIMD instructions operate on values held in the general-purpose registers, and must not be confused with the Advanced SIMD instructions that operate on a separate register file that provides registers of up to 128 bits.

Direct instruction support for 64-bit integers is limited, and most 64-bit operations require sequences of two or more instructions to synthesize them.

## E1.2.2.1 Integer arithmetic

The instruction set provides a wide range of operations on the values in registers, including bitwise logical operations, shifts, additions, subtractions, multiplications, and divisions. The pseudocode described in Arm Pseudocode Definition defines these operations, usually in one of three ways:

- By direct use of the pseudocode operators and built-in functions defined in Operators.
- By use of pseudocode helper functions defined in the main text.
- By a sequence of the form:
1. Use of the SInt() , UInt() , and Int() built-in functions defined in Converting bitstrings to integers to convert the bitstring contents of the instruction operands to the unbounded integers that they represent as two's complement or unsigned integers.
2. Use of mathematical operators, built-in functions and helper functions on those unbounded integers to calculate other such integers.
3. Use of either the bitstring extraction operator defined in Bitstring concatenation and slicing or of the saturation helper functions described in Pseudocode description of saturation to convert an unbounded integer result into a bitstring result that can be written to a register.

## E1.2.2.1.1 Shift and rotate operations

The following types of shift and rotate operations are used in instructions:

## Logical Shift Left

The LSL() pseudocode function moves each bit of a bitstring left by a specified number of bits. Zeros are shifted in at the right end of the bitstring. Bits that are shifted off the left end of the bitstring are discarded, except that the last such bit can be produced as a carry output.

## Logical Shift Right

The LSR() pseudocode function moves each bit of a bitstring right by a specified number of bits. Zeros are shifted in at the left end of the bitstring. Bits that are shifted off the right end of the bitstring are discarded, except that the last such bit can be produced as a carry output.

## Arithmetic Shift Right

The ASR() pseudocode function moves each bit of a bitstring right by a specified number of bits. Copies of the leftmost bit are shifted in at the left end of the bitstring. Bits that are shifted off the right end of the bitstring are discarded, except that the last such bit can be produced as a carry output.

## Rotate Right

The ROR() pseudocode function moves each bit of a bitstring right by a specified number of bits. Each bit that is shifted off the right end of the bitstring is re-introduced at the left end. The last bit shifted off the right end of the bitstring can be produced as a carry output.

## Rotate Right with Extend

The RRX() pseudocode function moves each bit of a bitstring right by one bit. A carry input is shifted in at the left end of the bitstring. The bit shifted off the right end of the bitstring can be produced as a carry output.

## E1.2.2.1.2 Pseudocode description of addition and subtraction

In pseudocode, addition and subtraction can be performed on any combination of unbounded integers and bitstrings, provided that if they are performed on two bitstrings, the bitstrings must be identical in length. The result is another unbounded integer if both operands are unbounded integers, and a bitstring of the same length as the bitstring operand or operands otherwise. For the definition of these operations, see Addition and subtraction.

The main addition and subtraction instructions can produce status information about both unsigned carry and signed overflow conditions. When necessary, multi-word additions and subtractions can be synthesized from this status information. In pseudocode, the AddWithCarry() function provides an addition with a carry input and a set of output Condition flags including carry output and overflow:

An important property of the AddWithCarry() function is that if:

- (result, nzcv) = AddWithCarry(x, NOT(y), carry\_in) Then: · If carry\_in == '1' , then result == x-y with: -nzcv&lt;0&gt; == '1' if signed overflow occurred during the subtraction. -nzcv&lt;1&gt; == '1' if unsigned borrow did not occur during the subtraction, that is, if x ≥ y . · If carry\_in == '0' , then result == x-y-1 with: -nzcv&lt;0&gt; == '1' if signed overflow occurred during the subtraction. .
- -nzcv&lt;1&gt; == '1' if unsigned borrow did not occur during the subtraction, that is, if x ≥ y

Taken together, this means that the carry\_in and nzcv&lt;1&gt; output in AddWithCarry() calls can act as NOT borrow flags for subtractions as well as carry flags for additions.

## E1.2.2.1.3 Pseudocode description of saturation

Some instructions perform saturating arithmetic , that is, if the result of the arithmetic overflows the destination signed or unsigned N-bit integer range, the result produced is the largest or smallest value in that range, rather than wrapping around modulo 2 N . This is supported in pseudocode by:

- The SignedSatQ() and UnsignedSatQ() functions when an operation requires, in addition to the saturated result, a Boolean argument that indicates whether saturation occurred.
- The SignedSat() and UnsignedSat() functions when only the saturated result is required.

SatQ(i, N, unsigned) returns either UnsignedSatQ(i, N) or SignedSatQ(i, N) depending on the value of its third argument, and Sat(i, N, unsigned) returns either UnsignedSat(i, N) or SignedSat(i, N) depending on the value of its third argument.

## E1.2.3 The general-purpose registers, and the PC, in AArch32 state

In the AArch32 Application level view, a PE has:

- Fifteen general-purpose 32-bit registers, R0 to R14, of which R13 and R14 have alternative names reflecting how they are, or can be, used:
- -R13 is usually identified as SP.
- -R14 is usually identified as LR.
- The PC ( Program Counter ), which can be described as R15.

The specialized uses of the SP (R13), LR (R14), and PC (R15) are:

## SP, the stack pointer

The PE uses SP as a pointer to the active stack.

In the T32 instruction set, some instructions cannot access SP. Instructions that can access SP can use SP as a general-purpose register.

The A32 instruction set provides more general access to SP, and it can be used as a general-purpose register.

Note

Using SP for any purpose other than as a stack pointer might break the requirements of operating systems, debuggers, and other software systems, causing them to malfunction.

Software can refer to SP as R13.

## LR, the link register

The link register can be used to hold return link information, and some cases described in this manual require this use of the LR. When software does not require the LR for linking, it can use it for other purposes. Software can refer to LR as R14.

## PC, the Program Counter

- When executing an A32 instruction, PC reads as the address of the current instruction plus 8.
- When executing a T32 instruction, PC reads as the address of the current instruction plus 4.
- Writing an address to PC causes a branch to that address.

Most T32 instructions cannot access PC.

The A32 instruction set provides more general access to the PC, and many A32 instructions can use the PC as a general-purpose register. However, Arm deprecates the use of PC for any purpose other than as the Program Counter. See Writing to the PC for more information.

Software can refer to PC as R15.

See AArch32 general-purpose registers, the PC, and the Special-purpose registers for the system level view of these registers.

Note

In general, Arm strongly recommends using the names SP, LR, and PC instead of R13, R14, and R15. However, sometimes it is simpler to use the R13-R15 names when referring to a group of registers. For example, it is simpler to refer to registers R8 to R15 , rather than to registers R8 to R12, the SP , LR, and PC . These two descriptions of the group of registers have the same meaning.

## E1.2.3.1 Writing to the PC

In the T32 and A32 instruction sets, many data-processing instructions can write to the PC. Writes to the PC are handled as follows:

- In T32 state, the following 16-bit T32 instruction encodings branch to the value written to the PC:
- -Encoding T2 of ADD, ADDS (register).
- -Encoding T1 of MOV, MOVS (register).

The value written to the PC is forced to be halfword-aligned by ignoring its least significant bit, treating that bit as being 0.

- The B , BL , CBNZ , CBZ , TBB , and TBH instructions remain in the same instruction set state and branch to the value written to the PC.

The definition of each of these instructions ensures that the value written to the PC is correctly aligned for the current instruction set state.

- The BLX (immediate) instruction switches between T32 and A32 states and branches to the value written to the PC. Its definition ensures that the value written to the PC is correctly aligned for the new instruction set state.
- The following instructions write a value to the PC, treating that value as an interworking address to branch to, with low-order bits that determine the new instruction set state:
- -BLX (register), BX , and BXJ .
- -LDR instructions with &lt;Rt&gt; equal to the PC.
- -POP and all forms of LDM except LDM (exception return), when the register list includes the PC.
- -In A32 state only, ADC , ADD , ADR , AND , ASR (immediate), BIC , EOR , LSL (immediate), LSR (immediate), MOV , MVN , ORR , ROR (immediate), RRX , RSB , RSC , SBC , and SUB instructions with &lt;Rd&gt; equal to the PC and without flag-setting specified.

For details of how an interworking address specifies the new instruction set state and instruction address, see Pseudocode description of operations on the AArch32 general-purpose registers and the PC.

Note

The register-shifted register instructions, which are available only in the A32 instruction set and are summarized in Data-processing register (register shift), are CONSTRAINED UNPREDICTABLE if they attempt to write to the PC, see Using R15 by instruction.

- Some instructions are treated as exception return instructions, and write both the PC and the CPSR. For more information, including which instructions are exception return instructions, see Exception return to an Exception level using AArch32.
- Some instructions cause an exception, and the exception handler address is written to the PC as part of the exception entry.

## E1.2.3.2 Pseudocode description of operations on the AArch32 general-purpose registers and the PC

In pseudocode, the uses of the R[] function, with an index parameter n , are:

- Reading or writing R0-R12, SP, and LR, using n = 0-12, 13, and 14 respectively.
- Reading the PC, using n = 15.

Pseudocode description of general-purpose register and PC operations describes accesses to these registers.

Descriptions of A32 store instructions that store the PC value use the PCStoreValue() pseudocode function to specify the PC value stored by the instruction.

Writing an address to the PC causes either a simple branch to that address or an interworking branch that also selects the instruction set to execute after the branch. A simple branch is performed by the BranchWritePC() function.

An interworking branch is performed by the BXWritePC() function.

The LoadWritePC() and ALUWritePC() functions are used for two cases where the behavior was systematically modified between architecture versions.

## E1.2.4 Process state, PSTATE

Process state or PSTATE is an abstraction of process state information. All of the instruction sets provide instructions that operate on elements of PSTATE.

Note

In this chapter, references to PSTATE link to the more appropriate of:

- The Application-level view of PSTATE given in this section.
- The System-level description in Process state, PSTATE.

The following PSTATE information is accessible at EL0:

## The condition flags

Flag-setting instructions set these. They are:

- N

Negative Condition flag. If the result of the instruction is regarded as a two's complement signed integer, the PE sets this to:

- 1 if the result is negative.
- 0 if the result is positive or zero.
- Z Zero Condition flag. Set to:
- 1 if the result of the instruction is zero.
- 0 otherwise.

Aresult of zero often indicates an equal result from a comparison.

- C Carry Condition flag. Set to:
- 1 if the instruction results in a carry condition, for example an unsigned overflow that is the result of an addition.
- 0 otherwise.
- V Overflow Condition flag. Set to:
- 1 if the instruction results in an overflow condition, for example a signed overflow that is the result of an addition.
- 0 otherwise.

Conditional instructions test the N, Z, C, and V Condition flags, combining them with the Condition code for the instruction, to determine whether the instruction must be executed. In this way, execution of the instruction is conditional on the result of a previous operation. For more information about conditional execution, see Conditional execution.

## The overflow or saturation flag

- Q Some instructions can set this. For those instructions that can, the PE:
- Sets it to 1 if the instruction indicates overflow or saturation.
- Leaves it unchanged otherwise.

For more information, see Pseudocode description of saturation.

## The greater than or equal flags

GE[3:0]

The instructions described in Parallel addition and subtraction instructions update these to indicate the results from individual bytes or halfwords of the operation. These flags can control a later SEL instruction. For more information, see SEL.

PSTATE also contains PE state controls . There is no direct access to these from application level instructions, but they can be changed by side-effects of application level instructions. They are:

## Instruction set state

J, T

## The IT block state

IT[7:0]

## Endianness mapping

E

The current instruction set state, as shown in Table E1-1. The J bit is RES0, see the Note in this section.

## Table E1-1 PSTATE.{J, T} encoding

|   J |   T | Instruction set state   |
|-----|-----|-------------------------|
|   0 |   0 | A32                     |
|   0 |   1 | T32                     |

A32

The PE is executing the A32 instruction set, summarized in A32 Instruction Set Encoding.

T32

The PE is executing the T32 instruction set, summarized in T32 Instruction Set Encoding.

Note

## Encoding with J==1 before Armv8, Jazelle, and T32EE states

In previous versions of the Arm architecture, the encoding {1, 0} selected Jazelle state, and encoding {1, 1} selected T32EE state. From the introduction of Armv8, the architecture does not support either of these states, and these are encodings for unimplemented instruction set states, see Unimplemented instruction sets. AArch32 state requires a Trivial Jazelle implementation, see Trivial implementation of the Jazelle extension.

The If-Then controls for the T32 IT instruction, which applies to the IT block of instructions that immediately follow the IT instruction. See IT for a description of the IT instruction and its associated IT block.

For more information about the use of PSTATE.IT, see Use of PSTATE.IT.

For data accesses, controls the endianness:

0 Little-endian.

1 Big-endian.

If an implementation does not provide:

- Big-endian support for data accesses, this bit is RES0.
- Little-endian support for data accesses, this bit is RES1.

Instruction fetches are always little-endian, and ignore PSTATE.E.

## Timing control bits

DIT

Data Independent Timing (DIT) bit. For more information, see About the DIT bit.

This bit is implemented only when FEAT\_DIT is implemented.

On a reset to AArch32 state, this bit is set to 0.

## E1.2.4.1 Accessing PSTATE fields at EL0

The following sections describe which PSTATE fields can be directly accessed at EL0, and how they can be accessed:

- The Application Program Status Register, APSR.
- The SETEND instruction.

## E1.2.4.1.1 The Application Program Status Register, APSR

At EL0, some PSTATE fields can be accessed using the Special-purpose Application Program Status Register (APSR). The APSR can be directly read using the MRS instruction, and directly written using the MSR (register) and MSR (immediate) instructions.

The APSR bit assignments are:

<!-- image -->

## N, Z, C, V, bits [31:28]

The PSTATE Condition flags.

- Q, bit [27]

The PSTATE overflow or saturation flag.

Bits[26:24]

Reserved, RES0. Software can use MSR instructions that write the top byte of the APSR without using a read-modify-write sequence. If it does this, it must write zeros to bits[26:24].

## Bits[23:20, 15:0]

Reserved bits that are allocated to system features, or are available for future expansion. Unprivileged execution ignores writes to fields that are accessible only at EL1 or higher. However, application level software that writes to the APSR must treat reserved bits as Do-Not-Modify (DNM) bits. For more information about the reserved bits, see The Current Program Status Register, CPSR.

These bits are UNKNOWN on a Read, and it is permitted that, on a read of APSR:

- Bit[22] returns the value of PSTATE.PAN.
- Bit[9] returns the value of PSTATE.E.
- Bits[8:6] return the value of PSTATE.{A,I,F}, the mask bits.
- Bits[4:0] return the value of PSTATE.M[4:0]. Bit[4] is RES1 indicating that the PE is in AArch32 state.

Note

This is an exception to the general rule that an UNKNOWN field must not return information that cannot be obtained, at the current Privilege level, by an architected mechanism.

## GE[3:0], bits [19:16]

The PSTATE greater than or equal flags.

The other PSTATE fields cannot be accessed by using the APSR.

The system level alias for the APSR is the CPSR. The CPSR is a superset of the APSR. See The Current Program Status Register, CPSR.

Writes to the PSTATE fields have side-effects on various aspects of PE operation. All of these side-effects, except side-effects on memory accesses associated with fetching instructions, are synchronous to the APSR write. This means they are guaranteed:

- Not to be visible to earlier instructions in the Execution stream.
- To be visible to later instructions in the Execution stream.

## E1.2.4.1.2 The SETEND instruction

The T32 and A32 instruction sets both include an instruction to manipulate PSTATE.E:

SETEND BE Sets PSTATE.E to 1, for big-endian operation.

SETEND LE Sets PSTATE.E to 0, for little-endian operation.

The SETEND instruction is unconditional. For more information, see SETEND. Arm deprecates use of the SETEND instruction.

## E1.2.4.2 Use of PSTATE.IT

PSTATE.IT provides the If-Then controls for the T32 IT instruction, which applies to the IT block of instructions that immediately follow the IT instruction.

PSTATE.IT divides into two subfields:

IT[7:5]

Holds the base condition for the current IT block. The base condition is the top three bits of the Condition code specified by the &lt;firstcond&gt; field of the IT instruction.

IT[4:0]

Encodes:

- Implicitly, the size of the IT block. This is the number of instructions that are to be conditionally executed. The size of the block is indicated by the position of the least significant 1 in this field, as shown in Table E1-2.
- For each instruction in the IT block, the least significant bit of the Condition code. This is encoded in the IT block entries that Table E1-2 shows as N x .

Note

Changing the least significant bit of a Condition code from 0 to 1 has the effect of inverting the Condition code.

Both subfields are all zeros when no IT block is active.

When an IT instruction is executed, PSTATE.IT is set according to the &lt;firstcond&gt; field of the instruction and the Then and Else (T and E) parameters in the instruction, see IT. This means that, on executing an IT instruction, the initial state of PSTATE.IT depends on the number of instructions in the IT block, as Table E1-2 shows:

Table E1-2 Initial state of PSTATE.IT on executing an IT instruction

| Number of instructions in IT block   | PSTATE.IT bits a   | PSTATE.IT bits a   | PSTATE.IT bits a   | PSTATE.IT bits a   | Notes   | Notes   | Notes                 |
|--------------------------------------|--------------------|--------------------|--------------------|--------------------|---------|---------|-----------------------|
|                                      | [7:5]              | [4]                | [3]                | [2]                | [1]     | [0]     |                       |
| 4                                    | cond_base          | N1                 | N2                 | N3                 | N4      | 1       | -                     |
| 3                                    | cond_base          | N1                 | N2                 | N3                 | 1       | 0       | -                     |
| 2                                    | cond_base          | N1                 | N2                 | 1                  | 0       | 0       | -                     |
| 1                                    | cond_base          | N1                 | 1                  | 0                  | 0       | 0       | -                     |
| Not executing an IT instruction      | 000                | 0                  | 0                  | 0                  | 0       | 0       | No IT block is active |

In Table E1-2, N1 refers to the first instruction in the IT block, and N2, N3, and N4 refer to the second, third, and fourth instructions in the IT block if they are present,

When permitted, an instruction in an IT block is conditional, see Conditional instructions and Conditional execution. The Condition code used is the current value of IT[7:4]. When an instruction in an IT block completes its execution normally, PSTATE.IT[4:0] is left-shifted by one bit, so that PSTATE[4] always relates to the next instruction to be executed.

Table E1-3 shows how PSTATE.IT during the execution of an IT instruction with four instructions in the IT block.

Table E1-3 Updates to PSTATE.IT when executing an IT instruction with a four-instruction IT block

| IT block instruction being executed   | PSTATE.IT bits a   | PSTATE.IT bits a   | PSTATE.IT bits a   | PSTATE.IT bits a   | Notes   | Notes   | Notes                 |
|---------------------------------------|--------------------|--------------------|--------------------|--------------------|---------|---------|-----------------------|
|                                       | [7:5]              | [4]                | [3]                | [2]                | [1]     | [0]     |                       |
| First                                 | cond_base          | N1                 | N2                 | N3                 | N4      | 1       | -                     |
| Second                                | cond_base          | N2                 | N3                 | N4                 | 1       | 0       | -                     |
| Third                                 | cond_base          | N3                 | N4                 | 1                  | 0       | 0       | -                     |
| Fourth                                | cond_base          | N4                 | 1                  | 0                  | 0       | 0       | -                     |
| Not executing an IT instruction       | 000                | 0                  | 0                  | 0                  | 0       | 0       | No IT block is active |

Afew instructions, for example BKPT , cannot be conditional and therefore are always executed ignoring the current value of PSTATE.IT.

For details of what happens if an instruction in an IT block takes an exception, see Overview of exception entry.

An instruction that might complete its normal execution by branching is only permitted in an IT block as the last instruction in the block. This means that normal execution of the instruction always results in PSTATE.IT advancing to execution where no IT block is active.

Implementations can provide a set of ITD control fields, SCTLR.ITD, SCTLR\_EL1.ITD, and HSCTLR.ITD, to disable use of IT for some instructions, making them UNDEFINED. When an implementation includes ITD control fields, Changes to an ITD control by an instruction in an IT block describes the permitted CONSTRAINED UNPREDICTABLE behaviors if an instruction in an IT block changes the value of an ITD control to disable the use of the IT instruction.

On a branch or an exception return, if PSTATE.IT is set to a value that is not consistent with the instruction stream being branched to or returned to, then instruction execution is CONSTRAINED UNPREDICTABLE.

PSTATE.IT affects instruction execution only in T32 state. In A32 state, PSTATE.IT must be 0b00000000 , otherwise the behavior is CONSTRAINED UNPREDICTABLE.

For more information, see CONSTRAINED UNPREDICTABLE behavior associated with IT instructions and PSTATE.IT.

## E1.2.4.2.1 Changes to an ITD control by an instruction in an IT block

In an implementation that includes SCTLR.ITD, SCTLR\_EL1.ITD, and HSCTLR.ITD controls, if an instruction in an IT block changes an ITD control so that the IT instruction using the IT block would be disabled, then one of the following behaviors applies:

- The change to the ITD field, once synchronized, has no effect on the execution of instructions in the current IT block, but applies only to any subsequent execution of an IT instruction to which the control applies.
- Synchronizing the change to the ITD field guarantees that all bits of PSTATE.IT are cleared to 0.

In addition, after the change to the ITD field has been synchronized, any remaining instructions in the IT block that would be made UNDEFINED by the new value of ITD are either:

- Executed normally.
- Treated as UNDEFINED.

The choice between the options described in this section is determined by the implementation, and any choice can vary between different changes to an ITD control by an instruction in an IT block.

## E1.2.4.3 Pseudocode description of PSTATE PE state fields

The pseudocode function CurrentInstrSet() returns the current instruction set. The pseudocode function SelectInstrSet() selects a new instruction set.

PSTATE.IT advances after normal execution of an IT block instruction. This is described by the AArch32.ITAdvance() pseudocode function.

The pseudocode function InITBlock() tests whether the current instruction is in an IT block. The pseudocode function LastInITBlock() tests whether the current instruction is the last instruction in an IT block.

The BigEndian() pseudocode function tests whether big-endian data memory accesses are currently selected.

## E1.2.5 About the DIT bit

A data-independent-time sequence of code is the sequence of instructions executed from the first instruction executed after a change of CPSR.DIT from 0 to 1 through the last instruction executed before a change of CPSR.DIT from 1 to 0, inclusive. Instructions speculatively executed between the change of CPSR.DIT from 0 to 1 and the change of CPSR.DIT from 1 to 0 are considered part of the data-independent-time sequence of code.

A data-independent-time resource is any of:

- a general-purpose register other than the zero register (ZR)
- Stack Pointer register
- SIMD&amp;FP register
- the NZCV flags

Note

The collection of NZCV is considered a single data-indepedent-time resource.

A data-independent-time instruction is an instruction that is required to honor the data-independent timing behaviors described in this section.

A data-independent-time value is any of:

- Any given value (V) read from memory by the Explicit Memory Read Effect of a data-independent-time instruction (I1) that is executed within a data-independent-time sequence of code (C), where V is not consumed by any other instruction (I2) for which any of the following apply:
- -I2 is not a data-independent-time instruction
- -I2 is not executed in C
- -Vis used to form the address or Logical Address Tag of a Memory Effect generated by I2

- Any given value (V) written to a data-independent-time resource by a data-independent-time instruction (I1) that is executed within a data-independent-time sequence of code (C), where V is not consumed by any other instruction (I2) for which any of the following apply:

- [ ] -I2 is not a data-independent-time instruction

- [ ] - I2 is not executed in C

- [ ] - Vis used to form the address or Logical Address Tag of a Memory Effect generated by I2

- Any given value (V) read from a data-independent-time resource by a data-independent-time instruction (I1) that is executed within a data-independent-time sequence of code (C) and none of the following apply:

- [ ] - Vwas produced by another instruction (I0) and any of the following apply:

- [ ] - I0 is not a data-independent-time instruction

- [ ] - I0 is not executed in C

- [ ] - Vis used to form the address or Logical Address Tag of a Memory Effect produced by I1.

- [ ] - Vis not consumed by any other instruction (I2) for which any of the following apply:

- [ ] - I2 is not a data-independent-time instruction

- [ ] - I2 is not executed in C

- [ ] - Vis used to form the address or Logical Address Tag of a Memory Effect generated by I2

- Any given value (V) written to memory by the Explicit Memory Write Effect of a data-independent-time instruction (I1) that is executed within a data-independent-time sequence of code (C) and none of the following apply:

- [ ] - Vwas produced by another instruction (I0) and any of the following apply:

- [ ] - I0 is not a data-independent-time instruction

- [ ] - I0 is not executed in C

- [ ] - Vis used to form the address or Logical Address Tag of a Memory Effect produced by I1.

- [ ] - Vwas sourced from the zero register.

- [ ] - Vis not consumed by any other instruction (I2) for which any of the following apply:

- [ ] - I2 is not a data-independent-time instruction

- [ ] - I2 is not executed in C

- [ ] - Vis used to form the address or Logical Address Tag of a Memory Effect generated by I2

- Any given value (V) speculatively read from memory at a Location (L) as the result of executing a data-independent-time sequence of code, where L is not explicitly read by the data-independent-time sequence of code. Examples of this include:

- [ ] - Reading additional bytes from memory while reading the bytes required by an Explicit Memory Read Effect

- [ ] - Hardware-generated prefetches

- [ ] - Prefetch memory instructions

The execution time of a given data-independent-time sequence of code must be independent of all data-independent-time values.

The execution time of a data-independent-time instruction (I1) executed within a data-independent-time sequence of code must be independent of all data-independent-time values consumed or produced by I1.

The time to respond to an asynchronous exception taken from within a data-independent-time sequence of code must be independent of all data-independent-time values.

The execution of a data-independent-time sequence of code (C1) must not cause an irreversible change in microarchitectural state of the PE that would permit a sequence of code (C2) that is executed after C1 to determine any data-independent-time value accessed during the execution of C1. For the purposes of this requirement, a data-independent-time value written by an Explicit Memory Write Effect that is held in caches is not considered an irreversible change in microarchitectural state.

The execution of a data-independent-time sequence of code (C1) must not alter the state of PMU counters in a way that allows a sequence of code (C2) that is executed after C1 to determine any data-independent-time value accessed during C1.

Note

In cases where an instruction is architecturally required to only read or write a subset of a data-independent-time resource, the entire data-independent-time resource is considered to have been read or written for the sake of these requirements.

Note

The architecture does not guarantee that the execution time of a data-independent-time sequence of code is independent of data-independent-time values if those values are read-from or written-to a peripheral.

Note

The classification of a value being a data-independent-time value due to having been read from a memory location (L) by an Explicit Memory Read Effect or written to L by an Explicit Memory Write Effect is based on the particular Effect generated by a data-independent-time instruction executed from within a data-independent-time sequence of code. The value held in L is not itself considered a data-independent-time value. As a result, it is possible for the execution time of a data-independent-time sequence of code to vary based on the value held in L if L is accessed via any of the following:

- Outside the data-independent-time sequence of code; either architecturally or speculatively
- Within a data-independent-time sequence of code but not as a data-independent-time value

Note

When the value of CPSR.DIT is 0, the architecture makes no statement about the timing properties of any instructions.

Acorresponding DIT bit is added to PSTATE in AArch64 state, and to CPSR in AArch32 state.

When an exception is taken from AArch32 state to AArch32 state, CPSR.DIT is copied to SPSR.DIT.

When an exception is taken from AArch32 state to AArch64 state, CPSR.DIT is copied to SPSR\_ELx.DIT.

When an exception returns to AArch32 state from AArch32 state, SPSR.DIT is copied to CPSR.DIT.

When an exception returns to AArch32 state from AArch64 state, SPSR\_ELx.DIT is copied to CPSR.DIT.

CPSR.DIT bit can be written using an MSR instruction at any Exception Level in AArch32 state, and read using an MRS instruction at any Exception Level.

## E1.2.6 Jazelle support

The architecture requires AArch32 state to include a trivial implementation of the Jazelle Extension, as described in Trivial implementation of the Jazelle extension.