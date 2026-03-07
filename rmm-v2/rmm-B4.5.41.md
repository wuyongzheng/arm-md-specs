## B4.5.41 RMI\_PSMMU\_EVENT\_DISCARD command

Discard a PSMMU event.

See also:

- A9.8.6 Page Request Interface events

## B4.5.41.1 Interface

## B4.5.41.1.1 Input values

| Name      | Register   | Bits   | Type        | Description           |
|-----------|------------|--------|-------------|-----------------------|
| fid       | X0         | 63:0   | UInt64      | FID, value 0xC40001F0 |
| psmmu_ptr | X1         | 63:0   | Address     | PA of PSMMU           |
| irq       | X2         | 1:0    | RmiPsmmuIrq | SMMUIRQ               |

The following unused bits of RMI\_PSMMU\_EVENT\_DISCARD input values SBZ: X2[63:2].

## B4.5.41.1.2 Context

The RMI\_PSMMU\_EVENT\_DISCARD command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| psmmu  | RmmPsmmu | PsmmuAt(psmmu_ptr) | false    | PSMMU         |

## B4.5.41.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.41.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* psmmu_valid
  * pre: !PsmmuAddrIsValid(psmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* psmmu_state
  * pre: psmmu.state != PSMMU_ACTIVE
  * post: result.status == RMI_ERROR_INPUT

## B4.5.41.2.1 Failure condition ordering

The RMI\_PSMMU\_EVENT\_DISCARD command does not have any failure condition orderings.

## B4.5.41.3 Success conditions

The RMI\_PSMMU\_EVENT\_DISCARD command does not have any success conditions.

## B4.5.41.4 Footprint

The RMI\_PSMMU\_EVENT\_DISCARD command does not have any footprint.