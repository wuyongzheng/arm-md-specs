## B4.3.22 RMI\_RTT\_UNMAP\_UNPROTECTED command

Removes a mapping at an Unprotected IPA.

## See also:

- A5.5 Realm Translation Table
- B4.3.19 RMI\_RTT\_MAP\_UNPROTECTED command

## B4.3.22.1 Interface

## B4.3.22.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000162                                  |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm                      |
| ipa    | X2         | 63:0   | Address | IPA at which the Granule is mapped in the target Realm |
| level  | X3         | 63:0   | Int64   | RTT level                                              |

## B4.3.22.1.2 Context

The RMI\_RTT\_UNMAP\_UNPROTECTED command operates on the following context.

| Name      | Type             | Value                                                       | Before   | Description                                                                  |
|-----------|------------------|-------------------------------------------------------------|----------|------------------------------------------------------------------------------|
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, level)                                    | false    | RTT walk result                                                              |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                             | false    | RTTE index                                                                   |
| walk_top  | Address          | RttSkipNonLiveEntries( Rtt(walk.rtt_addr), walk.level, ipa) | false    | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

## B4.3.22.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description                                                                  |
|--------|------------|--------|----------------------|------------------------------------------------------------------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status                                                        |
| top    | X1         | 63:0   | Address              | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

The values of the result and top output values for different command outcomes are summarized in the following table.

| Scenario                                                     | result                    | top    | walk.rtte.state                                              |
|--------------------------------------------------------------|---------------------------|--------|--------------------------------------------------------------|
| ipa is mapped at the target level                            | RMI_SUCCESS               | > ipa  | Before execution: ASSIGNED_NS After execution: UNASSIGNED_NS |
| ipa is not mapped                                            | (RMI_ERROR_RTT, <= level) | > ipa  | UNASSIGNED_NS                                                |
| ipa is mapped at a lower level                               | (RMI_ERROR_RTT, < level)  | == ipa | ASSIGNED_NS                                                  |
| RTT walk was not performed, due to any other command failure | Another error code        | 0      | Unknown                                                      |

## See also:

- A5.5.8 RTTE liveness and RTT liveness

## B4.3.22.2 Failure conditions

| ID          | Condition                                                                                                                             |
|-------------|---------------------------------------------------------------------------------------------------------------------------------------|
| rd_align    | pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT)                                                             |
| rd_bound    | pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT)                                                                    |
| rd_state    | pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT)                                                               |
| level_bound | pre: !RttLevelIsBlockOrPage(rd, level) post: ResultEqual(result, RMI_ERROR_INPUT)                                                     |
| ipa_align   | pre: !AddrIsRttLevelAligned(ipa, level) post: ResultEqual(result, RMI_ERROR_INPUT)                                                    |
| ipa_bound   | pre: (UInt(ipa) >= (2 ^ Realm(rd).ipa_width) &#124;&#124; AddrIsProtected(ipa, Realm(rd))) post: ResultEqual(result, RMI_ERROR_INPUT) |
| rtt_walk    | pre: walk.level < level post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top))                                   |
| rtte_state  | pre: walk.rtte.state != ASSIGNED_NS post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top))                       |

## B4.3.22.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [level_bound, ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.3.22.3 Success conditions

| ID         | Condition                        |
|------------|----------------------------------|
| rtte_state | walk.rtte.state == UNASSIGNED_NS |
| top        | top == walk_top                  |

## B4.3.22.4 Footprint

| ID   | Value                              |
|------|------------------------------------|
| rtte | RttEntry(walk.rtt_addr, entry_idx) |