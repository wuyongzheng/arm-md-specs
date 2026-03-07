## B4.5.73 RMI\_RTT\_INIT\_RIPAS command

Set the RIPAS of a target IPA range to RIPAS\_RAM, for a Realm in the REALM\_NEW state.

The RMI\_RTT\_INIT\_RIPAS command may initiate a Stateful RMI Operation.

## See also:

- A5.2.2 Realm IPA state
- B4.3.5 Range RMI operations
- D1.2.3 Initialize memory of New Realm flow

## B4.5.73.1 Interface

## B4.5.73.1.1 Input values

| Name   | Register   | Bits   | Type    | Description                       |
|--------|------------|--------|---------|-----------------------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC4000168             |
| rd     | X1         | 63:0   | Address | PA of the RD for the target Realm |
| base   | X2         | 63:0   | Address | Base of target IPA region         |
| top    | X3         | 63:0   | Address | Top of target IPA region          |

## B4.5.73.1.2 Context

The RMI\_RTT\_INIT\_RIPAS command operates on the following context.

| Name      | Type             | Value                                                                                  | Before                                                                                 | Description                                                                        |
|-----------|------------------|----------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| rmm       | RmmGlobal        | Rmm()                                                                                  | false                                                                                  | RMMglobal state                                                                    |
| realm_pre | RmmRealm         | RealmAt(rd)                                                                            | true                                                                                   | Realm                                                                              |
| realm     | RmmRealm         | RealmAt(rd)                                                                            | false                                                                                  | Realm                                                                              |
| walk      | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY)                        | false                                                                                  | RTT walk result                                                                    |
| walk_top  | Address          | RttSkipEntriesUnlessVoidOrData( ↪ → RttAt(walk.rtt_addr), walk.level, base, top) false | RttSkipEntriesUnlessVoidOrData( ↪ → RttAt(walk.rtt_addr), walk.level, base, top) false | Top IPA of RTTE_VOID entries, starting from entry at which the RTT walk terminated |


## B4.5.73.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                               |
|---------|------------|--------|-----------|-------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                            |
| out_top | X1         | 63:0   | Address   | Top IPA of range whose RIPAS was modified |

ID

The out\_top output value is valid only when the command result is RMI\_SUCCESS.

When the out\_top output value is valid, it is aligned to the size of the address range described by the RTT entry at the level where the RTT walk terminated.

## B4.5.73.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* size_valid
  * pre: UInt(top) <= UInt(base)
  * post: result.status == RMI_ERROR_INPUT
* top_bound
  * pre: !AddrIsProtected( ToAddress(UInt(top) -rmm.dynamic.rmi_granule_size), realm_pre)
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm_pre.state != REALM_NEW
  * post: result.status == RMI_ERROR_REALM
* base_align
  * pre: !AddrIsRttLevelAligned(base, walk.level)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_state
  * pre: (walk.rtte.state != RTTE_VOID && walk.rtte.state != RTTE_DATA)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* top_gran_align
  * pre: !AddrIsRmiGranuleAligned(top)
  * post: result.status == RMI_ERROR_INPUT
* no_progress
  * pre: UInt(base) == UInt(walk_top)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* not_unassigned
  * pre: Command encounters RTT entry whose state is neither RTTE_VOID nor RTTE_DATA.
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)

## B4.5.73.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [rd_bound, rd_state] < [base_align, rtte_state] [rd_bound, rd_state] < [no_progress, not_unassigned] [top_gran_align] < [no_progress]
```

ID

<!-- image -->

## B4.5.73.3 Success conditions

* rtte_ripas
  * post: RttEntriesInRangeRipas( RttAt(walk.rtt_addr), walk.level, base, walk_top, RIPAS_RAM)
* out_top
  * post: out_top == walk_top

## B4.5.73.4 Footprint

Value

RttAt(walk.rtt\_addr)


ID

rtte