## B5.4.7 RSI\_IPA\_STATE\_SET command

Request RIPAS of a target IPA range to be changed to a specified value.

See also:

- [A5.2 Realm view of memory management](rmm-A5.1.md#a52-realm-view-of-memory-management)
- [A5.4 RIPAS change](rmm-A5.4.md)
- [B5.2.2.2 Range RSI operation which returns progress address](rmm-B5.1.md#b5222-range-rsi-operation-which-returns-progress-address)
- [B5.4.6 RSI\_IPA\_STATE\_GET command](rmm-B5.4.6.md)

## B5.4.7.1 Interface

## B5.4.7.1.1 Input values

| Name   | Register   | Bits   | Type                | Description               |
|--------|------------|--------|---------------------|---------------------------|
| fid    | X0         | 63:0   | UInt64              | FID, value 0xC4000197     |
| base   | X1         | 63:0   | Address             | Base of target IPA region |
| top    | X2         | 63:0   | Address             | Top of target IPA region  |
| ripas  | X3         | 7:0    | RsiRipas            | RIPAS value               |
| flags  | X4         | 63:0   | RsiRipasChangeFlags | Flags                     |

The following unused bits of RSI\_IPA\_STATE\_SET input values SBZ: X3[63:8].

If ripas is not RIPAS\_RAM then flags.destroyed is ignored.

## B5.4.7.1.2 Context

The RSI\_IPA\_STATE\_SET command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |
| rec    | RmmRec   | CurrentRec()   | false    | Current REC   |


## B5.4.7.1.3 Output values

| Name     | Register   | Bits   | Type                 | Description                                              |
|----------|------------|--------|----------------------|----------------------------------------------------------|
| result   | X0         | 63:0   | RsiCommandReturnCode | Command result                                           |
| new_base | X1         | 63:0   | Address              | Base of IPA region which was not modified by the command |
| response | X2         | 0:0    | RsiResponse          | Whether the Host accepted or rejected the request        |

The following unused bits of RSI\_IPA\_STATE\_SET output values MBZ: X2[63:1].

If the Host rejects the request then:

- result == RSI\_SUCCESS
- new\_base == base
- response == RSI\_RESPONSE\_REJECT

ID

## B5.4.7.2 Failure conditions

* base_align
  * pre: !AddrIsRsiGranuleAligned(base)
  * post: result == RSI_ERROR_INPUT
* top_align
  * pre: !AddrIsRsiGranuleAligned(top)
  * post: result == RSI_ERROR_INPUT
* size_valid
  * pre: UInt(top) <= UInt(base)
  * post: result == RSI_ERROR_INPUT
* rgn_bound
  * pre: !AddrRangeIsProtected(base, top, realm)
  * post: result == RSI_ERROR_INPUT
* ripas_valid
  * pre: (ripas != RSI_RIPAS_EMPTY) && (ripas != RSI_RIPAS_RAM)
  * post: result == RSI_ERROR_INPUT

## B5.4.7.2.1 Failure condition ordering

The RSI\_IPA\_STATE\_SET command does not have any failure condition orderings.
## B5.4.7.3 Success conditions

* ripas
  * post: RIPAS of address range [base, new_base) is equal to ripas.
* new_base
  * post: new_base == rec.ripas_addr
* response
  * post: response == RecRipasResponseToRsi(rec)

## B5.4.7.4 Footprint

The RSI\_IPA\_STATE\_SET command does not have any footprint.