## B4.4 RMI types

This section defines types which are used in the RMI interface.

## B4.4.1 RmiCommandReturnCode type

The RmiCommandReturnCode fieldset contains a return code from an RMI command.

The RmiCommandReturnCode fieldset is a concrete type.

The width of the RmiCommandReturnCode fieldset is 64 bits.

See also:

- Chapter B1 Commands

The fields of the RmiCommandReturnCode fieldset are shown in the following diagram.

<!-- image -->

| 63   | 32     |
|------|--------|
| MBZ  | MBZ    |
| 31   | 0      |
| MBZ  | status |

The fields of the RmiCommandReturnCode fieldset are shown in the following table.

| Name   | Bits   | Description                                             | Value         |
|--------|--------|---------------------------------------------------------|---------------|
| status | 7:0    | Status of the command                                   | RmiStatusCode |
| index  | 15:8   | Index which identifies the reason for a command failure | UInt8         |
|        | 63:16  | Reserved                                                | MBZ           |

## B4.4.2 RmiDataFlags type

The RmiDataFlags fieldset contains flags provided by the Host during DATA Granule creation.

The RmiDataFlags fieldset is a concrete type.

The width of the RmiDataFlags fieldset is 64 bits.

The fields of the RmiDataFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiDataFlags fieldset are shown in the following table.

| Name    | Bits   | Description                              | Value                 |
|---------|--------|------------------------------------------|-----------------------|
| measure | 0:0    | Whether to measure DATA Granule contents | RmiDataMeasureContent |
|         | 63:1   | Reserved                                 | SBZ                   |

## B4.4.3 RmiDataMeasureContent type

The RmiDataMeasureContent enumeration represents whether to measure DATA Granule contents.

The RmiDataMeasureContent enumeration is a concrete type.

The width of the RmiDataMeasureContent enumeration is 1 bits.

The values of the RmiDataMeasureContent enumeration are shown in the following table.

|   Encoding | Name                   | Description                           |
|------------|------------------------|---------------------------------------|
|          0 | RMI_NO_MEASURE_CONTENT | Do not measure DATA Granule contents. |
|          1 | RMI_MEASURE_CONTENT    | Measure DATA Granule contents.        |

## B4.4.4 RmiEmulatedMmio type

The RmiEmulatedMmio enumeration represents whether the host has completed emulation for an Emulatable Abort.

The RmiEmulatedMmio enumeration is a concrete type.

The width of the RmiEmulatedMmio enumeration is 1 bits.

The values of the RmiEmulatedMmio enumeration are shown in the following table.

|   Encoding | Name                  | Description                                               |
|------------|-----------------------|-----------------------------------------------------------|
|          0 | RMI_NOT_EMULATED_MMIO | Host has not completed emulation for an Emulatable Abort. |
|          1 | RMI_EMULATED_MMIO     | Host has completed emulation for an Emulatable Abort.     |

## B4.4.5 RmiFeature type

The RmiFeature enumeration represents whether a feature is supported or enabled.

The RmiFeature enumeration is a concrete type.

The width of the RmiFeature enumeration is 1 bits.

The values of the RmiFeature enumeration are shown in the following table.

|   Encoding | Name              | Description                                                                               |
|------------|-------------------|-------------------------------------------------------------------------------------------|
|          0 | RMI_FEATURE_FALSE | • During discovery: Feature is not supported. • During selection: Feature is not enabled. |

|   Encoding | Name             | Description                                                                       |
|------------|------------------|-----------------------------------------------------------------------------------|
|          1 | RMI_FEATURE_TRUE | • During discovery: Feature is supported. • During selection: Feature is enabled. |

## B4.4.6 RmiFeatureRegister0 type

The RmiFeatureRegister0 fieldset contains feature register 0.

The RmiFeatureRegister0 fieldset is a concrete type.

The width of the RmiFeatureRegister0 fieldset is 64 bits.

## See also:

- A3.1 Realm feature discovery and selection
- B4.3.4 RMI\_FEATURES command

The fields of the RmiFeatureRegister0 fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiFeatureRegister0 fieldset are shown in the following table.

| Name    | Bits   | Description                                                                                                                                                                                                                           | Value      |
|---------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| S2SZ    | 7:0    | Maximum Realm IPA width supported by the RMM. Specifies the input address size for stage 2 translation to be 2 ^ S2SZ . Note this format expresses the IPA width directly and is therefore different from the VTCR_EL2.T0SZ encoding. | UInt8      |
| LPA2    | 8:8    | Whether LPA2 is supported.                                                                                                                                                                                                            | RmiFeature |
| SVE_EN  | 9:9    | Whether SVE is supported.                                                                                                                                                                                                             | RmiFeature |
| SVE_VL  | 13:10  | Maximum SVE vector length supported by the RMM. The effective vector length supported by the RMMis (SVE_VL + 1)*128 , similar to the value of ZCR_ELx.LEN .                                                                           | UInt4      |
| NUM_BPS | 19:14  | Number of breakpoints available, minus one. The value 0 is reserved.                                                                                                                                                                  | UInt6      |

| Name           | Bits   | Description                                                                                                                                               | Value      |
|----------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| NUM_WPS        | 25:20  | Number of watchpoints available, minus one. The value 0 is reserved.                                                                                      | UInt6      |
| PMU_EN         | 26:26  | Whether PMU is supported                                                                                                                                  | RmiFeature |
| PMU_NUM_CTRS   | 31:27  | Number of PMU counters available                                                                                                                          | UInt5      |
| HASH_SHA_256   | 32:32  | Whether SHA-256 is supported                                                                                                                              | RmiFeature |
| HASH_SHA_512   | 33:33  | Whether SHA-512 is supported                                                                                                                              | RmiFeature |
| GICV3_NUM_LRS  | 37:34  | Number of GICv3 List Registers which are available, minus one.                                                                                            | UInt4      |
| MAX_RECS_ORDER | 41:38  | Order of the maximum number of RECs which can be created per Realm. The maximum number of RECs is computed as follows: MAX_RECS = (2 ^ MAX_RECS_ORDER)- 1 | UInt4      |

## B4.4.7 RmiHashAlgorithm type

The RmiHashAlgorithm enumeration represents hash algorithm.

The RmiHashAlgorithm enumeration is a concrete type.

The width of the RmiHashAlgorithm enumeration is 8 bits.

The values of the RmiHashAlgorithm enumeration are shown in the following table.

|   Encoding | Name             | Description                                |
|------------|------------------|--------------------------------------------|
|          0 | RMI_HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [15]) |
|          1 | RMI_HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [15]) |

Unused encodings for the RmiHashAlgorithm enumeration are reserved for use by future versions of this specification.

## B4.4.8 RmiInjectSea type

The RmiInjectSea enumeration represents whether to inject a Synchronous External Abort into the Realm.

The RmiInjectSea enumeration is a concrete type.

The width of the RmiInjectSea enumeration is 1 bits.

The values of the RmiInjectSea enumeration are shown in the following table.

|   Encoding | Name              | Description                          |
|------------|-------------------|--------------------------------------|
|          0 | RMI_NO_INJECT_SEA | Do not inject an SEA into the Realm. |
|          1 | RMI_INJECT_SEA    | Inject an SEA into the Realm.        |

## B4.4.9 RmiInterfaceVersion type

The RmiInterfaceVersion fieldset contains an RMI interface version.

The RmiInterfaceVersion fieldset is a concrete type.

The width of the RmiInterfaceVersion fieldset is 64 bits.

See also:

- B4.1 RMI version
- B4.3.23 RMI\_VERSION command

The fields of the RmiInterfaceVersion fieldset are shown in the following diagram.

<!-- image -->

| 63    |             | 32          |
|-------|-------------|-------------|
| MBZ   | MBZ         | MBZ         |
| 30 31 |             | 0           |
| MBZ   | minor major | minor major |

The fields of the RmiInterfaceVersion fieldset are shown in the following table.

| Name   | Bits   | Description                                                            | Value   |
|--------|--------|------------------------------------------------------------------------|---------|
| minor  | 15:0   | Interface minor version number (the value y in interface version x.y ) | UInt16  |
| major  | 30:16  | Interface major version number (the value x in interface version x.y ) | UInt15  |
|        | 63:31  | Reserved                                                               | MBZ     |

## B4.4.10 RmiPmuOverflowStatus type

The RmiPmuOverflowStatus enumeration represents PMU overflow status.

The RmiPmuOverflowStatus enumeration is a concrete type.

The width of the RmiPmuOverflowStatus enumeration is 8 bits.

The values of the RmiPmuOverflowStatus enumeration are shown in the following table.

|   Encoding | Name                        | Description                 |
|------------|-----------------------------|-----------------------------|
|          0 | RMI_PMU_OVERFLOW_NOT_ACTIVE | PMU overflow is not active. |
|          1 | RMI_PMU_OVERFLOW_ACTIVE     | PMU overflow is active.     |

Unused encodings for the RmiPmuOverflowStatus enumeration are reserved for use by future versions of this specification.

## B4.4.11 RmiRealmFlags type

The RmiRealmFlags fieldset contains flags provided by the Host during Realm creation.

The RmiRealmFlags fieldset is a concrete type.

The width of the RmiRealmFlags fieldset is 64 bits.

The fields of the RmiRealmFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRealmFlags fieldset are shown in the following table.

| Name   | Bits   | Description             | Value      |
|--------|--------|-------------------------|------------|
| lpa2   | 0:0    | Whether LPA2 is enabled | RmiFeature |
| sve    | 1:1    | Whether SVE is enabled  | RmiFeature |
| pmu    | 2:2    | Whether PMU is enabled  | RmiFeature |
|        | 63:3   | Reserved                | SBZ        |

## B4.4.12 RmiRealmParams type

The RmiRealmParams structure contains parameters provided by the Host during Realm creation.

The RmiRealmParams structure is a concrete type.

The width of the RmiRealmParams structure is 4096 ( 0x1000 ) bytes.

## See also:

- A2.1.6 Realm parameters
- B4.3.9 RMI\_REALM\_CREATE command

The members of the RmiRealmParams structure are shown in the following table.

| Name   | Byte offset   | Type          | Description                                                                                                                                                                                                  |
|--------|---------------|---------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| flags  | 0x0           | RmiRealmFlags | Flags                                                                                                                                                                                                        |
| s2sz   | 0x8           | UInt8         | Requested IPA width. Specifies the input address size for stage 2 translation to be 2 ^ S2SZ . Note this format expresses the IPA width directly and is therefore different from the VTCR_EL2.T0SZ encoding. |
| sve_vl | 0x10          | UInt8         | Requested SVE vector length. The effective vector length requested is (sve_vl + 1)*128 , similar to the value of ZCR_ELx.LEN .                                                                               |

| Name            | Byte offset   | Type             | Description                                                |
|-----------------|---------------|------------------|------------------------------------------------------------|
| num_bps         | 0x18          | UInt8            | Number of breakpoints, minus one. The value 0 is reserved. |
| num_wps         | 0x20          | UInt8            | Number of watchpoints, minus one. The value 0 is reserved. |
| pmu_num_ctrs    | 0x28          | UInt8            | Requested number of PMU counters                           |
| hash_algo       | 0x30          | RmiHashAlgorithm | Algorithm used to measure the initial state of the Realm   |
| rpv             | 0x400         | Bits512          | Realm Personalization Value                                |
| vmid            | 0x800         | Bits16           | Virtual Machine Identifier                                 |
| rtt_base        | 0x808         | Address          | Realm Translation Table base                               |
| rtt_level_start | 0x810         | Int64            | RTT starting level                                         |
| rtt_num_start   | 0x818         | UInt32           | Number of starting level RTTs                              |

Unused bits of the RmiRealmParams structure SBZ.

## B4.4.13 RmiRecCreateFlags type

The RmiRecCreateFlags fieldset contains flags provided by the Host during REC creation.

The RmiRecCreateFlags fieldset is a concrete type.

The width of the RmiRecCreateFlags fieldset is 64 bits.

The fields of the RmiRecCreateFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRecCreateFlags fieldset are shown in the following table.

| Name     | Bits   | Description                           | Value          |
|----------|--------|---------------------------------------|----------------|
| runnable | 0:0    | Whether REC is eligible for execution | RmiRecRunnable |
|          | 63:1   | Reserved                              | SBZ            |

## B4.4.14 RmiRecEnter type

The RmiRecEnter structure contains data passed from the Host to the RMM on REC entry.

The RmiRecEnter structure is a concrete type.

The width of the RmiRecEnter structure is 2048 ( 0x800 ) bytes.

See also:

- A4.2.1 RmiRecEnter object
- B4.3.14 RMI\_REC\_ENTER command
- B4.4.16 RmiRecExit type

The members of the RmiRecEnter structure are shown in the following table.

| Name     | Byte offset   | Type             | Description   |
|----------|---------------|------------------|---------------|
| flags    | 0x0           | RmiRecEnterFlags | Flags         |
| gprs[0]  | 0x200         | Bits64           | Registers     |
| gprs[1]  | 0x208         | Bits64           | Registers     |
| gprs[2]  | 0x210         | Bits64           | Registers     |
| gprs[3]  | 0x218         | Bits64           | Registers     |
| gprs[4]  | 0x220         | Bits64           | Registers     |
| gprs[5]  | 0x228         | Bits64           | Registers     |
| gprs[6]  | 0x230         | Bits64           | Registers     |
| gprs[7]  | 0x238         | Bits64           | Registers     |
| gprs[8]  | 0x240         | Bits64           | Registers     |
| gprs[9]  | 0x248         | Bits64           | Registers     |
| gprs[10] | 0x250         | Bits64           | Registers     |
| gprs[11] | 0x258         | Bits64           | Registers     |
| gprs[12] | 0x260         | Bits64           | Registers     |
| gprs[13] | 0x268         | Bits64           | Registers     |
| gprs[14] | 0x270         | Bits64           | Registers     |
| gprs[15] | 0x278         | Bits64           | Registers     |
| gprs[16] | 0x280         | Bits64           | Registers     |
| gprs[17] | 0x288         | Bits64           | Registers     |
| gprs[18] | 0x290         | Bits64           | Registers     |
| gprs[19] | 0x298         | Bits64           | Registers     |
| gprs[20] | 0x2a0         | Bits64           | Registers     |
| gprs[21] | 0x2a8         | Bits64           | Registers     |
| gprs[22] | 0x2b0         | Bits64           | Registers     |
| gprs[23] | 0x2b8         | Bits64           | Registers     |
| gprs[24] | 0x2c0         | Bits64           | Registers     |

| Name          | Byte offset   | Type   | Description                             |
|---------------|---------------|--------|-----------------------------------------|
| gprs[25]      | 0x2c8         | Bits64 | Registers                               |
| gprs[26]      | 0x2d0         | Bits64 | Registers                               |
| gprs[27]      | 0x2d8         | Bits64 | Registers                               |
| gprs[28]      | 0x2e0         | Bits64 | Registers                               |
| gprs[29]      | 0x2e8         | Bits64 | Registers                               |
| gprs[30]      | 0x2f0         | Bits64 | Registers                               |
| gicv3_hcr     | 0x300         | Bits64 | GICv3 Hypervisor Control Register value |
| gicv3_lrs[0]  | 0x308         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[1]  | 0x310         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[2]  | 0x318         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[3]  | 0x320         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[4]  | 0x328         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[5]  | 0x330         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[6]  | 0x338         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[7]  | 0x340         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[8]  | 0x348         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[9]  | 0x350         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[10] | 0x358         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[11] | 0x360         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[12] | 0x368         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[13] | 0x370         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[14] | 0x378         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[15] | 0x380         | Bits64 | GICv3 List Register values              |

Unused bits of the RmiRecEnter structure SBZ.

## B4.4.15 RmiRecEnterFlags type

The RmiRecEnterFlags fieldset contains flags provided by the Host during REC entry.

The RmiRecEnterFlags fieldset is a concrete type.

The width of the RmiRecEnterFlags fieldset is 64 bits.

The fields of the RmiRecEnterFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRecEnterFlags fieldset are shown in the following table.

| Name           | Bits   | Description                                                           | Value           |
|----------------|--------|-----------------------------------------------------------------------|-----------------|
| emul_mmio      | 0:0    | Whether the host has completed emulation for an Emulatable Data Abort | RmiEmulatedMmio |
| inject_sea     | 1:1    | Whether to inject a Synchronous External Abort into the Realm.        | RmiInjectSea    |
| trap_wfi       | 2:2    | Whether to trap WFI execution by the Realm.                           | RmiTrap         |
| trap_wfe       | 3:3    | Whether to trap WFE execution by the Realm.                           | RmiTrap         |
| ripas_response | 4:4    | Host response to RIPAS change request.                                | RmiResponse     |
|                | 63:5   | Reserved                                                              | SBZ             |

## B4.4.16 RmiRecExit type

The RmiRecExit structure contains data passed from the RMM to the Host on REC exit.

The RmiRecExit structure is a concrete type.

The width of the RmiRecExit structure is 2048 ( 0x800 ) bytes.

## See also:

- A4.3.1 RmiRecExit object
- B4.3.14 RMI\_REC\_ENTER command
- B4.4.14 RmiRecEnter type

The members of the RmiRecExit structure are shown in the following table.

| Name        | Byte offset   | Type             | Description                           |
|-------------|---------------|------------------|---------------------------------------|
| exit_reason | 0x0           | RmiRecExitReason | Exit reason                           |
| esr         | 0x100         | Bits64           | Exception Syndrome Register           |
| far         | 0x108         | Bits64           | Fault Address Register                |
| hpfar       | 0x110         | Bits64           | Hypervisor IPA Fault Address register |
| gprs[0]     | 0x200         | Bits64           | Registers                             |

| Name         | Byte offset   | Type   | Description                             |
|--------------|---------------|--------|-----------------------------------------|
| gprs[1]      | 0x208         | Bits64 | Registers                               |
| gprs[2]      | 0x210         | Bits64 | Registers                               |
| gprs[3]      | 0x218         | Bits64 | Registers                               |
| gprs[4]      | 0x220         | Bits64 | Registers                               |
| gprs[5]      | 0x228         | Bits64 | Registers                               |
| gprs[6]      | 0x230         | Bits64 | Registers                               |
| gprs[7]      | 0x238         | Bits64 | Registers                               |
| gprs[8]      | 0x240         | Bits64 | Registers                               |
| gprs[9]      | 0x248         | Bits64 | Registers                               |
| gprs[10]     | 0x250         | Bits64 | Registers                               |
| gprs[11]     | 0x258         | Bits64 | Registers                               |
| gprs[12]     | 0x260         | Bits64 | Registers                               |
| gprs[13]     | 0x268         | Bits64 | Registers                               |
| gprs[14]     | 0x270         | Bits64 | Registers                               |
| gprs[15]     | 0x278         | Bits64 | Registers                               |
| gprs[16]     | 0x280         | Bits64 | Registers                               |
| gprs[17]     | 0x288         | Bits64 | Registers                               |
| gprs[18]     | 0x290         | Bits64 | Registers                               |
| gprs[19]     | 0x298         | Bits64 | Registers                               |
| gprs[20]     | 0x2a0         | Bits64 | Registers                               |
| gprs[21]     | 0x2a8         | Bits64 | Registers                               |
| gprs[22]     | 0x2b0         | Bits64 | Registers                               |
| gprs[23]     | 0x2b8         | Bits64 | Registers                               |
| gprs[24]     | 0x2c0         | Bits64 | Registers                               |
| gprs[25]     | 0x2c8         | Bits64 | Registers                               |
| gprs[26]     | 0x2d0         | Bits64 | Registers                               |
| gprs[27]     | 0x2d8         | Bits64 | Registers                               |
| gprs[28]     | 0x2e0         | Bits64 | Registers                               |
| gprs[29]     | 0x2e8         | Bits64 | Registers                               |
| gprs[30]     | 0x2f0         | Bits64 | Registers                               |
| gicv3_hcr    | 0x300         | Bits64 | GICv3 Hypervisor Control Register value |
| gicv3_lrs[0] | 0x308         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[1] | 0x310         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[2] | 0x318         | Bits64 | GICv3 List Register values              |
| gicv3_lrs[3] | 0x320         | Bits64 | GICv3 List Register values              |

| Name           | Byte offset   | Type                 | Description                                              |
|----------------|---------------|----------------------|----------------------------------------------------------|
| gicv3_lrs[4]   | 0x328         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[5]   | 0x330         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[6]   | 0x338         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[7]   | 0x340         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[8]   | 0x348         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[9]   | 0x350         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[10]  | 0x358         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[11]  | 0x360         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[12]  | 0x368         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[13]  | 0x370         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[14]  | 0x378         | Bits64               | GICv3 List Register values                               |
| gicv3_lrs[15]  | 0x380         | Bits64               | GICv3 List Register values                               |
| gicv3_misr     | 0x388         | Bits64               | GICv3 Maintenance Interrupt State Register value         |
| gicv3_vmcr     | 0x390         | Bits64               | GICv3 Virtual Machine Control Register value             |
| cntp_ctl       | 0x400         | Bits64               | Counter-timer Physical Timer Control Register value      |
| cntp_cval      | 0x408         | Bits64               | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl       | 0x410         | Bits64               | Counter-timer Virtual Timer Control Register value       |
| cntv_cval      | 0x418         | Bits64               | Counter-timer Virtual Timer CompareValue Register value  |
| ripas_base     | 0x500         | Bits64               | Base address of target region for pending RIPAS change   |
| ripas_top      | 0x508         | Bits64               | Top address of target region for pending RIPAS change    |
| ripas_value    | 0x510         | RmiRipas             | RIPAS value of pending RIPAS change                      |
| imm            | 0x600         | Bits16               | Host call immediate value                                |
| pmu_ovf_status | 0x700         | RmiPmuOverflowStatus | PMU overflow status                                      |

Unused bits of the RmiRecExit structure MBZ.

## B4.4.17 RmiRecExitReason type

The RmiRecExitReason enumeration represents the reason for a REC exit.

The RmiRecExitReason enumeration is a concrete type.

The width of the RmiRecExitReason enumeration is 8 bits.

The values of the RmiRecExitReason enumeration are shown in the following table.

|   Encoding | Name                  | Description                           |
|------------|-----------------------|---------------------------------------|
|          0 | RMI_EXIT_SYNC         | REC exit due to synchronous exception |
|          1 | RMI_EXIT_IRQ          | REC exit due to IRQ                   |
|          2 | RMI_EXIT_FIQ          | REC exit due to FIQ                   |
|          3 | RMI_EXIT_PSCI         | REC exit due to PSCI                  |
|          4 | RMI_EXIT_RIPAS_CHANGE | REC exit due to RIPAS change pending  |
|          5 | RMI_EXIT_HOST_CALL    | REC exit due to Host call             |
|          6 | RMI_EXIT_SERROR       | REC exit due to SError                |

Unused encodings for the RmiRecExitReason enumeration are reserved for use by future versions of this specification.

## B4.4.18 RmiRecMpidr type

The RmiRecMpidr fieldset contains MPIDR value which identifies a REC.

The RmiRecMpidr fieldset is a concrete type.

The width of the RmiRecMpidr fieldset is 64 bits.

See also:

- A2.3.3 REC index and MPIDR value
- B4.3.12 RMI\_REC\_CREATE command

The fields of the RmiRecMpidr fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRecMpidr fieldset are shown in the following table.

| Name   | Bits   | Description      | Value   |
|--------|--------|------------------|---------|
| aff0   | 3:0    | Affinity level 0 | Bits4   |
|        | 7:4    | Reserved         | SBZ     |
| aff1   | 15:8   | Affinity level 1 | Bits8   |
| aff2   | 23:16  | Affinity level 2 | Bits8   |
| aff3   | 31:24  | Affinity level 3 | Bits8   |
|        | 63:32  | Reserved         | SBZ     |

## B4.4.19 RmiRecParams type

The RmiRecParams structure contains parameters provided by the Host during REC creation.

The RmiRecParams structure is a concrete type.

The width of the RmiRecParams structure is 4096 ( 0x1000 ) bytes.

The number of valid entries in the aux array is determined by the return value from the RMI\_REC\_AUX\_COUNT command.

## See also:

- B4.3.11 RMI\_REC\_AUX\_COUNT command

The members of the RmiRecParams structure are shown in the following table.

| Name    | Byte offset   | Type              | Description                     |
|---------|---------------|-------------------|---------------------------------|
| flags   | 0x0           | RmiRecCreateFlags | Flags                           |
| mpidr   | 0x100         | RmiRecMpidr       | MPIDR of the REC                |
| pc      | 0x200         | Bits64            | Program counter                 |
| gprs[0] | 0x300         | Bits64            | General-purpose registers       |
| gprs[1] | 0x308         | Bits64            | General-purpose registers       |
| gprs[2] | 0x310         | Bits64            | General-purpose registers       |
| gprs[3] | 0x318         | Bits64            | General-purpose registers       |
| gprs[4] | 0x320         | Bits64            | General-purpose registers       |
| gprs[5] | 0x328         | Bits64            | General-purpose registers       |
| gprs[6] | 0x330         | Bits64            | General-purpose registers       |
| gprs[7] | 0x338         | Bits64            | General-purpose registers       |
| num_aux | 0x800         | UInt64            | Number of auxiliary Granules    |
| aux[0]  | 0x808         | Address           | Addresses of auxiliary Granules |
| aux[1]  | 0x810         | Address           | Addresses of auxiliary Granules |
| aux[2]  | 0x818         | Address           | Addresses of auxiliary Granules |
| aux[3]  | 0x820         | Address           | Addresses of auxiliary Granules |
| aux[4]  | 0x828         | Address           | Addresses of auxiliary Granules |
| aux[5]  | 0x830         | Address           | Addresses of auxiliary Granules |
| aux[6]  | 0x838         | Address           | Addresses of auxiliary Granules |
| aux[7]  | 0x840         | Address           | Addresses of auxiliary Granules |
| aux[8]  | 0x848         | Address           | Addresses of auxiliary Granules |
| aux[9]  | 0x850         | Address           | Addresses of auxiliary Granules |
| aux[10] | 0x858         | Address           | Addresses of auxiliary Granules |
| aux[11] | 0x860         | Address           | Addresses of auxiliary Granules |
| aux[12] | 0x868         | Address           | Addresses of auxiliary Granules |
| aux[13] | 0x870         | Address           | Addresses of auxiliary Granules |
| aux[14] | 0x878         | Address           | Addresses of auxiliary Granules |
| aux[15] | 0x880         | Address           | Addresses of auxiliary Granules |

Unused bits of the RmiRecParams structure SBZ.

## B4.4.20 RmiRecRun type

The RmiRecRun structure contains fields used to share information between RMM and Host during REC entry and REC exit.

The RmiRecRun structure is a concrete type.

The width of the RmiRecRun structure is 4096 ( 0x1000 ) bytes.

See also:

- A4.2.1 RmiRecEnter object
- A4.3.1 RmiRecExit object
- B4.3.14 RMI\_REC\_ENTER command

The members of the RmiRecRun structure are shown in the following table.

| Name   | Byte offset   | Type        | Description       |
|--------|---------------|-------------|-------------------|
| enter  | 0x0           | RmiRecEnter | Entry information |
| exit   | 0x800         | RmiRecExit  | Exit information  |

## B4.4.21 RmiRecRunnable type

The RmiRecRunnable enumeration represents whether a REC is eligible for execution.

The RmiRecRunnable enumeration is a concrete type.

The width of the RmiRecRunnable enumeration is 1 bits.

The values of the RmiRecRunnable enumeration are shown in the following table.

|   Encoding | Name             | Description                 |
|------------|------------------|-----------------------------|
|          0 | RMI_NOT_RUNNABLE | Not eligible for execution. |
|          1 | RMI_RUNNABLE     | Eligible for execution.     |

## B4.4.22 RmiResponse type

The RmiResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RmiResponse enumeration is a concrete type.

The width of the RmiResponse enumeration is 1 bits.

The values of the RmiResponse enumeration are shown in the following table.

|   Encoding | Name       | Description                      |
|------------|------------|----------------------------------|
|          0 | RMI_ACCEPT | Host accepted the Realm request. |
|          1 | RMI_REJECT | Host rejected the Realm request. |

## B4.4.23 RmiRipas type

The RmiRipas enumeration represents realm IPA state.

The RmiRipas enumeration is a concrete type.

The width of the RmiRipas enumeration is 8 bits.

The values of the RmiRipas enumeration are shown in the following table.

|   Encoding | Name          | Description                                                                    |
|------------|---------------|--------------------------------------------------------------------------------|
|          0 | RMI_EMPTY     | Address where no Realm resources are mapped.                                   |
|          1 | RMI_RAM       | Address where private code or data owned by the Realm is mapped.               |
|          2 | RMI_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |

Unused encodings for the RmiRipas enumeration are reserved for use by future versions of this specification.

## B4.4.24 RmiRttEntryState type

The RmiRttEntryState enumeration represents the state of an RTTE.

The RmiRttEntryState enumeration is a concrete type.

The width of the RmiRttEntryState enumeration is 8 bits.

The values of the RmiRttEntryState enumeration are shown in the following table.

|   Encoding | Name           | Description                                                                                                                                                           |
|------------|----------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          0 | RMI_UNASSIGNED | This RTTE is not associated with any Granule.                                                                                                                         |
|          1 | RMI_ASSIGNED   | The output address of this RTTE points to: • a DATA Granule, if the input address is a Protected IPA, or • an NS Granule, if the input address is an Unprotected IPA. |
|          2 | RMI_TABLE      | The output address of this RTTE points to the next-level RTT.                                                                                                         |

Unused encodings for the RmiRttEntryState enumeration are reserved for use by future versions of this specification.

## B4.4.25 RmiStatusCode type

The RmiStatusCode enumeration represents the status of an RMI operation.

The RmiStatusCode enumeration is a concrete type.

The width of the RmiStatusCode enumeration is 8 bits.

See also:

- B1.3 Command registers
- B1.5 Command context values

The values of the RmiStatusCode enumeration are shown in the following table.

|   Encoding | Name            | Description                                                                                              |
|------------|-----------------|----------------------------------------------------------------------------------------------------------|
|          0 | RMI_SUCCESS     | Command completed successfully                                                                           |
|          1 | RMI_ERROR_INPUT | The value of a command input value caused the command to fail                                            |
|          2 | RMI_ERROR_REALM | An attribute of a Realm does not match the expected value                                                |
|          3 | RMI_ERROR_REC   | An attribute of a REC does not match the expected value                                                  |
|          4 | RMI_ERROR_RTT   | An RTT walk terminated before reaching the target RTT level, or reached an RTTE with an unexpected value |

Unused encodings for the RmiStatusCode enumeration are reserved for use by future versions of this specification.

## B4.4.26 RmiTrap type

The RmiTrap enumeration represents whether a trap is enabled.

The RmiTrap enumeration is a concrete type.

The width of the RmiTrap enumeration is 1 bits.

The values of the RmiTrap enumeration are shown in the following table.

|   Encoding | Name        | Description       |
|------------|-------------|-------------------|
|          0 | RMI_NO_TRAP | Trap is disabled. |
|          1 | RMI_TRAP    | Trap is enabled.  |