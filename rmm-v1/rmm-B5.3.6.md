## B5.3.6 RSI\_IPA\_STATE\_SET command

Request RIPAS of a target IPA range to be changed to a specified value.

See also:

- A5.2 Realm view of memory management
- A5.4 RIPAS change
- B5.3.5 RSI\_IPA\_STATE\_GET command

## B5.3.6.1 Interface

## B5.3.6.1.1 Input values

| Name   | Register   | Bits   | Type                | Description               |
|--------|------------|--------|---------------------|---------------------------|
| fid    | X0         | 63:0   | UInt64              | FID, value 0xC4000197     |
| base   | X1         | 63:0   | Address             | Base of target IPA region |
| top    | X2         | 63:0   | Address             | Top of target IPA region  |
| ripas  | X3         | 7:0    | RsiRipas            | RIPAS value               |
| flags  | X4         | 63:0   | RsiRipasChangeFlags | Flags                     |

The following unused bits of RSI\_IPA\_STATE\_SET input values SBZ: X3[63:8].

## B5.3.6.1.2 Context

The RSI\_IPA\_STATE\_SET command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |
| rec    | RmmRec   | CurrentRec()   | false    | Current REC   |

## B5.3.6.1.3 Output values

| Name     | Register   | Bits   | Type                 | Description                                              |
|----------|------------|--------|----------------------|----------------------------------------------------------|
| result   | X0         | 63:0   | RsiCommandReturnCode | Command return status                                    |
| new_base | X1         | 63:0   | Address              | Base of IPA region which was not modified by the command |
| response | X2         | 0:0    | RsiResponse          | Whether the Host accepted or rejected the request        |

The following unused bits of RSI\_IPA\_STATE\_SET output values MBZ: X2[63:1].

If the Host rejects the request then:

- result == RSI\_SUCCESS
- new\_base == base
- response == RSI\_REJECT

ID

## B5.3.6.2 Failure conditions

## Condition

```
base_align pre: !AddrIsGranuleAligned(base) post: result == RSI_ERROR_INPUT top_align pre: !AddrIsGranuleAligned(top) post: result == RSI_ERROR_INPUT size_valid pre: UInt(top) <= UInt(base) post: result == RSI_ERROR_INPUT rgn_bound pre: !AddrRangeIsProtected(base, top, realm) post: result == RSI_ERROR_INPUT ripas_valid pre: (ripas != RSI_EMPTY) && (ripas != RSI_RAM) post: result == RSI_ERROR_INPUT
```

## B5.3.6.2.1 Failure condition ordering

The RSI\_IPA\_STATE\_SET command does not have any failure condition orderings.

## B5.3.6.3 Success conditions

```
ID Condition new_base new_base == rec.ripas_addr response response == RecRipasChangeResponse(rec)
```

## B5.3.6.4 Footprint

The RSI\_IPA\_STATE\_SET command does not have any footprint.