## B4.5.30 RMI\_PDEV\_MEC\_REFRESH command

Propagate a MEC refresh to a CMEM device.

See also:

- A11.1.2 MEC and CMEM devices

## B4.5.30.1 Interface

## B4.5.30.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001ED |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV        |
| rd       | X2         | 63:0   | Address | PA of the RD          |

## B4.5.30.1.2 Context

The RMI\_PDEV\_MEC\_REFRESH command operates on the following context.

| Name   | Type     | Value            | Before   | Description   |
|--------|----------|------------------|----------|---------------|
| pdev   | RmmPdev  | PdevAt(pdev_ptr) | false    | PDEV          |
| realm  | RmmRealm | RealmAt(rd)      | false    | Realm         |

## B4.5.30.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.30.2 Failure conditions

## ID Condition

| feat            | pre: post:   | Rmm().static.feat_cmem_cxl != FEATURE_TRUE result.status == RMI_ERROR_NOT_SUPPORTED   |
|-----------------|--------------|---------------------------------------------------------------------------------------|
| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT                   |
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                               |
| pdev_gran_state | pre: post:   | GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT               |
| pdev_category   | pre: post:   | pdev.category != PDEV_ENDPOINT_CMEM result.status == RMI_ERROR_DEVICE                 |
| pdev_state      | pre: post:   | pdev.state != PDEV_READY result.status == RMI_ERROR_DEVICE                            |

## ID

## Condition

```
comm_state pre: pdev.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_DEVICE rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_tracking pre: !PaIsTrackedFine(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT realm_state pre: realm.state != REALM_ZOMBIE post: result.status == RMI_ERROR_REALM
```

## B4.5.30.2.1 Failure condition ordering

```
[feat] < [pdev_align, pdev_bound, pdev_gran_state, rd_align, rd_tracking, rd_state] [pdev_gran_state] < [pdev_category, pdev_state, comm_state] [rd_state] < [realm_state]
```

<!-- image -->


## B4.5.30.3 Success conditions

```
ID Condition op post: pdev.op == PDEV_OP_MEC_REFRESH comm_state post: pdev.comm_state == DEV_COMM_PENDING
```

## B4.5.30.4 Footprint

| ID         | Value           |
|------------|-----------------|
| op         | pdev.op         |
| comm_state | pdev.comm_state |