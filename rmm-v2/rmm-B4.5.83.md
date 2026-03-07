## B4.5.83 RMI\_VDEV\_DESTROY command

Destroy a VDEV.

The RMI\_VDEV\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_VDEV\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- Chapter A9 Realm device assignment
- B4.3.4 Object creation and destruction

## B4.5.83.1 Interface

## B4.5.83.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000188 |
| rd       | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV        |

## B4.5.83.1.2 Context

The RMI\_VDEV\_DESTROY command operates on the following context.

| Name           | Type                                              | Value                                             | Before         | Description                       |
|----------------|---------------------------------------------------|---------------------------------------------------|----------------|-----------------------------------|
| realm_pre      | RmmRealm                                          | RealmAt(rd)                                       | true           | Realm                             |
| realm          | RmmRealm                                          | RealmAt(rd)                                       | false          | Realm                             |
| vdev_pre       | RmmVdev                                           | VdevAt(vdev_ptr)                                  | true           | VDEV                              |
| pdev_pre       | RmmPdev                                           | PdevAt(pdev_ptr)                                  | true           | PDEV                              |
| pdev           | RmmPdev                                           | PdevAt(pdev_ptr)                                  | false          | PDEV                              |
| psmmu          | RmmPsmmu                                          | PsmmuFromPdev(pdev)                               | false          | PSMMU                             |
| st_walk        | RmmPsmmuStWalkResult PsmmuStWalk( psmmu, VdevSid( | RmmPsmmuStWalkResult PsmmuStWalk( psmmu, VdevSid( | false          | Result of PSMMU Stream Table walk |
| ↪ → vdev_pre)) | ↪ → vdev_pre))                                    | ↪ → vdev_pre))                                    | ↪ → vdev_pre)) | ↪ → vdev_pre))                    |


## B4.5.83.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.83.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_gran_state
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
* vdev_tracking
  * pre: !PaIsTrackedFine(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_gran_state
  * pre: GranuleAt(vdev_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_realm
  * pre: vdev_pre.realm !=
* rd
  * post: result.status == RMI_ERROR_DEVICE
* vdev_pdev
  * pre: vdev_pre.pdev !=
* pdev_ptr
  * post: result.status == RMI_ERROR_DEVICE
* vdev_state
  * pre: (vdev_pre.vdev_state != VDEV_NEW && vdev_pre.vdev_state != VDEV_UNLOCKED && vdev_pre.vdev_state != VDEV_ERROR)
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.83.2.1 Failure condition ordering

```
[feat] < [rd_align, rd_bound, rd_gran_state, pdev_align, pdev_bound, pdev_gran_state, vdev_align, vdev_tracking, vdev_gran_state] [rd_gran_state, pdev_gran_state, vdev_gran_state] < [vdev_realm, vdev_pdev, vdev_state]
```

<!-- image -->

## B4.5.83.3 Success conditions

* gran_state
  * post: GranuleAt(vdev_ptr).state == GRAN_DELEGATED
* vdev_id_free
  * post: VdevIdIsFree(realm, vdev_pre.vdev_id)
* tdi_id_free
  * post: TdiIdIsFree(vdev_pre.tdi_id, pdev_pre.routing_id)
* realm_num_vdevs
  * post: realm.num_vdevs == realm_pre.num_vdevs - 1
* pdev_num_vdevs
  * post: pdev.num_vdevs == pdev_pre.num_vdevs - 1
* vsid_free
  * pre: vdev_pre.vsmmu == FEATURE_TRUE
  * post: VsidIsFree( VsmmuAt(vdev_pre.vsmmu_addr), vdev_pre.vsid)
* ste_state
  * post: st_walk.ste.state == PSMMU_ST_ENTRY_INVALID

## B4.5.83.4 Footprint

| ID                                             | Value                                                                      |
|------------------------------------------------|----------------------------------------------------------------------------|
| state realm_num_vdevs pdev_num_vdevs ste_state | GranuleAt(vdev_ptr).state realm.num_vdevs pdev.num_vdevs st_walk.ste.state |

