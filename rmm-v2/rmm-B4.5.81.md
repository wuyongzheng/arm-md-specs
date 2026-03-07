## B4.5.81 RMI\_VDEV\_COMPLETE command

Completes a pending VDEV request.

## See also:

- [A4.3.12 REC exit due to VDEV request](rmm-A4.3.md#a4312-rec-exit-due-to-vdev-request)
- [A9.4.4 Mapping from virtual device ID to VDEV object](rmm-A9.4.md#a944-mapping-from-virtual-device-id-to-vdev-object)

## B4.5.81.1 Interface

## B4.5.81.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC400018E |
| rec_ptr  | X1         | 63:0   | Address | PA of the REC         |
| vdev_ptr | X2         | 63:0   | Address | PA of the VDEV        |

## B4.5.81.1.2 Context

The RMI\_VDEV\_COMPLETE command operates on the following context.

| Name   | Type    | Value            | Before   | Description   |
|--------|---------|------------------|----------|---------------|
| rec    | RmmRec  | RecAt(rec_ptr)   | false    | REC           |
| vdev   | RmmVdev | VdevAt(vdev_ptr) | false    | VDEV          |

## B4.5.81.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.81.2 Failure conditions

* rec_align
  * pre: !AddrIsRmiGranuleAligned(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_bound
  * pre: !PaIsTracked(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* recv_state
  * pre: GranuleAt(rec_ptr).state != GRAN_REC
  * post: result.status == RMI_ERROR_INPUT
* vdev_align
  * pre: !AddrIsRmiGranuleAligned(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_bound
  * pre: !PaIsTracked(vdev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vdev_state
  * pre: GranuleAt(vdev_ptr).state != GRAN_VDEV
  * post: result.status == RMI_ERROR_INPUT
* pending
  * pre: rec.pending != REC_PENDING_VDEV_REQUEST
  * post: result.status == RMI_ERROR_INPUT
* owner
  * pre: rec.owner != vdev.
* realm
  * post: result.status == RMI_ERROR_INPUT
* vdev_id
  * pre: rec.vdev_id_1 != vdev.
* vdev_id
  * post: result.status == RMI_ERROR_INPUT
* comm_state
  * pre: vdev.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.81.2.1 Failure condition ordering

The RMI\_VDEV\_COMPLETE command does not have any failure condition orderings.

## B4.5.81.3 Success conditions

* pending
  * post: rec.pending == REC_PENDING_VDEV_COMPLETE
* vdev_pa
  * post: rec.vdev_pa_1 == vdev_ptr
* comm_state
  * pre: rec.vdev_comm_pending == RMM_TRUE
  * post: vdev.comm_state == DEV_COMM_PENDING

## B4.5.81.4 Footprint

| ID         | Value           |
|------------|-----------------|
| pending    | rec.pending     |
| vdev_pa    | rec.vdev_pa_1   |
| comm_state | vdev.comm_state |

