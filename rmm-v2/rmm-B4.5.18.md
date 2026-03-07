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

* base_align
  * pre: !AddrIsRmiGranuleAligned(base)
  * post: result.status == RMI_ERROR_INPUT
* top_align
  * pre: !AddrIsRmiGranuleAligned(top)
  * post: result.status == RMI_ERROR_INPUT
* top_bound
  * pre: UInt(top) <= UInt(base)
  * post: result.status == RMI_ERROR_INPUT
* tracking
  * pre: While processing the target range, the RMM was unable to proceed due to the state of a tracking region.
  * post: result.status == RMI_ERROR_INPUT
* state
  * pre: While processing the target range, the RMM encountered a Granule whose state is not GRAN_DELEGATED.
  * post: result.status == RMI_ERROR_INPUT

## B4.5.18.2.1 Failure condition ordering

The RMI\_GRANULE\_RANGE\_UNDELEGATE command does not have any failure condition orderings.

## B4.5.18.3 Success conditions

* state
  * post: GranulesAllState(base, out_top, GRAN_UNDELEGATED)
* content
  * post: Contents of Granules in range [base, out_top) are wiped.
* result
  * post: result.status == RMI_SUCCESS

## B4.5.18.4 Footprint

| ID         | Value                                  |
|------------|----------------------------------------|
| gran_state | State of Granules in range [base, top) |

