## B4.5.59 RMI\_RTT\_AUX\_FOLD command

Destroys a homogeneous auxiliary RTT.

The RMI\_RTT\_AUX\_FOLD command may initiate a Stateful RMI Operation.

See also:

- [A5.6.6 RTT folding](rmm-A5.6.md#a566-rtt-folding)
- [A10.3.1 Auxiliary RTT](rmm-A10.3.md#a1031-auxiliary-rtt)
- [B4.5.57 RMI\_RTT\_AUX\_CREATE command](rmm-B4.5.57.md)
- [B4.5.58 RMI\_RTT\_AUX\_DESTROY command](rmm-B4.5.58.md)

## B4.5.59.1 Interface

## B4.5.59.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400017F                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| ipa    | X2         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X3         | 63:0   | Int64   | RTT level                                  |
| index  | X4         | 63:0   | UInt64  | RTT tree index                             |

## B4.5.59.1.2 Context

The RMI\_RTT\_AUX\_FOLD command operates on the following context.

| Name      | Type             | Value                                  | Before   | Description           |
|-----------|------------------|----------------------------------------|----------|-----------------------|
| realm     | RmmRealm         | RealmAt(rd)                            | false    | Realm                 |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, index) | false    | RTT walk result       |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)        | false    | RTTE index            |
| fold_pre  | RmmRttEntry      | RttFold( RttAt(walk.rtte.addr))        | true     | Result of folding RTT |


## B4.5.59.1.3 Output values

| Name   | Register   | Bits   | Type      | Description                       |
|--------|------------|--------|-----------|-----------------------------------|
| result | X0         | 63:0   | RmiResult | Command result                    |
| rtt    | X1         | 63:0   | Address   | PA of the RTT which was destroyed |

## ID

## B4.5.59.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* level_bound
  * pre: (!RttLevelIsValid(realm, level) || RttLevelIsStarting(realm, level))
  * post: result.status == RMI_ERROR_INPUT
* ipa_align
  * pre: !AddrIsRttLevelAligned(ipa, level -1)
  * post: result.status == RMI_ERROR_INPUT
* ipa_bound
  * pre: !AddrIsProtected(ipa, realm)
  * post: result.status == RMI_ERROR_INPUT
* index_bound
  * pre: (realm.rtt_tree_per_plane == FEATURE_FALSE || index == RMM_RTT_TREE_PRIMARY || index > realm.num_aux_planes)
  * post: result.status == RMI_ERROR_INPUT
* rtt_walk
  * pre: walk.level < level -1
  * post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level == walk.level)
* rtte_state
  * pre: walk.rtte.state != RTTE_TABLE
  * post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level == walk.level)
* rtt_homo
  * pre: !RttIsHomogeneous(RttAt(walk.rtte.addr))
  * post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level == level)

## B4.5.59.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state, rtt_homo] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.5.59.3 Success conditions

* rtt
  * post: rtt == walk.rtte.addr
* result
  * post: result.status == RMI_SUCCESS
* rtte_state
  * post: walk.rtte.state == fold_pre.state
* rtte_addr
  * pre: fold_pre.state != RTTE_VOID && fold_pre.state != RTTE_UNMAPPED_NS
  * post: walk.rtte.addr == fold_pre.addr
* rtte_attr_prot
  * pre: fold_pre.state == RTTE_DATA
  * post: (RttMemAttrEqual( walk.rtte, fold_pre, RTT_PROTECTED) && RttS2APEqual( walk.rtte, fold_pre, S2AP_INDIRECT))
* rtte_attr_unprot
  * pre: fold_pre.state == RTTE_MAPPED_NS
  * post: (RttMemAttrEqual( walk.rtte, fold_pre, RTT_UNPROTECTED) && RttS2APEqual( walk.rtte, fold_pre, realm.rtt_s2ap_encoding))
* rtte_ripas
  * pre: AddrIsProtected(ipa, realm)
  * post: walk.rtte.ripas == fold_pre.ripas
* rtt_state
  * post: GranuleAt(walk.rtte.addr).state == GRAN_DELEGATED

## B4.5.59.4 Footprint

| ID        | Value                              |
|-----------|------------------------------------|
| rtt_state | GranuleAt(walk.rtte.addr).state    |
| rtte      | RttEntry(walk.rtt_addr, entry_idx) |

```
```