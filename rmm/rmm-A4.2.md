## A4.2 REC entry

This section describes REC entry.

## See also:

- A4.3 REC exit
- B4.3.14 RMI\_REC\_ENTER command

## A4.2.1 RmiRecEnter object

- An RmiRecEnter object is a data structure used to pass values from the Host to the RMM on REC entry.
- An RmiRecEnter object is stored in the RecRun object which is passed by the Host as an input to the RMI\_REC\_ENTER command.
- On REC entry, execution state is restored from the REC object and from the RmiRecEnter object to the PE.
- An RmiRecEnter object contains attributes which are used to manage Realm virtual interrupts.
- The attributes of an RmiRecEnter object are summarized in the following table.

| Name     | Byte offset   | Type             | Description   |
|----------|---------------|------------------|---------------|
| flags    | 0x0           | RmiRecEnterFlags | Flags         |
| gprs[0]  | 0x200         | Bits64           | Registers     |
| gprs[1]  | 0x208         | Bits64           | Registers     |
| gprs[2]  | 0x210         | Bits64           | Registers     |
| gprs[3]  | 0x218         | Bits64           | Registers     |
| gprs[4]  | 0x220         | Bits64           | Registers     |
| gprs[5]  | 0x228         | Bits64           | Registers     |
| gprs[6]  | 0x230         | Bits64           | Registers     |
| gprs[7]  | 0x238         | Bits64           | Registers     |
| gprs[8]  | 0x240         | Bits64           | Registers     |
| gprs[9]  | 0x248         | Bits64           | Registers     |
| gprs[10] | 0x250         | Bits64           | Registers     |
| gprs[11] | 0x258         | Bits64           | Registers     |
| gprs[12] | 0x260         | Bits64           | Registers     |
| gprs[13] | 0x268         | Bits64           | Registers     |
| gprs[14] | 0x270         | Bits64           | Registers     |
| gprs[15] | 0x278         | Bits64           | Registers     |
| gprs[16] | 0x280         | Bits64           | Registers     |
| gprs[17] | 0x288         | Bits64           | Registers     |
| gprs[18] | 0x290         | Bits64           | Registers     |
| gprs[19] | 0x298         | Bits64           | Registers     |
| gprs[20] | 0x2a0         | Bits64           | Registers     |



| Name          | Byte offset   | Type   | Description                             |
|---------------|---------------|--------|-----------------------------------------|
| gprs[21]      | 0x2a8         | Bits64 | Registers                               |
| gprs[22]      | 0x2b0         | Bits64 | Registers                               |
| gprs[23]      | 0x2b8         | Bits64 | Registers                               |
| gprs[24]      | 0x2c0         | Bits64 | Registers                               |
| gprs[25]      | 0x2c8         | Bits64 | Registers                               |
| gprs[26]      | 0x2d0         | Bits64 | Registers                               |
| gprs[27]      | 0x2d8         | Bits64 | Registers                               |
| gprs[28]      | 0x2e0         | Bits64 | Registers                               |
| gprs[29]      | 0x2e8         | Bits64 | Registers                               |
| gprs[30]      | 0x2f0         | Bits64 | Registers                               |
| gicv3_hcr     | 0x300         | Bits64 | GICv3 Hypervisor Control Register value |
| gicv3_lrs[0]  | 0x308         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[1]  | 0x310         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[2]  | 0x318         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[3]  | 0x320         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[4]  | 0x328         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[5]  | 0x330         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[6]  | 0x338         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[7]  | 0x340         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[8]  | 0x348         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[9]  | 0x350         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[10] | 0x358         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[11] | 0x360         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[12] | 0x368         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[13] | 0x370         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[14] | 0x378         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[15] | 0x380         | Bits64 | GICv3 List Register values              |

In this chapter, both enter and 'the RmiRecEnter object' refer to the RmiRecEnter object which is provided to the RMI\_REC\_ENTER command.

On REC entry, all enter fields are ignored unless specified otherwise.

See also:

- A2.3 Realm Execution Context
- A4.3.1 RmiRecExit object
- Chapter A6 Realm interrupts and timers
- B4.4.14 RmiRecEnter type

## A4.2.2 General purpose registers restored on REC entry

- On REC entry, if the most recent exit from the target REC was a REC exit due to PSCI, then all of the following occur:
- X0 to X6 contain the PSCI return code and PSCI output values.
- GPR values X7 to X30 are restored from the REC object to the PE.
- On REC entry, if either this is the first entry to this REC, or the most recent exit from the target REC was not a REC exit due to PSCI, then GPR values X0 to X30 are restored from the REC object to the PE.
- On REC entry, if rec.host\_call\_pending is HOST\_CALL\_PENDING, then GPR values X0 to X30 are copied from enter.gprs[0..30] to the RsiHostCall data structure.
- On REC entry, if writing to the RsiHostCall data structure fails due to the target IPA not being mapped then a REC exit to Data Abort results.
- On REC entry, if writing to the RsiHostCall data structure succeeds then rec.host\_call\_pending is NO\_HOST\_CALL\_PENDING.
- On REC entry, if RMM access to enter causes a GPF then the RMI\_REC\_ENTER command fails with RMI\_ERROR\_INPUT.

See also:

- A4.3.3 General purpose registers saved on REC exit
- A4.3.4.3 REC exit due to Data Abort
- A4.3.7 REC exit due to PSCI
- A4.3.9 REC exit due to Host call
- A4.5 Host call

## A4.2.3 REC entry following REC exit due to Data Abort

- On REC entry, if enter.flags.inject\_sea == RMI\_INJECT\_SEA then the value of enter.flags. ↪ → emul\_mmio is ignored.
- On REC entry, if the most recent exit from the target REC was a REC exit due to Emulatable Data Abort and enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the return address is the next instruction following the faulting instruction.
- On REC entry, if the most recent exit from the target REC was a REC exit due to Emulatable Data Abort and the Realm memory access was a read and enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the register indicated by ESR\_EL2.ISS.SRT is set to enter.gprs[0] .
- On execution of RMI\_REC\_ENTER, if the most recent exit from the target REC was not a REC exit due to Emulatable Data Abort and enter.flags.emul\_mmio == RMI\_EMULATED\_MMIO , then the RMI\_REC\_ENTER command fails.
- On REC entry, if the most recent exit from the target REC was a REC exit due to Data Abort at an Unprotected IPA and enter.flags.inject\_sea == RMI\_INJECT\_SEA , then a Synchronous External Abort is taken to the Realm.

See also:

- A4.3.4.3 REC exit due to Data Abort
- A4.4 Emulated Data Aborts
- A5.2.6 Realm access to an Unprotected IPA
- A5.2.7 Synchronous External Aborts