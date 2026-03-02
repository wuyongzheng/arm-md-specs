## B4.5.85 RMI\_VDEV\_GET\_MEASUREMENTS command

Get VDEV measurements.

See also:

- A9.6.1 Realm retrieval of device attestation evidence

## B4.5.85.1 Interface

## B4.5.85.1.1 Input values

| Name       | Register   | Bits   | Type    | Description           |
|------------|------------|--------|---------|-----------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001D1 |
| rd         | X1         | 63:0   | Address | PA of the RD          |
| pdev_ptr   | X2         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr   | X3         | 63:0   | Address | PA of the VDEV        |
| params_ptr | X4         | 63:0   | Address | PA of VDEV parameters |

- DRAFT If pdev.spdm == true and the device supports signed measurement, then: · The final SPDM GET\_MEASUREMENTS request issued by the RMM in reponse to this command includes a request for a signature. · The RMM first requests the Host to cache the request, and then requests the Host to cache the response. As a result, Host concatenates the request and the response within its cache. The cached data in turn includes any opaque data, and the signature. B4.5.85.1.2 Context The RMI\_VDEV\_GET\_MEASUREMENTS command operates on the following context.

| Name   | Type                                                     | Value                                                    | Before   | Description            |
|--------|----------------------------------------------------------|----------------------------------------------------------|----------|------------------------|
| realm  | RmmRealm                                                 | RealmAt(rd)                                              | false    | Realm                  |
| pdev   | RmmPdev                                                  | PdevAt(pdev_ptr)                                         | false    | PDEV                   |
| vdev   | RmmVdev                                                  | VdevAt(vdev_ptr)                                         | false    | VDEV                   |
| params | RmiVdevMeasureParams RmiVdevMeasureParamsAt( params_ptr) | RmiVdevMeasureParams RmiVdevMeasureParamsAt( params_ptr) | false    | Measurement parameters |

## B4.5.85.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.85.2 Failure conditions

RTJPLJ

ID

## Condition

```
DRAFT feat pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT pdev_align pre: !AddrIsRmiGranuleAligned(pdev_ptr) post: result.status == RMI_ERROR_INPUT pdev_bound pre: !PaIsTracked(pdev_ptr) post: result.status == RMI_ERROR_INPUT pdev_gran_state pre: GranuleAt(pdev_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT vdev_align pre: !AddrIsRmiGranuleAligned(vdev_ptr) post: result.status == RMI_ERROR_INPUT vdev_bound pre: !PaIsTracked(vdev_ptr) post: result.status == RMI_ERROR_INPUT vdev_gran_state pre: GranuleAt(vdev_ptr).state != GRAN_VDEV post: result.status == RMI_ERROR_INPUT vdev_realm pre: vdev.realm != rd post: result.status == RMI_ERROR_INPUT vdev_pdev pre: vdev.pdev != pdev_ptr post: result.status == RMI_ERROR_DEVICE comm_state pre: vdev.comm_state != DEV_COMM_IDLE post: result.status == RMI_ERROR_DEVICE params_align pre: !AddrIsRmiGranuleAligned(params_ptr) post: result.status == RMI_ERROR_INPUT params_pas pre: !NonSecureAccessPermitted(params_ptr) post: result.status == RMI_ERROR_INPUT
```

## B4.5.85.2.1 Failure condition ordering

```
[rd_bound, rd_state, vdev_bound, vdev_gran_state] < [vdev_realm] [feat] < [rd_align, rd_bound, rd_state, pdev_align, pdev_bound, pdev_gran_state, vdev_align, vdev_bound, vdev_gran_state, vdev_realm, params_align, params_pas] [vdev_gran_state] < [vdev_pdev, comm_state]
```

feat

<!-- image -->

## B4.5.85.3 Success conditions

| ID         | Condition                                 |
|------------|-------------------------------------------|
| op         | post: vdev.op == VDEV_OP_GET_MEAS         |
| comm_state | post: vdev.comm_state == DEV_COMM_PENDING |
| B4.5.85.4  | Footprint                                 |
| ID         | Value                                     |
| op         | vdev.op                                   |
| comm_state | vdev.comm_state                           |

<!-- image -->