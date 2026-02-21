## 16.7 Interconnect-specific features

## 16.7.1 Reporting of Unsupported Client Transactions

The SMMU behaves as though a single transaction is associated with one translation.

SMMU implementations might define their own input alignment restrictions leading to an unsupported client transaction error. For example, an implementation with an AMBA downstream interconnect is likely to treat an incoming transaction that crosses a 4KB boundary as unsupported, because these would violate the alignment rules of the downstream interconnect.

For AMBA 4 systems the following upstream client transactions are unsupported:

- Far Atomic operations (see section 16.7.6 Far Atomic operations ) where not supported by the downstream interconnect or SMMU implementation.

Such transactions will be aborted and an F\_UUT event will be recorded if possible.

## 16.7.2 Non-data transfer transactions

Some interconnect architectures support transactions that do not perform a data transfer, prefetch or translation request action.

If the input interconnect can express the following transactions from client devices, the transactions will be terminated silently by the SMMU as SLVERR (or equivalent on non-AMBA interconnect):

- DVMoperations (of all sub-types).
- Barriers.

The interconnect architecture of an implementation might support the following non-data operations, also known as Cache Maintenance Operations (CMOs), that perform address-based cache maintenance:

- Clean.
- Invalidate.
- CleanInvalidate.
- CleanToPersistence.
- Destructive hint (DH): Operation that has a hint side effect of invalidate.

Note: In AMBA AXI [8], the equivalent of the above operations are the CleanShared, MakeInvalid, CleanInvalid, CleanSharedPersist and InvalidateHint transactions, respectively.

SMMUv3.0:

- The SMMU does not support CMOs. If an SMMUv3.0 implementation can receive these operations from client devices, they are handled in an IMPLEMENTATION DEFINED way. A system that requires SMMU support for CMOs is required to implement SMMUv3.1 or later.

SMMUv3.1 and later:

- CMOs that are not address-based are not supported and are silently terminated by the SMMU.
- CMOs are permitted to pass into the system, without the transformation described in section 16.7.2.1 Control of Cache Maintenance Operations , when the transaction bypasses all implemented stages of translation. See section 16.7.2.3 Memory types and Shareability for Cache Maintenance Operations on memory types.
- -Note: For a Secure stream, SMMU\_S\_CR0.SIF still applies. See section 16.7.2.2 Permissions model for Cache Maintenance Operations .
- When one or more stages of translation is applied, the SMMU allows these operations to progress into the system subject to the configuration controls and permission model described in sections 16.7.2.1 Control of Cache Maintenance Operations and 16.7.2.2 Permissions model for Cache Maintenance Operations . Additionally, Invalidate operations might be transformed into Clean and Invalidate operations as part of these checks.

- When the input interconnect can deliver these operations, but the output interconnect does not support them, the transactions are silently terminated.

SMMU implementations supporting AMBA might define an IMPLEMENTATION DEFINED set of unsupported incoming transactions.

SMMU implementations supporting other interconnects might define their own set of unsupported incoming transactions.

Note: See section 3.22 Destructive reads and directed cache prefetch transactions . A destructive read (read with invalidate), write with directed prefetch, or standalone directed prefetch transaction is not considered to be a discrete Cache Maintenance Operation and is handled differently.

## 16.7.2.1 Control of Cache Maintenance Operations

In SMMUv3.1 and later, STE.DRE controls whether an Invalidate operation is transformed as follows:

| Input transaction class   | DRE == 0                                                                                                               | DRE == 1                                                              |
|---------------------------|------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|
| Invalidate                | Transformed into CleanInvalidate. The operation is treated identically to a CleanInvalidate for permission evaluation. | Eligible for output as Invalidate (if permissions checks allow)       |
| Destructive hint (DH)     | Transformed into No-op.                                                                                                | Eligible for output as destructive hint (if permissions checks allow) |

The STE.DRE field applies in this manner when one or more stages of translation are applied. This does not include the case where the only stage of translation is skipped due to STE.S1DSS.

## 16.7.2.2 Permissions model for Cache Maintenance Operations

In SMMUv3.1 and later, the SMMU\_S\_CR0.SIF permission check applies to Cache Maintenance Operations (CMOs). This applies when either translation or bypass occurs.

In SMMUv3.1 and later, when one or more stages of translation are applied, the following permissions are required for CMOs:

| Maintenance operation type                 | Required permissions                                                                                                                                                                       | Behavior if permissions not met                                                                                                                                                                                     |
|--------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Clean, CleanInvalidate, CleanToPersistence | Identical to ordinary read: Requires Read or Execute permission, (depending on input InD and INSTCFG) at privilege appropriate to PnU input and STE.PRIVCFG.                               | Identical to ordinary read.                                                                                                                                                                                         |
| Invalidate                                 | To progress as Invalidate, requires both Read-or-Execute permission (depending on input InD and INSTCFG) and Write permission at a privilege appropriate to the PnU input and STE.PRIVCFG. | If no Read/Exec permission is available behavior is identical to an ordinary read. If Read/Exec permission is available but Write permission is not, an Invalidate is transformed into a CleanInvalidate operation. |

| Maintenance operation type   | Required permissions                                                                                                                                                                                                                                      | Behavior if permissions not met   |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------|
| Destructive hint (DH)        | To progress as destructive hint, requires both Read-or-Execute permission (depending on input InD and STE.INSTCFG), and Write permission that does not result in HTTU update of Dirty state, at a privilege appropriate to the PnU input and STE.PRIVCFG. | Invalidate does not occur. (1)    |

(1) A DH operation is a hint. If the required permissions are not met for a DH at a given stage of translation, the DH operation is treated as a No-op and does not progress into the system. If HTTU of dirty state is enabled, a DH operation does not mark a page Dirty. If the translation for a DH operation is writable-clean, the SMMU does not perform the hardware update of dirty state and instead the DH operation is treated as a No-op and does not progress into the system. If a DH operation is permitted to progress through a stage of translation and HTTU of Access flag is enabled for that stage, AF is updated. If the translation conditions permit an AF update, but the DH is not permitted to progress into the system, a coincidental speculative update of AF might occur.

If a Clean, CleanInvalidate, Invalidate or CleanToPersistence operation leads to a fault, it is recorded as a read, that is RnW == 1. The read can be treated as either data or instruction, depending on the input InD/INSTCFG. On fault, these operations stall in the same way as an ordinary read transaction if the SMMU is configured for stalling fault behavior. Retry and termination behave the same as for an ordinary read or write transaction. If these transactions are stalled and retried, they are retried as the same transaction type. A DH transaction does not cause faults in the SMMUnor does it cause an abort response to be returned where the interconnect architecture requires a response.

An implementation is permitted to downgrade a DH operation as described in this section, for any reason.

Note: The input interconnect might supply all CMOs as Data.

See section 3.13.8 Hardware flag update for Cache Maintenance Operations and Destructive Reads for information on the behavior of HTTU for Invalidate operations.

When HTTU is enabled for Access flag updates and the translation descriptor and AFFD configuration require it, a Clean, CleanInvalidate, CleanToPersistence, Invalidate, or DH operation updates the Access flag. See section 3.13.2 Access flag hardware update .

## 16.7.2.3 Memory types and Shareability for Cache Maintenance Operations

Cache Maintenance Operations (CMOs) do not have a memory type. If an input shareability is provided, it does not undergo any normalization before entering the attribute determination process described in Chapter 13 Attribute Transformation . If an input shareability is not provided, the default shareability is taken as described in section 13.1.3 Default input attributes . After input, the output Shareability of a CMO is determined in the same way to that of an ordinary transaction.

Note: This means that the input shareability of a CMO is not dependent on the input memory type even if the input bus encodes a memory type, because the SMMU does not consider a memory type to be provided on input for a CMO.

In SMMUv3.1 and later, this rule applies to all such operations in all translation and bypass configurations, including:

- Global bypass (attribute set from GBPA).
- STE bypass (whether STE.Config == 0b100 or STE.S1DSS and STE.Config == 0b101 causes skip of the only stage of translation).
- Translation.

Note: On AMBA AXI5 interfaces [8], it is not permitted to issue CMOs, including the DH operations, with Sys shareability.

## 16.7.3 Treatment of AMBA Exclusives from client devices

The ACE-Lite specification does not permit Exclusive accesses to Inner-shareable or Outer-shareable AMBA domains. Therefore, if the SMMU interface to the system interconnect is ACE-Lite, a Non-shareable, or System-shareable, Exclusive access transaction that is translated into an Inner-shareable or Outer-shareable transaction cannot be marked as Exclusive. Arm recommends that such transactions are transformed into non-Exclusives.

For more information about the relationship between AMBA and Armv8 output attributes, see section 16.7.5.2 Conversion of Armv8 attributes to AMBA on output and representation of Shareability .

The outcome of such a transformed Exclusive transaction is equivalent to that of an ordinary transaction and depends on whether the transaction experiences a fault and, if it faults, fault configuration. The transaction will experience one of the following:

- Translates without fault, returning the non-exclusive transaction's response to the upstream client device. A response of EXOK is not possible (as the transaction is now non-exclusive). A response of OK will be treated as an exclusive fail by the upstream client device.
- Faults on translation and is terminated with abort. These aborts are reported to the upstream client device in the same way for transformed Exclusive transactions as for regular transactions (for example as SLVERR).
- Fault on stage 1 translation and be terminated with RAZ/WI semantics because CD.A == 0. This returns a response of OK.

## 16.7.4 Treatment of downstream aborts

Some systems might allow a Completer device to abort transactions, returning status to the Requester. Translated transactions initiated by a client device that are aborted in the memory system are not recorded in the SMMU. The abort is returned to the client device, which is responsible for recording and reporting such faults. Aborted transactions that were internally-initiated by the SMMU are recorded by the SMMU if possible to do so.

The event recorded by the SMMU, on one of its accesses being returned with abort status (whether aborted by the interconnect or Completer), depends on the type of access:

| STE fetch:                | F_STE_FETCH                               |
|---------------------------|-------------------------------------------|
| CD fetch:                 | F_CD_FETCH                                |
| VMS fetch:                | F_VMS_FETCH                               |
| Translation table walk:   | F_WALK_EABT                               |
| Command queue read entry: | GERROR.CMDQ_ERR &Command queue CERROR_ABT |
| Event queue access:       | GERROR.EVENTQ_ABT_ERR                     |
| PRI queue access:         | GERROR.PRIQ_ABT_ERR                       |
| MSI write:                | GERROR.MSI_*_ABT_ERR                      |

## 16.7.5 SMMU and AMBA attribute differences

## 16.7.5.1 Conversion of AMBA attributes to Armv8 on input and inferring Inner Attributes

AMBA does not explicitly encode separate inner attributes for an upstream client device. Arm recommends that the inner and outer attributes are considered to be the same as the outer attributes except in the following case for data operations:

- It is IMPLEMENTATION DEFINED whether Non-cacheable with any AxDOMAIN value is treated as iNC-oNC-OSH or whether Non-cacheable with an AxDOMAIN value of NSH/ISH/OSH is treated as

an iWB-oNC-{NSH,ISH,OSH} type. In the latter case, it must be considered to be Read-Allocate and Write-Allocate.

Note: Determination of the inner attributes might be used if the downstream interconnect can convey inner attributes.

## 16.7.5.1.1 Conversion of input attributes from AMBA to Armv8 architectural attributes

Incoming AMBA attributes are converted to SMMU/Armv8 architectural attributes as follows:

| AMBA attribute                                                    | Armv8 attribute                                         | Notes                                                                                                                                                                |
|-------------------------------------------------------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Device-Sys non-bufferable                                         | Device-nGnRnE                                           |                                                                                                                                                                      |
| Device-Sys bufferable                                             | Device-nGnRE                                            |                                                                                                                                                                      |
| Normal-Non-cacheable-Sys (bufferable or non-bufferable)           | Normal-iNC-oNC-OSH                                      |                                                                                                                                                                      |
| Normal-Non-cacheable {NSH,ISH,OSH} (bufferable or non-bufferable) | Normal-iNC-oNC-OSH Or Normal-iWB-oNC- {NSH,ISH,OSH}     | This is an IMPLEMENTATION DEFINED choice. When the input is treated as iNC-oNC-OSH, RA/WA/TR do not exist. Otherwise, RA,WA are 1 and marked non-transient.          |
| Normal-WriteThrough- {NSH,ISH,OSH}                                | Normal-iNC-oNC-OSH (1) Or Normal-iWT-oWT- {NSH,ISH,OSH} | This is an IMPLEMENTATION DEFINED choice. When the input is treated as iNC-oNC-OSH, RA/WA/TR do not exist. Otherwise, RA,WA are from input and marked non-transient. |
| Normal-WriteBack-{NSH,ISH,OSH}                                    | Normal-iWB-oWB- {NSH,ISH,OSH}                           | RA, WAfrom input. Always marked non-transient.                                                                                                                       |

An ACE-Sys input Shareability in considered to be OSH for the purposes of attribute combining and overriding as described in section 13.1 SMMU handling of attributes .

## 16.7.5.2 Conversion of Armv8 attributes to AMBA on output and representation of Shareability

The SMMU specifies the architectural Inner and Outer Cacheability and Shareability attributes. However, in some circumstances there is a non-obvious transformation of these attributes into an AMBA representation:

- The architecture considers any-Device/Normal-iNC-oNC to be OSH, while ACE considers these to be 'Sys'.
- Final attributes of any-Device/Normal-iNC-oNC are presented on AMBA as ACE-Device-Sys/ ACE-Normal-Non-cacheable-Sys.
- If the implementation does not transform final attributes of i{WB,WT}-oNC-OSH (inner cacheable of any variety) to Normal-Non-cacheable-SYS as set out in 16.7.5.3 Common interpretation of attribute encoding between SMMU and PE (for example, a different interpretation of attribute mapping is used to that of Arm PE IP) and these attributes are transformed to an ACE cacheable type, the type is represented as ACE-OSH.

## 16.7.5.2.1 Conversion of Armv8 architectural attributes to AMBA on output

SMMU/Armv8 architectural attributes are converted to AMBA attributes on output as follows:

| Armv8 attribute               | AMBA attribute                      | Notes                                                                            |
|-------------------------------|-------------------------------------|----------------------------------------------------------------------------------|
| Device-nGnRnE                 | Device-Sys non-bufferable           | Device-Sys non-bufferable                                                        |
| Device-(n)G(n)RE              | Device-Sys bufferable               | Device-Sys bufferable                                                            |
| Normal-iNC-oNC-OSH            | Normal-Non-cacheable-Sys bufferable | Architecturally, a Normal-iNC-oNC-{NSH,ISH} attribute is not possible, only OSH. |
| Normal-iNC-oWT -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iNC-oWB- {NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWT-oNC -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWT-oWT -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWT-oWB -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWB-oNC -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWB-oWT -{NSH,ISH,OSH} | Normal-Non-cacheable-Sys bufferable | (1)                                                                              |
| Normal-iWB-oWB -{NSH,ISH,OSH} | Normal-WriteBack-{NSH,ISH,OSH}      |                                                                                  |

(1) See 16.7.5.3 Common interpretation of attribute encoding between SMMU and PE below: these transformations correspond to the transformations implemented in the PEs in the system. The outputs shown correspond to Arm Cortex IP. For other PE IP, the interpretations of the Armv8 attributes are IMPLEMENTATION DEFINED.

When a cacheable type is output, AMBA interconnect RA and WA attributes are generated directly from the RA/WA portion of the Arm architectural attribute.

Section 13.1.7 Ensuring consistent output attributes mandates that the SMMU will not output architecturally-inconsistent attributes or attribute combinations that are illegal for the interconnect. For AMBA, the output AxDOMAIN is made consistent with the final AxCACHE value if it is not already. If required, this is made consistent by choosing the highest (most shareable) value of AxDOMAIN that is legal given AxCACHE. Normal Non-cacheable types are always bufferable. The output AxDOMAIN is ACE-Sys if the final attributes are a Device or a Non-cacheable type.

For example, in the case where:

- The SMMU is configured to bypass, SMMU\_CR0.SMMUEN == 0.
- SMMU\_GBPA.MTCFG == 1, and the input MemAttr is overridden to 'iWB-oWB' by SMMU\_GBPA.MemAttr.
- SMMU\_GBPA.SHCFG == 'use-incoming'.
- An ACE input attribute provides ACE-Device-Sys.

The final output of the SMMU is ACE-WB-OSH.

## 16.7.5.3 Common interpretation of attribute encoding between SMMU and PE

If interoperation with the Armv8 PE IP is required, a Normal memory attribute that is not iWB-oWB is transformed to the architectural type iNC-oNC-OSH. See 16.7.5.2 Conversion of Armv8 attributes to AMBA on output and representation of Shareability , in AMBA systems this is represented as ACE-NC-Sys.

For example, a final output attribute of iWT-oNC-NSH is converted to iNC-oNC-OSH and is therefore output into an AMBA system as ACE-NC-Sys.

Access attributes of type any-Device are unaffected by this rule.

Otherwise, for interoperation with other PE IP, the transformations between Normal memory attributes that are not iWB-oWB or iNC-oNC and AMBA attributes are IMPLEMENTATION DEFINED.

## 16.7.6 Far Atomic operations

If an interconnect and SMMU supports client device-initiated Far Atomic operations according to the atomic operations specified in Armv8.1-A [2], they experience permission checking as though they perform both a read and a write operation. See section 13.1.1 Attribute definitions for permission checking and fault reporting. An atomic access is considered to be a write that also performs a read, so is always considered to be Data. The InD attribute and any INSTCFG overrides are ignored for atomic accesses.

Note: For example, a Far Atomic increment to an address in a read-only page must cause a write Permissions Fault (if all other translation requirements are satisfied). If the transaction is configured to stall and is later retried, the entirety of the transaction must be retried atomically. It is prohibited to satisfy the read of data prior to raising a write fault for the update of the data and then use the same read data when the transaction is later retried. The retry must perform the unbroken atomic transaction in one action.

If an upstream interconnect can express this kind of atomic transaction, but the downstream interconnect or system cannot, one of the following occurs:

1. Terminate the transaction in the SMMU with an abort, and record an F\_UUT.
2. Support Far Atomic transactions within the SMMU, converting them to local monitor atomic operations using a fully-coherent cache in the SMMU.

In case (1) where far atomics are not supported at all, Arm recommends that the system ensures that upstream devices are not able to emit these transactions (and that software not expect to use them).

## 16.7.7 AMBA DVM messages with respect to CD.ASET == 1 TLB entries

CD.ASET == 1 affects the interaction of TLB entries with DVM messages in the following ways:

Entries created from StreamWorld == NS-EL1 are not required to be invalidated by:

- Guest OS TLB invalidation by ASID.
- Guest OS TLB invalidation by ASID and VA.

Entries created from StreamWorld == Secure are not required to be invalidated by:

- Secure TLB invalidation by ASID.
- Secure TLB invalidation by ASID and VA.

Entries created from StreamWorld == any-EL2-E2H are not required to be invalidated by:

- Hypervisor TLB invalidation by ASID.
- Hypervisor TLB invalidation by ASID and VA.

Entries created from StreamWorld == any-EL2 are not required to be invalidated by:

- Hypervisor TLB invalidation by VA.
- Hypervisor TLB invalidation by ASID.
- Hypervisor TLB invalidation by ASID and VA.

Entries created from StreamWorld == EL3 are not required to be invalidated by:

Chapter 16. System and Implementation Considerations 16.7. Interconnect-specific features

- EL3 TLB invalidation by VA.