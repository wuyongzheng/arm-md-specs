## A2.1 RMM

This section describes the global attributes and the lifecycle of the RMM.

## A2.1.1 RMM attributes

IRHWMT The global state of the RMM is modelled as comprising two components:

- Static attributes
- -Which optional features are supported by the implementation
- -Configuration values of the implementation
- Dynamic attributes
- -State which can be mutated through execution of RMM commands

IWJRJZ The Rmm() function returns an RmmGlobal data structure which models both the static and dynamic attributes of the implementation.

DLPNGM The attributes of the RMM are summarized in the following table.

| Name    | Type             | Description        |
|---------|------------------|--------------------|
| static  | RmmGlobalStatic  | Static attributes  |
| dynamic | RmmGlobalDynamic | Dynamic attributes |

IMZQZX Static attributes of the RMM can be read by execution of RMI\_FEATURES.

IQMGZX Dynamic attributes of the RMM can be read by execution of RMI\_RMM\_CONFIG\_GET.

- ILLTDW Dynamic attributes of the RMM can be modified by execution of RMI\_RMM\_CONFIG\_SET.

See also:

- A2.3.1 Granule size
- A2.3.4 Granule tracking region
- Chapter A3 Feature discovery and configuration

DRAFT

- B3.152 Rmm function
- B4.5.14 RMI\_FEATURES command
- B4.5.53 RMI\_RMM\_CONFIG\_GET command
- B4.5.54 RMI\_RMM\_CONFIG\_SET command
- C2.17 RmmGlobal type

## A2.1.2 RMM lifecycle

## A2.1.2.1 States

DXFMQC The states of a RMM are listed below.

| State                                                  | Description                                            |
|--------------------------------------------------------|--------------------------------------------------------|
| RMM_STATE_INIT                                         | Initial state of the RMM.                              |
| RMM_STATE_INTERMEDIATERMM is in an intermediate state. | RMM_STATE_INTERMEDIATERMM is in an intermediate state. |
| RMM_STATE_ACTIVE                                       | RMMis active.                                          |

RMI\_RMM\_CONFIG\_SET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_INIT.

IFDHLK

- ITNTTB RMI\_GRANULE\_TRACKING\_SET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

IHMVNJ RMI\_GRANULE\_TRACKING\_GET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

ISFCDR RMI\_GRANULE\_RANGE\_DELEGATE fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE. This means that any RMM operation which requires access to delegated memory is also prevented unless the RMM state is RMM\_STATE\_ACTIVE.

ITYYKQ RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

See also:

- A9.11.7 Coherent memory device attestation
- B4.5.1 RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH command
- B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command
- B4.5.20 RMI\_GRANULE\_TRACKING\_SET command
- B4.5.54 RMI\_RMM\_CONFIG\_SET command

## A2.1.2.2 State transitions

IHPMDX Permitted RMM state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

| From state             | To state               | Events           |
|------------------------|------------------------|------------------|
| RMM_STATE_INIT         | RMM_STATE_ACTIVE       | RMI_RMM_ACTIVATE |
| RMM_STATE_INIT         | RMM_STATE_INTERMEDIATE | RMI_RMM_ACTIVATE |
| RMM_STATE_INTERMEDIATE | RMM_STATE_ACTIVE       | RMI_OP_CONTINUE  |

IHWCTN Permitted RMM state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.

DRAFT

Figure A2.1: RMM state transitions

<!-- image -->

## See also:

- B4.5.22 RMI\_OP\_CONTINUE command
- B4.5.52 RMI\_RMM\_ACTIVATE command