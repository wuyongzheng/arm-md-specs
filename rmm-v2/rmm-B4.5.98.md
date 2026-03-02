## B4.5.98 RMI\_VSMMU\_EVENT\_NOTIFY command

Notify VSMMU of a pending event.

See also:

- A9.8.6 Page Request Interface events
- B4.5.97 RMI\_VSMMU\_EVENT\_COMPLETE command

## B4.5.98.1 Interface

## B4.5.98.1.1 Input values

| Name      | Register   | Bits   | Type    | Description           |
|-----------|------------|--------|---------|-----------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC40001D6 |
| psmmu_ptr | X1         | 63:0   | Address | PA of the PSMMU       |
| rd        | X2         | 63:0   | Address | PA of the RD          |
| vsmmu_ptr | X3         | 63:0   | Address | PA of the VSMMU       |
| pdev_ptr  | X4         | 63:0   | Address | PA of the PDEV        |
| vdev_ptr  | X5         | 63:0   | Address | PA of the VDEV        |

## B4.5.98.1.2 Context

The RMI\_VSMMU\_EVENT\_NOTIFY command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| psmmu  | RmmPsmmu | PsmmuAt(psmmu_ptr) | false    | PSMMU         |
| realm  | RmmRealm | RealmAt(rd)        | false    | Realm         |
| vsmmu  | RmmVsmmu | VsmmuAt(vsmmu_ptr) | false    | VSMMU         |
| pdev   | RmmPdev  | PdevAt(pdev_ptr)   | false    | PDEV          |
| vdev   | RmmVdev  | VdevAt(vdev_ptr)   | false    | VDEV          |


## B4.5.98.1.3 Output values

| Name     | Register   | Bits   | Type               | Description                                                                                   |
|----------|------------|--------|--------------------|-----------------------------------------------------------------------------------------------|
| result   | X0         | 63:0   | RmiResult          | Command result                                                                                |
| flags    | X1         | 63:0   | RmiVsmmuEventFlags | Action required by Host                                                                       |
| msi_addr | X2         | 63:0   | Address            | Address of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE. |
| msi_data | X3         | 63:0   | Bits64             | Data of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE.    |

| Name     | Register   | Bits   | Type    | Description                                                                                              |
|----------|------------|--------|---------|----------------------------------------------------------------------------------------------------------|
| fipa     | X4         | 63:0   | Address | Faulting IPA. This is valid if flags.abort == RMI_TRUE.                                                  |
| syndrome | X5         | 63:0   | Bits64  | RnW[0], S2[1] and Class[3:2] attributes, as specified by SMMU. This is valid if flags.abort == RMI_TRUE. |

## B4.5.98.2 Failure conditions

## ID Condition

| feat            | pre: post:   | Rmm().static.feat_vsmmu != FEATURE_TRUE result.status == RMI_ERROR_NOT_SUPPORTED   |
|-----------------|--------------|------------------------------------------------------------------------------------|
| psmmu_valid     | pre: post:   | !PsmmuAddrIsValid(psmmu_ptr) result.status == RMI_ERROR_INPUT                      |
| rd_align        | pre: post:   | !AddrIsRmiGranuleAligned(rd) result.status == RMI_ERROR_INPUT                      |
| rd_bound        | pre: post:   | !PaIsTracked(rd) result.status == RMI_ERROR_INPUT                                  |
| rd_state        | pre: post:    GranuleAt(rd).state != GRAN_RD result.status == RMI_ERROR_INPUT              |
| realm_state     | pre: post:   | realm.state != REALM_NEW result.status == RMI_ERROR_REALM                          |
| vsmmu_align     | pre: post:   | !AddrIsRmiGranuleAligned(vsmmu_ptr) result.status == RMI_ERROR_INPUT               |
| vsmmu_bound     | pre: post:   | !PaIsTracked(vsmmu_ptr) result.status == RMI_ERROR_INPUT                           |
| vsmmu_state     | pre: post:   | GranuleAt(vsmmu_ptr).state != GRAN_VSMMU result.status == RMI_ERROR_INPUT          |
| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT                |
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                            |
| pdev_gran_state | pre: post:   | GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT            |
| vdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(vdev_ptr) result.status == RMI_ERROR_INPUT                |
| vdev_bound      | pre: post:   | !PaIsTracked(vdev_ptr) result.status == RMI_ERROR_INPUT                            |
| vdev_gran_state | pre: post:   | GranuleAt(vdev_ptr).state != GRAN_VDEV result.status == RMI_ERROR_INPUT            |
| vdev_realm      | pre: post:   | vdev.realm != rd result.status == RMI_ERROR_INPUT                                  |
| vdev_pdev       | pre: post:   | vdev.pdev != pdev_ptr result.status == RMI_ERROR_DEVICE                            |

ID

## B4.5.98.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [feat] < [vsmmu_align, vsmmu_bound,
```

```
vsmmu_state]
```

<!-- image -->

## B4.5.98.3 Success conditions

## Condition

```
gerr_irq pre: VSMMU has asserted GERROR interrupt. post: (flags.irq == RMI_TRUE && msi_addr == vsmmu.msi_config.gerr_addr && msi_data == vsmmu.msi_config.gerr_data) priq_irq pre: VSMMU has asserted PRIQ interrupt. post: (flags.irq == RMI_TRUE && msi_addr == vsmmu.msi_config.priq_addr && msi_data == vsmmu.msi_config.priq_data)
```

## B4.5.98.4 Footprint

The RMI\_VSMMU\_EVENT\_NOTIFY command does not have any footprint.

