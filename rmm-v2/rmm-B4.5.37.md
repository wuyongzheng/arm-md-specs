## B4.5.37 RMI\_PDEV\_STREAM\_KEY\_REFRESH command

Initiate key refresh of a PDEV stream.

See also:

- A9.3 Physical device stream object

## B4.5.37.1 Interface

## B4.5.37.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                  |
|------------|------------|--------|---------|------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC400017A        |
| pdev_1_ptr | X1         | 63:0   | Address | PA of the first PDEV object  |
| pdev_2_ptr | X2         | 63:0   | Address | PA of the second PDEV object |
| stream_hnd | X3         | 63:0   | Bits64  | Stream handle                |

## B4.5.37.1.2 Context

The RMI\_PDEV\_STREAM\_KEY\_REFRESH command operates on the following context.

| Name          | Type Value                                                | Before   | Description                      |
|---------------|-----------------------------------------------------------|----------|----------------------------------|
| pdev_1        | RmmPdev PdevAt(pdev_1_ptr)                                | false    | First PDEV object                |
| pdev_2        | RmmPdev PdevAt(pdev_2_ptr)                                | false    | Second PDEV object               |
| stream_result | RmmPdevStreamResult PdevStreamFromHandle( pdev_1, pdev_2, | false    | Result of looking up PDEV stream |
| stream        | RmmPdevStream stream_result.stream                        | false    | PDEV stream                      |


## B4.5.37.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.37.2 Failure conditions

## ID Condition

```
feat pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED stream_valid pre: stream_result.valid != RMM_TRUE post: result.status == RMI_ERROR_INPUT stream_type pre: (stream.stream_type == PDEV_STREAM_NCOH_SYS || stream.stream_type == PDEV_STREAM_COH_SYS) post: result.status == RMI_ERROR_DEVICE
```

## ID

## Condition

```
stream_state pre: stream.state != PDEV_STREAM_CONNECTED post: result.status == RMI_ERROR_DEVICE pdev_1_align pre: !AddrIsRmiGranuleAligned(pdev_1_ptr) post: result.status == RMI_ERROR_INPUT pdev_1_bound pre: !PaIsTracked(pdev_1_ptr) post: result.status == RMI_ERROR_INPUT pdev_1_gran_sta te pre: GranuleAt(pdev_1_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT pdev_1_state pre: pdev_1.state != PDEV_READY post: result.status == RMI_ERROR_INPUT pdev_1_op pre: pdev_1.op != PDEV_OP_NONE post: result.status == RMI_ERROR_INPUT pdev_1_comm_sta te pre: pdev_1.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_INPUT pdev_1_p2p pre: (stream.stream_type == PDEV_STREAM_NCOH_P2P && PdevStreamFromType( pdev_1, PDEV_STREAM_NCOH).valid != RMM_TRUE) post: result.status == RMI_ERROR_INPUT pdev_2_align pre: (PdevStreamPdev2Required(stream.stream_type) && !AddrIsRmiGranuleAligned(pdev_2_ptr)) post: result.status == RMI_ERROR_INPUT pdev_2_bound pre: (PdevStreamPdev2Required(stream.stream_type) && !PaIsTracked(pdev_2_ptr)) post: result.status == RMI_ERROR_INPUT pdev_2_gran_sta te pre: (PdevStreamPdev2Required(stream.stream_type) && GranuleAt(pdev_2_ptr).state != GRAN_PDEV) post: result.status == RMI_ERROR_INPUT pdev_2_state pre: (PdevStreamPdev2Required(stream.stream_type) && pdev_2.state != PDEV_READY) post: result.status == RMI_ERROR_INPUT pdev_2_op pre: (PdevStreamPdev2Required(stream.stream_type) && pdev_2.op != PDEV_OP_NONE) post: result.status == RMI_ERROR_INPUT pdev_2_comm_sta te pre: (PdevStreamPdev2Required(stream.stream_type) && pdev_2.comm_state != DEV_COMM_IDLE) post: result.status == RMI_ERROR_INPUT pdev_2_p2p pre: (PdevStreamPdev2Required(stream.stream_type) && stream.stream_type == PDEV_STREAM_NCOH_P2P && PdevStreamFromType( pdev_2, PDEV_STREAM_NCOH).valid != RMM_TRUE) post: result.status == RMI_ERROR_INPUT
```

## B4.5.37.2.1 Failure condition ordering

The RMI\_PDEV\_STREAM\_KEY\_REFRESH command does not have any failure condition orderings.

## B4.5.37.3 Success conditions

| ID                | Condition                                                                                    |
|-------------------|----------------------------------------------------------------------------------------------|
| state             | post: stream.state == PDEV_STREAM_KEY_REFRESHING                                             |
| pdev_1_op         | post: pdev_1.op == PDEV_OP_KEY_REFRESH                                                       |
| pdev_1_comm_state | post: pdev_1.comm_state == DEV_COMM_PENDING                                                  |
| pdev_2_op         | pre: PdevStreamPdev2Required(stream.stream_type) post: pdev_2.op == PDEV_OP_KEY_REFRESH      |
| pdev_2_comm_state | pre: PdevStreamPdev2Required(stream.stream_type) post: pdev_2.comm_state == DEV_COMM_PENDING |

## B4.5.37.4 Footprint

The RMI\_PDEV\_STREAM\_KEY\_REFRESH command does not have any footprint.

<!-- image -->