## B4.5.53 RMI\_RMM\_CONFIG\_GET command

Get the system configuration.

See also:

## · A2.1 RMM

## B4.5.53.1 Interface

## B4.5.53.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                   |
|---------|------------|--------|---------|-------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC40001EC         |
| cfg_ptr | X1         | 63:0   | Address | PA of configuration structure |

## B4.5.53.1.2 Context

The RMI\_RMM\_CONFIG\_GET command operates on the following context.

| Name   | Type         | Value                   | Before   | Description     |
|--------|--------------|-------------------------|----------|-----------------|
| rmm    | RmmGlobal    | Rmm()                   | false    | RMMglobal state |
| cfg    | RmiRmmConfig | RmiRmmConfigAt(cfg_ptr) | false    | Configuration   |

## B4.5.53.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.53.2 Failure conditions

| ID        | Condition                                                                          |
|-----------|------------------------------------------------------------------------------------|
| rmm_state | pre: rmm.dynamic.state != RMM_STATE_ACTIVE post: result.status == RMI_ERROR_GLOBAL |
| cfg_align | pre: !AddrIsRmiGranuleAligned(cfg_ptr) post: result.status == RMI_ERROR_INPUT      |
| cfg_pas   | pre: !NonSecureAccessPermitted(cfg_ptr) post: result.status == RMI_ERROR_INPUT     |

## B4.5.53.2.1 Failure condition ordering

The RMI\_RMM\_CONFIG\_GET command does not have any failure condition orderings.

## B4.5.53.3 Success conditions

| ID                   | Condition                                                                                                                  |
|----------------------|----------------------------------------------------------------------------------------------------------------------------|
| rmi_granule_size     | post: cfg.rmi_granule_size == GranuleSizeToRmi( rmm.dynamic.rmi_granule_size)                                              |
| tracking_region_size | post: cfg.tracking_region_size == TrackingRegionSizeToRmi( rmm.dynamic.rmi_granule_size, rmm.dynamic.tracking_region_size) |

## B4.5.53.4 Footprint

The RMI\_RMM\_CONFIG\_GET command does not have any footprint.

<!-- image -->