## Chapter C2

## RMM types

This section describes types which are used to model the abstract state of the RMM.

## C2.1 RmmAddrRange type

The RmmAddrRange structure contains address range.


The RmmAddrRange structure is an abstract type.

The members of the RmmAddrRange structure are shown in the following table.

| Name   | Type    | Description                       |
|--------|---------|-----------------------------------|
| base   | Address | Base of address range (inclusive) |
| top    | Address | Top of address range (exclusive)  |

The RmmAddrRange structure is used in the following types:

- RmmVdev
- RmmCmem
- RmmPdevStream

## C2.2 RmmBoolean type

The RmmBoolean enumeration represents whether a feature is enabled.

The RmmBoolean enumeration is an abstract type.

The values of the RmmBoolean enumeration are shown in the following table.

| Name      | Description   |
|-----------|---------------|
| RMM_FALSE | False         |
| RMM_TRUE  | True          |

The RmmBoolean enumeration is used in the following types:

- RmmRttWalkNotAligned
- RmmVdevAddrResult
- RmmGlobalDynamic
- RmmRec
- RmmRttS2APDirect
- RmmPdevStreamResult
- RmmCmemPdev
- RmmPsmmu

## C2.3 RmmCmem type

The RmmCmem structure contains attributes of a CMEM.

The RmmCmem structure is an abstract type.

The members of the RmmCmem structure are shown in the following table.

| Name       | Type           | Description                                     |
|------------|----------------|-------------------------------------------------|
| chbcr_addr | Bits64         | Address of CHBCR register in the Host Bridge    |
| hb_hdm_id  | Bits8          | Host Bridge HDMdecider identifier               |
| addr_range | RmmAddrRange   | CMEMwindow. Base and size are aligned to 256MB. |
| ilv_gran   | UInt64         | Interleave granularity in bytes                 |
| ilv_ways   | UInt64         | Number of interleave ways                       |
| state      | RmmCmemState   | CMEMstate                                       |
| pdev       | RmmCmemPdev[8] | Bound PDEV objects                              |


## C2.4 RmmCmemPdev type

The RmmCmemPdev structure contains represents a binding between a CMEM and a PDEV.

The RmmCmemPdev structure is an abstract type.

The members of the RmmCmemPdev structure are shown in the following table.

| Name       | Type       | Description                               |
|------------|------------|-------------------------------------------|
| valid      | RmmBoolean | TRUE if this binding has been established |
| pdev_addr  | Address    | Address of PDEV                           |
| dev_hdm_id | Bits8      | Device HDMdecoder identifier              |

The RmmCmemPdev structure is used in the following types:

- RmmCmem

## C2.5 RmmCmemState type

The RmmCmemState enumeration represents the state of a CMEM.

The RmmCmemState enumeration is an abstract type.

The values of the RmmCmemState enumeration are shown in the following table.

| Name         | Description                                                   |
|--------------|---------------------------------------------------------------|
| CMEM_STARTED | Device is ready to provide coherent memory to the system.     |
| CMEM_STOPPED | Device is not ready to provide coherent memory to the system. |

The RmmCmemState enumeration is used in the following types:

- RmmCmem

## C2.6 RmmDataFlags type

The RmmDataFlags fieldset contains flags provided by the Host during DATA Granule creation.


The RmmDataFlags fieldset is a concrete type.

The width of the RmmDataFlags fieldset is 64 bits.

The fields of the RmmDataFlags fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmmDataFlags fieldset are shown in the following table.

| Name    | Bits   | Description                              | Value                 |
|---------|--------|------------------------------------------|-----------------------|
| measure | 0      | Whether to measure DATA Granule contents | RmmDataMeasureContent |
|         | 63:1   | Reserved                                 | SBZ                   |

The RmmDataFlags fieldset is used in the following types:

- RmmMeasurementDescriptorData

## C2.7 RmmDataMeasureContent type

The RmmDataMeasureContent enumeration represents whether to measure DATA Granule contents.

The RmmDataMeasureContent enumeration is a concrete type.

The width of the RmmDataMeasureContent enumeration is 1 bits.

The values of the RmmDataMeasureContent enumeration are shown in the following table.

|   Encoding | Name               | Description                           |
|------------|--------------------|---------------------------------------|
|          0 | NO_MEASURE_CONTENT | Do not measure DATA Granule contents. |
|          1 | MEASURE_CONTENT    | Measure DATA Granule contents.        |

The RmmDataMeasureContent enumeration is used in the following types:

- RmmDataFlags

## C2.8 RmmDevCommState type

The RmmDevCommState enumeration represents the state of communication between an RMM device object and a device.


The RmmDevCommState enumeration is an abstract type.

The values of the RmmDevCommState enumeration are shown in the following table.

| Name             | Description                                                                                                                                                                                                                                                 |
|------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DEV_COMM_ACTIVE  | The RMMhas initiated a device transaction. One or more device requests associated with this device transaction have been sent from the RMMto the device. The RMMhas not received all the expected device responses associated with this device transaction. |
| DEV_COMM_ERROR   | The RMMencountered an error during communication with the device.                                                                                                                                                                                           |
| DEV_COMM_IDLE    | The RMMis not communicating with the device.                                                                                                                                                                                                                |
| DEV_COMM_PENDING | The RMMhas a device request which is ready to be sent to the device.                                                                                                                                                                                        |

The RmmDevCommState enumeration is used in the following types:

- RmmVdev

- RmmPdev

## C2.9 RmmDevMemCoherent type

The RmmDevMemCoherent enumeration represents whether a device memory location is within the system coherent memory space.

The RmmDevMemCoherent enumeration is an abstract type.

The values of the RmmDevMemCoherent enumeration are shown in the following table.

| Name                 | Description                                                             |
|----------------------|-------------------------------------------------------------------------|
| DEV_MEM_COHERENT     | A device memory location is within the system coherent memory space     |
| DEV_MEM_NON_COHERENT | A device memory location is not within the system coherent memory space |

The RmmDevMemCoherent enumeration is used in the following types:

- RmmDevMemFlags

## C2.10 RmmDevMemFlags type

The RmmDevMemFlags structure contains flags which describe properties of a device memory mapping.

The RmmDevMemFlags structure is an abstract type.

The members of the RmmDevMemFlags structure are shown in the following table.

| Name   | Type              | Description                                                                                         |
|--------|-------------------|-----------------------------------------------------------------------------------------------------|
| coh    | RmmDevMemCoherent | Whether the output address of the device memory mapping is within the system coherent memory space. |
| order  | RmmDevMemOrdering | Ordering properties of the device memory location.                                                  |


The RmmDevMemFlags structure is used in the following types:

- RmmRec

## C2.11 RmmDevMemOrdering type

The RmmDevMemOrdering enumeration represents ordering properties of a device memory location.

The RmmDevMemOrdering enumeration is an abstract type.

The values of the RmmDevMemOrdering enumeration are shown in the following table.

| Name                  | Description                                                     |
|-----------------------|-----------------------------------------------------------------|
| DEV_MEM_LIMITED_ORDER | A device memory location is within a Limited Order Region (LOR) |

| Name                                                                                         | Description                                                                                  |
|----------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------|
| DEV_MEM_NOT_LIMITED_ORDERA device memory location is not within a Limited Order Region (LOR) | DEV_MEM_NOT_LIMITED_ORDERA device memory location is not within a Limited Order Region (LOR) |

The RmmDevMemOrdering enumeration is used in the following types:

- RmmDevMemFlags

## C2.12 RmmDptL0 type

The RmmDptL0 structure contains attributes of the Level 0 DPT.

The RmmDptL0 structure is an abstract type.

The members of the RmmDptL0 structure are shown in the following table.

| Name   | Type          | Description        |
|--------|---------------|--------------------|
| state  | RmmDptL0State | State of the table |

## C2.13 RmmDptL0Entry type

The RmmDptL0Entry structure contains attributes of a Level 0 DPT entry.

The RmmDptL0Entry structure is an abstract type.

The members of the RmmDptL0Entry structure are shown in the following table.

| Name   | Type               | Description        |
|--------|--------------------|--------------------|
| state  | RmmDptL0EntryState | State of the entry |


## C2.14 RmmDptL0EntryState type

The RmmDptL0EntryState enumeration represents state of a Level 0 DPT entry.

The RmmDptL0EntryState enumeration is an abstract type.

The values of the RmmDptL0EntryState enumeration are shown in the following table.

| Name               | Description                         |
|--------------------|-------------------------------------|
| DPT_L0_ENTRY_BLOCK | Level 0 DPT entry is a block entry. |
| DPT_L0_ENTRY_TABLE | Level 0 DPT entry is a table entry. |

The RmmDptL0EntryState enumeration is used in the following types:

- RmmDptL0Entry

## C2.15 RmmDptL0State type

The RmmDptL0State enumeration represents state of the Level 0 DPT.

The RmmDptL0State enumeration is an abstract type.

The values of the RmmDptL0State enumeration are shown in the following table.

| Name           | Description             |
|----------------|-------------------------|
| DPT_L0_INVALID | Level 0 DPT is invalid. |
| DPT_L0_VALID   | Level 0 DPT is valid.   |

The RmmDptL0State enumeration is used in the following types:

- RmmDptL0

## C2.16 RmmFeature type

The RmmFeature enumeration represents whether a feature is enabled.

The RmmFeature enumeration is an abstract type.

See also:

- Chapter A3 Feature discovery and configuration

The values of the RmmFeature enumeration are shown in the following table.

| Name          | Description                                                                               |
|---------------|-------------------------------------------------------------------------------------------|
| FEATURE_FALSE | • During discovery: Feature is not supported. • During selection: Feature is not enabled. |
| FEATURE_TRUE  | • During discovery: Feature is supported. • During selection: Feature is enabled.         |


The RmmFeature enumeration is used in the following types:

- RmmVdev
- RmmRealm
- RmmPdev
- RmmGlobalStatic
- RmmPsmmu

## C2.17 RmmGlobal type

The RmmGlobal structure contains global attributes of the RMM implementation.

The RmmGlobal structure is an abstract type.

The members of the RmmGlobal structure are shown in the following table.

| Name    | Type             | Description        |
|---------|------------------|--------------------|
| static  | RmmGlobalStatic  | Static attributes  |
| dynamic | RmmGlobalDynamic | Dynamic attributes |

## C2.18 RmmGlobalDynamic type

The RmmGlobalDynamic structure contains global dynamic attributes of the RMM implementation.

The RmmGlobalDynamic structure is an abstract type.

The members of the RmmGlobalDynamic structure are shown in the following table.

| Name                                                                         | Type                                            | Description                                                                                                                                                                                                                                                                                                              |
|------------------------------------------------------------------------------|-------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| state rmi_granule_size tracking_region_size num_tracked num_realms pat_valid | RmmState UInt64 UInt64 UInt64 UInt64 RmmBoolean | Lifecycle state Current RMI Granule size Current tracking region size Number of tracking regions which have been transitioned from untracked to tracked Number of Realms which have been created Whether the Platform Attestation Token reflects the current set of comprehensive trust devices attached to the platform |

The RmmGlobalDynamic structure is used in the following types:

- RmmGlobal


## C2.19 RmmGlobalStatic type

The RmmGlobalStatic structure contains global static attributes of the RMM implementation.

The RmmGlobalStatic structure is an abstract type.

See also:

- Chapter A3 Feature discovery and configuration

The members of the RmmGlobalStatic structure are shown in the following table.

| Name          | Type   | Description                                           |
|---------------|--------|-------------------------------------------------------|
| pasz          | UInt64 | Physical address size in bytes                        |
| dptps         | UInt64 | Size of the address space covered by the DPT in bytes |
| l0dptsz       | UInt64 | Level 0 DPT size in bytes                             |
| l0gptsz       | UInt64 | Level 0 GPT size in bytes                             |
| max_ipa_width | UInt64 | Maximum IPA width                                     |

| Name                            | Type                            | Description                                                              |
|---------------------------------|---------------------------------|--------------------------------------------------------------------------|
| feat_lpa2                       | RmmFeature                      | Whether LPA2 is supported                                                |
| feat_sve                        | RmmFeature                      | Whether SVE is supported                                                 |
| max_sve_vl                      | UInt64                          | Maximum SVE vector length                                                |
| num_bps                         | UInt64                          | Number of breakpoints available                                          |
| num_wps                         | UInt64                          | Number of watchpoints available                                          |
| feat_pmu                        | RmmFeature                      | Number of watchpoints available                                          |
| pmu_num_ctrs                    | UInt64                          | Number of PMU counters available                                         |
| feat_sha_256                    | RmmFeature                      | Whether SHA-256 is supported                                             |
| feat_sha_384                    | RmmFeature                      | Whether SHA-384 is supported                                             |
| feat_sha_512                    | RmmFeature                      | Whether SHA-512 is supported                                             |
| feat_da                         | RmmFeature                      | Whether Realm device assignment is supported                             |
| feat_da_coh                     | RmmFeature                      | Whether coherent device assignment is supported                          |
| feat_p2p                        | RmmFeature                      | Whether peer-to-peer device communication is supported                   |
| feat_vsmmu                      | RmmFeature                      | Whether virtual SMMUis supported                                         |
| feat_ats                        | RmmFeature                      | Whether ATS is supported                                                 |
| max_num_aux_planes UInt64       | max_num_aux_planes UInt64       | Maximum number of auxiliary Planes                                       |
| rtt_plane                       | RmmRttPlaneFeature              | RTT usage models supported for multi-Plane Realms                        |
| rtt_s2ap_indirect               | RmmFeature                       Whether S2AP indirect encoding is supported for multi-Plane Realms |
| mec_count                       | UInt64                          | Number of MECs                                                           |
| max_recs_order                  | UInt64                          | Order of the maximum number of RECs which can be created per Realm       |
| max_vdevs_order                 | UInt64                          | Order of the maximum number of VDEVs which can be created per PDEV       |
| rmi_granule_size_4kb RmmFeature | rmi_granule_size_4kb RmmFeature | Whether 4KB RMI Granule size is supported                                |
| rmi_granule_size_16k RmmFeature | rmi_granule_size_16k RmmFeature | Whether 16KB RMI Granule size is supported                               |
| rmi_granule_size_64k RmmFeature | rmi_granule_size_64k RmmFeature | Whether 64KB RMI Granule size is supported                               |
| feat_cmem_cxl                   | RmmFeature                      | Whether CXL type-3 coherent memory devices are supported                 |
| max_cmem                        | UInt8                           | Maximum number of CMEMdevices                                            |
| feat_non_tee_stream RmmFeature  | feat_non_tee_stream RmmFeature  | Whether NON_TEE PDEV stream type is supported                            |
| feat_vdev_krou                  | RmmFeature                      | Whether stream key refresh is required on VDEV unlock                    |
| feat_cmem_tse_req RmmFeature    | feat_cmem_tse_req RmmFeature    | Whether Target-Side Encryption is required forCMEM devices               |

The RmmGlobalStatic structure is used in the following types:

- RmmGlobal

## C2.20 RmmGptL0Entry type

The RmmGptL0Entry structure contains attributes of a Level 0 GPT entry.

The RmmGptL0Entry structure is an abstract type.

The members of the RmmGptL0Entry structure are shown in the following table.

| Name   | Type               | Description        |
|--------|--------------------|--------------------|
| state  | RmmGptL0EntryState | State of the entry |

## C2.21 RmmGptL0EntryState type

The RmmGptL0EntryState enumeration represents state of a Level 0 GPT entry.

The RmmGptL0EntryState enumeration is an abstract type.

The values of the RmmGptL0EntryState enumeration are shown in the following table.

| Name                      | Description                                    |
|---------------------------|------------------------------------------------|
| GPT_L0_ENTRY_BLOCK        | Level 0 GPT entry is a block entry.            |
| GPT_L0_ENTRY_INTERMEDIATE | Level 0 GPT entry is is an intermediate state. |
| GPT_L0_ENTRY_TABLE        | Level 0 GPT entry is a table entry.            |

The RmmGptL0EntryState enumeration is used in the following types:

- RmmGptL0Entry

## C2.22 RmmGranule type

The RmmGranule structure contains attributes of a Granule.

The RmmGranule structure is an abstract type.

The members of the RmmGranule structure are shown in the following table.

| Name   | Type            | Description     |
|--------|-----------------|-----------------|
| state  | RmmGranuleState | Lifecycle state |

## C2.23 RmmGranuleState type

The RmmGranuleState enumeration represents the state of a granule.


The RmmGranuleState enumeration is an abstract type.

The values of the RmmGranuleState enumeration are shown in the following table.

| Name             | Description                               |
|------------------|-------------------------------------------|
| GRAN_CMEM        | Coherent memory device object.            |
| GRAN_DATA        | Realm code or data.                       |
| GRAN_DELEGATED   | Delegated for use by the RMM.             |
| GRAN_DEV         | Device memory, mapped into a Realm.       |
| GRAN_INTERNAL    | Used for IMPLEMENTATION DEFINED purposes. |
| GRAN_PDEV        | Physical device object.                   |
| GRAN_RD          | Realm Descriptor object                   |
| GRAN_REC         | Realm Execution Context object.           |
| GRAN_RTT         | Realm Translation Table.                  |
| GRAN_UNDELEGATED | Not delegated for use by the RMM.         |
| GRAN_VDEV        | Virtual device object.                    |
| GRAN_VSMMU       | Virtual SMMUobject.                       |

The RmmGranuleState enumeration is used in the following types:

- RmmGranule

## C2.24 RmmHashAlgorithm type

The RmmHashAlgorithm enumeration represents hash algorithm.

The RmmHashAlgorithm enumeration is an abstract type.


The values of the RmmHashAlgorithm enumeration are shown in the following table.

| Name         | Description                                |
|--------------|--------------------------------------------|
| HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [25]) |
| HASH_SHA_384 | SHA-384 ( Secure Hash Standard (SHS) [25]) |
| HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [25]) |

The RmmHashAlgorithm enumeration is used in the following types:

- RmmPdev
- RmmRealm

## C2.25 RmmHipas type

The RmmHipas enumeration represents host IPA state.

The RmmHipas enumeration is an abstract type.

The values of the RmmHipas enumeration are shown in the following table.

| Name              | Description                                                     |
|-------------------|-----------------------------------------------------------------|
| HIPAS_ARCH_DEV    | Protected IPA which is associated with an architectural device. |
| HIPAS_DATA        | Protected IPA which is associated with a DATA Granule.          |
| HIPAS_MAPPED_NS   | Unprotected IPA which is associated with a physical Granule.    |
| HIPAS_NARCH_DEV   | Protected IPA which is associated with a GRAN_DEV Granule.      |
| HIPAS_UNMAPPED_NS | Unprotected IPA which is not associated with any Granule.       |
| HIPAS_VOID        | Protected IPA which is not associated with any Granule.         |

## C2.26 RmmLfaPolicy type

The RmmLfaPolicy enumeration represents a Live Firmware Activation policy.

The RmmLfaPolicy enumeration is an abstract type.

The values of the RmmLfaPolicy enumeration are shown in the following table.

| Name         | Description           |
|--------------|-----------------------|
| LFA_ALLOW    | LFA is permitted.     |
| LFA_DISALLOW | LFA is not permitted. |

The RmmLfaPolicy enumeration is used in the following types:

- RmmRealm


## C2.27 RmmMeasurementDescriptorData type

The RmmMeasurementDescriptorData structure contains data structure used to calculate the contribution to the RIM of a DATA Granule.

The RmmMeasurementDescriptorData structure is a concrete type.

The width of the RmmMeasurementDescriptorData structure is 256 ( 0x100 ) bytes.

See also:

- B4.5.66.4 RMI\_RTT\_DATA\_MAP\_INIT extension of RIM

The members of the RmmMeasurementDescriptorData structure are shown in the following table.

| Name      | Byte offset   | Type                | Description                            |
|-----------|---------------|---------------------|----------------------------------------|
| desc_type | 0x0           | Bits8               | Measurement descriptor type, value 0x0 |
| len       | 0x8           | UInt64              | Length of this data structure in bytes |
| rim       | 0x10          | RmmRealmMeasurement | Current RIM value                      |

| Name    | Byte offset   | Type                | Description                                                                                      |
|---------|---------------|---------------------|--------------------------------------------------------------------------------------------------|
| ipa     | 0x50          | Address             | IPA at which the DATA Granule is mapped in the Realm                                             |
| flags   | 0x58          | RmmDataFlags        | Flags provided by Host                                                                           |
| content | 0x60          | RmmRealmMeasurement | Hash of contents of DATA Granule, or zero if flags indicate DATA Granule contents are unmeasured |

Unused bits of the RmmMeasurementDescriptorData structure MBZ.

## C2.28 RmmMeasurementDescriptorRec type

The RmmMeasurementDescriptorRec structure contains data structure used to calculate the contribution to the RIM of a REC.

The RmmMeasurementDescriptorRec structure is a concrete type.

The width of the RmmMeasurementDescriptorRec structure is 256 ( 0x100 ) bytes.

See also:

- B4.5.49.4 RMI\_REC\_CREATE extension of RIM

The members of the RmmMeasurementDescriptorRec structure are shown in the following table.

| Name      | Byte offset   | Type                | Description                                                                                        |
|-----------|---------------|---------------------|----------------------------------------------------------------------------------------------------|
| desc_type | 0x0           | Bits8               | Measurement descriptor type, value 0x1                                                             |
| len       | 0x8           | UInt64              | Length of this data structure in bytes                                                             |
| rim       | 0x10          | RmmRealmMeasurement | Current RIM value                                                                                  |
| content   | 0x50          | RmmRealmMeasurement | Hash of an RMI Granule which contains REC parameters data structure. Unused bytes are zero-filled. |


Unused bits of the RmmMeasurementDescriptorRec structure MBZ.

## C2.29 RmmMecPolicy type

The RmmMecPolicy enumeration represents a MEC policy.

The RmmMecPolicy enumeration is an abstract type.

The values of the RmmMecPolicy enumeration are shown in the following table.

| Name               | Description                                                                                                   |
|--------------------|---------------------------------------------------------------------------------------------------------------|
| MEC_POLICY_PRIVATE | The MEC protects memory owned by a single Realm. A MEC with this policy may be referred to as a Private MEC . |

| Name              | Description                                                                                                   |
|-------------------|---------------------------------------------------------------------------------------------------------------|
| MEC_POLICY_SHARED | The MEC protects memory owned by multiple Realms. A MEC with this policy may be referred to as a Shared MEC . |

The RmmMecPolicy enumeration is used in the following types:

- RmmRealm

## C2.30 RmmMemCategory type

The RmmMemCategory enumeration represents memory category.

The RmmMemCategory enumeration is an abstract type.

The values of the RmmMemCategory enumeration are shown in the following table.

| Name                                           | Description                                    |
|------------------------------------------------|------------------------------------------------|
| MEM_CATEGORY_CONVENTIONAL Conventional memory. | MEM_CATEGORY_CONVENTIONAL Conventional memory. |
| MEM_CATEGORY_DEV_COH                           | Device coherent memory.                        |
| MEM_CATEGORY_DEV_NCOH                          | Device non-coherent memory.                    |

The RmmMemCategory enumeration is used in the following types:

- RmmTrackingRegion

## C2.31 RmmMemPermLocked type

The RmmMemPermLocked enumeration represents whether a memory permission value is locked.


The RmmMemPermLocked enumeration is an abstract type.

The values of the RmmMemPermLocked enumeration are shown in the following table.

| Name              | Description                         |
|-------------------|-------------------------------------|
| MEM_PERM_LOCKED   | Memory permission value is locked   |
| MEM_PERM_UNLOCKED | Memory permission value is unlocked |

The RmmMemPermLocked enumeration is used in the following types:

- RmmRealm

## C2.32 RmmMemPerms type

The RmmMemPerms structure contains memory permissions.

The RmmMemPerms structure is an abstract type.

The members of the RmmMemPerms structure are shown in the following table.

| Name   | Type       | Description                                                                                         |
|--------|------------|-----------------------------------------------------------------------------------------------------|
| values | Bits64[16] | Mapping from memory permission index to memory permission label Values use architectural encodings. |

The RmmMemPerms structure is used in the following types:

- RmmRealm

## C2.33 RmmOpCanCancel type

The RmmOpCanCancel enumeration represents whether a stateful operation can be cancelled.

The RmmOpCanCancel enumeration is an abstract type.

The values of the RmmOpCanCancel enumeration are shown in the following table.

| Name                 | Description                    |
|----------------------|--------------------------------|
| RMM_OP_CANNOT_CANCEL | Operation cannot be cancelled. |
| RMM_OP_CAN_CANCEL    | Operation can be cancelled.    |

## C2.34 RmmPdev type

The RmmPdev structure contains attributes of a PDEV.

The RmmPdev structure is an abstract type.

The members of the RmmPdev structure are shown in the following table.

| Name        | Type             | Description                                                             |
|-------------|------------------|-------------------------------------------------------------------------|
| category    | RmmPdevCategory  | Device category                                                         |
| pdev_id     | Bits64           | Device identifier                                                       |
| routing_id  | Bits64           | Routing identifier                                                      |
| rid_base    | Bits16           | Base of requester ID range (inclusive). The value is in PCI BDF format. |
| rid_top     | Bits16           | Top of requester ID range (exclusive). The value is in PCI BDF format.  |
| spdm        | RmmPdevSpdm      | Whether communication with the device uses SPDM                         |
| signed_meas | RmmFeature       | Whether device supports signed measurements                             |
| id_index    | UInt64           | Device identity index                                                   |
| hash_algo   | RmmHashAlgorithm | Algorithm used to generate device digests                               |
| state       | RmmPdevState     | Lifecycle state                                                         |
| op          | RmmPdevOperation | Operation performed on this PDEV                                        |


| Name                         | Type                         | Description                                                        |
|------------------------------|------------------------------|--------------------------------------------------------------------|
| comm_state                   | RmmDevCommState              | Device communication state                                         |
| max_num_vdevs                | UInt64                       | Maximum number of VDEVs which can be associated with this PDEV     |
| num_vdevs                    | UInt64                       | Number of VDEVs associated with this PDEV                          |
| p2p_enabled                  | RmmFeature                   | TRUE if this device can be associated with a Direct P2P IDE stream |
| negotiation_data_dig Bits512 | negotiation_data_dig Bits512 | Protocol negotiation data digest                                   |
| feat_tse                     | RmmFeature                   | Whether this device supports Target-Side Encryption                |
| cmem_count                   | UInt64                       | Number of CMEMobjects with which this PDEV is associated           |

## C2.35 RmmPdevCategory type

The RmmPdevCategory enumeration represents PDEV category.

The RmmPdevCategory enumeration is an abstract type.

The values of the RmmPdevCategory enumeration are shown in the following table.

| Name                         | Description                          |
|------------------------------|--------------------------------------|
| PDEV_ENDPOINT_ACCEL_OFF_CHIP | Off-chip accelerator endpoint device |
| PDEV_ENDPOINT_ACCEL_ON_CHIP  | On-chip accelerator endpoint device  |
| PDEV_ENDPOINT_CMEM           | Coherent memory endpoint device      |
| PDEV_ROOT_PORT               | Root Port                            |


The RmmPdevCategory enumeration is used in the following types:

- RmmPdev

## C2.36 RmmPdevOperation type

The RmmPdevOperation enumeration represents operation performed on a PDEV.

The RmmPdevOperation enumeration is an abstract type.

The values of the RmmPdevOperation enumeration are shown in the following table.

| Name               | Description                          |
|--------------------|--------------------------------------|
| PDEV_OP_CONNECT    | Request connection of a PDEV stream. |
| PDEV_OP_DISCONNECT | Request connection of a PDEV stream. |
| PDEV_OP_KEY_PURGE  | Request key flush of a PDEV stream.  |

| Name                                                                    | Description                                                             |
|-------------------------------------------------------------------------|-------------------------------------------------------------------------|
| PDEV_OP_KEY_REFRESH                                                     | Request key refresh of a PDEV stream.                                   |
| PDEV_OP_MEC_REFRESH                                                     | Request a MEC refresh.                                                  |
| PDEV_OP_NONE                                                            | No operation.                                                           |
| PDEV_OP_P2P_CONNECT                                                     | Request connection of a P2P stream.                                     |
| PDEV_OP_P2P_DISCONNECT                                                  | Request disconnection of a P2P stream.                                  |
| PDEV_OP_STOP                                                            | Change state to STOPPED.                                                |
| PDEV_OP_STREAM_COMPLETE Awaiting completion of a PDEV stream operation. | PDEV_OP_STREAM_COMPLETE Awaiting completion of a PDEV stream operation. |

The RmmPdevOperation enumeration is used in the following types:

- RmmPdev

## C2.37 RmmPdevSpdm type

The RmmPdevSpdm enumeration represents whether communication with the device uses SPDM.

The RmmPdevSpdm enumeration is an abstract type.

See also:

- A9.1.2 Device properties

The values of the RmmPdevSpdm enumeration are shown in the following table.

| Name       | Description                                      |
|------------|--------------------------------------------------|
| SPDM_FALSE | Communication with the device does not use SPDM. |
| SPDM_TRUE  | Communication with the device uses SPDM.         |


The RmmPdevSpdm enumeration is used in the following types:

- RmmPdev

## C2.38 RmmPdevState type

The RmmPdevState enumeration represents the state of a PDEV.

The RmmPdevState enumeration is an abstract type.

The values of the RmmPdevState enumeration are shown in the following table.

| Name           | Description                        |
|----------------|------------------------------------|
| PDEV_ERROR     | Device has reported a fatal error. |
| PDEV_HAS_KEY   | RMMhas device public key.          |
| PDEV_NEEDS_KEY | RMMneeds device public key.        |
| PDEV_NEW       | Initial state of the device.       |

| Name         | Description                                                           |
|--------------|-----------------------------------------------------------------------|
| PDEV_READY   | Secure connection between the RMMand the device has been established. |
| PDEV_STOPPED | Secure connection between the RMMand the device has been terminated.  |

The RmmPdevState enumeration is used in the following types:

- RmmPdev

## C2.39 RmmPdevStream type

The RmmPdevStream structure contains attributes of a PDEV stream.

The RmmPdevStream structure is an abstract type.

The members of the RmmPdevStream structure are shown in the following table.

| Name           | Type                    | Description                     |
|----------------|-------------------------|---------------------------------|
| handle         | Bits64                  | Stream handle                   |
| state          | RmmPdevStreamState      | Stream state                    |
| stream_type     RmmPdevStreamType | Stream type                     |
| ide_sid        | UInt64                  | IDE stream identifier           |
| num_addr_range | UInt64                  | Number of device address ranges |
| addr_range     | RmmAddrRange[16]        | Device address range            |

The RmmPdevStream structure is used in the following types:

- RmmPdevStreamResult

## C2.40 RmmPdevStreamResult type

The RmmPdevStreamResult structure contains result of looking up a PDEV stream.

The RmmPdevStreamResult structure is an abstract type.

The members of the RmmPdevStreamResult structure are shown in the following table.

| Name   | Type          | Description                  |
|--------|---------------|------------------------------|
| valid  | RmmBoolean    | Whether the lookup succeeded |
| stream | RmmPdevStream | Stream                       |

## C2.41 RmmPdevStreamState type

The RmmPdevStreamState enumeration represents the state of a PDEV stream.

The RmmPdevStreamState enumeration is an abstract type.

The values of the RmmPdevStreamState enumeration are shown in the following table.

| Name                       | Description                                            |
|----------------------------|--------------------------------------------------------|
| PDEV_STREAM_CONNECTED      | PDEV_STREAM_CONNECTED                                  |
| PDEV_STREAM_CONNECTING     | Stream is connected.                                   |
| PDEV_STREAM_DISCONNECTED   | Stream is connecting.                                  |
| PDEV_STREAM_DISCONNECTING  | Stream is not connected.                               |
| PDEV_STREAM_KEY_PURGING    | Stream is disconnecting. Stream keys are being purged. |
| PDEV_STREAM_KEY_REFRESHING | Stream keys are being refreshed.                       |

The RmmPdevStreamState enumeration is used in the following types:

- RmmPdevStream

## C2.42 RmmPdevStreamType type


The RmmPdevStreamType enumeration represents type of a PDEV stream.

The RmmPdevStreamType enumeration is an abstract type.

The values of the RmmPdevStreamType enumeration are shown in the following table.

| Name                 | Description                                                                           |
|----------------------|---------------------------------------------------------------------------------------|
| PDEV_STREAM_COH      | Coherent traffic between an upstream port and an accelerator endpoint device.         |
| PDEV_STREAM_COH_CMEM | Coherent traffic between an upstream port and a CMEMendpoint device.                  |
| PDEV_STREAM_COH_SYS  | Coherent traffic to an endpoint device which is protected by system construction.     |
| PDEV_STREAM_NCOH     | Non-coherent traffic between an upstream port and an endpoint device.                 |
| PDEV_STREAM_NCOH_P2P | Non-coherent traffic between two endpoint devices.                                    |
| PDEV_STREAM_NCOH_SYS | Non-coherent traffic to an endpoint device which is protected by system construction. |


| Name                | Description      |
|---------------------|------------------|
| PDEV_STREAM_NON_TEE | Non-TEE traffic. |

The RmmPdevStreamType enumeration is used in the following types:

- RmmPdevStream

## C2.43 RmmPsmmu type

The RmmPsmmu structure contains attributes of a PSMMU.

The RmmPsmmu structure is an abstract type.

The members of the RmmPsmmu structure are shown in the following table.

| Name        | Type             | Description                                                                          |
|-------------|------------------|--------------------------------------------------------------------------------------|
| state       | RmmPsmmuState    | State of the PSMMU                                                                   |
| sid_size    | UInt64            StreamID size in bits. This is read from the SMMU_IDR1.SIDSIZE register field. |
| feat_msi    | RmmFeature       | Whether the PSMMU supports MSI                                                       |
| feat_ats    | RmmFeature       | Whether the PSMMU supports ATS                                                       |
| feat_pri    | RmmFeature       | Whether the PSMMU supports PRI                                                       |
| msi_config  | RmmSmmuMsiConfig | MSI configuration                                                                    |
| ppr_pending | RmmBoolean       | Whether a PRI Page Request is pending on this PSMMU                                  |

## C2.44 RmmPsmmuState type

The RmmPsmmuState enumeration represents the state of a PSMMU.

The RmmPsmmuState enumeration is an abstract type.

While the state of a PSMMU is not ACTIVE, incoming transactions from Realm security state should be aborted. This can be achieved by setting SMMU\_R\_GBPA.ABORT == 1 .

See also:

- Arm System Memory Management Unit Architecture Specification [22]

The values of the RmmPsmmuState enumeration are shown in the following table.

| Name           | Description                   |
|----------------|-------------------------------|
| PSMMU_ACTIVE   | PSMMU has been activated.     |
| PSMMU_INACTIVE | PSMMU has not been activated. |

The RmmPsmmuState enumeration is used in the following types:

- RmmPsmmu

## C2.45 RmmPsmmuStEntry type

The RmmPsmmuStEntry structure contains attributes of a PSMMU Level 1 Stream Table entry.

The RmmPsmmuStEntry structure is an abstract type.

The members of the RmmPsmmuStEntry structure are shown in the following table.

| Name   | Type                 | Description        |
|--------|----------------------|--------------------|
| state  | RmmPsmmuStEntryState | State of the entry |

The RmmPsmmuStEntry structure is used in the following types:

- RmmPsmmuStWalkResult

## C2.46 RmmPsmmuStEntryState type

The RmmPsmmuStEntryState enumeration represents state of a PSMMU Stream Table entry.

The RmmPsmmuStEntryState enumeration is an abstract type.

The values of the RmmPsmmuStEntryState enumeration are shown in the following table.

| Name                                                               | Description                                                        |
|--------------------------------------------------------------------|--------------------------------------------------------------------|
| PSMMU_ST_ENTRY_INVALIDPSMMU Level 1 Stream Table entry is invalid. | PSMMU_ST_ENTRY_INVALIDPSMMU Level 1 Stream Table entry is invalid. |
| PSMMU_ST_ENTRY_TABLE PSMMU Level 1 Stream Table                    | entry is a table entry.                                            |
| PSMMU_ST_ENTRY_VALID                                               | PSMMU Level 1 Stream Table entry is valid.                         |


The RmmPsmmuStEntryState enumeration is used in the following types:

- RmmPsmmuStEntry

## C2.47 RmmPsmmuStWalkResult type

The RmmPsmmuStWalkResult structure contains result of a PSMMU Stream Table walk.

The RmmPsmmuStWalkResult structure is an abstract type.

The members of the RmmPsmmuStWalkResult structure are shown in the following table.

| Name   | Type            | Description                  |
|--------|-----------------|------------------------------|
| level  | Int8            | ST level reached by the walk |
| ste    | RmmPsmmuStEntry | STE reached by the walk      |

## C2.48 RmmReadWriteOp type

The RmmReadWriteOp enumeration represents a read or write operation.

The RmmReadWriteOp enumeration is an abstract type.

The values of the RmmReadWriteOp enumeration are shown in the following table.

| Name      | Description     |
|-----------|-----------------|
| RMM_READ  | Read operation  |
| RMM_WRITE | Write operation |

## C2.49 RmmRealm type

The RmmRealm structure contains attributes of a Realm.

The RmmRealm structure is an abstract type.

See also:

- A2.2 Realm

The members of the RmmRealm structure are shown in the following table.

| Name               | Type                         | Description                                                                                                                                                                                                         |
|--------------------|------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| feat_lpa2          | RmmFeature                   | Whether LPA2 is enabled for this Realm                                                                                                                                                                              |
| ipa_width          | UInt8                        | IPA width in bits                                                                                                                                                                                                   |
| rim                | RmmRealmMeasurement          | Realm Initial Measurement                                                                                                                                                                                           |
| rem                 RmmRealmMeasurement[4] | Realm Extensible Measurement                                                                                                                                                                                        |
| hash_algo          | RmmHashAlgorithm             | Algorithm used to compute Realm measurements                                                                                                                                                                        |
| rec_index          | UInt64                       | Index of next REC to be created                                                                                                                                                                                     |
| rtt_base           | Address[4]                   | Realm Translation Table base addresses If rtt_tree_per_plane is FEATURE_FALSE then only the first entry is valid. If rtt_tree_per_plane is FEATURE_TRUE then only the first (num_aux_planes + 1) entries are valid. |
| rtt_level_start    | Int64                        | RTT starting level                                                                                                                                                                                                  |
| rtt_num_start      | UInt64                       | Number of physically contiguous starting level RTTs                                                                                                                                                                 |
| state              | RmmRealmState                | Lifecycle state                                                                                                                                                                                                     |
| rpv                | Bits512                      | Realm Personalization Value                                                                                                                                                                                         |
| feat_da            | RmmFeature                   | Whether Realm device assignment is enabled for this Realm                                                                                                                                                           |
| feat_ats           | RmmFeature                   | Whether Address Translation Service is supported for devices assigned to the Realm                                                                                                                                  |
| ats_plane          | UInt64                       | Index of Plane whose stage 2 permissions are observed by ATS requests from devices assigned to the Realm                                                                                                            |
| rtt_tree_per_plane | RmmFeature                   | Whether this Realm has an RTT tree per Plane                                                                                                                                                                        |
| num_aux_planes     | UInt64                       | Number of auxiliary Planes                                                                                                                                                                                          |

| Name              | Type                 | Description                                                           |
|-------------------|----------------------|-----------------------------------------------------------------------|
| rtt_s2ap_encoding | RmmRttS2APEncoding   | S2AP encoding                                                         |
| overlay_perms     | RmmMemPerms[4]       | Memory overlay permissions                                            |
| overlay_locked    | RmmMemPermLocked[16] | Whether memory overlay value is locked                                |
| lfa_policy        | RmmLfaPolicy         | Live Firmware Activation policy for components within the Realm's TCB |
| mec_policy        | RmmMecPolicy         | MEC policy                                                            |
| num_recs          | UInt64               | Number of RECs owned by this Realm                                    |
| num_vdevs         | UInt64               | Number of VDEVs owned by this Realm                                   |
| num_vsmmus        | UInt64               | Number of VSMMUs owned by this Realm                                  |

## C2.50 RmmRealmMeasurement type

The RmmRealmMeasurement type is realm measurement.

The RmmRealmMeasurement type is a concrete type.

The width of the RmmRealmMeasurement type is 512 bits.

## C2.51 RmmRealmState type

The RmmRealmState enumeration represents the state of a Realm.

The RmmRealmState enumeration is an abstract type.

The values of the RmmRealmState enumeration are shown in the following table.

| Name             | Description                                             |
|------------------|---------------------------------------------------------|
| REALM_ACTIVE     | Eligible for execution.                                 |
| REALM_NEW        | Under construction. Not eligible for execution.         |
| REALM_SYSTEM_OFF | System has been turned off. Not eligible for execution. |
| REALM_ZOMBIE     | Ready for destruction. Not eligible for execution.      |


The RmmRealmState enumeration is used in the following types:

- RmmRealm

## C2.52 RmmRec type

The RmmRec structure contains attributes of a REC.

The RmmRec structure is an abstract type.

See also:

- A2.4 Realm Execution Context

The members of the RmmRec structure are shown in the following table.

| Name                            | Type                            | Description                                                                    |
|---------------------------------|---------------------------------|--------------------------------------------------------------------------------|
| owner                           | Address                         | PA of RD of Realm which owns this REC                                          |
| flags                           | RmmRecFlags                     | Flags which control REC behavior                                               |
| mpidr                           | Bits64                          | MPIDR value                                                                    |
| gic_owner                       | UInt64                          | Index of Plane which is the GIC owner                                          |
| state                           | RmmRecState                     | Lifecycle state                                                                |
| pending                         | RmmRecPending                   | Whether a REC operation is pending                                             |
| emulatable_abort                | RmmRecEmulatableAbort           | Whether the most recent exit from this REC was due to an Emulatable Data Abort |
| gprs                            | Bits64[32]                      | General-purpose register values                                                |
| pc                              | Bits64                          | Program counter value                                                          |
| sysregs                         | RmmSystemRegisters              | EL1 and EL0 system register values                                             |
| attest_state                    | RmmRecAttestState               | Attestation token generation state                                             |
| attest_challenge                | Bits512                         | Challenge for under-construction attestation token                             |
| ripas_addr                      | Address                         | Next IPA to be processed in RIPAS change                                       |
| ripas_top                       | Address                         | Top IPA of pending RIPAS change                                                |
| ripas_value                     | RmmRipas                        | RIPAS value of pending RIPAS change                                            |
| ripas_destroyed                  RmmRipasChangeDestroyed   | Whether a RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should be permitted   |
| ripas_response                  | RmmRecResponse                  | Host response to RIPAS change request                                          |
| dev_mem_addr                    | Address                         | Next IPA to be processed in VDEV mapping validation                            |
| dev_mem_top                     | Address                         | Top IPA of pending VDEV mapping validation                                     |
| dev_mem_pa                      | Address                         | PA of device memory                                                            |
| dev_mem_flags                   | RmmDevMemFlags                  | VDEV mapping validation flags                                                  |
| dev_mem_response RmmRecResponse | dev_mem_response RmmRecResponse | Host response to VDEV mapping validation request                               |
| s2ap_addr                       | Address                         | Next IPA to be processed in S2AP change                                        |
| s2ap_top                        | Address                         | Top IPA of pending S2AP change                                                 |
| s2ap_overlay_indexUInt4         | s2ap_overlay_indexUInt4         | Overlay index of pending S2AP change                                           |
| s2ap_response                   | RmmRecResponse                  | Host response to S2AP change request                                           |
| vdev_comm_pending RmmBoolean    | vdev_comm_pending RmmBoolean    | Whether a VDEV transaction should be initiated when the VDEV is provided       |
| vdev_id_1                       | Bits64                          | Virtual device ID 1                                                            |
| vdev_pa_1                       | Address                         | VDEV PA                                                                        |
| vdev_id_2                       | Bits64                          | Virtual device ID 2                                                            |
| vdev_attest_info_1              | RmmVdevAttestInfo               | Attestation information for first VDEV                                         |
| vdev_attest_info_2              | RmmVdevAttestInfo               | Attestation information for second VDEV                                        |

| Name        | Type   | Description           |
|-------------|--------|-----------------------|
| vsmmu_vsid  | Bits64 | Virtual SMMUStream ID |
| vsmmu_resp  | Bits64 | PRI response          |
| vsmmu_pasid | Bits64 | PASID                 |

## C2.53 RmmRecAttestState type

The RmmRecAttestState enumeration represents whether an attestation token generation operation is ongoing on this REC.

The RmmRecAttestState enumeration is an abstract type.

The values of the RmmRecAttestState enumeration are shown in the following table.

| Name                  | Description                                               |
|-----------------------|-----------------------------------------------------------|
| ATTEST_IN_PROGRESS    | An attestation token generation operation is in progress. |
| NO_ATTEST_IN_PROGRESS | No attestation token generation operation is in progress. |

The RmmRecAttestState enumeration is used in the following types:

- RmmRec

## C2.54 RmmRecEmulatableAbort type

The RmmRecEmulatableAbort enumeration represents whether the most recent exit from a REC was due to an Emulatable Data Abort.

The RmmRecEmulatableAbort enumeration is an abstract type.


The values of the RmmRecEmulatableAbort enumeration are shown in the following table.

| Name                 | Description                                                              |
|----------------------|--------------------------------------------------------------------------|
| EMULATABLE_ABORT     | The most recent exit from a REC was due to an Emulatable Data Abort.     |
| NOT_EMULATABLE_ABORT | The most recent exit from a REC was not due to an Emulatable Data Abort. |

The RmmRecEmulatableAbort enumeration is used in the following types:

- RmmRec

## C2.55 RmmRecFlags type

The RmmRecFlags structure contains REC flags.

The RmmRecFlags structure is an abstract type.

The members of the RmmRecFlags structure are shown in the following table.

| Name     | Type           | Description                       |
|----------|----------------|-----------------------------------|
| runnable | RmmRecRunnable | Whether the REC is elgible to run |

The RmmRecFlags structure is used in the following types:

- RmmRec

## C2.56 RmmRecPending type

The RmmRecPending enumeration represents whether a REC operation is pending.

The RmmRecPending enumeration is an abstract type.

The values of the RmmRecPending enumeration are shown in the following table.

| Name                                                                                                                                                              | Description                                                                                                                                                                                             |
|-------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| REC_PENDING_HOST_CALL REC_PENDING_NONE REC_PENDING_PSCI REC_PENDING_VDEV_COMPLETE REC_PENDING_VDEV_REQUEST REC_PENDING_VSMMU_COMMANDA REC_PENDING_VSMMU_COMPLETEA | A Host call is pending. No operation is pending. A PSCI operation is pending. A VDEV request has been completed. A VDEV request is pending. VSMMU command is pending. VSMMU command has been completed. |

The RmmRecPending enumeration is used in the following types:

- RmmRec


## C2.57 RmmRecResponse type

The RmmRecResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RmmRecResponse enumeration is an abstract type.

The values of the RmmRecResponse enumeration are shown in the following table.

| Name            | Description                      |
|-----------------|----------------------------------|
| RESPONSE_ACCEPT | Host accepted the Realm request. |
| RESPONSE_REJECT | Host rejected the Realm request. |

The RmmRecResponse enumeration is used in the following types:

- RmmRec

## C2.58 RmmRecRunnable type

The RmmRecRunnable enumeration represents whether a REC is eligible for execution.

The RmmRecRunnable enumeration is an abstract type.

The values of the RmmRecRunnable enumeration are shown in the following table.

| Name         | Description                 |
|--------------|-----------------------------|
| NOT_RUNNABLE | Not eligible for execution. |
| RUNNABLE     | Eligible for execution.     |

The RmmRecRunnable enumeration is used in the following types:

- RmmRecFlags

## C2.59 RmmRecState type

The RmmRecState enumeration represents the state of a REC.

The RmmRecState enumeration is an abstract type.

The values of the RmmRecState enumeration are shown in the following table.

| Name        | Description                   |
|-------------|-------------------------------|
| REC_READY   | REC is not currently running. |
| REC_RUNNING | REC is currently running.     |

The RmmRecState enumeration is used in the following types:

- RmmRec

## C2.60 RmmRipas type

The RmmRipas enumeration represents realm IPA state.

The RmmRipas enumeration is an abstract type.

The values of the RmmRipas enumeration are shown in the following table.

| Name            | Description                                                                    |
|-----------------|--------------------------------------------------------------------------------|
| RIPAS_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
| RIPAS_DEV       | Address where memory of an assigned Realm device is mapped.                    |
| RIPAS_EMPTY     | Address where no Realm resources are mapped.                                   |
| RIPAS_RAM       | Address where private code or data owned by the Realm is mapped.               |

The RmmRipas enumeration is used in the following types:


- RmmRec
- RmmRttEntry

## C2.61 RmmRipasChangeDestroyed type

The RmmRipasChangeDestroyed enumeration represents whether a RIPAS change from RIPAS\_DESTROYED to RIPAS\_RAM should be permitted.

The RmmRipasChangeDestroyed enumeration is an abstract type.

The values of the RmmRipasChangeDestroyed enumeration are shown in the following table.

| Name                | Description                                                               |
|---------------------|---------------------------------------------------------------------------|
| CHANGE_DESTROYED    | A RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should be permitted.     |
| NO_CHANGE_DESTROYED | A RIPAS change from RIPAS_DESTROYED to RIPAS_RAM should not be permitted. |

The RmmRipasChangeDestroyed enumeration is used in the following types:

- RmmRec

## C2.62 RmmRtt type

The RmmRtt structure contains an RTT.

The RmmRtt structure is an abstract type.

## C2.63 RmmRttEntry type

The RmmRttEntry structure contains attributes of an RTT Entry.


The RmmRttEntry structure is an abstract type.

See also:

- A5.6 Realm Translation Table

The members of the RmmRttEntry structure are shown in the following table.

| Name   | Type             | Description    |
|--------|------------------|----------------|
| addr   | Address          | Output address |
| ripas  | RmmRipas         | RIPAS          |
| state  | RmmRttEntryState | State          |

| Name          | Type               | Description                                                                                                                                                                                                                                                                                                                                                                                                                             |
|---------------|--------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| attr_prot     | RmmRttMemAttr      | Memory type and cacheability attributes for a Protected IPA This attribute and attr_unprot are aliased views of the underlying MemAttr field in the RTT descriptor. This view is valid if the RTT entry describes an address in Protected IPA space. The RMMuses stage 2 memory attributes to constrain the resultant memory type and cacheability attributes, based on the type of physical location identified by the output address. |
| attr_unprot   | Bits3              | Memory type and cacheability attributes for an Unprotected IPA This attribute and attr_prot are aliased views of the underlying MemAttr field in the RTT descriptor. This view is valid if the RTT entry describes an address in Unprotected IPA space. The Host controls memory type and cacheability attributes by setting the value of the MemAttr[2:0] field in the RTT descriptor.                                                 |
| sh            | RmmRttShareability | Shareability attributes.                                                                                                                                                                                                                                                                                                                                                                                                                |
| s2ap_direct   | RmmRttS2APDirect   | Directly-encoded S2AP This attribute is valid if the RTT entry describes an address in Unprotected IPA space and the Realm uses direct S2AP encoding.                                                                                                                                                                                                                                                                                   |
| s2ap_indirect | RmmRttS2APIndirect  Indirectly-encoded S2AP This attribute is valid if either of the following is true: • The RTT entry describes an address in Protected IPA space. • The RTT entry describes an address in Unprotected IPA space and the Realm uses indirect S2AP encoding.                                                                                                                                                                         |

The RmmRttEntry structure is used in the following types:

- RmmRttWalkResult

## C2.64 RmmRttEntryState type

The RmmRttEntryState enumeration represents the state of an RTTE.

The RmmRttEntryState enumeration is an abstract type.

The values of the RmmRttEntryState enumeration are shown in the following table.

| Name          | Description                                                                                                                                          |
|---------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| RTTE_ARCH_DEV | This RTTE is identified by a Protected IPA. The output address of this RTTE points to an RMMobject which is used to emulate an architectural device. |

| Name               | Description                                                                                                                       |
|--------------------|-----------------------------------------------------------------------------------------------------------------------------------|
| RTTE_AUX_DESTROYED | An auxiliary RTT was destroyed while a corresponding primary RTT entry was live.                                                  |
| RTTE_DATA          | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a DATA Granule.                             |
| RTTE_MAPPED_NS     | This RTTE is identified by an Unprotected IPA. The output address of this RTTE points to a Granule-aligned address within NS PAS. |
| RTTE_NARCH_DEV     | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a GRAN_DEV Granule.                         |
| RTTE_TABLE         | The output address of this RTTE points to the next-level RTT.                                                                     |
| RTTE_UNMAPPED_NS   | This RTTE is identified by an Unprotected IPA. This RTTE is not associated with any Granule.                                      |
| RTTE_VOID          | This RTTE is identified by a Protected IPA. This RTTE is not associated with any Granule.                                         |

The RmmRttEntryState enumeration is used in the following types:

- RmmRttEntry

## C2.65 RmmRttMemAttr type

The RmmRttMemAttr enumeration represents memory type and cacheability attributes.

The RmmRttMemAttr enumeration is an abstract type.

The values of the RmmRttMemAttr enumeration are shown in the following table.

| Name                  | Description                                                                        |
|-----------------------|------------------------------------------------------------------------------------|
| MEMATTR_CACHEABLE     | Memory type and cacheability attributes for a mapping to a cacheable location.     |
| MEMATTR_NON_CACHEABLE | Memory type and cacheability attributes for a mapping to a non-cacheable location. |
| MEMATTR_PASSTHROUGH   | Pass through memory type and cacheability attributes from stage 1 translation.     |


The RmmRttMemAttr enumeration is used in the following types:

- RmmRttEntry

## C2.66 RmmRttPlaneFeature type

The RmmRttPlaneFeature enumeration represents RTT usage models supported for multi-Plane Realms.

The RmmRttPlaneFeature enumeration is an abstract type.

See also:

- A3.12 Support for auxiliary Planes

The values of the RmmRttPlaneFeature enumeration are shown in the following table.

| Name                 | Description                                                                         |
|----------------------|-------------------------------------------------------------------------------------|
| RTT_PLANE_AUX        | A multi-Plane Realm uses auxiliary RTTs                                             |
| RTT_PLANE_AUX_SINGLE | A multi-Plane Realm can be configured to either use auxiliary RTTs, or a single RTT |
| RTT_PLANE_SINGLE     | A multi-Plane Realm uses a single RTT                                               |

The RmmRttPlaneFeature enumeration is used in the following types:

- RmmGlobalStatic

## C2.67 RmmRttProtected type

The RmmRttProtected enumeration represents specifies whether an RTT entry is in Protected IPA space or Unprotected IPA space.

The RmmRttProtected enumeration is an abstract type.

The values of the RmmRttProtected enumeration are shown in the following table.

| Name            | Description            |
|-----------------|------------------------|
| RTT_PROTECTED   | Protected IPA space.   |
| RTT_UNPROTECTED | Unprotected IPA space. |

## C2.68 RmmRttS2APBase type


The RmmRttS2APBase enumeration represents S2AP base value.

The RmmRttS2APBase enumeration is an abstract type.

The values of the RmmRttS2APBase enumeration are shown in the following table.

| Name           | Description   |
|----------------|---------------|
| S2AP_NO_ACCESS | NoAccess      |
| S2AP_RO        | RO            |
| S2AP_RW        | RW            |
| S2AP_RW_PUX    | RW+puX        |
| S2AP_WO        | WO            |

The RmmRttS2APBase enumeration is used in the following types:

- RmmRttS2APIndirect

## C2.69 RmmRttS2APDirect type

The RmmRttS2APDirect structure contains directly-encoded S2AP.

The RmmRttS2APDirect structure is an abstract type.

The members of the RmmRttS2APDirect structure are shown in the following table.

| Name   | Type       | Description      |
|--------|------------|------------------|
| read   | RmmBoolean | Read permission  |
| write  | RmmBoolean | Write permission |

The RmmRttS2APDirect structure is used in the following types:

- RmmRttEntry

## C2.70 RmmRttS2APEncoding type

The RmmRttS2APEncoding enumeration represents encoding used for S2AP.

The RmmRttS2APEncoding enumeration is an abstract type.

See also:

- A3.13 Support for Stage 2 Access Permissions indirect encoding

The values of the RmmRttS2APEncoding enumeration are shown in the following table.

| Name          | Description                                                   |
|---------------|---------------------------------------------------------------|
| S2AP_DIRECT   | S2AP is encoded directly in the RTT entry.                    |
| S2AP_INDIRECT | RTT entry includes indices which indirectly specify the S2AP. |


The RmmRttS2APEncoding enumeration is used in the following types:

- RmmRealm

## C2.71 RmmRttS2APIndirect type

The RmmRttS2APIndirect structure contains indirectly-encoded S2AP.

The RmmRttS2APIndirect structure is an abstract type.

The members of the RmmRttS2APIndirect structure are shown in the following table.

| Name          | Type           | Description              |
|---------------|----------------|--------------------------|
| base_index    | RmmRttS2APBase | Base permission index    |
| overlay_index | UInt4          | Overlay permission index |

The RmmRttS2APIndirect structure is used in the following types:

- RmmRttEntry

## C2.72 RmmRttShareability type

The RmmRttShareability enumeration represents shareability attributes.

The RmmRttShareability enumeration is an abstract type.

The values of the RmmRttShareability enumeration are shown in the following table.

| Name               | Description      |
|--------------------|------------------|
| SHAREABILITY_INNER | Inner Shareable. |
| SHAREABILITY_OUTER | Outer Shareable. |

The RmmRttShareability enumeration is used in the following types:

- RmmRttEntry

## C2.73 RmmRttWalkNotAligned type

The RmmRttWalkNotAligned structure contains result of an RTT walk which is not aligned to the requested level.

The RmmRttWalkNotAligned structure is an abstract type.

The members of the RmmRttWalkNotAligned structure are shown in the following table.

| Name   | Type             | Description                                                                          |
|--------|------------------|--------------------------------------------------------------------------------------|
| valid  | RmmBoolean       | TRUE if an RTT walk was performed whose result is not aligned to the requested level |
| index  | UInt64           | RTT index                                                                            |
| addr   | Address          | Address                                                                              |
| walk   | RmmRttWalkResult | Walk result                                                                          |


## C2.74 RmmRttWalkResult type

The RmmRttWalkResult structure contains result of an RTT walk.

The RmmRttWalkResult structure is an abstract type.

See also:

- A5.6.10 RTT walk

The members of the RmmRttWalkResult structure are shown in the following table.

| Name     | Type    | Description                        |
|----------|---------|------------------------------------|
| level    | Int8    | RTT level reached by the walk      |
| rtt_addr | Address | Address of RTT reached by the walk |

| Name   | Type        | Description              |
|--------|-------------|--------------------------|
| rtte   | RmmRttEntry | RTTE reached by the walk |

The RmmRttWalkResult structure is used in the following types:

- RmmRttWalkNotAligned

## C2.75 RmmSmmuMsiConfig type

The RmmSmmuMsiConfig structure contains MSI configuration of an SMMU.

The RmmSmmuMsiConfig structure is an abstract type.

The members of the RmmSmmuMsiConfig structure are shown in the following table.

| Name        | Type    | Description                                                                   |
|-------------|---------|-------------------------------------------------------------------------------|
| gerr_addr   | Address | MSI address of the GERROR interrupt (programmed to SMMU_R_GERROR_IRQ_CFG0)    |
| gerr_data   | Bits64   MSI data of the GERROR interrupt (programmed to SMMU_R_GERROR_IRQ_CFG1) |
| eventq_addr | Address | MSI address of the EVENTQ interrupt (programmed to SMMU_R_EVENTQ_IRQ_CFG0)    |
| eventq_data | Bits64  | MSI data of the EVENTQ interrupt (programmed to SMMU_R_EVENTQ_IRQ_CFG1)       |
| priq_addr   | Address | MSI address of the PRIQ interrupt (programmed to SMMU_R_PRIQ_IRQ_CFG0)        |
| priq_data   | Bits64  | MSI data of the PRIQ interrupt (programmed to SMMU_R_PRIQ_IRQ_CFG1)           |

The RmmSmmuMsiConfig structure is used in the following types:

- RmmVsmmu
- RmmPsmmu

## C2.76 RmmState type

The RmmState enumeration represents lifecycle state of the RMM.

The RmmState enumeration is an abstract type.

The values of the RmmState enumeration are shown in the following table.

| Name                                                   | Description                                            |
|--------------------------------------------------------|--------------------------------------------------------|
| RMM_STATE_ACTIVE                                       | RMMis active.                                          |
| RMM_STATE_INIT                                         | Initial state of the RMM.                              |
| RMM_STATE_INTERMEDIATERMM is in an intermediate state. | RMM_STATE_INTERMEDIATERMM is in an intermediate state. |

The RmmState enumeration is used in the following types:

- RmmGlobalDynamic

## C2.77 RmmSystemRegisters type

The RmmSystemRegisters structure contains EL0 and EL1 system registers.

The RmmSystemRegisters structure is an abstract type.

The RmmSystemRegisters structure is used in the following types:

- RmmRec

## C2.78 RmmTrackingRegion type

The RmmTrackingRegion structure contains attributes of a Granule tracking region.

The RmmTrackingRegion structure is an abstract type.

The members of the RmmTrackingRegion structure are shown in the following table.

| Name     | Type                   | Description            |
|----------|------------------------|------------------------|
| state    | RmmTrackingRegionState | Tracking region state. |
| category | RmmMemCategory         | Memory category.       |

## C2.79 RmmTrackingRegionState type

The RmmTrackingRegionState enumeration represents tracking region state.

The RmmTrackingRegionState enumeration is an abstract type.

The values of the RmmTrackingRegionState enumeration are shown in the following table.


| Name              | Description                                                       |
|-------------------|-------------------------------------------------------------------|
| TRACKING_COARSE   | Region is tracked at the granularity of the Tracking Region size. |
| TRACKING_FINE     | Region is tracked at the granularity of the RMI Granule size.     |
| TRACKING_NONE     | Region is not tracked.                                            |
| TRACKING_RESERVED | Region is reserved for use by the platform.                       |

The RmmTrackingRegionState enumeration is used in the following types:

- RmmTrackingRegion

## C2.80 RmmVdev type

The RmmVdev structure contains attributes of a VDEV.

The RmmVdev structure is an abstract type.

The members of the RmmVdev structure are shown in the following table.

| Name           | Type              | Description                                                                                |
|----------------|-------------------|--------------------------------------------------------------------------------------------|
| vdev_id        | Bits64            | Virtual device identifier                                                                  |
| tdi_id         | Bits64            | TDI identifier                                                                             |
| pdev           | Address           | PA of parent PDEV                                                                          |
| realm          | Address           | PA of RD of Realm which owns this VDEV                                                     |
| vdev_state     | RmmVdevState      | VDEV lifecycle state                                                                       |
| dma_state      | RmmVdevDmaState   | DMAstate                                                                                   |
| non_ats_plane  | UInt64            | Index of Plane whose stage 2 permissions are observed by non-ATS requests from the device  |
| op             | RmmVdevOperation  | Operation performed on this VDEV                                                           |
| comm_state     | RmmDevCommState   | Device communication state                                                                 |
| vsmmu          | RmmFeature        | Whether device uses a VSMMU                                                                |
| vsmmu_addr     | Address           | PA of VSMMU. This field is valid if vsmmu is FEATURE_TRUE.                                 |
| vsid           | Bits64             Virtual Stream Identifier. This field is valid if vsmmu is FEATURE_TRUE.             |
| attest_info    | RmmVdevAttestInfo | Attestation information                                                                    |
| meas_digest    | Bits512           | Measurement digest                                                                         |
| report_digest  | Bits512           | Interface report digest                                                                    |
| p2p_bound      | RmmFeature        | Whether VDEV is bound to a P2P peer VDEV                                                   |
| p2p_peer       | Bits64            | VDEV ID of P2P peer VDEV                                                                   |
| num_addr_range | UInt64            | Number of device address ranges                                                            |
| addr_range     | RmmAddrRange[8]   | Device address ranges. These ranges include both coherent and non- coherent device memory. |

## C2.81 RmmVdevAddrResult type

The RmmVdevAddrResult structure contains result of scanning VDEV address ranges.

The RmmVdevAddrResult structure is an abstract type.

The members of the RmmVdevAddrResult structure are shown in the following table.

| Name   | Type       | Description                        |
|--------|------------|------------------------------------|
| valid  | RmmBoolean | Whether a mapped Granule was found |
| addr   | Address    | PA of mapped Granule               |

## C2.82 RmmVdevAttestInfo type

The RmmVdevAttestInfo structure contains attestation information for a VDEV.

The RmmVdevAttestInfo structure is an abstract type.

The members of the RmmVdevAttestInfo structure are shown in the following table.

| Name         | Type   | Description                                                 |
|--------------|--------|-------------------------------------------------------------|
| lock_nonce   | UInt64 | Nonce generated on most recent transition to LOCKED state   |
| meas_nonce   | UInt64 | Nonce generated on most recent GET_MEASUREMENT request      |
| report_nonce | UInt64 | Nonce generated on most recent GET_INTERFACE_REPORT request |

The RmmVdevAttestInfo structure is used in the following types:

- RmmRec
- RmmVdev

## C2.83 RmmVdevDmaState type

The RmmVdevDmaState enumeration represents the state of DMA for a VDEV.

The RmmVdevDmaState enumeration is an abstract type.

The values of the RmmVdevDmaState enumeration are shown in the following table.

| Name              | Description     |
|-------------------|-----------------|
| VDEV_DMA_DISABLED | DMAis disabled. |
| VDEV_DMA_ENABLED  | DMAis enabled.  |


The RmmVdevDmaState enumeration is used in the following types:

- RmmVdev

## C2.84 RmmVdevOperation type

The RmmVdevOperation enumeration represents operation performed on a VDEV.

The RmmVdevOperation enumeration is an abstract type.

The values of the RmmVdevOperation enumeration are shown in the following table.

| Name                | Description                   |
|---------------------|-------------------------------|
| VDEV_OP_GET_MEAS    | Request a measurement report. |
| VDEV_OP_GET_REPORT  | Request an interface report.  |
| VDEV_OP_KEY_PURGE   | Purge keys of PDEV streams.   |
| VDEV_OP_KEY_REFRESH | Refresh keys of PDEV streams. |
| VDEV_OP_LOCK        | Change state to LOCKED.       |

| Name               | Description               |
|--------------------|---------------------------|
| VDEV_OP_NONE       | No operation.             |
| VDEV_OP_P2P_BIND   | Create a P2P binding.     |
| VDEV_OP_P2P_UNBIND | Remove a P2P binding.     |
| VDEV_OP_START      | Change state to STARTED.  |
| VDEV_OP_UNLOCK     | Change state to UNLOCKED. |

The RmmVdevOperation enumeration is used in the following types:

- RmmVdev

## C2.85 RmmVdevState type

The RmmVdevState enumeration represents the state of a VDEV.

The RmmVdevState enumeration is an abstract type.

The values of the RmmVdevState enumeration are shown in the following table.

| Name             | Description                                                                                                   |
|------------------|---------------------------------------------------------------------------------------------------------------|
| VDEV_ERROR       | Device interface has reported a fatal error.                                                                  |
| VDEV_KEY_PURGE    Waiting for purge of inactive keys to be performed on all streams associated with the device interface. |
| VDEV_KEY_REFRESH | Waiting for key refresh to be performed on all streams associated with the device interface.                  |
| VDEV_LOCKED      | Device interface is locked.                                                                                   |
| VDEV_NEW         | Initial state of the device interface.                                                                        |
| VDEV_STARTED     | Device interface is started.                                                                                  |
| VDEV_UNLOCKED    | Device interface is unlocked.                                                                                 |

The RmmVdevState enumeration is used in the following types:

- RmmVdev

## C2.86 RmmVsmmu type

The RmmVsmmu structure contains attributes of a VSMMU.

The RmmVsmmu structure is an abstract type.

The members of the RmmVsmmu structure are shown in the following table.

| Name   | Type          | Description        |
|--------|---------------|--------------------|
| state  | RmmVsmmuState | State of the VSMMU |

| Name       | Type             | Description                                              |
|------------|------------------|----------------------------------------------------------|
| realm      | Address          | PA of RD of Realm which owns this VSMMU                  |
| reg_base   | Address          | Base IPA of register base in Realm's Protected IPA space |
| reg_top    | Address          | Top IPA of register base in Realm's Protected IPA space  |
| aidr       | Bits64           | SMMU_AIDR register value                                 |
| idr        | Bits64[7]        | SMMU_IDR register values                                 |
| msi_config | RmmSmmuMsiConfig | MSI configuration                                        |

## C2.87 RmmVsmmuState type

The RmmVsmmuState enumeration represents the state of a VSMMU.

The RmmVsmmuState enumeration is an abstract type.

The values of the RmmVsmmuState enumeration are shown in the following table.

| Name           | Description                                |
|----------------|--------------------------------------------|
| VSMMU_ACTIVE   | VSMMU has been activated by the Realm.     |
| VSMMU_INACTIVE | VSMMU has not been activated by the Realm. |

The RmmVsmmuState enumeration is used in the following types:

- RmmVsmmu

