## B4.5.75 RMI\_RTT\_SET\_RIPAS command

Completes a request made by the Realm to change the RIPAS of a target IPA range.

The RMI\_RTT\_SET\_RIPAS command may initiate a Stateful RMI Operation.

See also:

- [A5.4 RIPAS change](rmm-A5.4.md)

## B4.5.75.1 Interface

## B4.5.75.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                       |
|---------|------------|--------|---------|-----------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC4000169             |
| rd      | X1         | 63:0   | Address | PA of the RD for the target Realm |
| rec_ptr | X2         | 63:0   | Address | PA of the target REC              |
| base    | X3         | 63:0   | Address | Base of target IPA region         |
| top     | X4         | 63:0   | Address | Top of target IPA region          |

## B4.5.75.1.2 Context

The RMI\_RTT\_SET\_RIPAS command operates on the following context.

| Name         | Type             | Value                                                                                                                                              | Before   | Description                                                                                                 |
|--------------|------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|----------|-------------------------------------------------------------------------------------------------------------|
| realm        | RmmRealm         | RealmAt(rd)                                                                                                                                        | false    | Realm                                                                                                       |
| realm_pre    | RmmRealm         | RealmAt(rd)                                                                                                                                        | true     | Realm                                                                                                       |
| rec          | RmmRec           | RecAt(rec_ptr)                                                                                                                                     | false    | REC                                                                                                         |
| walk         | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY)                                                                                    | false    | RTT walk result                                                                                             |
| ripas_pre    | RmmRipas         | walk.rtte.ripas                                                                                                                                    | true     | RIPAS before the command executed                                                                           |
| walk_top_pre | Address          | RttSkipEntriesWithRipas( RttAt(walk.rtt_addr), walk.level, base, top, (rec.ripas_value == RIPAS_RAM) && (rec.ripas_destroyed != CHANGE_DESTROYED)) | true     | Top IPA of entries which have associated RIPAS values, starting from entry at which the RTT walk terminated |


## B4.5.75.1.3 Output values

ID

| Name    | Register   | Bits   | Type      | Description                               |
|---------|------------|--------|-----------|-------------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                            |
| out_top | X1         | 63:0   | Address   | Top IPA of range whose RIPAS was modified |

The out\_top output value is valid only when the command result is RMI\_SUCCESS.

## B4.5.75.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* rec_align
  * pre: !AddrIsRmiGranuleAligned(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_bound
  * pre: !PaIsTracked(rec_ptr)
  * post: result.status == RMI_ERROR_INPUT
* rec_gran_state
  * pre: GranuleAt(rec_ptr).state != GRAN_REC
  * post: result.status == RMI_ERROR_INPUT
* rec_state
  * pre: rec.state == REC_RUNNING
  * post: result.status == RMI_ERROR_REC
* rec_owner
  * pre: rec.owner !=
* rd
  * post: result.status == RMI_ERROR_REC
* size_valid
  * pre: UInt(top) <= UInt(base)
  * post: result.status == RMI_ERROR_INPUT
* base_bound
  * pre: base != rec.
* ripas_addr
  * post: result.status == RMI_ERROR_INPUT
* top_bound
  * pre: UInt(top) > UInt(rec.ripas_top)
  * post: result.status == RMI_ERROR_INPUT
* base_align
  * pre: (!AddrIsRttLevelAligned(base, walk.level) && ripas_pre != rec.ripas_value)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* top_gran_align
  * pre: !AddrIsRmiGranuleAligned(top)
  * post: result.status == RMI_ERROR_INPUT
* no_progress
  * pre: (UInt(base) == UInt(walk_top_pre) && ripas_pre != rec.ripas_value)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* aux_live
  * pre: AddrRangeIsAuxLive(base, top, realm_pre)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) ram_invalid whose
* state
  * pre: ripas == RIPAS_RAM and command encounters RTT entry is neither RTTE_DATA nor RTTE_VOID.
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)

## B4.5.75.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [base_align] [rd_bound, rd_state] < [no_progress] [rec_bound, rec_gran_state] < [rec_state, [base_bound] < [base_align] [top_gran_align] < [no_progress]
```

```
rec_owner]
```

<!-- image -->

## B4.5.75.3 Success conditions

* rtte_ripas
  * post: RttEntriesInRangeRipas( RttAt(walk.rtt_addr), walk.level, base, walk_top_pre, rec.ripas_value)
* ripas_addr
  * post: rec.ripas_addr == MinAddress(top, walk_top_pre)
* out_top
  * post: out_top == MinAddress(top, walk_top_pre)

## B4.5.75.4 Footprint

| ID         | Value                |
|------------|----------------------|
| rtte       | RttAt(walk.rtt_addr) |
| ripas_addr | rec.ripas_addr       |