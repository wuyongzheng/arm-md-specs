## B5.4.6 RSI\_IPA\_STATE\_GET command

Get RIPAS of a target IPA range.

See also:

- A5.2 Realm view of memory management
- B5.4.7 RSI\_IPA\_STATE\_SET command

## B5.4.6.1 Interface

## B5.4.6.1.1 Input values

| Name   | Register   | Bits   | Type    | Description               |
|--------|------------|--------|---------|---------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000198     |
| base   | X1         | 63:0   | Address | Base of target IPA region |
| top    | X2         | 63:0   | Address | End of target IPA region  |

## B5.4.6.1.2 Context

The RSI\_IPA\_STATE\_GET command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |

## B5.4.6.1.3 Output values

| Name    | Register   | Bits   | Type                 | Description                                          |
|---------|------------|--------|----------------------|------------------------------------------------------|
| result  | X0         | 63:0   | RsiCommandReturnCode | Command result                                       |
| out_top | X1         | 63:0   | Address              | Top of IPA region which has the reported RIPAS value |
| ripas   | X2         | 7:0    | RsiRipas             | RIPAS value                                          |


The following unused bits of RSI\_IPA\_STATE\_GET output values MBZ: X2[63:8].

If result == RSI\_SUCCESS then all of the following are true:

- out\_top &gt; base
- out\_top &lt;= top
- All addresses within the range [base, out\_top) have the RIPAS value ripas .

Note that the RIPAS of a Protected IPA can change at any time to RIPAS\_DESTROYED without the Realm taking any action.

See also:

- A5.2.6 Changes to RIPAS while Realm state is REALM\_ACTIVE

## B5.4.6.2 Failure conditions

* base_align
  * pre: !AddrIsRsiGranuleAligned(base)
  * post: result == RSI_ERROR_INPUT
* end_align
  * pre: !AddrIsRsiGranuleAligned(top)
  * post: result == RSI_ERROR_INPUT
* size_valid
  * pre: UInt(top) <= UInt(base)
  * post: result == RSI_ERROR_INPUT
* rgn_bound
  * pre: !AddrRangeIsProtected(base, top, realm)
  * post: result == RSI_ERROR_INPUT

## B5.4.6.2.1 Failure condition ordering

The RSI\_IPA\_STATE\_GET command does not have any failure condition orderings.

## B5.4.6.3 Success conditions

* ripas
  * post: Value of out_top is such that RIPAS of address [base, out_top) is equal to ripas.

## B5.4.6.4 Footprint

The RSI\_IPA\_STATE\_GET command does not have any footprint.

