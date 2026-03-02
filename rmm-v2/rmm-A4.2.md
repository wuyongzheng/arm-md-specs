## A4.2 REC entry

This section describes REC entry.

## See also:

- A4.3 REC exit
- B4.5.51 RMI\_REC\_ENTER command

## A4.2.1 RmiRecEnter object

- An RmiRecEnter object is a data structure used to pass values from the Host to the RMM on REC entry.
- An RmiRecEnter object is stored in the RecRun object which is passed by the Host as an input to the RMI\_REC\_ENTER command.
- On REC entry, execution state is restored from the REC object and from the RmiRecEnter object to the PE.
- An RmiRecEnter object contains attributes which are used to manage Realm virtual interrupts.



- The attributes of an RmiRecEnter object are summarized in the following table.

| Name     | Byte offset   | Type             | Description   |
|----------|---------------|------------------|---------------|
| flags    | 0x0           | RmiRecEnterFlags | Flags         |
| gprs[31] | 0x200         | Bits64           | Registers     |

In this chapter, both rec\_enter and 'the RmiRecEnter object' refer to the RmiRecEnter object which is provided to the RMI\_REC\_ENTER command.

On REC entry, all rec\_enter fields are ignored unless specified otherwise.

## See also:

- A2.4 Realm Execution Context
- A4.3.1 RmiRecExit object


- Chapter A6 Realm interrupts and timers
- B4.6.64 RmiRecEnter type

## A4.2.2 General purpose registers restored on REC entry

On REC entry, if the most recent exit from the target REC was a REC exit due to PSCI, then all of the following occur:

- X0 to X6 contain the PSCI return code and PSCI output values.
- GPR values X7 to X30 are restored from the REC object to the PE.

On REC entry, if either this is the first entry to this REC, or the most recent exit from the target REC was not a REC exit due to PSCI, then GPR values X0 to X30 are restored from the REC object to the PE.

On REC entry, if rec.pending is REC\_PENDING\_HOST\_CALL, then GPR values X0 to X30 are copied from rec\_enter.gprs[0..30] to the RsiHostCall data structure.

On REC entry, if writing to the RsiHostCall data structure fails due to the target IPA not being mapped then a REC exit to Data Abort results.

OnRECentry, if writing to the RsiHostCall data structure succeeds then rec.pending is REC\_PENDING\_NONE.

- On REC entry, if RMM access to rec\_enter causes a GPF then the RMI\_REC\_ENTER command fails with RMI\_ERROR\_INPUT.

See also:

- A4.3.3 General purpose registers saved on REC exit
- A4.3.4.3 REC exit due to Data Abort
- A4.3.7 REC exit due to PSCI
- A4.3.9 REC exit due to Host call
- A4.5 Host call

## A4.2.3 REC entry following REC exit due to Data Abort

- On REC entry, if rec\_enter.flags.inject\_sea == RMI\_INJECT\_SEA then the value of rec\_enter.flags.emul\_mmio is ignored.
- On REC entry, if the most recent exit from the target REC was a REC exit due to Emulatable Data Abort and rec\_enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the return address is the next instruction following the faulting instruction.
- On REC entry, if the most recent exit from the target REC was a REC exit due to Emulatable Data Abort and the Realm memory access was a read and rec\_enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the register indicated by ESR\_EL2.ISS.SRT is set to rec\_enter.gprs[0] .
- On execution of RMI\_REC\_ENTER, if the most recent exit from the target REC was not a REC exit due to Emulatable Data Abort and rec\_enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the RMI\_REC\_ENTER command fails. RLJWRK On REC entry, if the most recent exit from the target REC was a REC exit due to Data Abort at an Unprotected IPA and rec\_enter.flags.inject\_sea == RMI\_INJECT\_SEA , then a Synchronous External Abort is taken to the Realm. See also: · A4.3.4.3 REC exit due to Data Abort · A4.4 Emulated Data Aborts · A5.2.7 Realm access to an Unprotected IPA · A5.2.8 Synchronous External Aborts