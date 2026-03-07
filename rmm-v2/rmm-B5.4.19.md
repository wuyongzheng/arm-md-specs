## B5.4.19 RSI\_VDEV\_GET\_INFO command

Get information for a device.

Device configuration information, including digests of attestation evidence for the device are written to an RsiVdevInfo structure, at an address specified by the caller. Digests are calculated using the PDEV Hash Algorithm.

## See also:

- A5.2.4 RSI command access to a Protected IPA
- A9.6.1 Realm retrieval of device attestation evidence
- B5.4.16 RSI\_REALM\_CONFIG command
- B5.5.28 RsiVdevInfo type

## B5.4.19.1 Interface

## B5.4.19.1.1 Input values

| Name    | Register   | Bits   | Type    | Description                                         |
|---------|------------|--------|---------|-----------------------------------------------------|
| fid     | X0         | 63:0   | UInt64  | FID, value 0xC400019D                               |
| vdev_id | X1         | 63:0   | Bits64  | Realm device identifier                             |
| addr    | X2         | 63:0   | Address | IPA to which the configuration data will be written |

## B5.4.19.1.2 Context

The RSI\_VDEV\_GET\_INFO command operates on the following context.

| Name   | Type             | Value                           | Before   | Description          |
|--------|------------------|---------------------------------|----------|----------------------|
| realm  | RmmRealm         | CurrentRealm()                  | false    | Current Realm        |
| vdev   | RmmVdev          | VdevFromVdevId( realm, vdev_id) | false    | Realm device         |
| pdev   | RmmPdev          | PdevAt(vdev.pdev)               | false    | Physical device      |
| cfg    | RsiVdevInfo      | RsiVdevInfoAt(addr)             | false    | Device configuration |
| walk   | RmmRttWalkResult | RttWalk( realm, addr,           | false    | RTT walk result      |


## B5.4.19.1.3 Output values

| Name   | Register   | Bits   | Type                 | Description    |
|--------|------------|--------|----------------------|----------------|
| result | X0         | 63:0   | RsiCommandReturnCode | Command result |

## ID

## B5.4.19.2 Failure conditions

* da_en
  * pre: realm.feat_da != FEATURE_TRUE
  * post: result == RSI_ERROR_STATE
* vdev_id
  * pre: VdevIdIsFree(realm, vdev_id)
  * post: result == RSI_ERROR_INPUT
* addr_align
  * pre: !AddrIsAligned(addr, 512)
  * post: result == RSI_ERROR_INPUT
* addr_bound
  * pre: !AddrIsProtected(addr, realm)
  * post: result == RSI_ERROR_INPUT
* addr_empty
  * pre: walk.rtte.ripas == RIPAS_EMPTY
  * post: result == RSI_ERROR_INPUT

## B5.4.19.2.1 Failure condition ordering

```
[da_en] < [vdev_id, addr_align, addr_bound]
```


<!-- image -->

## B5.4.19.3 Success conditions

* report_digest
  * post: cfg.report_digest == vdev.report_digest
* state
  * post: cfg.state == VdevStateToRsi(vdev.vdev_state)
* hash_algo
  * post: Equal(cfg.hash_algo, pdev.hash_algo)
* p2p_enabled
  * post: Equal(cfg.flags.p2p_enabled, pdev.p2p_enabled)
* p2p_bound
  * post: Equal(cfg.flags.p2p_bound, vdev.p2p_bound)
* attest_info
  * post: VdevAttestInfoEqual( cfg.lock_nonce, cfg.meas_nonce, cfg.report_nonce, vdev.attest_info)
* negotiation_data_digest
  * post: cfg.negotiation_data_digest == pdev.negotiation_data_digest
* meas_digest
  * post: cfg.meas_digest == vdev.meas_digest

## B5.4.19.4 Footprint

The RSI\_VDEV\_GET\_INFO command does not have any footprint.

<!-- image -->