## B4.5.76 RMI\_RTT\_SET\_S2AP command

Completes a request made by the Realm to change the S2AP of a target IPA range.

The RMI\_RTT\_SET\_S2AP command may initiate a Stateful RMI Operation.

See also:

- A10.3.2.3 Stage 2 Access Permissions change within a multi-Plane Realm
- B4.3.5 Range RMI operations

## B4.5.76.1 Interface

## B4.5.76.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                       |
|---------|------------|--------|---------|-----------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400018B             |
| rd      | X1         | 63:0   | Address | PA of the RD for the target Realm |
| rec_ptr | X2         | 63:0   | Address | PA of the target REC              |
| base    | X3         | 63:0   | Address | Base of target IPA region         |
| top     | X4         | 63:0   | Address | Top of target IPA region          |

## B4.5.76.1.2 Context

The RMI\_RTT\_SET\_S2AP command operates on the following context.

| Name        | Type Value                                                                       | Before   | Description                                        |
|-------------|----------------------------------------------------------------------------------|----------|----------------------------------------------------|
| realm       | RmmRealm RealmAt(rd)                                                             | false    | Realm                                              |
| realm_pre   | RmmRealm RealmAt(rd)                                                             | true     | Realm                                              |
| rec         | RmmRec RecAt(rec_ptr)                                                            | false    | REC                                                |
| not_aligned | RmmRttWalkNotAligned RttWalkAnyNotAligned( realm, base, top, RMM_RTT_PAGE_LEVEL) | false    | RTT walk result which is not aligned to page level |

DRAFT

## B4.5.76.1.3 Output values

| Name     | Register   | Bits   | Type      | Description                                            |
|----------|------------|--------|-----------|--------------------------------------------------------|
| result   | X0         | 63:0   | RmiResult | Command result                                         |
| out_top  | X1         | 63:0   | Address   | Top IPA of range whose S2AP was modified               |
| rtt_tree | X2         | 63:0   | UInt64    | Index of RTT tree in which base alignment check failed |

If result is RMI\_ERROR\_RTT or RMI\_ERROR\_RTT\_AUX then the following are true:

- out\_top is the IPA of the RTTE at which the base alignment check failed.
- rtt\_tree is the index of the RTT in which the base alignment check failed.

ID

## B4.5.76.2 Failure conditions

## Condition

```
DRAFT rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT rec_align pre: !AddrIsRmiGranuleAligned(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_bound pre: !PaIsTracked(rec_ptr) post: result.status == RMI_ERROR_INPUT rec_gran_state pre: GranuleAt(rec_ptr).state != GRAN_REC post: result.status == RMI_ERROR_INPUT rec_state pre: rec.state == REC_RUNNING post: result.status == RMI_ERROR_REC rec_owner pre: rec.owner != rd post: result.status == RMI_ERROR_REC size_valid pre: UInt(top) <= UInt(base) post: result.status == RMI_ERROR_INPUT base_bound pre: base != rec.s2ap_addr post: result.status == RMI_ERROR_INPUT top_bound pre: UInt(top) > UInt(rec.s2ap_top) post: result.status == RMI_ERROR_INPUT top_gran_align pre: !AddrIsRmiGranuleAligned(top) post: result.status == RMI_ERROR_INPUT base_align_pri pre: (not_aligned.valid == RMM_TRUE && !AddrRangeIsWithin( base, top, AlignDownToRttLevel( not_aligned.addr, not_aligned.walk.level ), AlignUpToRttLevel( not_aligned.addr, not_aligned.walk.level )) && not_aligned.index == RMM_RTT_TREE_PRIMARY && not_aligned.walk.rtte.s2ap_indirect.overlay_index != rec.s2ap_overlay_index) post: (result.status == RMI_ERROR_RTT && result.data.level.level == not_aligned.walk.level)
```

ID

## Condition

```
base_align_aux pre: (not_aligned.valid == RMM_TRUE && !AddrRangeIsWithin( base, top, AlignDownToRttLevel( not_aligned.addr, not_aligned.walk.level ), AlignUpToRttLevel( not_aligned.addr, not_aligned.walk.level )) && not_aligned.index != RMM_RTT_TREE_PRIMARY && not_aligned.walk.rtte.s2ap_indirect.overlay_index != rec.s2ap_overlay_index) post: (result.status == RMI_ERROR_RTT && result.data.level.level == not_aligned.walk.level)
```

## B4.5.76.2.1 Failure condition ordering

The RMI\_RTT\_SET\_S2AP command does not have any failure condition orderings.

## B4.5.76.3 Success conditions

| ID        | Condition                      |
|-----------|--------------------------------|
| s2ap_addr | post: rec.s2ap_addr == out_top |

## B4.5.76.4 Footprint

| ID        | Value         |
|-----------|---------------|
| s2ap_addr | rec.s2ap_addr |

DRAFT