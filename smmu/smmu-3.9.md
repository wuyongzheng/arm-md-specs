## 3.9 Support for PCI Express, PASIDs, PRI, and ATS

A PCI RequesterID maps directly to the low-order bits of a StreamID, therefore maps to one STE, see section 3.2 Stream numbering . A PCIe Function is then the minimum granularity that can be assigned to a VM. The PCIe PASID prefix allows a Function to be subdivided into parts, each of which is intended to be assigned to a different user space process at stage 1. The prefix is optional. Transactions from one StreamID might be supplied with a SubstreamID or not, on a per-transaction basis. Because the prefix just identifies a portion of a Function, the Function remains otherwise indivisible and remains the granularity at which assignments to VMs are made. Therefore, in PCI terms:

- Stage 2 is associated with a RequesterID (identifying a Function). The Function is assigned to a VM.
- Stage 1 is associated with a (RequesterID, PASID) tuple. That is, the PASID differentiates between different stage 1 translation contexts.
- The PASID identifies which of the parts or contexts of the Function are assigned to which process or driver at stage 1.
- If transactions from a Function are translated using stage 2 but stage 1 is unused and in bypass, there are no stage 1 translation contexts to differentiate with a PASID. Supply of a PASID or SubstreamID to a configuration without stage 1 translation causes the translation to fail. Such transactions are terminated with an abort and C\_BAD\_SUBSTREAMID is recorded.

PASIDs can be up to 20 bits in size. PASIDs are optional, configurable, and of a size determined by the minimum of the endpoint, system software, PCIe Root Complex and the individually-supported substream width of the SMMU.

The SMMU is not required to report an error in the case where an endpoint and Root Complex emit a PASID with a value greater than can be expressed in the SubstreamID width supported by the SMMU. In this scenario, the PASID might be truncated to the SubstreamID size on arrival at the SMMU.

To minimize PCIe-specific terms, a RequesterID is referred to using a StreamID (to which the RequesterID maps in a hardware-specific manner). In the SMMU, a PASID is referred to as a SubstreamID. Even when a client device supports SubstreamIDs, it is not mandatory to supply a SubstreamID with all transactions from that device. PCIe permits a PASID to be supplied, or not, on a per-transaction basis. Therefore, where a SubstreamID is input to the SMMU, a validity flag is also provided and this is asserted when a PASID is present.

The PASID tag provides additional permission attributes on top of the standard PCIe read/write attribute. The tag can express an Execute and Privileged state that correspond to the SMMU INST and PRIV attributes. A PCIe transaction without a PASID is considered Data, unprivileged. The mapping between PCIe and SMMU permissions is described in section 13.7 PCIe permission attribute interpretation .

## 3.9.1 ATS Interface

An optional extra hardware interface might be provided by an SMMU implementation to support PCIe ATS [1] and PRI. This interface conveys translation and paging requests and responses to and from the PCIe Root Complex, which bridges requests and responses into the PCIe domain.

Whether the SMMU implements ATS can be discovered from SMMU\_(R\_)IDR0.ATS. If ATS is implemented, whether the SMMU also implements PRI can be discovered from SMMU\_(R\_)IDR0.PRI. This support determines the behavior of SMMU-local configuration and commands but does not guarantee that the rest of the system, and all clients of an SMMU, also support ATS and PRI. The ATS and PRI capabilities of dependent PCIe Root Complexes and endpoints thereof are discovered through other means.

PCIe ATS has the following properties:

- Note: ATS aims to improve the performance of a system using an SMMU, known as a Translation Agent in PCIe terminology, by caching translations within the endpoint or Requester. This can remove contention on a shared TLB, or reduce latency by helping the device to request translation ahead of time.
- The remote endpoint Address Translation Cache (ATC, which is equivalent to a TLB) is filled on-demand by making a Translation Request to the Root Complex which forwards it to the SMMU. If the translation exists

and permission checks pass, a Translation Completion response is given with a Physical Address and the ATC caches this response.

- The return of a translated, physical address to an endpoint grants the endpoint permission to access the physical address. The endpoint can now make direct access to PAs, which it does by tagging outgoing traffic as Translated. The Root Complex is expected to provide this tag to the SMMU. The SMMU might then allow such transactions to bypass translation and access PA space directly.
- If a Translation Request would result in a fault or error, a negative response is returned and the endpoint is not able to access the address using ATS. This denial might be fatal to the endpoint, reported in a device-specific manner, or when PRI is used, initiate a page-in request.
- Page access permission checking is performed at the time of the Translation Request, and takes the form of a request for permission to read or to read/write (and, optionally, to execute). The response grants the device access to read or to read/write (and, optionally, to execute) as specified in [1]. The response returns the permissions that are available, which might consist of a subset of the requested permissions.

Note: For example, a request to read and write a page might succeed, but only permission to read might be granted. The endpoint does not write pages it has not been granted write access to.

- ATS translation failures are reported to the endpoint, which might make an error software-visible, but the SMMUdoes not record fault events for ATS translation failures.
- Invalidation of the ATC translations is required whenever a translation changes in the SMMU. This is done in software. Broadcast invalidation operations might affect the internal translation caches of the SMMU, but these operations are not forwarded into the PCIe domain.
- -Note: An Arm broadcast TLB invalidation provides an address, ASID and VMID. The SMMU does not map this information back to the RequesterID of an endpoint in hardware.
- -Note: When CD.TBI0 or CD.TBI1 are used to enable use of tagged pointers with an endpoint that uses ATS, system software must assume that a given virtual address has been cached by the endpoint's ATC with any value of address bits [63:56]. This means that invalidation of a given virtual address V A[55:12] requires either 256 ATS Invalidate operations to invalidate all possible aliases that the ATC might have cached, or an ATS Invalidate-all operation.
- ATS Invalidation is performed using SMMU commands which the SMMU forwards to the Root Complex. The invalidation responses are collected, and the SMMU maintains the ordering semantics upheld by the Root Complex in which a transaction that might be affected by an ATS Invalidate operation must be visible before the ATS Invalidation completes.
- ATS must be disabled at all endpoints before SMMU translation is disabled by clearing SMMU\_(R\_)CR0.SMMUEN.
- An ATS Translation Request might be fulfilled using SMMU TLB entries, or cause SMMU TLB entries to be inserted. Therefore, after a change of translation configuration, an ATS Invalidate Request must be preceded by SMMU TLB invalidation. Software must ensure that the SMMU TLB invalidation is complete before initiating the ATS Invalidation.

Note: This order ensures that an ATS Translation Request performed after an ATS Invalidate Request cannot observe stale cached translations.

- ATS and PRI are not supported from Secure streams.
- -In Secure STEs, the EATS field is RES0.
- -CMD\_ATC\_INV and CMD\_PRI\_RESP are not able to target Secure StreamIDs.
- -The SMMU terminates any incoming traffic marked Translated on a Secure StreamID, aborting the transaction and recording F\_TRANSL\_FORBIDDEN.
- -It is IMPLEMENTATION DEFINED whether it is possible for ATS Translation Requests with a Secure StreamID to reach the SMMU.
- -If it is possible for an implementation to receive an ATS Translation Request from a Secure StreamID, the request is aborted with a UR response and F\_BAD\_ATS\_TREQ is recorded into the Secure Event

queue. The check for a Secure ATS Translation Request takes place prior to checking of StreamID or configuration lookup.

- Support for CMD\_ATC\_INV and CMD\_PRI\_RESP on the Secure Command queue is optional and is indicated by SMMU\_S\_IDR3.SAMS.
- The Smallest Translation Unit, (STU, as programmed into the ATS Control Register of the Endpoint) is defined as the smallest granule that the SMMU implements, as discovered from SMMU\_IDR5. Software must program the same STU size for all devices serviced by an SMMU, and must not assume all SMMUs in the system are identical in this respect.

The Page Request Interface (PRI) adds the ability for PCIe functions to target DMA at unpinned dynamically-paged memory. PRI depends on ATS, but ATS does not require PRI. Like ATS, PRI can be enabled on a per-function basis. When enabled:

- If an ATS request fails with a not-present result, the endpoint issues a PRI page request to ask software to make the requested pages resident.
- Software receives these PRI Page Requests (PPRs) on the PRI queue and issues a positive PRI response command to the SMMU after making pages present. If a requested address is unavailable, a programming failure has caused the device to request an illegal address, and software must issue a negative PRI response command.
- The net effect is that a hypervisor or OS can use unpinned, dynamically-paged memory for DMA.
- The PRI queue is of a fixed size and PPRs must not be lost. To ensure this, page request credits are issued by the most privileged system software (that which controls the PRI queue) to each PCIe endpoint using the PRI capability in its configuration space.
- If a guest is allowed to use PRI, it enables PRI (through the configuration space) and sets up its own PRI queue. The hypervisor needs to proxy PPRs from the host PRI queue to the guest PRI queue. However, the total system number of PRI queue entries is limited by the PRI queue size of the hypervisor.
- The PRI queue size is limited up to a per-SMMU maximum, indicated by SMMU\_IDR1.PRIQS. Arm expects that where PRI is used with virtualization then each guest discovers how many PRI queue entries its emulated SMMU supports. The host allocates N from its allocation of L, and ensures that the guest gives out a maximum of N credits (using configuration space) to devices controlled by the guest. L is the total number of PRI queue entries in the PRI queue of the host and is the maximum number of credits actually given out to devices.
- If the PRI queue becomes full because of erroneous behavior in a client device, the SMMU and Root Complex will respond to further incoming Page Request messages by returning a successful PRG response. This will not fatally terminate device traffic and a device will simply try ATS, fail, and try PRI again. Arm expects that a system employing this technique would remain functional and free-flowing, if requests were consumed from the PRI queue and space for new requests created, see section 8.1 PRI queue overflow .

Note: ATS operation enables an endpoint to issue Translated transactions that bypass the SMMU in some configurations. In these cases use of ATS could be a security issue, particularly when considering untrusted, subverted, or non-compliant ATS devices. For example, a custom FPGA-based device might mark requests as Translated despite the ATS protocol and translation tables not having granted access.

SMMU\_(R\_)CR0.ATSCHK controls whether the SMMU allows Translated traffic to bypass with no further checks, other than an address size check. If configured as requiring further checks, that is SMMU\_(R\_)CR0.ATSCHK == 1, Translated transactions from an endpoint are controlled by the associated STE.EATS field, which provides a per-device control of whether ATS traffic is allowed. When allowed, that is when the effective value of STE.EATS is 0b01 , 0b10 or 0b11 , Translated transactions are accepted. Otherwise, when the effective value of STE.EATS is 0b00 , the transaction is terminated with an abort, and an F\_TRANSL\_FORBIDDEN event is recorded.

Note: An implementation might perform this traffic interception and checking in a manner that is much quicker than performing full translation, thereby retaining a performance advantage of using ATS while achieving greater safety than permitting all ATS traffic.

STE.EATS also allows a mode in which ATS responses are returned with IPAs, the output from the stage 1 of a stage 1 and stage 2 configuration, so that later Translated transactions from the endpoint are considered IPAs and further translated by the SMMU using the stage 2 configuration of the stream. This allows ATS to be used

(for example with PRI) while maintaining stage 2 isolation. This mode is optional in an implementation, and support is discovered through SMMU\_IDR0.NS1ATS. When implemented, this mode can only be used when SMMU\_(R\_)CR0.ATSCHK is 1, as stage 2 translation needs to be applied.

Note: When ATS is used with nested stage 1 and stage 2 translation, any modification to stage 1 or stage 2 requires an invalidation of ATC entries, which cache information derived from both stages. This also applies to the EATS == 0b10 Split-stage ATS case.

If SMMU\_(R\_)CR0.SMMUEN == 1, translated transactions that bypass the SMMU, either when SMMU\_(R\_)CR0.ATSCHK is 0, or when SMMU\_(R\_)CR0.ATSCHK is 1 and the effective value of STE.EATS is not 0b00 , are subject to address size checks. See section 3.9.1.1 Handling of addresses in ATS-related transactions for more information on the required behavior.

Note: This situation would not normally arise outside of incorrect ATS Invalidation when transitioning between Split-stage ATS mode and regular ATS mode.

The recommended mapping between StreamID and RequesterID is described in 3.2 Stream numbering .

Arm expects that most highly-integrated non-PCIe devices requiring translation and paging facilities will use IMPLEMENTATION SPECIFIC distributed SMMU TLB facilities, rather than using ATS and PRI. Using SMMU facilities allows such devices to participate in broadcast TLB invalidation and use the Stall fault model.

If the translation requested by an ATS request is valid and HTTU is enabled, the SMMU must update Translation Table Dirty/Access flags on receipt of the ATS Translation Request, see 3.13 Translation tables and Access flag/Dirty state below. An ATS request is either for a read-only translation (in which case the NW flag of the request is set) so only the Access flag is updated, or for a read-write translation (in which case the NW flag of the request is clear) for which both the Access flag and the dirty state of the page are updated.

Note: Because the intention is for the actual traffic to bypass the SMMU, the ATS request is the only opportunity the SMMU will have to note the access in the flags.

A PASID tag can also be applied to an ATS Translation Request to select translation under a specific SubstreamID. A PASID-tagged ATS TR requests that the endpoint be granted access to a given address, according to the Execute and Privileged attributes of the PASID in addition to the existing NW write intention.

When the SMMU returns an ATS Translation Completion for a request that had a PASID, the Global bit of the Translation Completion Data Entry must be zero.

Note: The TDISP eXtended TEE (XT) Extensions specification [5] replaces the Global bit with the TE bit. For more information on the TE bit, see 3.9.4.2 TE bit on ATS Translation Completions .

Note: The SMMU differentiates translation contexts intended to be shared with the PE from those not shared, using the CD.ASET mechanism. Whether a global translation matches is also a function of ASET. However, no mechanism exists to indicate that all possible global translations (from all contexts used by an endpoint) share an identical address space layout so that global translations can be used. The ATS Global flag must be cleared because a non-shared context must not match global translations from a shared context (and vice versa).

Note: Arm expects that general-purpose software will require HTTU for use with PRI. See section 3.13.7 ATS, PRI and translation table flag update for more information on flag updates with ATS.

Note: PRI requires ATS to be implemented, but ATS does not require PRI to be implemented.

Note: An SMMU that does not support HTTU can support paged DMA mappings for non-PCI devices using the Stall fault model, see section 3.12 Fault models, recording and reporting . PCIe cannot be used with the Stall fault model, so a requirement for paged DMA with PCIe implies a requirement for PRI, which implies a requirement for HTTU.

Transactions that make use of ATS might differ from ordinary PCIe non-ATS transactions in several ways:

- Translation Requests that do not successfully translate, including those that would ordinarily have CD.A == 0 RAZ/WI behavior, cause an error in the endpoint (recorded in an endpoint-defined manner) or a PRI request, instead of an error or fault being recorded using the SMMU Event queue.
- Changes to translations require use of CMD\_ATC\_INV in addition to SMMU TLB invalidation.

- ATS Translated transactions might not represent Instruction/Data and/or Privileged/User marking on the interconnect to memory in the same way as Untranslated transactions.
- Pages with execute-only and no read, write or execute permissions cannot be represented, and are inaccessible when using ATS, see section 13.7 PCIe permission attribute interpretation .

## 3.9.1.1 Handling of addresses in ATS-related transactions

Note: In ATS Translation Completions and ATS Translated transactions, the address field is 64 bits wide regardless of the implemented physical address size of the system.

Note: It is possible that a buggy or malicious device issues an ATS Translated transaction with non-zero most significant address bits.

See also 13.6.2 ATS attribute overview .

If an ATS Translated transaction arrives at the SMMU with a physical address where bits above the implemented PA size are non-zero, then one of the following behaviors occurs. It is IMPLEMENTATION DEFINED which behavior occurs:

- The transaction is terminated with an abort, and no event or fault is recorded.
- The address in the transaction is truncated to the supported PA size of the SMMU as advertised in SMMU\_IDR5.OAS, and the truncated address is used for DPT checks, Granule Protection Checks, and the address that is propagated into the system if the transaction is permitted to proceed.

## 3.9.1.2 Responses to ATS Translation Requests

A Translation Request made from a StreamID for which ATS is explicitly or implicitly disabled (because of SMMU\_(R\_)CR0.SMMUEN == 0, or the effective EATS == 0b00 including where this is because of a Secure STE, or STE.Config == 0b000 ) results in an ATS Translation Completion with Unsupported Request (UR) status.

| Configuration or scenario                                                 | For an ATS Translation Request, leads to               |
|---------------------------------------------------------------------------|--------------------------------------------------------|
| SMMUEN == 0                                                               | Terminated with UR status and F_BAD_ATS_TREQ generated |
| Using a Secure StreamID                                                   | Terminated with UR status and F_BAD_ATS_TREQ generated |
| STE.Config == 0b000                                                       | Terminated with UR status                              |
| STE.Config == 0b100                                                       | Terminated with UR status and F_BAD_ATS_TREQ generated |
| Effective STE.EATS == 0b00 (Note: Includes EATS == 0b1x when ATSCHK == 0) | Terminated with UR status and F_BAD_ATS_TREQ generated |

A Translation Request that encounters an Address Size, Access or Translation fault arising from the translation process for a page, at either stage, results in an ATS Translation Completion with Success status and R == W == 0 in the Completion Data Entry for that page and no fault is recorded in the SMMU. If the R == W == 0 Translation Completion Data Entry is the first or only entry in the Translation Completion, its translation size is equal to the STU size. A Permission fault can also lead to this response, but other cases that would cause a Permission fault for an ordinary transaction might result in some, but not all, permissions being granted to the endpoint. See 13.7 PCIe permission attribute interpretation for information on permission calculation for ATS.

Consistent with Armv8-A, in a two-stage translation, the IPA to PA translation of the output address of a stage 1 Table, Block, or Page descriptor is not architecturally performed unless the descriptor is valid and no fault would arise from the descriptor. This behavior applies to a two-stage translation that is performed for an ATS Translation Request, which means that translation stops if stage 1 leads to an Address Size, Access, or Translation fault, or evaluates to a Translation Completion that grants no permissions. If the final IPA for stage 1 is valid, but does

not provide any access permissions for the Translation Request, the IPA is not translated at stage 2, and no faults from stage 2 are visible. For example, this might happen if the translation tables do not grant any Unprivileged access permissions at stage 1 and the Translation Request has an effective Priv value of 0. See 13.7.1 Permission attributes granted in ATS Translation Completions .

Note: The case of Split-stage ATS is included, because permissions are determined from both stages. For more information, see section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses .

If STE.S1DSS causes a stage 1 skip, and STE.Config == 0b101 (stage 1-only), the response is Success, U == 0, R == W == 1, identity-mapping (see 13.6 PCIe and ATS attribute/permissions handling ).

A Translation Request that encounters any configuration error (for example ILLEGAL structure contents, or external abort on structure fetch) results in an ATS Translation Completion with Completer Abort (CA) status:

| If an ordinary transaction were to trigger a . . .                                                                         | . . . an ATS Translation Request with the same properties leads to:                                                                                                                                                                                                                                                            |
|----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| C_BAD_STREAMID                                                                                                             | Terminate with CA status. If SMMU_CR2.REC_CFG_ATS == 1 and SMMU_CR2.RECINVSID == 1, the event is recorded. Otherwise, no event is recorded.                                                                                                                                                                                    |
| F_STE_FETCH C_BAD_STE F_VMS_FETCH F_CFG_CONFLICT F_TLB_CONFLICT C_BAD_SUBSTREAMID F_STREAM_DISABLED F_WALK_EABT F_CD_FETCH | Terminate with CA status. If SMMU_CR2.REC_CFG_ATS == 1, the event is recorded. Otherwise, no event is recorded.                                                                                                                                                                                                                |
| F_ADDR_SIZE F_ACCESS F_TRANSLATION                                                                                         | Success: R == W==0(access denied) This includes stage 2 faults for a CD fetch or stage 1 translation table walk.                                                                                                                                                                                                               |
| F_PERMISSION                                                                                                               | Success. R, Wand Exe permission is granted, where requested, from available translation table permissions. In the extreme case, a translation with no access permission gives R == W==0. Where F_PERMISSION arises at stage 2 for a CD fetch or stage 1 translation table walk, the response of Success and R == W==0is given. |
| GPF on output address                                                                                                      | Terminate with CA status. Note: See Interactions with PCIe ATS for details of when Granule Protection Checks are performed on the output address for ATS Translation Requests.                                                                                                                                                 |

For Event records that are recorded for ATS Translation requests when SMMU\_(R\_)CR2.REC\_CFG\_ATS == 1, the RnW field is UNKNOWN.

Note: In an SMMU for RME, F\_STE\_FETCH, F\_CD\_FETCH, F\_VMS\_FETCH and F\_WALK\_EABT can be generated as the result of a GPC fault. See 3.25.2 Interactions with PCIe ATS .

The effects of STE overrides on ATS Translation requests are described in Table 13.4 and Table 13.5.

## 3.9.1.3 Handling of ATS Translated transactions

Translated transactions generally pass through the SMMU unless one of the following applies:

- SMMUEN is disabled for the Security state of the transaction.
- A Secure stream is used.
- ATSCHK is 1 for the Security state of the transaction, and therefore additional checks are performed.

| Configuration or scenario                              | For a Translated Transaction, leads to:                                             |
|--------------------------------------------------------|-------------------------------------------------------------------------------------|
| SMMUEN == 0                                            | F_TRANSL_FORBIDDEN and aborted.                                                     |
| Using a Secure StreamID                                | F_TRANSL_FORBIDDEN and aborted.                                                     |
| STE.Config == 0b000                                    | If ATSCHK == 1, aborted.                                                            |
| STE.Config == 0b100                                    | If ATSCHK == 1, F_TRANSL_FORBIDDEN and aborted.                                     |
| Effective STE.EATS == 0b00                             | If ATSCHK == 1, F_TRANSL_FORBIDDEN and aborted.                                     |
| GPC fault on output address                            | Aborted. The GPC fault is reported as described in 3.25.4 Reporting of GPC faults . |
| STE.EATS == 0b10 if inappropriate for the protocol (1) | IMPLEMENTATION DEFINED whether F_TRANSL_FORBIDDEN and aborted.                      |

(1) Some bus protocols, for example CHI, require a translated address to represent a physical address and therefore must have Full ATS enabled. It is IMPLEMENTATION DEFINED whether the SMMU can detect cases where such protocols are in use for StreamIDs that do not have Full ATS enabled by STE.EATS = 0bx1 . If the SMMU can detect this case, then if SMMU\_(R\_)CR0.ATSCHK = 1, transactions checked by the SMMU on a protocol that can only convey a physical address are terminated with an abort and reported as F\_TRANSL\_FORBIDDEN if STE.EATS is 0b10 .

| If an ordinary transaction were to trigger a . . .                                                  | . . . a Translated transaction with the same properties leads to:                                                                                                                                                                                                                                                                                           |
|-----------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| F_UUT                                                                                               | Aborted. No event is recorded in the Event queue.                                                                                                                                                                                                                                                                                                           |
| C_BAD_STREAMID C_BAD_SUBSTREAMID F_STE_FETCH F_VMS_FETCH C_BAD_STE F_CFG_CONFLICT F_STREAM_DISABLED | If ATSCHK == 1, aborted. If ATSCHK == 1 and SMMU_CR2.REC_CFG_ATS == 1, the event is recorded in the Event queue. Otherwise, no event is recorded. Note: If ATSCHK == 0, the SMMUdoes not check configuration for Translated transactions, so does not detect these conditions. Note: Reporting of C_BAD_STREAMID is not affected by SMMU_(R_)CR2.RECINVSID. |

If a Translated transaction experiences a second stage 2 translation because of an STE.EATS == 0b10 configuration, and if a fault occurs during that stage 2 translation, then the transaction is terminated with an abort and an event is recorded in the same way as for an ordinary transaction.

If a PASID is supplied on a Translated transaction, it might be used for the purposes of determining MPAM attributes, see 17.3 PCIe ATS transactions .

If SMMU\_IDR3.PASIDTT is 0 or an ATS Translated transaction does not contain a PASID TLP prefix, the Translated transaction is treated as though it is presented to the SMMU with PnU == 0, InD == 0, and SSV == 0.

If SMMU\_IDR3.PASIDTT is 1 and an ATS Translated transaction contains a PASID TLP prefix, PnU (Priv) and InD (Exe) bits are specified by the Translated transaction.

These attributes are then overridden by STE.PRIVCFG and STE.INSTCFG as specified in Table 13.4 and considered as follows for the purposes of translation and permissions checking:

| STE.EATS           | Behavior                                                                                                                                                                        |
|--------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b01 (Full ATS)    | For Non-secure streams, no effect. For a Realm stream, then if the target PA space is Non-secure and the access is Instruction, not Data, then F_TRANSL_FORBIDDEN is generated. |
| 0b10 (Split-stage) | The attributes are input into the stage 2 translation.                                                                                                                          |
| 0b11 (Use DPT)     | Same as for 0b01 (Full ATS).                                                                                                                                                    |

The effects of other STE overrides on ATS Translated transactions are described in Table 13.5.

When processing an ATS Translated transaction with SSV = 1:

If the SMMU encounters a translation-related fault then the appropriate Event is recorded. If SMMU\_CR2.REC\_CFG\_ATS == 1 and the SMMU encounters an error when fetching a configuration structure for the ATS Translated transaction then the appropriate Event is recorded.

If SMMU\_(R\_)CR0.SMMUEN == 1 and SMMU\_(R\_)CR0.ATSCHK == 1, events for an ATS Translated transaction are reported with the following priority:

1. C\_BAD\_STREAMID.
2. F\_STE\_FETCH.
3. C\_BAD\_STE.

F\_VMS\_FETCH is only lower priority than C\_BAD\_STE. F\_VMS\_FETCH priority relative to other lower

4. If SMMU\_IDR3.PASIDTT == 1 and SSV=1: F\_VMS\_FETCH priority events in this list is IMPLEMENTATION DEFINED.
5. F\_TRANSL\_FORBIDDEN arising from any of the following:
- STE.EATS is 0b00 (ATS disabled).
- STE.EATS is 0b10 (Split-stage) and use of Split-stage ATS is not appropriate for the bus protocol.
- STE.NSCFG is 0b01 , and an ATS Translated Transaction specifies SEC\_SID == Realm and XT == 0. For more information, see 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions .
6. If SMMU\_IDR3.PASIDTT == 1 and SSV=1: C\_BAD\_SUBSTREAMID.
7. F\_STREAM\_DISABLED.
8. If SMMU\_IDR3.PASIDTT == 1 and SSV=1: Events encountered whilst trying to fetch any L1CD or CD as a result of:
- The stage 2 translation for the fetch of the L1CD or CD.
- F\_CD\_FETCH.
9. If SMMU\_IDR3.PASIDTT == 1 and SSV=1: C\_BAD\_CD.
10. If STE.EATS is 0b10 (Split-stage), then F\_ADDR\_SIZE arising from the check of the input address against IAS. Note: This is reported as a stage 1 fault.
11. If STE.EATS is 0b10 (Split-stage), translation-related events from stage 2 translation.
12. If STE.EATS is 0b11 (DPT), F\_TRANSL\_FORBIDDEN from the DPT check.

In an SMMU with SMMU\_(R\_)IDR3.DPT set to 1, Translated Transactions are subject to DPT checks.

When an ATS Translated transaction arrives at the SMMU with SEC\_SID = Realm, the following checks are performed:

1. Checks relating to SMMU\_R\_CR0.{ATSCHK, DPT\_WALK\_EN} and STE.EATS:
- SMMU\_R\_CR0.ATSCHK is RES1, therefore if STE.EATS is 0b00 , 0b01 , or 0b10 , then:
3. -For PCIe and CXL.io transactions, EATS behavior is as specified in SMMUv3.
- If SMMU\_R\_CR0.DPT\_WALK\_EN = 0, and STE.EATS = 0b11 , and the DPT check cannot be resolved by an existing DPT TLB entry, this is a DPT lookup fault, and is reported as DPT\_DISABLED at level 0, and an F\_TRANSL\_FORBIDDEN event is recorded.
- If SMMU\_R\_CR0.DPT\_WALK\_EN = 1, and STE.EATS = 0b11 , the transaction is checked against DPT configuration. If the DPT check fails because of a Device Access fault, then the transaction is terminated with an abort, and an F\_TRANSL\_FORBIDDEN event is recorded. If the DPT check fails because of a DPT lookup fault, then the transaction is terminated with an abort, an F\_TRANSL\_FORBIDDEN event is recorded, and the DPT lookup fault is reported in the appropriate register.
2. The output PA space of the transaction is determined as follows:
- If STE.EATS selected Split-stage configuration, the PA space of the transaction is determined from stage 2 translation. If this resolves to a Non-secure PA and the transaction is marked as Instruction not Data, then the transaction is terminated with an abort and an F\_PERMISSION event is recorded.
- If STE.EATS selected DPT configuration, the PA space of the transaction is determined from the DPT. This is permitted to be a previously-cached value from the result of an earlier ATS translation request, or from a fresh walk of the DPT. If this resolves to a Non-secure PA and the transaction is marked as Instruction not Data, then the transaction is terminated with an abort and an F\_TRANSL\_FORBIDDEN event is recorded.
- Otherwise, the output PA space of the transaction is determined from the input NS attribute and STE.NSCFG. If this resolves to a Non-secure PA and the transaction is marked as Instruction not Data, then the transaction is terminated with an abort and an F\_TRANSL\_FORBIDDEN event is recorded.

Note: SMMU support for the PASID TLP prefix on ATS Translated transactions is optional and therefore the SMMUmight not be able to distinguish Instruction versus Data accesses on ATS Translated transactions. The STE.INSTCFG override might force a read transaction to appear as Instruction for the purpose of Permission checks, but Arm does not a recommend this configuration.

3. The GPC for the transaction is performed, checking against the PA space determined in step 2.

Note: The TDISP eXtended TEE (XT) Extensions specification [5] introduces the XT bit, which affects how the ATS Translated transaction with SEC\_SID = Realm are handled. For more information, see 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions .

When an ATS Translated transaction arrives at the SMMU with SEC\_SID = Non-secure, the following checks are performed:

1. Checks relating to SMMU\_CR0.{ATSCHK, DPT\_WALK\_EN} and STE.EATS:
- If SMMU\_CR0.ATSCHK is 0, no checks are performed in this step.
- If SMMU\_CR0.ATSCHK is 1 and STE.EATS is 0b00 , 0b01 or 0b10 , then:

-For PCIe and CXL.io transactions the EATS behavior is as specified in SMMUv3.

- If SMMU\_CR0.DPT\_WALK\_EN = 0, and STE.EATS = 0b11 , and the DPT check cannot be resolved by an existing DPT TLB entry. This is a DPT lookup fault and is reported as DPT\_DISABLED at level 0, and an F\_TRANSL\_FORBIDDEN event is recorded.

- If SMMU\_CR0.DPT\_WALK\_EN = 1, and STE.EATS = 0b11 , the transaction is checked against DPT configuration. If the DPT check fails then the transaction is terminated with an abort, and an F\_TRANSL\_FORBIDDEN event is recorded.
2. The GPC for the transaction is performed, based on the transaction targetting Non-secure PA space.

## 3.9.1.4 ATS Invalidation timeout

A CMD\_ATC\_INV causes an ATS Invalidate Request to be sent to an endpoint and, in the case that a response is not received within the timeout period specified by ATS, Arm strongly recommends the following behavior:

- The Root Complex isolates the endpoint in a PCI-specific manner, if it is possible to do so.
- A CMD\_SYNC that waits for completion of one or more prior CMD\_ATC\_INV operations causes a CERROR\_ATC\_INV\_SYNC command error if any of the CMD\_ATC\_INV operations have not successfully completed. See 7.1 Command queue errors .
- -Note: Command processing stops and this situation is differentiated from a normal completion of a CMD\_SYNC, which avoids the potential re-use and corruption of a page that has been unmapped but whose translation was incorrectly invalidated.
- If it is not possible for an implementation to cause CERROR\_ATC\_INV\_SYNC for a CMD\_SYNC that waits for the completion of failed CMD\_ATC\_INV operations, Arm recommends that the CMD\_SYNC either does not complete or a command error must be raised. An IMPLEMENTATION DEFINED error mechanism asynchronous to the completion of the CMD\_SYNC must record information of the failure.
- -Note: This scenario is not recoverable but prevents the invalidation from appearing to have completed, leading to potential data corruption (the error is contained and propagation is avoided).
- -Note: A completion of a CMD\_SYNC without completing an invalidation might lead to corruption of a page that is subsequently re-used by different mappings.

## 3.9.1.5 ATS Invalidation errors

ACMD\_ATC\_INVthatgenerates an ATS Invalidate Request that causes a UR response from an endpoint completes without error in the SMMU. An invalidation might not have been performed in response to the command.

Note: A UR response to an invalidation can occur in several circumstances as specified by [1], including where an invalidation is sent with an out-of-range PASID value.

## 3.9.2 Changing ATS configuration

The ATS behavior of an endpoint is dependent on the STE.EATS field that is associated with the endpoint and on SMMU\_(R\_)CR0.ATSCHK. In addition to enabling extra checks on Translated transactions, ATSCHK changes the interpretation of the EATS == 0b10 encoding, and because ATSCHK is permitted to be cached in configuration caches, this means that a change to ATSCHK must be followed by invalidation of any STEs that are required to heed the new value.

Note: The EATS encodings of 0bx1 and 0b10 will respond to Translation Requests and interpret Translated transactions using different address spaces. A direct transition between these encodings might cause IPAs to be interpreted as PAs or vice-versa, which might lead to data corruption.

To enable ATS on an existing valid STE with EATS == 0b00 :

1. EATS is set to 0bx1 or 0b10 and caches of the STE are invalidated (including CMD\_SYNC to ensure completion of the invalidation)
2. ATS is enabled at the endpoint.

To disable ATS on an existing STE with EATS != 0b00 :

1. ATS must be disabled at the endpoint, the ATCs invalidated, and CMD\_SYNC used to ensure visibility of prior transactions using ATS that are in progress.
2. EATS is then set to 0b00 .

## 3. Caches of the STE are then invalidated.

EATS must not be transitioned between 0bx1 and 0b10 (in either direction) without first disabling ATS with the procedure described in this section, transitioning through EATS == 0b00 . EATS is permitted to be transitioned between 0b01 and 0b11 (in either direction) without first transitioning through EATS == 0b00 .

EATS == 0b10 is valid only when SMMU\_(R\_)CR0.ATSCHK == 1. ATSCHK must not be cleared while STE configurations (and the possibility of caches thereof) exist with EATS == 0b10 . Before clearing ATSCHK, all STE configurations with EATS == 0b10 must be re-configured to use EATS == 0b00 or EATS == 0bx1 , using the procedures described in this section.

Note: This ensures that Translated traffic using IPA addressing (originating from Translation Requests handled by a stage 1-only EATS == 0b10 configuration) does not encounter an SMMU with ATSCHK == 0, which would pass the traffic into the system with a PA.

Although ATSCHK == 0 causes EATS == 0b10 to be interpreted as 0b00 (ATS disabled), ATSCHK must not be used as a global ATS disable.

To set ATSCHK to 1:

1. Set SMMU\_(R\_)CR0.ATSCHK == 1 and wait for Update procedure to complete.
2. STEs (pre)fetched after this point will interpret STE.EATS according to the new ATSCHK value.
3. Unexpected Translated traffic that is associated with an STE with EATS == 0b00 will now be terminated.
4. ATS can be enabled on an STE as described here:
- a. Note: The STE update procedure invalidates the STE, which will invalidate any old ATSCHK value cached with it.

To clear ATSCHK to 0:

1. Ensure that the ATS is disabled for all STEs that were using EATS == 0b10 , flushing ATCs and transitioning through EATS == 0b00 .
- a. Note: After this point, there will be no relevant caches of ATSCHK.
2. Set SMMU\_(R\_)CR0.ATSCHK == 0 and wait for the Update procedure to complete.
3. STEs (pre)fetched after this point will interpret STE.EATS according to the new ATSCHK value.
4. Translated traffic now bypasses the SMMU without additional checks.
5. Split-stage ATS cannot be enabled on an STE, meaning EATS == 0b10 must not be used.

Referring to section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses and 13.6.4 Full ATS skipping stage 1 , it is possible to configure ATS for a stream where only requests made from substreams (PASIDs) return actual translations, and non-substream Translation Requests return an identity-mapped response that might be cached at the endpoint. Substream configuration (STE.S1DSS and STE.S1CDMax) therefore affects the contents of ATS Translation Completion responses and any change of this configuration must also invalidate endpoint ATCs.

## 3.9.3 SMMU interactions with CXL

The Compute Express Link Specification (CXL) [6] introduces some new features to ATS.

An SMMU implementation intended to be used with Type 1 or Type 2 CXL devices (those that issue CXL.cache transactions) must support ATS (SMMU\_(R\_)IDR0.ATS == 1).

An SMMU implementation is permitted to not check CXL.cache transactions against STE.EATS, even if SMMU\_(R\_)CR0.ATSCHK = 1.

It is a software error to configure STE.EATS = 0b10 for a StreamID associated with a CXL device that issues CXL.cache transactions. In this scenario, no event is recorded.

If the SMMU receives an ATS Translation Request that has the Source-CXL bit set, for a StreamID that has STE.EATS = 0b10 , the ATS Translation Completion has the CXL.io bit set.

If the translation for an ATS Translation Request with the Source-CXL bit set returns a memory type other than Inner Write-Back Cacheable, Outer Write-Back Cacheable, Shareable, the CXL.io bit is set in the ATS Translation Completion.

If the memory attributes for a translation request cannot be determined, for example if both stages of translation are disabled, by setting STE.S1DSS= 0b01 and STE.Config= 0b101 , and STE.SHCFG or STE.MTCFG are configured to Use incoming, then the SMMU uses default attributes of Inner Write-Back Cacheable, Outer Write-Back Cacheable, Shareable when issuing an ATS Translation Completion.

## 3.9.4 SMMU interactions with the PCIe fields T, TE and XT

The following sections describe the SMMU interactions with the T, TE and XT bits. The T bit is defined in the PCI Express specification [1], and the TE and XT bits are defined in the TDISP eXtended TEE (XT) Extensions specification [5].

## 3.9.4.1 T bit and the PCIe IDE TLP prefix fields

This section applies only when SMMU\_R\_IDR3.XT is 0.

For information on the behavior of the T bit when SMMU\_R\_IDR3.XT is 1, see:

- 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions .
- 3.9.4.4 XT and T fields on PRI messages, ATS Invalidation messages and Translation completions .

The PCI Express specification [1] includes the IDE TLP prefix. This includes a 1 bit field, T, which indicates a TEE (Trusted Execution Environment) request. This means that a TLP can be in one of three states:

1. No IDE TLP prefix.
2. With IDE TLP prefix and T=0: the transaction is encrypted and protected, and is not from a source associated with a TEE.
3. With IDE TLP prefix and T=1: the transaction is encrypted and protected, and is from a source associated with a TEE.

In an Arm system, the absence of the IDE TLP prefix, or the presence of the IDE TLP prefix with T set to 0, means the transaction is associated with Non-secure state. This applies in both directions. For example:

- Device to host transactions with T set to 0 are presented to the SMMU with SEC\_SID = Non-secure.
- CMD\_ATC\_INV and CMD\_PRI\_RESP commands issued to a Non-secure Command queue are forwarded to the PCIe Root Port with T set to 0. This also applies for a Secure Command queue if SMMU\_S\_IDR3.SAMS is 0.

An SMMU implementation does not distinguish between the absence of the IDE TLP prefix and the presence of the IDE TLP prefix with T set to 0.

A transaction with the IDE TLP prefix and T set to 1 is associated with Realm state and has an implicit input NS attribute of Realm.

Transactions arriving from PCIe (including ATS translation requests and PRI messages) with the T bit in the IDE TLP prefix set to 1 are presented to the SMMU with SEC\_SID = Realm.

PRI requests with the T bit in the IDE TLP prefix set to 1 are delivered to the Realm PRI queue.

The SMMU transmits ATS Translation Completions with a T bit value matching the T bit value in the corresponding ATS Translation Request.

CMD\_ATC\_INV and CMD\_PRI\_RESP commands issued to a Realm Command queue are issued to PCIe with T set to 1. If the StreamID in the command does not match an IDE Selective Stream RID range programmed in the Root Port, the command is not propagated further.

For CMD\_ATC\_INV, this error is reported as CERROR\_ATC\_INV\_SYNC on the next CMD\_SYNC for the queue where the command was issued.

For CMD\_PRI\_RESP, this error is not reported.

Note: Before the TDISP eXtended TEE (XT) Extensions [5] were introduced, the PCI Express [1] specification did not provide a mechanism for an ATS Translated transaction to distinguish whether it targets a Non-secure or Realm physical address. The T bit in the IDE TLP prefix only indicated whether the request is from a source associated with a TEE or not. For more information on the XT bit, see 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions .

## 3.9.4.2 TE bit on ATS Translation Completions

This section applies only when SMMU\_R\_IDR3.XT is 1.

The TDISP eXtended TEE (XT) Extensions specification [5] introduces the TE (TE Memory Attribute) bit for ATS Translation Completion TLPs. The TE bit occupies the same position in the TLP where the Global bit was previously located.

On an ATS Translation Completion for a Non-secure stream, the SMMU sets TE to 0. Note: This is consistent with the SMMUv3 behavior in which the Global bit is always set to 0 in ATS Translation Completions.

On an ATS Translation Completion for a Realm stream, the SMMU sets TE as follows:

- If the completion status is not Success, TE is 0.
- If the completion status is Success with R == W == 0, TE is 0.
- Otherwise:
- -If the translation resolved to a Non-secure PA, TE is 0.
- -If the translation resolved to a Realm PA, TE is 1.

Note: The determination of the TE bit value on ATS Translation Completions applies regardless of whether STE.EATS is 0b01 , 0b10 or 0b11 .

Note: If all stages of translation are bypassed as the result of STE.S1DSS configuration, and the Translation Completion status is therefore Success with identity-mapping, the PA space for TE calculation is derived by applying STE.NSCFG on the input NS attribute.

## 3.9.4.3 XT bit on Untranslated transactions, Translation requests and Translated transactions

This section applies only when SMMU\_R\_IDR3.XT is 1.

The TDISP eXtended TEE (XT) Extensions specification [5] introduces the XT bit, which is evaluated together with the existing T bit. The combination of these bits is interpreted as follows:

|   XT |   T | Meaning                                            |
|------|-----|----------------------------------------------------|
|    0 |   0 | Non-TEE request that must target non-TEE memory.   |
|    0 |   1 | TEE request that can target TEE or non-TEE memory. |
|    1 |   0 | TEE request that must target non-TEE memory.       |
|    1 |   1 | TEE request that must target TEE memory.           |

An SMMU client is permitted to directly present the XT and T bits to the SMMU. In this case, the SEC\_SID is determined from the bitwise-OR of T and XT:

|   T | SEC_SID     |
|-----|-------------|
|   0 | Non-secure. |
|   1 | Realm.      |

Note: An SMMU implementation does not distinguish between the absence of the IDE TLP prefix and the presence of the IDE TLP prefix with {XT, T} set to {0, 0}.

If the SEC\_SID is Realm, then the T bit is interpreted as follows:

|   T | Behavior                          |
|-----|-----------------------------------|
|   0 | Input NS attribute is Non-secure. |
|   1 | Input NS attribute is Realm.      |

Alternatively, an SMMU client is permitted to transform the XT and T bits into the following attributes that are presented to the SMMU:

- SEC\_SID = Non-secure.
- SEC\_SID = Realm, Input PAS is unspecified.
- SEC\_SID = Realm, Input PAS is Non-secure.
- SEC\_SID = Realm, Input PAS is Realm.

The XT value and Input NS attribute are then derived as follows:

| Attribute                 |   XT | Input NS attribute   |
|---------------------------|------|----------------------|
| Input PAS is unspecified. |    0 | Realm.               |
| Input PAS is Realm.       |    1 | Realm.               |
| Input PAS is Non-secure.  |    1 | Non-secure.          |

CMD\_ATC\_INV and CMD\_PRI\_RESP commands issued to a Non-secure Command queue are forwarded to the PCIe Root Port with {XT, T} set to {0, 0}. This also applies for a Secure Command queue if SMMU\_S\_IDR3.SAMS is 0.

Note: All of the behaviors specified in the following table are performed before input into the GPC, and all faults are raised with higher priority than GPC faults on the target address of the transaction.

Note: In the following table, the STE.NSCFG encoding 0b01 gives the specified behavior only if SMMU\_R\_IDR3.XT is 1. Otherwise this encoding is Reserved, behaves as 0b00 .

For an Untranslated transaction, Translation request or Translated transaction, The XT value is considered in conjunction with STE.NSCFG, as follows:

| NSCFG   | XT   | Untranslated transaction                                                                                                                                                                                         | Translation request                                                                                                                                                                                                                                                                                                                                                                                                                                          | Translated transaction                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
|---------|------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| != 0b01 | x    | The input NS attribute, STE.NSCFG and all enabled stages of translation behave as specified in SMMUv3.                                                                                                           | The input NS attribute, STE.NSCFG and all enabled stages of translation behave as specified in SMMUv3.                                                                                                                                                                                                                                                                                                                                                       | If STE.EATS selects Split-stage ATS, the output PA space is determined from stage 2 translation. If STE.EATS selects Full ATS with DPT, the output PA space is determined from the DPT configuration. If STE.EATS selects Full ATS, then the output PA space is the input NS attribute overridden by STE.NSCFG.                                                                                                                                                                                                                                                                                                                                |
| 0b01    | 0    | The input NS attribute, STE.NSCFG and all enabled stages of translation behave as specified in SMMUv3.                                                                                                           | The input NS attribute, STE.NSCFG and all enabled stages of translation behave as specified in SMMUv3.                                                                                                                                                                                                                                                                                                                                                       | Terminated with an abort, and F_TRANSL_FORBIDDEN.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| 0b01    | 1    | SMMUcomputes the expected output PA space according to all enabled stages of translation. If this does not match the input NS attribute, an F_PERMISSION is reported for the final enabled stage of translation. | SMMUcomputes the expected output PA space according to all enabled stages of translation. If this does not match the input NS attribute, an ATS Translation Completion with Success status and R ==W==0 is returned. In this case, granule protection checks are not performed. Note: If STE.EATS selects Split-stage ATS, then stage 2 translation is included in this computation, in the same way that it is included for the computation of permissions. | If STE.EATS selects Split-stage ATS, and the input NS attribute does not match the output PA space returned by the stage 2 translation, then the SMMUraises F_PERMISSION and terminates the transaction with abort. If STE.EATS selects Full ATS with DPT, and the input NS attribute does not match the output PA space returned by the DPT, then the DPT check fails as a Device Access fault. This means that the SMMUraises F_TRANSL_FORBIDDEN and terminates the transaction with abort. If STE.EATS selects Full ATS, then the output PA space is determined from the input NS attribute, and the SMMUdoes not perform any extra checks. |

## 3.9.4.4 XT and T fields on PRI messages, ATS Invalidation messages and Translation completions

This section applies only when SMMU\_R\_IDR3.XT is 1.

The SMMU ignores the XT bit on PRI requests and ATS Invalidation completions.

Note: The XT bit is always 0 on PRI requests and ATS Invalidation completions and the PCIe Root Port sets XT to 0 on PRI responses and ATS Invalidation requests.

The SMMU transmits ATS Translation Completions with both:

- A T bit value matching the T bit value in the corresponding ATS Translation Request.
- The XT bit value matching the XT bit value in the corresponding ATS Translation Request.