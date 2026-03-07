## B4.5.87 RMI\_VDEV\_LOCK command

Lock VDEV.

See also:

- [A9.4.3 Virtual device lifecycle](rmm-A9.4.md#a943-virtual-device-lifecycle)

## B4.5.87.1 Interface

## B4.5.87.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001D2 |
| rd       | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV        |

## B4.5.87.1.2 Context

The RMI\_VDEV\_LOCK command operates on the following context.

| Name   | Type     | Value            | Before   | Description   |
|--------|----------|------------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd)      | false    | Realm         |
| pdev   | RmmPdev  | PdevAt(pdev_ptr) | false    | PDEV          |
| vdev   | RmmVdev  | VdevAt(vdev_ptr) | false    | VDEV          |

## B4.5.87.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.87.2 Failure conditions

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
* vdev_state
  * pre: vdev.vdev_state != VDEV_UNLOCKED
  * post: result.status == RMI_ERROR_DEVICE
* comm_state
  * pre: vdev.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.87.3 Success conditions

* comm_state
  * post: vdev.op == VDEV_OP_LOCK vdev.comm_state

## B4.5.87.4 Footprint

==

DEV\_COMM\_PENDING

| ID         | Value           |
|------------|-----------------|
| op         | vdev.op         |
| comm_state | vdev.comm_state |

<!-- image -->