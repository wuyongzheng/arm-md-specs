## B4.5.18 RMI\_GRANULE\_RANGE\_UNDELEGATE command

Undelegates a range of Granules.

The RMI\_GRANULE\_RANGE\_UNDELEGATE command may initiate a Stateful RMI Operation.

## See also:

- A2.3.6.2 Granule delegation
- B4.3.5 Range RMI operations
- B4.5.17 RMI\_GRANULE\_RANGE\_DELEGATE command

## B4.5.18.1 Interface

## B4.5.18.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                 |
|--------|------------|--------|---------|-----------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC40001F2       |
| base   | X1         | 63:0   | Address | Base PA of the target range |
| top    | X2         | 63:0   | Address | Top PA of the target range  |

## B4.5.18.1.2 Output values

| Name    | Register   | Bits   | Type      | Description                                     |
|---------|------------|--------|-----------|-------------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                                  |
| out_top | X1         | 63:0   | Address   | Top PA of range whose state is GRAN_UNDELEGATED |

If result is RMI\_INCOMPLETE then the value of out\_top is UNKNOWN.


## B4.5.18.2 Failure conditions

Condition

| base_align   | pre: post:   | !AddrIsRmiGranuleAligned(base) result.status == RMI_ERROR_INPUT                                                                          |
|--------------|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| top_align    | pre: post:   | !AddrIsRmiGranuleAligned(top) result.status == RMI_ERROR_INPUT                                                                           |
| top_bound    | pre: post:   | UInt(top) <= UInt(base) result.status == RMI_ERROR_INPUT                                                                                 |
| tracking     | pre: post:   | While processing the target range, the RMM was unable to proceed due to the state of a tracking region. result.status == RMI_ERROR_INPUT |
| state        | pre: post:   | While processing the target range, the RMM encountered a Granule whose state is not GRAN_DELEGATED. result.status == RMI_ERROR_INPUT     |


ID

## B4.5.18.2.1 Failure condition ordering

The RMI\_GRANULE\_RANGE\_UNDELEGATE command does not have any failure condition orderings.

## B4.5.18.3 Success conditions

| ID      | Condition                                                      |
|---------|----------------------------------------------------------------|
| state   | post: GranulesAllState(base, out_top, GRAN_UNDELEGATED)        |
| content | post: Contents of Granules in range [base, out_top) are wiped. |
| result  | post: result.status == RMI_SUCCESS                             |

## B4.5.18.4 Footprint

| ID         | Value                                  |
|------------|----------------------------------------|
| gran_state | State of Granules in range [base, top) |

