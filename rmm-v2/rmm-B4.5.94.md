## B4.5.94 RMI\_VSMMU\_CMD\_GET command

Get a command from the VSMMU.

## B4.5.94.1 Interface

## B4.5.94.1.1 Input values

| Name      | Register   | Bits   | Type    | Description           |
|-----------|------------|--------|---------|-----------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC400020C |
| vsmmu_ptr | X1         | 63:0   | Address | PA of the VSMMU       |
| rd        | X2         | 63:0   | Address | PA of the RD          |

## B4.5.94.1.2 Context

The RMI\_VSMMU\_CMD\_GET command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| vsmmu  | RmmVsmmu | VsmmuAt(vsmmu_ptr) | false    | VSMMU         |
| realm  | RmmRealm | RealmAt(rd)        | false    | Realm         |

## B4.5.94.1.3 Output values

| Name     | Register   | Bits   | Type             | Description                                                                                   |
|----------|------------|--------|------------------|-----------------------------------------------------------------------------------------------|
| result   | X0         | 63:0   | RmiResult        | Command result                                                                                |
| flags    | X1         | 63:0   | RmiVsmmuCmdFlags | Command flags                                                                                 |
| vsid     | X2         | 63:0   | Bits64           | Virtual SMMUStream ID                                                                         |
| msi_addr | X3         | 63:0   | Address          | Address of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE. |
| msi_data | X4         | 63:0   | Bits64           | Data of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE.    |


## B4.5.94.2 Failure conditions

* feat
  * pre: Rmm().static.feat_vsmmu != FEATURE_TRUE
  * post: result.status == RMI_ERROR_NOT_SUPPORTED
* vsmmu_align
  * pre: !AddrIsRmiGranuleAligned(vsmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_bound
  * pre: !PaIsTracked(vsmmu_ptr)
  * post: result.status == RMI_ERROR_INPUT
* vsmmu_state
  * pre: GranuleAt(vsmmu_ptr).state != GRAN_VSMMU
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
* vsmmu_owner
  * pre: vsmmu.realm !=
* rd
  * post: result.status == RMI_ERROR_INPUT
* realm_state
  * pre: realm.state != REALM_NEW
  * post: result.status == RMI_ERROR_REALM

## B4.5.94.2.1 Failure condition ordering

```
[vsmmu_align, vsmmu_bound, vsmmu_state, rd_bound, rd_state] < [realm_state, vsmmu_owner] [feat] < [vsmmu_align, vsmmu_bound, vsmmu_state]
```

<!-- image -->


## B4.5.94.3 Success conditions

The RMI\_VSMMU\_CMD\_GET command does not have any success conditions.

## B4.5.94.4 Footprint

The RMI\_VSMMU\_CMD\_GET command does not have any footprint.