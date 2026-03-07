## B4.5.80 RMI\_VDEV\_COMMUNICATE command

Perform device communication associated with a VDEV.

See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)

## B4.5.80.1 Interface

## B4.5.80.1.1 Input values

| Name     | Register   | Bits   | Type    | Description                            |
|----------|------------|--------|---------|----------------------------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000186                  |
| rd       | X1         | 63:0   | Address | PA of the RD                           |
| pdev_ptr | X2         | 63:0   | Address | PA of the PDEV                         |
| vdev_ptr | X3         | 63:0   | Address | PA of the VDEV                         |
| data_ptr | X4         | 63:0   | Address | PA of the communication data structure |

An implementation may store state in a PDEV object which is required for communication with the child VDEVs. For this reason, and to simplify locking of PDEV and VDEV objects which may be performed by the implementation, a PDEV pointer is passed to RMI\_VDEV\_COMMUNICATE. B4.5.80.1.2 Context The RMI\_VDEV\_COMMUNICATE command operates on the following context.

| Name     | Type           | Value                      | Before   | Description                 |
|----------|----------------|----------------------------|----------|-----------------------------|
| rmm      | RmmGlobal      | Rmm()                      | false    | RMMglobal state             |
| realm    | RmmRealm       | RealmAt(rd)                | false    | Realm                       |
| pdev     | RmmPdev        | PdevAt(pdev_ptr)           | false    | PDEV                        |
| vdev_pre | RmmVdev        | VdevAt(vdev_ptr)           | true     | VDEV                        |
| vdev     | RmmVdev        | VdevAt(vdev_ptr)           | false    | VDEV                        |
| data     | RmiDevCommData | RmiDevCommDataAt(data_ptr) | false    | Device communication object |

## B4.5.80.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.80.2 Failure conditions

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
* vdev_align
  * pre: !AddrIsRmiGranuleAligned(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_bound
  * pre: !PaIsTracked(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_gran_state
  * pre: GranuleAt(vdev_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* vdev_realm
  * pre: vdev.realm !=
* rd
  * post: result.status == RMI_ERROR_INPUT
* data_align
  * pre: !AddrIsRmiGranuleAligned(data_ptr)
  * post: result.status == RMI_ERROR_INPUT
* data_pas
  * pre: !NonSecureAccessPermitted(data_ptr)
  * post: result.status == RMI_ERROR_INPUT
* req_align
  * pre: !AddrIsRmiGranuleAligned(data.enter.req_addr)
  * post: result.status == RMI_ERROR_INPUT
* req_pas
  * pre: !NonSecureAccessPermitted(data.enter.req_addr)
  * post: result.status == RMI_ERROR_INPUT
* resp_align
  * pre: !AddrIsRmiGranuleAligned(data.enter.rsp_addr)
  * post: result.status == RMI_ERROR_INPUT
* resp_pas
  * pre: !NonSecureAccessPermitted(data.enter.rsp_addr)
  * post: result.status == RMI_ERROR_INPUT
* rsp_len
  * pre: data.enter.rsp_len > rmm.dynamic.
* rmi_granule_size
  * post: result.status == RMI_ERROR_INPUT
* vdev_pdev
  * pre: vdev.pdev !=
* pdev_ptr
  * post: result.status == RMI_ERROR_DEVICE
* comm_state
  * pre: vdev.comm_state == DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE
* busy
  * pre: PdevIsBusy(pdev)
  * post: result.status == RMI_BUSY

## B4.5.80.2.1 Failure condition ordering

```
[feat] < [rd_align, rd_bound, rd_state, pdev_align, pdev_bound, pdev_gran_state, vdev_align, vdev_bound, vdev_gran_state, vdev_realm, data_align, data_pas, req_align, req_pas, resp_align,
```

ID

```
resp_pas, rsp_len] [pdev_gran_state, vdev_gran_state] < [vdev_pdev, comm_state]
```

<!-- image -->

## B4.5.80.3 Success conditions

* complete
  * pre: DeviceCommunicate(vdev, data) == DEV_COMM_IDLE
  * post: RmiDevCommComplete(data.exit.flags)
* incomplete
  * pre: DeviceCommunicate(vdev, data) != DEV_COMM_IDLE
  * post: !RmiDevCommComplete(data.exit.flags)
* comm_state
  * post: vdev.comm_state == DeviceCommunicate(vdev, data)
* error
  * pre: DeviceCommunicate(vdev, data) == DEV_COMM_ERROR
  * post: vdev.vdev_state == VDEV_ERROR
* locked_unlocked
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.vdev_state == VDEV_LOCKED && vdev.op == VDEV_OP_UNLOCK)
  * post: vdev.vdev_state == VDEV_UNLOCKED
* started_unlocked
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.vdev_state == VDEV_STARTED && vdev.op == VDEV_OP_UNLOCK && rmm.static.feat_vdev_krou == FEATURE_FALSE)
  * post: vdev.vdev_state == VDEV_UNLOCKED
* started_key_refresh
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.vdev_state == VDEV_STARTED && vdev.op == VDEV_OP_UNLOCK && rmm.static.feat_vdev_krou == FEATURE_TRUE)
  * post: vdev.vdev_state == VDEV_KEY_REFRESH
* key_refresh
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_KEY_REFRESH)
  * post: vdev.vdev_state == VDEV_KEY_PURGE
* key_purge
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_KEY_PURGE)
  * post: vdev.vdev_state == VDEV_UNLOCKED
* lock_state
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_LOCK)
  * post: vdev.vdev_state == VDEV_LOCKED
* lock_nonce
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_LOCK)
  * post: vdev.attest_info.lock_nonce == VdevGenerateNonce(vdev_pre)
* start_state
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_START)
  * post: vdev.vdev_state == VDEV_STARTED
* meas_nonce
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_GET_MEAS)
  * post: vdev.attest_info.meas_nonce == VdevGenerateNonce(vdev_pre)
* intf_count
  * pre: (DeviceCommunicate(vdev, data) == DEV_COMM_IDLE && vdev.op == VDEV_OP_GET_REPORT)
  * post: vdev.attest_info.report_nonce == VdevGenerateNonce(vdev_pre)
* op
  * pre: DeviceCommunicate(vdev, data) == DEV_COMM_IDLE
  * post: vdev.op == VDEV_OP_NONE

## B4.5.80.4 Footprint

| ID           | Value                         |
|--------------|-------------------------------|
| state        | vdev.vdev_state               |
| op           | vdev.op                       |
| comm_state   | vdev.comm_state               |
| lock_nonce   | vdev.attest_info.lock_nonce   |
| meas_nonce   | vdev.attest_info.meas_nonce   |
| report_nonce | vdev.attest_info.report_nonce |

