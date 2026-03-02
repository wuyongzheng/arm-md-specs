## Chapter C1 RMM types

This section describes types which are used to model the abstract state of the RMM.

## C1.1 RmmDataFlags type

The RmmDataFlags fieldset contains flags provided by the Host during DATA Granule creation.

The RmmDataFlags fieldset is a concrete type.

The width of the RmmDataFlags fieldset is 64 bits.

The fields of the RmmDataFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmmDataFlags fieldset are shown in the following table.

| Name    | Bits   | Description                              | Value                 |
|---------|--------|------------------------------------------|-----------------------|
| measure | 0:0    | Whether to measure DATA Granule contents | RmmDataMeasureContent |
|         | 63:1   | Reserved                                 | SBZ                   |

## C1.2 RmmDataMeasureContent type

The RmmDataMeasureContent enumeration represents whether to measure DATA Granule contents.

The RmmDataMeasureContent enumeration is a concrete type.

The width of the RmmDataMeasureContent enumeration is 1 bits.

The values of the RmmDataMeasureContent enumeration are shown in the following table.

|   Encoding | Name               | Description                           |
|------------|--------------------|---------------------------------------|
|          0 | NO_MEASURE_CONTENT | Do not measure DATA Granule contents. |
|          1 | MEASURE_CONTENT    | Measure DATA Granule contents.        |

## C1.3 RmmFeature type

The RmmFeature enumeration represents whether a feature is enabled.

The RmmFeature enumeration is an abstract type.

The values of the RmmFeature enumeration are shown in the following table.

| Name          | Description                                                                               |
|---------------|-------------------------------------------------------------------------------------------|
| FEATURE_FALSE | • During discovery: Feature is not supported. • During selection: Feature is not enabled. |
| FEATURE_TRUE  | • During discovery: Feature is supported. • During selection: Feature is enabled.         |

## C1.4 RmmFeatures type

The RmmFeatures structure contains features supported by RMM implementation.

The RmmFeatures structure is an abstract type.

The members of the RmmFeatures structure are shown in the following table.

| Name          | Type       | Description               |
|---------------|------------|---------------------------|
| max_ipa_width | UInt64     | Maximum IPA width         |
| feat_lpa2     | RmmFeature | Whether LPA2 is supported |
| feat_sve      | RmmFeature | Whether SVE is supported  |

| Name           | Type       | Description                                                        |
|----------------|------------|--------------------------------------------------------------------|
| max_sve_vl     | UInt64     | Maximum SVE vector length                                          |
| num_bps        | UInt64     | Number of breakpoints available                                    |
| num_wps        | UInt64     | Number of watchpoints available                                    |
| feat_pmu       | RmmFeature | Number of watchpoints available                                    |
| pmu_num_ctrs   | UInt64     | Number of PMU counters available                                   |
| feat_sha_256   | RmmFeature | Whether SHA-256 is supported                                       |
| feat_sha_512   | RmmFeature | Whether SHA-512 is supported                                       |
| max_recs_order | UInt64     | Order of the maximum number of RECs which can be created per Realm |

## C1.5 RmmGptEntry type

The RmmGptEntry enumeration represents granule Protection Table entry.

The RmmGptEntry enumeration is an abstract type.

See also:

- B3.20 GranuleAccessPermitted function

The values of the RmmGptEntry enumeration are shown in the following table.

| Name       | Description                               |
|------------|-------------------------------------------|
| GPT_AAP    | Access permitted via any PAS.             |
| GPT_NS     | Access permitted via Non-secure PAS only. |
| GPT_REALM  | Access permitted via Realm PAS only.      |
| GPT_ROOT   | Access permitted via Root PAS only.       |
| GPT_SECURE | Access permitted via Secure PAS only.     |

## C1.6 RmmGranule type

The RmmGranule structure contains attributes of a Granule.

The RmmGranule structure is an abstract type.

The members of the RmmGranule structure are shown in the following table.

| Name   | Type            | Description     |
|--------|-----------------|-----------------|
| gpt    | RmmGptEntry     | GPT entry       |
| state  | RmmGranuleState | Lifecycle state |

## C1.7 RmmGranuleState type

The RmmGranuleState enumeration represents the state of a granule.

The RmmGranuleState enumeration is an abstract type.

The values of the RmmGranuleState enumeration are shown in the following table.

| Name        | Description                                |
|-------------|--------------------------------------------|
| DATA        | Realm code or data.                        |
| DELEGATED   | Delegated for use by the RMM.              |
| RD          | Realm Descriptor.                          |
| REC         | Realm Execution Context.                   |
| REC_AUX     | Realm Execution Context auxiliary Granule. |
| RTT         | Realm Translation Table.                   |
| UNDELEGATED | Not delegated for use by the RMM.          |

## C1.8 RmmHashAlgorithm type

The RmmHashAlgorithm enumeration represents hash algorithm.

The RmmHashAlgorithm enumeration is an abstract type.

The values of the RmmHashAlgorithm enumeration are shown in the following table.

| Name         | Description                                |
|--------------|--------------------------------------------|
| HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [15]) |
| HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [15]) |

## C1.9 RmmHipas type

The RmmHipas enumeration represents host IPA state.

The RmmHipas enumeration is an abstract type.

The values of the RmmHipas enumeration are shown in the following table.

| Name                | Description                                               |
|---------------------|-----------------------------------------------------------|
| HIPAS_ASSIGNED      | Protected IPA which is associated with a DATA Granule.    |
| HIPAS_ASSIGNED_NS   | Unprotected IPA which is associated with an NS Granule.   |
| HIPAS_UNASSIGNED    | Protected IPA which is not associated with any Granule.   |
| HIPAS_UNASSIGNED_NS | Unprotected IPA which is not associated with any Granule. |

## C1.10 RmmHostCallPending type

The RmmHostCallPending enumeration represents whether a Host call is pending.

The RmmHostCallPending enumeration is an abstract type.

The values of the RmmHostCallPending enumeration are shown in the following table.

| Name                 | Description              |
|----------------------|--------------------------|
| HOST_CALL_PENDING    | No Host call is pending. |
| NO_HOST_CALL_PENDING | A Host call is pending.  |

## C1.11 RmmMeasurementDescriptorData type

The RmmMeasurementDescriptorData structure contains data structure used to calculate the contribution to the RIM of a DATA Granule.

The RmmMeasurementDescriptorData structure is a concrete type.

The width of the RmmMeasurementDescriptorData structure is 256 ( 0x100 ) bytes.

See also:

- B4.3.1.4 RMI\_DATA\_CREATE extension of RIM

The members of the RmmMeasurementDescriptorData structure are shown in the following table.

| Name      | Byte offset   | Type                | Description                                                                                      |
|-----------|---------------|---------------------|--------------------------------------------------------------------------------------------------|
| desc_type | 0x0           | Bits8               | Measurement descriptor type, value 0x0                                                           |
| len       | 0x8           | UInt64              | Length of this data structure in bytes                                                           |
| rim       | 0x10          | RmmRealmMeasurement | Current RIM value                                                                                |
| ipa       | 0x50          | Address             | IPA at which the DATA Granule is mapped in the Realm                                             |
| flags     | 0x58          | RmmDataFlags        | Flags provided by Host                                                                           |
| content   | 0x60          | RmmRealmMeasurement | Hash of contents of DATA Granule, or zero if flags indicate DATA Granule contents are unmeasured |

Unused bits of the RmmMeasurementDescriptorData structure MBZ.

## C1.12 RmmMeasurementDescriptorRec type

The RmmMeasurementDescriptorRec structure contains data structure used to calculate the contribution to the RIM of a REC.

The RmmMeasurementDescriptorRec structure is a concrete type.

The width of the RmmMeasurementDescriptorRec structure is 256 ( 0x100 ) bytes.

See also:

- B4.3.12.4 RMI\_REC\_CREATE extension of RIM

The members of the RmmMeasurementDescriptorRec structure are shown in the following table.

| Name      | Byte offset   | Type                | Description                                                   |
|-----------|---------------|---------------------|---------------------------------------------------------------|
| desc_type | 0x0           | Bits8               | Measurement descriptor type, value 0x1                        |
| len       | 0x8           | UInt64              | Length of this data structure in bytes                        |
| rim       | 0x10          | RmmRealmMeasurement | Current RIM value                                             |
| content   | 0x50          | RmmRealmMeasurement | Hash of 4KB page which contains REC parameters data structure |

Unused bits of the RmmMeasurementDescriptorRec structure MBZ.

## C1.13 RmmMeasurementDescriptorRipas type

The RmmMeasurementDescriptorRipas structure contains data structure used to calculate the contribution to the RIM of a RIPAS change.

The RmmMeasurementDescriptorRipas structure is a concrete type.

The width of the RmmMeasurementDescriptorRipas structure is 256 ( 0x100 ) bytes.

See also:

- B4.3.18.4 RMI\_RTT\_INIT\_RIPAS extension of RIM

The members of the RmmMeasurementDescriptorRipas structure are shown in the following table.

| Name      | Byte offset   | Type                | Description                            |
|-----------|---------------|---------------------|----------------------------------------|
| desc_type | 0x0           | Bits8               | Measurement descriptor type, value 0x2 |
| len       | 0x8           | UInt64              | Length of this data structure in bytes |
| rim       | 0x10          | RmmRealmMeasurement | Current RIM value                      |
| base      | 0x50          | Address             | Base IPA of the RIPAS change           |
| top       | 0x58          | Address             | Top IPA of the RIPAS change            |

Unused bits of the RmmMeasurementDescriptorRipas structure MBZ.

## C1.14 RmmPhysicalAddressSpace type

The RmmPhysicalAddressSpace enumeration represents the PAS of a Granule.

The RmmPhysicalAddressSpace enumeration is an abstract type.

See also:

- B3.20 GranuleAccessPermitted function

The values of the RmmPhysicalAddressSpace enumeration are shown in the following table.

| Name       | Description     |
|------------|-----------------|
| PAS_NS     | Non-secure PAS. |
| PAS_REALM  | Realm PAS.      |
| PAS_ROOT   | Root PAS.       |
| PAS_SECURE | Secure PAS.     |

## C1.15 RmmPsciPending type

The RmmPsciPending enumeration represents whether a PSCI request is pending.

The RmmPsciPending enumeration is an abstract type.

The values of the RmmPsciPending enumeration are shown in the following table.

| Name                    | Description                 |
|-------------------------|-----------------------------|
| NO_PSCI_REQUEST_PENDING | A PSCI request is pending.  |
| PSCI_REQUEST_PENDING    | No PSCI request is pending. |

## C1.16 RmmRealm type

The RmmRealm structure contains attributes of a Realm.

The RmmRealm structure is an abstract type.

See also:

- A2.1 Realm

The members of the RmmRealm structure are shown in the following table.

| Name            | Type                   | Description                                         |
|-----------------|------------------------|-----------------------------------------------------|
| feat_lpa2       | RmmFeature             | Whether LPA2 is enabled for this Realm              |
| ipa_width       | UInt8                  | IPA width in bits                                   |
| measurements    | RmmRealmMeasurement[5] | Realm measurements                                  |
| hash_algo       | RmmHashAlgorithm       | Algorithm used to compute Realm measurements        |
| rec_index       | UInt64                 | Index of next REC to be created                     |
| rtt_base        | Address                | Realm Translation Table base address                |
| rtt_level_start | Int64                  | RTT starting level                                  |
| rtt_num_start   | UInt64                 | Number of physically contiguous starting level RTTs |
| state           | RmmRealmState          | Lifecycle state                                     |
| vmid            | Bits16                 | Virtual Machine Identifier                          |
| rpv             | Bits512                | Realm Personalization Value                         |

| Name     | Type   | Description                        |
|----------|--------|------------------------------------|
| num_recs | UInt64 | Number of RECs owned by this Realm |

## C1.17 RmmRealmMeasurement type

The RmmRealmMeasurement type is realm measurement.

The RmmRealmMeasurement type is a concrete type.

The width of the RmmRealmMeasurement type is 512 bits.

## C1.18 RmmRealmState type

The RmmRealmState enumeration represents the state of a Realm.

The RmmRealmState enumeration is an abstract type.

The values of the RmmRealmState enumeration are shown in the following table.

| Name             | Description                                             |
|------------------|---------------------------------------------------------|
| REALM_ACTIVE     | Eligible for execution.                                 |
| REALM_NEW        | Under construction. Not eligible for execution.         |
| REALM_SYSTEM_OFF | System has been turned off. Not eligible for execution. |

## C1.19 RmmRec type

The RmmRec structure contains attributes of a REC.

The RmmRec structure is an abstract type.

See also:

- A2.3 Realm Execution Context

The members of the RmmRec structure are shown in the following table.

| Name             | Type                  | Description                                                                    |
|------------------|-----------------------|--------------------------------------------------------------------------------|
| attest_state     | RmmRecAttestState     | Attestation token generation state                                             |
| attest_challenge | Bits512               | Challenge for under-construction attestation token                             |
| aux              | Address[16]           | Addresses of auxiliary Granules                                                |
| emulatable_abort | RmmRecEmulatableAbort | Whether the most recent exit from this REC was due to an Emulatable Data Abort |
| flags            | RmmRecFlags           | Flags which control REC behavior                                               |
| gprs             | Bits64[32]            | General-purpose register values                                                |
| mpidr            | Bits64                | MPIDR value                                                                    |
| owner            | Address               | PA of RD of Realm which owns this REC                                          |

| Name              | Type                    | Description                                               |
|-------------------|-------------------------|-----------------------------------------------------------|
| pc                | Bits64                  | Program counter value                                     |
| psci_pending      | RmmPsciPending          | Whether a PSCI request is pending                         |
| state             | RmmRecState             | Lifecycle state                                           |
| sysregs           | RmmSystemRegisters      | EL1 and EL0 system register values                        |
| ripas_addr        | Address                 | Next address to be processed in RIPAS change              |
| ripas_top         | Address                 | Top address of pending RIPAS change                       |
| ripas_value       | RmmRipas                | RIPAS value of pending RIPAS change                       |
| ripas_destroyed   | RmmRipasChangeDestroyed | Whether a RIPAS change from DESTROYED should be permitted |
| ripas_response    | RmmRecResponse          | Host response to RIPAS change request                     |
| host_call_pending | RmmHostCallPending      | Whether a Host call is pending                            |

## C1.20 RmmRecAttestState type

The RmmRecAttestState enumeration represents whether an attestation token generation operation is ongoing on this REC.

The RmmRecAttestState enumeration is an abstract type.

The values of the RmmRecAttestState enumeration are shown in the following table.

| Name                  | Description                                               |
|-----------------------|-----------------------------------------------------------|
| ATTEST_IN_PROGRESS    | An attestation token generation operation is in progress. |
| NO_ATTEST_IN_PROGRESS | No attestation token generation operation is in progress. |

## C1.21 RmmRecEmulatableAbort type

The RmmRecEmulatableAbort enumeration represents whether the most recent exit from a REC was due to an Emulatable Data Abort.

The RmmRecEmulatableAbort enumeration is an abstract type.

The values of the RmmRecEmulatableAbort enumeration are shown in the following table.

| Name                 | Description                                                              |
|----------------------|--------------------------------------------------------------------------|
| EMULATABLE_ABORT     | The most recent exit from a REC was due to an Emulatable Data Abort.     |
| NOT_EMULATABLE_ABORT | The most recent exit from a REC was not due to an Emulatable Data Abort. |

## C1.22 RmmRecFlags type

The RmmRecFlags structure contains REC flags.

The RmmRecFlags structure is an abstract type.

The members of the RmmRecFlags structure are shown in the following table.

| Name     | Type           | Description                       |
|----------|----------------|-----------------------------------|
| runnable | RmmRecRunnable | Whether the REC is elgible to run |

## C1.23 RmmRecResponse type

The RmmRecResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RmmRecResponse enumeration is an abstract type.

The values of the RmmRecResponse enumeration are shown in the following table.

| Name   | Description                      |
|--------|----------------------------------|
| ACCEPT | Host accepted the Realm request. |
| REJECT | Host rejected the Realm request. |

## C1.24 RmmRecRunnable type

The RmmRecRunnable enumeration represents whether a REC is eligible for execution.

The RmmRecRunnable enumeration is an abstract type.

The values of the RmmRecRunnable enumeration are shown in the following table.

| Name         | Description                 |
|--------------|-----------------------------|
| NOT_RUNNABLE | Not eligible for execution. |
| RUNNABLE     | Eligible for execution.     |

## C1.25 RmmRecState type

The RmmRecState enumeration represents the state of a REC.

The RmmRecState enumeration is an abstract type.

The values of the RmmRecState enumeration are shown in the following table.

| Name        | Description                   |
|-------------|-------------------------------|
| REC_READY   | REC is not currently running. |
| REC_RUNNING | REC is currently running.     |

| Name   | Description   |
|--------|---------------|

## C1.26 RmmRipas type

The RmmRipas enumeration represents realm IPA state.

The RmmRipas enumeration is an abstract type.

The values of the RmmRipas enumeration are shown in the following table.

| Name      | Description                                                                    |
|-----------|--------------------------------------------------------------------------------|
| DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
| DEV       | Address where memory of an assigned Realm device is mapped.                    |
| EMPTY     | Address where no Realm resources are mapped.                                   |
| RAM       | Address where private code or data owned by the Realm is mapped.               |

## C1.27 RmmRipasChangeDestroyed type

The RmmRipasChangeDestroyed enumeration represents whether a RIPAS change from DESTROYED should be permitted.

The RmmRipasChangeDestroyed enumeration is an abstract type.

The values of the RmmRipasChangeDestroyed enumeration are shown in the following table.

| Name                | Description                                            |
|---------------------|--------------------------------------------------------|
| CHANGE_DESTROYED    | A RIPAS change from DESTROYED should be permitted.     |
| NO_CHANGE_DESTROYED | A RIPAS change from DESTROYED should not be permitted. |

## C1.28 RmmRtt type

The RmmRtt structure contains an RTT.

The RmmRtt structure is an abstract type.

The members of the RmmRtt structure are shown in the following table.

| Name    | Type             | Description   |
|---------|------------------|---------------|
| entries | RmmRttEntry[512] | Entries       |

## C1.29 RmmRttEntry type

The RmmRttEntry structure contains attributes of an RTT Entry.

The RmmRttEntry structure is an abstract type.

See also:

- A5.5 Realm Translation Table

The members of the RmmRttEntry structure are shown in the following table.

| Name    | Type             | Description    |
|---------|------------------|----------------|
| addr    | Address          | Output address |
| ripas   | RmmRipas         | RIPAS          |
| state   | RmmRttEntryState | State          |
| MemAttr | Bits3            | MemAttr        |
| S2AP    | Bits2            | S2AP           |

## C1.30 RmmRttEntryState type

The RmmRttEntryState enumeration represents the state of an RTTE.

The RmmRttEntryState enumeration is an abstract type.

The values of the RmmRttEntryState enumeration are shown in the following table.

| Name          | Description                                                                                             |
|---------------|---------------------------------------------------------------------------------------------------------|
| ASSIGNED      | This RTTE is identified by a Protected IPA. The output address of this RTTE points to a DATA Granule.   |
| ASSIGNED_NS   | This RTTE is identified by an Unprotected IPA. The output address of this RTTE points to an NS Granule. |
| TABLE         | The output address of this RTTE points to the next-level RTT.                                           |
| UNASSIGNED    | This RTTE is identified by a Protected IPA. This RTTE is not associated with any Granule.               |
| UNASSIGNED_NS | This RTTE is identified by an Unprotected IPA. This RTTE is not associated with any Granule.            |

## C1.31 RmmRttWalkResult type

The RmmRttWalkResult structure contains result of an RTT walk.

The RmmRttWalkResult structure is an abstract type.

See also:

- A5.5.10 RTT walk

The members of the RmmRttWalkResult structure are shown in the following table.

| Name     | Type        | Description                        |
|----------|-------------|------------------------------------|
| level    | Int8        | RTT level reached by the walk      |
| rtt_addr | Address     | Address of RTT reached by the walk |
| rtte     | RmmRttEntry | RTTE reached by the walk           |

## C1.32 RmmSystemRegisters type

The RmmSystemRegisters structure contains EL0 and EL1 system registers.

The RmmSystemRegisters structure is an abstract type.