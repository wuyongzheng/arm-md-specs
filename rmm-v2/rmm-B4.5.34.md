## B4.5.34 RMI\_PDEV\_STREAM\_CONNECT command

Initiate connection of a PDEV stream.

See also:

- A9.3 Physical device stream object

## B4.5.34.1 Interface

## B4.5.34.1.1 Input values

| Name       | Register   | Bits   | Type    | Description                  |
|------------|------------|--------|---------|------------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC4000204        |
| params_ptr | X1         | 63:0   | Address | PA of PDEV stream parameters |

## B4.5.34.1.2 Context

The RMI\_PDEV\_STREAM\_CONNECT command operates on the following context.

| Name          | Type                | Value                                  | Before   | Description                      |
|---------------|---------------------|----------------------------------------|----------|----------------------------------|
| params        | RmiPdevStreamParams | RmiPdevStreamParamsAt( params_ptr)     | false    | Parameters                       |
| pdev_1        | RmmPdev             | PdevAt(params.pdev_1)                  | false    | First PDEV object                |
| pdev_2        | RmmPdev             | PdevAt(params.pdev_2)                  | false    | Second PDEV object               |
| stream_result | RmmPdevStreamResult  PdevStreamAlloc( pdev_1, pdev_2) | false    | Result of allocating PDEV stream |
| stream        | RmmPdevStream       | stream_result.stream                   | false    | PDEV stream                      |

## B4.5.34.1.3 Output values

| Name       | Register   | Bits   | Type      | Description        |
|------------|------------|--------|-----------|--------------------|
| result     | X0         | 63:0   | RmiResult | Command result     |
| stream_hnd | X1         | 63:0   | Bits64    | PDEV stream handle |

## B4.5.34.2 Failure conditions

| ID           | Condition                                                                                |
|--------------|------------------------------------------------------------------------------------------|
| feat_da      | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| params_align | pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT         |
| params_pas   | pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT        |

## ID

## Condition

```
params_valid pre: !RmiPdevStreamParamsIsValid(params_ptr) post: result.status == RMI_ERROR_INPUT feat_non_tee_st ream pre: (params.stream_type == RMI_PDEV_STREAM_NON_TEE && Rmm().static.feat_non_tee_stream != FEATURE_TRUE) post: result.status == RMI_ERROR_NOT_SUPPORTED pdev_1_align pre: !AddrIsRmiGranuleAligned(params.pdev_1) post: result.status == RMI_ERROR_INPUT pdev_1_bound pre: !PaIsTracked(params.pdev_1) post: result.status == RMI_ERROR_INPUT pdev_1_gran_sta te pre: GranuleAt(params.pdev_1).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT pdev_1_category pre: !pdev_1.category IN { PDEV_ENDPOINT_ACCEL_OFF_CHIP, PDEV_ENDPOINT_ACCEL_ON_CHIP, PDEV_ENDPOINT_CMEM } post: result.status == RMI_ERROR_INPUT pdev_1_state pre: pdev_1.state != PDEV_READY post: result.status == RMI_ERROR_INPUT pdev_1_op pre: pdev_1.op != PDEV_OP_NONE post: result.status == RMI_ERROR_INPUT pdev_1_comm_sta te pre: pdev_1.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_INPUT pdev_2_align pre: (PdevStreamPdev2Required(params.stream_type) && !AddrIsRmiGranuleAligned(params.pdev_2)) post: result.status == RMI_ERROR_INPUT pdev_2_bound pre: (PdevStreamPdev2Required(params.stream_type) && !PaIsTracked(params.pdev_2)) post: result.status == RMI_ERROR_INPUT pdev_2_gran_sta te pre: (PdevStreamPdev2Required(params.stream_type) && GranuleAt(params.pdev_2).state != GRAN_PDEV) post: result.status == RMI_ERROR_INPUT pdev_2_category pre: (PdevStreamPdev2Required(params.stream_type) && pdev_2.category != PdevStreamPdev2Category(params.stream_type)) post: result.status == RMI_ERROR_INPUT pdev_2_state pre: (PdevStreamPdev2Required(params.stream_type) && pdev_2.state != PDEV_READY) post: result.status == RMI_ERROR_INPUT pdev_2_op pre: (PdevStreamPdev2Required(params.stream_type) && pdev_2.op != PDEV_OP_NONE) post: result.status == RMI_ERROR_INPUT pdev_2_comm_sta te pre: (PdevStreamPdev2Required(params.stream_type) && pdev_2.comm_state != DEV_COMM_IDLE) post: result.status == RMI_ERROR_INPUT disconnected pre: stream.state != PDEV_STREAM_DISCONNECTED post: result.status == RMI_ERROR_INPUT
```

ID

## Condition

```
stream_type_exi sts pre: PdevStreamFromType( pdev_1, PdevStreamTypeFromRmi( params.stream_type)).valid == RMM_TRUE post: result.status == RMI_ERROR_INPUT stream_alloc_fa iled pre: stream_result.valid != RMM_TRUE post: result.status == RMI_ERROR_INPUT
```

## B4.5.34.2.1 Failure condition ordering

The RMI\_PDEV\_STREAM\_CONNECT command does not have any failure condition orderings.

## B4.5.34.3 Success conditions

## Condition

ID

```
stream_hnd post: stream_hnd == stream.handle pdev_1_op post: pdev_1.op == PDEV_OP_CONNECT pdev_1_comm_state post: pdev_1.comm_state == DEV_COMM_PENDING pdev_2_op pre: PdevStreamPdev2Required(params.stream_type) post: pdev_2.op == PDEV_OP_CONNECT pdev_2_comm_state pre: PdevStreamPdev2Required(params.stream_type) post: pdev_2.comm_state == DEV_COMM_PENDING state post: stream.state == PDEV_STREAM_CONNECTING stream_type post: Equal(stream.stream_type, params.stream_type) ide_sid post: stream.ide_sid == params.ide_sid num_addr_range post: stream.num_addr_range == params.num_addr_range addr_range post: RmiAddrRangesEqual16( stream.addr_range, params.addr_range, params.num_addr_range)
```

## B4.5.34.4 Footprint

The RMI\_PDEV\_STREAM\_CONNECT command does not have any footprint.