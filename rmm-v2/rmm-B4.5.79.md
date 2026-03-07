## B4.5.79 RMI\_VDEV\_ABORT command

Abort device communication associated with a VDEV.

See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)

## B4.5.79.1 Interface

## B4.5.79.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000185 |
| rd       | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV        |

## B4.5.79.1.2 Context

The RMI\_VDEV\_ABORT command operates on the following context.

| Name   | Type     | Value            | Before   | Description   |
|--------|----------|------------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd)      | false    | Realm         |
| pdev   | RmmPdev  | PdevAt(pdev_ptr) | false    | PDEV          |
| vdev   | RmmVdev  | VdevAt(vdev_ptr) | false    | VDEV          |

## B4.5.79.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.79.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* pdev_align
  * pre: !AddrIsRmiGranuleAligned(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_bound
  * pre: !PaIsTracked(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_gran_state
  * pre: GranuleAt(pdev_ptr).state != GRAN_PDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_align
  * pre: !AddrIsRmiGranuleAligned(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_bound
  * pre: !PaIsTracked(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_gran_state
  * pre: GranuleAt(vdev_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_realm
  * pre: vdev.realm != rd
  * post: result.status == RMI_ERROR_INPUT
* vdev_pdev
  * pre: vdev.pdev != pdev_ptr
  * post: result.status == RMI_ERROR_DEVICE
* comm_state
  * pre: vdev.comm_state == DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE

## pre: post: B4.5.79.2.1 Failure condition ordering [feat] &lt; [rd\_align, rd\_bound, rd\_state, pdev\_align, pdev\_bound, pdev\_gran\_state, vdev\_align, vdev\_bound, vdev\_gran\_state, vdev\_realm] [vdev\_gran\_state] &lt; [vdev\_pdev, comm\_state]

## B4.5.79.3 Success conditions

* state
  * post: vdev.vdev_state == VDEV_ERROR
* comm_state
  * post: vdev.comm_state == DEV_COMM_IDLE

## B4.5.79.4 Footprint

## Value

vdev.vdev\_state

## ID

state

| ID         | Value           |
|------------|-----------------|
| comm_state | vdev.comm_state |

<!-- image -->