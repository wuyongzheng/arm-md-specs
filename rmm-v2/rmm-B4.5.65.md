## B4.5.65 RMI\_RTT\_DATA\_MAP command

Create mappings to conventional memory within a target Protected IPA range.

The RMI\_RTT\_DATA\_MAP command may initiate a Stateful RMI Operation.

## See also:

- A2.3.8 Granule wiping
- [A5.3.5 Create mappings from Protected IPA space to wiped conventional memory](rmm-A5.3.md#a535-create-mappings-from-protected-ipa-space-to-wiped-conventional-memory)
- [B4.5.67 RMI\_RTT\_DATA\_UNMAP command](rmm-B4.5.67.md)
- [D1.5.1 Add memory to Active Realm flow](rmm-D1.5.md#d151-add-memory-to-active-realm-flow)

## B4.5.65.1 Interface

## B4.5.65.1.1 Input values

| Name   | Register   | Bits   | Type                     | Description                                                                                                                                                                                                                                                                                                                                                         |
|--------|------------|--------|--------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64                   | FID, value 0xC40001F5                                                                                                                                                                                                                                                                                                                                               |
| rd     | X1         | 63:0   | Address                  | PA of the RD for the target Realm                                                                                                                                                                                                                                                                                                                                   |
| base   | X2         | 63:0   | Address                  | Base of the target IPA range                                                                                                                                                                                                                                                                                                                                        |
| top    | X3         | 63:0   | Address                  | Top of the target IPA range                                                                                                                                                                                                                                                                                                                                         |
| flags  | X4         | 63:0    RmiRttProtMapFlags | Flags                                                                                                                                                                                                                                                                                                                                                               |
| oaddr  | X5         | 63:0   | RmiAddrSetDesc           | Output address set descriptor. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which will be mapped into the target IPA range. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the PA of a Granule that holds an RMI Address List. This describes a list of PA regions which will be mapped into the target IPA range. |

## B4.5.65.1.2 Context

The RMI\_RTT\_DATA\_MAP command operates on the following context.

| Name     | Type     | Value                      | Before   | Description                             |
|----------|----------|----------------------------|----------|-----------------------------------------|
| realm    | RmmRealm | RealmAt(rd)                | false    | Realm                                   |
| size     | UInt64   | UInt(top) - UInt(base)     | false    | Size of target IPA range in bytes       |
| progress | UInt64   | UInt(out_top) - UInt(base) | false    | Size of IPA range which has been mapped |

| Name        | Type              | Value                                                           | Before   | Description                                                |
|-------------|-------------------|-----------------------------------------------------------------|----------|------------------------------------------------------------|
| walk        | RmmRttWalkResult  | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of RTT walk from base of the target IPA range       |
| oaddr_first | Address           | AddrSetEntry( oaddr, flags.oaddr_type, 0)                       | false    | PA of start of the output address set                      |
| region      | RmmTrackingRegion | TrackingRegionAt( oaddr_first)                                  | false    | Tracking region containing start of the output address set |

## B4.5.65.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                            |
|---------|------------|--------|-----------|----------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                         |
| out_top | X1         | 63:0   | Address   | Top IPA of range which has been mapped |

## B4.5.65.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* base_align
  * pre: !AddrIsRmiGranuleAligned(base)
  * post: result.status == RMI_ERROR_INPUT
* top_align
  * pre: !AddrIsRmiGranuleAligned(top)
  * post: result.status == RMI_ERROR_INPUT
* size_valid
  * pre: UInt(top) <= UInt(base)
  * post: result.status == RMI_ERROR_INPUT
* ipa_bound
  * pre: !AddrRangeIsProtected(base, top, realm)
  * post: result.status == RMI_ERROR_INPUT
* oaddr_single_align
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_SINGLE && !AddrIsRmiGranuleAligned(oaddr.data.single.addr))
  * post: result.status == RMI_ERROR_INPUT
* oaddr_list_align
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !AddrIsAligned(oaddr.data.list_addr.addr, 8))
  * post: result.status == RMI_ERROR_INPUT
* oaddr_type
  * pre: (flags.oaddr_type != RMI_ADDR_TYPE_SINGLE && flags.oaddr_type != RMI_ADDR_TYPE_LIST)
  * post: result.status == RMI_ERROR_INPUT
* oaddr_list_pas
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !NonSecureAccessPermitted(oaddr.data.list_addr.addr))
  * post: result.status == RMI_ERROR_INPUT
* rtte_state
  * pre: walk.rtte.state != RTTE_VOID
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_size
  * pre: (walk.rtte.state == RTTE_VOID && RttLevelSize(walk.level) > size)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* trk_untracked
  * pre: !TrackingRegionIsTracked(region)
  * post: result.status == RMI_ERROR_TRACKING
* trk_gran
  * pre: (TrackingRegionIsTracked(region) && TrackingRegionGranularity(region) > size)
  * post: result.status == RMI_ERROR_TRACKING
* gran_state
  * pre: GranuleAt(oaddr_first).state != GRAN_DELEGATED
  * post: result.status == RMI_ERROR_INPUT
* dpt_gran
  * pre: (realm.feat_ats == FEATURE_TRUE && !DptEntryCanDescribe(oaddr_first, size))
  * post: result.status == RMI_ERROR_DPT B4.5.65.2.1 Failure condition ordering The RMI_RTT_DATA_MAP command does not have any failure condition orderings.

## B4.5.65.3 Success conditions

* gran_contents
  * post: Contents of first size bytes of output address set are wiped.
* gran_state_contig
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE
  * post: GranulesAllState( RmiAddrRangeDescDecode(oaddr.data.single).base, size, GRAN_DATA)
* gran_state_list
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST
  * post: GranulesAllStateList( oaddr.data.list_addr.addr, size, GRAN_DATA)
* result
  * post: result.status == RMI_SUCCESS
* state
  * post: RttTreeRangeAllState( realm, RMM_RTT_TREE_PRIMARY, base, out_top, RTTE_DATA)
* addr_contig
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE
  * post: RttTreeRangeAllOaddrContig( realm, RMM_RTT_TREE_PRIMARY, base, progress)
* addr_list
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST
  * post: RttTreeRangeAllOaddrList( realm, RMM_RTT_TREE_PRIMARY, base, oaddr.data.list_addr.addr, progress)
* memattr
  * post: RttTreeRangeAllMemAttr( realm, RMM_RTT_TREE_PRIMARY, base, out_top, MEMATTR_CACHEABLE)
* shareability
  * post: RttTreeRangeAllShareability( realm, RMM_RTT_TREE_PRIMARY, base, out_top, SHAREABILITY_INNER)

## B4.5.65.4 Footprint

The RMI\_RTT\_DATA\_MAP command does not have any footprint.

<!-- image -->