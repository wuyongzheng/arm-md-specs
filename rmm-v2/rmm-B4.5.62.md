## B4.5.62 RMI\_RTT\_AUX\_UNPROT\_MAP command

Propagate mappings within a contiguous range of Unprotected IPA space from the primary RTT tree to an auxiliary RTT tree.

The RMI\_RTT\_AUX\_UNPROT\_MAP command may initiate a Stateful RMI Operation.

## See also:

- A5.3.15 Create mappings within Unprotected IPA space in auxiliary RTT tree
- A10.3.1 Auxiliary RTT
- B4.5.63 RMI\_RTT\_AUX\_UNPROT\_UNMAP command

## B4.5.62.1 Interface

## B4.5.62.1.1 Input values

| Name   | Register   | Bits   | Type              | Description                       |
|--------|------------|--------|-------------------|-----------------------------------|
| fid    | X0         | 63:0   | UInt64            | FID, value 0xC40001FF             |
| rd     | X1         | 63:0   | Address           | PA of the RD for the target Realm |
| base   | X2         | 63:0   | Address           | Base of the target IPA range      |
| top    | X3         | 63:0   | Address           | Top of the target IPA range       |
| flags  | X4         | 63:0   | RmiRttAuxMapFlags | Flags                             |

## B4.5.62.1.2 Context

The RMI\_RTT\_AUX\_UNPROT\_MAP command operates on the following context.

| Name     | Type             | Value                                                           | Before   | Description                                                    |
|----------|------------------|-----------------------------------------------------------------|----------|----------------------------------------------------------------|
| realm    | RmmRealm         | RealmAt(rd)                                                     | false    | Realm                                                          |
| size     | UInt64           | UInt(top) - UInt(base)                                          | false    | Size of target IPA range in bytes                              |
| walk_pri | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of primary RTT walk from base of the target IPA range   |
| walk_aux | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, flags.tree_index)     | false    | Result of auxiliary RTT walk from base of the target IPA range |


## B4.5.62.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                            |
|---------|------------|--------|-----------|----------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                         |
| out_top | X1         | 63:0   | Address   | Top IPA of range which has been mapped |

ID

## B4.5.62.2 Failure conditions

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
  * pre: !AddrIsAligned( base, RttLevelSize(walk_pri.level))
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
* index_bound
  * pre: (realm.rtt_tree_per_plane == FEATURE_FALSE || flags.tree_index == RMM_RTT_TREE_PRIMARY || flags.tree_index > realm.num_aux_planes)
  * post: result.status == RMI_ERROR_INPUT
* pri_state
  * pre: walk_pri.rtte.state != RTTE_MAPPED_NS
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk_pri.level)
* aux_size
  * pre: (walk_aux.rtte.state == RTTE_VOID && RttLevelSize(walk_aux.level) > size)
  * post: (result.status == RMI_ERROR_RTT_AUX && result.data.level.level == walk_aux.level)

## B4.5.62.2.1 Failure condition ordering

The RMI\_RTT\_AUX\_UNPROT\_MAP command does not have any failure condition orderings.

## B4.5.62.3 Success conditions

* result
  * post: result.status == RMI_SUCCESS
* state
  * post: RttTreeRangeAllState( realm, flags.tree_index, base, out_top, RTTE_MAPPED_NS)
* addr
  * post: RttTreeRangeAllOaddrEqual( realm, RMM_RTT_TREE_PRIMARY, flags.tree_index, base, out_top)
* memattr
  * post: RttTreeRangeAllMemAttrEqual( realm, RMM_RTT_TREE_PRIMARY, flags.tree_index, base, out_top)
* shareability
  * post: RttTreeRangeAllShareabilityEqual( realm, RMM_RTT_TREE_PRIMARY, flags.tree_index, base, out_top)

## B4.5.62.4 Footprint

The RMI\_RTT\_AUX\_UNPROT\_MAP command does not have any footprint.

<!-- image -->