## B4.5.68 RMI\_RTT\_DESTROY command

Destroys a primary RTT.

The RMI\_RTT\_DESTROY command may initiate a Stateful RMI Operation.

## See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)
- [A5.6.9 RTT destruction](rmm-A5.6.md#a569-rtt-destruction)
- [B4.5.64 RMI\_RTT\_CREATE command](rmm-B4.5.64.md)
- [B4.5.72 RMI\_RTT\_FOLD command](rmm-B4.5.72.md)

## B4.5.68.1 Interface

## B4.5.68.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400015E                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| ipa    | X2         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X3         | 63:0   | Int64   | RTT level                                  |

## B4.5.68.1.2 Context

The RMI\_RTT\_DESTROY command operates on the following context.

| Name      | Type             | Value                                                         | Before   | Description                                                                  |
|-----------|------------------|---------------------------------------------------------------|----------|------------------------------------------------------------------------------|
| realm     | RmmRealm         | RealmAt(rd)                                                   | false    | Realm                                                                        |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, RMM_RTT_TREE_PRIMARY)         | false    | RTT walk result                                                              |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                               | false    | RTTE index                                                                   |
| walk_top  | Address          | RttSkipNonLiveEntries( RttAt(walk.rtt_addr), walk.level, ipa) | false    | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |


## B4.5.68.1.3 Output values

| Name   | Register   | Bits   | Type      | Description                                                                  |
|--------|------------|--------|-----------|------------------------------------------------------------------------------|
| result | X0         | 63:0   | RmiResult | Command result                                                               |
| rtt    | X1         | 63:0   | Address   | PA of the RTT which was destroyed                                            |
| top    | X2         | 63:0   | Address   | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

ID

The rtt output value is valid only when the command result is RMI\_SUCCESS.

The values of the result and top output values for different command outcomes are summarized in the following table.

| Scenario                                                     | result                   | top    | walk.rtte.state                                                                      |
|--------------------------------------------------------------|--------------------------|--------|--------------------------------------------------------------------------------------|
| Target RTT exists and is not live                            | RMI_SUCCESS              | ipa    | Before execution: RTTE_TABLE After execution: RTTE_VOID and RIPAS is RIPAS_DESTROYED |
| Missing RTT                                                  | (RMI_ERROR_RTT, < level) | ipa    | RTTE_VOID or RTTE_UNMAPPED_NS                                                        |
| Block mapping at lower level                                 | (RMI_ERROR_RTT, < level) | == ipa | RTTE_DATA or RTTE_MAPPED_NS                                                          |
| Live RTT at target level                                     | (RMI_ERROR_RTT, level)   | == ipa | RTTE_TABLE                                                                           |
| RTT walk was not performed, due to any other command failure | Another error code       | 0      | Unknown                                                                              |

## See also:

- [A5.6.8 RTTE liveness and RTT liveness](rmm-A5.6.md#a568-rtte-liveness-and-rtt-liveness)

## B4.5.68.2 Failure conditions

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
  * pre: !AddrIsRttLevelAligned(ipa, level - 1)
  * post: result.status == RMI_ERROR_INPUT
* ipa_bound
  * pre: UInt(ipa) >= (2 ^ realm.ipa_width)
  * post: result.status == RMI_ERROR_INPUT
* rtt_walk
  * pre: walk.level < level - 1 (
  * post: result.status == RMI_ERROR_RTT && result.data.level.level == walk.level && top == walk_top)
* rtte_state
  * pre: walk.rtte.state != RTTE_TABLE (
  * post: result.status == RMI_ERROR_RTT && result.data.level.level == walk.level && top == walk_top)
* rtt_live
  * pre: RttIsLive(RttAt(walk.rtte.addr))
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == level && top == ipa)
* aux_ref
  * pre: AddrIsAuxRef(ipa, realm)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)

## B4.5.68.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [rtte_state] < [rtt_live, aux_ref] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.5.68.3 Success conditions

* rtt
  * post: rtt == walk.rtte.
* addrtop
  * post: top == walk_top
* result
  * post: result.status == RMI_SUCCESS
* state_prot
  * pre: AddrIsProtected(ipa, realm)
  * post: walk.rtte.state == RTTE_VOID
* ripas
  * pre: AddrIsProtected(ipa, realm)
  * post: walk.rtte.ripas == RIPAS_DESTROYED
* state_unprot
  * pre: !AddrIsProtected(ipa, realm)
  * post: walk.rtte.state == RTTE_UNMAPPED_NS
* rtt_state
  * post: GranuleAt(walk.rtte.addr).state == GRAN_DELEGATED

## B4.5.68.4 Footprint

| ID        | Value                                       |
|-----------|---------------------------------------------|
| rtt_state | GranuleAt(walk.rtte.addr).state             |
| rtte      | RttEntryAt(RttAt(walk.rtt_addr), entry_idx) |

<!-- image -->