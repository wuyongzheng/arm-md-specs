## B4.5.77 RMI\_RTT\_UNPROT\_MAP command

Create mappings to conventional memory within a target Unprotected IPA range.

The RMI\_RTT\_UNPROT\_MAP command may initiate a Stateful RMI Operation.

## See also:

- A5.3.11 Create mappings from Unprotected IPA space
- B4.5.78 RMI\_RTT\_UNPROT\_UNMAP command

## B4.5.77.1 Interface

## B4.5.77.1.1 Input values

| Name   | Register   | Bits   | Type                       | Description                                                                                                                                                                                                                                                                                                                                                         |
|--------|------------|--------|----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64                     | FID, value 0xC40001FB                                                                                                                                                                                                                                                                                                                                               |
| rd     | X1         | 63:0   | Address                    | PA of the RD for the target Realm                                                                                                                                                                                                                                                                                                                                   |
| base   | X2         | 63:0   | Address                    | Base of the target IPA range                                                                                                                                                                                                                                                                                                                                        |
| top    | X3         | 63:0   | Address                    | Top of the target IPA range                                                                                                                                                                                                                                                                                                                                         |
| flags  | X4         | 63:0    RmiRttUnprotMapFlags | Flags                                                                                                                                                                                                                                                                                                                                                               |
| oaddr  | X5         | 63:0   | RmiAddrSetDesc             | Output address set descriptor. If flags.oaddr_type == RMI_ADDR_TYPE_SINGLE then this describes a contiguous PA range which will be mapped into the target IPA range. If flags.oaddr_type == RMI_ADDR_TYPE_LIST then this is the PA of a Granule that holds an RMI Address List. This describes a list of PA regions which will be mapped into the target IPA range. |

## B4.5.77.1.2 Context

The RMI\_RTT\_UNPROT\_MAP command operates on the following context.

| Name     | Type             | Value                                                           | Before   | Description                                          |
|----------|------------------|-----------------------------------------------------------------|----------|------------------------------------------------------|
| realm    | RmmRealm         | RealmAt(rd)                                                     | false    | Realm                                                |
| size     | UInt64           | UInt(top) - UInt(base)                                          | false    | Size of target IPA range in bytes                    |
| progress | UInt64           | UInt(out_top) - UInt(base)                                      | false    | Size of IPA range which has been mapped              |
| walk     | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of RTT walk from base of the target IPA range |

ID

## B4.5.77.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                            |
|---------|------------|--------|-----------|----------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                         |
| out_top | X1         | 63:0   | Address   | Top IPA of range which has been mapped |

## B4.5.77.2 Failure conditions

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
* oaddr_type
  * pre: (flags.oaddr_type != RMI_ADDR_TYPE_SINGLE && flags.oaddr_type != RMI_ADDR_TYPE_LIST)
  * post: result.status == RMI_ERROR_INPUT
* oaddr_align
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !AddrIsAligned(oaddr.data.list_addr.addr, 8))
  * post: result.status == RMI_ERROR_INPUT
* oaddr_list_pas
  * pre: (flags.oaddr_type == RMI_ADDR_TYPE_LIST && !NonSecureAccessPermitted( oaddr.data.list_addr.addr))
  * post: result.status == RMI_ERROR_INPUT
* rtte_state
  * pre: walk.rtte.state != RTTE_UNMAPPED_NS (
  * post: result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_size
  * pre: (walk.rtte.state == RTTE_VOID && RttLevelSize(walk.level) > size) (
  * post: result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)

## B4.5.77.2.1 Failure condition ordering

The RMI\_RTT\_UNPROT\_MAP command does not have any failure condition orderings.

## B4.5.77.3 Success conditions

* state
  * post: RttTreeRangeAllState( realm, RMM_RTT_TREE_PRIMARY, base, out_top, RTTE_MAPPED_NS)
* addr_contig
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_SINGLE
  * post: RttTreeRangeAllOaddrContig( realm, RMM_RTT_TREE_PRIMARY, base, progress)
* addr_list
  * pre: flags.oaddr_type == RMI_ADDR_TYPE_LIST
  * post: RttTreeRangeAllOaddrList( realm, RMM_RTT_TREE_PRIMARY, base, oaddr.data.list_addr.addr, progress)
* memattr
  * post: RttTreeRangeAllMemAttr( realm, RMM_RTT_TREE_PRIMARY, base, out_top, flags.memattr)
* s2ap
  * post: RttTreeRangeAllS2AP( realm, RMM_RTT_TREE_PRIMARY, base, out_top, flags.s2ap)
* result
  * post: result.status == RMI_SUCCESS

## B4.5.77.4 Footprint

The RMI\_RTT\_UNPROT\_MAP command does not have any footprint.

```
RmiAddrRangeDescDecode(oaddr.data.single).base,
```