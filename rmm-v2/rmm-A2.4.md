## A2.4 Realm Execution Context

This section describes the concept of a Realm Execution Context (REC).

## A2.4.1 Overview


A Realm Execution Context (REC) is an R-EL0&amp;1 execution context which is associated with a Realm VPE.

A REC object is an RMM data structure which is used to store the register state of a REC.

## See also:

- [A2.2.2 Realm execution environment](rmm-A2.2.md#a222-realm-execution-environment)
- Chapter A4 Realm exception model

## A2.4.2 REC attributes

This section describes the attributes of a REC.

- A REC attribute is a property of a REC whose value can be observed or modified either by the Host or by the Realm which owns the REC.
- Examples of ways in which a REC attribute may be observable include the outcome of an RMM command, and the PE state following Realm entry.
- The attributes of a REC are summarized in the following table.

| Name             | Type                    | Description                                                                    |
|------------------|-------------------------|--------------------------------------------------------------------------------|
| owner            | Address                 | PA of RD of Realm which owns this REC                                          |
| flags            | RmmRecFlags             | Flags which control REC behavior                                               |
| mpidr            | Bits64                  | MPIDR value                                                                    |
| gic_owner        | UInt64                  | Index of Plane which is the GIC owner                                          |
| state            | RmmRecState             | Lifecycle state                                                                |
| pending          | RmmRecPending           | Whether a REC operation is pending                                             |
| emulatable_abort | RmmRecEmulatableAbort   | Whether the most recent exit from this REC was due to an Emulatable Data Abort |
| gprs             | Bits64[32]              | General-purpose register values                                                |
| pc               | Bits64                  | Program counter value                                                          |
| sysregs          | RmmSystemRegisters      | EL1 and EL0 system register values                                             |
| attest_state     | RmmRecAttestState       | Attestation token generation state                                             |
| attest_challenge | Bits512                 | Challenge for under-construction attestation token                             |
| ripas_addr       | Address                 | Next IPA to be processed in RIPAS change                                       |
| ripas_top        | Address                 | Top IPA of pending RIPAS change                                                |
| ripas_value      | RmmRipas                | RIPAS value of pending RIPAS change                                            |
| ripas_destroyed  | RmmRipasChangeDestroyed | Whether a RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should be permitted   |
| ripas_response   | RmmRecResponse          | Host response to RIPAS change request                                          |
| dev_mem_addr     | Address                 | Next IPA to be processed in VDEV mapping validation                            |


| Name                            | Type                            | Description                                                              |
|---------------------------------|---------------------------------|--------------------------------------------------------------------------|
| dev_mem_top                     | Address                         | Top IPA of pending VDEV mapping validation                               |
| dev_mem_pa                      | Address                         | PA of device memory                                                      |
| dev_mem_flags                   | RmmDevMemFlags                  | VDEV mapping validation flags                                            |
| dev_mem_response RmmRecResponse | dev_mem_response RmmRecResponse | Host response to VDEV mapping validation request                         |
| s2ap_addr                       | Address                         | Next IPA to be processed in S2AP change                                  |
| s2ap_top                        | Address                         | Top IPA of pending S2AP change                                           |
| s2ap_overlay_indexUInt4         | s2ap_overlay_indexUInt4         | Overlay index of pending S2AP change                                     |
| s2ap_response                   | RmmRecResponse                  | Host response to S2AP change request                                     |
| vdev_comm_pending RmmBoolean    | vdev_comm_pending RmmBoolean    | Whether a VDEV transaction should be initiated when the VDEV is provided |
| vdev_id_1                       | Bits64                          | Virtual device ID 1                                                      |
| vdev_pa_1                       | Address                         | VDEV PA                                                                  |
| vdev_id_2                       | Bits64                          | Virtual device ID 2                                                      |
| vdev_attest_info_1              | RmmVdevAttestInfo               | Attestation information for first VDEV                                   |
| vdev_attest_info_2              | RmmVdevAttestInfo               | Attestation information for second VDEV                                  |
| vsmmu_vsid                      | Bits64                          | Virtual SMMUStream ID                                                    |
| vsmmu_resp                      | Bits64                          | PRI response                                                             |
| vsmmu_pasid                     | Bits64                          | PASID                                                                    |

| I BGVRT   | The gprs attribute of a REC is the set of general-purpose register values which are saved by the RMMon exit from the REC and restored by the RMMon entry to the REC.                                                                  |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I FPJDL   | The mpidr attribute of a REC is a value which can be used to identify the VPE associated with the REC.                                                                                                                                |
| I BLVKZ   | The pc attribute of a REC is the program counter which is saved by the RMMon exit from the REC and restored by the RMMon entry to the REC.                                                                                            |
| I GHFNQ   | The runnable flag of a REC determines whether the REC is eligible for execution. The RMI_REC_ENTER command results in a REC entry only if the value of the flag is RUNNABLE.                                                          |
| I SCCMH   | The runnable flag of a RECis controlled by the Realm. Its initial value is reflected in the Realm Initial Measurement, and during Realm execution its value can be changed by execution of the PSCI_CPU_ON and PSCI_CPU_OFF commands. |
| I PMYBG   | The state attribute of a REC is controlled by the Host, by execution of the RMI_REC_ENTER command.                                                                                                                                    |
| D CDXDZ   | The sysregs attribute of a REC is the set of system register values which are saved by the RMMon exit from the REC and restored by the RMMon entry to the REC.                                                                        |
| D RWKGW   | The gic_owner attribute of a REC is the index of the Plane which is the GIC owner for the REC.                                                                                                                                        |


- A2.4.3 REC index and MPIDR value
- A2.4.4 REC lifecycle
- A4.3.4.3 REC exit due to Data Abort
- A10.4 Planes interrupts
- B4.5.51 RMI\_REC\_ENTER command

- B6.3.2 PSCI\_CPU\_OFF command
- B6.3.3 PSCI\_CPU\_ON command
- C2.52 RmmRec type

## A2.4.3 REC index and MPIDR value

The REC index is the unsigned integer value generated from MPIDR fields as follows:

```
index = aff0 + 16 * aff1 + 16 * 256 * aff2 + 16 * 256 * 256 * aff3
```

This is illustrated by the following table.


| REC index   | Aff3   | Aff2   | Aff1   | Aff0[3:0]   |
|-------------|--------|--------|--------|-------------|
| 0           | 0      | 0      | 0      | 0           |
| 1           | 0      | 0      | 0      | 1           |
| . . .       | . . .  | . . .  | . . .  | . . .       |
| 16          | 0      | 0      | 1      | 0           |
| . . .       | . . .  | . . .  | . . .  | . . .       |
| 4096        | 0      | 1      | 0      | 0           |
| . . .       | . . .  | . . .  | . . .  | . . .       |
| 1048576     | 1      | 0      | 0      | 0           |
| . . .       | . . .  | . . .  | . . .  | . . .       |

The Aff0[7:4] field of a REC MPIDR value is RES0 for compatibility with GICv3.


When creating the n th REC in a Realm, the Host is required to use the MPIDR corresponding to REC index n .

## See also:

- [B3.107 RecIndex function](rmm-B3.md#b3107-recindex-function)
- [B4.5.49 RMI\_REC\_CREATE command](rmm-B4.5.49.md)
- [B4.6.68 RmiRecMpidr type](rmm-B4.6.md#b4668-rmirecmpidr-type)

## A2.4.4 REC lifecycle

## A2.4.4.1 States

The states of a REC are listed below.

| State       | Description                   |
|-------------|-------------------------------|
| REC_READY   | REC is not currently running. |
| REC_RUNNING | REC is currently running.     |

## A2.4.4.2 State transitions

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

<!-- image -->


Figure A2.10: REC state transitions

The maximum number of RECs per Realm is an IMPLEMENTATION DEFINED value which is discoverable via RMI\_FEATURES.

## See also:

- [B4.5.49 RMI\_REC\_CREATE command](rmm-B4.5.49.md)
- [B4.5.50 RMI\_REC\_DESTROY command](rmm-B4.5.50.md)
- [B4.5.51 RMI\_REC\_ENTER command](rmm-B4.5.51.md)

## See also:

- [B4.5.14 RMI\_FEATURES command](rmm-B4.5.14.md)