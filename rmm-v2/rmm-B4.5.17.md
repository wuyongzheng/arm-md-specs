## B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command

Delegates a range of Granules.

The RMI\_GRANULE\_RANGE\_DELEGATE command may initiate a Stateful RMI Operation.

## See also:

- A2.3.6.2 Granule delegation
- B4.3.5 Range RMI operations
- B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command

## B4.5.17.1 Interface

## B4.5.17.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                 |
|--------|------------|--------|---------|-----------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001F1       |
| base   | X1         | 63:0   | Address | Base PA of the target range |
| top    | X2         | 63:0   | Address | Top PA of the target range  |

## B4.5.17.1.2 Context

The RMI\_GRANULE\_RANGE\_DELEGATE command operates on the following context.

| Name   | Type      | Value   | Before   | Description     |
|--------|-----------|---------|----------|-----------------|
| rmm    | RmmGlobal | Rmm()   | false    | RMMglobal state |

## B4.5.17.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                                   |
|---------|------------|--------|-----------|-----------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                                |
| out_top | X1         | 63:0   | Address   | Top PA of range whose state is GRAN_DELEGATED |


If result is RMI\_INCOMPLETE then the value of out\_top is UNKNOWN.

## B4.5.17.2 Failure conditions

| ID         | Condition                                                                          |
|------------|------------------------------------------------------------------------------------|
| rmm_state  | pre: rmm.dynamic.state != RMM_STATE_ACTIVE post: result.status == RMI_ERROR_GLOBAL |
| base_align | pre: !AddrIsRmiGranuleAligned(base) post: result.status == RMI_ERROR_INPUT         |
| top_align  | pre: !AddrIsRmiGranuleAligned(top) post: result.status == RMI_ERROR_INPUT          |


| ID        | Condition                                                                                                                                           |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| top_bound | pre: UInt(top) <= UInt(base) post: result.status == RMI_ERROR_INPUT                                                                                 |
| populated | pre: While processing the target range, the RMM was unable to proceed due to memory being unpopulated. post: result.status == RMI_ERROR_INPUT       |
| tracking  | pre: While processing the target range, the RMM was unable to proceed due to the state of a tracking region. post: result.status == RMI_ERROR_INPUT |
| state     | pre: While processing the target range, the RMM encountered a Granule whose state is not GRAN_UNDELEGATED. post: result.status == RMI_ERROR_INPUT   |

## B4.5.17.2.1 Failure condition ordering

The RMI\_GRANULE\_RANGE\_DELEGATE command does not have any failure condition orderings.

## B4.5.17.3 Success conditions

| ID         | Condition                                                   |
|------------|-------------------------------------------------------------|
| state       post: GranulesAllState(base, out_top, GRAN_DELEGATED) |
| result     | post: result.status == RMI_SUCCESS                          |
| B4.5.17.4  | Footprint                                                   |
| ID         | Value                                                       |
| gran_state | State of Granules in range [base, top)                      |