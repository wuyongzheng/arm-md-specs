## B5.5 RSI types

This section defines types which are used in the RSI interface.

## B5.5.1 RsiArchDevType type

The RsiArchDevType enumeration represents architectural device type.

The RsiArchDevType enumeration is a concrete type.

The width of the RsiArchDevType enumeration is 64 bits.

The values of the RsiArchDevType enumeration are shown in the following table.

|   Encoding | Name                | Description   |
|------------|---------------------|---------------|
|          0 | RSI_ARCH_DEV_SMMUV3 | SMMUv3        |

Unused encodings for the RsiArchDevType enumeration are reserved for use by future versions of this specification.

## B5.5.2 RsiBoolean type

The RsiBoolean enumeration represents a boolean value.

The RsiBoolean enumeration is a concrete type.

The width of the RsiBoolean enumeration is 1 bits.

The values of the RsiBoolean enumeration are shown in the following table.

|   Encoding | Name      | Description   |
|------------|-----------|---------------|
|          0 | RSI_FALSE | False         |
|          1 | RSI_TRUE  | True          |


The RsiBoolean enumeration is used in the following types:

- RsiSysregAddress

## B5.5.3 RsiCommandReturnCode type

The RsiCommandReturnCode enumeration represents a return code from an RSI command.

The RsiCommandReturnCode enumeration is a concrete type.

The width of the RsiCommandReturnCode enumeration is 64 bits.

See also:

- Chapter B1 Commands

The values of the RsiCommandReturnCode enumeration are shown in the following table.

|   Encoding | Name        | Description                    |
|------------|-------------|--------------------------------|
|          0 | RSI_SUCCESS | Command completed successfully |

|   Encoding | Name              | Description                                                                                    |
|------------|-------------------|------------------------------------------------------------------------------------------------|
|          1 | RSI_ERROR_INPUT   | The value of a command input value caused the command to fail                                  |
|          2 | RSI_ERROR_STATE   | The state of the current Realm or current REC does not match the state expected by the command |
|          3 | RSI_INCOMPLETE    | The operation requested by the command is not complete                                         |
|          4 | RSI_ERROR_UNKNOWN | The operation requested by the command failed for an unknown reason                            |
|          5 | RSI_ERROR_DEVICE  | The state of a Realm device does not match the state expected by the command                   |

Unused encodings for the RsiCommandReturnCode enumeration are reserved for use by future versions of this specification.

## B5.5.4 RsiDevMemCoherent type

The RsiDevMemCoherent enumeration represents whether a device memory location is within the system coherent memory space.

The RsiDevMemCoherent enumeration is a concrete type.

The width of the RsiDevMemCoherent enumeration is 1 bits.

The values of the RsiDevMemCoherent enumeration are shown in the following table.

|   Encoding | Name                     | Description                                                             |
|------------|--------------------------|-------------------------------------------------------------------------|
|          0 | RSI_DEV_MEM_NON_COHERENT | A device memory location is not within the system coherent memory space |
|          1 | RSI_DEV_MEM_COHERENT     | A device memory location is within the system coherent memory space     |


The RsiDevMemCoherent enumeration is used in the following types:

- RsiDevMemFlags

## B5.5.5 RsiDevMemFlags type

The RsiDevMemFlags fieldset contains flags which describe properties of a device memory mapping.

The RsiDevMemFlags fieldset is a concrete type.

The width of the RsiDevMemFlags fieldset is 64 bits.

The fields of the RsiDevMemFlags fieldset are shown in the following diagram.

The fields of the RsiDevMemFlags fieldset are shown in the following table.

| Name   | Bits   | Description                                                                                         | Value             |
|--------|--------|-----------------------------------------------------------------------------------------------------|-------------------|
| coh    | 0      | Whether the output address of the device memory mapping is within the system coherent memory space. | RsiDevMemCoherent |
| order  | 1      | Ordering properties of the device memory location.                                                  | RsiDevMemOrdering |
|        | 63:2   | Reserved                                                                                            | SBZ               |

## B5.5.6 RsiDevMemOrdering type

The RsiDevMemOrdering enumeration represents ordering properties of a device memory location.

The RsiDevMemOrdering enumeration is a concrete type.

The width of the RsiDevMemOrdering enumeration is 1 bits.


The values of the RsiDevMemOrdering enumeration are shown in the following table.

|   Encoding | Name                          | Description                                                         |
|------------|-------------------------------|---------------------------------------------------------------------|
|          0 | RSI_DEV_MEM_NOT_LIMITED_ORDER | A device memory location is not within a Limited Order Region (LOR) |
|          1 | RSI_DEV_MEM_LIMITED_ORDER     | A device memory location is within a Limited Order Region (LOR)     |

The RsiDevMemOrdering enumeration is used in the following types:

- RsiDevMemFlags

## B5.5.7 RsiFeature type

The RsiFeature enumeration represents whether a feature is enabled.

The RsiFeature enumeration is a concrete type.

The width of the RsiFeature enumeration is 1 bits.

The values of the RsiFeature enumeration are shown in the following table.

|   Encoding | Name              | Description             |
|------------|-------------------|-------------------------|
|          0 | RSI_FEATURE_FALSE | Feature is not enabled. |
|          1 | RSI_FEATURE_TRUE  | Feature is enabled.     |

The RsiFeature enumeration is used in the following types:

- RsiVdevDmaFlags
- RsiFeatureRegister0
- RsiVdevFlags

## B5.5.8 RsiFeatureRegister0 type

The RsiFeatureRegister0 fieldset contains RSI feature register 0.

The RsiFeatureRegister0 fieldset is a concrete type.

The width of the RsiFeatureRegister0 fieldset is 64 bits.

The fields of the RsiFeatureRegister0 fieldset are shown in the following diagram.


The fields of the RsiFeatureRegister0 fieldset are shown in the following table.

| Name   | Bits   | Description                                                                        | Value      |
|--------|--------|------------------------------------------------------------------------------------|------------|
| DA     | 0      | Whether Realm device assignment is supported                                       | RsiFeature |
| MRO    | 1      | Whether 'mostly read-only' permissions are supported                               | RsiFeature |
| ATS    | 2      | Whether Address Translation Service is supported for devices assigned to the Realm | RsiFeature |
|        | 63:3   | Reserved                                                                           | MBZ        |

## B5.5.9 RsiGicOwner type

The RsiGicOwner enumeration represents which Plane is GIC owner.

The RsiGicOwner enumeration is a concrete type.

The width of the RsiGicOwner enumeration is 1 bits.

The values of the RsiGicOwner enumeration are shown in the following table.

|   Encoding | Name            | Description           |
|------------|-----------------|-----------------------|
|          0 | RSI_GIC_OWNER_0 | Plane 0 is GIC owner. |
|          1 | RSI_GIC_OWNER_N | Plane N is GIC owner. |

The RsiGicOwner enumeration is used in the following types:

- RsiPlaneEnterFlags

## B5.5.10 RsiHashAlgorithm type

The RsiHashAlgorithm enumeration represents hash algorithm.

The RsiHashAlgorithm enumeration is a concrete type.

The width of the RsiHashAlgorithm enumeration is 8 bits.

See also:

- [B5.4.16 RSI\_REALM\_CONFIG command](rmm-B5.4.16.md)

The values of the RsiHashAlgorithm enumeration are shown in the following table.

|   Encoding | Name             | Description                                |
|------------|------------------|--------------------------------------------|
|          0 | RSI_HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [25]) |
|          1 | RSI_HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [25]) |
|          2 | RSI_HASH_SHA_384 | SHA-384 ( Secure Hash Standard (SHS) [25]) |


Unused encodings for the RsiHashAlgorithm enumeration are reserved for use by future versions of this specification.

The RsiHashAlgorithm enumeration is used in the following types:

- RsiVdevInfo
- RsiRealmConfig

## B5.5.11 RsiHostCall type

The RsiHostCall structure contains data structure used to pass Host call arguments and return values.

The RsiHostCall structure is a concrete type.

The width of the RsiHostCall structure is 256 ( 0x100 ) bytes.

See also:

- [A4.5 Host call](rmm-A4.4.md#a45-host-call)
- [B5.4.5 RSI\_HOST\_CALL command](rmm-B5.4.5.md)

The members of the RsiHostCall structure are shown in the following table.

| Name     | Byte offset   | Type   | Description     |
|----------|---------------|--------|-----------------|
| imm      | 0x0           | UInt16 | Immediate value |
| gprs[31] | 0x8           | Bits64 | Registers       |

Unused bits of the RsiHostCall structure SBZ.

## B5.5.12 RsiInterfaceVersion type

The RsiInterfaceVersion fieldset contains an RSI interface version.

The RsiInterfaceVersion fieldset is a concrete type.

The width of the RsiInterfaceVersion fieldset is 64 bits.

See also:

- [B5.1 RSI version](rmm-B5.1.md)
- [B5.4.22 RSI\_VERSION command](rmm-B5.4.22.md)

The fields of the RsiInterfaceVersion fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RsiInterfaceVersion fieldset are shown in the following table.

| Name   | Bits   | Description                                                            | Value   |
|--------|--------|------------------------------------------------------------------------|---------|
| minor  | 15:0   | Interface minor version number (the value y in interface version x.y ) | UInt16  |
| major  | 30:16  | Interface major version number (the value x in interface version x.y ) | UInt15  |
|        | 63:31  | Reserved                                                               | SBZ     |

## B5.5.13 RsiPlaneEnter type

The RsiPlaneEnter structure contains data passed from P0 to the RMM on Plane entry.

The RsiPlaneEnter structure is a concrete type.

The width of the RsiPlaneEnter structure is 2048 ( 0x800 ) bytes.

The members of the RsiPlaneEnter structure are shown in the following table.

| Name   | Byte offset   | Type               | Description     |
|--------|---------------|--------------------|-----------------|
| flags  | 0x0           | RsiPlaneEnterFlags | Flags           |
| pc     | 0x8           | Bits64             | Program counter |
| pstate | 0x10          | Bits64             | PSTATE          |


| Name          | Byte offset   | Type   | Description                             |
|---------------|---------------|--------|-----------------------------------------|
| gprs[31]      | 0x100         | Bits64 | Registers                               |
| gicv3_hcr     | 0x200         | Bits64 | GICv3 Hypervisor Control Register value |
| gicv3_lrs[16] | 0x208         | Bits64 | GICv3 List Register values              |
| elr_el1       | 0x400         | Bits64 | ELR_EL1 value                           |

Unused bits of the RsiPlaneEnter structure SBZ.

The RsiPlaneEnter structure is used in the following types:

- RsiPlaneRun

## B5.5.14 RsiPlaneEnterFlags type

The RsiPlaneEnterFlags fieldset contains flags provided by P0 during Plane entry.

The RsiPlaneEnterFlags fieldset is a concrete type.

The width of the RsiPlaneEnterFlags fieldset is 64 bits.

The fields of the RsiPlaneEnterFlags fieldset are shown in the following diagram.

<!-- image -->


The fields of the RsiPlaneEnterFlags fieldset are shown in the following table.

| Name      |   Bits | Description                                                                                                                                                                  | Value       |
|-----------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------|
| trap_wfi  |      0 | Whether to trap WFI execution by the Plane.                                                                                                                                  | RsiTrap     |
| trap_wfe  |      1 | Whether to trap WFE execution by the Plane.                                                                                                                                  | RsiTrap     |
| trap_hc   |      2 | Whether to trap RSI_HOST_CALL execution by the Plane. RSI_TRAP: execution of RSI_HOST_CALL causes Plane exit RSI_NO_TRAP: execution of RSI_HOST_CALL causes REC exit to Host | RsiTrap     |
| gic_owner |      3 | Whether to transfer GIC ownership to the target Plane.                                                                                                                       | RsiGicOwner |

| Name      | Bits   | Description                                            | Value   |
|-----------|--------|--------------------------------------------------------|---------|
| trap_simd | 4      | Whether to trap access to SIMD and SVE by the Plane.   | RsiTrap |
| trap_dbg  | 5      | Whether to trap debug exceptions taken from the Plane. | RsiTrap |
|           | 63:6   | Reserved                                               | SBZ     |

The RsiPlaneEnterFlags fieldset is used in the following types:

## · RsiPlaneEnter

## B5.5.15 RsiPlaneExit type

The RsiPlaneExit structure contains data passed from the RMM to P0 on Plane exit.

The RsiPlaneExit structure is a concrete type.

The width of the RsiPlaneExit structure is 2048 ( 0x800 ) bytes.

The members of the RsiPlaneExit structure are shown in the following table.

| Name          | Byte offset   | Type                     | Description                                              |
|---------------|---------------|--------------------------|----------------------------------------------------------|
| reason        | 0x0            RsiPlaneExitReason | Exit reason                                              |
| pc            | 0x8           | Bits64                   | Program counter                                          |
| pstate        | 0x10          | Bits64                   | PSTATE                                                   |
| gprs[31]      | 0x100         | Bits64                   | Registers                                                |
| esr_el2       | 0x200         | Bits64                   | Exception Syndrome Register                              |
| far_el2       | 0x208         | Bits64                   | Fault Address Register                                   |
| hpfar_el2     | 0x210         | Bits64                   | Hypervisor IPA Fault Address register                    |
| gicv3_hcr     | 0x300         | Bits64                   | GICv3 Hypervisor Control Register value                  |
| gicv3_lrs[16] | 0x308         | Bits64                   | GICv3 List Register values                               |
| gicv3_misr    | 0x388         | Bits64                   | GICv3 Maintenance Interrupt State Register value         |
| gicv3_vmcr    | 0x390         | Bits64                   | GICv3 Virtual Machine Control Register value             |
| cntp_ctl      | 0x400         | Bits64                   | Counter-timer Physical Timer Control Register value      |
| cntp_cval     | 0x408         | Bits64                   | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl      | 0x410         | Bits64                   | Counter-timer Virtual Timer Control Register value       |
| cntv_cval     | 0x418         | Bits64                   | Counter-timer Virtual Timer CompareValue Register value  |
| sctlr_el1     | 0x500         | Bits64                   | SCTLR_EL1 value                                          |

| Name           | Byte offset   | Type                 | Description         |
|----------------|---------------|----------------------|---------------------|
| vbar_el1       | 0x508         | Bits64               | VBAR_EL1 value      |
| elr_el1        | 0x510         | Bits64               | ELR_EL1 value       |
| pmu_ovf_status | 0x600         | RsiPmuOverflowStatus | PMU overflow status |

Unused bits of the RsiPlaneExit structure SBZ.

The RsiPlaneExit structure is used in the following types:

- RsiPlaneRun

## B5.5.16 RsiPlaneExitReason type

The RsiPlaneExitReason enumeration represents the reason for a Plane exit.

The RsiPlaneExitReason enumeration is a concrete type.

The width of the RsiPlaneExitReason enumeration is 8 bits.

The values of the RsiPlaneExitReason enumeration are shown in the following table.

|   Encoding | Name          | Description                             |
|------------|---------------|-----------------------------------------|
|          0 | RSI_EXIT_SYNC | Plane exit due to synchronous exception |
|          1 | RSI_EXIT_IRQ  | Plane exit due to IRQ                   |
|          2 | RSI_EXIT_HOST | Plane exit due to Host action           |

Unused encodings for the RsiPlaneExitReason enumeration are reserved for use by future versions of this specification.

The RsiPlaneExitReason enumeration is used in the following types:

- RsiPlaneExit

## B5.5.17 RsiPlaneRun type

The RsiPlaneRun structure contains fields used to share information between RMM and P0 during Plane entry and Plane exit.

The RsiPlaneRun structure is a concrete type.

The width of the RsiPlaneRun structure is 4096 ( 0x1000 ) bytes.

The members of the RsiPlaneRun structure are shown in the following table.

| Name   | Byte offset   | Type          | Description       |
|--------|---------------|---------------|-------------------|
| enter  | 0x0           | RsiPlaneEnter | Entry information |
| exit   | 0x800         | RsiPlaneExit  | Exit information  |


## B5.5.18 RsiPmuOverflowStatus type

The RsiPmuOverflowStatus enumeration represents PMU overflow status.

The RsiPmuOverflowStatus enumeration is a concrete type.

The width of the RsiPmuOverflowStatus enumeration is 8 bits.

The values of the RsiPmuOverflowStatus enumeration are shown in the following table.

|   Encoding | Name                        | Description                 |
|------------|-----------------------------|-----------------------------|
|          0 | RSI_PMU_OVERFLOW_NOT_ACTIVE | PMU overflow is not active. |
|          1 | RSI_PMU_OVERFLOW_ACTIVE     | PMU overflow is active.     |

Unused encodings for the RsiPmuOverflowStatus enumeration are reserved for use by future versions of this specification.

The RsiPmuOverflowStatus enumeration is used in the following types:

- RsiPlaneExit

## B5.5.19 RsiRealmConfig type

The RsiRealmConfig structure contains realm configuration.

The RsiRealmConfig structure is a concrete type.

The width of the RsiRealmConfig structure is 4096 ( 0x1000 ) bytes.

See also:

- [B5.4.16 RSI\_REALM\_CONFIG command](rmm-B5.4.16.md)

The members of the RsiRealmConfig structure are shown in the following table.

| Name           | Byte offset   | Type             | Description                                                                                              |
|----------------|---------------|------------------|----------------------------------------------------------------------------------------------------------|
| ipa_width      | 0x0           | UInt64           | IPA width in bits                                                                                        |
| hash_algo      | 0x8           | RsiHashAlgorithm | Hash algorithm                                                                                           |
| num_aux_planes | 0x10          | UInt64           | Number of auxiliary Planes                                                                               |
| gicv3_vtr      | 0x18          | Bits64           | GICv3 VGIC Type Register value                                                                           |
| ats_plane      | 0x20          | UInt64           | Index of Plane whose stage 2 permissions are observed by ATS requests from devices assigned to the Realm |
| rpv            | 0x200         | Bits512          | Realm Personalization Value                                                                              |


Unused bits of the RsiRealmConfig structure MBZ.

## B5.5.20 RsiResponse type

The RsiResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RsiResponse enumeration is a concrete type.

The width of the RsiResponse enumeration is 1 bits.

The values of the RsiResponse enumeration are shown in the following table.

|   Encoding | Name                | Description                      |
|------------|---------------------|----------------------------------|
|          0 | RSI_RESPONSE_ACCEPT | Host accepted the Realm request. |
|          1 | RSI_RESPONSE_REJECT | Host rejected the Realm request. |

## B5.5.21 RsiRipas type

The RsiRipas enumeration represents realm IPA state.

The RsiRipas enumeration is a concrete type.

The width of the RsiRipas enumeration is 8 bits.

See also:

- [A5.4 RIPAS change](rmm-A5.4.md)
- [B5.4.6 RSI\_IPA\_STATE\_GET command](rmm-B5.4.6.md)
- [B5.4.7 RSI\_IPA\_STATE\_SET command](rmm-B5.4.7.md)

The values of the RsiRipas enumeration are shown in the following table.

|   Encoding | Name                | Description                                                                    |
|------------|---------------------|--------------------------------------------------------------------------------|
|          0 | RSI_RIPAS_EMPTY     | Address where no Realm resources are mapped.                                   |
|          1 | RSI_RIPAS_RAM       | Address where private code or data owned by the Realm is mapped.               |
|          2 | RSI_RIPAS_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
|          3 | RSI_RIPAS_DEV       | Address where memory of an assigned Realm device is mapped.                    |


Unused encodings for the RsiRipas enumeration are reserved for use by future versions of this specification.

## B5.5.22 RsiRipasChangeDestroyed type

The RsiRipasChangeDestroyed enumeration represents whether a RIPAS change from RIPAS\_DESTROYED to RIPAS\_RAM should be permitted.

The RsiRipasChangeDestroyed enumeration is a concrete type.

The width of the RsiRipasChangeDestroyed enumeration is 1 bits.

The values of the RsiRipasChangeDestroyed enumeration are shown in the following table.

|   Encoding | Name                    | Description                                                               |
|------------|-------------------------|---------------------------------------------------------------------------|
|          0 | RSI_NO_CHANGE_DESTROYED | A RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should not be permitted. |
|          1 | RSI_CHANGE_DESTROYED    | A RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should be permitted.     |

The RsiRipasChangeDestroyed enumeration is used in the following types:

- RsiRipasChangeFlags

## B5.5.23 RsiRipasChangeFlags type

The RsiRipasChangeFlags fieldset contains flags provided by the Realm when requesting a RIPAS change.

The RsiRipasChangeFlags fieldset is a concrete type.

The width of the RsiRipasChangeFlags fieldset is 64 bits.

The fields of the RsiRipasChangeFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RsiRipasChangeFlags fieldset are shown in the following table.

| Name      | Bits   | Description                                                                  | Value                   |
|-----------|--------|------------------------------------------------------------------------------|-------------------------|
| destroyed | 0      | Whether a RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should be permitted | RsiRipasChangeDestroyed |
|           | 63:1   | Reserved                                                                     | SBZ                     |


## B5.5.24 RsiSysregAddress type

The RsiSysregAddress fieldset contains system register address.

The RsiSysregAddress fieldset is a concrete type.

The width of the RsiSysregAddress fieldset is 64 bits.

The fields of the RsiSysregAddress fieldset are shown in the following diagram.

The fields of the RsiSysregAddress fieldset are shown in the following table.

| Name   | Bits   | Description                   | Value      |
|--------|--------|-------------------------------|------------|
| Op2    | 2:0    | Op2                           | Bits3      |
| CRm    | 6:3    | CRm                           | Bits4      |
| CRn    | 10:7   | CRn                           | Bits4      |
| Op1    | 13:11  | Op1                           | Bits3      |
| Op0    | 15:14  | Op0                           | Bits2      |
| d128   | 16     | Perform 128-bit sysreg access | RsiBoolean |
|        | 63:17  | Reserved                      | SBZ        |

## B5.5.25 RsiTrap type

The RsiTrap enumeration represents whether a trap is enabled.


The RsiTrap enumeration is a concrete type.

The width of the RsiTrap enumeration is 1 bits.

The values of the RsiTrap enumeration are shown in the following table.

|   Encoding | Name        | Description       |
|------------|-------------|-------------------|
|          0 | RSI_NO_TRAP | Trap is disabled. |
|          1 | RSI_TRAP    | Trap is enabled.  |

The RsiTrap enumeration is used in the following types:

- RsiPlaneEnterFlags

## B5.5.26 RsiVdevDmaFlags type

The RsiVdevDmaFlags fieldset contains flags which control device DMA.

The RsiVdevDmaFlags fieldset is a concrete type.

The width of the RsiVdevDmaFlags fieldset is 64 bits.

The fields of the RsiVdevDmaFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RsiVdevDmaFlags fieldset are shown in the following table.

| Name   | Bits   | Description                            | Value      |
|--------|--------|----------------------------------------|------------|
| ats    | 0      | Whether to enable ATS for this device. | RsiFeature |
|        | 63:1   | Reserved                               | SBZ        |

## B5.5.27 RsiVdevFlags type

The RsiVdevFlags fieldset contains flags which describe properties of a device.

The RsiVdevFlags fieldset is a concrete type.

The width of the RsiVdevFlags fieldset is 64 bits.

The fields of the RsiVdevFlags fieldset are shown in the following diagram.


<!-- image -->

The fields of the RsiVdevFlags fieldset are shown in the following table.

| Name        | Bits   | Description                                      | Value      |
|-------------|--------|--------------------------------------------------|------------|
| vsmmu       | 0      | Whether this device is associated with a VSMMU   | RsiFeature |
| p2p_enabled | 1      | Whether this device can be added to a P2P stream | RsiFeature |
| p2p_bound   | 2      | Whether this device is bound to a peer VDEV      | RsiFeature |
|             | 63:3   | Reserved                                         | MBZ        |

The RsiVdevFlags fieldset is used in the following types:

- RsiVdevInfo

## B5.5.28 RsiVdevInfo type

The RsiVdevInfo structure contains device configuration information.

The RsiVdevInfo structure is a concrete type.

The width of the RsiVdevInfo structure is 512 ( 0x200 ) bytes.

See also:

- [A9.6 Realm management of an assigned virtual device](rmm-A9.6.md)
- [B5.4.19 RSI\_VDEV\_GET\_INFO command](rmm-B5.4.19.md)

The members of the RsiVdevInfo structure are shown in the following table.

| Name                 | Byte offset   | Type                    | Description                                                                                                                                                                                |
|----------------------|---------------|-------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags                | 0x0           | RsiVdevFlags            | Flags                                                                                                                                                                                      |
| id_index             | 0x8           | UInt64                  | Device identity index                                                                                                                                                                      |
| hash_algo            | 0x10          | RsiHashAlgorithm        | Algorithm used to generate device digests                                                                                                                                                  |
| lock_nonce           | 0x18          | UInt64                  | Nonce generated on most recent transition to LOCKED state                                                                                                                                  |
| meas_nonce           | 0x20          | UInt64                  | Nonce generated on most recent GET_MEASUREMENT request                                                                                                                                     |
| report_nonce         | 0x28          | UInt64                  | Nonce generated on most recent GET_INTERFACE_REPORT request                                                                                                                                |
| format_type          | 0x30          | RsiVdevReportFormatType | Report format type                                                                                                                                                                         |
| format_version       | 0x38          | Bits64                  | Report format version If format_type is RSI_VDEV_REPORT_FORMAT_TDISP then this field specifies the TDISP version, encoded as follows: bits[31:16]: major version bits[15:0]: minor version |
| state                | 0x40          | RsiVdevState            | State of the device                                                                                                                                                                        |
| negotiation_data_dig | 0x80          | Bits512                 | Negotiation data digest                                                                                                                                                                    |


est

| Name            | Byte offset   | Type    | Description                                                                                                              |
|-----------------|---------------|---------|--------------------------------------------------------------------------------------------------------------------------|
| identity_digest | 0xc0          | Bits512 | Identity digest                                                                                                          |
| pubkey_digest   | 0x100         | Bits512 | Public key digest                                                                                                        |
| meas_digest     | 0x140         | Bits512 | Measurement digest                                                                                                       |
| report_digest   | 0x180         | Bits512 | Interface report digest                                                                                                  |
| vsmmu_addr      | 0x1c0         | Address | Base IPA of the VSMMU which is associated with this device. This field is valid only if flags.vsmmu == RSI_FEATURE_TRUE. |
| vsmmu_vsid      | 0x1c8         | Bits64  | Virtual Stream ID. This field is valid only if flags.vsmmu == RSI_FEATURE_TRUE.                                          |

Unused bits of the RsiVdevInfo structure MBZ.

## B5.5.29 RsiVdevReportFormatType type

The RsiVdevReportFormatType enumeration represents device report format type.

The RsiVdevReportFormatType enumeration is a concrete type.

The width of the RsiVdevReportFormatType enumeration is 8 bits.

The values of the RsiVdevReportFormatType enumeration are shown in the following table.

|   Encoding | Name                          | Description                                  |
|------------|-------------------------------|----------------------------------------------|
|          0 | RSI_VDEV_REPORT_FORMAT_IMPDEF | The report format is IMPLEMENTATION DEFINED. |
|          1 | RSI_VDEV_REPORT_FORMAT_TDISP  | The report format is TDISP.                  |


Unused encodings for the RsiVdevReportFormatType enumeration are reserved for use by future versions of this specification.

The RsiVdevReportFormatType enumeration is used in the following types:

- RsiVdevInfo

## B5.5.30 RsiVdevState type

The RsiVdevState enumeration represents the state of a VDEV.

The RsiVdevState enumeration is a concrete type.

The width of the RsiVdevState enumeration is 8 bits.

The values of the RsiVdevState enumeration are shown in the following table.

|   Encoding | Name              | Description                   |
|------------|-------------------|-------------------------------|
|          0 | RSI_VDEV_UNLOCKED | Device interface is unlocked. |
|          1 | RSI_VDEV_LOCKED   | Device interface is locked.   |

|   Encoding | Name             | Description                                  |
|------------|------------------|----------------------------------------------|
|          2 | RSI_VDEV_STARTED | Device interface is started.                 |
|          3 | RSI_VDEV_ERROR   | Device interface has reported a fatal error. |

Unused encodings for the RsiVdevState enumeration are reserved for use by future versions of this specification.

The RsiVdevState enumeration is used in the following types:

- RsiVdevInfo

<!-- image -->