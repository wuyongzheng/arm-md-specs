## H4.3 DCC and ITR access modes

The DCC and ITR support two access modes:

| DCC and ITR access mode, links to description   | Applies when:                                 |
|-------------------------------------------------|-----------------------------------------------|
| Normal access mode                              | EDSCR.MA == 0 or the PE is in Non-debug state |
| Memory access mode                              | EDSCR.MA == 1 and the PE is in Debug state    |

## H4.3.1 Normal access mode

The Normal access mode allows use of the DCC as a communications channel between target and host. It also allows the use of the ITR for issuing instructions to the PE in Debug state.

In Normal access mode, if there is no overrun or underrun, the following occurs:

## For accesses by software:

- Direct writes to DBGDTRTX update the value in DTRTX and indirectly write 1 to TXfull.
- Direct reads from DBGDTRRX return the value in DTRRX and indirectly write 0 to RXfull.
- In AArch64 state, direct writes to DBGDTR\_EL0 update both DTRTX and DTRRX, indirectly write 1 to TXfull, and do not change RXfull:
- -DTRTX is set from bits[31:0] of the transfer register.
- -DTRRXis set from bits[63:32] of the transfer register.
- In AArch64 state, direct reads from DBGDTR\_EL0 return the concatenation of DTRRX and DTRTX, indirectly write 0 to RXfull, and do not change TXfull:
- -Bits[31:0] of the transfer register are set from DTRRX.
- -Bits[63:32] of the transfer register are set from DTRTX.

Note

For DBGDTR\_EL0, the word order is reversed for reads with respect to writes.

Software reads TXfull and RXfull using DCCSR.

## For accesses by the external debug interface:

- Writes to EDITR trigger the instruction to be executed if the PE is in Debug state:
- -If the PE is in AArch64 state, this is an A64 instruction.
- -If the PE is in AArch32 state, this is a T32 instruction. The T32 instruction is a pair of halfwords where the first halfword is taken from the lower 16-bits, and the second halfword is taken from the upper 16-bits.
- Reads of DBGDTRTX\_EL0 return the value in DTRTX and indirectly write 0 to TXfull.
- Writes to DBGDTRTX\_EL0 update the value in DTRTX and do not change TXfull.
- Reads of DBGDTRRX\_EL0 return the value in DTRRX and do not change RXfull.
- Writes to DBGDTRRX\_EL0 update the value in DTRRX and indirectly write 1 to RXfull. TXfull and RXfull are visible to the external debug interface in EDSCR.

The PE detects overrun and underrun by the external debug interface, and records errors in EDSCR.{TXU, RXO, ITO, ERR}. See Flow control of the DCC and ITR registers.

See also Synchronization of DCC and ITR accesses.

## H4.3.2 Memory access mode

When the PE is in Debug state, Memory access mode can be selected to accelerate word-aligned block reads or writes of memory by an external debugger. Memory access mode can be enabled only in Debug state, and no instructions can be issued directly by the debugger when in Memory access mode.

If there is no overrun or underrun when in Memory access mode, an access by the external debug interface results in the following:

- External reads from DBGDTRTX\_EL0 cause:
1. The existing value in DTRTX to be returned. This clears EDSCR.TXfull to 0.
2. The equivalent of LDR W1,[X0],#4 , if in AArch64 state, or LDR R1,[R0],#4 , if in AArch32 state, to be executed.
3. The equivalent of the MSR DBGDTRTX\_EL0,X1 instruction, if in AArch64 state, or the MCR p14,0,R1,c0,c5,0 instruction, if in AArch32 state, to be executed.
4. EDSCR.{TXfull, ITE} to be set to {1,1}, and X1 or R1 to be set to an UNKNOWN value.
- External writes to DBGDTRRX\_EL0 cause:
1. The value in DTRRX to be updated. This sets EDSCR.RXfull to 1.
2. The equivalent of the instruction MRS X1,DBGDTRRX\_EL0 , if in AArch64 state, or MRC p14,0,R1,c0,c5,0 if in AArch32 state, to be executed.
3. The equivalent of the instruction STR W1,[X0],#4 , if in AArch64 state, or STR R1,[R0],#4, if in AArch32 state, to be executed.
4. EDSCR.{RXfull, ITE} to be set to {0,1}, and X1 or R1 to be set to an UNKNOWN value.
- External reads from DBGDTRRX\_EL0 return the last value written to DTRRX.
- External writes to EDITR generate an overrun error.

During these accesses, EDSCR.{TXfull, RXfull, ITE} are used for flow control.

Note

An overrun or underrun might result in EDSCR.ERR being set to 1 asynchronously to the sequence of operations that are outlined in this section. As this is timing-dependent, it is UNPREDICTABLE when the EDSCR.ERR flag affects the instructions and therefore whether neither instruction, only the first instruction, or both instructions are executed. If the second instruction is executed, then the first instruction must have been executed. However, in each case X1 or R1 is set to an UNKNOWN value. This means that:

- In both cases, if the memory access instruction is not executed, then the base register X0 or R0 is not updated, meaning the debugger can determine the last accessed location.
- In the list describing External reads from DBGDTRTX\_EL0, DTRTX and EDSCR.TXfull get set to UNKNOWN values. If the load was executed, then the value that was read by the PE is lost. This means the operation might need to be repeated by the debugger, and it is not advisable to use Memory access mode to read from read-sensitive locations using the underrun and overrun detection for flow control.
- In the list describing External writes to DBGDTRRX\_EL0, EDSCR.RXfull is set to an UNKNOWN value.

AData Abort from the memory access can also set EDSCR.ERR to 1. See Data Aborts in Memory access mode.

The architecture does not require precisely when these flags are set or cleared by the sequence of operations outlined in this section. For example, in the case of an external write to DBGDTRRX\_EL0, in AArch64 state, RXfull might be cleared after step 2, or it might not be cleared until after step 3, as an implementation is free to fuse these steps into a single operation. The architecture does require that the flags are set as at step 4 when the PE is ready to accept a further read or write without causing an overrun error or an underrun error.

The process outlined in this section represents a simple sequential execution model of Memory access mode. An implementation is free to pipeline, buffer, and reorder instructions and transactions, as long as the following remain true:

- Data items are transferred into and out of the DTR in order and without loss of data, other than as a result of an overrun or an underrun.
- Data Aborts occur in order.
- The constraints of the memory type are met.
- In the list describing External reads from:

- -The MSR equivalent operation at step 3 of the sequence reads the value loaded by step 2.
- -If the list is performed in a loop, for all but the first iteration of this list, the value read by step 1 returns the values written by the MSR equivalent operation at the previous iteration of step 3.
- In the list describing External writes to:
- -The MRS equivalent operation at step 2 of the sequence returns the value written at step 1.
- -The STR equivalent at step 3 of the sequence writes the value read at step 2.
- If the PE cannot accept a read or write, as applicable, during the sequence, then the flags are updated to indicate an overrun or underrun.

See Flow control of the DCC and ITR registers for more information on overrun and underrun.

## H4.3.2.1 Ordering, access sizes and effect on Exclusives monitors

For the purposes of memory ordering, access sizes, and effect on the Exclusives monitor, accesses in Memory access mode are consistent with load/store word instructions executed by the PE.

The simple sequential access model of Memory access mode, as stated in Memory access mode, must also be ordered with respect to instructions executed as a result of External writes to EDITR in Normal mode both before and after accesses to the DTR registers in Memory access mode.

## H4.3.2.2 Data Aborts in Memory access mode

If a memory access generates a Data Abort, then:

- The Data Abort exception is taken. See Exceptions in Debug state:
- -This means EDSCR.ERR is set to 1, see Cumulative error flag.
- -If the Data Abort occurs on stage 2 of an address translation, then the values returned in the ISV field and in bits[23:14] of the ISS are UNKNOWN. If this Data Abort is taken to EL2 using AArch64, the ISS is returned by ESR\_EL2. ISS encoding for an exception from a Data Abort describes the usual encoding of this ISS. If EL2 is using AArch32 and this Data Abort is taken to Hyp mode, the ISS is returned by HSR. ISS encoding for exception from a Data Abort describes the usual encoding of this ISS.
- Register R0 retains the address that generated the abort.
- Register R1 is set to an UNKNOWN value.
- EDSCR.TXfull, for a load, or EDSCR.RXfull, for a store, is set to an UNKNOWN value.
- DTRTX, for a load, or DTRRX, for a store, is set to an UNKNOWN value.
- EDSCR.ITE is set to 1.

## H4.3.2.3 Illegal Execution state exception

If PSTATE.IL is set to 1 when EDSCR.MA == 1, then on an external write access to DBGDTRRX\_EL0 or an external read from DBGDTRTX\_EL0, it is CONSTRAINED UNPREDICTABLE whether the PE:

- Takes an Illegal Execution state exception without performing any operations. In this case:
- -EDSCR.ERR is set to 1, see Cumulative error flag.
- -Register R0 is unchanged.
- -Register R1 is set to an UNKNOWN value.
- -EDSCR.TXfull or EDSCR.RXfull, as applicable, is set to an UNKNOWN value.
- -DTRTX or DTRRX, as applicable, is set an UNKNOWN value.
- -EDSCR.ITE is set to 1.

See also Exceptions in Debug state.

- Ignores PSTATE.IL.

Note

The typical usage model for Memory access mode involves executing instructions in Normal access mode to set up X0 before setting EDSCR.MA to 1. These instructions generate an Illegal state exception if PSTATE.IL is set to 1.

## H4.3.2.4 Alignment constraints

If the address in R0 is not aligned to a multiple of four, the behavior is as follows:

- For each external DTR access a CONSTRAINED UNPREDICTABLE choice of:
1. The PE makes an unaligned memory access to R0. If alignment checking is enabled for the memory access, this generates an Alignment fault.
2. The PE makes a memory access to Align(X[0],4) in AArch64 state, or Align(R[0],4) in AArch32 state.
3. The PE generates an Alignment fault, regardless of whether alignment checking is enabled.
4. The PE does nothing.
- Following each memory access, if there is no Data Abort, R0 is updated with an UNKNOWN value.
- For external writes to DBGDTRRX\_EL0, if the PE writes to memory, an UNKNOWN value is written.
- For external reads of DBGDTRTX\_EL0 an UNKNOWN value is returned.
- The RXfull and TXfull flags are left in an UNKNOWN state, meaning that a DBGDTRTX\_EL0 read can trigger a TXunderrun, and a DBGDTRTX\_EL0 write can trigger an RX overrun.

## H4.3.3 Memory-mapped accesses to the DCC and ITR

Writes to the flags in EDSCR by external debug interface accesses to the DCC and the ITR registers are indirect writes, because they are a side-effect of the access. The indirect write might not occur for a memory-mapped access to the external debug interface. For more information, see Register access permissions for memory-mapped accesses.