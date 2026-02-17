## B4.3.17 RMI\_RTT\_FOLD command

Destroys a homogeneous RTT.

See also:

- A5.5 Realm Translation Table
- A5.5.6 RTT folding
- B4.3.15 RMI\_RTT\_CREATE command
- B4.3.16 RMI\_RTT\_DESTROY command

## B4.3.17.1 Interface

## B4.3.17.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000166                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| ipa    | X2         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X3         | 63:0   | Int64   | RTT level                                  |

## B4.3.17.1.2 Context

The RMI\_RTT\_FOLD command operates on the following context.

| Name      | Type             | Value                           | Before   | Description           |
|-----------|------------------|---------------------------------|----------|-----------------------|
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, level - 1)    | false    | RTT walk result       |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level) | false    | RTTE index            |
| fold      | RmmRttEntry      | RttFold( Rtt(walk.rtte.addr))   | true     | Result of folding RTT |

## B4.3.17.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description                       |
|--------|------------|--------|----------------------|-----------------------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status             |
| rtt    | X1         | 63:0   | Address              | PA of the RTT which was destroyed |

The rtt output value is valid only when the command result is RMI\_SUCCESS.

## B4.3.17.2 Failure conditions

ID

## Condition

```
rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) level_bound pre: (!RttLevelIsValid(rd, level) || RttLevelIsStarting(rd, level)) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_align pre: !AddrIsRttLevelAligned(ipa, level -1) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_bound pre: UInt(ipa) >= (2 ^ Realm(rd).ipa_width) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_walk pre: walk.level < level -1 post: ResultEqual(result, RMI_ERROR_RTT, walk.level) rtte_state pre: walk.rtte.state != TABLE post: ResultEqual(result, RMI_ERROR_RTT, walk.level) rtt_homo pre: !RttIsHomogeneous(Rtt(walk.rtte.addr)) post: ResultEqual(result, RMI_ERROR_RTT, level)
```

## B4.3.17.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state, rtt_homo] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.3.17.3 Success conditions

## Condition

ID

```
rtte_state walk.rtte.state == fold.state rtte_addr pre: (fold.state != UNASSIGNED && fold.state != UNASSIGNED_NS) post: walk.rtte.addr == fold.addr
```

| ID         | Condition                                                                                                     |
|------------|---------------------------------------------------------------------------------------------------------------|
| rtte_attr  | pre: (fold.state == ASSIGNED &#124;&#124; fold.state == ASSIGNED_NS) post: (walk.rtte.MemAttr == fold.MemAttr |
| rtte_ripas | pre: AddrIsProtected(ipa, Realm(rd)) post: walk.rtte.ripas == fold.ripas                                      |
| rtt_state  | Granule(walk.rtte.addr).state == DELEGATED                                                                    |
| rtt        | rtt == walk.rtte.addr                                                                                         |

## B4.3.17.4 Footprint

| ID        | Value                              |
|-----------|------------------------------------|
| rtt_state | Granule(walk.rtte.addr).state      |
| rtte      | RttEntry(walk.rtt_addr, entry_idx) |