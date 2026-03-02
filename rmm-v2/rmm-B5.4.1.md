## B5.4.1 RSI\_ARCH\_DEV\_ACTIVATE command

Activate an architectural device.

See also:

## · A9.8.4 VSMMU validation

## B5.4.1.1 Interface

## B5.4.1.1.1 Input values

| Name     | Register   | Bits   | Type           | Description               |
|----------|------------|--------|----------------|---------------------------|
| fid      | X0         | 63:0   | UInt64         | FID, value 0xC400019B     |
| base     | X1         | 63:0   | Address        | Base of target IPA region |
| dev_type | X2         | 63:0   | RsiArchDevType | Device type               |

## B5.4.1.1.2 Context

The RSI\_ARCH\_DEV\_ACTIVATE command operates on the following context.

| Name   | Type             | Value                                     | Before   | Description     |
|--------|------------------|-------------------------------------------|----------|-----------------|
| realm  | RmmRealm         | CurrentRealm() RttWalk( realm, base,      | false    | Current Realm   |
| walk   | RmmRttWalkResult | RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | RTT walk result |
| vsmmu  | RmmVsmmu         | VsmmuAt(walk.rtte.addr)                   | false    | VSMMU           |

## B5.4.1.1.3 Output values

DRAFT

| Name   | Register   | Bits   | Type                 | Description    |
|--------|------------|--------|----------------------|----------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result |

## B5.4.1.2 Failure conditions

| ID          | Condition                                                             |
|-------------|-----------------------------------------------------------------------|
| base_align  | pre: !AddrIsRsiGranuleAligned(base) post: result == RSI_ERROR_INPUT   |
| base_bound  | pre: !AddrIsProtected(base, realm) post: result == RSI_ERROR_INPUT    |
| rtte_state  | pre: walk.rtte.state != RTTE_ARCH_DEV post: result == RSI_ERROR_INPUT |
| vsmmu_state | pre: vsmmu.state == VSMMU_ACTIVE post: result == RSI_ERROR_INPUT      |

## B5.4.1.2.1 Failure condition ordering

The RSI\_ARCH\_DEV\_ACTIVATE command does not have any failure condition orderings.

## B5.4.1.3 Success conditions

```
ID Condition ripas post: RIPAS of entire address range of the device is equal to RIPAS_DEV. state post: vsmmu.state == VSMMU_ACTIVE
```

## B5.4.1.4 Footprint

The RSI\_ARCH\_DEV\_ACTIVATE command does not have any footprint.

<!-- image -->