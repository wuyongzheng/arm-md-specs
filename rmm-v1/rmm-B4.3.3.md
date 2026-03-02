## B4.3.3 RMI\_DATA\_DESTROY command

Destroys a Data Granule.

See also:

- Chapter A5 Realm memory management
- B4.3.1 RMI\_DATA\_CREATE command
- B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command
- D1.2.5 Realm destruction flow

## B4.3.3.1 Interface

## B4.3.3.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                            |
|--------|------------|--------|---------|--------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000155                                  |
| rd     | X1         | 63:0   | Address | PA of the RD which owns the target Data                |
| ipa    | X2         | 63:0   | Address | IPA at which the Granule is mapped in the target Realm |

## B4.3.3.1.2 Context

The RMI\_DATA\_DESTROY command operates on the following context.

| Name      | Type             | Value                                                       | Before   | Description                                                                  |
|-----------|------------------|-------------------------------------------------------------|----------|------------------------------------------------------------------------------|
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, RMM_RTT_PAGE_LEVEL)                       | false    | RTT walk result                                                              |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                             | false    | RTTE index                                                                   |
| walk_top  | Address          | RttSkipNonLiveEntries( Rtt(walk.rtt_addr), walk.level, ipa) | false    | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

## B4.3.3.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description                                                                  |
|--------|------------|--------|----------------------|------------------------------------------------------------------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status                                                        |
| data   | X1         | 63:0   | Address              | PA of the Data Granule which was destroyed                                   |
| top    | X2         | 63:0   | Address              | Top IPA of non-live RTT entries, from entry at which the RTT walk terminated |

The data output value is valid only when the command result is RMI\_SUCCESS.

ID

The values of the result and top output values for different command outcomes are summarized in the following table.

| Scenario                                                     | result                           | top    | walk.rtte.state                                                               |
|--------------------------------------------------------------|----------------------------------|--------|-------------------------------------------------------------------------------|
| ipa is mapped as a page                                      | RMI_SUCCESS                      | > ipa  | Before execution: ASSIGNED After execution: UNASSIGNED and RIPAS is DESTROYED |
| ipa is not mapped                                            | (RMI_ERROR_RTT, <= 3)            | > ipa  | UNASSIGNED                                                                    |
| ipa is mapped as a block                                     | (RMI_ERROR_RTT, 0 0 < level < 3) | == ipa | ASSIGNED                                                                      |
| RTT walk was not performed, due to any other command failure | Another error code               | 0      | Unknown                                                                       |

## See also:

- A5.5.8 RTTE liveness and RTT liveness

## B4.3.3.2 Failure conditions

## Condition

```
rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) ipa_align pre: !AddrIsGranuleAligned(ipa) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_bound pre: !AddrIsProtected(ipa, Realm(rd)) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_walk pre: walk.level < RMM_RTT_PAGE_LEVEL post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top)) rtte_state pre: walk.rtte.state != ASSIGNED post: (ResultEqual(result, RMI_ERROR_RTT, walk.level) && (top == walk_top))
```

## B4.3.3.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [ipa_bound] < [rtt_walk, rtte_state]
```

## ID

<!-- image -->

## B4.3.3.3 Success conditions

## Condition

data\_state

Granule(walk.rtte.addr).state == DELEGATED

rtte\_state

walk.rtte.state == UNASSIGNED

ripas\_ram

pre:

walk.rtte.ripas == RAM

post:

walk.rtte.ripas == DESTROYED

data

data == walk.rtte.addr

top

top == walk\_top

## B4.3.3.4 Footprint

| ID         | Value                              |
|------------|------------------------------------|
| data_state | Granule(walk.rtte.addr).state      |
| rtte       | RttEntry(walk.rtt_addr, entry_idx) |