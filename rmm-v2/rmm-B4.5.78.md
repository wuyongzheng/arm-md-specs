## B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command

Removes mappings to conventional memory within a target Unprotected IPA range.

The RMI\_RTT\_UNPROT\_UNMAP command may initiate a Stateful RMI Operation.

## See also:

- A5.3.12 Remove mappings from Unprotected IPA space
- B4.5.77 RMI\_RTT\_UNPROT\_MAP command

## B4.5.78.1 Interface

## B4.5.78.1.1 Input values

| Name   | Register   | Bits   | Type                 | Description                                                                                                                                                                                                                                                                                                                                                                |
|--------|------------|--------|----------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64               | FID, value 0xC40001FC                                                                                                                                                                                                                                                                                                                                                      |
| rd     | X1         | 63:0   | Address              | PA of the RD for the target Realm                                                                                                                                                                                                                                                                                                                                          |
| base   | X2         | 63:0   | Address              | Base of the target IPA range                                                                                                                                                                                                                                                                                                                                               |
| top    | X3         | 63:0   | Address              | Top of the target IPA range                                                                                                                                                                                                                                                                                                                                                |
| flags  | X4         | 63:0   | RmiRttUnmapFlags     | Flags                                                                                                                                                                                                                                                                                                                                                                      |
| oaddr  | X5         | 63:0    RmiAddrSetDesc | Output address set descriptor. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which has been unmapped from the target IPA range. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the PA of a Granule that holds an RMI Address List. This describes a list of PA regions which have been unmapped from the target IPA range. |

## B4.5.78.1.2 Context

The RMI\_RTT\_UNPROT\_UNMAP command operates on the following context.

| Name      | Type             | Value                                                           | Before   | Description                                          |
|-----------|------------------|-----------------------------------------------------------------|----------|------------------------------------------------------|
| realm_pre | RmmRealm         | RealmAt(rd)                                                     | true     | Realm                                                |
| realm     | RmmRealm         | RealmAt(rd)                                                     | false    | Realm                                                |
| size      | UInt64           | UInt(top) - UInt(base)                                          | false    | Size of target IPA range in bytes                    |
| progress  | UInt64           | UInt(out_top) - UInt(base)                                      | false    | Size of IPA range which has been unmapped            |
| walk_pre  | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | true     | Result of RTT walk from base of the target IPA range |

| Name   | Type             | Value                                                           | Before   | Description                                          |
|--------|------------------|-----------------------------------------------------------------|----------|------------------------------------------------------|
| walk   | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of RTT walk from base of the target IPA range |

## B4.5.78.1.3 Output values

| Name      | Register   | Bits   | Type             | Description                                                                                                                                                                                                                                                                                                                                                                                                                           |
|-----------|------------|--------|------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| result    | X0         | 63:0   | RmiResult        | Command result                                                                                                                                                                                                                                                                                                                                                                                                                        |
| out_top   | X1         | 63:0   | Address          | Top IPA of range which has been mapped                                                                                                                                                                                                                                                                                                                                                                                                |
| out_range | X2         | 63:0   | RmiAddrRangeDesc | Output address range. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which has been unmapped from the target IPA range. If flags.oaddr_type != RMI_ADDR_TYPE_SINGLE then this value is zero. Number of entries in output address list. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the number of entries which have been written to the output address list. If flags.oaddr_type != |
| out_count | X3         | 63:0    UInt64     | RMI_ADDR_TYPE_LIST then this value is zero.                                                                                                                                                                                                                                                                                                                                                                                           |

## B4.5.78.2 Failure conditions

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
  * pre: AddrIsProtected(base, realm)
  * post: result.status == RMI_ERROR_INPUT
* oaddr_align
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !AddrIsAligned(oaddr.data.list_addr.addr, 8))
  * post: result.status == RMI_ERROR_INPUT
* oaddr_list_pas
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !NonSecureAccessPermitted( oaddr.data.list_addr.addr))
  * post: result.status == RMI_ERROR_INPUT
* rtte_state
  * pre: walk.rtte.state != RTTE_MAPPED_NS
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_size
  * pre: (walk.rtte.state == RTTE_MAPPED_NS && RttLevelSize(walk.level) > size)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) B4.5.78.2.1 Failure condition ordering The RMI_RTT_UNPROT_UNMAP command does not have any failure condition orderings.

## B4.5.78.3 Success conditions

* state
  * post: RttTreeRangeAllState( realm, RMM_RTT_TREE_PRIMARY, base, out_top, RTTE_UNMAPPED_NS)
* addr_single
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE
  * post: out_range.data.addr ==
* addr_list
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST
  * post: RttTreeRangeAllOaddrList( realm, RMM_RTT_TREE_PRIMARY, base, oaddr.data.list_addr.addr, progress)
* result
  * post: result.status == RMI_SUCCESS

## B4.5.78.4 Footprint

The RMI\_RTT\_UNPROT\_UNMAP command does not have any footprint.