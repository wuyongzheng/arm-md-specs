## D4.2 Programmers' model

## D4.2.1 Accessing ETE registers

IVYNRB

- RNBPML
- IKPYGY

The ETE architecture provides registers for programming the ETE trace unit and reading back the programmed settings. These registers can be accessed by using one or more of the following access mechanisms:

- An external debug interface, for use by an external debugger.
- System instructions, for use by self-hosted software running on the PE being traced.

When register accesses occur simultaneously from multiple access mechanisms, the trace unit behaves as if all accesses occur atomically in any order.

## D4.2.1.1 External debug interface

The external debug interface defines an address-mapped peripheral that occupies 4KB of address space.

Note

The PE does not have to be in Debug state to program the ETE registers.

- ITBMWG Unless otherwise stated in this section, information for supported access sizes for external debug interface is covered in Supported access sizes.
- RVQWLY
- RVNNPF

RKYDTQ

The trace unit supports the following access sizes:

- Word-aligned 32-bit accesses to access 32-bit registers or either half of a 64-bit register mapped to a doubleword-aligned pair of adjacent 32-bit locations.
- Doubleword-aligned 64-bit accesses to access 64-bit registers mapped to a doubleword-aligned pair of adjacent 32-bit locations. The order in which the two halves are accessed is not specified.

Note

This means that a system implementing the Debug registers using a 32-bit bus, such as AMBA APB in CoreSight systems, with a wider system interconnect must implement a bridge between the system and the debug bus that can split 64-bit accesses.

All registers are only single-copy atomic at word granularity.

- The trace unit does not support the following accesses:
- Byte.
- Halfword.
- Unaligned word. These accesses are not single-copy atomic at word granularity.
- Unaligned doubleword. These accesses are not single-copy atomic at doubleword granularity.
- Doubleword accesses to a pair of 32-bit locations that are not a doubleword-aligned pair forming a 64-bit register.
- Quadword or higher.
- Exclusives.
- RCFRFW For accesses from the external debug interface, the size of an access is determined by the interface. In an Arm Debug Interface compliant Memory Access Port, MEM-AP, this is specified by the MEM-AP CSW register. The CoreSight APB-AP supports only word accesses.

RYFRMG The behavior of the accesses that are unsupported by the trace unit is CONSTRAINED UNPREDICTABLE and is one of the following:

- Accesses generate an External abort, and writes set the accessed register or registers to an UNKNOWN value or values.
- Reads return UNKNOWN data and writes are ignored.
- Reads return UNKNOWN data and writes set the accessed register or registers to an UNKNOWN value. This is the Arm preferred behavior.

RYSHRS

RKQMKX

RWXKDP

For accesses from the external debug interface which return an error response when AllowExternalTraceAccess() returns FALSE, EDPRSR.STAD is only set to 1 when this is the highest priority cause of the error. The following causes are higher priority than AllowExternalTraceAccess() :

- The trace unit Core power domain is powered down.
- The OS Lock is locked and the register is defined to return an error response due to the OS Lock being locked.

Accesses from the external debug interface to unimplemented or Reserved trace unit registers behave as follows:

- When the trace unit core power domain is off, the access returns an error.
- Otherwise:
- -For accesses in the range of offsets 0xF00 to 0xFFC , the access behaves as RES0H.
- -For accesses in the range of offsets 0x000 to 0xEFC :
- -When the OS Lock is locked, the response is a CONSTRAINED UNPREDICTABLE choice of an error response or behaving as RES0H.
- -When the OS Lock is unlocked and AllowExternalTraceAccess() returns FALSE, the response is a CONSTRAINED UNPREDICTABLE choice of an error response or behaving as RES0H.
- -Otherwise, the access behaves as RES0H.

Reads of write-only registers are Reserved.

RSVSNR Writes to read-only registers are Reserved.

IWTJFD

For accesses that return an error, see Behavior of a not permitted memory-mapped access for more details on how this error is handled.

## D4.2.1.2 System instructions

RVGVTS Instructions with CRn &gt;= 0b1000 are not allocated for accessing trace unit registers.

RSGPQB

IWCXDT

While the PE is in EL0, all accesses are UNDEFINED.

For consistency with the Arm architecture, System instruction accesses to registers which are not implemented generate an Undefined Instruction exception. These accesses include:

- Writes to read-only registers.
- Reads from write-only registers.
- Accesses to registers which are not present due to the configuration of the trace unit.

## D4.2.2 Synchronization of register updates

## D4.2.2.1 System registers

As defined in Synchronization requirements for AArch64 System registers, direct writes to trace unit registers are only guaranteed to be visible to execution after a subsequent Context synchronization event, which consists of one of the following:

- Taking an exception.
- Returning from an exception.
- Performing an Instruction Synchronization Barrier operation.
- Exit from Debug state.
- Executing a DCPS instruction in Debug state.
- Executing a DRPS instruction in Debug state.

Direct reads of trace unit registers while the trace unit is not in the Stable or Idle states are not guaranteed to contain the results of the trace operation of execution previous to the direct read operation.

As defined in Synchronization requirements for AArch64 System registers, a direct write to a register using the same register number that was used by a previous System instruction to write it, the final result is the value of the second write, without requiring any context synchronization between the two write instructions.

IKWCGH

IPNZZH

IQPVJQ

IWLGQK

SHSXGZ

RWPWWS

As defined in Synchronization requirements for AArch64 System registers, a direct read of a register using the same register number that was used by an earlier direct write is guaranteed to observe the value that was written, without requiring any context synchronization between the write and read instructions.

Context synchronization events are important when changing the value of TRCPRGCTLR.EN or when changing the OS Lock. After writing to TRCPRGCTLR to change the value of TRCPRGCTLR.EN, one read of TRCSTATR is required before programming any other registers. A Context synchronization event is required between writing to TRCPRGCTLRand reading TRCSTATR. If multiple reads of TRCSTATR are required, a Context synchronization event is required between each read of TRCSTATR to ensure any change to the trace unit state is observed.

When indirect writes or external writes to the registers in Table D4-2 occur, both of the following can observe the writes:

- Direct reads in finite time without explicit synchronization.
- Subsequent indirect reads without explicit synchronization.

## Table D4-2 Registers with a guarantee of observability

| Register    | Notes                                          |
|-------------|------------------------------------------------|
| TRCCLAIMSET | Claim Tag Set Register                         |
| TRCCLAIMCLR | Claim Tag Clear Register                       |
| TRCCNTVR<n> | Counter Value Register <n>                     |
| TRCSEQSTR   | Sequencer State Register                       |
| TRCSSCSR<n> | Single-shot Comparator Control Status Register |

RJQTMC

When the trace unit becomes enabled or disabled as a result of a direct write, for any instruction in program order before the direct write, the new state of the trace unit does not affect trace operations.

RKNQWS

SYKGMP

RWZQWC

RGQKGX

RXLXQL

IRCKQJ

When the trace unit becomes enabled or disabled as a result of a direct write, for any instruction after a Context synchronization event in program order after the direct write, the new state of the trace unit takes effect for any trace operations.

Note

The registers which control whether the trace unit is enabled or disabled are:

- TRCPRGCTLR.
- OSLAR\_EL1.

Arm recommends that a Context synchronization event is executed after programming the Trace Unit registers, to ensure that all updates are synchronized to the trace unit before normal code execution resumes.

When a Context synchronization event occurs while the trace unit is in the Idle or Stable states, and at no other time, indirect writes to the trace unit registers are guaranteed to be visible to direct reads.

When either of the following events occurs, and at no other time, indirect writes to the trace unit registers are guaranteed to be visible to indirect reads or external reads:

- The trace unit transitions into the Stable state.
- The trace unit transitions into the Idle state.

The trace unit functions perform indirect writes to the registers and indirect reads from the registers in architectural order.

See Trace unit programming states for more details on programming the trace unit.

## D4.2.2.2 External debugger registers

| I KNWDX   | As defined in the Synchronization of changes to the external debug registers, this section refers to accesses from the external debug interface as external reads and external writes .                                                                                                                                                                                                                                            |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I HMNWB   | As defined in Synchronization of changes to the external debug registers, explicit synchronization is not required for an external read or an external write by an external agent to be observable to a following external read or external write by that agent to the same register using the same address, so explicit synchronization is never required for registers that are accessible only in the external debug interface. |
| I YXWFD   | As defined in Synchronization of changes to the external debug registers, when an external write to a register using the same register number that was used by a previous external write is performed, the final result is the value of the second write, without requiring any context synchronization between the two write accesses.                                                                                            |
| R PGTLX   | The trace unit does not require explicit synchronization for an external write to be visible to indirect reads.                                                                                                                                                                                                                                                                                                                    |
| R DYRZC   | The trace unit does not require explicit synchronization for an external write to be visible to subsequent external reads.                                                                                                                                                                                                                                                                                                         |
| I RDFSX   | As defined in Synchronization of changes to the external debug registers, explicit synchronization is required for an external write to be visible to direct reads.                                                                                                                                                                                                                                                                |
| R MMYRJ   | While the trace unit is in the Stable or Idle states, the trace unit does not require explicit synchronization for indirect writes to be visible to external reads.                                                                                                                                                                                                                                                                |
|           | D4.2.2.3 Synchronization and the authentication interface                                                                                                                                                                                                                                                                                                                                                                          |
| R WYWMJ   | Changes to the authentication interface are indirect writes to TRCAUTHSTATUS by the controller of the authentication interface. It is IMPLEMENTATION DEFINED whether a change on the authentication interface is guaranteed to be observable to an external read of the register only after a Context synchronization event or in finite time.                                                                                     |
| I XVVKN   | For more information, see Synchronization and the authentication interface.                                                                                                                                                                                                                                                                                                                                                        |