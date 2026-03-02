## B4.5.54 RMI\_RMM\_CONFIG\_SET command

Set the system configuration.

See also:

## · A2.1 RMM

## B4.5.54.1 Interface

## B4.5.54.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                   |
|---------|------------|--------|---------|-------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400016E         |
| cfg_ptr | X1         | 63:0   | Address | PA of configuration structure |

## B4.5.54.1.2 Context

The RMI\_RMM\_CONFIG\_SET command operates on the following context.

| Name   | Type         | Value                   | Before   | Description     |
|--------|--------------|-------------------------|----------|-----------------|
| rmm    | RmmGlobal    | Rmm()                   | false    | RMMglobal state |
| cfg    | RmiRmmConfig | RmiRmmConfigAt(cfg_ptr) | false    | Configuration   |

## B4.5.54.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

DRAFT

## B4.5.54.2 Failure conditions

| ID        | Condition                                                                        |
|-----------|----------------------------------------------------------------------------------|
| rmm_state | pre: rmm.dynamic.state != RMM_STATE_INIT post: result.status == RMI_ERROR_GLOBAL |
| cfg_align | pre: !AddrIsRmiGranuleAligned(cfg_ptr) post: result.status == RMI_ERROR_INPUT    |
| cfg_pas   | pre: !NonSecureAccessPermitted(cfg_ptr) post: result.status == RMI_ERROR_INPUT   |
| cfg_supp  | pre: !RmmConfigIsSupported(cfg) post: result.status == RMI_ERROR_INPUT           |
| tracked   | pre: rmm.dynamic.num_tracked != 0 post: result.status == RMI_ERROR_INPUT         |

## B4.5.54.2.1 Failure condition ordering

The RMI\_RMM\_CONFIG\_SET command does not have any failure condition orderings.

## B4.5.54.3 Success conditions

| ID                   | Condition                                                                                                            |
|----------------------|----------------------------------------------------------------------------------------------------------------------|
| rmi_granule_size     | post: rmm.dynamic.rmi_granule_size == GranuleSizeFromRmi( cfg.rmi_granule_size)                                      |
| tracking_region_size | post: rmm.dynamic.tracking_region_size == TrackingRegionSizeFromRmi( cfg.rmi_granule_size, cfg.tracking_region_size) |

## B4.5.54.4 Footprint

| ID                   | Value                            |
|----------------------|----------------------------------|
| rmi_granule_size     | rmm.dynamic.rmi_granule_size     |
| tracking_region_size | rmm.dynamic.tracking_region_size |

<!-- image -->