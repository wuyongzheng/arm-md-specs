## A4.3 REC exit

This section describes REC exit.

## See also:

- A4.2 REC entry
- B4.3.14 RMI\_REC\_ENTER command

## A4.3.1 RmiRecExit object

- DPBDCB An RmiRecExit object is a data structure used to pass values from the RMM to the Host on REC exit.
- IVHJTL An RmiRecExit object is stored in the RecRun object which is passed by the Host as an input to the RMI\_REC\_ENTER command.
- IJKWPB On REC exit, execution state is saved from the PE to the REC object and to the RmiRecExit object.
- IZSCNM An RmiRecExit object contains attributes which are used to manage Realm virtual interrupts and Realm timers.
- DFFCMN The attributes of an RmiRecExit object are summarized in the following table.

| Name        | Byte offset   | Type             | Description                           |
|-------------|---------------|------------------|---------------------------------------|
| exit_reason | 0x0           | RmiRecExitReason | Exit reason                           |
| esr         | 0x100         | Bits64           | Exception Syndrome Register           |
| far         | 0x108         | Bits64           | Fault Address Register                |
| hpfar       | 0x110         | Bits64           | Hypervisor IPA Fault Address register |
| gprs[0]     | 0x200         | Bits64           | Registers                             |
| gprs[1]     | 0x208         | Bits64           | Registers                             |
| gprs[2]     | 0x210         | Bits64           | Registers                             |
| gprs[3]     | 0x218         | Bits64           | Registers                             |
| gprs[4]     | 0x220         | Bits64           | Registers                             |
| gprs[5]     | 0x228         | Bits64           | Registers                             |
| gprs[6]     | 0x230         | Bits64           | Registers                             |
| gprs[7]     | 0x238         | Bits64           | Registers                             |
| gprs[8]     | 0x240         | Bits64           | Registers                             |
| gprs[9]     | 0x248         | Bits64           | Registers                             |
| gprs[10]    | 0x250         | Bits64           | Registers                             |
| gprs[11]    | 0x258         | Bits64           | Registers                             |
| gprs[12]    | 0x260         | Bits64           | Registers                             |
| gprs[13]    | 0x268         | Bits64           | Registers                             |
| gprs[14]    | 0x270         | Bits64           | Registers                             |
| gprs[15]    | 0x278         | Bits64           | Registers                             |
| gprs[16]    | 0x280         | Bits64           | Registers                             |
| gprs[17]    | 0x288         | Bits64           | Registers                             |

| Name          | Byte offset   | Type   | Description                                         |
|---------------|---------------|--------|-----------------------------------------------------|
| gprs[18]      | 0x290         | Bits64 | Registers                                           |
| gprs[19]      | 0x298         | Bits64 | Registers                                           |
| gprs[20]      | 0x2a0         | Bits64 | Registers                                           |
| gprs[21]      | 0x2a8         | Bits64 | Registers                                           |
| gprs[22]      | 0x2b0         | Bits64 | Registers                                           |
| gprs[23]      | 0x2b8         | Bits64 | Registers                                           |
| gprs[24]      | 0x2c0         | Bits64 | Registers                                           |
| gprs[25]      | 0x2c8         | Bits64 | Registers                                           |
| gprs[26]      | 0x2d0         | Bits64 | Registers                                           |
| gprs[27]      | 0x2d8         | Bits64 | Registers                                           |
| gprs[28]      | 0x2e0         | Bits64 | Registers                                           |
| gprs[29]      | 0x2e8         | Bits64 | Registers                                           |
| gprs[30]      | 0x2f0         | Bits64 | Registers                                           |
| gicv3_hcr     | 0x300         | Bits64 | GICv3 Hypervisor Control Register value             |
| gicv3_lrs[0]  | 0x308         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[1]  | 0x310         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[2]  | 0x318         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[3]  | 0x320         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[4]  | 0x328         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[5]  | 0x330         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[6]  | 0x338         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[7]  | 0x340         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[8]  | 0x348         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[9]  | 0x350         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[10] | 0x358         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[11] | 0x360         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[12] | 0x368         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[13] | 0x370         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[14] | 0x378         | Bits64 | GICv3 List Register values                          |
| gicv3_lrs[15] | 0x380         | Bits64 | GICv3 List Register values                          |
| gicv3_misr    | 0x388         | Bits64 | GICv3 Maintenance Interrupt State Register value    |
| gicv3_vmcr    | 0x390         | Bits64 | GICv3 Virtual Machine Control Register value        |
| cntp_ctl      | 0x400         | Bits64 | Counter-timer Physical Timer Control Register value |

IFQZXZ

RPNWZV

| Name           | Byte offset   | Type                 | Description                                              |
|----------------|---------------|----------------------|----------------------------------------------------------|
| cntp_cval      | 0x408         | Bits64               | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl       | 0x410         | Bits64               | Counter-timer Virtual Timer Control Register value       |
| cntv_cval      | 0x418         | Bits64               | Counter-timer Virtual Timer CompareValue Register value  |
| ripas_base     | 0x500         | Bits64               | Base address of target region for pending RIPAS change   |
| ripas_top      | 0x508         | Bits64               | Top address of target region for pending RIPAS change    |
| ripas_value    | 0x510         | RmiRipas             | RIPAS value of pending RIPAS change                      |
| imm            | 0x600         | Bits16               | Host call immediate value                                |
| pmu_ovf_status | 0x700         | RmiPmuOverflowStatus | PMU overflow status                                      |

In this chapter, both exit and 'the RmiRecExit object' refer to the RmiRecExit object which is provided to the RMI\_REC\_ENTER command.

On REC exit, all exit fields are zero unless specified otherwise.

See also:

- A2.3 Realm Execution Context
- A4.2.1 RmiRecEnter object
- A4.5 Host call
- Chapter A6 Realm interrupts and timers
- Chapter A8 Realm debug and performance monitoring
- B4.4.16 RmiRecExit type

## A4.3.2 Realm exit reason

- IDYWHJ On return from the RMI\_REC\_ENTER command, the reason for the REC exit is indicated by exit.exit\_reason and exit.esr .

See also:

- B4.4.17 RmiRecExitReason type

## A4.3.3 General purpose registers saved on REC exit

RPBKVB On REC exit due to PSCI, all of the following are true:

- exit.gprs[0] contains the PSCI FID.
- exit.gprs[1..3] contain the corresponding PSCI arguments. If the PSCI command has fewer than 3 arguments, the remaining values contain zero.
- GPR values X7 to X30 are saved from the PE to the REC object.

RFNZKM On REC exit for any reason which is not REC exit due to PSCI, GPR values X0 to X30 are saved from the PE to the REC.

RMZGPT On REC exit for any reason which is neither REC exit due to Host call nor REC exit due to PSCI, exit.gprs is zero.

RFRGVT

On REC exit, if RMM access to exit causes a GPF then the RMI\_REC\_ENTER command fails with RMI\_ERROR\_INPUT.

## See also:

- A4.2.2 General purpose registers restored on REC entry
- A4.3.7 REC exit due to PSCI
- A4.3.9 REC exit due to Host call

## A4.3.4 REC exit due to synchronous exception

- ISNDHF A synchronous exception taken to R-EL2 can cause a REC exit.
- IRPSNC The following table summarises the behavior of synchronous exceptions taken to R-EL2.

| Exception class                                                   | Behavior                                                                                 |
|-------------------------------------------------------------------|------------------------------------------------------------------------------------------|
| Trapped WFI or WFE instruction execution                          | REC exit due to WFI or WFE                                                               |
| HVC instruction execution in AArch64 state                        | Unknown exception taken to Realm                                                         |
| SMC instruction execution in AArch64 state                        | One of: • REC exit due to PSCI • RSI command handled by RMM, followed by return to Realm |
| Trapped MSR, MRS or System instruction execution in AArch64 state | Emulated by RMM, followed by return to Realm                                             |
| Instruction Abort from a lower Exception level                    | REC exit due to Instruction Abort                                                        |
| Data Abort from a lower Exception level                           | REC exit due to Data Abort                                                               |

RYLFMD Realm execution of an SMC which is not part of one of the following ABIs results in a return value of SMCCC\_NOT\_SUPPORTED:

- PSCI
- RSI

## See also:

- A4.5 Host call
- Chapter B5 Realm Services Interface
- Chapter B6 Power State Control Interface

## A4.3.4.1 REC exit due to WFI or WFE

- DGLHPX A REC exit due to WFI or WFE is a REC exit due to WFI, WFIT, WFE or WFET instruction execution in a Realm.
- RVTJQF On WFI or WFIT instruction execution in a Realm, a REC exit due to WFI or WFE is caused if enter.trap\_wfi is RMI\_TRAP.
- RGBNGW On WFE or WFET instruction execution in a Realm, a REC exit due to WFI or WFE is caused if enter.trap\_wfe is RMI\_TRAP.
- RYQWST On REC exit due to WFI or WFE, all of the following are true:
- exit.exit\_reason is RMI\_EXIT\_SYNC.
- exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- exit.esr.ISS.TI contains the value of ESR\_EL2.ISS.TI at the time of the Realm exit.
- All other exit fields except for exit.givc3\_* , exit\_cnt* and exit.pmu\_ovf\_status are zero.

RBPYBC

- RMGWRC

DCYRMT

DMTZMC

RRYVFL

On REC exit due to WFI or WFE, if the exit was caused by WFET or WFIT instruction execution then exit.gprs[0] contains the timeout value.

## See also:

- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU

## A4.3.4.2 REC exit due to Instruction Abort

DGYQXK A REC exit due to Instruction Abort is a REC exit due to a Realm instruction fetch from a Protected IPA for which either of the following is true:

- HIPAS is UNASSIGNED and RIPAS is RAM
- RIPAS is DESTROYED

On REC exit due to Instruction Abort, all of the following are true:

- exit.exit\_reason is RMI\_EXIT\_SYNC.
- exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- exit.esr.ISS.SET contains the value of ESR\_EL2.ISS.SET at the time of the Realm exit.
- exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- exit.esr.ISS.IFSC contains the value of ESR\_EL2.ISS.IFSC at the time of the Realm exit.
- exit.hpfar contains the value of HPFAR\_EL2 at the time of the Realm exit.
- All other exit fields except for exit.givc3\_* , exit\_cnt* and exit.pmu\_ovf\_status are zero.

## See also:

- A5.2.2 Realm IPA state
- A5.2.3 Realm access to a Protected IPA
- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU

## A4.3.4.3 REC exit due to Data Abort

A

REC exit due to Emulatable Data Abort is a REC exit due to a Realm data access to one of the following:

- an Unprotected IPA whose HIPAS is UNASSIGNED\_NS, where the access caused ESR\_EL2.ISS.ISV to be set to '1'
- an Unprotected IPA whose HIPAS is ASSIGNED\_NS, where the access caused a stage 2 permission fault and caused ESR\_EL2.ISS.ISV to be set to '1'

A REC exit due to Non-emulatable Data Abort is a REC exit due to a Realm data access to one of the following:

- an Unprotected IPA whose HIPAS is UNASSIGNED\_NS, where the access caused ESR\_EL2.ISS.ISV to be set to '0'
- an Unprotected IPA whose HIPAS is ASSIGNED\_NS, where the access caused a stage 2 permission fault and caused ESR\_EL2.ISS.ISV to be set to '0'
- a Protected IPA whose HIPAS is UNASSIGNED and whose RIPAS is RAM
- a Protected IPA whose RIPAS is DESTROYED.

On REC exit due to Data Abort, all of the following are true:

- exit.exit\_reason is RMI\_EXIT\_SYNC.
- exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- exit.esr.ISS.SET contains the value of ESR\_EL2.ISS.SET at the time of the Realm exit.
- exit.esr.ISS.FnV contains the value of ESR\_EL2.ISS.FnV at the time of the Realm exit.
- exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- exit.esr.ISS.DFSC contains the value of ESR\_EL2.ISS.DFSC at the time of the Realm exit.
- exit.hpfar contains the value of HPFAR\_EL2 at the time of the Realm exit.

On REC exit due to Emulatable Data Abort, all of the following are true:

- rec.emulatable\_abort is EMULATABLE\_ABORT.
- exit.esr.ISS.ISV contains the value of ESR\_EL2.ISS.ISV at the time of the Realm exit.
- exit.esr.ISS.SAS contains the value of ESR\_EL2.ISS.SAS at the time of the Realm exit.
- exit.esr.ISS.SF contains the value of ESR\_EL2.ISS.SF at the time of the Realm exit.
- exit.esr.ISS.WnR contains the value of ESR\_EL2.ISS.WnR at the time of the Realm exit.
- exit.far contains the value of FAR\_EL2 at the time of the Realm exit, with bits more significant than the size of a Granule masked to zero.

On REC exit due to Non-emulatable Data Abort at an Unprotected IPA, all of the following are true:

- exit.esr.IL contains the value of ESR\_EL2.IL at the time of the Realm exit.

On REC exit due to Data Abort, all other exit fields except for exit.givc3\_* , exit\_cnt* and exit.pmu\_ovf\_status are zero.

XXHXJC On REC exit due to Emulatable Data Abort, ESR\_EL2.ISS.SSE is not propagated to the Host. This is because this field is used to emulate sign extension on loads, which must be performed by the RMM so that the Realm can rely on architecturally correct behavior of the virtual execution environment.

- XHSWFR On REC exit due to Emulatable Data Abort, the Host can calculate the faulting IPA from the exit.hpfar and exit.far values.
- RFFNHW On REC exit due to Emulatable Data Abort, if the Realm memory access was a write, exit.gprs[0] contains the value of the register indicated by ESR\_EL2.ISS.SRT at the time of the Realm exit.

RQBTPR On REC exit not due to Emulatable Data Abort, rec.emulatable\_abort is NOT\_EMULATABLE\_ABORT.

See also:

- A4.2.3 REC entry following REC exit due to Data Abort
- A4.4 Emulated Data Aborts
- A5.2.1 Realm IPA space
- A5.2.3 Realm access to a Protected IPA
- A5.2.6 Realm access to an Unprotected IPA
- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU

## A4.3.5 REC exit due to IRQ

- DYLWXK A REC exit due to IRQ is a REC exit due to an IRQ exception which should be handled by the Host.
- RTYJSX On REC exit due to IRQ, exit.exit\_reason is RMI\_EXIT\_IRQ.
- RCSQXV On REC exit due to IRQ, exit.esr is zero.

See also:

- Chapter A6 Realm interrupts and timers

## A4.3.6 REC exit due to FIQ

- DZTYMM A REC exit due to FIQ is a REC exit due to an FIQ exception which should be handled by the Host.
- RPDSBD On REC exit due to FIQ, exit.exit\_reason is RMI\_EXIT\_FIQ.
- RGXZRF On REC exit due to FIQ, exit.esr is zero.

See also:

- Chapter A6 Realm interrupts and timers

## A4.3.7 REC exit due to PSCI

IZSGFP A PSCI function executed by a Realm is either:

- handled by the RMM, returning to the Realm, or
- forwarded by the RMM to the Host via a REC exit due to PSCI .

DRFTQD A REC exit due to PSCI is a REC exit due to Realm PSCI function execution by SMC instruction which was forwarded by the RMM to the Host.

IVBJXY The following table summarises the behavior of PSCI function execution by a Realm.

PSCI functions not listed in this table are not supported. Calling a non-supported PSCI function results in a return value of PSCI\_NOT\_SUPPORTED.

| PSCI function      | Can result in REC exit due to PSCI   | Requires Host to call RMI_PSCI_COMPLETE   |
|--------------------|--------------------------------------|-------------------------------------------|
| PSCI_VERSION       | No                                   | -                                         |
| PSCI_FEATURES      | No                                   | -                                         |
| PSCI_CPU_SUSPEND   | Yes                                  | No                                        |
| PSCI_CPU_OFF       | Yes                                  | No                                        |
| PSCI_CPU_ON        | Yes                                  | Yes                                       |
| PSCI_AFFINITY_INFO | Yes                                  | Yes                                       |
| PSCI_SYSTEM_OFF    | Yes                                  | No                                        |
| PSCI_SYSTEM_RESET  | Yes                                  | No                                        |

RNTZNJ On REC exit due to PSCI, exit.exit\_reason is RMI\_EXIT\_PSCI.

RSXGJK On REC exit due to PSCI, exit.gprs contains sanitised parameters from the PSCI call.

RYTDGT On REC exit due to PSCI, if the command arguments include an MPIDR value, rec.psci\_pending is set to PSCI\_REQUEST\_PENDING. Otherwise, rec.psci\_pending is set to NO\_PSCI\_REQUEST\_PENDING.

IKKFMQ Following REC exit due to PSCI, if rec.psci\_pending is PSCI\_REQUEST\_PENDING, the Host must complete the request by calling the RMI\_PSCI\_COMPLETE command, prior to re-entering the REC.

In the call to RMI\_PSCI\_COMPLETE, the Host provides the target REC, which corresponds to the MPIDR value provided by the Realm. This is necessary because the RMM does not maintain a mapping from MPIDR values to REC addresses. The RMM validates that the REC provided by the Host matches the MPIDR value.

In the call to RMI\_PSCI\_COMPLETE, the Host provides a PSCI status value, which the RMM handles as follows:

- If the Host provides PSCI\_SUCCESS, the RMM performs the PSCI operation requested by the Realm. The result of the PSCI operation is recorded in the REC and returned to the Realm on the next entry to the calling REC.
- If the Host provides a status value other than PSCI\_SUCCESS, the RMM validates that the status code is permitted for the PSCI operation requested by the Realm. If the status code is permitted, it is recorded in the REC and returned to the Realm on the next entry to the calling REC.

## See also:

- A4.3.3 General purpose registers saved on REC exit
- B3.27 PsciReturnCodePermitted function
- B4.3.7 RMI\_PSCI\_COMPLETE command
- Chapter B6 Power State Control Interface

IMCKKH

RQRMMN

- D1.4 PSCI flows

## A4.3.8 REC exit due to RIPAS change pending

- DJGCVY A REC exit due to RIPAS change pending is a REC exit due to the Realm issuing a RIPAS change request .
- RQSSKK On REC exit due to RIPAS change pending, all of the following are true:
- exit.exit\_reason is RMI\_EXIT\_RIPAS\_CHANGE.
- exit.ripas\_base is the base address of the region on which a RIPAS change is pending.
- exit.ripas\_top is the top address of the region on which a RIPAS change is pending.
- exit.ripas\_value is the requested RIPAS value.
- rec.ripas\_addr is the base address of the region on which a RIPAS change is pending.
- rec.ripas\_top is the top address of the region on which a RIPAS change is pending.
- rec.ripas\_value is the requested RIPAS value.

## On REC exit due to RIPAS change pending:

- exit holds the base address and the size of the region on which a RIPAS change is pending. These values inform the Host of the bounds of the RIPAS change request.
- rec holds the next address to be processed in a RIPAS change, and the top of the requested RIPAS change region. These values are used by the RMM to enforce that the RMI\_RTT\_SET\_RIPAS command can only apply RIPAS change within the bounds of the RIPAS change request, and to report the progress of the RIPAS change to the Realm on the next REC entry.

On REC exit not due to RIPAS change pending, all of the following are true:

- rec.ripas\_addr is 0
- rec.ripas\_top is 0

## See also:

- A2.3.2 REC attributes
- A5.4 RIPAS change

## A4.3.9 REC exit due to Host call

DWFZXK A REC exit due to Host call is a REC exit due to RSI\_HOST\_CALL execution in a Realm.

- RGTJRP On REC exit due to Host call, all of the following are true:
- rec.host\_call\_pending is HOST\_CALL\_PENDING.
- exit.exit\_reason is RMI\_EXIT\_HOST\_CALL.
- exit.imm contains the immediate value passed to the RSI\_HOST\_CALL command.
- exit.gprs[0..30] contain the register values passed to the RSI\_HOST\_CALL command.
- All other exit fields except for exit.givc3\_* , exit\_cnt* and exit.pmu\_ovf\_status are zero.

## See also:

- A4.5 Host call
- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU
- B5.3.4 RSI\_HOST\_CALL command

## A4.3.10 REC exit due to SError

DPGMHP

- A REC exit due to SError is a REC exit due to an SError interrupt during Realm execution.
- RLRCFP On REC exit due to SError, all of the following occur:
- exit.exit\_reason is RMI\_EXIT\_SERROR.

- exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- exit.esr.ISS.IDS contains the value of ESR\_EL2.ISS.IDS at the time of the Realm exit.
- exit.esr.ISS.AET contains the value of ESR\_EL2.ISS.AET at the time of the Realm exit.
- exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- exit.esr.ISS.DFSC contains the value of ESR\_EL2.ISS.DFSC at the time of the Realm exit.
- All other exit fields except for exit.givc3\_* , exit\_cnt* and exit.pmu\_ovf\_status are zero.

## See also:

- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU