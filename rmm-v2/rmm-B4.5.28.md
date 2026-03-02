## B4.5.28 RMI\_PDEV\_DESTROY command

Destroy a PDEV.

The RMI\_PDEV\_DESTROY command may initiate a Stateful RMI Operation.

The RMI\_PDEV\_DESTROY command may initiate a memory-transferring RMI Operation.

## See also:

- Chapter A9 Realm device assignment
- B4.3.4 Object creation and destruction

## B4.5.28.1 Interface

## B4.5.28.1.1 Input values

| Name     | Register   | Bits   | Type    | Description           |
|----------|------------|--------|---------|-----------------------|
| fid      | X0         | 63:0   | UInt64  | FID, value 0xC4000177 |
| pdev_ptr | X1         | 63:0   | Address | PA of the PDEV        |

## B4.5.28.1.2 Context

The RMI\_PDEV\_DESTROY command operates on the following context.

| Name     | Type    | Value            | Before   | Description   |
|----------|---------|------------------|----------|---------------|
| pdev_pre | RmmPdev | PdevAt(pdev_ptr) | true     | PDEV          |

## B4.5.28.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |


## B4.5.28.2 Failure conditions

| ID              | Condition                                                                                |
|-----------------|------------------------------------------------------------------------------------------|
| feat            | pre: Rmm().static.feat_da != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED |
| pdev_align      | pre: !AddrIsRmiGranuleAligned(pdev_ptr) post: result.status == RMI_ERROR_INPUT           |
| pdev_tracking   | pre: !PaIsTrackedFine(pdev_ptr) post: result.status == RMI_ERROR_INPUT                   |
| pdev_gran_state | pre: GranuleAt(pdev_ptr).state != GRAN_PDEV post: result.status == RMI_ERROR_INPUT       |
| pdev_state      | pre: pdev_pre.state != PDEV_STOPPED post: result.status == RMI_ERROR_DEVICE              |

## ID

## Condition

pdev\_stream\_liv e

pre:

PdevStreamLive(pdev\_pre)

post:

result.status == RMI\_ERROR\_DEVICE

cmem\_count

pre:

pdev\_pre.cmem\_count != 0

post:

result.status == RMI\_ERROR\_DEVICE

## B4.5.28.2.1 Failure condition ordering

```
[pdev_gran_state] < [pdev_state] [feat] < [pdev_align, pdev_tracking, pdev_gran_state, pdev_stream_live, cmem_count]
```

pdev\_state,

<!-- image -->

## B4.5.28.3 Success conditions

Condition post:

GranuleAt(pdev\_ptr).state == GRAN\_DELEGATED

## B4.5.28.4 Footprint

| ID    | Value                     |
|-------|---------------------------|
| state | GranuleAt(pdev_ptr).state |


ID

gran\_state