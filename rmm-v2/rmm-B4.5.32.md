## B4.5.32 RMI\_PDEV\_STOP command

Stop a PDEV.

See also:

- [Chapter A9 Realm device assignment](rmm-A8.md#chapter-a9-realm-device-assignment)

## B4.5.32.1 Interface

## B4.5.32.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC400017C |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV        |

## B4.5.32.1.2 Context

The RMI\_PDEV\_STOP command operates on the following context.

| Name   | Type    | Value            | Before   | Description   |
|--------|---------|------------------|----------|---------------|
| pdev   | RmmPdev | PdevAt(pdev_ptr) | false    | PDEV          |

## B4.5.32.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.32.2 Failure conditions

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
* comm_state
  * pre: pdev.comm_state != DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE
* num_vdevs
  * pre: pdev.num_vdevs != 0
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.32.2.1 Failure condition ordering

[feat] &lt; [pdev\_align, pdev\_bound, pdev\_gran\_state] [pdev\_gran\_state] &lt; [num\_vdevs, comm\_state]

<!-- image -->

## B4.5.32.3 Success conditions

* op
  * post: pdev.op == PDEV_OP_STOP
* comm_state
  * post: pdev.comm_state == DEV_COMM_PENDING

## B4.5.32.4 Footprint

| ID         | Value           |
|------------|-----------------|
| op         | pdev.op         |
| comm_state | pdev.comm_state |

