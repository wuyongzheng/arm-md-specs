## B5.4.21 RSI\_VDEV\_VALIDATE\_MAPPING command

Validate Realm device memory mappings.

See also:

- A9.6.2 Realm validation of device memory mappings
- B5.2.2.2 Range RSI operation which returns progress address

## B5.4.21.1 Interface

## B5.4.21.1.1 Input values

| Name         | Register   | Bits   | Type           | Description                                               |
|--------------|------------|--------|----------------|-----------------------------------------------------------|
| fid          | X0         | 63:0   | UInt64         | FID, value 0xC400019F                                     |
| vdev_id      | X1         | 63:0   | Bits64         | Realm device identifier                                   |
| ipa_base     | X2         | 63:0   | Address        | Base of target IPA region                                 |
| ipa_top      | X3         | 63:0   | Address        | Top of target IPA region                                  |
| pa_base      | X4         | 63:0   | Address        | Base of target PA region                                  |
| flags        | X5         | 63:0   | RsiDevMemFlags | Flags                                                     |
| lock_nonce   | X6         | 63:0   | UInt64         | Nonce generated on most recent transition to LOCKED state |
| meas_nonce   | X7         | 63:0   | UInt64         | GET_MEASUREMENT request sequence number                   |
| report_nonce | X8         | 63:0   | UInt64         | GET_INTERFACE_REPORT request sequence number              |

## B5.4.21.1.2 Context

The RSI\_VDEV\_VALIDATE\_MAPPING command operates on the following context.


| Name   | Type     | Value                           | Before   | Description   |
|--------|----------|---------------------------------|----------|---------------|
| realm  | RmmRealm | CurrentRealm()                  | false    | Current Realm |
| rec    | RmmRec   | CurrentRec()                    | false    | Current REC   |
| vdev   | RmmVdev  | VdevFromVdevId( realm, vdev_id) | false    | Realm device  |

## B5.4.21.1.3 Output values

| Name         | Register   | Bits   | Type                 | Description                                              |
|--------------|------------|--------|----------------------|----------------------------------------------------------|
| result       | X0         | 63:0   | RsiCommandReturnCode | Command result                                           |
| new_ipa_base | X1         | 63:0   | Address              | Base of IPA region which was not modified by the command |

ID

| Name     | Register   | Bits   | Type        | Description                                       |
|----------|------------|--------|-------------|---------------------------------------------------|
| response | X2         | 0:0    | RsiResponse | Whether the Host accepted or rejected the request |

The following unused bits of RSI\_VDEV\_VALIDATE\_MAPPING output values MBZ: X2[63:1].

## B5.4.21.2 Failure conditions

* da_en
  * pre: realm.feat_da != FEATURE_TRUE
  * post: result == RSI_ERROR_STATE
* vdev_id
  * pre: VdevIdIsFree(realm, vdev_id)
  * post: result == RSI_ERROR_INPUT
* state
  * pre: (vdev.vdev_state != VDEV_LOCKED && vdev.vdev_state != VDEV_STARTED)
  * post: result == RSI_ERROR_INPUT
* ipa_base_align
  * pre: !AddrIsRsiGranuleAligned(ipa_base)
  * post: result == RSI_ERROR_INPUT
* ipa_top_align
  * pre: !AddrIsRsiGranuleAligned(ipa_top)
  * post: result == RSI_ERROR_INPUT
* pa_align
  * pre: !AddrIsRsiGranuleAligned(pa_base)
  * post: result == RSI_ERROR_INPUT
* size_valid
  * pre: UInt(ipa_top) <= UInt(ipa_base)
  * post: result == RSI_ERROR_INPUT
* rgn_bound
  * pre: !AddrRangeIsProtected(ipa_base, ipa_top,
  * post: result == RSI_ERROR_INPUT
* attest_info
  * pre: !VdevAttestInfoEqual( lock_nonce, meas_nonce, report_nonce, vdev.attest_info)
  * post: result == RSI_ERROR_DEVICE

## B5.4.21.2.1 Failure condition ordering

```
[da_en] < [vdev_id]
```

<!-- image -->

## B5.4.21.3 Success conditions

* new_ipa_base
  * post: new_ipa_base == rec.dev_mem_addr
* response
  * post: response == RecDevMemResponseToRsi(rec)

## B5.4.21.4 Footprint

The RSI\_VDEV\_VALIDATE\_MAPPING command does not have any footprint.

<!-- image -->