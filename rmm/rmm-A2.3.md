## A2.3 Realm Execution Context

This section describes the concept of a Realm Execution Context (REC).

## A2.3.1 Overview

- DLRFCP A Realm Execution Context (REC) is an R-EL0&amp;1 execution context which is associated with a Realm VPE.

A REC object is an RMM data structure which is used to store the register state of a REC.

See also:

- A2.1.2 Realm execution environment
- Chapter A4 Realm exception model

## A2.3.2 REC attributes

This section describes the attributes of a REC.

- DZLGLT A REC attribute is a property of a REC whose value can be observed or modified either by the Host or by the Realm which owns the REC.
- ICSGGT Examples of ways in which a REC attribute may be observable include the outcome of an RMM command, and the PE state following Realm entry.
- DLQSFT The attributes of a REC are summarized in the following table.

| Name             | Type                    | Description                                                                    |
|------------------|-------------------------|--------------------------------------------------------------------------------|
| attest_state     | RmmRecAttestState       | Attestation token generation state                                             |
| attest_challenge | Bits512                 | Challenge for under-construction attestation token                             |
| aux              | Address[16]             | Addresses of auxiliary Granules                                                |
| emulatable_abort | RmmRecEmulatableAbort   | Whether the most recent exit from this REC was due to an Emulatable Data Abort |
| flags            | RmmRecFlags             | Flags which control REC behavior                                               |
| gprs             | Bits64[32]              | General-purpose register values                                                |
| mpidr            | Bits64                  | MPIDR value                                                                    |
| owner            | Address                 | PA of RD of Realm which owns this REC                                          |
| pc               | Bits64                  | Program counter value                                                          |
| psci_pending     | RmmPsciPending          | Whether a PSCI request is pending                                              |
| state            | RmmRecState             | Lifecycle state                                                                |
| sysregs          | RmmSystemRegisters      | EL1 and EL0 system register values                                             |
| ripas_addr       | Address                 | Next address to be processed in RIPAS change                                   |
| ripas_top        | Address                 | Top address of pending RIPAS change                                            |
| ripas_value      | RmmRipas                | RIPAS value of pending RIPAS change                                            |
| ripas_destroyed  | RmmRipasChangeDestroyed | Whether a RIPAS change from DESTROYED should be permitted                      |
| ripas_response   | RmmRecResponse          | Host response to RIPAS change request                                          |

host\_call\_pending

RmmHostCallPending

IPVMTY The aux attribute of a REC is a list of auxiliary Granules .

IRWFZF The number of auxiliary Granules required for a REC is returned by the RMI\_REC\_AUX\_COUNT command.

XLRWHB Depending on the configuration of the CCA platform and of the Realm, the amount of storage space required for a REC may exceed a single Granule.

ITGLBK The number of auxiliary Granules required for a REC can vary between Realms on a CCA platform.

RMMBNR The number of auxiliary Granules required for a REC is a constant for the lifetime of a given Realm.

IBGVRT The gprs attribute of a REC is the set of general-purpose register values which are saved by the RMM on exit from the REC and restored by the RMM on entry to the REC.

IFPJDL The mpidr attribute of a REC is a value which can be used to identify the VPE associated with the REC.

IBLVKZ The pc attribute of a REC is the program counter which is saved by the RMM on exit from the REC and restored by the RMM on entry to the REC.

IGHFNQ The runnable flag of a REC determines whether the REC is eligible for execution. The RMI\_REC\_ENTER command results in a REC entry only if the value of the flag is RUNNABLE.

ISCCMH The runnable flag of a REC is controlled by the Realm. Its initial value is reflected in the Realm Initial Measurement, and during Realm execution its value can be changed by execution of the PSCI\_CPU\_ON and PSCI\_CPU\_OFF commands.

IPMYBG The state attribute of a REC is controlled by the Host, by execution of the RMI\_REC\_ENTER command.

DCDXDZ The sysregs attribute of a REC is the set of system register values which are saved by the RMM on exit from the REC and restored by the RMM on entry to the REC.

See also:

- A2.3.3 REC index and MPIDR value
- A2.3.4 REC lifecycle
- A4.3.4.3 REC exit due to Data Abort
- B4.3.14 RMI\_REC\_ENTER command
- B6.3.2 PSCI\_CPU\_OFF command
- B6.3.3 PSCI\_CPU\_ON command
- C1.19 RmmRec type

## A2.3.3 REC index and MPIDR value

DKQVHN The REC index is the unsigned integer value generated by concatenation of MPIDR fields:

```
index = Aff3:Aff2:Aff1:Aff0[3:0]
```

This is illustrated by the following table.

| REC index   | Aff3   | Aff2   | Aff1   | Aff0[3:0]   |
|-------------|--------|--------|--------|-------------|
| 0           | 0      | 0      | 0      | 0           |
| 1           | 0      | 0      | 0      | 1           |
| . . .       | . . .  | . . .  | . . .  | . . .       |
| 16          | 0      | 0      | 1      | 0           |

IPVLZY

ITTWVM

IPHMWT

IFNSTJ

| REC index   | Aff3   | Aff2   | Aff1   | Aff0[3:0]   |
|-------------|--------|--------|--------|-------------|
| 4096        | 0      | 1      | 0      | 0           |
| . . .       | . . .  | . . .  | . . .  | . . .       |
| 1048576     | 1      | 0      | 0      | 0           |
| . . .       | . . .  | . . .  | . . .  | . . .       |

The Aff0[7:4] field of a REC MPIDR value is RES0 for compatibility with GICv3.

When creating the n th REC in a Realm, the Host is required to use the MPIDR corresponding to REC index n

## See also:

- B3.38 RecIndex function
- B4.3.12 RMI\_REC\_CREATE command
- B4.4.18 RmiRecMpidr type

## A2.3.4 REC lifecycle

## A2.3.4.1 States

DHTXQY The states of a REC are listed below.

| State       | Description                   |
|-------------|-------------------------------|
| REC_READY   | REC is not currently running. |
| REC_RUNNING | REC is currently running.     |

## A2.3.4.2 State transitions

Permitted REC state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a REC object. A transition to the pseudo-state NULL represents destruction of a REC object.

| From state   | To state    | Events                    |
|--------------|-------------|---------------------------|
| NULL         | REC_READY   | RMI_REC_CREATE            |
| REC_READY    | NULL        | RMI_REC_DESTROY           |
| REC_READY    | REC_RUNNING | RMI_REC_ENTER             |
| REC_RUNNING  | REC_READY   | Return from RMI_REC_ENTER |

Permitted REC state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

A transition from the pseudo-state NULL represents creation of a REC. A transition to the pseudo-state NULL represents destruction of a REC.

.

Figure A2.3: REC state transitions

<!-- image -->

ILYXCN The maximum number of RECs per Realm is an IMPLEMENTATION DEFINED value which is discoverable via RMI\_FEATURES.

See also:

- B4.3.12 RMI\_REC\_CREATE command
- B4.3.13 RMI\_REC\_DESTROY command
- B4.3.14 RMI\_REC\_ENTER command

See also:

- B4.3.4 RMI\_FEATURES command