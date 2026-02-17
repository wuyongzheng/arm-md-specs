## B4.3.2 RMI\_DATA\_CREATE\_UNKNOWN command

Creates a Data Granule with unknown contents.

See also:

- A2.2.4 Granule wiping
- Chapter A5 Realm memory management
- B4.3.3 RMI\_DATA\_DESTROY command
- D1.5.1 Add memory to Active Realm flow

## B4.3.2.1 Interface

## B4.3.2.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                                                 |
|--------|------------|--------|---------|-------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000154                                       |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm                           |
| data   | X2         | 63:0   | Address | PA of the target Data                                       |
| ipa    | X3         | 63:0   | Address | IPA at which the Granule will be mapped in the target Realm |

## B4.3.2.1.2 Context

The RMI\_DATA\_CREATE\_UNKNOWN command operates on the following context.

| Name      | Type             | Value                                 | Before   | Description     |
|-----------|------------------|---------------------------------------|----------|-----------------|
| realm     | RmmRealm         | Realm(rd)                             | false    | Realm           |
| walk      | RmmRttWalkResult | RttWalk( rd, ipa, RMM_RTT_PAGE_LEVEL) | false    | RTT walk result |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)       | false    | RTTE index      |

## B4.3.2.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description           |
|--------|------------|--------|----------------------|-----------------------|
| result | X0         | 63:0   | RmiCommandReturnCode | Command return status |

## B4.3.2.2 Failure conditions

| ID         | Condition                                                                   |
|------------|-----------------------------------------------------------------------------|
| data_align | pre: !AddrIsGranuleAligned(data) post: ResultEqual(result, RMI_ERROR_INPUT) |
| data_bound | pre: !PaIsDelegable(data) post: ResultEqual(result, RMI_ERROR_INPUT)        |

ID

## Condition

```
data_state pre: Granule(data).state != DELEGATED post: ResultEqual(result, RMI_ERROR_INPUT) data_bound2 pre: ((realm.feat_lpa2 == FEATURE_FALSE) && (UInt(data) >= 2^48)) post: ResultEqual(result, RMI_ERROR_INPUT) rd_align pre: !AddrIsGranuleAligned(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_bound pre: !PaIsDelegable(rd) post: ResultEqual(result, RMI_ERROR_INPUT) rd_state pre: Granule(rd).state != RD post: ResultEqual(result, RMI_ERROR_INPUT) ipa_align pre: !AddrIsGranuleAligned(ipa) post: ResultEqual(result, RMI_ERROR_INPUT) ipa_bound pre: !AddrIsProtected(ipa, Realm(rd)) post: ResultEqual(result, RMI_ERROR_INPUT) rtt_walk pre: walk.level < RMM_RTT_PAGE_LEVEL post: ResultEqual(result, RMI_ERROR_RTT, walk.level) rtte_state pre: walk.rtte.state != UNASSIGNED post: ResultEqual(result, RMI_ERROR_RTT, walk.level)
```

## B4.3.2.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [rtt_walk, rtte_state] [ipa_bound] < [rtt_walk, rtte_state]
```

<!-- image -->

## B4.3.2.3 Success conditions

## Condition

ID

data\_state data\_content

rtte\_state rtte\_addr

Granule(data).state

Contents of

target walk.rtte.state

==

walk.rtte.addr

## B4.3.2.4 Footprint

==

==

DATA

Granule

ASSIGNED

data are

wiped.

| ID         | Value                              |
|------------|------------------------------------|
| data_state | Granule(data).state                |
| rtte       | RttEntry(walk.rtt_addr, entry_idx) |