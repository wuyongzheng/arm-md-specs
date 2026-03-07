## B4.5.40 RMI\_PSMMU\_DEACTIVATE command

Deactivate a PSMMU.

The RMI\_PSMMU\_DEACTIVATE command may initiate a Stateful RMI Operation.

The RMI\_PSMMU\_DEACTIVATE command may initiate a memory-transferring RMI Operation.

## See also:

- [A9.7 Physical SMMU](rmm-A9.7.md)
- [B4.5.39 RMI\_PSMMU\_ACTIVATE command](rmm-B4.5.39.md)

## B4.5.40.1 Interface

## B4.5.40.1.1 Input values

| Name      | Register   | Bits   | Type    | Description           |
|-----------|------------|--------|---------|-----------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC40001D8 |
| psmmu_ptr | X1         | 63:0   | Address | PA of PSMMU           |

## B4.5.40.1.2 Context

The RMI\_PSMMU\_DEACTIVATE command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| psmmu  | RmmPsmmu | PsmmuAt(psmmu_ptr) | false    | PSMMU         |

## B4.5.40.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.40.2 Failure conditions

* feat
  * pre: Rmm().static.feat_da != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* psmmu_valid
  * pre: !PsmmuAddrIsValid(psmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* psmmu_state
  * pre: psmmu.state != PSMMU_ACTIVE
  * post: result.status == RMI_ERROR_INPUT
* psmmu_live
  * pre: PsmmuL1StIsLive(psmmu)
  * post: result.status == RMI_ERROR_INPUT

## B4.5.40.2.1 Failure condition ordering

The RMI\_PSMMU\_DEACTIVATE command does not have any failure condition orderings.

## B4.5.40.3 Success conditions

* state
  * post: psmmu.state == PSMMU_INACTIVE

## B4.5.40.4 Footprint

The RMI\_PSMMU\_DEACTIVATE command does not have any footprint.

<!-- image -->