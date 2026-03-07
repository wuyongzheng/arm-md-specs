## B4.5.56 RMI\_RTT\_ARCH\_DEV\_UNMAP command

Removes mappings to an architectural device within a target Protected IPA range.

See also:

- [A5.3.10 Remove mappings from Protected IPA space to an architectural device](rmm-A5.3.md#a5310-remove-mappings-from-protected-ipa-space-to-an-architectural-device)
- [A9.8 Virtual SMMU](rmm-A9.8.md)
- [B4.5.55 RMI\_RTT\_ARCH\_DEV\_MAP command](rmm-B4.5.55.md)

## B4.5.56.1 Interface

## B4.5.56.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                       |
|---------|------------|--------|---------|-----------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC40001FA             |
| rd      | X1         | 63:0   | Address | PA of the RD for the target Realm |
| dev_ptr | X2         | 63:0   | Address | PA of the device                  |
| base    | X3         | 63:0   | Address | Base of the target IPA range      |
| top     | X4         | 63:0   | Address | Top of the target IPA range       |

## B4.5.56.1.2 Context

The RMI\_RTT\_ARCH\_DEV\_UNMAP command operates on the following context.

| Name                                | Type                                                         | Value                                                                                        | Before                             | Description                                                                                                              |
|-------------------------------------|--------------------------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------|--------------------------------------------------------------------------------------------------------------------------|
| rmm realm_pre realm vsmmu size walk | RmmGlobal RmmRealm RmmRealm RmmVsmmu UInt64 RmmRttWalkResult | Rmm() RealmAt(rd) RealmAt(rd) VsmmuAt(dev_ptr) UInt(top) RttWalk( realm, RMM_RTT_PAGE_LEVEL, | false true false false false false | RMMglobal state Realm Realm VSMMU Size of target IPA range in bytes Result of RTT walk from base of the target IPA range |


## B4.5.56.1.3 Output values

| Name    | Register   | Bits   | Type      | Description                            |
|---------|------------|--------|-----------|----------------------------------------|
| result  | X0         | 63:0   | RmiResult | Command result                         |
| out_top | X1         | 63:0   | Address   | Top IPA of range which has been mapped |

ID

## B4.5.56.2 Failure conditions

* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* dev_align
  * pre: !AddrIsRmiGranuleAligned(dev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* dev_bound
  * pre: !PaIsTracked(dev_ptr)
  * post: result.status == RMI_ERROR_INPUT
* dev_state
  * pre: GranuleAt(dev_ptr).state != GRAN_VSMMU
  * post: result.status == RMI_ERROR_INPUT
* dev_realm
  * pre: vsmmu.realm !=
* rd
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
* rtte_state
  * pre: walk.rtte.state != RTTE_ARCH_DEV
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_addr
  * pre: (walk.rtte.state == RTTE_NARCH_DEV && walk.rtte.addr != dev_ptr)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_size
  * pre: (walk.rtte.state == RTTE_NARCH_DEV && RttLevelSize(walk.level) > size)
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)

## B4.5.56.2.1 Failure condition ordering

The RMI\_RTT\_ARCH\_DEV\_UNMAP command does not have any failure condition orderings.

## B4.5.56.3 Success conditions

* state
  * post: RttTreeRangeAllState( realm, base, out_top, RTTE_VOID)
* ripas
  * post: RealmIpaRangeAllRipasIf( realm_pre, realm, base, out_top, RIPAS_DEV,
* dev_state
  * post: vsmmu.state == VSMMU_INACTIVE
* result
  * post: result.status == RMI_SUCCESS

## B4.5.56.4 Footprint

The RMI\_RTT\_ARCH\_DEV\_UNMAP command does not have any footprint.

<!-- image -->