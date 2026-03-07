## B4.5.89 RMI\_VDEV\_P2P\_UNBIND command

Remove a P2P binding between two VDEVs.

See also:

- [A9.10 Peer-to-peer device communication](rmm-A9.10.md)

## B4.5.89.1 Interface

## B4.5.89.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                  |
|------------|------------|--------|---------|------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001D5        |
| rd         | X1         | 63:0   | Address | PA of the RD                 |
| pdev_1_ptr | X2         | 63:0   | Address | PA of the first PDEV object  |
| pdev_2_ptr | X3         | 63:0   | Address | PA of the second PDEV object |
| stream_hnd | X4         | 63:0   | Bits64  | Stream handle                |
| vdev_1_ptr | X5         | 63:0   | Address | PA of the first VDEV object  |
| vdev_2_ptr | X6         | 63:0   | Address | PA of the second VDEV object |

## B4.5.89.1.2 Context

The RMI\_VDEV\_P2P\_UNBIND command operates on the following context.

| Name          | Type                | Value                                             | Before   | Description                      |
|---------------|---------------------|---------------------------------------------------|----------|----------------------------------|
| realm         | RmmRealm            | RealmAt(rd)                                       | false    | Realm                            |
| pdev_1        | RmmPdev             | PdevAt(pdev_1_ptr)                                | false    | First PDEV                       |
| pdev_2        | RmmPdev             | PdevAt(pdev_2_ptr)                                | false    | Second PDEV                      |
| stream_result | RmmPdevStreamResult | PdevStreamFromHandle( pdev_1, pdev_2, stream_hnd) | false    | Result of looking up PDEV stream |
| stream        | RmmPdevStream       | stream_result.stream                              | false    | PDEV stream                      |
| vdev_1        | RmmVdev             | VdevAt(vdev_1_ptr)                                | false    | First VDEV                       |
| vdev_2        | RmmVdev             | VdevAt(vdev_2_ptr)                                | false    | Second VDEV                      |


## B4.5.89.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.89.2 Failure conditions

* vdev_2_gran_state
  * pre: GranuleAt(vdev_2_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_2_realm
  * pre: vdev_2.realm != rd
  * post: result.status == RMI_ERROR_INPUT
* vdev_2_pdev
  * pre: vdev_2.pdev != pdev_2_ptr
  * post: result.status == RMI_ERROR_INPUT
* vdev_2_state
  * pre: vdev_2.vdev_state != VDEV_STARTED
  * post: result.status == RMI_ERROR_DEVICE
* vdev_2_comm
  * pre: vdev_2.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE
* vdev_2_p2p_bound
  * pre: vdev_2.p2p_bound != FEATURE_TRUE
  * post: result.status == RMI_ERROR_DEVICE
* vdev_2_p2p_peer
  * pre: vdev_2.p2p_peer != vdev_1.vdev_id
  * post: result.status == RMI_ERROR_DEVICE
* feat
  * pre: Rmm().static.feat_p2p != FEATURE_TRUE
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
* stream_valid
  * pre: stream_result.valid != RMM_TRUE
  * post: result.status == RMI_ERROR_INPUT
* stream_type
  * pre: stream.stream_type != PDEV_STREAM_NCOH_P2P
  * post: result.status == RMI_ERROR_INPUT
* pdev_1_align
  * pre: !AddrIsRmiGranuleAligned(pdev_1_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_1_bound
  * pre: !PaIsTracked(pdev_1_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_1_gran_state
  * pre: GranuleAt(pdev_1_ptr).state != GRAN_PDEV
  * post: result.status == RMI_ERROR_INPUT
* pdev_2_align
  * pre: !AddrIsRmiGranuleAligned(pdev_2_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_2_bound
  * pre: !PaIsTracked(pdev_2_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_2_gran_state
  * pre: GranuleAt(pdev_2_ptr).state != GRAN_PDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_align
  * pre: !AddrIsRmiGranuleAligned(vdev_1_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_bound
  * pre: !PaIsTracked(vdev_1_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_gran_state
  * pre: GranuleAt(vdev_1_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_realm
  * pre: vdev_1.realm !=
* rd
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_pdev
  * pre: vdev_1.pdev !=
* pdev_1_ptr
  * post: result.status == RMI_ERROR_INPUT
* vdev_1_state
  * pre: vdev_1.vdev_state != VDEV_STARTED
  * post: result.status == RMI_ERROR_DEVICE
* vdev_1_comm
  * pre: vdev_1.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE
* vdev_1_p2p_bound
  * pre: vdev_1.p2p_bound != FEATURE_TRUE
  * post: result.status == RMI_ERROR_DEVICE
* vdev_1_p2p_peer
  * pre: vdev_1.p2p_peer != vdev_2.
* vdev_id
  * post: result.status == RMI_ERROR_DEVICE
* vdev_2_align
  * pre: !AddrIsRmiGranuleAligned(vdev_2_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_2_bound
  * pre: !PaIsTracked(vdev_2_ptr)
  * post: result.status == RMI_ERROR_INPUT

## B4.5.89.2.1 Failure condition ordering

vdev\_2\_realm

## [feat] &lt; [rd\_align, rd\_bound, rd\_state, pdev\_1\_align, pdev\_1\_bound, pdev\_1\_gran\_state, pdev\_2\_align, pdev\_2\_bound, pdev\_2\_gran\_state, vdev\_1\_align, vdev\_1\_bound, vdev\_1\_gran\_state, vdev\_1\_realm, vdev\_1\_pdev, vdev\_1\_state, vdev\_1\_comm, vdev\_1\_p2p\_bound, vdev\_1\_p2p\_peer, vdev\_2\_align, vdev\_2\_bound, vdev\_2\_gran\_state, vdev\_2\_realm, vdev\_2\_pdev, vdev\_2\_state, vdev\_2\_comm, vdev\_2\_p2p\_bound, vdev\_2\_p2p\_peer] vdev\_2\_pdev vdev\_2\_state vdev\_2\_comm vdev\_2\_p2p\_bound vdev\_2\_p2p\_peer
## B4.5.89.3 Success conditions

* vdev_1_op
  * post: vdev_1.op == VDEV_OP_P2P_UNBIND
* vdev_1_comm
  * post: vdev_1.comm_state == DEV_COMM_PENDING
* vdev_1_p2p_bound
  * post: vdev_1.p2p_bound == FEATURE_FALSE
* vdev_2_op
  * post: vdev_2.op == VDEV_OP_P2P_UNBIND
* vdev_2_comm
  * post: vdev_2.comm_state == DEV_COMM_PENDING
* vdev_2_p2p_bound
  * post: vdev_2.p2p_bound == FEATURE_FALSE

## B4.5.89.4 Footprint

## Value

## ID

vdev\_1\_op

vdev\_1.op

vdev\_1\_comm

vdev\_1.comm\_state

stream\_valid stream\_type

| ID               | Value             |
|------------------|-------------------|
| vdev_1_p2p_bound | vdev_1.p2p_bound  |
| vdev_2_op        | vdev_2.op         |
| vdev_2_comm      | vdev_2.comm_state |
| vdev_2_p2p_bound | vdev_2.p2p_bound  |

<!-- image -->