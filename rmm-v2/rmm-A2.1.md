## A2.1 RMM

This section describes the global attributes and the lifecycle of the RMM.

## A2.1.1 RMM attributes

The global state of the RMM is modelled as comprising two components:

- Static attributes
- -Which optional features are supported by the implementation
- -Configuration values of the implementation
- Dynamic attributes
- -State which can be mutated through execution of RMM commands

The Rmm() function returns an RmmGlobal data structure which models both the static and dynamic attributes of the implementation.

The attributes of the RMM are summarized in the following table.

| Name    | Type             | Description        |
|---------|------------------|--------------------|
| static  | RmmGlobalStatic  | Static attributes  |
| dynamic | RmmGlobalDynamic | Dynamic attributes |

Static attributes of the RMM can be read by execution of RMI\_FEATURES.

Dynamic attributes of the RMM can be read by execution of RMI\_RMM\_CONFIG\_GET.

- Dynamic attributes of the RMM can be modified by execution of RMI\_RMM\_CONFIG\_SET.

See also:

- [A2.3.1 Granule size](rmm-A2.3.md#a231-granule-size)
- [A2.3.4 Granule tracking region](rmm-A2.3.md#a234-granule-tracking-region)
- [Chapter A3 Feature discovery and configuration](rmm-A3.md)


- [B3.152 Rmm function](rmm-B3.md#b3152-rmm-function)
- [B4.5.14 RMI\_FEATURES command](rmm-B4.5.14.md)
- [B4.5.53 RMI\_RMM\_CONFIG\_GET command](rmm-B4.5.53.md)
- [B4.5.54 RMI\_RMM\_CONFIG\_SET command](rmm-B4.5.54.md)
- [C2.17 RmmGlobal type](rmm-C2.md#c217-rmmglobal-type)

## A2.1.2 RMM lifecycle

## A2.1.2.1 States

The states of a RMM are listed below.

| State                                                  | Description                                            |
|--------------------------------------------------------|--------------------------------------------------------|
| RMM_STATE_INIT                                         | Initial state of the RMM.                              |
| RMM_STATE_INTERMEDIATERMM is in an intermediate state. | RMM_STATE_INTERMEDIATERMM is in an intermediate state. |
| RMM_STATE_ACTIVE                                       | RMMis active.                                          |

RMI\_RMM\_CONFIG\_SET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_INIT.


- RMI\_GRANULE\_TRACKING\_SET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

RMI\_GRANULE\_TRACKING\_GET fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

RMI\_GRANULE\_RANGE\_DELEGATE fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE. This means that any RMM operation which requires access to delegated memory is also prevented unless the RMM state is RMM\_STATE\_ACTIVE.

RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH fails with RMI\_ERROR\_GLOBAL unless the RMM state is RMM\_STATE\_ACTIVE.

See also:

- [A9.11.7 Coherent memory device attestation](rmm-A9.11.md#a9117-coherent-memory-device-attestation)
- [B4.5.1 RMI\_ATTEST\_PLAT\_TOKEN\_REFRESH command](rmm-B4.5.1.md)
- [B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command](rmm-B4.5.17.md)
- [B4.5.20 RMI\_GRANULE\_TRACKING\_SET command](rmm-B4.5.20.md)
- [B4.5.54 RMI\_RMM\_CONFIG\_SET command](rmm-B4.5.54.md)

## A2.1.2.2 State transitions

Permitted RMM state transitions are shown in the following table. The rightmost column lists the events which can cause the corresponding state transition.

| From state             | To state               | Events           |
|------------------------|------------------------|------------------|
| RMM_STATE_INIT         | RMM_STATE_ACTIVE       | RMI_RMM_ACTIVATE |
| RMM_STATE_INIT         | RMM_STATE_INTERMEDIATE | RMI_RMM_ACTIVATE |
| RMM_STATE_INTERMEDIATE | RMM_STATE_ACTIVE       | RMI_OP_CONTINUE  |

Permitted RMM state transitions are shown in the following figure. Each arc is labeled with the events which can cause the corresponding state transition.


Figure A2.1: RMM state transitions

<!-- image -->

## See also:

- [B4.5.22 RMI\_OP\_CONTINUE command](rmm-B4.5.22.md)
- [B4.5.52 RMI\_RMM\_ACTIVATE command](rmm-B4.5.52.md)