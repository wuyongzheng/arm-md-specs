## D1.1 Exception levels

RFYTFG The architecture defines four Exception levels : EL0, EL1, EL2, and EL3.

RVPSDB

EL3 is the highest Exception level and EL0 the lowest. Therefore, EL3 is higher than EL2, EL2 is higher than EL1, and

EL1 is higher than EL0.

RNXCRB

APEmust implement EL1 and EL0.

RKPZJW

APEwith FEAT\_RME must implement EL3 and EL2.

In a PE without FEAT\_RME, all the following are true:

- Whether EL3 is implemented is IMPLEMENTATION DEFINED.

- Whether EL2 is implemented is IMPLEMENTATION DEFINED.

- The PE is not required to implement a contiguous set of Exception levels.

IWRRKQ

EL2 provides support for the virtualization of EL0 and EL1.

RCCQWK

Unprivileged execution is any execution that occurs at EL0.

RNZZNS

The current Exception level changes only when any of the following occur:

- Taking an exception.

- Returning from an exception.

- Processor reset.

- Exiting from Debug state.

- If in Debug state, executing a DCPSx instruction.

- If in Debug state, executing a DRPS instruction.

RXRQKF The target Exception level is the Exception level to which an exception is taken.

RFFJBB

Each exception type has a target Exception level that is either:

- Implicit in the type of the exception.

- Defined by configuration bits in the System registers.

RTKYYF

An exception cannot be taken to EL0.

RQNTPB

An exception cannot cause entry to a lower Exception level.

## D1.1.1 Execution state

RHTYJH

The architecture defines two Execution states. The AArch32 Execution state uses 32-bit processing. The AArch64 Execution state uses 64-bit processing.

IWKKGD The AArch32 Execution state is compatible with Armv7-A operation.

RNKNVR

An Exception level is described as:

- Using AArch64 when execution in that Exception level is in the AArch64 Execution state.

- Using AArch32 when execution in that Exception level is in the AArch32 Execution state.

RVZTWD The PE can only change Execution state at reset, or when changing Exception level.

RQNVJL

If an Exception level is using AArch32, then all lower Exception levels are using AArch32.

RBDMRT

If an Exception level is using AArch64, then all higher Exception levels are using AArch64.

RMWGKL

Interaction between the AArch64 and AArch32 Execution states is called interprocessing .

IKSMPY

In this chapter, the described behavior assumes the highest implemented Exception level is using AArch64.

## D1.1.2 Security states

RWPBBJ

The architecture defines the following Security states :

- Secure state.

- Non-secure state.

- If FEAT\_RME is implemented, also both of:

- Realm state.

- Root state.

IXKGPG

## Execution in:

- Secure state cannot be observed or modified by an agent associated with any of:

- Non-secure state.

- Realm state.

- Realm state cannot be observed or modified by an agent associated with any of:

- Non-secure state.

- Secure state.

- Root state cannot be observed or modified by an agent associated with any other Security state.

RNRXJT

The architecture defines the following Physical Address (PA) spaces:

- Secure.

- Non-secure.

- If FEAT\_RME is implemented, also the following:

- Realm.

- Root.

- If FEAT\_RME\_GDI is implemented, also both of:

- System Agent.

- Non-secure Protected.

## IRKGZF Memory assigned to the:

- Secure physical address space cannot be read or modified by an agent associated with any of:

- Non-secure state.

- Realm state.

- Realm physical address space cannot be read or modified by an agent associated with any of:

- Non-secure state.

- Secure state.

- Root physical address space cannot be read or modified by an agent associated with any other Security state.

## RZFPTR EL3 is always in:

- Secure state in a PE without FEAT\_RME.

- Root state in a PE with FEAT\_RME.

IHGPBB The Effective value of SCR\_EL3.{NSE, NS} selects the Security state of EL2 and lower.

IYFMYJ

For details on the System Agent and Non-secure Protected PA spaces, see Granular Data Isolation.

RSGMFG

EL2 and lower cannot be in Root state.

RDVTDD EL2 can only be in Secure state if, in addition to the Effective value of SCR\_EL3.{NSE, NS} selecting Secure state, both of the following are true:

- FEAT\_SEL2 is implemented.

- The Effective value of SCR\_EL3.EEL2 is 0b1 .

IZZCQM

The state of SCR\_EL3.NS, and SCR\_EL3.NSE if FEAT\_RME is implemented, can only change in EL3.

IDJJQJ

In a PE with FEAT\_RME, all the following are true:

IZLZWD

IYBGYV

- Root state, Realm state, and Non-secure state must be implemented.
- Whether Secure state is implemented is IMPLEMENTATION DEFINED.
- If Secure state is implemented, the PE must also implement FEAT\_SEL2.

In a PE with FEAT\_RME, software can discover whether Secure state is implemented by discovering whether FEAT\_SEL2 is implemented from ID\_AA64PFR0\_EL1.SEL2.

Figure D1-1 illustrates the Security states in a PE with FEAT\_RME.

Figure D1-1 Security states

<!-- image -->

## Where:

- RMMisRealm Management Monitor.
- SPMis Secure Partition Manager.
- VMis Virtual Machine.

## D1.1.3 Effect of not implementing an Exception level

RKFGRW

An exception cannot be taken to an unimplemented Exception level.

RHRDVX

Any configurable instruction control that defines an exception to an unimplemented Exception level does not cause that exception to the unimplemented Exception level. The Effective value of the configurable exception control is the value that does not cause an exception to that Exception level.

RWPVKJ

System calls made to an unimplemented Exception level from a lower Exception level are UNDEFINED.

RWPXJS

The translation regime associated with an unimplemented Exception level is not implemented.

RWKQBG

Any exception return that targets an unimplemented Exception level is an illegal return.

RGTCCW

Every accessible register associated with an unimplemented Exception level is RES0 unless the register is associated with the Exception level only to provide the ability to transfer execution to a lower Exception level.

## D1.1.3.1 Behavior when EL3 is not implemented

RBSNQL

If EL3 is not implemented, SCR\_EL3.NS has a fixed Effective value that is IMPLEMENTATION DEFINED.

IBWVTM

An implementation can provide a configuration input that determines the Effective value of SCR\_EL3.NS at reset.

RLBZCK

If EL3 is not implemented, and the Effective value of SCR\_EL3.NS is 0, all of the following are true:

RZTWJS

- The Effective value of MDCR\_EL3.EPMAD is 1.
- The Effective value of MDCR\_EL3.EDAD is 1.
- The Effective value of MDCR\_EL3.SPME is 1.
- The Effective value of MDCR\_EL3.NSPB is 0b01 .
- The Effective value of MDCR\_EL3.SPD32 is 0b11 .
- The Effective value of MDCR\_EL3.STE is 1.

If EL3 is not implemented, the Effective value of MDCR\_EL3.STE is the inverse of the Effective value of SCR\_EL3.NS.

RRDYPY If all of the following are true, the Effective value of SCR\_EL3.EEL2 is 1:

- EL3 is not implemented.
- EL2 is implemented.
- The Effective value of SCR\_EL3.NS is 0.

## D1.1.3.2 Behavior when EL2 is not implemented

If EL2 is not implemented, all of the following are true:

- Virtual interrupts are disabled.
- The Effective value of CNTHCTL\_EL2[1:0] is 0b11 .
- The Effective value of HCR\_EL2.E2H is 0.
- The Effective value of HCR\_EL2.TGE is 0.
- The Effective value of MDCR\_EL2.HPMN is the value of PMCR\_EL0.N.

## D1.1.3.3 Behavior when EL2 is not implemented and EL3 is implemented

RRJFFP If EL2 is not implemented and EL3 is implemented, all of the following are true:

- Except for any of the following registers, every accessible register associated with EL2 is RES0:
- -If EL1 can use AArch32 then the following registers are not RES0:
- -DACR32\_EL2.
- -DBGVCR32\_EL2.
- -FPEXC32\_EL2.
- -IFSR32\_EL2.
- -For VPIDR\_EL2:
- -Reads return the value of MIDR\_EL1.
- -Writes to VPIDR\_EL2 are ignored.
- -For VMPIDR\_EL2:
- -Reads return the value of MPIDR\_EL1.
- -Writes to VMPIDR\_EL2 are ignored.
- The Effective value of HCR\_EL2.RW is the value of SCR\_EL3.RW.
- SCR\_EL3.HCE is RES0.
- The following Address translation and TLB invalidation instructions are UNDEFINED:
- -AT S1E2R.
- -AT S1E2W.
- -TLBI VAE2, TLBI VAE2NXS.
- -TLBI VALE2, TLBI VALE2NXS.
- -TLBI VAE2IS, TLBI VAE2ISNXS.
- -TLBI VALE2IS, TLBI VALE2ISNXS.
- -TLBI VAE2OS, TLBI VAE2OSNXS.
- -TLBI VALE2OS, TLBI VALE2OSNXS.
- -TLBI ALLE2, TLBI ALLE2NXS.
- -TLBI ALLE2IS, TLBI ALLE2ISNXS.
- -TLBI ALLE2OS, TLBI ALLE2OSNXS.
- -TLBI RVAE2, TLBI RVAE2NXS.
- -TLBI RVALE2, TLBI RVALE2NXS.

RPQDWN

IWCCCB

- -TLBI RVAE2IS, TLBI RVAE2ISNXS.
- -TLBI RVALE2IS, TLBI RVALE2ISNXS.
- -TLBI RVAE2OS, TLBI RVAE2OSNXS.
- -TLBI RVALE2OS, TLBI RVALE2OSNXS.

## D1.1.3.4 Typical Exception level usage model

The architecture does not specify what software uses which Exception level. Such choices are outside the scope of the architecture. However, the following is a common usage model for the Exception levels:

| Exception level   | Usage                                                                          |
|-------------------|--------------------------------------------------------------------------------|
| EL0               | Applications.                                                                  |
| EL1               | OS kernel and associated functions that are typically described as privileged. |
| EL2               | Hypervisor.                                                                    |
| EL3               | Monitor.                                                                       |