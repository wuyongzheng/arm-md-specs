## B5.3.5 RSI\_IPA\_STATE\_GET command

Get RIPAS of a target IPA range.

See also:

- A5.2 Realm view of memory management
- B5.3.6 RSI\_IPA\_STATE\_SET command

## B5.3.5.1 Interface

## B5.3.5.1.1 Input values

| Name   | Register   | Bits   | Type    | Description               |
|--------|------------|--------|---------|---------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000198     |
| base   | X1         | 63:0   | Address | Base of target IPA region |
| top    | X2         | 63:0   | Address | End of target IPA region  |

## B5.3.5.1.2 Context

The RSI\_IPA\_STATE\_GET command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |

## B5.3.5.1.3 Output values

| Name    | Register   | Bits   | Type                 | Description                                          |
|---------|------------|--------|----------------------|------------------------------------------------------|
| result  | X0         | 63:0   | RsiCommandReturnCode | Command return status                                |
| out_top | X1         | 63:0   | Address              | Top of IPA region which has the reported RIPAS value |
| ripas   | X2         | 7:0    | RsiRipas             | RIPAS value                                          |

The following unused bits of RSI\_IPA\_STATE\_GET output values MBZ: X2[63:8].

If result == RSI\_SUCCESS then all of the following are true:

- out\_top &gt; base
- out\_top &lt;= top
- All addresses within the range [base, out\_top) have the RIPAS value ripas .

Note that the RIPAS of a Protected IPA can change at any time to DESTROYED without the Realm taking any action.

See also:

- A5.2.5 Changes to RIPAS while Realm state is REALM\_ACTIVE

## B5.3.5.2 Failure conditions

| ID         | Condition                                                                    |
|------------|------------------------------------------------------------------------------|
| base_align | pre: !AddrIsGranuleAligned(base) post: result == RSI_ERROR_INPUT             |
| end_align  | pre: !AddrIsGranuleAligned(top) post: result == RSI_ERROR_INPUT              |
| size_valid | pre: UInt(top) <= UInt(base) post: result == RSI_ERROR_INPUT                 |
| rgn_bound  | pre: !AddrRangeIsProtected(base, top, realm) post: result == RSI_ERROR_INPUT |

## B5.3.5.2.1 Failure condition ordering

The RSI\_IPA\_STATE\_GET command does not have any failure condition orderings.

## B5.3.5.3 Success conditions

The RSI\_IPA\_STATE\_GET command does not have any success conditions.

## B5.3.5.4 Footprint

The RSI\_IPA\_STATE\_GET command does not have any footprint.