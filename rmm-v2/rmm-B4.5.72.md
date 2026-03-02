## B4.5.72 RMI\_RTT\_FOLD command

Destroys a homogeneous primary RTT.

The RMI\_RTT\_FOLD command may initiate a Stateful RMI Operation.

## See also:

- A5.6 Realm Translation Table
- A5.6.6 RTT folding
- B4.5.64 RMI\_RTT\_CREATE command
- B4.5.68 RMI\_RTT\_DESTROY command

## B4.5.72.1 Interface

## B4.5.72.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000166                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| ipa    | X2         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X3         | 63:0   | Int64   | RTT level                                  |

## B4.5.72.1.2 Context

The RMI\_RTT\_FOLD command operates on the following context.

| Name      | Type             | Value                                                 | Before   | Description           |
|-----------|------------------|-------------------------------------------------------|----------|-----------------------|
| realm     | RmmRealm         | RealmAt(rd)                                           | false    | Realm                 |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, RMM_RTT_TREE_PRIMARY) | false    | RTT walk result       |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                       | false    | RTTE index            |
| fold_pre  | RmmRttEntry      | RttFold( RttAt(walk.rtte.addr))                       | true     | Result of folding RTT |

DRAFT

## B4.5.72.1.3 Output values

| Name   | Register   | Bits   | Type      | Description                       |
|--------|------------|--------|-----------|-----------------------------------|
| result | X0         | 63:0   | RmiResult | Command result                    |
| rtt    | X1         | 63:0   | Address   | PA of the RTT which was destroyed |

The rtt output value is valid only when the command result is RMI\_SUCCESS.

## ID

## B4.5.72.2 Failure conditions

## Condition

```
rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT level_bound pre: (!RttLevelIsValid(realm, level) || RttLevelIsStarting(realm, level)) post: result.status == RMI_ERROR_INPUT ipa_align pre: !AddrIsRttLevelAligned(ipa, level -1) post: result.status == RMI_ERROR_INPUT ipa_bound pre: UInt(ipa) >= (2 ^ realm.ipa_width) post: result.status == RMI_ERROR_INPUT rtt_walk pre: walk.level < level -1 post: (result.status == RMI_ERROR_RTT && result.data.level.level == rtte_state pre: walk.rtte.state != RTTE_TABLE post: (result.status == RMI_ERROR_RTT && result.data.level.level == rtt_homo pre: !RttIsHomogeneous(RttAt(walk.rtte.addr)) post: (result.status == RMI_ERROR_RTT && result.data.level.level == level) aux_ref pre: AddrIsAuxRef(ipa, realm) post: (result.status == RMI_ERROR_RTT && result.data.level.level ==
```

## B4.5.72.2.1 Failure condition ordering

```
DRAFT walk.level) walk.level) walk.level)
```

```
[rd_bound, rd_state] < [rtt_walk, rtte_state, rtt_homo, aux_ref] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.5.72.3 Success conditions

ID

## Condition

```
rtt post: rtt == walk.rtte.addr result post: result.status == RMI_SUCCESS rtte_state post: walk.rtte.state == fold_pre.state rtte_addr pre: fold_pre.state != RTTE_VOID && fold_pre.state != RTTE_UNMAPPED_NS post: walk.rtte.addr == fold_pre.addr rtte_attr_prot pre: fold_pre.state == RTTE_DATA post: (RttMemAttrEqual( walk.rtte, fold_pre, RTT_PROTECTED) && RttS2APEqual( walk.rtte, fold_pre, S2AP_INDIRECT)) rtte_attr_unprot pre: fold_pre.state == RTTE_MAPPED_NS post: (RttMemAttrEqual( walk.rtte, fold_pre, RTT_UNPROTECTED) && RttS2APEqual( walk.rtte, fold_pre, realm.rtt_s2ap_encoding)) rtte_ripas pre: AddrIsProtected(ipa, realm) post: walk.rtte.ripas == fold_pre.ripas rtt_state post: GranuleAt(walk.rtte.addr).state ==
```

## B4.5.72.4 Footprint

| ID        | Value                                       |
|-----------|---------------------------------------------|
| rtt_state | GranuleAt(walk.rtte.addr).state             |
| rtte      | RttEntryAt(RttAt(walk.rtt_addr), entry_idx) |

```
DRAFT GRAN_DELEGATED
```