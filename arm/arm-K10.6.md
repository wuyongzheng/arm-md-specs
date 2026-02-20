## K10.6 Use of the GCS Extension

This appendix describes the example codes for the Guarded Control Stack. It contains the following sections:

- Recording the call stacks from the current PE.
- Recording the call stacks from a different PE.
- Overwriting a Guarded Control Stack record from a higher Exception level.
- Thread migration between PEs.
- Switching EL0 Guarded Control Stacks from EL1.
- Synchronization of GCS accesses.

## K10.6.1 Recording the call stacks from the current PE

SNNHCN

Example K10-4shows an code sequence whereby code running on a PE can inspect the contents of the current GCS, and the synchronization that is required as part of that process.

Instructions 1, 7 and 8 are part of the program being recorded. All other instructions are part of Call stack recording software.

## Example K10-4

```
S.No. Instruction 1 BL ; Produces a store to an address 0x100. 2 MRS x0,GCSPR_EL0 3 GCSB DSYNC ; The Memory effect from instruction 1 is Ordered-before ; the Memory effect from instruction 4 as both access the same Location. 4 LDR x1,[x0] ; Load from the address 0x100. 5 STR x1,[x2] ; Store the Call stack elsewhere. 6 GCSB DSYNC ; The Memory effect from instruction 4 is Ordered-before ; the Memory effect from instruction 7 as both access the same Location. 7 RET ; Produces a load from the address 0x100. 8 BL ; Produces a store to the address 0x100.
```

## K10.6.2 Recording the call stacks from a different PE

SMLWCC

Example K10-5 shows an code sequence of code running on PE1 where the call stack is being recorded by the GCS, and PE2 is consuming the call stack from the GCS.

Instructions 1, 9 and 10 from PE1 are part of the program being recorded. All other instructions are part of Call stack recording software.

x1 is a pointer to a shared variable whose initial value is 0.

```
Example K10-5 PE1: S.No. Instruction 1 BL ; Produces a store to an address 0x100 2 GCSB DSYNC ; Instructions which observe the Memory effect from instruction 4 ; also observe the Memory effect from instruction 1 3 MOV x0,#1 4 STLR x0,[x1] ; Set flag to 1 loop1: 5 LDAR x0,[x1] 6 SUB x0,x0,#0x1 7 CBZ loop1 8 GCSB DSYNC ; Instructions with Memory effects that are Ordered-before ; Memory effects from instruction 5 are also Ordered-before ; Memory effects from instruction 10. 9 RET ; Produces a load from the address 0x100 10 BL ; Produces a store to the address 0x100 PE2:
```

```
S.No. Instruction loop2: 1 LDAR x0,[x1] 2 CBZ loop2 3 LDR ; Load from the address 0x100 4 STR ; Store the Call stack elsewhere 5 MOV x0,#2 6 STLR x0,[x1] ; Set flag to 2
```

## K10.6.3 Overwriting a Guarded Control Stack record from a higher Exception level

SKPMKV

Example K10-6 shows an code sequence where a EL0 GCS record is modified by code running at a higher Exception level.

Instructions 1, 2, 11 and 12 are executed at EL0. Execution of instruction 3 is attempted from EL0 and a synchronous exception is generated. All other instructions are executed at EL1.

## Example K10-6

```
S.No. Instruction or Exception 1 BL ; Produces a store to an address 0x100 2 <program legitimately increments the LR by 4> 3 RET ; Causes an exception as LR did not match the GCS record 4 MRS x0,GCSPR_EL0 5 GCSB DSYNC ; The Memory effect of instructions 1, 3 are Ordered-before ; the Memory effect of instructions 6, 8 6 LDR x1,[x0] ; Load from the address 0x100 7 ADD x1,x1,#0x4 ; Increment the loaded value by 4 8 STR x1,[x0] ; Store the incremented value at the address 0x100 9 GCSB DSYNC ; The Memory effect of instructions 6, 8 are Ordered-before ; the Memory effect of instructions 11, 12 10 ERET 11 RET ; Observes the store from instruction 8 12 BL ; Produces a store to the address 0x100
```

## K10.6.4 Thread migration between PEs

SQDRRJ

Example K10-7 shows an code sequence whereby Stack A is migrated from PE1 to PE2, entirely in EL0 code. x1 is a pointer to a shared variable whose initial value is 0, x3 is a pointer to a shared variable where the address of Stack Ais stored, and x2 is a pointer to the head of Stack B which is migrated in to PE1.

```
Example K10-7 PE1: S.No. Instruction 1 BL ; Produces a store to stack A ; GCSPR_EL0 is 0x1000 after instruction 1 2 MOV x2,#0x8000 ; Stack B starts at 0x8000 3 GCSSS1 x2 ; x2 is input and points to stack B 4 GCSSS2 x2 ; x2 is output and contains 0xFF8 after this instruction ; Instruction 4 includes a GCSB effect ; so that stack A contents are ; visible to PE2 5 STR x2,[x3] ; Store stack A address 6 MOV x0,#0x1 7 STLR x0,[x1] ; set flag to 1 8 BL ; Produces a store to stack B PE2:
```

```
S.No. Instruction 1 BL ; Produces a store to stack C loop: 2 LDAR x0,[x1] 3 CBZ loop 4 LDR x2,[x3] ; Load stack A address, x2 will be 0xFF8 after this ; instruction 5 GCSSS1 x2 ; x2 is input and points to stack A 6 GCSSS2 x2 ; x2 is output and points to stack C ; GCSPR_EL0 is 0x1000 after instruction 6 ; Instruction 6 includes a GCSB effect ; so that stack A contents are ; visible to PE2 7 RET ; Load from stack A ; Observes the store from instruction 1 on PE1
```

## K10.6.5 Switching EL0 Guarded Control Stacks from EL1

SVSNDV

Example K10-8 and Example K10-9 show code sequences for EL1 software switching the Guarded Control Stack of EL0 tasks. The EL1 software switches out Task 1 prior to confirming that Task 2 is ready for switching.

## Example K10-8 Switching out an EL0 stack prior to synchronizing incoming stack

```
S.No. Instruction <Task 1 is executed at EL0 and an exception is taken to EL1> 1 ADR x1, PCB1 ; Load the address of a memory structure that ; Stores the context of Task 1 2 MRS x0, GCSCRE0_EL1 3 STR x0,[x1],#0x8 ; Save GCSCRE0_EL1 of Task 1 4 MRS x0, GCSPR_EL0 5 STR x0,[x1],#0x8 ; Save GCSPR_EL0 of Task 1 6 GCSB DSYNC ; Synchronize GCS data of Task 1 7 MOV x0,#0x1 8 STLR x0,[x1] ; Save a flag to indicate that Task 1 is switched out 9 ADR x2, PCB2 ; Load the address of a memory structure that ; Stores the context of Task 2 10 loop: LDAR x0,[x2,#0x10] 11 CBZ x0, loop ; Wait till Task 2 is switched out by some other PE 12 GCSB DSYNC ; Synchronize GCS data of Task 2 13 LDR x0,[x2],#0x8 14 MSR GCSCRE0_EL1,x0 ; Set GCSCRE0_EL1 of Task 2 15 LDR x0,[x2],#0x8 16 MSR GCSPR_EL0,x0 ; Set GCSPR_EL0 of Task 2 17 ISB <An ERET will be executed to resume EL0 execution of Task 2>
```

## Example K10-9 Switching out an EL0 stack after synchronizing incoming stack

```
S.No. Instruction <Task 1 is executed at EL0 and an exception is taken to EL1> 1 ADR x2, PCB2 ; Load the address of a memory structure that ; Stores the context of Task 2 2 loop: LDAR x0,[x2,#0x10] 3 CBZ x0, loop ; Wait till Task 2 is switched out by some other PE 4 GCSB DSYNC ; Synchronize GCS data of Task 1 and Task 2 5 ADR x1, PCB1 ; Load the address of a memory structure that ; Stores the context of Task 1 6 MRS x0, GCSCRE0_EL1 7 STR x0,[x1],#0x8 ; Save GCSCRE0_EL1 of Task 1 8 MRS x0, GCSPR_EL0 9 STR x0,[x1],#0x8 ; Save GCSPR_EL0 of Task 1 10 MOV x0,#0x1 11 STLR x0,[x1] ; Save a flag to indicate that Task 1 is switched out 12 LDR x0,[x2],#0x8 13 MSR GCSCRE0_EL1,x0 ; Set GCSCRE0_EL1 of Task 2 14 LDR x0,[x2],#0x8 15 MSR GCSPR_EL0,x0 ; Set GCSPR_EL0 of Task 2 16 ISB <An ERET will be executed to resume EL0 execution of Task 2>
```

## K10.6.6 Synchronization of GCS accesses

IBSXKN

In Example K10-10, the store access from the STR instruction is observed by the GCS load access from the RET instruction, by virtue of the GCSB instruction.

IJVVRW

IZFDQL

IHKFDQ

IWFPWV

<!-- image -->

In Example K10-11, the GCS store access from the BL instruction is observed by the GCS load access from the RET instruction without requiring any explicit synchronization.

<!-- image -->

In Example K10-12, the atomic GCS access from the GCSSS1 instruction is observed by the GCS load access from the GCSSS2 instruction without requiring any explicit synchronization.

<!-- image -->

In Example K10-13, the GCS store access from the BL instruction on PE1 is observed by the GCS load access from the RET instruction on PE2, by virtue of the appropriate GCSB instructions and the ordering ensured by the STLR and LDAR instructions.

<!-- image -->

In Example K10-14, the GCS store access from the BL instruction on PE1 is observed by the GCS accesses from the GCSSS1 instruction on PE2, by virtue of the appropriate GCSB instruction and the ordering ensured by the STLR and LDAR instructions.

IDBSTS

IPRKMB

IRCSNZ

```
;x1 is a pointer to a shared variable whose initial value is 0 PE1: BL ; Store to an address 0x100 GCSB DSYNC ; Produce a GCSB effect MOV x0,#1 STLR x0,[x1] ; Set flag to 1 PE2: loop: LDAR x0,[x1] CBZ loop GCSSS1 ; Load from the address 0x100
```

In Example K10-15, the GCS store access from the BL instruction is observed by the load access from the LDR instruction, by virtue of the GCSB instruction.

```
Example K10-15 BL ; Store to an address 0x100 GCSB DSYNC ; Produce a GCSB effect MOV x3,#0x100 LDR x2,[x3] ; Load from the address 0x100
```

In Example K10-16, the GCS store access from the BL instruction on PE1 is observed by the load access from the LDR instruction on PE2, by virtue of the appropriate GCSB instruction and the ordering ensured by the STLR and LDAR instructions.

Example K10-16

```
;x1 is a pointer to a shared variable whose initial value is 0 PE1: BL ; Store to an address 0x100 GCSB DSYNC ; Produce a GCSB effect MOV x0,#1 STLR x0,[x1] ; Set flag to 1 PE2: loop: LDAR x0,[x1] CBZ loop MOV x3,#0x100 LDR x2,[x3] ; Load from the address 0x100
```

In Example K10-17, the GCS store access from the GCSSS1 instruction on PE1 is observed by the GCS load access from the RET instruction on PE2, by virtue of the appropriate GCSB instruction and the ordering ensured by the STLR and LDAR instructions.

```
Example K10-14
```

IFDQNJ

IWLGDG

IKWRFP

```
;x1 is a pointer to a shared variable whose initial value is 0 PE1: GCSSS1 ; Store to an address 0x100 MOV x0,#1 STLR x0,[x1] ; Set flag to 1 PE2: loop: LDAR x0,[x1] CBZ loop GCSB DSYNC ; Produce a GCSB effect RET ; Load from the address 0x100
```

In Example K10-18, the store access from the STR instruction on PE1 is observed by the GCS load access from the RET instruction on PE2, by virtue of the appropriate GCSB instruction and the ordering ensured by the STLR and LDAR instructions.

```
Example K10-18
```

```
;x1 is a pointer to a shared variable whose initial value is 0 PE1: STR ; Store to an address 0x100 MOV x0,#1 STLR x0,[x1] ; Set flag to 1 PE2: loop: LDAR x0,[x1] CBZ loop GCSB DSYNC ; Produce a GCSB effect RET ; Load from the address 0x100
```

In Example K10-19, the GCS store access from the BL instruction on PE1 is observed by the load access from the LDR instruction on PE2, by virtue of the appropriate GCSB instruction and the DSB instruction ensuring completion of the store.

```
Example K10-19
```

```
PE1: BL ; Store to an address 0x100 GCSB DSYNC DSB <raise an IRQ to PE2> PE2: <IRQ exception occurred> LDR x1,[x0] ; Read from the address 0x100
```

In Example K10-20, the GCS store access from the BL instruction on PE1 is observed by the GCS load access from the RET instruction on PE2, by virtue of the appropriate GCSB instructions and the DSB ensuring completion of the store.

```
Example K10-17
```

IKXZTV

ICHFPV

IWCSFM

<!-- image -->

In Example K10-21, the GCS store access from the BL instruction on PE1 is observed by the load access from the LDR instruction on PE2, on the assumption that the TLBI operation is observed by PE1 after the BL , and that the TLBI operation is completed by the DSB instruction on PE2.

<!-- image -->

In Example K10-22, the DC IVAC instruction in the following sequence does not invalidate the data produced by the BL instruction:

<!-- image -->

## K10.6.6.1 Interaction with non-coherent observers

The GCS store access from the BL instruction on PE1 is observed by the load access from the LDR instruction on, by virtue of the ordering induced by the DC and DMB instructions on PE1 and the LDAR on E1.

IYMVPM

IJPQYQ

<!-- image -->

In Example K10-24, the STR instruction from a non-coherent observer E1 in the following sequence is observed by the RET instruction on PE1.

<!-- image -->

In Example K10-25, the Memory Write effect from the STR instruction from a non-coherent observer E1 in the following sequence is observed by the GCS Memory Read effect from the RET instruction on PE2. PE1 and PE2 are in a same Inner Shareable domain, and the address 0x100 is marked with the Inner Shareable attribute.

IBWBVR

```
Example K10-25 E1: STR x1,[x0] ; Write to an address 0x100 DC CVAC, x0 DMB MOV x2,#1 STR x2,[x4] ; Send a flag to PE1 PE1: loop: LDAR x3,[x4] ; Wait for the flag from E1 CBZ x3,loop DC IVAC, x0 DMB ; Ensure DC IVAC and STR are ordered MOV x2,#2 STR x2,[x4] ; Send a flag to PE2 PE2: loop: LDAR x3,[x4] ; Wait for the flag from PE1 SUB x3,x3,#2 CBNZ x3,loop GCSB DSYNC ; Synchronize GCS accesses RET ; Load from the address 0x100
```

In Example K10-26, the GCS Memory Write effect from the BL instruction on PE1 is observed by the Memory Read effect from the LDR instruction from a non-coherent observer E1 in the following sequence. PE1 and PE2 are in a same Inner Shareable domain, and the address 0x100 is marked with the Inner Shareable attribute.

<!-- image -->