## B4.3.16 RMI\_RTT\_DESTROY command

Destroys an RTT.

See also:

- A5.5 Realm Translation Table
- A5.5.9 RTT destruction
- B4.3.15 RMI\_RTT\_CREATE command
- B4.3.17 RMI\_RTT\_FOLD command

## B4.3.16.1 Interface

## B4.3.16.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                |
|--------|------------|--------|---------|--------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400015E                      |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm          |
| ipa    | X2         | 63:0   | Address | Base of the IPA range described by the RTT |
| level  | X3         | 63:0   | Int64   | RTT level                                  |

## B4.3.16.1.2 Context

The RMI\_RTT\_DESTROY command operates on the following context.

| Name      | Type             | Value                                                       | Before   | Description                                                                  |
|-----------|------------------|-------------------------------------------------------------|----------|------------------------------------------------------------------------------|
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, level - 1)                                | false    | RTT walk result                                                              |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                             | false    | RTTE index                                                                   |
| walk_top  | Address          | RttSkipNonLiveEntries( Rtt(walk.rtt_addr), walk.level, ipa) | false    | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

## B4.3.16.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description                                                                  |
|--------|------------|--------|----------------------|------------------------------------------------------------------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status                                                        |
| rtt    | X1         | 63:0   | Address              | PA of the RTT which was destroyed                                            |
| top    | X2         | 63:0   | Address              | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

The rtt output value is valid only when the command result is RMI\_SUCCESS.

ID

The values of the result and top output values for different command outcomes are summarized in the following table.

| Scenario                                                     | result                   | top    | walk.rtte.state                                                            |
|--------------------------------------------------------------|--------------------------|--------|----------------------------------------------------------------------------|
| Target RTT exists and is not live                            | RMI_SUCCESS              | > ipa  | Before execution: TABLE After execution: UNASSIGNED and RIPAS is DESTROYED |
| Missing RTT                                                  | (RMI_ERROR_RTT, < level) | > ipa  | UNASSIGNED or UNASSIGNED_NS                                                |
| Block mapping at lower level                                 | (RMI_ERROR_RTT, < level) | == ipa | ASSIGNED or ASSIGNED_NS                                                    |
| Live RTT at target level                                     | (RMI_ERROR_RTT, level)   | == ipa | TABLE                                                                      |
| RTT walk was not performed, due to any other command failure | Another error code       | 0      | Unknown                                                                    |

## See also:

- A5.5.8 RTTE liveness and RTT liveness

## B4.3.16.2 Failure conditions

Condition

```
rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) level_bound pre: (!RttLevelIsValid(rd, level) || RttLevelIsStarting(rd, level)) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_align pre: !AddrIsRttLevelAligned(ipa, level -1) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_bound pre: UInt(ipa) >= (2 ^ Realm(rd).ipa_width) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_walk pre: walk.level < level -1 post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top)) rtte_state pre: walk.rtte.state != TABLE post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top)) rtt_live pre: RttIsLive(Rtt(walk.rtte.addr)) post: (ResultEqual(result, RMI_ERROR_RTT, level) && (top == ipa))
```

## B4.3.16.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state, rtt_live] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.3.16.3 Success conditions

| ID         | Condition                                  |
|------------|--------------------------------------------|
| rtte_state | walk.rtte.state == UNASSIGNED              |
| ripas      | walk.rtte.ripas == DESTROYED               |
| rtt_state  | Granule(walk.rtte.addr).state == DELEGATED |
| rtt        | rtt == walk.rtte.addr                      |
| top        | top == walk_top                            |

## B4.3.16.4 Footprint

| ID        | Value                              |
|-----------|------------------------------------|
| rtt_state | Granule(walk.rtte.addr).state      |
| rtte      | RttEntry(walk.rtt_addr, entry_idx) |