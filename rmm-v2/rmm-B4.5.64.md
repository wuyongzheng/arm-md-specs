## B4.5.64 RMI\_RTT\_CREATE command

Creates a primary RTT.

The RMI\_RTT\_CREATE command may initiate a Stateful RMI Operation.

See also:

- [A5.6 Realm Translation Table](rmm-A5.6.md)
- [A5.6.7 RTT unfolding](rmm-A5.6.md#a567-rtt-unfolding)
- [B4.5.68 RMI\_RTT\_DESTROY command](rmm-B4.5.68.md)
- [B4.5.72 RMI\_RTT\_FOLD command](rmm-B4.5.72.md)

## B4.5.64.1 Interface

## B4.5.64.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400015D                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| rtt    | X2         | 63:0   | Address | PA of the target RTT                       |
| ipa    | X3         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X4         | 63:0   | Int64   | RTT level                                  |

## B4.5.64.1.2 Context

The RMI\_RTT\_CREATE command operates on the following context.

| Name      | Type             | Value                                                 | Before   | Description                              |
|-----------|------------------|-------------------------------------------------------|----------|------------------------------------------|
| realm     | RmmRealm         | RealmAt(rd)                                           | false    | Realm                                    |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, RMM_RTT_TREE_PRIMARY) | false    | RTT walk result                          |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                       | false    | RTTE index                               |
| walk_pre  | RmmRttWalkResult | RttWalk( realm, ipa, level - 1, RMM_RTT_TREE_PRIMARY) | true     | RTT walk result before command execution |
| rtte_pre  | RmmRttEntry      | walk_pre.rtte                                         | true     | RTTE before command execution            |


## B4.5.64.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

## B4.5.64.2 Failure conditions


## ID Condition rd\_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI\_ERROR\_INPUT rd\_bound pre: !PaIsTracked(rd) post: result.status == RMI\_ERROR\_INPUT rd\_state pre: GranuleAt(rd).state != GRAN\_RD post: result.status == RMI\_ERROR\_INPUT level\_bound pre: (!RttLevelIsValid(realm, level) || RttLevelIsStarting(realm, level)) post: result.status == RMI\_ERROR\_INPUT ipa\_align pre: !AddrIsRttLevelAligned(ipa, level -1) post: result.status == RMI\_ERROR\_INPUT ipa\_bound pre: UInt(ipa) &gt;= (2 ^ realm.ipa\_width) post: result.status == RMI\_ERROR\_INPUT rtt\_align pre: !AddrIsRmiGranuleAligned(rtt) post: result.status == RMI\_ERROR\_INPUT rtt\_bound pre: !PaIsDelegableConventionalFine(rtt) post: result.status == RMI\_ERROR\_INPUT rtt\_state pre: GranuleAt(rtt).state != GRAN\_DELEGATED post: result.status == RMI\_ERROR\_INPUT rtt\_bound2 pre: ((realm.feat\_lpa2 == FEATURE\_FALSE) &amp;&amp; (UInt(rtt) &gt;= 2^48)) post: result.status == RMI\_ERROR\_INPUT rtt\_walk pre: walk.level &lt; level -1 post: (result.status == RMI\_ERROR\_RTT &amp;&amp; result.data.level.level == walk.level) rtte\_state pre: walk.rtte.state == RTTE\_TABLE post: (result.status == RMI\_ERROR\_RTT &amp;&amp; result.data.level.level == walk.level) B4.5.64.2.1 Failure condition ordering [rd\_bound, rd\_state] &lt; [rtt\_walk, rtte\_state] [level\_bound, ipa\_bound] &lt; [rtt\_walk, rtte\_state] rd\_align rd\_bound rtt\_walk rd\_state level\_bound ipa\_bound ipa\_align rtt\_align rtt\_bound rtt\_state rtt\_bound2 rtte\_state
## B4.5.64.3 Success conditions

* rtt_state
  * post: GranuleAt(rtt).state == GRAN_RTT
* rtte_addr
  * post: walk.rtte.addr == rtt
* result
  * post: result.status == RMI_SUCCESS
* rtte_state
  * post: walk.rtte.state == RTTE_TABLE
* rtte_c_ripas
  * pre: AddrIsProtected(ipa, realm)
  * post: RttAllEntriesRipas(RttAt(rtt), rtte_pre.ripas)
* rtte_c_state
  * post: RttAllEntriesState(RttAt(rtt), rtte_pre.state)
* rtte_c_addr
  * pre: rtte_pre.state != RTTE_VOID && rtte_pre.state != RTTE_UNMAPPED_NS
  * post: RttAllEntriesContiguous(RttAt(rtt), rtte_pre.addr, level)
* rtte_c_mem_attr
  * pre: rtte_pre.state != RTTE_VOID && rtte_pre.state != RTTE_UNMAPPED_NS
  * post: RttAllEntriesMemAttr(RttAt(rtt), rtte_pre)
* rtte_c_s2ap
  * pre: AddrIsProtected(ipa, realm)
  * post: RttAllEntriesS2AP(RttAt(rtt), rtte_pre)

## B4.5.64.4 Footprint

| ID        | Value                                       |
|-----------|---------------------------------------------|
| rtt_state | GranuleAt(rtt).state                        |
| rtte      | RttEntryAt(RttAt(walk.rtt_addr), entry_idx) |

