## B4.5.42 RMI\_PSMMU\_IRQ\_NOTIFY command

Notify RMM of an SMMU interrupt.

See also:

- A9.7.6 PSMMU interrupts
- A9.8.6 Page Request Interface events

## B4.5.42.1 Interface

## B4.5.42.1.1 Input values

| Name      | Register   | Bits   | Type           | Description               |
|-----------|------------|--------|----------------|---------------------------|
| fid       | X0         | 63:0   | UInt64         | FID, value 0xC400016F     |
| psmmu_ptr | X1         | 63:0   | Address        | PA of PSMMU               |
| irqs      | X2         | 63:0   | RmiPsmmuIrqSet | Set of pending PSMMU IRQs |

## B4.5.42.1.2 Context

The RMI\_PSMMU\_IRQ\_NOTIFY command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| psmmu  | RmmPsmmu | PsmmuAt(psmmu_ptr) | false    | PSMMU         |

## B4.5.42.1.3 Output values

| Name       | Register   | Bits   | Type              | Description                                                  |
|------------|------------|--------|-------------------|--------------------------------------------------------------|
| result     | X0         | 63:0   | RmiResult         | Command result                                               |
| flags      | X1         | 63:0   | RmiPsmmuIrqResult | Result of triaging the IRQ                                   |
| event_num  | X2         | 63:0   | UInt64            | SMMUevent number                                             |
| sid        | X3         | 63:0   | Bits64            | PSMMU Stream ID This is valid if flags.vsmmu == RMI_TRUE.    |
| fetch_addr | X4         | 63:0   | Address           | Physical fetch address, as specified by SMMU                 |
| input_addr | X5         | 63:0   | Address           | Physical input address, as specified by SMMU                 |
| fipa       | X6         | 63:0   | Address           | Faulting IPA, as specified bySMMU                            |
| syndrome   | X7         | 63:0   | Bits64            | RnW[0], S2[1] and Class[3:2] attributes, as specified bySMMU |


## B4.5.42.2 Failure conditions

| ID          | Condition                                                                                |
|-------------|------------------------------------------------------------------------------------------|
| feat        | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| psmmu_valid | pre: !PsmmuAddrIsValid(psmmu_ptr) post: result.status == RMI_ERROR_INPUT                 |
| psmmu_state | pre: psmmu.state != PSMMU_ACTIVE post: result.status == RMI_ERROR_INPUT                  |

## B4.5.42.2.1 Failure condition ordering

The RMI\_PSMMU\_IRQ\_NOTIFY command does not have any failure condition orderings.

## B4.5.42.3 Success conditions

The RMI\_PSMMU\_IRQ\_NOTIFY command does not have any success conditions.

## B4.5.42.4 Footprint

The RMI\_PSMMU\_IRQ\_NOTIFY command does not have any footprint.

<!-- image -->