## B4.5.84 RMI\_VDEV\_GET\_INTERFACE\_REPORT command

Get VDEV interface report.

See also:

- A9.6.1 Realm retrieval of device attestation evidence

## B4.5.84.1 Interface

## B4.5.84.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC40001D0 |
| rd       | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV        |

## B4.5.84.1.2 Context

The RMI\_VDEV\_GET\_INTERFACE\_REPORT command operates on the following context.

| Name   | Type     | Value            | Before   | Description   |
|--------|----------|------------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd)      | false    | Realm         |
| pdev   | RmmPdev  | PdevAt(pdev_ptr) | false    | PDEV          |
| vdev   | RmmVdev  | VdevAt(vdev_ptr) | false    | VDEV          |

## B4.5.84.1.3 Output values


| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.84.2 Failure conditions

| ID       | Condition                                                                                |
|----------|------------------------------------------------------------------------------------------|
| feat     | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| rd_align | pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT                 |
| rd_bound | pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT                             |
| rd_state | pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT               |

ID

Condition

| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT     |
|-----------------|--------------|-------------------------------------------------------------------------|
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                 |
| pdev_gran_state | pre: post:   | GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT |
| vdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(vdev_ptr) result.status == RMI_ERROR_INPUT     |
| vdev_bound      | pre: post:   | !PaIsTracked(vdev_ptr) result.status == RMI_ERROR_INPUT                 |
| vdev_gran_state | pre: post:   | GranuleAt(vdev_ptr).state != GRAN_VDEV result.status == RMI_ERROR_INPUT |
| vdev_realm      | pre: post:   | vdev.realm != rd result.status == RMI_ERROR_INPUT                       |
| vdev_pdev       | pre: post:   | vdev.pdev != pdev_ptr result.status == RMI_ERROR_DEVICE                 |
| vdev_state      | pre:         | (vdev.vdev_state != VDEV_LOCKED && vdev.vdev_state != VDEV_STARTED)     |
| comm_state      | pre: post:   | vdev.comm_state != DEV_COMM_IDLE result.status == RMI_ERROR_DEVICE      |

```
pre: post: pre: post: B4.5.84.2.1 Failure condition ordering [rd_bound, rd_state, vdev_bound, vdev_gran_state] < [vdev_realm] [feat] < [rd_align, rd_bound, rd_state, pdev_align, pdev_bound, pdev_gran_state, vdev_align, vdev_bound, vdev_gran_state, vdev_realm] [vdev_gran_state] < [vdev_pdev, vdev_state, comm_state]
```

<!-- image -->

## B4.5.84.3 Success conditions

| ID         | Condition                                 |
|------------|-------------------------------------------|
| op         | post: vdev.op == VDEV_OP_GET_REPORT       |
| comm_state | post: vdev.comm_state == DEV_COMM_PENDING |

## B4.5.84.4 Footprint

| ID         | Value           |
|------------|-----------------|
| op         | vdev.op         |
| comm_state | vdev.comm_state |

<!-- image -->