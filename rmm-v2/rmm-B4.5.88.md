## B4.5.88 RMI\_VDEV\_P2P\_BIND command

Create a P2P binding between two VDEVs.

See also:

- A9.10 Peer-to-peer device communication

## B4.5.88.1 Interface

## B4.5.88.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                  |
|------------|------------|--------|---------|------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001D4        |
| rd         | X1         | 63:0   | Address | PA of the RD                 |
| rec_ptr    | X2         | 63:0   | Address | PA of the target REC         |
| pdev_1_ptr | X3         | 63:0   | Address | PA of the first PDEV object  |
| stream_hnd | X4         | 63:0   | Bits64  | Stream handle                |
| pdev_2_ptr | X5         | 63:0   | Address | PA of the second PDEV object |
| vdev_1_ptr | X6         | 63:0   | Address | PA of the first VDEV object  |
| vdev_2_ptr | X7         | 63:0   | Address | PA of the second VDEV object |

## B4.5.88.1.2 Context

The RMI\_VDEV\_P2P\_BIND command operates on the following context.

| Name          | Type                | Value                                             | Before   | Description                      |
|---------------|---------------------|---------------------------------------------------|----------|----------------------------------|
| realm         | RmmRealm            | RealmAt(rd)                                       | false    | Realm                            |
| rec           | RmmRec              | RecAt(rec_ptr)                                    | false    | REC                              |
| pdev_1        | RmmPdev             | PdevAt(pdev_1_ptr)                                | false    | First PDEV                       |
| pdev_2        | RmmPdev             | PdevAt(pdev_2_ptr)                                | false    | Second PDEV                      |
| stream_result | RmmPdevStreamResult | PdevStreamFromHandle( pdev_1, pdev_2, stream_hnd) | false    | Result of looking up PDEV stream |
| stream        | RmmPdevStream       | stream_result.stream                              | false    | PDEV stream                      |
| vdev_1        | RmmVdev             | VdevAt(vdev_1_ptr)                                | false    | First VDEV                       |
| vdev_2        | RmmVdev             | VdevAt(vdev_2_ptr)                                | false    | Second VDEV                      |

DRAFT

## B4.5.88.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## ID

## B4.5.88.2 Failure conditions

## Condition

```
DRAFT feat pre: Rmm().static.feat_p2p != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT rec_align pre: !AddrIsRmiGranuleAligned(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_bound pre: !PaIsTracked(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_gran_state pre: GranuleAt(rec_ptr).state != GRAN_REC post: result.status == RMI_ERROR_INPUT rec_state pre: rec.state == REC_RUNNING post: result.status == RMI_ERROR_REC rec_owner pre: rec.owner != rd post: result.status == RMI_ERROR_REC stream_valid pre: stream_result.valid != RMM_TRUE post: result.status == RMI_ERROR_INPUT stream_type pre: stream.stream_type != PDEV_STREAM_NCOH_P2P post: result.status == RMI_ERROR_INPUT pdev_1_align pre: !AddrIsRmiGranuleAligned(pdev_1_ptr) post: result.status == RMI_ERROR_INPUT pdev_1_bound pre: !PaIsTracked(pdev_1_ptr) post: result.status == RMI_ERROR_INPUT pdev_1_gran_sta te pre: GranuleAt(pdev_1_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT pdev_2_align pre: !AddrIsRmiGranuleAligned(pdev_2_ptr) post: result.status == RMI_ERROR_INPUT pdev_2_bound pre: !PaIsTracked(pdev_2_ptr) post: result.status == RMI_ERROR_INPUT pdev_2_gran_sta te pre: GranuleAt(pdev_2_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT vdev_1_align pre: !AddrIsRmiGranuleAligned(vdev_1_ptr) post: result.status == RMI_ERROR_INPUT vdev_1_bound pre: !PaIsTracked(vdev_1_ptr) post: result.status == RMI_ERROR_INPUT vdev_1_gran_sta te pre: GranuleAt(vdev_1_ptr).state != GRAN_VDEV post: result.status == RMI_ERROR_INPUT vdev_1_realm pre: vdev_1.realm != rd post: result.status == RMI_ERROR_INPUT vdev_1_pdev pre: vdev_1.pdev != pdev_1_ptr post: result.status == RMI_ERROR_INPUT vdev_1_state pre: vdev_1.vdev_state != VDEV_STARTED post: result.status == RMI_ERROR_DEVICE
```

## ID

## Condition

```
DRAFT vdev_1_comm pre: vdev_1.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_DEVICE vdev_1_attest_i nfo pre: !VdevAttestInfoEqual( vdev_1.attest_info, rec.vdev_attest_info_1) post: result.status == RMI_ERROR_DEVICE vdev_1_p2p_boun d pre: vdev_1.p2p_bound != FEATURE_FALSE post: result.status == RMI_ERROR_DEVICE vdev_2_align pre: !AddrIsRmiGranuleAligned(vdev_2_ptr) post: result.status == RMI_ERROR_INPUT vdev_2_bound pre: !PaIsTracked(vdev_2_ptr) post: result.status == RMI_ERROR_INPUT vdev_2_gran_sta te pre: GranuleAt(vdev_2_ptr).state != GRAN_VDEV post: result.status == RMI_ERROR_INPUT vdev_2_realm pre: vdev_2.realm != rd post: result.status == RMI_ERROR_INPUT vdev_2_pdev pre: vdev_2.pdev != pdev_2_ptr post: result.status == RMI_ERROR_INPUT vdev_2_state pre: vdev_2.vdev_state != VDEV_STARTED post: result.status == RMI_ERROR_DEVICE vdev_2_comm pre: vdev_2.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_DEVICE vdev_2_attest_i nfo pre: !VdevAttestInfoEqual( vdev_2.attest_info, rec.vdev_attest_info_2) post: result.status == RMI_ERROR_DEVICE vdev_2_p2p_boun d pre: vdev_2.p2p_bound != FEATURE_FALSE post: result.status == RMI_ERROR_DEVICE
```

## B4.5.88.2.1 Failure condition ordering

```
[feat] < [rd_align, rd_bound, rd_state, rec_bound, rec_gran_state, rec_state, rec_owner, pdev_1_align, pdev_1_bound, pdev_1_gran_state, pdev_2_align, pdev_2_bound, pdev_2_gran_state, vdev_1_align, vdev_1_bound, vdev_1_gran_state, vdev_1_realm, vdev_1_pdev, vdev_1_state, vdev_1_comm, vdev_1_attest_info, vdev_1_p2p_bound, vdev_2_align, vdev_2_bound, vdev_2_gran_state, vdev_2_realm, vdev_2_pdev, vdev_2_state, vdev_2_comm, vdev_2_attest_info, vdev_2_p2p_bound]
```

## ID

feat rd\_align rd\_bound rd\_state rec\_bound rec\_gran\_state rec\_state rec\_owner pdev\_1\_align pdev\_1\_bound pdev\_1\_gran\_state pdev\_2\_align pdev\_2\_bound pdev\_2\_gran\_state vdev\_1\_align vdev\_1\_bound vdev\_1\_gran\_state vdev\_1\_realm vdev\_1\_pdev vdev\_1\_state vdev\_1\_comm vdev\_1\_at est\_info vdev\_1\_p2p\_bound vdev\_2\_align vdev\_2\_bound vdev\_2\_gran\_state vdev\_2\_realm vdev\_2\_pdev vdev\_2\_state vdev\_2\_comm vdev\_2\_at est\_info vdev\_2\_p2p\_bound

## B4.5.88.3 Success conditions

## Condition

```
vdev_1_op post: vdev_1.op == VDEV_OP_P2P_BIND vdev_1_comm post: vdev_1.comm_state == DEV_COMM_PENDING
```

rec\_align stream\_valid

stream\_type

| ID               | Condition                                   |
|------------------|---------------------------------------------|
| vdev_1_p2p_bound | post: vdev_1.p2p_bound == FEATURE_TRUE      |
| vdev_1_p2p_peer  | post: vdev_1.p2p_peer == vdev_2.vdev_id     |
| vdev_2_op        | post: vdev_2.op == VDEV_OP_P2P_BIND         |
| vdev_2_comm      | post: vdev_2.comm_state == DEV_COMM_PENDING |
| vdev_2_p2p_bound | post: vdev_2.p2p_bound == FEATURE_TRUE      |
| vdev_2_p2p_peer  | post: vdev_2.p2p_peer == vdev_1.vdev_id     |

## B4.5.88.4 Footprint

| ID                                                                                                                                                | Value                                                                                                                                                               |
|---------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| vdev_1_op vdev_1_comm vdev_1_p2p_bound vdev_1_p2p_stream vdev_1_p2p_peer vdev_2_op vdev_2_comm vdev_2_p2p_bound vdev_2_p2p_stream vdev_2_p2p_peer | DRAFT vdev_1.op vdev_1.comm_state vdev_1.p2p_bound vdev_1.p2p_stream vdev_1.p2p_peer vdev_2.op vdev_2.comm_state vdev_2.p2p_bound vdev_2.p2p_stream vdev_2.p2p_peer |