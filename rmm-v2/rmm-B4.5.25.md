## B4.5.25 RMI\_PDEV\_ABORT command

Abort device communication associated with a PDEV.

See also:

- Chapter A9 Realm device assignment

## B4.5.25.1 Interface

## B4.5.25.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000174 |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV        |

## B4.5.25.1.2 Context

The RMI\_PDEV\_ABORT command operates on the following context.

| Name           | Type         | Value            | Before   | Description    |
|----------------|--------------|------------------|----------|----------------|
| pdev           | RmmPdev      | PdevAt(pdev_ptr) | false    | PDEV           |
| pdev_state_pre | RmmPdevState | pdev.state       | true     | Previous state |

## B4.5.25.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.25.2 Failure conditions

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
  * pre: pdev.comm_state == DEV_COMM_IDLE
  * post: result.status == RMI_ERROR_DEVICE

## B4.5.25.2.1 Failure condition ordering

[feat] &lt; [pdev\_align, pdev\_bound, pdev\_gran\_state] [pdev\_gran\_state] &lt; [comm\_state]

<!-- image -->

## B4.5.25.3 Success conditions

* comm_state
  * Condition post: pdev.comm_state == DEV_COMM_IDLE

## B4.5.25.4 Footprint

| ID         | Value           |
|------------|-----------------|
| comm_state | pdev.comm_state |