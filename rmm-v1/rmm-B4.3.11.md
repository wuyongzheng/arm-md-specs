## B4.3.11 RMI\_REC\_AUX\_COUNT command

Get number of auxiliary Granules required for a REC.

See also:

- [A2.3 Realm Execution Context](rmm-A2.3.md)
- [B4.3.12 RMI\_REC\_CREATE command](rmm-B4.3.12.md)
- [B4.4.19 RmiRecParams type](rmm-B4.4.md#b4419-rmirecparams-type)
- [D1.2.4 REC creation flow](rmm-D1.2.md#d124-rec-creation-flow)

## B4.3.11.1 Interface

## B4.3.11.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                       |
|--------|------------|--------|---------|-----------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000167             |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm |

## B4.3.11.1.2 Output values

| Name      | Register   | Bits   | Type                 | Description                                     |
|-----------|------------|--------|----------------------|-------------------------------------------------|
| result    | X0         | 63:0   | RmiCommandReturnCode | Command return status                           |
| aux_count | X1         | 63:0   | UInt64               | Number of auxiliary Granules required for a REC |

## B4.3.11.2 Failure conditions

* rd_align
  * pre: !AddrIsGranuleAligned(rd)
  * post: ResultEqual(result, RMI_ERROR_INPUT)
* rd_bound
  * pre: !PaIsDelegable(rd)
  * post: ResultEqual(result, RMI_ERROR_INPUT)
* rd_state
  * pre: Granule(rd).state != RD
  * post: ResultEqual(result, RMI_ERROR_INPUT)

## B4.3.11.2.1 Failure condition ordering

The RMI\_REC\_AUX\_COUNT command does not have any failure condition orderings.

## B4.3.11.3 Success conditions

* aux_count
  * aux_count == RecAuxCount(rd)

## B4.3.11.4 Footprint

The RMI\_REC\_AUX\_COUNT command does not have any footprint.