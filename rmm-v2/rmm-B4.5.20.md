## B4.5.20 RMI\_GRANULE\_TRACKING\_SET command

Set configuration of a Granule tracking region.

The RMI\_GRANULE\_TRACKING\_SET command may initiate a Stateful RMI Operation.

The RMI\_GRANULE\_TRACKING\_SET command may initiate a memory-transferring RMI Operation.

## See also:

- [A2.3.4 Granule tracking region](rmm-A2.3.md#a234-granule-tracking-region)
- [B4.5.19 RMI\_GRANULE\_TRACKING\_GET command](rmm-B4.5.19.md)

## B4.5.20.1 Interface

## B4.5.20.1.1 Input values

| Name     | Register   | Bits   | Type                   | Description               |
|----------|------------|--------|------------------------|---------------------------|
| fid      | X0         | 63:0   | UInt64                 | FID, value 0xC40001E3     |
| addr     | X1         | 63:0   | Address                | PA of the tracking region |
| category | X2         | 1:0    | RmiMemCategory         | Memory category           |
| state    | X3         | 2:0    | RmiTrackingRegionState | state                     |

The following unused bits of RMI\_GRANULE\_TRACKING\_SET input values SBZ: X2[63:2], X3[63:3].

## B4.5.20.1.2 Context

The RMI\_GRANULE\_TRACKING\_SET command operates on the following context.

| Name       | Type              | Value                  | Before   | Description     |
|------------|-------------------|------------------------|----------|-----------------|
| rmm_pre    | RmmGlobal         | Rmm()                  | true     | RMMglobal state |
| rmm        | RmmGlobal         | Rmm()                  | false    | RMMglobal state |
| region_pre | RmmTrackingRegion | TrackingRegionAt(addr) | true     | Tracking region |
| region     | RmmTrackingRegion | TrackingRegionAt(addr) | false    | Tracking region |


## B4.5.20.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.20.2 Failure conditions

* rmm_state
  * pre: rmm.dynamic.state != RMM_STATE_ACTIVE
  * post: result.status == RMI_ERROR_GLOBAL
* state_valid
  * pre: (state != RMI_TRACKING_NONE && state != RMI_TRACKING_FINE && state != RMI_TRACKING_COARSE)
  * post: result.status == RMI_ERROR_INPUT
* addr_align
  * pre: !AddrIsTrackingRegionAligned(addr)
  * post: result.status == RMI_ERROR_INPUT
* addr_bound
  * pre: UInt(addr) > rmm.static.
* pasz
  * post: result.status == RMI_ERROR_INPUT
* category
  * pre: !MemCategoryIsCompatible(category, addr)
  * post: result.status == RMI_ERROR_INPUT
* reserved
  * pre: region.state == TRACKING_RESERVED
  * post: result.status == RMI_ERROR_INPUT
* in_state
  * pre: State of a Granule in input list is not GRAN_DELEGATED.
  * post: result.status == RMI_ERROR_INPUT
* in_loc_dram
  * pre: Tracking region is backed by DRAM and a Granule in input list is not located in DRAM.
  * post: result.status == RMI_ERROR_INPUT
* in_loc_cmem
  * pre: Tracking region is backed by a CMEM Interleave Set and a Granule in input list is located neither in DRAM nor in that CMEM Interleave Set.
  * post: result.status == RMI_ERROR_INPUT B4.5.20.2.1 Failure condition ordering The RMI_GRANULE_TRACKING_SET command does not have any failure condition orderings.

## B4.5.20.3 Success conditions

* tracked_inc
  * pre: (!TrackingRegionIsTracked(region_pre) && TrackingRegionIsTracked(region))
  * post: rmm.dynamic.num_tracked == rmm_pre.dynamic.num_tracked + 1
* tracked_dec
  * pre: (TrackingRegionIsTracked(region_pre) && !TrackingRegionIsTracked(region))
  * post: rmm.dynamic.num_tracked == rmm_pre.dynamic.num_tracked - 1
* result
  * post: result.status == RMI_SUCCESS
* state
  * post: Equal(region.state, state)

## B4.5.20.4 Footprint

| ID          | Value                   |
|-------------|-------------------------|
| num_tracked | rmm.dynamic.num_tracked |