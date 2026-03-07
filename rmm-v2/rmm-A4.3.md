## A4.3 REC exit

This section describes REC exit.

## See also:

- [A4.2 REC entry](rmm-A4.2.md)
- [B4.5.51 RMI\_REC\_ENTER command](rmm-B4.5.51.md)

## A4.3.1 RmiRecExit object

- An RmiRecExit object is a data structure used to pass values from the RMM to the Host on REC exit.
- An RmiRecExit object is stored in the RecRun object which is passed by the Host as an input to the RMI\_REC\_ENTER command.
- On REC exit, execution state is saved from the PE to the REC object and to the RmiRecExit object.
- An RmiRecExit object contains attributes which are used to manage Realm virtual interrupts and Realm timers.


The attributes of an RmiRecExit object are summarized in the following table.

| Name        | Byte offset   | Type                   | Description                                              |
|-------------|---------------|------------------------|----------------------------------------------------------|
| exit_reason | 0x0            RmiRecExitReason | Exit reason                                              |
| esr         | 0x100         | Bits64                 | Exception Syndrome Register                              |
| far         | 0x108         | Bits64                 | Fault Address Register                                   |
| hpfar       | 0x110         | Bits64                 | Hypervisor IPA Fault Address register                    |
| rtt_tree    | 0x118         | UInt64                 | Index of RTT tree active at time of the exit             |
| gprs[31]    | 0x200         | Bits64                 | Registers                                                |
| cntp_ctl    | 0x400         | Bits64                 | Counter-timer Physical Timer Control Register value      |
| cntp_cval   | 0x408         | Bits64                 | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl    | 0x410         | Bits64                 | Counter-timer Virtual Timer Control Register value       |
| cntv_cval   | 0x418         | Bits64                 | Counter-timer Virtual Timer CompareValue Register value  |
| ripas_base  | 0x500         | Bits64                 | Base IPA of target region for pending RIPAS change       |
| ripas_top   | 0x508         | Bits64                 | Top IPA of target region for pending RIPAS change        |
| ripas_value | 0x510         | RmiRipas               | RIPAS value of pending RIPAS change                      |
| s2ap_base   | 0x520         | Bits64                 | Base IPA of target region for pending S2AP change        |
| s2ap_top    | 0x528         | Bits64                 | Top IPA of target region for pending S2AP change         |
| vdev_id_1   | 0x530         | Bits64                 | Virtual device ID 1                                      |
| vdev_id_2   | 0x538         | Bits64                 | Virtual device ID 2                                      |



| Name           | Byte offset   | Type                 | Description                                           |
|----------------|---------------|----------------------|-------------------------------------------------------|
| dev_mem_base   | 0x540         | Bits64               | Base IPA of target region for VDEV mapping validation |
| dev_mem_top    | 0x548         | Bits64               | Top IPA of target region for VDEV mapping validation  |
| dev_mem_pa     | 0x550         | Address              | Base PA of device memory region                       |
| imm            | 0x600         | Bits16               | Host call immediate value                             |
| plane          | 0x608         | UInt64               | Plane index                                           |
| pmu_ovf_status | 0x700         | RmiPmuOverflowStatus | PMU overflow status                                   |
| vsmmu          | 0x710         | Address              | Virtual SMMUbase IPA                                  |

In this chapter, both rec\_exit and 'the RmiRecExit object' refer to the RmiRecExit object which is provided to the RMI\_REC\_ENTER command.

On REC exit, all rec\_exit fields are zero unless specified otherwise.

See also:

- [A2.4 Realm Execution Context](rmm-A2.4.md)
- [A4.2.1 RmiRecEnter object](rmm-A4.2.md#a421-rmirecenter-object)
- [A4.5 Host call](rmm-A4.4.md#a45-host-call)
- [Chapter A6 Realm interrupts and timers](rmm-A6.md)
- [Chapter A8 Realm debug and performance monitoring](rmm-A8.md)
- [B4.6.66 RmiRecExit type](rmm-B4.6.md#b4666-rmirecexit-type)

## A4.3.2 Realm exit reason

On return from the RMI\_REC\_ENTER command, the reason for the REC exit is indicated by rec\_exit.exit\_reason and rec\_exit.esr .

## See also:

- [B4.6.67 RmiRecExitReason type](rmm-B4.6.md#b4667-rmirecexitreason-type)

## A4.3.3 General purpose registers saved on REC exit

On REC exit due to PSCI, all of the following are true:

- rec\_exit.gprs[0] contains the PSCI FID.
- rec\_exit.gprs[1..3] contain the corresponding PSCI arguments. If the PSCI command has fewer than 3 arguments, the remaining values contain zero.
- GPR values X7 to X30 are saved from the PE to the REC object.

On REC exit for any reason which is not REC exit due to PSCI, GPR values X0 to X30 are saved from the PE to the REC.


On REC exit for any reason except for the following, rec\_exit.gprs is zero.

- REC exit due to Host call
- REC exit due to PSCI
- REC exit due to Emulatable Data Abort, and the Realm memory access was a write



On REC exit, if RMM access to rec\_exit causes a GPF then the RMI\_REC\_ENTER command fails with RMI\_ERROR\_INPUT.

See also:

- [A4.2.2 General purpose registers restored on REC entry](rmm-A4.2.md#a422-general-purpose-registers-restored-on-rec-entry)
- [A4.3.7 REC exit due to PSCI](rmm-A4.3.md#a437-rec-exit-due-to-psci)
- [A4.3.9 REC exit due to Host call](rmm-A4.3.md#a439-rec-exit-due-to-host-call)

## A4.3.4 REC exit due to synchronous exception

A synchronous exception taken to R-EL2 can cause a REC exit.

- The following table summarises the behavior of synchronous exceptions taken to R-EL2.

| Exception class                                                   | Behavior                                                                                                                                                                                                            |
|-------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Trapped WFI or WFE instruction execution                          | If taken from the Primary Plane, REC exit due to WFI or WFE Otherwise, Plane exit due to synchronous exception.                                                                                                     |
| HVC instruction execution in AArch64 state                        | If taken from the Primary Plane, Unknown exception taken to Realm. Otherwise, Plane exit due to synchronous exception.                                                                                              |
| SMC instruction execution in AArch64 state                         If taken from the Primary Plane, one of: • SMCCC_VERSION emuulated byRMM • REC exit due to PSCI • RSI command handled by RMM, followed by return to Realm Otherwise, Plane exit due to synchronous exception. |
| Trapped MSR, MRS or System instruction execution in AArch64 state | If taken from the Primary Plane, one of: • REC exit due to System register access • Emulated by RMM, followed by return to Realm Otherwise, Plane exit due to synchronous exception.                                |
| Instruction Abort from a lower Exception level                    | REC exit due to Instruction Abort                                                                                                                                                                                   |
| Data Abort from a lower Exception level                           | REC exit due to Data Abort                                                                                                                                                                                          |


Realm execution of an SMC which is not part of one of the following ABIs results in a return value of SMCCC\_NOT\_SUPPORTED:

- SMCCC\_VERSION
- PSCI
- RSI

See also:

- [A4.5 Host call](rmm-A4.4.md#a45-host-call)
- [A10.2.3 Plane exit](rmm-A10.2.md#a1023-plane-exit)
- Chapter B5 Realm Services Interface
- Chapter B6 Power State Control Interface

## A4.3.4.1 REC exit due to WFI or WFE

A REC exit due to WFI or WFE


is a REC exit due to WFI, WFIT, WFE or WFET instruction execution in a Realm.

On WFI or WFIT instruction execution in a Realm, a REC exit due to WFI or WFE is caused if rec\_enter.trap\_wfi is RMI\_TRAP.


On WFE or WFET instruction execution in a Realm, a REC exit due to WFI or WFE is caused if rec\_enter.trap\_wfe is RMI\_TRAP.

On REC exit due to WFI or WFE, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_SYNC.
- rec\_exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- rec\_exit.esr.ISS.TI contains the value of ESR\_EL2.ISS.TI at the time of the Realm exit.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

On REC exit due to WFI or WFE, if the exit was caused by WFET or WFIT instruction execution then rec\_exit.gprs[0] contains the timeout value.

## See also:

- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A6.2 Realm timers](rmm-A6.2.md)
- [A8.1 Realm PMU](rmm-A8.md#a81-realm-pmu)

## A4.3.4.2 REC exit due to Instruction Abort

A REC exit due to Instruction Abort is a REC exit due to a Realm instruction fetch from a Protected IPA for which any of the following is true:

- HIPAS\_VOID and RIPAS\_RAM
- RIPAS\_DESTROYED
- The access is from a Plane which uses an Auxiliary RTT tree, and the IPA is not mapped in that tree

On REC exit due to Instruction Abort, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_SYNC.
- rec\_exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- rec\_exit.esr.ISS.SET contains the value of ESR\_EL2.ISS.SET at the time of the Realm exit.
- rec\_exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- rec\_exit.esr.ISS.IFSC contains the value of ESR\_EL2.ISS.IFSC at the time of the Realm exit.
- rec\_exit.hpfar contains the value of HPFAR\_EL2 at the time of the Realm exit.
- rec\_exit.rtt\_tree contains the index of the RTT tree within which the contents of an RTTE cause the Realm to exit.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.


Low bits of HPFAR\_EL2.FIPA are set to zero in order to align the address to the RMI Granule size. rec\_exit.hpfar therefore only reveals the Realm's access patterns at the granularity of the RMI Granule size.

## See also:

- [A5.2.2 Realm IPA state](rmm-A5.1.md#a522-realm-ipa-state)
- [A5.2.3 Realm access to a Protected IPA](rmm-A5.1.md#a523-realm-access-to-a-protected-ipa)
- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A6.2 Realm timers](rmm-A6.2.md)
- [A8.1 Realm PMU](rmm-A8.md#a81-realm-pmu)
- [A10.3.1 Auxiliary RTT](rmm-A10.3.md#a1031-auxiliary-rtt)

## A4.3.4.3 REC exit due to Data Abort

A REC exit due to Emulatable Data Abort is a REC exit due to a Realm data access to one of the following:

- an Unprotected IPA which is HIPAS\_UNMAPPED\_NS, where the access caused ESR\_EL2.ISS.ISV to be set to '1'
- an Unprotected IPA which is HIPAS\_MAPPED\_NS, where the access caused a stage 2 permission fault and caused ESR\_EL2.ISS.ISV to be set to '1'
- the access is from a Plane which uses an Auxiliary RTT tree, and the IPA is not mapped in that tree




<!-- image -->


A REC exit due to Non-emulatable Data Abort is a REC exit due to a Realm data access to one of the following:

- an Unprotected IPA which is HIPAS\_UNMAPPED\_NS, where the access caused ESR\_EL2.ISS.ISV to be set to '0'
- an Unprotected IPA which is HIPAS\_MAPPED\_NS, where the access caused a stage 2 permission fault and caused ESR\_EL2.ISS.ISV to be set to '0'
- a Protected IPA which is HIPAS\_VOID and RIPAS\_RAM
- a Protected IPA which is RIPAS\_DESTROYED.

## On REC exit due to Data Abort, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_SYNC.
- rec\_exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- rec\_exit.esr.ISS.SET contains the value of ESR\_EL2.ISS.SET at the time of the Realm exit.
- rec\_exit.esr.ISS.FnV contains the value of ESR\_EL2.ISS.FnV at the time of the Realm exit.
- rec\_exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- rec\_exit.esr.ISS.DFSC contains the value of ESR\_EL2.ISS.DFSC at the time of the Realm exit.
- rec\_exit.hpfar contains the value of HPFAR\_EL2 at the time of the Realm exit.
- rec\_exit.rtt\_tree contains the index of the RTT tree within which the contents of an RTTE cause the Realm to exit.

On REC exit due to Emulatable Data Abort, all of the following are true:

- rec.emulatable\_abort is EMULATABLE\_ABORT.
- rec\_exit.esr.ISS.ISV contains the value of ESR\_EL2.ISS.ISV at the time of the Realm exit.
- rec\_exit.esr.ISS.SAS contains the value of ESR\_EL2.ISS.SAS at the time of the Realm exit.
- rec\_exit.esr.ISS.SF contains the value of ESR\_EL2.ISS.SF at the time of the Realm exit.
- rec\_exit.esr.ISS.WnR contains the value of ESR\_EL2.ISS.WnR at the time of the Realm exit.
- rec\_exit.far contains the value of FAR\_EL2 at the time of the Realm exit, with bits more significant than the size of a Granule masked to zero.

On REC exit due to Non-emulatable Data Abort at an Unprotected IPA, all of the following are true:

- rec\_exit.esr.IL contains the value of ESR\_EL2.IL at the time of the Realm exit.

On REC exit due to Data Abort, all other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.


- On REC exit due to Emulatable Data Abort, ESR\_EL2.ISS.SSE is not propagated to the Host. This is because this field is used to emulate sign extension on loads, which must be performed by the RMM so that the Realm can rely on architecturally correct behavior of the virtual execution environment.
- On REC exit due to Emulatable Data Abort, the Host can calculate the faulting IPA from the rec\_exit.hpfar and rec\_exit.far values.
- On REC exit due to Emulatable Data Abort, if the Realm memory access was a write, rec\_exit.gprs[0] contains the value of the register indicated by ESR\_EL2.ISS.SRT

at the time of the Realm exit.

- On REC exit not due to Emulatable Data Abort, rec.emulatable\_abort is NOT\_EMULATABLE\_ABORT. See also:
- A4.2.3 REC entry following REC exit due to Data Abort
- A4.4 Emulated Data Aborts
- A5.2.1 Realm IPA space
- A5.2.3 Realm access to a Protected IPA
- A5.2.7 Realm access to an Unprotected IPA
- A6.1 Realm interrupts
- A6.2 Realm timers
- A8.1 Realm PMU
- A10.3.1 Auxiliary RTT

## A4.3.4.4 REC exit due to System register access


A REC exit due to System register access is a REC exit due to a system register access.


On REC exit due to System register access, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_SYNC.
- rec\_exit.esr contains the value of ESR\_EL2 at the time of the Realm exit.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

## See also:

- [A6.1 Realm interrupts](rmm-A6.1.md)

## A4.3.5 REC exit due to IRQ

- A REC exit due to IRQ is a REC exit due to an IRQ exception which should be handled by the Host.

- On REC exit due to IRQ, rec\_exit.exit\_reason

is RMI\_EXIT\_IRQ.


- On REC exit due to IRQ, rec\_exit.esr is zero.

See also:

- [Chapter A6 Realm interrupts and timers](rmm-A6.md)

## A4.3.6 REC exit due to FIQ

- A REC exit due to FIQ is a REC exit due to an FIQ exception which should be handled by the Host.

- On REC exit due to FIQ, rec\_exit.exit\_reason is RMI\_EXIT\_FIQ.

- On REC exit due to FIQ, rec\_exit.esr is zero.

See also:

- [Chapter A6 Realm interrupts and timers](rmm-A6.md)

## A4.3.7 REC exit due to PSCI

- A PSCI function executed by a Realm is either:

- handled by the RMM, returning to the Realm, or

- forwarded by the RMM to the Host via a REC exit due to PSCI .

A REC exit due to PSCI is a REC exit due to Realm PSCI function execution by SMC instruction which was forwarded by the RMM to the Host.

- The following table summarises the behavior of PSCI function execution by a Realm.

PSCI functions not listed in this table are not supported. Calling a non-supported PSCI function results in a return value of PSCI\_NOT\_SUPPORTED.


| PSCI function    | Can result in REC exit due to PSCI   | Requires Host to call RMI_PSCI_COMPLETE   |
|------------------|--------------------------------------|-------------------------------------------|
| PSCI_VERSION     | No                                   | -                                         |
| PSCI_FEATURES    | No                                   | -                                         |
| PSCI_CPU_SUSPEND | Yes                                  | No                                        |
| PSCI_CPU_OFF     | Yes                                  | No                                        |
| PSCI_CPU_ON      | Yes                                  | Yes                                       |

| PSCI function      | Can result in REC exit due to PSCI   | Requires Host to call RMI_PSCI_COMPLETE   |
|--------------------|--------------------------------------|-------------------------------------------|
| PSCI_AFFINITY_INFO | Yes                                  | Yes                                       |
| PSCI_SYSTEM_OFF    | Yes                                  | No                                        |
| PSCI_SYSTEM_RESET  | Yes                                  | No                                        |


On REC exit due to PSCI, rec\_exit.exit\_reason is RMI\_EXIT\_PSCI.


On REC exit due to PSCI, rec\_exit.gprs contains sanitised parameters from the PSCI call.


On REC exit due to PSCI, if the command arguments include an MPIDR value, rec.pending is set to REC\_PENDING\_PSCI. Otherwise, rec.pending is set to REC\_PENDING\_NONE.


Following REC exit due to PSCI, if rec.pending by calling the RMI\_PSCI\_COMPLETE command, prior to re-entering the REC.

is REC\_PENDING\_PSCI, the Host must complete the request

In the call to RMI\_PSCI\_COMPLETE, the Host provides the target REC, which corresponds to the MPIDR value provided by the Realm. This is necessary because the RMM does not maintain a mapping from MPIDR values to REC addresses. The RMM validates that the REC provided by the Host matches the MPIDR value.

- In the call to RMI\_PSCI\_COMPLETE, the Host provides a PSCI status value, which the RMM handles as follows: · If the Host provides PSCI\_SUCCESS, the RMM performs the PSCI operation requested by the Realm. The result of the PSCI operation is recorded in the REC and returned to the Realm on the next entry to the calling REC. · If the Host provides a status value other than PSCI\_SUCCESS, the RMM validates that the status code is permitted for the PSCI operation requested by the Realm. If the status code is permitted, it is recorded in the REC and returned to the Realm on the next entry to the calling REC. See also: · A4.3.3 General purpose registers saved on REC exit · B3.87 PsciReturnCodePermitted function · B4.5.38 RMI\_PSCI\_COMPLETE command
- Chapter B6 Power State Control Interface
- D1.4 PSCI flows

## A4.3.8 REC exit due to RIPAS change pending

A REC exit due to RIPAS change pending is a REC exit due to the Realm issuing a RIPAS change request .

On REC exit due to RIPAS change pending, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_RIPAS\_CHANGE.
- rec\_exit.ripas\_base is the base IPA of the region on which a RIPAS change is pending.
- rec\_exit.ripas\_top is the top IPA of the region on which a RIPAS change is pending.
- rec\_exit.ripas\_value is the requested RIPAS value.
- rec.ripas\_addr is the base IPA of the region on which a RIPAS change is pending.
- rec.ripas\_top is the top IPA of the region on which a RIPAS change is pending.
- rec.ripas\_value is the requested RIPAS value.

On REC exit due to RIPAS change pending:

- rec\_exit holds the base IPA and the size of the region on which a RIPAS change is pending. These values inform the Host of the bounds of the RIPAS change request.
- rec holds the next IPA to be processed in a RIPAS change, and the top of the requested RIPAS change region. These values are used by the RMM to enforce that the RMI\_RTT\_SET\_RIPAS command can only

apply RIPAS change within the bounds of the RIPAS change request, and to report the progress of the RIPAS change to the Realm on the next REC entry.

## See also:

- [A2.4.2 REC attributes](rmm-A2.4.md#a242-rec-attributes)
- [A5.4 RIPAS change](rmm-A5.4.md)

## A4.3.9 REC exit due to Host call

A REC exit due to Host call is a REC exit due to RSI\_HOST\_CALL execution in a Realm.

On REC exit due to Host call, all of the following are true:

- rec.pending is REC\_PENDING\_HOST\_CALL.
- rec\_exit.exit\_reason is RMI\_EXIT\_HOST\_CALL.
- rec\_exit.imm contains the immediate value passed to the RSI\_HOST\_CALL command.
- rec\_exit.plane contains the index of the Plane which executed the RSI\_HOST\_CALL command.
- rec\_exit.gprs[0..30] contain the register values passed to the RSI\_HOST\_CALL command.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

## See also:

- [A4.5 Host call](rmm-A4.4.md#a45-host-call)
- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A6.2 Realm timers](rmm-A6.2.md)
- [A8.1 Realm PMU](rmm-A8.md#a81-realm-pmu)
- [B5.4.5 RSI\_HOST\_CALL command](rmm-B5.4.5.md)

## A4.3.10 REC exit due to SError


A REC exit due to SError is a REC exit due to an SError interrupt during Realm execution.


On REC exit due to SError, all of the following occur:

- rec\_exit.exit\_reason is RMI\_EXIT\_SERROR.
- rec\_exit.esr.EC contains the value of ESR\_EL2.EC at the time of the Realm exit.
- rec\_exit.esr.ISS.IDS contains the value of ESR\_EL2.ISS.IDS at the time of the Realm exit.


- rec\_exit.esr.ISS.AET contains the value of ESR\_EL2.ISS.AET at the time of the Realm exit.
- rec\_exit.esr.ISS.EA contains the value of ESR\_EL2.ISS.EA at the time of the Realm exit.
- rec\_exit.esr.ISS.DFSC contains the value of ESR\_EL2.ISS.DFSC at the time of the Realm exit.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

## See also:

- [A6.1 Realm interrupts](rmm-A6.1.md)
- [A6.2 Realm timers](rmm-A6.2.md)
- [A8.1 Realm PMU](rmm-A8.md#a81-realm-pmu)

## A4.3.11 REC exit due to S2AP change pending

A REC exit due to S2AP change pending is a REC exit due to the Realm issuing an S2AP change request .


On REC exit due to S2AP change pending, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_S2AP\_CHANGE.
- rec\_exit.s2ap\_base is the base IPA of the region on which an S2AP change is pending.
- rec\_exit.s2ap\_top is the top IPA of the region on which an S2AP change is pending.
- rec.s2ap\_addr is the base IPA of the region on which an S2AP change is pending.
- rec.s2ap\_top is the top IPA of the region on which an S2AP change is pending.
- rec.s2ap\_value is the requested S2AP value.



- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

On REC exit due to RIPAS change pending:

- rec\_exit holds the base IPA and the size of the region on which an S2AP change is pending. These values inform the Host of the bounds of the RIPAS change request.
- rec holds the next IPA to be processed in an S2AP change, and the top of the requested S2AP change region. These values are used by the RMM to enforce that the RMI\_RTT\_SET\_S2AP command can only apply S2AP change within the bounds of the S2AP change request, and to report the progress of the S2AP change to the Realm on the next REC entry.
- On REC exit not due to S2AP change pending, all of the following are true:
- rec.s2ap\_addr is 0
- rec.s2ap\_top is 0

## See also:

- [A2.4.2 REC attributes](rmm-A2.4.md#a242-rec-attributes)
- [A10.3.2.3 Stage 2 Access Permissions change within a multi-Plane Realm](rmm-A10.3.md#a10323-stage-2-access-permissions-change-within-a-multi-plane-realm)

## A4.3.12 REC exit due to VDEV request

- A REC exit due to VDEV request is a REC exit due to the RMM requiring the Host to provide the VDEV object which matches a specified virtual device ID.
- On REC exit due to VDEV request, rec\_exit.exit\_reason is RMI\_EXIT\_VDEV\_REQUEST.
- On REC exit due to VDEV request, rec\_exit.vdev\_id\_1 contains the requested virtual device ID.
- On REC exit due to VDEV request, rec.vdev\_pending is set to REC\_PENDING\_VDEV\_REQUEST.
- R0005 On REC exit due to VDEV request rec.vdev\_comm\_pending is set to RMM\_TRUE if the exit was triggered by execution of any of the following commands:
- RSI\_VDEV\_P2P\_BIND

Otherwise rec.vdev\_comm\_pending is set to RMM\_FALSE .

Following REC exit due to VDEV request, the Host must complete the request by calling the RMI\_VDEV\_COMPLETE


command, prior to re-entering the REC.

In the call to RMI\_VDEV\_COMPLETE, the Host provides the target VDEV, which corresponds to the virtual device ID value provided by the Realm. This is necessary because the RMM does not maintain a mapping from virtual device IDs to VDEV objects. The RMM validates that the VDEV provided by the Host matches the virtual device ID value.

## See also:

- [A9.4.4 Mapping from virtual device ID to VDEV object](rmm-A9.4.md#a944-mapping-from-virtual-device-id-to-vdev-object)
- [B4.5.81 RMI\_VDEV\_COMPLETE command](rmm-B4.5.81.md)

## A4.3.13 REC exit due to VDEV mapping validation

- A REC exit due to VDEV mapping validation is a REC exit due to the Realm issuing a VDEV mapping validation request .

On REC exit due to VDEV mapping validation, all of the following are true:

- rec\_exit.exit\_reason is RMI\_EXIT\_VDEV\_VALIDATE\_MAPPING.
- rec\_exit.vdev\_id\_1 is the virtual device identifier.
- rec\_exit.dev\_mem\_base is the base IPA of the region on which VDEV mapping validation is pending.
- rec\_exit.dev\_mem\_top is the top IPA of the region on which VDEV mapping validation is pending.


- rec.dev\_mem\_addr is the base IPA of the region on which VDEV mapping validation is pending.
- rec.dev\_mem\_top is the top IPA of the region on which VDEV mapping validation is pending.
- rec\_exit.dev\_mem\_pa is the base PA of the device memory region.
- rec.dev\_mem\_pa is the base PA of the device memory region.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

## On REC exit due to VDEV mapping validation:

- rec\_exit holds the base IPA and the size of the region on which VDEV mapping validation is pending. These values inform the Host of the bounds of the VDEV mapping validation request.
- rec\_exit holds the base PA of the device memory region. This value enables the Host to create device memory mappings (by calling RMI\_RTT\_DEV\_MAP) on demand.
- rec holds the next IPA to be processed in a VDEV mapping validation, and the top of the requested IPA region. These values are used by the RMM to enforce that the RMI\_RTT\_DEV\_VALIDATE command can only apply VDEV mapping validation within the bounds of the VDEV mapping validation request, and to report the progress of the VDEV mapping validation to the Realm on the next REC entry.

## See also:

- [A2.4.2 REC attributes](rmm-A2.4.md#a242-rec-attributes)
- [A5.5 VDEV mapping validation](rmm-A5.5.md)
- [A9.6.2 Realm validation of device memory mappings](rmm-A9.6.md#a962-realm-validation-of-device-memory-mappings)
- [B4.5.71 RMI\_RTT\_DEV\_VALIDATE command](rmm-B4.5.71.md)

## A4.3.14 REC exit due to VDEV P2P binding

- D0006 A REC exit due to VDEV P2P binding is a REC exit due to the Realm issuing a VDEV P2P binding request .
- R0007 On REC exit due to VDEV P2P binding, all of the following are true:
- rec\_exit.exit\_reason is RMI\_EXIT\_VDEV\_P2P\_BINDING.
- rec\_exit.vdev\_id\_1 is the virtual device identifier of the first VDEV .
- rec\_exit.vdev\_id\_2 is the virtual device identifier of the second VDEV.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

I0008 Following REC exit due to VDEV P2P binding, the Host is expected to complete the request by calling the RMI\_VDEV\_P2P\_BIND command.


In the call to RMI\_VDEV\_P2P\_BIND, the Host provides the target VDEVs, which correspond to the virtual device ID values provided by the Realm. This is necessary because the RMM does not maintain a mapping from virtual device IDs to VDEV objects. The RMM validates that the VDEVs provided by the Host match the virtual device ID values.

The Realm can validate that the binding request was undertaken by executing RSI\_VDEV\_GET\_INFO.

## See also:

- [A2.4.2 REC attributes](rmm-A2.4.md#a242-rec-attributes)
- [A9.10 Peer-to-peer device communication](rmm-A9.10.md)
- [B4.5.88 RMI\_VDEV\_P2P\_BIND command](rmm-B4.5.88.md)
- [B5.4.19 RSI\_VDEV\_GET\_INFO command](rmm-B5.4.19.md)

## A4.3.15 REC exit due to VSMMU command

- A REC exit due to VSMMU command is a REC exit due to the Realm enqueing a VSMMU command which requires action to be taken by the Host.
- On REC exit due to VSMMU command, all of the following are true:
- rec\_exit.exit\_reason is RMI\_EXIT\_VSMMU\_COMMAND.


- rec\_exit.vsmmu is the Virtual SMMU base IPA for which the command was enqueued.
- All other rec\_exit fields except for rec\_exit.cnt* and rec\_exit.pmu\_ovf\_status are zero.

Following REC exit due to VSMMU command, the Host is expected to call the RMI\_VSMMU\_CMD\_GET command. The return values of that command include flags which inform the Host which further action is required. See also:

- A2.4.2 REC attributes
- A9.8.5 VSMMU commands
- B4.5.94 RMI\_VSMMU\_CMD\_GET command

<!-- image -->