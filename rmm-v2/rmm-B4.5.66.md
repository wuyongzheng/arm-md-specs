## B4.5.66 RMI\_RTT\_DATA\_MAP\_INIT command

Create a mapping from Protected IPA space to conventional memory, copying contents from a Non-secure Granule provided by the caller.

The RMI\_RTT\_DATA\_MAP\_INIT command may initiate a Stateful RMI Operation.

## See also:

- [A5.3.4 Mapping initial Realm image in Protected IPA space](rmm-A5.3.md#a534-mapping-initial-realm-image-in-protected-ipa-space)
- [B4.5.67 RMI\_RTT\_DATA\_UNMAP command](rmm-B4.5.67.md)
- [D1.2.3 Initialize memory of New Realm flow](rmm-D1.2.md#d123-initialize-memory-of-new-realm-flow)

## B4.5.66.1 Interface

## B4.5.66.1.1 Input values

| Name   | Register   | Bits   | Type         | Description                                                 |
|--------|------------|--------|--------------|-------------------------------------------------------------|
| fid    | X0         | 63:0   | UInt64       | FID, value 0xC4000153                                       |
| rd     | X1         | 63:0   | Address      | PA of the RD for the target Realm                           |
| data   | X2         | 63:0   | Address      | PA of the target Data                                       |
| ipa    | X3         | 63:0   | Address      | IPA at which the Granule will be mapped in the target Realm |
| src    | X4         | 63:0   | Address      | PA of the source Granule                                    |
| flags  | X5         | 63:0   | RmiDataFlags | Flags                                                       |

## B4.5.66.1.2 Context

The RMI\_RTT\_DATA\_MAP\_INIT command operates on the following context.

| Name      | Type             | Value                                                          | Before   | Description     |
|-----------|------------------|----------------------------------------------------------------|----------|-----------------|
| realm_pre | RmmRealm         | RealmAt(rd)                                                    | true     | Realm           |
| realm     | RmmRealm         | RealmAt(rd)                                                    | false    | Realm           |
| walk      | RmmRttWalkResult | RttWalk( realm, ipa, RMM_RTT_PAGE_LEVEL, RMM_RTT_TREE_PRIMARY) | false    | RTT walk result |
| entry_idx | UInt64           | RttEntryIndex( ipa, walk.level)                                | false    | RTTE index      |


## B4.5.66.1.3 Output values

| Name   | Register   | Bits   | Type      | Description    |
|--------|------------|--------|-----------|----------------|
| result | X0         | 63:0   | RmiResult | Command result |

ID

## B4.5.66.2 Failure conditions

* src_align
  * pre: !AddrIsRmiGranuleAligned(src)
  * post: result.status == RMI_ERROR_INPUT
* src_pas
  * pre: !NonSecureAccessPermitted(src)
  * post: result.status == RMI_ERROR_INPUT
* data_align
  * pre: !AddrIsRmiGranuleAligned(data)
  * post: result.status == RMI_ERROR_INPUT
* data_bound
  * pre: !PaIsDelegableConventionalFine(data)
  * post: result.status == RMI_ERROR_INPUT
* data_state
  * pre: GranuleAt(data).state != GRAN_DELEGATED
  * post: result.status == RMI_ERROR_INPUT
* data_bound2
  * pre: ((realm.feat_lpa2 == FEATURE_FALSE) && (UInt(data) >= 2^48))
  * post: result.status == RMI_ERROR_INPUT
* rd_align
  * pre: !AddrIsRmiGranuleAligned(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_bound
  * pre: !PaIsTracked(rd)
  * post: result.status == RMI_ERROR_INPUT
* rd_state
  * pre: GranuleAt(rd).state != GRAN_RD
  * post: result.status == RMI_ERROR_INPUT
* ipa_align
  * pre: !AddrIsRmiGranuleAligned(ipa)
  * post: result.status == RMI_ERROR_INPUT
* ipa_bound
  * pre: !AddrIsProtected(ipa, realm_pre)
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm_pre.state != REALM_NEW
  * post: result.status == RMI_ERROR_REALM
* rtt_walk
  * pre: walk.level < RMM_RTT_PAGE_LEVEL
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* rtte_state
  * pre: walk.rtte.state != RTTE_VOID
  * post: (result.status == RMI_ERROR_RTT && result.data.level.level == walk.level)
* dpt
  * pre: Missing failure conditions: -ATS is enabled for the Realm and either: -Any ATS-capable PSMMU has not been -L1DPT is
* missing
  * post: result.status == RMI_ERROR_INPUT

## B4.5.66.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [rd_bound, rd_state] < [rtt_walk, [ipa_bound] < [rtt_walk, rtte_state]
```

```
rtte_state]
```

```
activated
```

## ID

<!-- image -->

## B4.5.66.3 Success conditions

* data_state
  * post: GranuleAt(data).state == GRAN_DATA
* data_content
  * post: Contents of target Granule are copied from source Granule.
* rtte_ripas
  * post: walk.rtte.ripas == RIPAS_RAM
* rtte_addr
  * post: walk.rtte.addr == data
* rtte_memattr
  * post: walk.rtte.attr_prot == MEMATTR_CACHEABLE
* rtte_sh
  * post: walk.rtte.sh == SHAREABILITY_INNER
* rim
  * post: realm.rim == RimExtendData( realm_pre, ipa, data, flags)
* result
  * post: result.status == RMI_SUCCESS
* rtte_state
  * post: walk.rtte.state == RTTE_DATA B4.5.66.4 RMI_RTT_DATA_MAP_INIT extension of RIM On successful execution of RMI_RTT_DATA_MAP_INIT, the new RIM value of the target Realm is calculated by the RMM as follows: 1. If flags.measure == RMI_MEASURE_CONTENT then using the RHA of the target Realm, compute the hash of the contents of the DATA Granule. 2. Allocate an RmmMeasurementDescriptorData data structure. 3. Populate the measurement descriptor: - Set the desc_type field to the descriptor type. - Set the len field to the descriptor length. - Set the rim field to the current RIM value of the target Realm. - Set the ipa field to the IPA at which the DATA Granule is mapped in the target Realm. - Set the flags field to the flags provided by the Host. - If flags.measure == RMI_MEASURE_CONTENT then set the content field to the hash of the contents of the DATA Granule. Otherwise, set the content field to zero. 4. Using the RHA of the target Realm, compute the hash of the measurement descriptor. Set the RIM of the target Realm to this value, zero filling upper bytes if the RHA output is smaller than the size of the RIM.

## See also:

- [A7.1.1 Realm Initial Measurement](rmm-A7.1.md#a711-realm-initial-measurement)
- [B3.111 RimExtendData function](rmm-B3.md#b3111-rimextenddata-function)
- [C2.27 RmmMeasurementDescriptorData type](rmm-C2.md#c227-rmmmeasurementdescriptordata-type)

## B4.5.66.5 Footprint

| ID         | Value                                       |
|------------|---------------------------------------------|
| data_state | GranuleAt(data).state                       |
| rim        | realm.rim                                   |
| rtte       | RttEntryAt(RttAt(walk.rtt_addr), entry_idx) |

<!-- image -->