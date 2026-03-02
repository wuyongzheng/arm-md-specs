## B4.5.93 RMI\_VSMMU\_CMD\_COMPLETE command

Complete a command from the VSMMU.

## B4.5.93.1 Interface

## B4.5.93.1.1 Input values

| Name      | Register   | Bits   | Type    | Description           |
|-----------|------------|--------|---------|-----------------------|
| fid       | X0         | 63:0   | UInt64  | FID, value 0xC400020D |
| rd        | X1         | 63:0   | Address | PA of the RD          |
| vsmmu_ptr | X2         | 63:0   | Address | PA of the VSMMU       |
| pdev_ptr  | X3         | 63:0   | Address | PA of the parent PDEV |
| vdev_ptr  | X4         | 63:0   | Address | PA of the VDEV        |

## B4.5.93.1.2 Context

The RMI\_VSMMU\_CMD\_COMPLETE command operates on the following context.

| Name   | Type     | Value              | Before   | Description   |
|--------|----------|--------------------|----------|---------------|
| realm  | RmmRealm | RealmAt(rd)        | false    | Realm         |
| vsmmu  | RmmVsmmu | VsmmuAt(vsmmu_ptr) | false    | VSMMU         |
| pdev   | RmmPdev  | PdevAt(pdev_ptr)   | false    | PDEV          |
| vdev   | RmmVdev  | VdevAt(vdev_ptr)   | false    | VDEV          |

## B4.5.93.1.3 Output values

DRAFT

| Name     | Register   | Bits   | Type             | Description                                                                                   |
|----------|------------|--------|------------------|-----------------------------------------------------------------------------------------------|
| result   | X0         | 63:0   | RmiResult        | Command result                                                                                |
| flags    | X1         | 63:0   | RmiVsmmuCmdFlags | Command flags                                                                                 |
| vsid     | X2         | 63:0   | Bits64           | Virtual SMMUStream ID                                                                         |
| msi_addr | X3         | 63:0   | Address          | Address of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE. |
| msi_data | X4         | 63:0   | Bits64           | Data of virtual MSI to be injected into the Realm. This is valid if flags.irq == RMI_TRUE.    |

## B4.5.93.2 Failure conditions

ID

## Condition

| feat            | pre: post:   | Rmm().static.feat_vsmmu != FEATURE_TRUE result.status == RMI_ERROR_NOT_SUPPORTED   |
|-----------------|--------------|------------------------------------------------------------------------------------|
| rd_align        | pre: post:   | !AddrIsRmiGranuleAligned(rd) result.status == RMI_ERROR_INPUT                      |
| rd_bound        | pre: post:   | !PaIsTracked(rd) result.status == RMI_ERROR_INPUT                                  |
| rd_state        | pre: post:   | GranuleAt(rd).state != GRAN_RD result.status == RMI_ERROR_INPUT                    |
| realm_state     | pre: post:   | realm.state != REALM_NEW result.status == RMI_ERROR_REALM                          |
| vsmmu_align     | pre: post:   | !AddrIsRmiGranuleAligned(vsmmu_ptr) result.status == RMI_ERROR_INPUT               |
| vsmmu_bound     | pre: post:   | !PaIsTracked(vsmmu_ptr) result.status == RMI_ERROR_INPUT                           |
| vsmmu_state     | pre: post:   | GranuleAt(vsmmu_ptr).state != GRAN_VSMMU result.status == RMI_ERROR_INPUT          |
| pdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(pdev_ptr) result.status == RMI_ERROR_INPUT                |
| pdev_bound      | pre: post:   | !PaIsTracked(pdev_ptr) result.status == RMI_ERROR_INPUT                            |
| pdev_gran_state | pre: post:   | DRAFT GranuleAt(pdev_ptr).state != GRAN_PDEV result.status == RMI_ERROR_INPUT      |
| vdev_align      | pre: post:   | !AddrIsRmiGranuleAligned(vdev_ptr) result.status == RMI_ERROR_INPUT                |
| vdev_bound      | pre: post:   | !PaIsTracked(vdev_ptr) result.status == RMI_ERROR_INPUT                            |
| vdev_gran_state | pre: post:   | GranuleAt(vdev_ptr).state != GRAN_VDEV result.status == RMI_ERROR_INPUT            |
| vdev_realm      | pre: post:   | vdev.realm != rd result.status == RMI_ERROR_INPUT                                  |
| vdev_vsmmu      | pre: post:   | vdev.vsmmu_addr != vsmmu_ptr result.status == RMI_ERROR_INPUT                      |
| vsmmu_realm     | pre: post:   | vsmmu.realm != rd result.status == RMI_ERROR_INPUT                                 |
| vdev_pdev       | pre: post:   | vdev.pdev != pdev_ptr result.status == RMI_ERROR_DEVICE                            |

## B4.5.93.2.1 Failure condition ordering

```
[rd_bound, rd_state] < [realm_state] [feat] < [vsmmu_align, vsmmu_bound, vsmmu_state]
```

<!-- image -->

## B4.5.93.3 Success conditions

The RMI\_VSMMU\_CMD\_COMPLETE command does not have any success conditions.

Chapter B4. Realm Management Interface B4.5. RMI commands

## B4.5.93.4 Footprint

The RMI\_VSMMU\_CMD\_COMPLETE command does not have any footprint.

DRAFT