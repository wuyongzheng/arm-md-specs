## B4.5.55 RMI\_RTT\_ARCH\_DEV\_MAP command

Create mappings to an architectural device within a target Protected IPA range.

See also:

- A5.3.9 Create mappings from Protected IPA space to an architectural device
- A9.8 Virtual SMMU
- B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command

## B4.5.55.1 Interface

## B4.5.55.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                       |
|---------|------------|--------|---------|-----------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC40001F9             |
| rd      | X1         | 63:0   | Address | PA of the RD for the target Realm |
| dev_ptr | X2         | 63:0   | Address | PA of the device                  |
| base    | X3         | 63:0   | Address | Base of the target IPA range      |
| top     | X4         | 63:0   | Address | Top of the target IPA range       |

## B4.5.55.1.2 Context

The RMI\_RTT\_ARCH\_DEV\_MAP command operates on the following context.

| Name   | Type             | Value                                                           | Before   | Description                                          |
|--------|------------------|-----------------------------------------------------------------|----------|------------------------------------------------------|
| rmm    | RmmGlobal        | Rmm()                                                           | false    | RMMglobal state                                      |
| realm  | RmmRealm         | RealmAt(rd)                                                     | false    | Realm                                                |
| vsmmu  | RmmVsmmu         | VsmmuAt(dev_ptr)                                                | false    | VSMMU                                                |
| size   | UInt64           | UInt(top) - UInt(base)                                          | false    | Size of target IPA range in bytes                    |
| walk   | RmmRttWalkResult | RttWalk( realm, base, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | Result of RTT walk from base of the target IPA range |

DRAFT

## B4.5.55.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                            |
|---------|------------|--------|-----------|----------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                         |
| out_top | X1         | 63:0   | Address   | Top IPA of range which has been mapped |

## B4.5.55.2 Failure conditions

## ID

## Condition

```
DRAFT feat pre: Rmm().static.feat_vsmmu != FEATURE_TRUE post: result.status == RMI_ERROR_NOT_SUPPORTED rd_align pre: !AddrIsRmiGranuleAligned(rd) post: result.status == RMI_ERROR_INPUT rd_bound pre: !PaIsTracked(rd) post: result.status == RMI_ERROR_INPUT rd_state pre: GranuleAt(rd).state != GRAN_RD post: result.status == RMI_ERROR_INPUT dev_align pre: !AddrIsRmiGranuleAligned(dev_ptr) post: result.status == RMI_ERROR_INPUT dev_bound pre: !PaIsTracked(dev_ptr) post: result.status == RMI_ERROR_INPUT dev_state pre: GranuleAt(dev_ptr).state != GRAN_VSMMU post: result.status == RMI_ERROR_INPUT dev_realm pre: vsmmu.realm != rd post: result.status == RMI_ERROR_INPUT base_align pre: !AddrIsRmiGranuleAligned(base) post: result.status == RMI_ERROR_INPUT top_align pre: !AddrIsRmiGranuleAligned(top) post: result.status == RMI_ERROR_INPUT size_valid pre: UInt(top) <= UInt(base) post: result.status == RMI_ERROR_INPUT ipa_bound pre: !AddrRangeIsProtected(base, top, realm) post: result.status == RMI_ERROR_INPUT rtte_state pre: walk.rtte.state != RTTE_VOID post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) rtte_size pre: (walk.rtte.state == RTTE_VOID && RttLevelSize(walk.level) > size) post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level) rtte_ripas pre: walk.rtte.ripas != RIPAS_EMPTY post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
```

## B4.5.55.2.1 Failure condition ordering

The RMI\_RTT\_ARCH\_DEV\_MAP command does not have any failure condition orderings.

## B4.5.55.3 Success conditions

## Condition

## ID

```
state post: RttTreeRangeAllState( realm, RMM_RTT_TREE_PRIMARY, base, out_top, RTTE_ARCH_DEV) addr post: RttTreeRangeAllOaddr( realm, RMM_RTT_TREE_PRIMARY, base, top, dev_ptr)
```

| ID     | Condition                          |
|--------|------------------------------------|
| result | post: result.status == RMI_SUCCESS |

## B4.5.55.4 Footprint

The RMI\_RTT\_ARCH\_DEV\_MAP command does not have any footprint.

<!-- image -->