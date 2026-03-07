## B4.5.82 RMI\_VDEV\_CREATE command

Create a VDEV.

The RMI\_VDEV\_CREATE command may initiate a Stateful RMI Operation.

The RMI\_VDEV\_CREATE command may initiate a memory-transferring RMI Operation.

## See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)
- [A9.4.2 Virtual device invariants](rmm-A9.4.md#a942-virtual-device-invariants)
- [B4.3.4 Object creation and destruction](rmm-B4.3.md#b434-object-creation-and-destruction)

## B4.5.82.1 Interface

## B4.5.82.1.1 Input values

| Name       | Register   | Bits   | Type    | Description           |
|------------|------------|--------|---------|-----------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000187 |
| rd         | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr   | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr   | X3         | 63:0   | Address | PA of the VDEV        |
| params_ptr | X4         | 63:0   | Address | PA of VDEV parameters |

## B4.5.82.1.2 Context

The RMI\_VDEV\_CREATE command operates on the following context.

| Name          | Type                                                    | Value                                                   | Before   | Description                              |
|---------------|---------------------------------------------------------|---------------------------------------------------------|----------|------------------------------------------|
| realm_pre     | RmmRealm                                                | RealmAt(rd)                                             | true     | Realm                                    |
| realm         | RmmRealm                                                | RealmAt(rd)                                             | false    | Realm                                    |
| pdev          | RmmPdev                                                 | PdevAt(pdev_ptr)                                        | false    | PDEV                                     |
| num_vdevs_pre | UInt64                                                  | pdev.num_vdevs                                          | true     | Number of VDEVs associated with the PDEV |
| vdev          | RmmVdev                                                 | VdevAt(vdev_ptr)                                        | false    | VDEV                                     |
| params        | RmiVdevParams                                           | RmiVdevParamsAt( params_ptr)                            | false    | VDEV parameters                          |
| stream_result | RmmPdevStreamResult                                     | PdevStreamFromType( pdev, PDEV_STREAM_NCOH)             | false    | Result of looking up PDEV stream         |
| psmmu         | RmmPsmmu                                                | PsmmuFromPdev(pdev)                                     | false    | PSMMU                                    |
| st_walk       | RmmPsmmuStWalkResult PsmmuStWalk( psmmu, VdevSid(vdev)) | RmmPsmmuStWalkResult PsmmuStWalk( psmmu, VdevSid(vdev)) | false    | Result of PSMMU Stream Table walk        |


ID

## B4.5.82.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.82.2 Failure conditions

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
* pdev_state
  * pre: pdev.state != PDEV_READY
  * post: result.status == RMI_ERROR_DEVICE
* pdev_category
  * pre: !pdev.category IN { PDEV_ENDPOINT_ACCEL_OFF_CHIP, PDEV_ENDPOINT_ACCEL_ON_CHIP }
  * post: result.status == RMI_ERROR_DEVICE
* pdev_streams
  * pre: PdevStreamsForVdev(pdev)
  * post: result.status == RMI_ERROR_DEVICE
* pdev_num_vdevs
  * pre: pdev.num_vdevs == pdev.
* max_num_vdevs
  * post: result.status == RMI_ERROR_DEVICE
* vdev_align
  * pre: !AddrIsRmiGranuleAligned(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_bound
  * pre: !PaIsDelegableConventionalFine(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_gran_state
  * pre: GranuleAt(vdev_ptr).state !=
  * post: result.status == RMI_ERROR_INPUT
* params_align
  * pre: !AddrIsRmiGranuleAligned(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_pas
  * pre: !NonSecureAccessPermitted(params_ptr)
  * post: result.status == RMI_ERROR_INPUT
* params_valid
  * pre: !RmiVdevParamsIsValid(params_ptr)
  * post: result.status == RMI_ERROR_INPUT GRAN_DELEGATED
* addr_range_valid
  * pre: !RmiAddrRangesValid8( params.addr_range, params.num_addr_range)
  * post: result.status == RMI_ERROR_INPUT
* da_en
  * pre: realm.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_REALM
* vdev_id_free
  * pre: !VdevIdIsFree(realm, params.vdev_id)
  * post: result.status == RMI_ERROR_INPUT
* tdi_id_free
  * pre: !TdiIdIsFree(params.tdi_id, pdev.routing_id)
  * post: result.status == RMI_ERROR_INPUT
* stream_exists
  * pre: stream_result.valid != RMM_TRUE
  * post: result.status == RMI_ERROR_INPUT
* tdi_id_bound
  * pre: (UInt(params.tdi_id) < UInt(pdev.rid_base) || UInt(params.tdi_id) >= UInt(pdev.rid_top))
  * post: result.status == RMI_ERROR_INPUT
* psmmu_st_l2
  * pre: (st_walk.level != 2 || st_walk.ste.state != PSMMU_ST_ENTRY_INVALID)
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_align
  * pre: (params.flags.VSMMU == RMI_FEATURE_TRUE && !AddrIsRmiGranuleAligned(params.vsmmu_addr))
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_bound
  * pre: (params.flags.VSMMU == RMI_FEATURE_TRUE && !PaIsTracked(params.vsmmu_addr))
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_state
  * pre: (params.flags.VSMMU == RMI_FEATURE_TRUE && GranuleAt(params.vsmmu_addr).state != GRAN_VSMMU)
  * post: result.status == RMI_ERROR_INPUT
* vsid_free
  * pre: (params.flags.VSMMU == RMI_FEATURE_TRUE && !VsidIsFree( VsmmuAt(params.vsmmu_addr), params.vsid))
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_compat
  * pre: (params.flags.VSMMU == RMI_FEATURE_TRUE && !PdevVsmmuIsCompatible( pdev, VsmmuAt(params.vsmmu_addr)))
  * post: result.status == RMI_ERROR_INPUT

## B4.5.82.2.1 Failure condition ordering

```
[feat] < [rd_align, rd_bound, pdev_bound, pdev_gran_state, vdev_align, vdev_bound, vdev_gran_state, params_align, params_pas, params_valid, vsmmu_align, vsmmu_bound, vsmmu_state, vsid_free] [feat] < [pdev_gran_state] [feat] < [rd_state] [pdev_gran_state, vsmmu_state] < [vsmmu_compat] [pdev_gran_state] < [pdev_category, pdev_state, pdev_num_vdevs, pdev_streams] [rd_state] < [da_en]
```

ID

<!-- image -->

## B4.5.82.3 Success conditions

* pdev_num_vdevs
  * post: pdev.num_vdevs == num_vdevs_pre + 1
* gran_state
  * post: GranuleAt(vdev_ptr).state == GRAN_VDEV
* vdev_id
  * post: vdev.vdev_id == params.vdev_id
* tdi_id
  * post: vdev.tdi_id == params.tdi_id
* pdev
  * post: vdev.pdev == pdev_ptr
* realm
  * post: vdev.realm == rd
* vdev_state
  * post: vdev.vdev_state == VDEV_NEW
* dma_state
  * post: vdev.dma_state == VDEV_DMA_DISABLED
* op
  * post: vdev.op == VDEV_OP_UNLOCK
* comm_state
  * post: vdev.comm_state == DEV_COMM_PENDING
* tdi_id_used
  * post: !TdiIdIsFree(params.tdi_id, pdev.routing_id)
* vsmmu
  * post: Equal(vdev.vsmmu, params.flags.VSMMU)
* vsmmu_addr
  * pre: params.flags.VSMMU == RMI_FEATURE_TRUE
  * post: vdev.vsmmu_addr == params.vsmmu_addr
* vsid
  * pre: params.flags.VSMMU == RMI_FEATURE_TRUE
  * post: vdev.vsid == params.vsid
* vsid_alloc
  * pre: params.flags.VSMMU == RMI_FEATURE_TRUE
  * post: !VsidIsFree( VsmmuAt(params.vsmmu_addr), params.vsid)
* realm_num_vdevs
  * post: realm.num_vdevs == realm_pre.num_vdevs + 1
* lock_nonce
  * post: vdev.attest_info.lock_nonce == 0
* meas_nonce
  * post: vdev.attest_info.meas_nonce == 0
* report_nonce
  * post: vdev.attest_info.report_nonce == 0
* p2p_bound
  * post: vdev.p2p_bound == FEATURE_FALSE
* num_addr_range
  * post: vdev.num_addr_range == params.num_addr_range
* addr_range
  * post: RmiAddrRangesEqual8( vdev.addr_range, params.addr_range, params.num_addr_range)
* ste_state
  * post: st_walk.ste.state == PSMMU_ST_ENTRY_VALID

## B4.5.82.4 Footprint

| ID              | Value                     |
|-----------------|---------------------------|
| state           | GranuleAt(vdev_ptr).state |
| pdev_num_vdevs  | pdev.num_vdevs            |
| realm_num_vdevs | realm.num_vdevs           |
| ste_state       | st_walk.ste.state         |

<!-- image -->