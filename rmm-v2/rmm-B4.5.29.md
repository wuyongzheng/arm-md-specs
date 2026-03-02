## B4.5.29 RMI\_PDEV\_GET\_STATE command

Get state of a PDEV.

See also:

- Chapter A9 Realm device assignment

## B4.5.29.1 Interface

## B4.5.29.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000178 |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV        |

## B4.5.29.1.2 Context

The RMI\_PDEV\_GET\_STATE command operates on the following context.

| Name   | Type    | Value            | Before   | Description   |
|--------|---------|------------------|----------|---------------|
| pdev   | RmmPdev | PdevAt(pdev_ptr) | false    | PDEV          |

## B4.5.29.1.3 Output values

| Name   | Register   | Bits   | Type         | Description    |
|--------|------------|--------|--------------|----------------|
| result | X0         | 63:0   | RmiResult    | Command result |
| state  | X1         | 7:0    | RmiPdevState | PDEV state     |

DRAFT

The following unused bits of RMI\_PDEV\_GET\_STATE output values MBZ: X1[63:8].

## B4.5.29.2 Failure conditions

| ID              | Condition                                                                                |
|-----------------|------------------------------------------------------------------------------------------|
| feat            | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| pdev_align      | pre: !AddrIsRmiGranuleAligned(pdev_ptr) post: result.status == RMI_ERROR_INPUT           |
| pdev_bound      | pre: !PaIsTracked(pdev_ptr) post: result.status == RMI_ERROR_INPUT                       |
| pdev_gran_state | pre: GranuleAt(pdev_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT       |

## B4.5.29.2.1 Failure condition ordering

[feat] &lt; [pdev\_align, pdev\_bound, pdev\_gran\_state]

<!-- image -->

## B4.5.29.3 Success conditions

ID

Condition

state

post: Equal(state, pdev.state)

## B4.5.29.4 Footprint

The RMI\_PDEV\_GET\_STATE command does not have any footprint.

DRAFT