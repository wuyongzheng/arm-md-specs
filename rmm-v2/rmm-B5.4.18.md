## B5.4.18 RSI\_VDEV\_DMA\_ENABLE command

Enable DMA.

## B5.4.18.1

Interface

## B5.4.18.1.1 Input values

| Name          | Register   | Bits   | Type            | Description                                                                               |
|---------------|------------|--------|-----------------|-------------------------------------------------------------------------------------------|
| fid           | X0         | 63:0   | UInt64          | FID, value 0xC400019C                                                                     |
| vdev_id       | X1         | 63:0   | Bits64          | Realm device identifier                                                                   |
| flags         | X2         | 63:0   | RsiVdevDmaFlags | Flags                                                                                     |
| non_ats_plane | X3         | 63:0   | UInt64          | Index of Plane whose stage 2 permissions are observed by non-ATS requests from the device |
| lock_nonce    | X4         | 63:0   | UInt64          | Nonce generated on most recent transition to LOCKED state                                 |
| meas_nonce    | X5         | 63:0   | UInt64          | GET_MEASUREMENT request sequence number                                                   |
| report_nonce  | X6         | 63:0   | UInt64          | GET_INTERFACE_REPORT request sequence number                                              |

## B5.4.18.1.2 Context

The RSI\_VDEV\_DMA\_ENABLE command operates on the following context.

| Name   | Type     | Value                           | Before   | Description   |
|--------|----------|---------------------------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm()                  | false    | Current Realm |
| vdev   | RmmVdev  | VdevFromVdevId( realm, vdev_id) | false    | Realm device  |

DRAFT

## B5.4.18.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description    |
|--------|------------|--------|----------------------|----------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result |

## B5.4.18.2 Failure conditions

| ID      | Condition                                                          |
|---------|--------------------------------------------------------------------|
| da_en   | pre: realm.feat_da != FEATURE_TRUE post: result == RSI_ERROR_STATE |
| vdev_id | pre: VdevIdIsFree(realm, vdev_id) post: result == RSI_ERROR_INPUT  |

## ID

## Condition

```
non_ats_plane pre: (non_ats_plane == 0 || non_ats_plane > post: result == RSI_ERROR_INPUT attest_info pre: !VdevAttestInfoEqual( lock_nonce, meas_nonce, report_nonce, vdev.attest_info) post: result == RSI_ERROR_DEVICE vdev_state pre: vdev.vdev_state != VDEV_STARTED post: result == RSI_ERROR_DEVICE
```

```
realm.num_aux_planes)
```

## B5.4.18.2.1 Failure condition ordering

[da\_en] &lt; [vdev\_id, non\_ats\_plane]

<!-- image -->

## B5.4.18.3 Success conditions

```
ID Condition dma_state post: vdev.dma_state == VDEV_DMA_ENABLED non_ats_plane post: vdev.non_ats_plane == non_ats_plane
```

## B5.4.18.4 Footprint

The RSI\_VDEV\_DMA\_ENABLE command does not have any footprint.