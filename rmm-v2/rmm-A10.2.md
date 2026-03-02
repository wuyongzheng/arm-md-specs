## A10.2 Planes exception model

## A10.2.1 Plane exception model overview

- DGBWCV A Plane entry is a transition from P0 to Pn, due to execution of RSI\_PLANE\_ENTER.
- ILTWZG P0 provides the index of the target Plane (Pn) as an input to the RSI\_PLANE\_ENTER command.
- DCBVCZ A Plane exit is return to P0 from an execution of RSI\_PLANE\_ENTER which caused a Plane entry.
- DHBXDY A PlaneRun object is a data structure used to pass values between the RMM and P0 on Plane entry and on Plane exit.
- ICPWTD A PlaneRun object is stored in Realm memory.
- IZHWPL Between a Plane entry and a Plane exit, a REC exit and REC entry may occur.

As an example:

1. Running in REC A, P0 executes RSI\_PLANE\_ENTER, passing target Plane index 1.

This causes a Realm exit to the RMM, followed by a Realm entry to P1, within REC A.

2. Running in REC A, P1 accesses an IPA which is not mapped (HIPAS\_VOID, RIPAS\_RAM).

This causes a REC exit to the Host.

3. The Host executes RMI\_REC\_ENTER, passing the address of REC A.

This causes the RMM to return to P1 within REC A.

4. Running in REC A, P1 accesses an IPA which is RIPAS\_EMPTY.

This causes a Plane exit to P0.

- RLDDBH Following a REC exit from P0, on the next entry to the same REC, control returns to P0.
- RNCLJT Following a REC exit from Pn, on the next entry to the same REC, by default control returns to Pn.
- ITXLTM Following a REC exit from Pn, on the next entry to the same REC, the existence of Pending virtual interrupts on the REC can cause control to return to P0, with a Plane exit due to IRQ.
- RGPDRP Following a REC exit from Pn, on the next entry to the same REC, if a Plane exit due to IRQ does not occur and enter.flags.force\_p0 is RMI\_FORCE\_P0 then control returns to P0, with a Plane exit due to Host action.

See also:

- A4.1 Realm exception model overview
- A10.2.3.2 Plane exit due to IRQ
- A10.2.3.3 Plane exit due to Host action
- A10.4 Planes interrupts
- B5.4.13 RSI\_PLANE\_ENTER command
- B5.5.17 RsiPlaneRun type

## A10.2.2 Plane entry

- DMDZZH An RsiPlaneEnter object is a data structure used to pass values from P0 to the RMM on Plane entry.
- IMSTNW An RsiPlaneEnter object is stored in the RsiPlaneRun object which is passed by P0 as an input to the RSI\_PLANE\_ENTER command.
- IDLWGM In this chapter, both plane\_enter and 'the RsiPlaneEnter object' refer to the RsiPlaneEnter object which is provided to the RSI\_PLANE\_ENTER command.
- IDGVWQ On Plane entry, execution state is restored from the RsiPlaneEnter object to the PE.

DRAFT

IKPPTJ On Plane entry, if plane\_enter.pstate.M[3] is set to '1' then the command fails.

IYNKND On Plane entry, SPSR\_EL2 is set to the value of plane\_enter.pstate .

IPQHSC An RsiPlaneEnter object contains attributes which are used to manage Pn virtual interrupts.

DMFJTN

The attributes of an RsiPlaneEnter object are summarized in the following table.

| Name          | Byte offset   | Type               | Description                             |
|---------------|---------------|--------------------|-----------------------------------------|
| flags         | 0x0           | RsiPlaneEnterFlags | Flags                                   |
| pc            | 0x8           | Bits64             | Program counter                         |
| pstate        | 0x10          | Bits64             | PSTATE                                  |
| gprs[31]      | 0x100         | Bits64             | Registers                               |
| gicv3_hcr     | 0x200         | Bits64             | GICv3 Hypervisor Control Register value |
| gicv3_lrs[16] | 0x208         | Bits64             | GICv3 List Register values              |
| elr_el1       | 0x400         | Bits64             | ELR_EL1 value                           |

## A10.2.3 Plane exit

- DBKJDY An RsiPlaneExit object is a data structure used to pass values from the RMM to P0 on Plane exit.

- IGQLBJ An RsiPlaneExit object is stored in the RsiPlaneRun object which is passed by P0 as an input to the RSI\_PLANE\_ENTER command.

- IMMZTG In this chapter, both plane\_exit and 'the RsiPlaneExit object' refer to the RsiPlaneExit object which is provided to the RSI\_PLANE\_ENTER command.

- IMPLMS On Plane exit, execution state is saved from the PE to the RsiPlaneExit object.

- DJYGLX The attributes of an RsiPlaneExit object are summarized in the following table.

| Name          | Byte offset   | Type               | Description                                      |
|---------------|---------------|--------------------|--------------------------------------------------|
| reason        | 0x0           | RsiPlaneExitReason | Exit reason                                      |
| pc            | 0x8           | Bits64             | Program counter                                  |
| pstate        | 0x10          | Bits64             | PSTATE                                           |
| gprs[31]      | 0x100         | Bits64             | Registers                                        |
| esr_el2       | 0x200         | Bits64             | Exception Syndrome Register                      |
| far_el2       | 0x208         | Bits64             | Fault Address Register                           |
| hpfar_el2     | 0x210         | Bits64             | Hypervisor IPA Fault Address register            |
| gicv3_hcr     | 0x300         | Bits64             | GICv3 Hypervisor Control Register value          |
| gicv3_lrs[16] | 0x308         | Bits64             | GICv3 List Register values                       |
| gicv3_misr    | 0x388         | Bits64             | GICv3 Maintenance Interrupt State Register value |
| gicv3_vmcr    | 0x390         | Bits64             | GICv3 Virtual Machine Control Register           |

DRAFT

value

RRNVZY

| Name           | Byte offset   | Type                 | Description                                              |
|----------------|---------------|----------------------|----------------------------------------------------------|
| cntp_ctl       | 0x400         | Bits64               | Counter-timer Physical Timer Control Register value      |
| cntp_cval      | 0x408         | Bits64               | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl       | 0x410         | Bits64               | Counter-timer Virtual Timer Control Register value       |
| cntv_cval      | 0x418         | Bits64               | Counter-timer Virtual Timer CompareValue Register value  |
| sctlr_el1      | 0x500         | Bits64               | SCTLR_EL1 value                                          |
| vbar_el1       | 0x508         | Bits64               | VBAR_EL1 value                                           |
| elr_el1        | 0x510         | Bits64               | ELR_EL1 value                                            |
| pmu_ovf_status | 0x600         | RsiPmuOverflowStatus | PMU overflow status                                      |

DRAFT ILPKMN RsiPlaneExit uses architectural encodings (of ESR, FAR, HPFAR) which are normally observable only to EL2; however, the exit is taken to P0 at EL1. This is justified on the grounds that P0 exists essentially in order to allow part of the job of the hypervisor to be performed inside the Realm. IMPMRX On Plane exit, all RsiPlaneExit fields are zero unless specified otherwise. RBXFJD On Plane exit, plane\_exit.pc contains the value of the Program Counter at the time of the Plane exit. A10.2.3.1 Plane exit due to synchronous exception RGJWRD An exception due to any of the following in Pn causes a Plane exit due to Synchronous Exception: · Trapped WFE instruction execution, if plane\_enter.flags.trap\_wfe == RSI\_TRAP · Trapped WFI instruction execution, if plane\_enter.flags.trap\_wfi == RSI\_TRAP · Data Abort at a Protected IPA

- -Permission fault
- -Access to an IPA which is RIPAS\_EMPTY
- Instruction Abort at a Protected IPA
- -Permission fault
- -Access to an IPA which is RIPAS\_EMPTY
- HVC instruction execution
- RSI\_HOST\_CALL execution, if plane\_enter.flags.trap\_hc == RSI\_TRAP
- Access to a SIMD register or an SVE register, if plane\_enter.flags.trap\_simd == RSI\_TRAP
- Any other SMC instruction execution
- A debug exception which would otherwise be taken to Pn, if plane\_enter.flags.trap\_dbg == RSI\_TRAP

Realm entry to Pn with rec\_enter.flags.inject\_sea == RMI\_INJECT\_SEA results in a Plane exit due to Synchronous Exception.

RLWCQY

On Plane exit due to Synchronous Exception, all of the following are true:

- plane\_exit.exit\_reason is RSI\_EXIT\_SYNC.
- plane\_exit.esr\_el2 contains the value of ESR\_EL2 at the time of the Plane exit.
- If plane\_exit.esr\_el2.EC indicates Data Abort from a lower Exception level and plane\_exit.esr\_el2.ISV == 1 then plane\_exit.far\_el2 contains the value of FAR\_EL2 at the time of the Plane exit.
- If plane\_exit.esr\_el2.EC indicates Data Abort from a lower Exception level or Instruction Abort from a lower Exception level, plane\_exit.hpfar\_el2 contains the value of HPFAR\_EL2 at the time of the Plane exit.
- plane\_exit.pstate contains the value of SPSR\_EL2 at the time of the Plane exit.

## See also:

- A4.3.9 REC exit due to Host call
- A10.2.7 Pn usage of SIMD and SVE

## A10.2.3.2 Plane exit due to IRQ

DDHSNV A Plane exit due to IRQ is a Plane exit due to a Pending interrupt which should be handled by P0.

RQRMVQ

On Plane exit due to IRQ, plane\_exit.exit\_reason

## See also:

- A10.4 Planes interrupts

## A10.2.3.3 Plane exit due to Host action

DSNFXK A Plane exit due to Host action results from a REC entry with enter.flags.force\_p0 being set to RMI\_FORCE\_P0.

RFPRWB

On Plane exit due to Host action, all of the following are true:

- plane\_exit.exit\_reason is RSI\_EXIT\_HOST.
- plane\_exit.esr\_el2 contains the value of ESR\_EL2 at the time of the Plane exit.
- plane\_exit.pstate contains the value of SPSR\_EL2 at the time of the Plane exit.

## See also:

- A4.2 REC entry

## A10.2.4 REC exit from Pn

RHBMWH An exception due to any of the following in Pn cause a REC exit to the Host:

- The following Synchronous Exceptions:
- -Access to an IPA which is RIPAS\_DESTROYED
- -Access to an IPA which is HIPAS\_VOID and whose RIPAS is not RIPAS\_EMPTY
- -Synchronous External Abort
- The following Asynchronous Exceptions:
- -IRQ
- -FIQ
- -SError
- RSI\_HOST\_CALL execution, if plane\_enter.flags.trap\_hc == RSI\_NO\_TRAP . In this case, the result is a REC exit due to Host call.
- ILWSFS Any other exception during execution of Pn causes a Plane exit to P0.

## A10.2.5 Pn execution of HVC and SMC

is RSI\_EXIT\_IRQ.

DRAFT

IPVRDD

IWVLCQ

On Plane exit due to execution by Pn of an HVC instruction, possible actions taken by P0 include the following:

- Emulate the instruction
- Forward the request to the Host using RSI\_HOST\_CALL
- Return SMCCC\_NOT\_SUPPORTED to Pn.

On Plane exit due to execution by Pn of an RSI command, possible actions taken by P0 include the following:

- Emulate the RSI command
- Return SMCCC\_NOT\_SUPPORTED to Pn.

## See also:

- Chapter B5 Realm Services Interface
- B5.4.5 RSI\_HOST\_CALL command

## A10.2.6 Pn system registers

- RLWFQV On Realm creation, all Pn EL0 and EL1 system register values take architecturally-defined reset values.
- RGHFLS On Plane exit, all EL0 and EL1 system register values are saved from the PE to the REC.
- RCLNNC On Plane entry, all EL0 and EL1 system register values are restored from the REC to the PE. Some system register values are then overwritten with values provided by P0 to RSI\_PLANE\_ENTER.
- UVFWCD A REC must have sufficient storage for a copy of all EL0 and EL1 system register values per Plane.
- ICSBWG P0 can access Pn EL0 and EL1 system register values stored in the REC using the RSI\_PLANE\_SYSREG\_READ and RSI\_PLANE\_SYSREG\_WRITE commands.

## See also:

- B5.4.14 RSI\_PLANE\_SYSREG\_READ command
- B5.4.15 RSI\_PLANE\_SYSREG\_WRITE command

## A10.2.7 Pn usage of SIMD and SVE

- RRTZLB On access by Pn to a SIMD register or an SVE register, if plane\_enter.flags.trap\_simd == RSI\_TRAP then a Plane exit due to Synchronous Exception occurs.

DRAFT

- SHGPCK Arm expects P0 to perform context switching of SIMD and SVE state by accessing the architectural SIMD and SVE registers.
- USDXSD Arm expects the implementation to store a single copy of SIMD / SVE state in each REC, when SIMD / SVE is enabled for the parent Realm.