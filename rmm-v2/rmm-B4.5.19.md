## B4.5.19 RMI\_GRANULE\_TRACKING\_GET command

Get configuration of a Granule tracking region.

See also:

- [A2.3.4 Granule tracking region](rmm-A2.3.md#a234-granule-tracking-region)
- [B4.5.20 RMI\_GRANULE\_TRACKING\_SET command](rmm-B4.5.20.md)

## B4.5.19.1 Interface

## B4.5.19.1.1 Input values

| Name   | Register   | Bits   | Type    | Description               |
|--------|------------|--------|---------|---------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001E1     |
| addr   | X1         | 63:0   | Address | PA of the tracking region |

## B4.5.19.1.2 Context

The RMI\_GRANULE\_TRACKING\_GET command operates on the following context.

| Name   | Type              | Value                  | Before   | Description     |
|--------|-------------------|------------------------|----------|-----------------|
| rmm    | RmmGlobal         | Rmm()                  | false    | RMMglobal state |
| region | RmmTrackingRegion | TrackingRegionAt(addr) | false    | Tracking region |

## B4.5.19.1.3 Output values

| Name     | Register   | Bits   | Type                   | Description           |
|----------|------------|--------|------------------------|-----------------------|
| result   | X0         | 63:0   | RmiResult              | Command result        |
| category | X1         | 1:0    | RmiMemCategory         | Memory category       |
| state    | X2         | 2:0    | RmiTrackingRegionState | Tracking region state |


The following unused bits of RMI\_GRANULE\_TRACKING\_GET output values MBZ: X1[63:2], X2[63:3].

## B4.5.19.2 Failure conditions

* addr_align
  * pre: !AddrIsTrackingRegionAligned(addr)
  * post: result.status == RMI_ERROR_INPUT
* addr_bound
  * pre: UInt(addr) > rmm.static.pasz
  * post: result.status == RMI_ERROR_INPUT

## B4.5.19.2.1 Failure condition ordering

The RMI\_GRANULE\_TRACKING\_GET command does not have any failure condition orderings.

## B4.5.19.3 Success conditions

* state
  * post: Equal(state, region.state)
* category
  * post: Equal(category, region.category)

## B4.5.19.4 Footprint

The RMI\_GRANULE\_TRACKING\_GET command does not have any footprint.

<!-- image -->