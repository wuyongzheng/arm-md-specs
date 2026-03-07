## B5.4.23 RSI\_VSMMU\_GET\_INFO command

Get information of a VSMMU.

See also:

- [A9.8.4 VSMMU validation](rmm-A9.8.md#a984-vsmmu-validation)

## B5.4.23.1 Interface

## B5.4.23.1.1 Input values

| Name   | Register   | Bits   | Type    | Description           |
|--------|------------|--------|---------|-----------------------|
| fid    | X0         | 63:0   | UInt64  | FID, value 0xC400019A |
| addr   | X1         | 63:0   | Address | Base IPA of the VSMMU |

## B5.4.23.1.2 Context

The RSI\_VSMMU\_GET\_INFO command operates on the following context.

| Name   | Type             | Value                                     | Before   | Description     |
|--------|------------------|-------------------------------------------|----------|-----------------|
| realm  | RmmRealm         | CurrentRealm() RttWalk( realm, addr,      | false    | Current Realm   |
| walk   | RmmRttWalkResult | RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | RTT walk result |

## B5.4.23.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description          |
|--------|------------|--------|----------------------|----------------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result       |
| top    | X1         | 63:0   | Address              | Top IPA of the VSMMU |


## B5.4.23.2 Failure conditions

* addr_align
  * pre: !AddrIsRsiGranuleAligned(addr)
  * post: result == RSI_ERROR_INPUT
* addr_bound
  * pre: !AddrIsProtected(addr, realm)
  * post: result == RSI_ERROR_INPUT
* rtte_state
  * pre: walk.rtte.state != RTTE_ARCH_DEV
  * post: result == RSI_ERROR_INPUT
* vsmmu_base
  * pre: addr != VsmmuAt(walk.rtte.addr).reg_base
  * post: result == RSI_ERROR_INPUT

## B5.4.23.2.1 Failure condition ordering

The RSI\_VSMMU\_GET\_INFO command does not have any failure condition orderings.

## B5.4.23.3 Success conditions

* vsmmu_base
  * post: top == VsmmuAt(walk.rtte.addr).reg_top

## B5.4.23.4 Footprint

The RSI\_VSMMU\_GET\_INFO command does not have any footprint.

<!-- image -->