## B4.3.21 RMI\_RTT\_SET\_RIPAS command

Completes a request made by the Realm to change the RIPAS of a target IPA range.

See also:

- A5.4 RIPAS change

## B4.3.21.1 Interface

## B4.3.21.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                       |
|---------|------------|--------|---------|-----------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC4000169             |
| rd      | X1         | 63:0   | Address | PA of the RD for the target Realm |
| rec_ptr | X2         | 63:0   | Address | PA of the target REC              |
| base    | X3         | 63:0   | Address | Base of target IPA region         |
| top     | X4         | 63:0   | Address | Top of target IPA region          |

## B4.3.21.1.2 Context

The RMI\_RTT\_SET\_RIPAS command operates on the following context.

| Name     | Type             | Value                                                                                                        | Before   | Description                                                                                                 |
|----------|------------------|--------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| realm    | RmmRealm         | Realm(rd)                                                                                                    | true     | Realm                                                                                                       |
| rec      | RmmRec           | Rec(rec_ptr)                                                                                                 | false    | REC                                                                                                         |
| walk     | RmmRttWalkResult | RttWalk( rd, base, RMM_RTT_PAGE_LEVEL)                                                                       | false    | RTT walk result                                                                                             |
| ripas    | RmmRipas         | walk.rtte.ripas                                                                                              | true     | RIPAS before the command executed                                                                           |
| walk_top | Address          | RttSkipEntriesWithRipas( Rtt(walk.rtt_addr), walk.level, base, top, rec.ripas_destroyed != CHANGE_DESTROYED) | true     | Top IPA of entries which have associated RIPAS values, starting from entry at which the RTT walk terminated |

## B4.3.21.1.3 Output values

| Name    | Register   | Bits   | Type                 | Description                               |
|---------|------------|--------|----------------------|-------------------------------------------|
| result  | X0         | 63:0   | RmiCommandReturnCode | Command return status                     |
| out_top | X1         | 63:0   | Address              | Top IPA of range whose RIPAS was modified |

The out\_top output value is valid only when the command result is RMI\_SUCCESS.

ID

## B4.3.21.2 Failure conditions

## Condition

```
rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) rec_align pre: !AddrIsGranuleAligned(rec_ptr) post: ResultEqual(result, RMI_ERROR_INPUT) rec_bound pre: !PaIsDelegable(rec_ptr) post: ResultEqual(result, RMI_ERROR_INPUT) rec_gran_state pre: Granule(rec_ptr).state != REC post: ResultEqual(result, RMI_ERROR_INPUT) rec_state pre: rec.state == REC_RUNNING post: ResultEqual(result, RMI_ERROR_REC) rec_owner pre: rec.owner != rd post: ResultEqual(result, RMI_ERROR_REC) size_valid pre: UInt(top) <= UInt(base) post: ResultEqual(result, RMI_ERROR_INPUT) base_bound pre: base != rec.ripas_addr post: ResultEqual(result, RMI_ERROR_INPUT) top_bound pre: UInt(top) > UInt(rec.ripas_top) post: ResultEqual(result, RMI_ERROR_INPUT) base_align pre: (!AddrIsRttLevelAligned(base, walk.level) && ripas != rec.ripas_value) post: ResultEqual(result, RMI_ERROR_RTT, walk.level) top_gran_align pre: !AddrIsGranuleAligned(top) post: ResultEqual(result, RMI_ERROR_INPUT) no_progress pre: (UInt(base) == UInt(walk_top) && ripas != rec.ripas_value) post: ResultEqual(result, RMI_ERROR_RTT, walk.level)
```

## B4.3.21.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [base_align] [rd_bound, rd_state] < [no_progress] [rec_bound, rec_gran_state] < [rec_state, rec_owner] [base_bound] < [base_align] [top_gran_align] < [no_progress]
```

<!-- image -->

ID

## B4.3.21.3 Success conditions

## Condition

```
rtte_ripas RttEntriesInRangeRipas( Rtt(walk.rtt_addr), walk.level, base, walk_top, rec.ripas_value) ripas_addr rec.ripas_addr == MinAddress(top, walk_top) out_top out_top == MinAddress(top, walk_top)
```

## B4.3.21.4 Footprint

| ID         | Value              |
|------------|--------------------|
| rtte       | Rtt(walk.rtt_addr) |
| ripas_addr | rec.ripas_addr     |