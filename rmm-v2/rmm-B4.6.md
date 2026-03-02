## B4.6 RMI types

This section defines types which are used in the RMI interface.

## B4.6.1 RmiAddrBlockSize type

The RmiAddrBlockSize enumeration represents size of a block of contiguous address space.

The RmiAddrBlockSize enumeration is a concrete type.

The width of the RmiAddrBlockSize enumeration is 2 bits.

The values of the RmiAddrBlockSize enumeration are shown in the following table.

|   Encoding | Name         | Description         |
|------------|--------------|---------------------|
|          0 | RMI_PAGE_L3  | Level 3 page size.  |
|          1 | RMI_BLOCK_L2 | Level 2 block size. |
|          2 | RMI_BLOCK_L1 | Level 1 block size. |
|          3 | RMI_BLOCK_L0 | Level 0 block size. |

The RmiAddrBlockSize enumeration is used in the following types:

- RmiAddrRangeDesc16KB
- RmiAddrRangeDesc4KB
- RmiAddrRangeDesc
- RmiAddrSetDesc
- RmiOpMemDonateReq
- RmiAddrRangeDesc64KB

## B4.6.2 RmiAddrRange type

The RmiAddrRange structure contains address range.

DRAFT

The RmiAddrRange structure is a concrete type.

The width of the RmiAddrRange structure is 16 ( 0x10 ) bytes.

The members of the RmiAddrRange structure are shown in the following table.

| Name   | Byte offset   | Type    | Description                       |
|--------|---------------|---------|-----------------------------------|
| base   | 0x0           | Address | Base of address range (inclusive) |
| top    | 0x8           | Address | Top of address range (exclusive)  |

The RmiAddrRange structure is used in the following types:

- RmiCmemParams
- RmiVdevParams
- RmiPdevStreamParams

## B4.6.3 RmiAddrRangeDesc type

The RmiAddrRangeDesc fieldset contains a descriptor which identifies a contiguous address range.

The RmiAddrRangeDesc fieldset is a concrete type.

The width of the RmiAddrRangeDesc fieldset is 64 bits.

See also:

- B4.4 RMI Address Range Descriptor

The fields of the RmiAddrRangeDesc fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiAddrRangeDesc fieldset are shown in the following table.

| Name   | Bits   | Description   | Value     |
|--------|--------|---------------|-----------|
| data   | 63:0   | Conditional   | See below |

Encodings for field data:

| Name         | Condition                                                    | Fieldset             |
|--------------|--------------------------------------------------------------|----------------------|
| granule_4kb  | RmmGlobal().static.rmm_granule_size == RMI_GRANULE_SIZE_4KB  | RmiAddrRangeDesc4KB  |
| granule_16kb | RmmGlobal().static.rmm_granule_size == RMI_GRANULE_SIZE_16KB | RmiAddrRangeDesc16KB |
| granule_64kb | RmmGlobal().static.rmm_granule_size == RMI_GRANULE_SIZE_64KB | RmiAddrRangeDesc64KB |

DRAFT

The RmiAddrRangeDesc fieldset is used in the following types:

- RmiAddrSetDesc

## B4.6.4 RmiAddrRangeDesc16KB type

The RmiAddrRangeDesc16KB fieldset contains a descriptor which identifies a contiguous address range, when RMI Granule Size is 16KB.

The RmiAddrRangeDesc16KB fieldset is a concrete type.

The width of the RmiAddrRangeDesc16KB fieldset is 64 bits.

The fields of the RmiAddrRangeDesc16KB fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiAddrRangeDesc16KB fieldset are shown in the following table.

| Name   | Bits   | Description                      | Value            |
|--------|--------|----------------------------------|------------------|
| size   | 1:0    | Size of each block in the range  | RmiAddrBlockSize |
| count  | 13:2   | Number of blocks in the range    | UInt12           |
| addr   | 51:14  | Base address of the range        | Bits38           |
|        | 62:52  | Reserved                         | SBZ              |
| state  | 63     | State of memory within the range | RmiOpMemState    |

The RmiAddrRangeDesc16KB fieldset is used in the following types:

- RmiAddrSetDesc
- RmiAddrRangeDesc

## B4.6.5 RmiAddrRangeDesc4KB type

DRAFT

The RmiAddrRangeDesc4KB fieldset contains a descriptor which identifies a contiguous address range, when RMI Granule Size is 4KB.

The RmiAddrRangeDesc4KB fieldset is a concrete type.

The width of the RmiAddrRangeDesc4KB fieldset is 64 bits.

The fields of the RmiAddrRangeDesc4KB fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiAddrRangeDesc4KB fieldset are shown in the following table.

| Name   | Bits   | Description                      | Value            |
|--------|--------|----------------------------------|------------------|
| size   | 1:0    | Size of each block in the range  | RmiAddrBlockSize |
| count  | 11:2   | Number of blocks in the range    | UInt10           |
| addr   | 51:12  | Base address of the range        | Bits40           |
|        | 62:52  | Reserved                         | SBZ              |
| state  | 63     | State of memory within the range | RmiOpMemState    |

The RmiAddrRangeDesc4KB fieldset is used in the following types:

- RmiAddrSetDesc
- RmiAddrRangeDesc

## B4.6.6 RmiAddrRangeDesc64KB type

DRAFT

The RmiAddrRangeDesc64KB fieldset contains a descriptor which identifies a contiguous address range, when RMI Granule Size is 64KB.

The RmiAddrRangeDesc64KB fieldset is a concrete type.

The width of the RmiAddrRangeDesc64KB fieldset is 64 bits.

The fields of the RmiAddrRangeDesc64KB fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiAddrRangeDesc64KB fieldset are shown in the following table.

| Name   | Bits   | Description                      | Value            |
|--------|--------|----------------------------------|------------------|
| size   | 1:0    | Size of each block in the range  | RmiAddrBlockSize |
| count  | 15:2   | Number of blocks in the range    | UInt14           |
| addr   | 51:16  | Base address of the range        | Bits36           |
|        | 62:52  | Reserved                         | SBZ              |
| state  | 63     | State of memory within the range | RmiOpMemState    |

The RmiAddrRangeDesc64KB fieldset is used in the following types:

- RmiAddrSetDesc
- RmiAddrRangeDesc

## B4.6.7 RmiAddrSetDesc type

DRAFT

The RmiAddrSetDesc fieldset contains a descriptor which identifies an address set.

The RmiAddrSetDesc fieldset is a concrete type.

The width of the RmiAddrSetDesc fieldset is 64 bits.

The fields of the RmiAddrSetDesc fieldset are shown in the following diagram.

The fields of the RmiAddrSetDesc fieldset are shown in the following table.

| Name   | Bits   | Description   | Value     |
|--------|--------|---------------|-----------|
| data   | 63:0   | Conditional   | See below |

Encodings for field data:

| Name      | Condition                                | Fieldset         |
|-----------|------------------------------------------|------------------|
| single    | flags.oaddr_type == RMI_ADDR_TYPE_SINGLE | RmiAddrRangeDesc |
| list_addr | flags.oaddr_type == RMI_ADDR_TYPE_LIST   | RmiAddrSetList   |

## B4.6.8 RmiAddrSetList type

The RmiAddrSetList fieldset contains address of a Granule which contains a list of RMI Address Range Descriptors.

The RmiAddrSetList fieldset is a concrete type.

The width of the RmiAddrSetList fieldset is 64 bits.

The fields of the RmiAddrSetList fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiAddrSetList fieldset are shown in the following table.

| Name   | Bits   | Description            | Value   |
|--------|--------|------------------------|---------|
| addr   | 63:0   | Address of the Granule | Address |

The RmiAddrSetList fieldset is used in the following types:

- RmiAddrSetDesc

## B4.6.9 RmiBoolean type

DRAFT

The RmiBoolean enumeration represents a boolean value.

The RmiBoolean enumeration is a concrete type.

The width of the RmiBoolean enumeration is 1 bits.

The values of the RmiBoolean enumeration are shown in the following table.

|   Encoding | Name      | Description   |
|------------|-----------|---------------|
|          0 | RMI_FALSE | False         |
|          1 | RMI_TRUE  | True          |

The RmiBoolean enumeration is used in the following types:

- RmiDevCommExitFlags
- RmiVsmmuEventFlags
- RmiPsmmuIrqResult
- RmiVsmmuCmdFlags
- RmiPsmmuIrqSet

## B4.6.10 RmiCmemFlags type

The RmiCmemFlags fieldset contains flags provided by the Host during CMEM creation.

The RmiCmemFlags fieldset is a concrete type.

The width of the RmiCmemFlags fieldset is 64 bits.

The fields of the RmiCmemFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiCmemFlags fieldset are shown in the following table.

| Name   | Bits   | Description   | Value   |
|--------|--------|---------------|---------|
|        | 63:0   | Reserved      | SBZ     |

The RmiCmemFlags fieldset is used in the following types:

- RmiCmemParams

## B4.6.11 RmiCmemParams type

The RmiCmemParams structure contains parameters provided by the Host during CMEM creation.

The RmiCmemParams structure is a concrete type.

The width of the RmiCmemParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiCmemParams structure are shown in the following table.

| Name       | Byte offset   | Type         | Description                                     |
|------------|---------------|--------------|-------------------------------------------------|
| flags      | 0x0           | RmiCmemFlags | Flags                                           |
| chbcr_addr | 0x8           | Bits64       | Address of CHBCR register in the Host Bridge    |
| hb_hdm_id  | 0x10          | Bits8        | Host Bridge HDMdecoder identifier               |
| addr_range | 0x18          | RmiAddrRange | CMEMwindow. Base and size are aligned to 256MB. |
| ilv_gran   | 0x28          | UInt64       | Interleave granularity in bytes                 |
| ilv_ways   | 0x30          | UInt64       | Number of interleave ways                       |

DRAFT

Unused bits of the RmiCmemParams structure SBZ.

## B4.6.12 RmiCmemPdevParams type

The RmiCmemPdevParams structure contains parameters provided by the Host during additon of PDEV to CMEM.

The RmiCmemPdevParams structure is a concrete type.

The width of the RmiCmemPdevParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiCmemPdevParams structure are shown in the following table.

| Name           | Byte offset   | Type   | Description                                                                                          |
|----------------|---------------|--------|------------------------------------------------------------------------------------------------------|
| dev_hdm_id     | 0x0           | Bits8  | Device HDMdecoder identifier                                                                         |
| dpa_skip_range | 0x8           | Bits64 | Device memory address to skip. This is programmed to the DPA skip register of the device HDMdecoder. |

Unused bits of the RmiCmemPdevParams structure SBZ.

## B4.6.13 RmiContinueBeyond type

The RmiContinueBeyond enumeration represents how RMI\_OP\_CONTINUE should behave once it has transitioned all objects in the target set from the intermediate state to the destination state.

The RmiContinueBeyond enumeration is a concrete type.

The width of the RmiContinueBeyond enumeration is 1 bits.

The values of the RmiContinueBeyond enumeration are shown in the following table.

|   Encoding | Name Description                                            |
|------------|-------------------------------------------------------------|
|          0 | RMI_CONTINUE_KEEP_GOING Continue processing the target set. |
|          1 | RMI_CONTINUE_STOP Return to the Host.                       |

The RmiContinueBeyond enumeration is used in the following types:

- RmiContinueFlags

DRAFT

## B4.6.14 RmiContinueFlags type

The RmiContinueFlags fieldset contains flags provided by the Host when continuing an incomplete operation.

The RmiContinueFlags fieldset is a concrete type.

The width of the RmiContinueFlags fieldset is 64 bits.

The fields of the RmiContinueFlags fieldset are shown in the following diagram.

The fields of the RmiContinueFlags fieldset are shown in the following table.

| Name   | Bits   | Description                                                                                                                                   | Value             |
|--------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------|-------------------|
| beyond | 0      | How RMI_OP_CONTINUE should behave once it has transitioned all objects in the target set from the intermediate state to the destination state | RmiContinueBeyond |
|        | 63:1   | Reserved                                                                                                                                      | SBZ               |

## B4.6.15 RmiDataFlags type

The RmiDataFlags fieldset contains flags provided by the Host during DATA Granule creation.

The RmiDataFlags fieldset is a concrete type.

The width of the RmiDataFlags fieldset is 64 bits.

The fields of the RmiDataFlags fieldset are shown in the following diagram.

DRAFT

The fields of the RmiDataFlags fieldset are shown in the following table.

| Name    | Bits   | Description                              | Value                 |
|---------|--------|------------------------------------------|-----------------------|
| measure | 0      | Whether to measure DATA Granule contents | RmiDataMeasureContent |
|         | 63:1   | Reserved                                 | SBZ                   |

## B4.6.16 RmiDataMeasureContent type

The RmiDataMeasureContent enumeration represents whether to measure DATA Granule contents.

The RmiDataMeasureContent enumeration is a concrete type.

The width of the RmiDataMeasureContent enumeration is 1 bits.

The values of the RmiDataMeasureContent enumeration are shown in the following table.

|   Encoding | Name                   | Description                           |
|------------|------------------------|---------------------------------------|
|          0 | RMI_NO_MEASURE_CONTENT | Do not measure DATA Granule contents. |
|          1 | RMI_MEASURE_CONTENT    | Measure DATA Granule contents.        |

The RmiDataMeasureContent enumeration is used in the following types:

· RmiDataFlags

## B4.6.17 RmiDevCommData type

The RmiDevCommData structure contains data structure shared between Host and RMM for device communication.

The RmiDevCommData structure is a concrete type.

The width of the RmiDevCommData structure is 4096 ( 0x1000 ) bytes.

The members of the RmiDevCommData structure are shown in the following table.

DRAFT

| Name   | Byte offset   | Type            | Description       |
|--------|---------------|-----------------|-------------------|
| enter  | 0x0           | RmiDevCommEnter | Entry information |
| exit   | 0x800         | RmiDevCommExit  | Exit information  |

Unused bits of the RmiDevCommData structure SBZ.

## B4.6.18 RmiDevCommEnter type

The RmiDevCommEnter structure contains data passed from the Host to the RMM during device communication.

The RmiDevCommEnter structure is a concrete type.

The width of the RmiDevCommEnter structure is 256 ( 0x100 ) bytes.

See also:

- A9.5.2.2 Device communication enter data structure

The members of the RmiDevCommEnter structure are shown in the following table.

| Name     | Byte offset   | Type             | Description                                      |
|----------|---------------|------------------|--------------------------------------------------|
| status   | 0x0           | RmiDevCommStatus | Status of device transaction                     |
| req_addr | 0x8           | Address          | Address of request buffer                        |
| rsp_addr | 0x10          | Address          | Address of response buffer                       |
| rsp_len  | 0x18          | UInt64           | Amount of valid data in response buffer in bytes |

Unused bits of the RmiDevCommEnter structure SBZ.

The RmiDevCommEnter structure is used in the following types:

- RmiDevCommData

## B4.6.19 RmiDevCommExit type

The RmiDevCommExit structure contains data passed from the RMM to the Host during device communication.

The RmiDevCommExit structure is a concrete type.

The width of the RmiDevCommExit structure is 256 ( 0x100 ) bytes.

See also:

- A9.5.2.1 Device communication exit data structure

The members of the RmiDevCommExit structure are shown in the following table.

| Name             | Byte offset   | Type                | Description                                                                                                  |
|------------------|---------------|---------------------|--------------------------------------------------------------------------------------------------------------|
| flags            | 0x0           | RmiDevCommExitFlags | Flags indicating action(s) which the Host is requested to perform                                            |
| req_cache_offset | 0x8           | UInt64              | If flags.req_cache is true, offset in the device request buffer to the start of data to be cached, in bytes  |
| req_cache_len    | 0x10          | UInt64              | If flags.req_cache is true, amount of device request data to be cached, in bytes                             |
| rsp_cache_offset | 0x18          | UInt64              | If flags.rsp_cache is true, offset in the device response buffer to the start of data to be cached, in bytes |
| rsp_cache_len    | 0x20          | UInt64              | If flags.rsp_cache is true, amount of device response data to be cached, in bytes                            |
| cache_object_id  | 0x28          | RmiDevCommObject    | If flags.req_cache is true and / or flags.rsp_cache is true, identifier for the object to be cached          |
| protocol         | 0x30          | RmiDevCommProtocol  | If flags.req_send is true, protocol to use                                                                   |
| req_delay        | 0x38          | UInt64              | If flags.req_send is true, amount of time to wait before sending the request, in microseconds.               |

DRAFT

| Name        | Byte offset   | Type   | Description                                                                                                                       |
|-------------|---------------|--------|-----------------------------------------------------------------------------------------------------------------------------------|
| req_len     | 0x40          | UInt64 | If flags.req_send is true, amount of valid data in request buffer in bytes                                                        |
| rsp_timeout | 0x48          | UInt64 | Amount of time to wait (measured from the most recent exit which had flags.rsp_reset = true) for device response in microseconds. |

Unused bits of the RmiDevCommExit structure MBZ.

The RmiDevCommExit structure is used in the following types:

- RmiDevCommData

## B4.6.20 RmiDevCommExitFlags type

The RmiDevCommExitFlags fieldset contains flags provided by the RMM during a device transaction.

The RmiDevCommExitFlags fieldset is a concrete type.

The width of the RmiDevCommExitFlags fieldset is 64 bits.

The fields of the RmiDevCommExitFlags fieldset are shown in the following diagram.

<!-- image -->

DRAFT

The fields of the RmiDevCommExitFlags fieldset are shown in the following table.

| Name      |   Bits | Description                                                                             | Value      |
|-----------|--------|-----------------------------------------------------------------------------------------|------------|
| req_cache |      0 | Whether the Host is requested to cache data from the device request buffer              | RmiBoolean |
| rsp_cache |      1 | Whether the Host is requested to cache data from the device response buffer             | RmiBoolean |
| req_send  |      2 | Whether the Host is requested to send data from the device request buffer to the device | RmiBoolean |
| rsp_wait  |      3 | Whether the RMMis waiting for a response from the device                                | RmiBoolean |
| rsp_reset |      4 | Whether to reset the response timer                                                     | RmiBoolean |

| Name        | Bits   | Description                                                                                                                                                 | Value      |
|-------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| multi       | 5      | Whether the device transaction contains more than one (device request, device response) tuple                                                               | RmiBoolean |
| stream_wait | 6      | Whether a transaction associated with another device, to which this device is connected via a PDEV stream, must proceed before this transaction can proceed | RmiBoolean |
|             | 63:7   | Reserved                                                                                                                                                    | MBZ        |

The RmiDevCommExitFlags fieldset is used in the following types:

- RmiDevCommExit

## B4.6.21 RmiDevCommObject type

The RmiDevCommObject enumeration represents identifier of a device communication object which the Host is requested to cache.

The RmiDevCommObject enumeration is a concrete type.

The width of the RmiDevCommObject enumeration is 8 bits.

The values of the RmiDevCommObject enumeration are shown in the following table.

|   Encoding | Name                     | Description                                    |
|------------|--------------------------|------------------------------------------------|
|          0 | RMI_DEV_NEGOTIATION_DATA | Negotiation data associated with a PDEV        |
|          1 | RMI_DEV_IDENTITY         | Device identity associated with a PDEV         |
|          2 | RMI_DEV_MEASUREMENTS     | Device measurements associated with a VDEV     |
|          3 | RMI_DEV_INTERFACE_REPORT | Device interface report associated with a VDEV |

DRAFT

Unused encodings for the RmiDevCommObject enumeration are reserved for use by future versions of this specification.

The RmiDevCommObject enumeration is used in the following types:

- RmiDevCommExit

## B4.6.22 RmiDevCommProtocol type

The RmiDevCommProtocol enumeration represents protocol used for device communication.

The RmiDevCommProtocol enumeration is a concrete type.

The width of the RmiDevCommProtocol enumeration is 8 bits.

The values of the RmiDevCommProtocol enumeration are shown in the following table.

|   Encoding | Name                     | Description                                                                  |
|------------|--------------------------|------------------------------------------------------------------------------|
|          0 | RMI_PROTOCOL_SPDM        | SPDM See Security Protocol and Data Model (SPDM) [21]                        |
|          1 | RMI_PROTOCOL_SECURE_SPDM | Secure SPDM See Secured Messages using SPDM Specification version 1.1.0 [17] |

Unused encodings for the RmiDevCommProtocol enumeration are reserved for use by future versions of this specification.

The RmiDevCommProtocol enumeration is used in the following types:

- RmiDevCommExit

## B4.6.23 RmiDevCommStatus type

The RmiDevCommStatus enumeration represents status passed from the Host to the RMM during device communication.

The RmiDevCommStatus enumeration is a concrete type.

The width of the RmiDevCommStatus enumeration is 8 bits.

The values of the RmiDevCommStatus enumeration are shown in the following table.

|   Encoding | Name                  | Description                                                                                                                                                                                                                                                        |
|------------|-----------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          0 | RMI_DEV_COMM_NONE     | No device response has been received from the device. Either: • The device transaction is PENDING, or • The device transaction is ACTIVE and no device response has been received from the device. The device transaction is ACTIVE and a device response has been |
|          1 | RMI_DEV_COMM_RESPONSE | received from the device. Either: • The device did not provide a device response within the expected time period, or                                                                                                                                               |
|          2 | RMI_DEV_COMM_ERROR    | • The device indicated an error.                                                                                                                                                                                                                                   |

DRAFT

Unused encodings for the RmiDevCommStatus enumeration are reserved for use by future versions of this specification.

The RmiDevCommStatus enumeration is used in the following types:

- RmiDevCommEnter

## B4.6.24 RmiEmulatedMmio type

The RmiEmulatedMmio enumeration represents whether the host has completed emulation for an Emulatable Abort.

The RmiEmulatedMmio enumeration is a concrete type.

The width of the RmiEmulatedMmio enumeration is 1 bits.

The values of the RmiEmulatedMmio enumeration are shown in the following table.

|   Encoding | Name                  | Description                                               |
|------------|-----------------------|-----------------------------------------------------------|
|          0 | RMI_NOT_EMULATED_MMIO | Host has not completed emulation for an Emulatable Abort. |
|          1 | RMI_EMULATED_MMIO     | Host has completed emulation for an Emulatable Abort.     |

The RmiEmulatedMmio enumeration is used in the following types:

- RmiRecEnterFlags

## B4.6.25 RmiFeature type

The RmiFeature enumeration represents whether a feature is supported or enabled.

The RmiFeature enumeration is a concrete type.

The width of the RmiFeature enumeration is 1 bits.

The values of the RmiFeature enumeration are shown in the following table.

| Encoding   | Name                               | Description                                                                                                                                                                 |
|------------|------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0 1        | RMI_FEATURE_FALSE RMI_FEATURE_TRUE | • During discovery: Feature is not supported. • During selection: Feature is not enabled. • During discovery: Feature is supported. • During selection: Feature is enabled. |

The RmiFeature enumeration is used in the following types:

- RmiVdevFlags
- RmiFeatureRegister2
- RmiFeatureRegister1
- RmiPdevFlags
- RmiRealmFlags0
- RmiPsmmuFlags
- RmiRealmFlags1
- RmiFeatureRegister3
- RmiFeatureRegister0

## B4.6.26 RmiFeatureRegister0 type

The RmiFeatureRegister0 fieldset contains RMI feature register 0.

The RmiFeatureRegister0 fieldset is a concrete type.

The width of the RmiFeatureRegister0 fieldset is 64 bits.

See also:

- Chapter A3 Feature discovery and configuration
- B4.5.14 RMI\_FEATURES command

The fields of the RmiFeatureRegister0 fieldset are shown in the following diagram.

DRAFT

The fields of the RmiFeatureRegister0 fieldset are shown in the following table.

| Name         | Bits   | Description                                                                                                                                                                                                                                 | Value      |
|--------------|--------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| S2SZ         | 7:0    | DRAFT Maximum Realm IPA width supported by the RMM. Specifies the input address size for stage 2 translation to be 2 ^ S2SZ . Note this format expresses the IPA width directly and is therefore different from the VTCR_EL2.T0SZ encoding. | UInt8      |
| LPA2         | 8      | Whether LPA2 is supported.                                                                                                                                                                                                                  | RmiFeature |
| SVE          | 9      | Whether SVE is supported.                                                                                                                                                                                                                   | RmiFeature |
| SVE_VL       | 13:10  | Maximum SVE vector length supported by the RMM. The effective vector length supported by the RMMis (SVE_VL + 1)*128 , similar to the value of ZCR_ELx.LEN .                                                                                 | UInt4      |
| NUM_BPS      | 19:14  | Number of breakpoints available, minus one. The value 0 is reserved.                                                                                                                                                                        | UInt6      |
| NUM_WPS      | 25:20  | Number of watchpoints available, minus one. The value 0 is reserved.                                                                                                                                                                        | UInt6      |
| PMU          | 26     | Whether PMU is supported                                                                                                                                                                                                                    | RmiFeature |
| PMU_NUM_CTRS | 31:27  | Number of PMU counters available                                                                                                                                                                                                            | UInt5      |
|              | 63:32  | Reserved                                                                                                                                                                                                                                    | MBZ        |

## B4.6.27 RmiFeatureRegister1 type

The RmiFeatureRegister1 fieldset contains RMI feature register 1.

The RmiFeatureRegister1 fieldset is a concrete type.

The width of the RmiFeatureRegister1 fieldset is 64 bits.

See also:

- Chapter A3 Feature discovery and configuration

- Chapter A11 Realm memory encryption
- B4.5.14 RMI\_FEATURES command

The fields of the RmiFeatureRegister1 fieldset are shown in the following diagram.

The fields of the RmiFeatureRegister1 fieldset are shown in the following table.

| Name             | Bits   | Description                                                                                                                                               | Value      |
|------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| RMI_GRAN_SZ_4KB  | 0      | Whether an RMI Granule size of 4KB is supported                                                                                                           | RmiFeature |
| RMI_GRAN_SZ_16KB | 1      | DRAFT Whether an RMI Granule size of 16KB is supported                                                                                                    | RmiFeature |
| RMI_GRAN_SZ_64KB | 2      | Whether an RMI Granule size of 64KB is supported                                                                                                          | RmiFeature |
| HASH_SHA_256     | 3      | Whether SHA-256 is supported                                                                                                                              | RmiFeature |
| HASH_SHA_384     | 4      | Whether SHA-384 is supported                                                                                                                              | RmiFeature |
| HASH_SHA_512     | 5      | Whether SHA-512 is supported                                                                                                                              | RmiFeature |
| MAX_RECS_ORDER   | 9:6    | Order of the maximum number of RECs which can be created per Realm. The maximum number of RECs is computed as follows: MAX_RECS = (2 ^ MAX_RECS_ORDER)- 1 | UInt4      |
| L0GPTSZ          | 13:10  | Value of Level 0 GPT entry size as encoded in GPCCR_EL3.L0GPTSZ.                                                                                          | Bits4      |
| PPS              | 16:14  | Value of Protected Physical Address Size as encoded in GPCCR_EL3.PPS.                                                                                     | Bits3      |
|                  | 63:17  | Reserved                                                                                                                                                  | MBZ        |

## B4.6.28 RmiFeatureRegister2 type

The RmiFeatureRegister2 fieldset contains RMI feature register 2.

The RmiFeatureRegister2 fieldset is a concrete type.

The width of the RmiFeatureRegister2 fieldset is 64 bits.

See also:

- Chapter A3 Feature discovery and configuration
- B4.5.14 RMI\_FEATURES command

The fields of the RmiFeatureRegister2 fieldset are shown in the following diagram.

The fields of the RmiFeatureRegister2 fieldset are shown in the following table.

| Name            | Bits   | Description                                                                                                                                                | Value      |
|-----------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| DA              | 0      | Whether Realm device assignment is supported                                                                                                               | RmiFeature |
| DA_COH          | 1      | Whether coherent device assignment is supported. If DA == RMI_FEATURE_FALSE, this flag should also be RMI_FEATURE_FALSE.                                   | RmiFeature |
| VSMMU           | 2      | Whether virtual SMMUis supported. If DA == RMI_FEATURE_FALSE, this flag should also be RMI_FEATURE_FALSE.                                                  | RmiFeature |
| ATS             | 3      | Whether ATS is supported. If DA == RMI_FEATURE_FALSE, this flag should also be RMI_FEATURE_FALSE.                                                          | RmiFeature |
| MAX_VDEVS_ORDER | 7:4    | Order of the maximum number of VDEVs which can be created per PDEV. The maximum number of VDEVs is computed as follows: MAX_VDEVS = (2^MAX_VDEVS_ORDER)- 1 | UInt4      |
| VDEV_KROU       | 8      | Whether VDEV key refresh on unlock is required                                                                                                             | RmiFeature |
| NON_TEE_STREAM  | 9      | Whether NON_TEE PDEV stream type is supported                                                                                                              | RmiFeature |
| P2P             | 10     | Whether peer-to-peer device communication is supported. If DA == RMI_FEATURE_FALSE, this flag should also be RMI_FEATURE_FALSE.                            | RmiFeature |

DRAFT

| Name         | Bits   | Description                                                | Value      |
|--------------|--------|------------------------------------------------------------|------------|
| CMEM_CXL     | 11     | Whether CXL type-3 coherent memory devices are supported   | RmiFeature |
| MAX_CMEM     | 19:12  | Maximum number of CMEMdevices.                             | UInt8      |
| CMEM_TSE_REQ | 20     | Whether Target-Side Encryption is required for CMEMdevices | RmiFeature |
|              | 63:21  | Reserved                                                   | MBZ        |

## B4.6.29 RmiFeatureRegister3 type

The RmiFeatureRegister3 fieldset contains RMI feature register 3.

The RmiFeatureRegister3 fieldset is a concrete type.

The width of the RmiFeatureRegister3 fieldset is 64 bits.

See also:

- Chapter A3 Feature discovery and configuration
- B4.5.14 RMI\_FEATURES command

The fields of the RmiFeatureRegister3 fieldset are shown in the following diagram.

<!-- image -->

DRAFT

The fields of the RmiFeatureRegister3 fieldset are shown in the following table.

| Name               | Bits   | Description                                                                                                                                    | Value              |
|--------------------|--------|------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| MAX_NUM_AUX_PLANES | 3:0    | Maximum number of auxiliary Planes                                                                                                             | UInt4              |
| RTT_PLANE          | 5:4    | RTT usage models supported for multi-Plane Realms. If only a single Plane is supported (that is, MAX_NUM_AUX_PLANES is 0), this field is RES0. | RmiRttPlaneFeature |
| RTT_S2AP_INDIRECT  | 6      | Whether S2AP indirect encoding is supported Reserved                                                                                           | RmiFeature MBZ     |
| RTT_S2AP_INDIRECT  | 63:7   |                                                                                                                                                |                    |

## B4.6.30 RmiFeatureRegister4 type

The RmiFeatureRegister4 fieldset contains RMI feature register 4.

The RmiFeatureRegister4 fieldset is a concrete type.

The width of the RmiFeatureRegister4 fieldset is 64 bits.

See also:

- Chapter A3 Feature discovery and configuration
- B4.5.14 RMI\_FEATURES command

The fields of the RmiFeatureRegister4 fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiFeatureRegister4 fieldset are shown in the following table.

| Name      | Bits   | Description     | Value   |
|-----------|--------|-----------------|---------|
| MEC_COUNT | 63:0   | Number of MECs. | UInt64  |

## B4.6.31 RmiForceP0 type

The RmiForceP0 enumeration represents whether to force control to return Plane 0.

The RmiForceP0 enumeration is a concrete type.

The width of the RmiForceP0 enumeration is 1 bits.

The values of the RmiForceP0 enumeration are shown in the following table.

|   Encoding | Name            | Description                                           |
|------------|-----------------|-------------------------------------------------------|
|          0 | RMI_NO_FORCE_P0 | Do not affect the Plane to which control is returned. |
|          1 | RMI_FORCE_P0    | Force control to return to Plane 0.                   |

DRAFT

The RmiForceP0 enumeration is used in the following types:

- RmiRecEnterFlags

## B4.6.32 RmiGranuleSize type

The RmiGranuleSize enumeration represents a Granule size.

The RmiGranuleSize enumeration is a concrete type.

The width of the RmiGranuleSize enumeration is 8 bits.

The values of the RmiGranuleSize enumeration are shown in the following table.

|   Encoding | Name                  | Description   |
|------------|-----------------------|---------------|
|          0 | RMI_GRANULE_SIZE_4KB  | 4KB.          |
|          1 | RMI_GRANULE_SIZE_16KB | 16KB.         |
|          2 | RMI_GRANULE_SIZE_64KB | 64KB.         |

Unused encodings for the RmiGranuleSize enumeration are reserved for use by future versions of this specification.

The RmiGranuleSize enumeration is used in the following types:

- RmiRmmConfig

## B4.6.33 RmiHashAlgorithm type

The RmiHashAlgorithm enumeration represents hash algorithm.

The RmiHashAlgorithm enumeration is a concrete type.

The width of the RmiHashAlgorithm enumeration is 8 bits.

The values of the RmiHashAlgorithm enumeration are shown in the following table.

|   Encoding | Name             | Description                                |
|------------|------------------|--------------------------------------------|
|          0 | RMI_HASH_SHA_256 | SHA-256 ( Secure Hash Standard (SHS) [25]) |
|          1 | RMI_HASH_SHA_512 | SHA-512 ( Secure Hash Standard (SHS) [25]) |
|          2 | RMI_HASH_SHA_384 | SHA-384 ( Secure Hash Standard (SHS) [25]) |

Unused encodings for the RmiHashAlgorithm enumeration are reserved for use by future versions of this specification.

The RmiHashAlgorithm enumeration is used in the following types:

- RmiRealmParams
- RmiPdevParams

## B4.6.34 RmiInjectSea type

The RmiInjectSea enumeration represents whether to inject a Synchronous External Abort into the Realm.

The RmiInjectSea enumeration is a concrete type.

The width of the RmiInjectSea enumeration is 1 bits.

The values of the RmiInjectSea enumeration are shown in the following table.

|   Encoding | Name              | Description                          |
|------------|-------------------|--------------------------------------|
|          0 | RMI_NO_INJECT_SEA | Do not inject an SEA into the Realm. |
|          1 | RMI_INJECT_SEA    | Inject an SEA into the Realm.        |

The RmiInjectSea enumeration is used in the following types:

- RmiRecEnterFlags

DRAFT

## B4.6.35 RmiInterfaceVersion type

The RmiInterfaceVersion fieldset contains an RMI interface version.

The RmiInterfaceVersion fieldset is a concrete type.

The width of the RmiInterfaceVersion fieldset is 64 bits.

See also:

- B4.1 RMI version
- B4.5.92 RMI\_VERSION command

The fields of the RmiInterfaceVersion fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiInterfaceVersion fieldset are shown in the following table.

| Name   | Bits   | Description                                                            | Value   |
|--------|--------|------------------------------------------------------------------------|---------|
| minor  | 15:0   | Interface minor version number (the value y in interface version x.y ) | UInt16  |
| major  | 30:16  | Interface major version number (the value x in interface version x.y ) | UInt15  |
|        | 63:31  | Reserved                                                               | MBZ     |

## B4.6.36 RmiLfaPolicy type

The RmiLfaPolicy enumeration represents a Live Firmware Activation policy.

The RmiLfaPolicy enumeration is a concrete type.

DRAFT

The width of the RmiLfaPolicy enumeration is 2 bits.

See also:

- A3.14 Live Firmware Activation

The values of the RmiLfaPolicy enumeration are shown in the following table.

|   Encoding | Name             | Description           |
|------------|------------------|-----------------------|
|          0 | RMI_LFA_DISALLOW | LFA is not permitted. |
|          1 | RMI_LFA_ALLOW    | LFA is permitted.     |

Unused encodings for the RmiLfaPolicy enumeration are reserved for use by future versions of this specification. The RmiLfaPolicy enumeration is used in the following types:

- RmiRealmFlags0

## B4.6.37 RmiMecPolicy type

The RmiMecPolicy enumeration represents a MEC policy.

The RmiMecPolicy enumeration is a concrete type.

The width of the RmiMecPolicy enumeration is 2 bits.

The values of the RmiMecPolicy enumeration are shown in the following table.

|   Encoding | Name                   | Description                                                                                                   |
|------------|------------------------|---------------------------------------------------------------------------------------------------------------|
|          0 | RMI_MEC_POLICY_SHARED  | The MEC protects memory owned by multiple Realms. A MEC with this policy may be referred to as a Shared MEC . |
|          1 | RMI_MEC_POLICY_PRIVATE | The MEC protects memory owned by a single Realm. A MEC with this policy may be referred to as a Private MEC . |

Unused encodings for the RmiMecPolicy enumeration are reserved for use by future versions of this specification.

The RmiMecPolicy enumeration is used in the following types:

- RmiRealmFlags0

## B4.6.38 RmiMemCategory type

The RmiMemCategory enumeration represents memory category.

The RmiMemCategory enumeration is a concrete type.

The width of the RmiMemCategory enumeration is 2 bits.

The values of the RmiMemCategory enumeration are shown in the following table.

|   Encoding | Name                          | Description                 |
|------------|-------------------------------|-----------------------------|
|          0 | RMI_MEM_CATEGORY_CONVENTIONAL | Conventional memory.        |
|          1 | RMI_MEM_CATEGORY_DEV_NCOH     | Device non-coherent memory. |
|          2 | RMI_MEM_CATEGORY_DEV_COH      | Device coherent memory.     |

DRAFT

Unused encodings for the RmiMemCategory enumeration are reserved for use by future versions of this specification.

## B4.6.39 RmiOpCanCancel type

The RmiOpCanCancel enumeration represents whether RMI operation can be cancelled.

The RmiOpCanCancel enumeration is a concrete type.

The width of the RmiOpCanCancel enumeration is 1 bits.

The values of the RmiOpCanCancel enumeration are shown in the following table.

|   Encoding | Name                 | Description                    |
|------------|----------------------|--------------------------------|
|          0 | RMI_OP_CANNOT_CANCEL | Operation cannot be cancelled. |

|   Encoding | Name              | Description                 |
|------------|-------------------|-----------------------------|
|          1 | RMI_OP_CAN_CANCEL | Operation can be cancelled. |

The RmiOpCanCancel enumeration is used in the following types:

- RmiResult
- RmiResultDataIncomplete

## B4.6.40 RmiOpMemContig type

The RmiOpMemContig enumeration represents RMI operation memory contiguity property.

The RmiOpMemContig enumeration is a concrete type.

The width of the RmiOpMemContig enumeration is 1 bits.

See also:

- B4.3.2 Stateful RMI operations

The values of the RmiOpMemContig enumeration are shown in the following table.

|   Encoding | Name                  | Description                                                                                |
|------------|-----------------------|--------------------------------------------------------------------------------------------|
|          0 | RMI_OP_MEM_NON_CONTIG | Base of each block is aligned to the block size. Blocks are not required to be contiguous. |
|          1 | RMI_OP_MEM_CONTIG     | A single contiguous region of memory, with the base aligned to the total size.             |

The RmiOpMemContig enumeration is used in the following types:

- RmiOpMemDonateReq

DRAFT

## B4.6.41 RmiOpMemDonateReq type

The RmiOpMemDonateReq fieldset contains RMI operation memory donation requirements.

The RmiOpMemDonateReq fieldset is a concrete type.

The width of the RmiOpMemDonateReq fieldset is 64 bits.

See also:

- B4.3.2 Stateful RMI operations

The fields of the RmiOpMemDonateReq fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiOpMemDonateReq fieldset are shown in the following table.

| Name   | Bits   | Description                                  | Value            |
|--------|--------|----------------------------------------------|------------------|
| size   | 1:0    | Size of each block                           | RmiAddrBlockSize |
| count  | 15:2   | Number of blocks required                    | UInt14           |
| contig | 16     | Whether blocks are required to be contiguous | RmiOpMemContig   |
| state  | 17     | Required initial state of memory             | RmiOpMemState    |
|        | 63:18  | Reserved                                     | SBZ              |

## B4.6.42 RmiOpMemReq type

The RmiOpMemReq enumeration represents RMI operation memory transfer requirements.

The RmiOpMemReq enumeration is a concrete type.

The width of the RmiOpMemReq enumeration is 2 bits.

See also:

- B4.3.2 Stateful RMI operations

The values of the RmiOpMemReq enumeration are shown in the following table.

|   Encoding | Name                   | Description                                        |
|------------|------------------------|----------------------------------------------------|
|          0 | RMI_OP_MEM_REQ_NONE    | RMI operation is not memory-transferring.          |
|          1 | RMI_OP_MEM_REQ_DONATE  | The RMI operation requires memory to be donated.   |
|          2 | RMI_OP_MEM_REQ_RECLAIM | The RMI operation requires memory to be reclaimed. |

Unused encodings for the RmiOpMemReq enumeration are reserved for use by future versions of this specification.

The RmiOpMemReq enumeration is used in the following types:

- RmiResult
- RmiResultDataIncomplete

DRAFT

## B4.6.43 RmiOpMemState type

The RmiOpMemState enumeration represents RMI operation memory state.

The RmiOpMemState enumeration is a concrete type.

The width of the RmiOpMemState enumeration is 1 bits.

The values of the RmiOpMemState enumeration are shown in the following table.

|   Encoding | Name                   | Description                                  |
|------------|------------------------|----------------------------------------------|
|          0 | RMI_OP_MEM_DELEGATED   | Initial state of memory is GRAN_DELEGATED.   |
|          1 | RMI_OP_MEM_UNDELEGATED | Initial state of memory is GRAN_UNDELEGATED. |

The RmiOpMemState enumeration is used in the following types:

- RmiAddrRangeDesc16KB
- RmiAddrRangeDesc4KB
- RmiAddrRangeDesc
- RmiAddrSetDesc
- RmiOpMemDonateReq
- RmiAddrRangeDesc64KB

## B4.6.44 RmiPdevCategory type

The RmiPdevCategory enumeration represents PDEV category.

The RmiPdevCategory enumeration is a concrete type.

The width of the RmiPdevCategory enumeration is 2 bits.

The values of the RmiPdevCategory enumeration are shown in the following table.

|   Encoding | Name                             | Description                          |
|------------|----------------------------------|--------------------------------------|
|          0 | RMI_PDEV_ROOT_PORT               | Root Port                            |
|          1 | RMI_PDEV_ENDPOINT_ACCEL_OFF_CHIP | Off-chip accelerator endpoint device |
|          2 | RMI_PDEV_ENDPOINT_ACCEL_ON_CHIP  | On-chip accelerator endpoint device  |
|          3 | RMI_PDEV_ENDPOINT_CMEM           | Coherent memory endpoint device      |

DRAFT

The RmiPdevCategory enumeration is used in the following types:

- RmiPdevFlags

## B4.6.45 RmiPdevFlags type

The RmiPdevFlags fieldset contains flags provided by the Host during PDEV creation.

The RmiPdevFlags fieldset is a concrete type.

The width of the RmiPdevFlags fieldset is 64 bits.

See also:

- A9.2.1 Physical device attributes
- B3.129 RmiPdevFlagsSupported function

The fields of the RmiPdevFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiPdevFlags fieldset are shown in the following table.

| Name     | Bits   | Description                                      | Value           |
|----------|--------|--------------------------------------------------|-----------------|
| spdm     | 0      | Whether communication with the device uses SPDM  | RmiPdevSpdm     |
| category | 2:1    | Device category                                  | RmiPdevCategory |
| p2p      | 3      | Whether this device can be added to a P2P stream | RmiFeature      |
|          | 63:4   | Reserved                                         | SBZ             |

The RmiPdevFlags fieldset is used in the following types:

- RmiPdevParams

## B4.6.46 RmiPdevParams type

The RmiPdevParams structure contains parameters provided by the Host during PDEV creation.

The RmiPdevParams structure is a concrete type.

The width of the RmiPdevParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiPdevParams structure are shown in the following table.

| Name       | Byte offset   | Type         | Description                                                                         |
|------------|---------------|--------------|-------------------------------------------------------------------------------------|
| flags      | 0x0           | RmiPdevFlags | Flags                                                                               |
| pdev_id    | 0x8           | Bits64       | Physical device identifier For a PCIe device: • This is the PCIe routing identifier |
| routing_id | 0x10          | Bits64       | • The value is in PCI BDF Routing identifier                                        |
| id_index   | 0x18          | UInt64       | Device identity index                                                               |

DRAFT

| Name            | Byte offset   | Type             | Description                                                                                                                                                     |
|-----------------|---------------|------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------|
| rid_base        | 0x20          | Bits16           | Base of requester ID range (inclusive). The value is in PCI BDF format.                                                                                         |
| rid_top         | 0x28          | Bits16           | Top of requester ID range (exclusive). The value is in PCI BDF format.                                                                                          |
| hash_algo       | 0x30          | RmiHashAlgorithm | Algorithm used to generate device digests                                                                                                                       |
| max_vdevs_order | 0x38          | UInt64           | Order of the maximum number of VDEVs which can be created for this PDEV. The maximum number of VDEVs is computed as follows: max_vdevs = (2^max_vdevs_order)- 1 |

Unused bits of the RmiPdevParams structure SBZ.

## B4.6.47 RmiPdevSpdm type

The RmiPdevSpdm enumeration represents whether communication with the device uses SPDM.

The RmiPdevSpdm enumeration is a concrete type.

The width of the RmiPdevSpdm enumeration is 1 bits.

See also:

- A9.1.2 Device properties

The values of the RmiPdevSpdm enumeration are shown in the following table.

|   Encoding | Name           | Description                                      |
|------------|----------------|--------------------------------------------------|
|          0 | RMI_SPDM_FALSE | Communication with the device does not use SPDM. |
|          1 | RMI_SPDM_TRUE  | Communication with the device uses SPDM.         |

DRAFT

The RmiPdevSpdm enumeration is used in the following types:

- RmiPdevFlags

## B4.6.48 RmiPdevState type

The RmiPdevState enumeration represents the state of a PDEV.

The RmiPdevState enumeration is a concrete type.

The width of the RmiPdevState enumeration is 8 bits.

The values of the RmiPdevState enumeration are shown in the following table.

|   Encoding | Name               | Description                  |
|------------|--------------------|------------------------------|
|          0 | RMI_PDEV_NEW       | Initial state of the device. |
|          1 | RMI_PDEV_NEEDS_KEY | RMMneeds device public key.  |

|   Encoding | Name             | Description                                                           |
|------------|------------------|-----------------------------------------------------------------------|
|          2 | RMI_PDEV_HAS_KEY | RMMhas device public key.                                             |
|          3 | RMI_PDEV_READY   | Secure connection between the RMMand the device has been established. |
|          4 | RMI_PDEV_STOPPED | Secure connection between the RMMand the device has been terminated.  |
|          5 | RMI_PDEV_ERROR   | Device has reported a fatal error.                                    |

Unused encodings for the RmiPdevState enumeration are reserved for use by future versions of this specification.

## B4.6.49 RmiPdevStreamFlags type

The RmiPdevStreamFlags fieldset contains flags provided by the Host during PDEV stream creation.

The RmiPdevStreamFlags fieldset is a concrete type.

The width of the RmiPdevStreamFlags fieldset is 64 bits.

The fields of the RmiPdevStreamFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiPdevStreamFlags fieldset are shown in the following table.

| Name   | Bits   | Description   | Value   |
|--------|--------|---------------|---------|
|        | 63:0   | Reserved      | SBZ     |

DRAFT

The RmiPdevStreamFlags fieldset is used in the following types:

- RmiPdevStreamParams

## B4.6.50 RmiPdevStreamParams type

The RmiPdevStreamParams structure contains parameters provided by the Host during PDEV stream creation.

The RmiPdevStreamParams structure is a concrete type.

The width of the RmiPdevStreamParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiPdevStreamParams structure are shown in the following table.

| Name        | Byte offset   | Type               | Description            |
|-------------|---------------|--------------------|------------------------|
| flags       | 0x0           | RmiPdevStreamFlags | Flags                  |
| stream_type | 0x8           | RmiPdevStreamType  | Stream type            |
| pdev_1      | 0x10          | Address            | Address of first PDEV. |
| pdev_2      | 0x18          | Address            | Address of second PDEV |

| Name           | Byte offset   | Type         | Description                     |
|----------------|---------------|--------------|---------------------------------|
| ide_sid        | 0x20          | UInt64       | IDE stream ID                   |
| num_addr_range | 0x28          | UInt64       | Number of device address ranges |
| addr_range[16] | 0x100         | RmiAddrRange | Device address range            |

Unused bits of the RmiPdevStreamParams structure SBZ.

## B4.6.51 RmiPdevStreamType type

The RmiPdevStreamType enumeration represents type of a PDEV stream.

The RmiPdevStreamType enumeration is a concrete type.

The width of the RmiPdevStreamType enumeration is 8 bits.

The values of the RmiPdevStreamType enumeration are shown in the following table.

|   Encoding | Name                     | Description                                                                           |
|------------|--------------------------|---------------------------------------------------------------------------------------|
|          0 | RMI_PDEV_STREAM_NON_TEE  | Non-TEE traffic.                                                                      |
|          1 | RMI_PDEV_STREAM_NCOH     | Non-coherent traffic between an upstream port and an endpoint device.                 |
|          2 | RMI_PDEV_STREAM_COH      | DRAFT Coherent traffic between an upstream port and an accelerator endpoint device.   |
|          3 | RMI_PDEV_STREAM_NCOH_SYS | Non-coherent traffic to an endpoint device which is protected by system construction. |
|          4 | RMI_PDEV_STREAM_COH_SYS  | Coherent traffic to an endpoint device which is protected by system construction.     |
|          5 | RMI_PDEV_STREAM_NCOH_P2P | Non-coherent traffic between two endpoint devices.                                    |
|          6 | RMI_PDEV_STREAM_COH_CMEM | Coherent traffic between an upstream port and aCMEM endpoint device.                  |

Unused encodings for the RmiPdevStreamType enumeration are reserved for use by future versions of this specification.

The RmiPdevStreamType enumeration is used in the following types:

- RmiPdevStreamParams

## B4.6.52 RmiPmuOverflowStatus type

The RmiPmuOverflowStatus enumeration represents PMU overflow status.

The RmiPmuOverflowStatus enumeration is a concrete type.

The width of the RmiPmuOverflowStatus enumeration is 8 bits.

The values of the RmiPmuOverflowStatus enumeration are shown in the following table.

|   Encoding | Name                        | Description                 |
|------------|-----------------------------|-----------------------------|
|          0 | RMI_PMU_OVERFLOW_NOT_ACTIVE | PMU overflow is not active. |
|          1 | RMI_PMU_OVERFLOW_ACTIVE     | PMU overflow is active.     |

Unused encodings for the RmiPmuOverflowStatus enumeration are reserved for use by future versions of this specification.

The RmiPmuOverflowStatus enumeration is used in the following types:

- RmiRecExit

## B4.6.53 RmiPsmmuAction type

The RmiPsmmuAction enumeration represents action required by Host in response to a PSMMU interrupt.

The RmiPsmmuAction enumeration is a concrete type.

The width of the RmiPsmmuAction enumeration is 1 bits.

The values of the RmiPsmmuAction enumeration are shown in the following table.

|   Encoding | Name Description                                               |
|------------|----------------------------------------------------------------|
|          0 | RMI_PSMMU_ACTION_NONE No action required.                      |
|          1 | RMI_PSMMU_ACTION_VIRQ Inject a virtual interrupt into a Realm. |

## B4.6.54 RmiPsmmuFlags type

The RmiPsmmuFlags fieldset contains flags provided by the Host during PSMMU activation.

The RmiPsmmuFlags fieldset is a concrete type.

The width of the RmiPsmmuFlags fieldset is 64 bits.

DRAFT

The fields of the RmiPsmmuFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiPsmmuFlags fieldset are shown in the following table.

| Name   | Bits   | Description           | Value      |
|--------|--------|-----------------------|------------|
| msi    | 0      | Whether to enable MSI | RmiFeature |
| ats    | 1      | Whether to enable ATS | RmiFeature |
| pri    | 2      | Whether to enable PRI | RmiFeature |
|        | 63:3   | Reserved              | SBZ        |

The RmiPsmmuFlags fieldset is used in the following types:

- RmiPsmmuParams

## B4.6.55 RmiPsmmuIrq type

The RmiPsmmuIrq enumeration represents identifies a single PSMMU IRQ.

The RmiPsmmuIrq enumeration is a concrete type.

The width of the RmiPsmmuIrq enumeration is 2 bits.

The values of the RmiPsmmuIrq enumeration are shown in the following table.

|   Encoding | Name                 | Description       |
|------------|----------------------|-------------------|
|          0 | RMI_PSMMU_IRQ_GERROR | GERROR interrupt. |
|          1 | RMI_PSMMU_IRQ_EVENTQ | EVENTQ interrupt. |
|          2 | RMI_PSMMU_IRQ_PRIQ   | PRIQ interrupt.   |
|          3 | RMI_PSMMU_IRQ_CMDQ   | CMDQ interrupt.   |

## B4.6.56 RmiPsmmuIrqResult type

The RmiPsmmuIrqResult fieldset contains flags which describe the result of triaging a PSMMU IRQ.

DRAFT

The RmiPsmmuIrqResult fieldset is a concrete type.

The width of the RmiPsmmuIrqResult fieldset is 64 bits.

The fields of the RmiPsmmuIrqResult fieldset are shown in the following diagram.

The fields of the RmiPsmmuIrqResult fieldset are shown in the following table.

| Name        | Bits   | Description                                                       | Value      |
|-------------|--------|-------------------------------------------------------------------|------------|
| pending     | 0      | Whether there are further PSMMU IRQs pending for processing       | RmiBoolean |
| vsmmu_event | 1      | Whether a VSMMU event needs to be handled by the Host             | RmiBoolean |
| smmu_event  | 2      | Whether an SMMUevent needs to be handled by the Host              | RmiBoolean |
| empty       | 3      | True if the queue for which the interrupt was raised is not empty | RmiBoolean |
|             | 63:4   | Reserved                                                          | SBZ        |

## B4.6.57 RmiPsmmuIrqSet type

The RmiPsmmuIrqSet fieldset contains identifies a set of pending PSMMU IRQs.

The RmiPsmmuIrqSet fieldset is a concrete type.

The width of the RmiPsmmuIrqSet fieldset is 64 bits.

The fields of the RmiPsmmuIrqSet fieldset are shown in the following diagram.

<!-- image -->

DRAFT

The fields of the RmiPsmmuIrqSet fieldset are shown in the following table.

| Name   | Bits   | Description                         | Value      |
|--------|--------|-------------------------------------|------------|
| gerror | 0      | Whether GERROR interrupt is pending | RmiBoolean |
| eventq | 1      | Whether EVENTQ interrupt is pending | RmiBoolean |
| priq   | 2      | Whether PRIQ interrupt is pending   | RmiBoolean |
| cmdq   | 3      | Whether CMDQ interrupt is pending   | RmiBoolean |
|        | 63:4   | Reserved                            | SBZ        |

## B4.6.58 RmiPsmmuParams type

The RmiPsmmuParams structure contains PSMMU parameters.

The RmiPsmmuParams structure is a concrete type.

The width of the RmiPsmmuParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiPsmmuParams structure are shown in the following table.

| Name        | Byte offset   | Type          | Description                                  |
|-------------|---------------|---------------|----------------------------------------------|
| flags       | 0x0           | RmiPsmmuFlags | Flags                                        |
| gerr_addr   | 0x8           | Address       | Physical MSI address of the GERROR interrupt |
| gerr_data   | 0x10          | Bits64        | Physical MSI data of the GERROR interrupt    |
| eventq_addr | 0x18          | Address       | Physical MSI address of the EVENTQ interrupt |
| eventq_data | 0x20          | Bits64        | Physical MSI data of the EVENTQ interrupt    |
| priq_addr   | 0x28          | Address       | Physical MSI address of the PRIQ interrupt   |
| priq_data   | 0x30          | Bits64        | Physical MSI data of the PRIQ interrupt      |

Unused bits of the RmiPsmmuParams structure SBZ.

## B4.6.59 RmiPublicKeyParams type

The RmiPublicKeyParams structure contains public key parameters.

The RmiPublicKeyParams structure is a concrete type.

The width of the RmiPublicKeyParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiPublicKeyParams structure are shown in the following table.

| Name           | Byte offset   | Type                  | Description                     |
|----------------|---------------|-----------------------|---------------------------------|
| key[1024]      | 0x0           | Bits8                 | Key data                        |
| metadata[1024] | 0x400         | Bits8                 | Key metadata                    |
| key_len        | 0x800         | UInt64                | Length of key data in bytes     |
| metadata_len   | 0x808         | UInt64                | Length of key metadata in bytes |
| algo           | 0x810         | RmiSignatureAlgorithm | Signature algorithm             |

DRAFT

Unused bits of the RmiPublicKeyParams structure SBZ.

## B4.6.60 RmiRealmFlags0 type

The RmiRealmFlags0 fieldset contains flags provided by the Host during Realm creation, which are reflected in Realm Initial Measurement.

The RmiRealmFlags0 fieldset is a concrete type.

The width of the RmiRealmFlags0 fieldset is 64 bits.

The fields of the RmiRealmFlags0 fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiRealmFlags0 fieldset are shown in the following table.

| Name       | Bits   | Description                                                                 | Value        |
|------------|--------|-----------------------------------------------------------------------------|--------------|
| lpa2       | 0      | Whether LPA2 is enabled                                                     | RmiFeature   |
| sve        | 1      | Whether SVE is enabled                                                      | RmiFeature   |
| pmu        | 2      | Whether PMU is enabled                                                      | RmiFeature   |
| da         | 3      | Whether Realm device assignment is enabled                                  | RmiFeature   |
|            | 4      | Reserved                                                                    | SBZ          |
| lfa_policy | 6:5    | DRAFT Live Firmware Activation policy for components within the Realm's TCB | RmiLfaPolicy |
| mec_policy | 8:7    | MEC policy                                                                  | RmiMecPolicy |
|            | 63:9   | Reserved                                                                    | SBZ          |

The RmiRealmFlags0 fieldset is used in the following types:

- RmiRealmParams

## B4.6.61 RmiRealmFlags1 type

The RmiRealmFlags1 fieldset contains flags provided by the Host during Realm creation, which are not reflected in Realm Initial Measurement.

The RmiRealmFlags1 fieldset is a concrete type.

The width of the RmiRealmFlags1 fieldset is 64 bits.

The fields of the RmiRealmFlags1 fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRealmFlags1 fieldset are shown in the following table.

| Name               | Bits   | Description                                                                                                                                                                       | Value              |
|--------------------|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------|
| rtt_tree_per_plane | 0      | DRAFT RMI_FEATURE_FALSE: all Planes share a single RTT tree RMI_FEATURE_TRUE: each Plane has a separate RTT tree If the Realm has no auxiliary Planes then this field is ignored. | RmiFeature         |
| rtt_s2ap_encoding  | 1      | S2AP encoding                                                                                                                                                                     | RmiRttS2APEncoding |
| ats                | 2      | Whether Address Translation Service is supported for devices assigned to the Realm                                                                                                | RmiFeature         |
|                    | 63:3   | Reserved                                                                                                                                                                          | SBZ                |

The RmiRealmFlags1 fieldset is used in the following types:

- RmiRealmParams

## B4.6.62 RmiRealmParams type

The RmiRealmParams structure contains parameters provided by the Host during Realm creation.

The RmiRealmParams structure is a concrete type.

The width of the RmiRealmParams structure is 4096 ( 0x1000 ) bytes.

See also:

- A2.2.6 Realm parameters
- B4.5.46 RMI\_REALM\_CREATE command

The members of the RmiRealmParams structure are shown in the following table.

| Name   | Byte offset   | Type           | Description   |
|--------|---------------|----------------|---------------|
| flags0 | 0x0           | RmiRealmFlags0 | Flags         |

| Name            | Byte offset   | Type                   | Description                                                                                                                                                                                        |
|-----------------|---------------|------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| s2sz            | 0x8           | UInt8                  | IPA width. Specifies the input address size for stage 2 translation to be 2 ^ S2SZ . Note this format expresses the IPA width directly and is therefore different from the VTCR_EL2.T0SZ encoding. |
| sve_vl          | 0x10          | UInt8                  | SVE vector length. The effective vector length requested is (sve_vl + 1)*128 , similar to the value of ZCR_ELx.LEN .                                                                               |
| num_bps         | 0x18          | UInt8                  | Number of breakpoints, minus one. The value 0 is reserved.                                                                                                                                         |
| num_wps         | 0x20          | UInt8                  | Number of watchpoints, minus one. The value 0 is reserved.                                                                                                                                         |
| pmu_num_ctrs    | 0x28          | UInt8                  | Number of PMU counters                                                                                                                                                                             |
| hash_algo       | 0x30          | DRAFT RmiHashAlgorithm | Algorithm used to measure the initial state of the Realm                                                                                                                                           |
| num_aux_planes  | 0x38          | UInt64                 | Number of auxiliary Planes                                                                                                                                                                         |
| rpv             | 0x400         | Bits512                | Realm Personalization Value                                                                                                                                                                        |
| ats_plane       | 0x440         | UInt64                 | Index of Plane whose stage 2 permissions are observed by ATS requests from devices assigned to the Realm                                                                                           |
| rtt_base        | 0x808         | Address                | Base address of primary RTT                                                                                                                                                                        |
| rtt_level_start | 0x810         | Int64                  | RTT starting level                                                                                                                                                                                 |
| rtt_num_start   | 0x818         | UInt32                 | Number of starting level RTTs                                                                                                                                                                      |
| flags1          | 0x820         | RmiRealmFlags1         | Flags                                                                                                                                                                                              |
| aux_rtt_base[3] | 0xf80         | Address                | Base address of auxiliary RTTs                                                                                                                                                                     |

Unused bits of the RmiRealmParams structure SBZ.

## B4.6.63 RmiRecCreateFlags type

The RmiRecCreateFlags fieldset contains flags provided by the Host during REC creation.

The RmiRecCreateFlags fieldset is a concrete type.

The width of the RmiRecCreateFlags fieldset is 64 bits.

The fields of the RmiRecCreateFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRecCreateFlags fieldset are shown in the following table.

| Name     | Bits   | Description                           | Value          |
|----------|--------|---------------------------------------|----------------|
| runnable | 0      | Whether REC is eligible for execution | RmiRecRunnable |
|          | 63:1   | Reserved                              | SBZ            |

The RmiRecCreateFlags fieldset is used in the following types:

- RmiRecParams

## B4.6.64 RmiRecEnter type

The RmiRecEnter structure contains data passed from the Host to the RMM on REC entry.

The RmiRecEnter structure is a concrete type.

The width of the RmiRecEnter structure is 2048 ( 0x800 ) bytes.

## See also:

- A4.2.1 RmiRecEnter object
- B4.5.51 RMI\_REC\_ENTER command
- B4.6.66 RmiRecExit type

The members of the RmiRecEnter structure are shown in the following table.

| Name     | Byte offset   | Type             | Description   |
|----------|---------------|------------------|---------------|
| flags    | 0x0           | RmiRecEnterFlags | Flags         |
| gprs[31] | 0x200         | Bits64           | Registers     |

Unused bits of the RmiRecEnter structure SBZ.

The RmiRecEnter structure is used in the following types:

- RmiRecRun

DRAFT

## B4.6.65 RmiRecEnterFlags type

The RmiRecEnterFlags fieldset contains flags provided by the Host during REC entry.

The RmiRecEnterFlags fieldset is a concrete type.

The width of the RmiRecEnterFlags fieldset is 64 bits.

The fields of the RmiRecEnterFlags fieldset are shown in the following diagram.

The fields of the RmiRecEnterFlags fieldset are shown in the following table.

| Name             | Bits   | Description                                                           | Value           |
|------------------|--------|-----------------------------------------------------------------------|-----------------|
| emul_mmio        | 0      | Whether the host has completed emulation for an Emulatable Data Abort | RmiEmulatedMmio |
| inject_sea       | 1      | Whether to inject a Synchronous External Abort into the Realm.        | RmiInjectSea    |
| trap_wfi         | 2      | Whether to trap WFI execution by the Realm.                           | RmiTrap         |
| trap_wfe         | 3      | Whether to trap WFE execution by the Realm.                           | RmiTrap         |
| ripas_response   | 4      | Host response to RIPAS change request.                                | RmiResponse     |
| s2ap_response    | 5      | Host response to S2AP change request.                                 | RmiResponse     |
| dev_mem_response | 6      | Host response to VDEV mapping validation request.                     | RmiResponse     |
| force_p0         | 7      | Whether to force control to return Plane 0                            | RmiForceP0      |
|                  | 63:8   | Reserved                                                              | SBZ             |

DRAFT

The RmiRecEnterFlags fieldset is used in the following types:

- RmiRecEnter

## B4.6.66 RmiRecExit type

The RmiRecExit structure contains data passed from the RMM to the Host on REC exit.

The RmiRecExit structure is a concrete type.

The width of the RmiRecExit structure is 2048 ( 0x800 ) bytes.

See also:

- A4.3.1 RmiRecExit object
- B4.5.51 RMI\_REC\_ENTER command
- B4.6.64 RmiRecEnter type

The members of the RmiRecExit structure are shown in the following table.

| Name           | Byte offset   | Type                 | Description                                              |
|----------------|---------------|----------------------|----------------------------------------------------------|
| exit_reason    | 0x0           | RmiRecExitReason     | Exit reason                                              |
| esr            | 0x100         | Bits64               | Exception Syndrome Register                              |
| far            | 0x108         | Bits64               | Fault Address Register                                   |
| hpfar          | 0x110         | Bits64               | Hypervisor IPA Fault Address register                    |
| rtt_tree       | 0x118         | UInt64               | Index of RTT tree active at time of the exit             |
| gprs[31]       | 0x200         | Bits64               | Registers                                                |
| cntp_ctl       | 0x400         | Bits64               | Counter-timer Physical Timer Control Register value      |
| cntp_cval      | 0x408         | Bits64               | Counter-timer Physical Timer CompareValue Register value |
| cntv_ctl       | 0x410         | Bits64               | Counter-timer Virtual Timer Control Register value       |
| cntv_cval      | 0x418         | Bits64               | Counter-timer Virtual Timer CompareValue Register value  |
| ripas_base     | 0x500         | Bits64               | Base IPA of target region for pending RIPAS change       |
| ripas_top      | 0x508         | DRAFT Bits64         | Top IPA of target region for pending RIPAS change        |
| ripas_value    | 0x510         | RmiRipas             | RIPAS value of pending RIPAS change                      |
| s2ap_base      | 0x520         | Bits64               | Base IPA of target region for pending S2AP change        |
| s2ap_top       | 0x528         | Bits64               | Top IPA of target region for pending S2AP change         |
| vdev_id_1      | 0x530         | Bits64               | Virtual device ID 1                                      |
| vdev_id_2      | 0x538         | Bits64               | Virtual device ID 2                                      |
| dev_mem_base   | 0x540         | Bits64               | Base IPA of target region for VDEV mapping validation    |
| dev_mem_top    | 0x548         | Bits64               | Top IPA of target region for VDEV mapping validation     |
| dev_mem_pa     | 0x550         | Address              | Base PA of device memory region                          |
| imm            | 0x600         | Bits16               | Host call immediate value                                |
| plane          | 0x608         | UInt64               | Plane index                                              |
| pmu_ovf_status | 0x700         | RmiPmuOverflowStatus | PMU overflow status                                      |
| vsmmu          | 0x710         | Address              | Virtual SMMUbase IPA                                     |

Unused bits of the RmiRecExit structure MBZ.

The RmiRecExit structure is used in the following types:

- RmiRecRun

## B4.6.67 RmiRecExitReason type

The RmiRecExitReason enumeration represents the reason for a REC exit.

The RmiRecExitReason enumeration is a concrete type.

The width of the RmiRecExitReason enumeration is 8 bits.

The values of the RmiRecExitReason enumeration are shown in the following table.

|   Encoding | Name                                 | Description                             |
|------------|--------------------------------------|-----------------------------------------|
|          0 | RMI_EXIT_SYNC                        | REC exit due to synchronous exception   |
|          1 | RMI_EXIT_IRQ                         | REC exit due to IRQ                     |
|          2 | RMI_EXIT_FIQ                         | REC exit due to FIQ                     |
|          3 | RMI_EXIT_PSCI                        | REC exit due to PSCI                    |
|          4 | RMI_EXIT_RIPAS_CHANGE                | REC exit due to RIPAS change pending    |
|          5 | RMI_EXIT_HOST_CALL                   | REC exit due to Host call               |
|          6 | RMI_EXIT_SERROR                      | REC exit due to SError                  |
|          7 | RMI_EXIT_S2AP_CHANGE                 | REC exit due to S2AP change pending     |
|          8 | RMI_EXIT_VDEV_REQUEST                | REC exit due to VDEV request            |
|          9 | DRAFT RMI_EXIT_VDEV_VALIDATE_MAPPING | REC exit due to VDEV mapping validation |
|         10 | RMI_EXIT_VSMMU_COMMAND               | REC exit due to VSMMU command           |
|         11 | RMI_EXIT_VDEV_P2P_BINDING            | REC exit due to VDEV P2P binding        |

Unused encodings for the RmiRecExitReason enumeration are reserved for use by future versions of this specification.

The RmiRecExitReason enumeration is used in the following types:

- RmiRecExit

## B4.6.68 RmiRecMpidr type

The RmiRecMpidr fieldset contains MPIDR value which identifies a REC.

The RmiRecMpidr fieldset is a concrete type.

The width of the RmiRecMpidr fieldset is 64 bits.

## See also:

- A2.4.3 REC index and MPIDR value
- B4.5.49 RMI\_REC\_CREATE command

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

The RmiRecMpidr fieldset is used in the following types:

- RmiRecParams

## B4.6.69 RmiRecParams type

The RmiRecParams structure contains parameters provided by the Host during REC creation.

The RmiRecParams structure is a concrete type.

The width of the RmiRecParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiRecParams structure are shown in the following table.

| Name    | Byte offset   | Type              | Description               |
|---------|---------------|-------------------|---------------------------|
| flags   | 0x0           | RmiRecCreateFlags | Flags                     |
| mpidr   | 0x100         | RmiRecMpidr       | MPIDR of the REC          |
| pc      | 0x200         | Bits64            | Program counter           |
| gprs[8] | 0x300         | Bits64            | General-purpose registers |

DRAFT

Unused bits of the RmiRecParams structure SBZ.

## B4.6.70 RmiRecRun type

The RmiRecRun structure contains fields used to share information between RMM and Host during REC entry and REC exit.

The RmiRecRun structure is a concrete type.

The width of the RmiRecRun structure is 4096 ( 0x1000 ) bytes.

See also:

- A4.2.1 RmiRecEnter object
- A4.3.1 RmiRecExit object

- B4.5.51 RMI\_REC\_ENTER command

The members of the RmiRecRun structure are shown in the following table.

| Name   | Byte offset   | Type        | Description       |
|--------|---------------|-------------|-------------------|
| enter  | 0x0           | RmiRecEnter | Entry information |
| exit   | 0x800         | RmiRecExit  | Exit information  |

## B4.6.71 RmiRecRunnable type

The RmiRecRunnable enumeration represents whether a REC is eligible for execution.

The RmiRecRunnable enumeration is a concrete type.

The width of the RmiRecRunnable enumeration is 1 bits.

The values of the RmiRecRunnable enumeration are shown in the following table.

|   Encoding | Name             | Description                 |
|------------|------------------|-----------------------------|
|          0 | RMI_NOT_RUNNABLE | Not eligible for execution. |
|          1 | RMI_RUNNABLE     | Eligible for execution.     |

The RmiRecRunnable enumeration is used in the following types:

- RmiRecCreateFlags

## B4.6.72 RmiResponse type

The RmiResponse enumeration represents whether the Host accepted or rejected a Realm request.

The RmiResponse enumeration is a concrete type.

DRAFT

The width of the RmiResponse enumeration is 1 bits.

The values of the RmiResponse enumeration are shown in the following table.

|   Encoding | Name                | Description                      |
|------------|---------------------|----------------------------------|
|          0 | RMI_RESPONSE_ACCEPT | Host accepted the Realm request. |
|          1 | RMI_RESPONSE_REJECT | Host rejected the Realm request. |

The RmiResponse enumeration is used in the following types:

- RmiRecEnterFlags

## B4.6.73 RmiResult type

The RmiResult fieldset contains a return code from an RMI command.

The RmiResult fieldset is a concrete type.

The width of the RmiResult fieldset is 64 bits.

See also:

- Chapter B1 Commands

The fields of the RmiResult fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiResult fieldset are shown in the following table.

| Name   | Bits   | Description           | Value         |
|--------|--------|-----------------------|---------------|
| status | 7:0    | Status of the command | RmiStatusCode |
| data   | 63:8   | Conditional           | See below     |

Encodings for field data:

<!-- image -->

| Name             | Condition                                                                                                                     | Fieldset                                   |
|------------------|-------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------|
| incomplete level | DRAFT status == RMI_INCOMPLETE status IN { RMI_ERROR_DPT, RMI_ERROR_RTT, RMI_ERROR_RTT_AUX, RMI_ERROR_PSMMU_ST } !status IN { | RmiResultDataIncomplete RmiResultDataLevel |
| null             | RMI_ERROR_DPT, RMI_ERROR_RTT, RMI_ERROR_RTT_AUX, RMI_ERROR_PSMMU_ST, RMI_INCOMPLETE }                                         | RmiResultDataNull                          |

## B4.6.74 RmiResultDataIncomplete type

The RmiResultDataIncomplete fieldset contains encoding for additional data from an RMI command which returned RMI\_INCOMPLETE.

The RmiResultDataIncomplete fieldset is a concrete type.

The width of the RmiResultDataIncomplete fieldset is 56 bits.

The fields of the RmiResultDataIncomplete fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiResultDataIncomplete fieldset are shown in the following table.

| Name   | Bits   | Description                        | Value          |
|--------|--------|------------------------------------|----------------|
| mem    | 1:0    | Memory transfer requirements       | RmiOpMemReq    |
| cancel | 2      | Whether operation can be cancelled | RmiOpCanCancel |
|        | 55:3   | Reserved                           | MBZ            |

The RmiResultDataIncomplete fieldset is used in the following types:

- RmiResult

## B4.6.75 RmiResultDataLevel type

The RmiResultDataLevel fieldset contains encoding for additional data from an RMI command which indicates a level.

The RmiResultDataLevel fieldset is a concrete type.

The width of the RmiResultDataLevel fieldset is 56 bits.

The fields of the RmiResultDataLevel fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiResultDataLevel fieldset are shown in the following table.

| Name   | Bits   | Description                                                         | Value   |
|--------|--------|---------------------------------------------------------------------|---------|
| level  | 7:0    | Level at which access to a table or other data structure terminated | UInt8   |
|        | 55:8   | Reserved                                                            | MBZ     |

DRAFT

The RmiResultDataLevel fieldset is used in the following types:

- RmiResult

## B4.6.76 RmiResultDataNull type

The RmiResultDataNull fieldset contains encoding for null additional data from an RMI command.

The RmiResultDataNull fieldset is a concrete type.

The width of the RmiResultDataNull fieldset is 56 bits.

The fields of the RmiResultDataNull fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiResultDataNull fieldset are shown in the following table.

| Name   | Bits   | Description   | Value   |
|--------|--------|---------------|---------|
|        | 55:0   | Reserved      | MBZ     |

The RmiResultDataNull fieldset is used in the following types:

- RmiResult

## B4.6.77 RmiRipas type

The RmiRipas enumeration represents realm IPA state.

The RmiRipas enumeration is a concrete type.

The width of the RmiRipas enumeration is 8 bits.

The values of the RmiRipas enumeration are shown in the following table.

|   Encoding | Name                | Description                                                                    |
|------------|---------------------|--------------------------------------------------------------------------------|
|          0 | RMI_RIPAS_EMPTY     | Address where no Realm resources are mapped.                                   |
|          1 | RMI_RIPAS_RAM       | Address where private code or data owned by the Realm is mapped.               |
|          2 | RMI_RIPAS_DESTROYED | Address which is inaccessible to the Realm due to an action taken by the Host. |
|          3 | RMI_RIPAS_DEV       | Address where memory of an assigned Realm device is mapped.                    |

Unused encodings for the RmiRipas enumeration are reserved for use by future versions of this specification.

The RmiRipas enumeration is used in the following types:

- RmiRecExit

## B4.6.78 RmiRmmConfig type

The RmiRmmConfig structure contains global configuration of the RMM.

The RmiRmmConfig structure is a concrete type.

The width of the RmiRmmConfig structure is 4096 ( 0x1000 ) bytes.

DRAFT

The members of the RmiRmmConfig structure are shown in the following table.

| Name                     | Byte offset              | Type           | Description                                                                                                                                                                                                                                                                                                                                                            |
|--------------------------|--------------------------|----------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| tracking_region_size 0x0 | tracking_region_size 0x0 | UInt8          | Tracking region size The encoding of this value depends on the RMI Granule size, as follows: RMI Granule size = 4KB • 0: Tracking region size = 1GB RMI Granule size = 16KB • 0: Tracking region size = 32MB • 1: Tracking region size = 64GB RMI Granule size = 64KB • 0: Tracking region size = 512MB • 1: Tracking region size = 4TB All other values are reserved. |
| rmi_granule_size         | 0x8                      | RmiGranuleSize | RMI Granule size                                                                                                                                                                                                                                                                                                                                                       |

Unused bits of the RmiRmmConfig structure SBZ.

## B4.6.79 RmiRttAddrType type

The RmiRttAddrType enumeration represents meaning of an address value which is the input or output of an RTT command.

The RmiRttAddrType enumeration is a concrete type.

The width of the RmiRttAddrType enumeration is 2 bits.

The values of the RmiRttAddrType enumeration are shown in the following table.

|   Encoding | Name                 | Description                                                                                  |
|------------|----------------------|----------------------------------------------------------------------------------------------|
|          0 | RMI_ADDR_TYPE_NONE   | Address value is ignored                                                                     |
|          1 | RMI_ADDR_TYPE_SINGLE | Address value is a single RMI Address Range Descriptor                                       |
|          2 | RMI_ADDR_TYPE_LIST   | Address value is the address of a Granule that holds a list of RMI Address Range Descriptors |

Unused encodings for the RmiRttAddrType enumeration are reserved for use by future versions of this specification.

The RmiRttAddrType enumeration is used in the following types:

- RmiRttUnprotMapFlags
- RmiRttUnmapFlags
- RmiRttProtMapFlags

## B4.6.80 RmiRttAuxBlock type

The RmiRttAuxBlock enumeration represents control behaviour of auxiliary RTT mapping operation when target IPA range is a subset of a block mapping in the auxiliary RTT tree.

The RmiRttAuxBlock enumeration is a concrete type.

The width of the RmiRttAuxBlock enumeration is 1 bits.

The values of the RmiRttAuxBlock enumeration are shown in the following table.

DRAFT

|   Encoding | Name                        | Description                                             |
|------------|-----------------------------|---------------------------------------------------------|
|          0 | RMI_RTT_AUX_BLOCK_NO_CREATE | Do not create a block mapping in the auxiliary RTT tree |
|          1 | RMI_RTT_AUX_BLOCK_CREATE    | Create a block mapping in the auxiliary RTT tree        |

The RmiRttAuxBlock enumeration is used in the following types:

- RmiRttAuxMapFlags

## B4.6.81 RmiRttAuxInvalidPri type

The RmiRttAuxInvalidPri enumeration represents control behaviour of auxiliary RTT mapping operation when primary RTTE is invalid.

The RmiRttAuxInvalidPri enumeration is a concrete type.

The width of the RmiRttAuxInvalidPri enumeration is 1 bits.

The values of the RmiRttAuxInvalidPri enumeration are shown in the following table.

|   Encoding | Name                             | Description                                              |
|------------|----------------------------------|----------------------------------------------------------|
|          0 | RMI_RTT_AUX_INVALID_PRI_STOP     | Stop the operation and return an error to the caller     |
|          1 | RMI_RTT_AUX_INVALID_PRI_CONTINUE | Set auxiliary RTTE to invalid and continue the operation |

The RmiRttAuxInvalidPri enumeration is used in the following types:

- RmiRttAuxMapFlags

## B4.6.82 RmiRttAuxMapFlags type

The RmiRttAuxMapFlags fieldset contains flags provided by the Host to commands which create mappings in an auxiliary RTT tree.

The RmiRttAuxMapFlags fieldset is a concrete type.

The width of the RmiRttAuxMapFlags fieldset is 64 bits.

The fields of the RmiRttAuxMapFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRttAuxMapFlags fieldset are shown in the following table.

| Name        | Bits   | Description                                                                                      | Value               |
|-------------|--------|--------------------------------------------------------------------------------------------------|---------------------|
| tree_index  | 1:0    | Index of auxiliary RTT tree                                                                      | UInt2               |
| block       | 2      | Control behaviour when target IPA range is a subset of a block mapping in the auxiliary RTT tree | RmiRttAuxBlock      |
| invalid_pri | 3      | Control behaviour when primary RTTE is invalid                                                   | RmiRttAuxInvalidPri |
|             | 63:4   | Reserved                                                                                         | SBZ                 |

## B4.6.83 RmiRttAuxUnmapFlags type

The RmiRttAuxUnmapFlags fieldset contains flags provided by the Host to commands which remove mappings in an auxiliary RTT tree.

The RmiRttAuxUnmapFlags fieldset is a concrete type.

The width of the RmiRttAuxUnmapFlags fieldset is 64 bits.

The fields of the RmiRttAuxUnmapFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiRttAuxUnmapFlags fieldset are shown in the following table.

| Name       | Bits   | Description                 | Value   |
|------------|--------|-----------------------------|---------|
| tree_index | 1:0    | Index of auxiliary RTT tree | UInt2   |
|            | 63:2   | Reserved                    | SBZ     |

## B4.6.84 RmiRttEntryState type

The RmiRttEntryState enumeration represents the state of an RTTE.

The RmiRttEntryState enumeration is a concrete type.

The width of the RmiRttEntryState enumeration is 8 bits.

DRAFT

The values of the RmiRttEntryState enumeration are shown in the following table.

|   Encoding | Name                   | Description                                                                                                                                                                                       |
|------------|------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          0 | RMI_RTTE_VOID          | This RTTE is not associated with any Granule.                                                                                                                                                     |
|          1 | RMI_RTTE_DATA          | The output address of this RTTE points to: • a DATA Granule, if the input address is a Protected IPA, or • any Granule-aligned address within NS PAS, if the input address is an Unprotected IPA. |
|          2 | RMI_RTTE_TABLE         | The output address of this RTTE points to the next-level RTT.                                                                                                                                     |
|          3 | RMI_RTTE_NARCH_DEV     | The output address of this RTTE points to an GRAN_DEV Granule.                                                                                                                                    |
|          4 | RMI_RTTE_AUX_DESTROYED | An auxiliary RTT was destroyed.                                                                                                                                                                   |
|          5 | RMI_RTTE_ARCH_DEV      | The output address of this RTTE points to a VSMMU Granule.                                                                                                                                        |

Unused encodings for the RmiRttEntryState enumeration are reserved for use by future versions of this specification.

## B4.6.85 RmiRttPlaneFeature type

The RmiRttPlaneFeature enumeration represents RTT usage models supported for multi-Plane Realms.

The RmiRttPlaneFeature enumeration is a concrete type.

The width of the RmiRttPlaneFeature enumeration is 2 bits.

See also:

- A3.12 Support for auxiliary Planes

The values of the RmiRttPlaneFeature enumeration are shown in the following table.

|   Encoding | Name                     | Description                                                                         |
|------------|--------------------------|-------------------------------------------------------------------------------------|
|          0 | RMI_RTT_PLANE_AUX        | A multi-Plane Realm uses auxiliary RTTs                                             |
|          1 | RMI_RTT_PLANE_AUX_SINGLE | A multi-Plane Realm can be configured to either use auxiliary RTTs, or a single RTT |
|          2 | RMI_RTT_PLANE_SINGLE     | A multi-Plane Realm uses a single RTT                                               |

Unused encodings for the RmiRttPlaneFeature enumeration are reserved for use by future versions of this specification.

The RmiRttPlaneFeature enumeration is used in the following types:

- RmiFeatureRegister3

## B4.6.86 RmiRttProtMapFlags type

The RmiRttProtMapFlags fieldset contains flags provided by the Host to commands which create mappings in Protected IPA space.

The RmiRttProtMapFlags fieldset is a concrete type.

The width of the RmiRttProtMapFlags fieldset is 64 bits.

DRAFT

The fields of the RmiRttProtMapFlags fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiRttProtMapFlags fieldset are shown in the following table.

| Name       | Bits   | Description                                                                                                | Value          |
|------------|--------|------------------------------------------------------------------------------------------------------------|----------------|
| oaddr_type | 1:0    | Type of oaddr input value                                                                                  | RmiRttAddrType |
| list_count | 15:2   | Number of valid entries in the oaddr list. If paddr_type != RMI_ADDR_TYPE_LIST then this field is ignored. | UInt14         |
|            | 63:16  | Reserved                                                                                                   | SBZ            |

## B4.6.87 RmiRttS2APBase type

The RmiRttS2APBase enumeration represents S2AP base value.

The RmiRttS2APBase enumeration is a concrete type.

The width of the RmiRttS2APBase enumeration is 4 bits.

The values of the RmiRttS2APBase enumeration are shown in the following table.

|   Encoding | Name               | Description   |
|------------|--------------------|---------------|
|          0 | RMI_S2AP_NO_ACCESS | NoAccess      |
|          1 | RMI_S2AP_RO        | RO            |
|          2 | RMI_S2AP_WO        | WO            |
|          3 | RMI_S2AP_RW        | RW            |
|          4 | RMI_S2AP_RW_PUX    | RW+puX        |

Unused encodings for the RmiRttS2APBase enumeration are reserved for use by future versions of this specification.

DRAFT

## B4.6.88 RmiRttS2APEncoding type

The RmiRttS2APEncoding enumeration represents S2AP encoding.

The RmiRttS2APEncoding enumeration is a concrete type.

The width of the RmiRttS2APEncoding enumeration is 1 bits.

See also:

- A3.13 Support for Stage 2 Access Permissions indirect encoding

The values of the RmiRttS2APEncoding enumeration are shown in the following table.

|   Encoding | Name              | Description                                                   |
|------------|-------------------|---------------------------------------------------------------|
|          0 | RMI_S2AP_DIRECT   | S2AP is encoded directly in the RTT entry.                    |
|          1 | RMI_S2AP_INDIRECT | RTT entry includes indices which indirectly specify the S2AP. |

The RmiRttS2APEncoding enumeration is used in the following types:

- RmiRealmFlags1

## B4.6.89 RmiRttUnmapFlags type

The RmiRttUnmapFlags fieldset contains flags provided by the Host to commands which remove mappings from IPA space.

The RmiRttUnmapFlags fieldset is a concrete type.

The width of the RmiRttUnmapFlags fieldset is 64 bits.

The fields of the RmiRttUnmapFlags fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiRttUnmapFlags fieldset are shown in the following table.

| Name       | Bits   | Description               | Value          |
|------------|--------|---------------------------|----------------|
| oaddr_type | 1:0    | Type of oaddr input value | RmiRttAddrType |
|            | 63:2   | Reserved                  | SBZ            |

## B4.6.90 RmiRttUnprotMapFlags type

DRAFT

The RmiRttUnprotMapFlags fieldset contains flags provided by the Host to commands which create mappings in Unprotected IPA space.

The RmiRttUnprotMapFlags fieldset is a concrete type.

The width of the RmiRttUnprotMapFlags fieldset is 64 bits.

The fields of the RmiRttUnprotMapFlags fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiRttUnprotMapFlags fieldset are shown in the following table.

| Name       | Bits   | Description                                                                                                                                                                                                                                                              | Value          |
|------------|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| oaddr_type | 1:0    | Type of oaddr input value                                                                                                                                                                                                                                                | RmiRttAddrType |
| list_count | 15:2   | Number of valid entries in the oaddr list. If paddr_type != RMI_ADDR_TYPE_LIST then this field is ignored.                                                                                                                                                               | UInt14         |
| memattr    | 18:16  | Memory attributes. This field is encoded as for MemAttr[2:0] in a translation table page or block descriptor.                                                                                                                                                            | Bits3          |
| s2ap       | 22:19  | Stage 2 access permissions. If the Realm uses S2AP direct encoding, this is encoded as for AP in a translation table page or block descriptor. If the Realm uses S2AP indirect encoding, this is encoded as for PIIndex in a translation table page or block descriptor. | Bits4          |
|            | 61:23  | Reserved                                                                                                                                                                                                                                                                 | SBZ            |

## B4.6.91 RmiSignatureAlgorithm type

The RmiSignatureAlgorithm enumeration represents signature algorithm.

The RmiSignatureAlgorithm enumeration is a concrete type.

The width of the RmiSignatureAlgorithm enumeration is 8 bits.

The values of the RmiSignatureAlgorithm enumeration are shown in the following table.

|   Encoding | Name                | Description                                                                                                                            |
|------------|---------------------|----------------------------------------------------------------------------------------------------------------------------------------|
|          0 | RMI_SIG_RSASSA_3072 | SSA-3072 ( RSA Cryptography Specifications Version 2.2 [26])                                                                           |
|          1 | RMI_SIG_ECDSA_P256  | ECDSA-P256 ( Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA) [27]) |
|          2 | RMI_SIG_ECDSA_P384  | ECDSA-P384 ( Deterministic Usage of the Digital Signature Algorithm (DSA) and Elliptic Curve Digital Signature Algorithm (ECDSA) [27]) |

DRAFT

Unused encodings for the RmiSignatureAlgorithm enumeration are reserved for use by future versions of this specification.

The RmiSignatureAlgorithm enumeration is used in the following types:

- RmiPublicKeyParams

## B4.6.92 RmiStatusCode type

The RmiStatusCode enumeration represents the status of an RMI command.

The RmiStatusCode enumeration is a concrete type.

The width of the RmiStatusCode enumeration is 8 bits.

See also:

- B1.3 Command registers
- B1.5 Command context values

The values of the RmiStatusCode enumeration are shown in the following table.

|   Encoding | Name                    | Description                                                                                                                                                                                                                                                                 |
|------------|-------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|          0 | RMI_SUCCESS             | Command completed successfully, leaving no intermediate state                                                                                                                                                                                                               |
|          1 | RMI_ERROR_INPUT         | The value of a command input value caused the command to fail                                                                                                                                                                                                               |
|          2 | RMI_ERROR_REALM         | An attribute of a Realm does not match the expected value                                                                                                                                                                                                                   |
|          3 | RMI_ERROR_REC           | An attribute of a REC does not match the expected value                                                                                                                                                                                                                     |
|          4 | RMI_ERROR_RTT           | An RTT walk terminated before reaching the target RTT level, or reached an RTTE with an unexpected value                                                                                                                                                                    |
|          5 | RMI_ERROR_NOT_SUPPORTED | The command is not supported                                                                                                                                                                                                                                                |
|          6 | RMI_ERROR_DEVICE        | An attribute of a device does not match the expected value                                                                                                                                                                                                                  |
|          7 | RMI_ERROR_RTT_AUX       | RTTE in an auxiliary RTT contained an unexpected value                                                                                                                                                                                                                      |
|          8 | RMI_ERROR_PSMMU_ST      | An PSMMU Stream Table walk terminated before reaching the target level, or reached an entry with an unexpected value                                                                                                                                                        |
|          9 | RMI_ERROR_DPT           | A DPT walk terminated before reaching the target level, or reached an entry with an unexpected value                                                                                                                                                                        |
|         10 | RMI_BUSY                | DRAFT The command failed to make progress, for an IMPLEMENTATION DEFINED reason. The reason for the lack of progress may be temporary, and may be resolved without requiring any action to be taken by the Host. The command did not result in any changes of system state. |
|         11 | RMI_ERROR_GLOBAL        | An attribute of RMMglobal state does not match the expected value                                                                                                                                                                                                           |
|         12 | RMI_ERROR_TRACKING      | The state of a tracking region does not match the expected value                                                                                                                                                                                                            |
|         13 | RMI_INCOMPLETE          | The command initiated a state transition but did not complete, leaving an object in an intermediate state. The target object cannot be the subject of any other RMI command, until this one has been completed.                                                             |
|         14 | RMI_BLOCKED             | The command failed to make progress due to a target object being in an intermediate state. An incomplete operation must be completed before this one can proceed. The command did not result in any changes of system state.                                                |
|         15 | RMI_ERROR_GPT           | A GPT walk terminated before reaching the target level, or reached an entry with an unexpected value                                                                                                                                                                        |
|         16 | RMI_ERROR_GRANULE       | An attribute of a Granule does not match the expected value                                                                                                                                                                                                                 |

Unused encodings for the RmiStatusCode enumeration are reserved for use by future versions of this specification.

The RmiStatusCode enumeration is used in the following types:

## · RmiResult

## B4.6.93 RmiTrackingRegionState type

The RmiTrackingRegionState enumeration represents tracking region state.

The RmiTrackingRegionState enumeration is a concrete type.

The width of the RmiTrackingRegionState enumeration is 3 bits.

The values of the RmiTrackingRegionState enumeration are shown in the following table.

|   Encoding | Name                  | Description                                                       |
|------------|-----------------------|-------------------------------------------------------------------|
|          0 | RMI_TRACKING_RESERVED | Region is reserved for use by the platform.                       |
|          1 | RMI_TRACKING_NONE     | Region is not tracked.                                            |
|          2 | RMI_TRACKING_FINE     | Region is tracked at the granularity of the RMI Granule size.     |
|          3 | RMI_TRACKING_COARSE   | Region is tracked at the granularity of the Tracking Region size. |

Unused encodings for the RmiTrackingRegionState enumeration are reserved for use by future versions of this specification.

## B4.6.94 RmiTrap type

The RmiTrap enumeration represents whether a trap is enabled.

The RmiTrap enumeration is a concrete type.

The width of the RmiTrap enumeration is 1 bits.

The values of the RmiTrap enumeration are shown in the following table.

|   Encoding | Name        | Description       |
|------------|-------------|-------------------|
|          0 | RMI_NO_TRAP | Trap is disabled. |
|          1 | RMI_TRAP    | Trap is enabled.  |

DRAFT

The RmiTrap enumeration is used in the following types:

- RmiRecEnterFlags

## B4.6.95 RmiVdevFlags type

The RmiVdevFlags fieldset contains flags provided by the Host during VDEV creation.

The RmiVdevFlags fieldset is a concrete type.

The width of the RmiVdevFlags fieldset is 64 bits.

The fields of the RmiVdevFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiVdevFlags fieldset are shown in the following table.

| Name   | Bits   | Description                 | Value      |
|--------|--------|-----------------------------|------------|
| VSMMU  | 0      | Whether device uses a VSMMU | RmiFeature |
|        | 63:1   | Reserved                    | SBZ        |

The RmiVdevFlags fieldset is used in the following types:

- RmiVdevParams

## B4.6.96 RmiVdevMeasureFlags type

The RmiVdevMeasureFlags fieldset contains flags which describe properties of device measurements.

The RmiVdevMeasureFlags fieldset is a concrete type.

The width of the RmiVdevMeasureFlags fieldset is 64 bits.

## See also:

- A9.5.5 Device measurement retrieval

The fields of the RmiVdevMeasureFlags fieldset are shown in the following diagram.

<!-- image -->

<!-- image -->

The fields of the RmiVdevMeasureFlags fieldset are shown in the following table.

DRAFT

| Name   | Bits   | Description                                  | Value             |
|--------|--------|----------------------------------------------|-------------------|
| raw    | 0      | Whether the return value is a raw bitstream. | RmiVdevMeasureRaw |
|        | 63:1   | Reserved                                     | SBZ               |

The RmiVdevMeasureFlags fieldset is used in the following types:

- RmiVdevMeasureParams

## B4.6.97 RmiVdevMeasureParams type

The RmiVdevMeasureParams structure contains device measurement parameters.

The RmiVdevMeasureParams structure is a concrete type.

The width of the RmiVdevMeasureParams structure is 4096 ( 0x1000 ) bytes.

See also:

- A9.5.5 Device measurement retrieval

The members of the RmiVdevMeasureParams structure are shown in the following table.

| Name   | Byte offset   | Type                | Description                                           |
|--------|---------------|---------------------|-------------------------------------------------------|
| flags  | 0x0           | RmiVdevMeasureFlags | Attestation type                                      |
| nonce  | 0x100         | Bits256             | Nonce value used in requests for signed measurements. |

Unused bits of the RmiVdevMeasureParams structure MBZ.

## B4.6.98 RmiVdevMeasureRaw type

DRAFT

The RmiVdevMeasureRaw enumeration represents whether a device measurement is a raw bitstream.

The RmiVdevMeasureRaw enumeration is a concrete type.

The width of the RmiVdevMeasureRaw enumeration is 1 bits.

See also:

- A9.5.5 Device measurement retrieval

The values of the RmiVdevMeasureRaw enumeration are shown in the following table.

|   Encoding | Name                     | Description                        |
|------------|--------------------------|------------------------------------|
|          0 | RMI_VDEV_MEASURE_NOT_RAW | Returned value is measurement hash |
|          1 | RMI_VDEV_MEASURE_RAW     | Returned value is a raw bitstream  |

The RmiVdevMeasureRaw enumeration is used in the following types:

- RmiVdevMeasureFlags

## B4.6.99 RmiVdevParams type

The RmiVdevParams structure contains parameters provided by the Host during VDEV creation.

The RmiVdevParams structure is a concrete type.

The width of the RmiVdevParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiVdevParams structure are shown in the following table.

| Name           | Byte offset   | Type         | Description                                                                                              |
|----------------|---------------|--------------|----------------------------------------------------------------------------------------------------------|
| flags          | 0x0           | RmiVdevFlags | Flags                                                                                                    |
| vdev_id        | 0x8           | Bits64       | Virtual device identifier For a PCIe device this is the PCIe routing identifier of the virtual endpoint. |
| tdi_id         | 0x10          | Bits64       | TDI identifier                                                                                           |
| vsmmu_addr     | 0x20          | Address      | PA of VSMMU. This field is ignored unless flags.VSMMU is RMI_TRUE.                                       |
| vsid           | 0x28          | Bits64       | Virtual Stream Identifier. This field is ignored unless flags.VSMMU is RMI_TRUE.                         |
| num_addr_range | 0x30          | UInt64       | Number of device address ranges.                                                                         |
| addr_range[8]  | 0x200         | RmiAddrRange | Device address ranges. These ranges include both coherent and non- coherent device memory.               |

Unused bits of the RmiVdevParams structure SBZ.

## B4.6.100 RmiVdevState type

DRAFT

The RmiVdevState enumeration represents the state of a VDEV.

The RmiVdevState enumeration is a concrete type.

The width of the RmiVdevState enumeration is 8 bits.

The values of the RmiVdevState enumeration are shown in the following table.

|   Encoding | Name                 | Description                                                                                  |
|------------|----------------------|----------------------------------------------------------------------------------------------|
|          0 | RMI_VDEV_NEW         | Initial state of the device interface.                                                       |
|          1 | RMI_VDEV_UNLOCKED    | Device interface is unlocked.                                                                |
|          2 | RMI_VDEV_LOCKED      | Device interface is locked.                                                                  |
|          3 | RMI_VDEV_STARTED     | Device interface is started.                                                                 |
|          4 | RMI_VDEV_ERROR       | Device interface has reported a fatal error.                                                 |
|          5 | RMI_VDEV_KEY_REFRESH | Waiting for key refresh to be performed on all streams associated with the device interface. |

|   Encoding | Name               | Description                                                                                             |
|------------|--------------------|---------------------------------------------------------------------------------------------------------|
|          6 | RMI_VDEV_KEY_PURGE | Waiting for purge of inactive keys to be performed on all streams associated with the device interface. |

Unused encodings for the RmiVdevState enumeration are reserved for use by future versions of this specification.

## B4.6.101 RmiVsmmuCmdFlags type

The RmiVsmmuCmdFlags fieldset contains flags which describe the result of triaging a VSMMU command.

The RmiVsmmuCmdFlags fieldset is a concrete type.

The width of the RmiVsmmuCmdFlags fieldset is 64 bits.

The fields of the RmiVsmmuCmdFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiVsmmuCmdFlags fieldset are shown in the following table.

| Name         | Bits   | Description                                                       | Value      |
|--------------|--------|-------------------------------------------------------------------|------------|
| pending      | 0      | Whether a further VSMMU command is pending                        | RmiBoolean |
| cmd_complete | 1      | Whether VSMMU command requires further processing by theRMM       | RmiBoolean |
| irq          | 2      | Whether VSMMU event requires an IRQ to be injected into the Realm | RmiBoolean |
|              | 63:3   | Reserved                                                          | SBZ        |

DRAFT

## B4.6.102 RmiVsmmuEventFlags type

The RmiVsmmuEventFlags fieldset contains flags which describe the result of triaging a VSMMU event.

The RmiVsmmuEventFlags fieldset is a concrete type.

The width of the RmiVsmmuEventFlags fieldset is 64 bits.

The fields of the RmiVsmmuEventFlags fieldset are shown in the following diagram.

The fields of the RmiVsmmuEventFlags fieldset are shown in the following table.

| Name   | Bits   | Description                                                       | Value      |
|--------|--------|-------------------------------------------------------------------|------------|
| irq    | 0      | Whether VSMMU event requires an IRQ to be injected into the Realm | RmiBoolean |
| abort  | 1      | Whether RMMaccess to VSMMU queue failed due to Data Abort         | RmiBoolean |
|        | 63:2   | Reserved                                                          | SBZ        |

## B4.6.103 RmiVsmmuFeatures type

The RmiVsmmuFeatures structure contains VSMMU features supported by the RMM.

The RmiVsmmuFeatures structure is a concrete type.

The width of the RmiVsmmuFeatures structure is 256 ( 0x100 ) bytes.

DRAFT

The members of the RmiVsmmuFeatures structure are shown in the following table.

| Name   | Byte offset   | Type   | Description              |
|--------|---------------|--------|--------------------------|
| aidr   | 0x0           | Bits64 | SMMU_AIDR register value |
| idr[7] | 0x8           | Bits64 | SMMU_IDR register values |

Unused bits of the RmiVsmmuFeatures structure SBZ.

## B4.6.104 RmiVsmmuFlags type

The RmiVsmmuFlags fieldset contains flags provided by the Host during PDEV creation.

The RmiVsmmuFlags fieldset is a concrete type.

The width of the RmiVsmmuFlags fieldset is 64 bits.

The fields of the RmiVsmmuFlags fieldset are shown in the following diagram.

<!-- image -->

The fields of the RmiVsmmuFlags fieldset are shown in the following table.

| Name   | Bits   | Description   | Value   |
|--------|--------|---------------|---------|
|        | 63:0   | Reserved      | SBZ     |

The RmiVsmmuFlags fieldset is used in the following types:

- RmiVsmmuParams

## B4.6.105 RmiVsmmuParams type

The RmiVsmmuParams structure contains parameters provided by the Host during VSMMU creation.

The RmiVsmmuParams structure is a concrete type.

The width of the RmiVsmmuParams structure is 4096 ( 0x1000 ) bytes.

The members of the RmiVsmmuParams structure are shown in the following table.

| Name     | Byte offset   | Type          | Description                                              |
|----------|---------------|---------------|----------------------------------------------------------|
| flags    | 0x0           | RmiVsmmuFlags | Flags                                                    |
| reg_base | 0x8           | Address       | Base IPA of register base in Realm's Protected IPA space |
| reg_top  | 0x10          | Address       | Top IPA of register base in Realm's Protected IPA space  |
| aidr     | 0x18          | Bits64        | SMMU_AIDR register value                                 |
| idr[7]   | 0x20          | Bits64        | SMMU_IDR register values                                 |

DRAFT

Unused bits of the RmiVsmmuParams structure SBZ.