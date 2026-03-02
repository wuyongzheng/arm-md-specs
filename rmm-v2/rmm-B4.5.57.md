## B4.5.57 RMI\_RTT\_AUX\_CREATE command

Creates an auxiliary RTT.

The RMI\_RTT\_AUX\_CREATE command may initiate a Stateful RMI Operation.

See also:

- A10.3.1 Auxiliary RTT
- B4.5.58 RMI\_RTT\_AUX\_DESTROY command
- B4.5.59 RMI\_RTT\_AUX\_FOLD command

## B4.5.57.1 Interface

## B4.5.57.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400017D                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| rtt    | X2         | 63:0   | Address | PA of the target RTT                       |
| ipa    | X3         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X4         | 63:0   | Int64   | RTT level                                  |
| index  | X5         | 63:0   | UInt64  | RTT tree index                             |

## B4.5.57.1.2 Context

The RMI\_RTT\_AUX\_CREATE command operates on the following context.

| Name      | Type             | Value                                       | Before   | Description                   |
|-----------|------------------|---------------------------------------------|----------|-------------------------------|
| realm     | RmmRealm         | RealmAt(rd)                                 | false    | Realm                         |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, index)      | false    | RTT walk result               |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)             | false    | RTTE index                    |
| unfold    | RmmRttEntry      | RttWalk( realm, ipa, level - 1, index).rtte | true     | RTTE before command execution |

DRAFT

## B4.5.57.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

ID

## B4.5.57.2 Failure conditions

## Condition

```
DRAFT rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT level_bound pre: (!RttLevelIsValid(realm, level) || RttLevelIsStarting(realm, level)) post: result.status == RMI_ERROR_INPUT ipa_align pre: !AddrIsRttLevelAligned(ipa, level -1) post: result.status == RMI_ERROR_INPUT ipa_bound pre: !AddrIsProtected(ipa, realm) post: result.status == RMI_ERROR_INPUT index_bound pre: (realm.rtt_tree_per_plane == FEATURE_FALSE || index == RMM_RTT_TREE_PRIMARY || index > realm.num_aux_planes) post: result.status == RMI_ERROR_INPUT rtt_align pre: !AddrIsRmiGranuleAligned(rtt) post: result.status == RMI_ERROR_INPUT rtt_bound pre: !PaIsDelegableConventionalFine(rtt) post: result.status == RMI_ERROR_INPUT rtt_state pre: GranuleAt(rtt).state != GRAN_DELEGATED post: result.status == RMI_ERROR_INPUT rtt_bound2 pre: ((realm.feat_lpa2 == FEATURE_FALSE) && (UInt(rtt) >= 2^48)) post: result.status == RMI_ERROR_INPUT rtt_walk pre: walk.level < level -1 post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level == rtte_state pre: walk.rtte.state == RTTE_TABLE post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level ==
```

## B4.5.57.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.5.57.3 Success conditions

```
walk.level) walk.level)
```

```
ID Condition rtt_state post: GranuleAt(rtt).state == GRAN_RTT rtte_addr post: walk.rtte.addr == rtt result post: result.status == RMI_SUCCESS rtte_state post: walk.rtte.state == RTTE_TABLE rtte_c_ripas pre: AddrIsProtected(ipa, realm) post: RttAllEntriesRipas(RttAt(rtt), unfold.ripas) rtte_c_state post: RttAllEntriesState(RttAt(rtt), unfold.state) rtte_c_addr pre: unfold.state != RTTE_VOID post: RttAllEntriesContiguous(RttAt(rtt), unfold.addr, level)
```

## B4.5.57.4 Footprint

| ID        | Value                              |
|-----------|------------------------------------|
| rtt_state | GranuleAt(rtt).state               |
| rtte      | RttEntry(walk.rtt_addr, entry_idx) |

DRAFT