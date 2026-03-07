## B4.5.86 RMI\_VDEV\_GET\_STATE command

Get state of a VDEV.

See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)

## B4.5.86.1 Interface

## B4.5.86.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000189 |
| vdev_ptr | X1         | 63:0   | Address | PA of the VDEV        |

## B4.5.86.1.2 Context

The RMI\_VDEV\_GET\_STATE command operates on the following context.

| Name   | Type    | Value            | Before   | Description   |
|--------|---------|------------------|----------|---------------|
| vdev   | RmmVdev | VdevAt(vdev_ptr) | false    | VDEV          |

## B4.5.86.1.3 Output values

| Name   | Register   | Bits   | Type         | Description    |
|--------|------------|--------|--------------|----------------|
| result | X0         | 63:0   | RmiResult    | Command result |
| state  | X1         | 7:0    | RmiVdevState | VDEV state     |


The following unused bits of RMI\_VDEV\_GET\_STATE output values MBZ: X1[63:8].

## B4.5.86.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* vdev_align
  * pre: !AddrIsRmiGranuleAligned(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_bound
  * pre: !PaIsTracked(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_gran_state
  * pre: GranuleAt(vdev_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* state

## B4.5.86.2.1 Failure condition ordering

[feat] &lt; [vdev\_align, vdev\_bound, vdev\_gran\_state]

<!-- image -->

## B4.5.86.3 Success conditions

Condition post: Equal(state, vdev.vdev\_state)

## B4.5.86.4 Footprint

The RMI\_VDEV\_GET\_STATE command does not have any footprint.

