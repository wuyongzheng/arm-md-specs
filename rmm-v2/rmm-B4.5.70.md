## B4.5.70 RMI\_RTT\_DEV\_UNMAP command

Removes mappings to device memory within a target Protected IPA range.

The RMI\_RTT\_DEV\_UNMAP command may initiate a Stateful RMI Operation.

## See also:

- A5.3.8 Remove mappings from Protected IPA space to device memory
- Chapter A9 Realm device assignment
- B4.5.69 RMI\_RTT\_DEV\_MAP command

## B4.5.70.1 Interface

## B4.5.70.1.1 Input values

| Name   | Register   | Bits   | Type                 | Description                                                                                                                                                                                                                                                                                                                                                                |
|--------|------------|--------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64               | FID, value 0xC40001F8                                                                                                                                                                                                                                                                                                                                                      |
| rd     | X1         | 63:0   | Address              | PA of the RD for the target Realm                                                                                                                                                                                                                                                                                                                                          |
| base   | X2         | 63:0   | Address              | Base of the target IPA range                                                                                                                                                                                                                                                                                                                                               |
| top    | X3         | 63:0   | Address              | Top of the target IPA range                                                                                                                                                                                                                                                                                                                                                |
| flags  | X4         | 63:0   | RmiRttUnmapFlags     | Flags                                                                                                                                                                                                                                                                                                                                                                      |
| oaddr  | X5         | 63:0   | DRAFT RmiAddrSetDesc | Output address set descriptor. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which has been unmapped from the target IPA range. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the PA of a Granule that holds an RMI Address List. This describes a list of PA regions which have been unmapped from the target IPA range. |

## B4.5.70.1.2 Context

The RMI\_RTT\_DEV\_UNMAP command operates on the following context.

| Name      | Type      | Value                      | Before   | Description                               |
|-----------|-----------|----------------------------|----------|-------------------------------------------|
| rmm       | RmmGlobal | Rmm()                      | false    | RMMglobal state                           |
| realm_pre | RmmRealm  | RealmAt(rd)                | true     | Realm                                     |
| realm     | RmmRealm  | RealmAt(rd)                | false    | Realm                                     |
| size      | UInt64    | UInt(top) - UInt(base)     | false    | Size of target IPA range in bytes         |
| progress  | UInt64    | UInt(out_top) - UInt(base) | false    | Size of IPA range which has been unmapped |

B4.5. RMI commands

| Name        | Type              | Value                                                           | Before   | Description                                                |
|-------------|-------------------|-----------------------------------------------------------------|----------|------------------------------------------------------------|
| walk_pre    | RmmRttWalkResult  | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | true     | Result of RTT walk from base of the target IPA range       |
| oaddr_first | Address           | walk_pre.rtte.addr                                              | false    | PA of start of the output address set                      |
| region      | RmmTrackingRegion | TrackingRegionAt( oaddr_first)                                  | false    | Tracking region containing start of the output address set |
| walk        | RmmRttWalkResult  | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of RTT walk from base of the target IPA range       |

## B4.5.70.1.3 Output values

| Name      | Register   | Bits   | Type                   | Description                                                                                                                                                                                                                                   |
|-----------|------------|--------|------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| result    | X0         | 63:0   | RmiResult              | Command result                                                                                                                                                                                                                                |
| out_top   | X1         | 63:0   | Address                | Top IPA of range which has been mapped                                                                                                                                                                                                        |
| out_range | X2         | 63:0   | DRAFT RmiAddrRangeDesc | Output address range. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which has been unmapped from the target IPA range. If flags.oaddr_type != RMI_ADDR_TYPE_SINGLE then this value is zero.           |
| out_count | X3         | 63:0   | UInt64                 | Number of entries in output address list. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the number of entries which have been written to the output address list. If flags.oaddr_type != RMI_ADDR_TYPE_LIST then this value is zero. |

## B4.5.70.2 Failure conditions

| ID       | Condition                                                                |
|----------|--------------------------------------------------------------------------|
| rd_align | pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT |
| rd_bound | pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT             |

## ID

## Condition

```
DRAFT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT base_align pre: !AddrIsRmiGranuleAligned(base) post: result.status == RMI_ERROR_INPUT top_align pre: !AddrIsRmiGranuleAligned(top) post: result.status == RMI_ERROR_INPUT size_valid pre: UInt(top) <= UInt(base) post: result.status == RMI_ERROR_INPUT ipa_bound pre: !AddrRangeIsProtected(base, top, realm) post: result.status == RMI_ERROR_INPUT oaddr_align pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !AddrIsAligned(oaddr.data.list_addr.addr, 8)) post: result.status == RMI_ERROR_INPUT oaddr_list_pas pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !NonSecureAccessPermitted( oaddr.data.list_addr.addr)) post: result.status == RMI_ERROR_INPUT rtte_state pre: walk.rtte.state != RTTE_NARCH_DEV post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) rtte_size pre: (walk.rtte.state == RTTE_NARCH_DEV && RttLevelSize(walk.level) > size) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) trk_gran pre: (TrackingRegionIsTracked(region) && TrackingRegionGranularity(region) > size) post: result.status == RMI_ERROR_TRACKING dpt_gran pre: (realm.feat_ats == FEATURE_TRUE && !DptEntryCanDescribe(oaddr_first, size)) post: result.status == RMI_ERROR_DPT
```

## B4.5.70.2.1 Failure condition ordering

The RMI\_RTT\_DEV\_UNMAP command does not have any failure condition orderings.

## B4.5.70.3 Success conditions

## Condition

ID

```
state post: RttTreeRangeAllState( realm, RMM_RTT_TREE_PRIMARY, base, out_top, RTTE_VOID) ripas post: RealmIpaRangeAllRipasIf( realm_pre, realm, base, out_top, RIPAS_DEV, RIPAS_DESTROYED) addr_single pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE post: out_range.data.addr == walk_pre.rtte.addr
```

```
ID Condition
```

```
addr_list pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST post: RttTreeRangeAllOaddrList( realm, RMM_RTT_TREE_PRIMARY, base, oaddr.data.list_addr.addr, progress) gran_state_contig pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE post: GranulesAllState( RmiAddrRangeDescDecode(oaddr.data.single).base, progress, GRAN_DELEGATED) gran_state_list pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST post: GranulesAllStateList( oaddr.data.list_addr.addr, progress, GRAN_DELEGATED) result post: result.status == RMI_SUCCESS
```

## B4.5.70.4 Footprint

The RMI\_RTT\_DEV\_UNMAP command does not have any footprint.

DRAFT