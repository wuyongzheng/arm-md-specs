## B5.4.11 RSI\_MEM\_SET\_PERM\_INDEX command

Set overlay permission index for a specified IPA range.

See also:

- A10.3.2 Stage 2 Access Permissions within a multi-Plane Realm
- B5.2.2.2 Range RSI operation which returns progress address

## B5.4.11.1 Interface

## B5.4.11.1.1 Input values

| Name       | Register   | Bits   | Type    | Description               |
|------------|------------|--------|---------|---------------------------|
| fid        | X0         | 63:0   | UInt64  | FID, value 0xC40001A1     |
| base       | X1         | 63:0   | Address | Base of target IPA region |
| top        | X2         | 63:0   | Address | Top of target IPA region  |
| perm_index | X3         | 63:0   | UInt64  | Permission index          |
| handle     | X4         | 63:0   | Bits64  | Handle value              |

## B5.4.11.1.2 Context

The RSI\_MEM\_SET\_PERM\_INDEX command operates on the following context.

| Name   | Type     | Value          | Before   | Description   |
|--------|----------|----------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm() | false    | Current Realm |
| rec    | RmmRec   | CurrentRec()   | false    | Current REC   |

## B5.4.11.1.3 Output values

DRAFT

| Name       | Register   | Bits   | Type                 | Description                                              |
|------------|------------|--------|----------------------|----------------------------------------------------------|
| result     | X0         | 63:0   | RsiCommandReturnCode | Command result                                           |
| new_base   | X1         | 63:0   | Address              | Base of IPA region which was not modified by the command |
| response   | X2         | 0:0    | RsiResponse          | Whether the Host accepted or rejected the request        |
| new_handle | X3         | 63:0   | Bits64               | New handle value                                         |

The following unused bits of RSI\_MEM\_SET\_PERM\_INDEX output values MBZ: X2[63:1].

## B5.4.11.2 Failure conditions

## ID Condition realm)

```
base_align pre: !AddrIsRsiGranuleAligned(base) post: result == RSI_ERROR_INPUT top_align pre: !AddrIsRsiGranuleAligned(top) post: result == RSI_ERROR_INPUT size_valid pre: UInt(top) <= UInt(base) post: result == RSI_ERROR_INPUT rgn_bound pre: !AddrRangeIsProtected(base, top, post: result == RSI_ERROR_INPUT perm_bound pre: perm_index >= RMM_NUM_PERM_OVERLAY_INDICES post: result == RSI_ERROR_INPUT handle pre: Handle is invalid post: result == RSI_ERROR_INPUT
```

## B5.4.11.2.1 Failure condition ordering

DRAFT The RSI\_MEM\_SET\_PERM\_INDEX command does not have any failure condition orderings. B5.4.11.3 Success conditions ID Condition locked post: realm.overlay\_locked[[perm\_index]] == MEM\_PERM\_LOCKED new\_base post: new\_base == rec.s2ap\_addr response post: response == RecS2APResponseToRsi(rec) new\_handle post: New handle is generated

## B5.4.11.4 Footprint

| ID     | Value                              |
|--------|------------------------------------|
| locked | realm.overlay_locked[[perm_index]] |