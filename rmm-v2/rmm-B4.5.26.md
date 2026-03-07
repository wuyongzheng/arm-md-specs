## B4.5.26 RMI\_PDEV\_COMMUNICATE command

Perform device communication associated with a PDEV.

See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)

## B4.5.26.1 Interface

## B4.5.26.1.1 Input values

| Name     | Register   | Bits   | Type    | Description                            |
|----------|------------|--------|---------|----------------------------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000175                  |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV                         |
| data_ptr | X2         | 63:0   | Address | PA of the communication data structure |

## B4.5.26.1.2 Context

The RMI\_PDEV\_COMMUNICATE command operates on the following context.

| Name           | Type           | Value                      | Before   | Description                 |
|----------------|----------------|----------------------------|----------|-----------------------------|
| rmm            | RmmGlobal      | Rmm()                      | false    | RMMglobal state             |
| pdev           | RmmPdev        | PdevAt(pdev_ptr)           | false    | PDEV                        |
| pdev_state_pre | RmmPdevState   | PdevAt(pdev_ptr).state     | true     | PDEV previous state         |
| data           | RmiDevCommData | RmiDevCommDataAt(data_ptr) | false    | Device communication object |


## B4.5.26.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.26.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* pdev_align
  * pre: !AddrIsRmiGranuleAligned(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_bound
  * pre: !PaIsTracked(pdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* pdev_gran_state
  * pre: GranuleAt(pdev_ptr).state != GRAN_PDEV
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
* comm_state
  * pre: (pdev.comm_state == DEV_COMM_IDLE || pdev.comm_state == DEV_COMM_ERROR)
  * post: result.status == RMI_ERROR_DEVICE
* busy
  * pre: PdevIsBusy(pdev)
  * post: result.status == RMI_BUSY B4.5.26.2.1 Failure condition ordering [feat] < [pdev_align, pdev_bound, pdev_gran_state, data_align, data_pas, req_align, req_pas, resp_align, resp_pas, rsp_len] [pdev_gran_state] < [comm_state] feat pdev_align pdev_bound pdev_gran_state comm_state data_align data_pas req_align req_pas resp_align resp_pas rsp_len busy

## B4.5.26.3 Success conditions

* comm_state
  * post: pdev.comm_state == DeviceCommunicate(pdev,
* error
  * pre: DeviceCommunicate(pdev, data) == DEV_COMM_ERROR
  * post: pdev.state == PDEV_ERROR
* new
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev_state_pre == PDEV_NEW)
  * post: pdev.state == PDEV_NEEDS_KEY
* has_key
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev_state_pre == PDEV_HAS_KEY)
  * post: pdev.state == PDEV_READY
* ready_on_chip
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev_state_pre == PDEV_NEW && pdev.category == PDEV_ENDPOINT_ACCEL_ON_CHIP && pdev.spdm == SPDM_FALSE)
  * post: pdev.state == PDEV_READY
* ready
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev_state_pre == PDEV_READY)
  * post: pdev.state == PDEV_READY
* stop_state
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev.op == PDEV_OP_STOP)
  * post: pdev.state == PDEV_STOPPED
* op_connect
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev.op == PDEV_OP_CONNECT)
  * post: pdev.op == PDEV_OP_STREAM_COMPLETE
* op_disconnect
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev.op == PDEV_OP_DISCONNECT)
  * post: pdev.op == PDEV_OP_STREAM_COMPLETE
* op_key_refresh
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev.op == PDEV_OP_KEY_REFRESH)
  * post: pdev.op == PDEV_OP_STREAM_COMPLETE
* op_none
  * pre: (DeviceCommunicate(pdev, data) == DEV_COMM_IDLE && pdev.op != PDEV_OP_CONNECT && pdev.op != PDEV_OP_DISCONNECT && pdev.op != PDEV_OP_KEY_REFRESH)
  * post: pdev.op == PDEV_OP_NONE
* complete
  * pre: DeviceCommunicate(pdev, data) == DEV_COMM_IDLE
  * post: RmiDevCommComplete(data.exit.flags)
* incomplete
  * pre: DeviceCommunicate(pdev, data) != DEV_COMM_IDLE
  * post: !RmiDevCommComplete(data.exit.flags)

## B4.5.26.4 Footprint

| ID         | Value                 |
|------------|-----------------------|
| state      | pdev.state            |
| op         | pdev_gran_statedev.op |
| comm_state | pdev.comm_state       |