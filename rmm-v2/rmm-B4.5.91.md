## B4.5.91 RMI\_VDEV\_UNLOCK command

Unlock a VDEV.

See also:

- [A9.4.3 Virtual device lifecycle](rmm-A9.4.md#a943-virtual-device-lifecycle)

## B4.5.91.1 Interface

## B4.5.91.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC400018A |
| rd       | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV        |

## B4.5.91.1.2 Context

The RMI\_VDEV\_UNLOCK command operates on the following context.

| Name   | Type              | Value                | Before   | Description                            |
|--------|-------------------|----------------------|----------|----------------------------------------|
| realm  | RmmRealm          | RealmAt(rd)          | false    | Realm                                  |
| pdev   | RmmPdev           | PdevAt(pdev_ptr)     | false    | PDEV                                   |
| vdev   | RmmVdev           | VdevAt(vdev_ptr)     | false    | VDEV                                   |
| mapped | RmmVdevAddrResult | VdevFindMapped(vdev) | false    | Result of scanning for mapped Granules |


## B4.5.91.1.3 Output values

| Name   | Register   | Bits   | Type      | Description                 |
|--------|------------|--------|-----------|-----------------------------|
| result | X0         | 63:0   | RmiResult | Command result              |
| addr   | X1         | 63:0   | Address   | Address of assigned Granule |

## B4.5.91.2 Failure conditions

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
  * pre: (vdev.vdev_state != VDEV_LOCKED && vdev.vdev_state != VDEV_STARTED && vdev.vdev_state != VDEV_ERROR)
  * post: result.status == RMI_ERROR_DEVICE
* comm_state
  * pre: vdev.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE
* gran_mapped
  * pre: mapped.valid == RMM_TRUE (
  * post: result.status == RMI_ERROR_GRANULE && addr == mapped.addr)

## B4.5.91.2.1 Failure condition ordering

```
[rd_bound, rd_state, vdev_bound, vdev_gran_state] < [vdev_realm] [feat] < [rd_align, rd_bound, rd_state, pdev_align, pdev_bound, pdev_gran_state, vdev_align, vdev_bound, vdev_gran_state, vdev_realm] [vdev_gran_state] < [vdev_pdev, vdev_state, comm_state, gran_mapped]
```

<!-- image -->

<!-- image -->

## B4.5.91.3 Success conditions

* dma_state
  * post: vdev.dma_state == VDEV_DMA_DISABLED
* op
  * post: vdev.op == VDEV_OP_UNLOCK
* comm_state
  * post: vdev.comm_state == DEV_COMM_PENDING

