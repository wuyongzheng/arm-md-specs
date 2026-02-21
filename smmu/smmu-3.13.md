## 3.13 Translation tables and Access flag/Dirty state

The SMMU might support Hardware Translation Table Update (HTTU) of the Access flag and the dirty state of the page for AArch64 translation tables.

Some Armv8-A PEs might support Hardware Update to Access flag and dirty state [2]. SMMU support of HTTU can coexist with both hardware and software flag update from the PEs. The SMMU update of descriptors behaves in an identical manner to those described in [2], with the additional SMMU-specific behavior in section 3.13.4 HTTU behavior summary , although its configuration method differs.

HTTU increases the efficiency of maintaining Access flag and dirty state in translation tables. A single translation table can be shared between any combination of agents that perform software updates of flags, and other agents that perform HTTU. Agents supporting HTTU update the flags atomically. Software must also use atomic primitives to perform its own updates on translation tables when they are shared with another agent that performs HTTU.

Note: In general, an update of the Access flag and the dirty state of the page in a system is associated with the use of dynamic paging and, in the context of the SMMU, associated with DMA targeting paged memory. Arm does not expect applications that constrain DMA access to static, pinned or non-paged mappings to perform or require dynamic update to the Access or to the dirty state of the page.

Support for HTTU is indicated by SMMU\_IDR0.HTTU, and can be one of the following:

- No flag updates are supported.
- Only Access flag updates are supported.
- Update of both the Access flag and the dirty state of the page is supported.

If HTTU is supported, separate enable bits in the CDs and STEs determine whether a particular stage 1 or stage 2 translation table (referenced from the CD or STE) is updated in this manner, and the scope of the updates.

Note: It is possible for several CDs to reference the same translation table, or for several STEs to reference the same CD. Where translation tables are shared between CDs that contain the same ASID (within a translation regime), the CD HA and HD fields must be identical. See section 5.4.1 CD notes .

Note: Accessed means a translation to which an access has been made. Software might attempt to detect a working set by clearing the Access flags and observing which flags are set again. Dirty state of the page means a writable translation to which a write access or other modification has been made. When reclaiming or repurposing a Dirty page, software might preserve the modifications to storage. Clean means a writable translation to which a modification has not been made. When reclaiming or repurposing a Clean page, software might simply discard the page contents (as another up-to-date copy might be available in storage elsewhere).

## 3.13.1 Software update of flags

Note: In the context of a PE that does not support HTTU, software is generally expected to maintain the Access flag and the dirty state of a page, where required, as follows:

- A read or write that fetches a translation table descriptor with AF == 0 causes an Access fault, if AFFD == 0. An exception handler marks the descriptor as AF == 1 and retries the instruction that caused the access. Agents are not permitted to cache such entries in TLBs. No TLB invalidation is required when setting AF to 1.
- A Dirty state is usually implemented in software by write-protecting a translation. A write access to such a translation generates a Permission fault, at which point the exception handler might rewrite the descriptor to mark it writable. The exception handler might use additional software structures or a software-defined descriptor flag to differentiate a genuinely non-writable page from a page that is only temporarily non-writable in order to generate the Permission fault. In this arrangement, a descriptor that has write permission is considered to be writable-dirty and a descriptor that has no write permission but is marked as temporarily unwritable is considered to be writable-clean .
- A write to a genuinely non-writable page is an error. A write to a writable-clean (temporarily non-writable) page causes the page to become writable-dirty. A write to a writable-dirty page causes no additional state change.

- An Access fault takes priority over a Permission fault. That is, a write to a writable-clean page with AF == 0 and AFFD == 0 causes an Access fault, and only after AF == 1 does a Permission fault occur.

When pinned DMA translations are used with an SMMU, software can update the translation flags as appropriate to the expected access. Arm does not expect faults to be generated when pinned translations are used, and such faults represent a programming error. Arm expects software to use the Terminate model for such scenarios, so that faulting transactions are terminated.

An SMMU can operate in a similar manner to the PE example when using unpinned DMA translations, so that transactions that are translated by the SMMU cause faults to be recorded and the SMMU driver software sets descriptor state in response to these records. For more information about faults, see section 3.12 Fault models, recording and reporting .

Where this is the case, Arm recommends that this is implemented using the Stall model. Arm expects that the SMMUdriver maintains software Access or dirty state by doing one of the following:

- Responding to an F\_ACCESS fault by setting AF to 1 in the relevant translation table descriptor.
- Responding to an F\_PERMISSION fault for write to a writable-clean page by marking the page as writable-dirty.
- Finally, issuing a CMD\_RESUME to the SMMU to retry the transactions held up due to the fault

Note: The AFFD field in a stage 1 and stage 2 configuration modifies the behavior of the AF flag of a descriptor. A descriptor, at a translation stage with AFFD == 1, and AF == 0 does not cause an F\_ACCESS to be generated. Instead, the translation is used as though AF == 1. This configuration is only relevant where HTTU is not used.

A translation table can be shared between multiple agents, if all agents that update the Access flag and the dirty state of the page use the same semantics to differentiate a descriptor marked non-writable from one marked temporarily non-writable. Usually, this is a software-defined bit that flags a page as potentially writable as opposed to a page that is intended to always be non-writable.

HTTU removes the fault record and software handling from the path of updating translation table flags. An agent is permitted to perform HTTU on a translation table that might be shared with an agent performing software update. The Dirty Bit Modifier field has been added in Armv8.1-A to differentiate non-writable and writable-clean states. For more information about the Dirty Bit Modifier, see section 3.13.3 Dirty state hardware update . Software intending to provide software-updated translation table descriptor flags from one agent (for example a PE without HTTU) while sharing translations with another agent that uses HTTU must use the DBM flag convention, and perform atomic updates.

## 3.13.2 Access flag hardware update

When HTTU is supported and enabled for a stream, a translation that causes an SMMU fetch of a descriptor with AF == 0 that would, without HTTU and with AFFD == 0, have caused an Access fault performs an atomic update to set AF == 1 in the descriptor. Note: This includes stage 2 translation for the fetch of an L1CD or CD.

The SMMU never clears AF.

If access to a descriptor causes a permission fault, it is UNKNOWN whether the AF flag of the descriptor is updated to 1.

When HTTU is disabled, or not supported by the SMMU, a transaction that leads to access of translations with AF == 0 and AFFD == 0 causes F\_ACCESS.

If the update of the dirty state of the page takes place, the final translation table descriptor will also have AF == 1.

## 3.13.3 Dirty state hardware update

## 3.13.3.1 Direct Permission Scheme

In order to coexist with an agent that is not using hardware update, HTTU defines a new flag, at bit[51] of Block and Page descriptors, called the Dirty Bit Modifier (DBM). The DBM bit marks the overall intention of a translation as ultimately writable, to differentiate a non-writable page from a writable-clean page in the same

way as a software-maintained mechanism would. The DBM bit only applies to a stage of translation that uses the Direct Permission Scheme.

Note: The Armv8-A stage 1 descriptor field AP[2:1] has no bit[0]. The stage 2 equivalent is named S2AP[1:0].

When HTTU of the dirty state of a page is supported and enabled for the stream, a non-writable descriptor is automatically marked as writable by the SMMU when a translation for a write occurs, if it is a descriptor with DBM== 1. A Permission Fault is not generated, and the translation continues.

Specifically, if a descriptor is read-only only as a result of AP[2:1] == 0b1x at stage 1, or non-writable using S2AP[1:0] == 0b0x at stage 2, then if DBM == 1 and a translation for write occurs, the SMMU atomically sets AP[2] to 0 in the descriptor held in memory, in a coherent manner if appropriate. If DBM == 0, the page has no write permission and a write translation results in a Permission fault.

Note: HTTU of the dirty state of a page is not applicable to a descriptor that is made effectively read-only because of the hierarchical control of access permissions using APTable. All references to page or block permissions in this section are made on the assumption that the page or block is otherwise accessible, will not generate a Permission fault for other reasons, such as PAN or the APTable having removed access, and that a page is only read-only (or otherwise non-writable) because of the page or block AP/S2AP permissions.

When the APTable does not remove write access:

- A read-only stage 1 descriptor has DBM == 0 and AP[2:1] == 0b1x . A non-writable stage 2 descriptor has DBM== 0 and S2AP[1:0] == 0b0x .

A write causes a Permission fault as the page has no write permission.

The software fault handler invokes an error-handling routine. Because DBM == 0, the software handler can determine that the page is not allowed to be written. In the case of an SMMU stalled fault, software can use CMD\_RESUME to terminate an erroneous transaction.

- A writable-clean translation table descriptor has DBM == 1 and AP[2:1] == 0b1x /S2AP[1:0] == 0b0x .

Without HTTU, this descriptor is Non-writable and a write causes a Permission fault. Because DBM == 1, the page is intended to be writable and the software fault handler can mark the page as dirty by setting AP[2] == 0/S2AP[1] == 1 and performing the appropriate TLB invalidation. The page is now marked writable-dirty. In the case of an SMMU stalled fault, software can use CMD\_RESUME to retry the transaction, which might then continue without fault.

When HTTU is enabled, a write transaction causes the SMMU to atomically set AP[2] == 0 or S2AP[1] == 1 as appropriate, and then allows the write to proceed.

- A writable-dirty descriptor has AP[2] == 0/S2AP[1:0] == 0b1x .

With or without HTTU, this page is writable and will not generate a Permission fault on a write.

Note: Although DBM is ignored by hardware in this state, it might be useful for software to use the convention of leaving DBM == 1 when a page AP[2] transitions from non-writable to writable. This allows the DBM bit to be used as a one-bit flag to indicate that, overall, a page is intended to be written regardless of its current Clean or Dirty state.

- The SMMU never sets or clears DBM.
- The SMMU never clears S2AP[1].
- The SMMU never sets AP[2]. A descriptor is never made writable by the SMMU unless DBM == 1.

The SMMU never sets S2AP[1] == 1 for the stage 2 translation for the fetch of an L1CD or CD.

## 3.13.3.2 Indirect Permission Scheme

When the Indirect Permission Scheme is used for stage 1 Base permissions, CD.HD exclusively defines whether the dirty state is managed by hardware or software.

When the Indirect Permission Scheme is used for stage 2 Base permissions, STE.S2HD exclusively defines whether the dirty state is managed by hardware or software.

Note: If the Indirect Permission Scheme is in use for a stage of translation, there is no DBM field in either the Block or Page descriptor.

## 3.13.4 HTTU behavior summary

SMMUHTTU operation has the same behavior as described in Hardware Updates to Access Flag and dirty state in the Armv8.9-A architecture [2].

The following HTTU behavior is specific to the SMMU:

- A descriptor update that occurred because of a completed ATOS translation is made visible to the required Shareability domain, as specified by the translation table walk attributes, by completion of a CMD\_SYNC that was submitted after the ATOS translation began.
- Adescriptor update that occurred because of a completed incoming transaction is made visible to the required Shareability domain (as specified by the translation table walk attributes) by completion of a CMD\_SYNC that was submitted after the completion of the incoming transaction.
- -In addition, the completion of a TLB invalidation operation makes descriptor updates that were caused by transactions that are themselves completed by the completion of the TLB invalidation visible. Both broadcast and explicit CMD\_TLBI\_* invalidations have this property.

The SMMU HTTU behavior follows the same rules as the A-profile architecture[2], including all TLB invalidation completion requirements on HTTU visibility, with the following exception:

- If stage 2 hardware update of Dirty state is enabled, the SMMU is permitted to speculatively update the Dirty state of a stage 2 descriptor used for a stage 1 translation table walk, even if stage 1 hardware updates of Access flag or Dirty state are disabled. Note: In the A-profile architecture[2] this is only permitted if stage 1 hardware updates of Access flag or Dirty state are enabled.

## 3.13.5 HTTU with two stages of translation

When two stages of translation exist, multiple translation table descriptors determine the translation, that is the stage 1 descriptor, the stage 2 descriptors mapping all steps of the stage 1 walk, and finally the stage 2 descriptor mapping the IPA output of stage 1. Therefore one access might result in several descriptor updates. Figure 3.9 shows an example:

## Chapter 3. Operation

3.13. Translation tables and Access flag/Dirty state

Figure 3.9: Example Hardware flag update with nested translation

<!-- image -->

Note: Figure 3.9 is an example procedure and does not depict all permitted ways of performing a nested translation walk with HTTU enabled.

Because a stage 1 descriptor hardware update is a write, the stage 2 mapping for its IPA must allow writes for the update to succeed.

## 3.13.6 Access flag in Table descriptors

An SMMU that supports HTTU might also support hardware update of Access flag in Table descriptors. This functionality is indicated by SMMU\_IDR0.HTTU and can be enabled in stage 1 and stage 2 translation independently using the following controls:

| Stage of translation   | Control field   |
|------------------------|-----------------|
| Stage 1                | CD.HAFT         |
| Stage 2                | STE.S2HAFT      |

If hardware update of Access flag is disabled for a translation stage, then hardware update of Access flag in Table descriptors is also disabled.

The SMMU behaviors for hardware update of Access flag in Table descriptors are the same as in the PE architecture, including the following requirements:

- When the Access flag in a Table descriptor must be updated.
- When the Access flag in a Table descriptor is permitted to be updated.

- If HAFT is enabled, then any Table entry with the Access flag clear is not permitted to be cached in a TLB.
- The ordering requirements for hardware update of Access flag in a Table descriptor relative to hardware updates of other descriptors updated in the translation table walk, and the final access.

Hardware updates of Access flag in Table descriptors are made observable by completion of a CMD\_SYNC in the same manner as hardware updates of the Access flag in page or block descriptors. See section 3.13.4 HTTU behavior summary .

Hardware updates of Access flag in Table descriptors are caused by ATS Translation Requests in the same manner as hardware updates of the Access flag in page or block descriptors. See section 3.13.7 ATS, PRI and translation table flag update .

## 3.13.7 ATS, PRI and translation table flag update

When ATS and PRI are used to support device access to dynamically paged memory, the Access state and the dirty state of the page need to be maintained. This section describes the SMMU page flag maintenance behavior in a system using ATS with PRI targeting dynamically paged memory.

Note: Maintenance of the Access flag and the dirty state of the page is primarily of importance to DMA to unpinned or paged memory, because use-cases with DMA to pinned memory would normally statically initialize page state.

## 3.13.7.1 Hardware flag update for ATS &amp; PRI

Because the purpose of ATS is to cache translations outside the SMMU and to avoid subsequent translation interaction with the SMMU, if HTTU is enabled it is performed at the time of the ATS Translation Request (TR).

When an ATS TR is made, it must be assumed that a device will subsequently access the page. If the page is otherwise valid and an ATS response will be returned, AF is set to 1 in the descriptor in the same way as a direct transaction access through the SMMU.

In addition to the behavior that is described earlier in this section, if hardware-management of dirty state is enabled and an ATS request for write access (with NW == 0) is made to a page that is marked writable-clean, the SMMU assumes a write will be made to that page and marks the page as writable-dirty before returning the ATS response that grants write access. When this happens, the modification to the page data by a device is not visible before the page state is visible as writable-dirty. If HTTU is only enabled for Access, an ATS request for a write to a writable-clean or Read Only page results in an ATS Translation Completion with W == 0, and write access is denied.

If an ATS Translation Request is made for a write (NW == 0) to a nested translation configuration and the associated stage 1 translation is read-only (not writable), the dirty state is not updated in either of the stage 1 descriptor, or the stage 2 descriptor that is used to translate the output address from the stage 1 descriptor.

Note: This also applies if the stage 2 translation of the stage 1 output address is writable-clean.

When HTTU is enabled for stage 1 and stage 2 and Split-stage ATS is used (STE.EATS == 0b10 ), the ATS TR performs HTTU at stage 1, and updates for the stage 2 descriptors that are used to fetch and update the stage 1 descriptors are made. The following applies to the stage 2 descriptor for the final IPA:

- The AF in the stage 2 descriptor for the final IPA is permitted to be speculatively set to 1 by the ATS TR.
- If write permission is granted in the ATS Translation Completion, a writable-clean stage 2 descriptor for the final IPA is permitted to be marked as writable-dirty by the ATS TR.
- -When a subsequent Translated access to the IPA is translated, this choice does not affect the HTTU behavior of stage 2.
- -This choice does not affect the permissions that are returned in the Translation Completion, which reflect whether a write transaction is permitted by the combined permissions of both stages and treat a writable-clean stage 2 descriptor as writable. See section 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses .
- The stage 2 translation of a subsequent Translated access marks the stage 2 descriptor as Accessed and might mark the descriptor as writable-dirty, provided that the ATS TR has not already performed this action.

## 3.13.7.2 Behavior with respect to flag maintenance for ATS &amp; PRI without HTTU

If HTTU is not enabled for the Access flag, an ATS request to a page with AF == 0 and AFFD == 0 is denied. For this address a response granting R == W == 0, that is no access, is returned. The client device might then raise an error in a device-specific manner, or might issue a PRI page request, if supported and configured, to request that software makes the page available. Software can manually set AF == 1 on receipt of the PRI page request in anticipation of the device access.

An ATS request to any read-only page does not grant write access, that is it returns W == 0, if hardware update of dirty state of the page is not enabled. Read access might be granted in the response, if the conditions for the Access flag set out in this section are satisfied. The client device might raise an error in a device-specific manner, or might issue a PRI page request to request write access to the address. On receipt of a PRI request, software could assume that a request issued for write was initiated because data will shortly be written and mark the page writable-dirty before responding to the PRI request.

An ATS request for write to a page marked writable might grant write access, that is it returns W == 1 in the response. Software must consider writable pages as potentially dirty.

Note: PCIe PRI requests can be issued speculatively by an Endpoint. This implies speculatively marking the page as Dirty. This is not permitted by the Armv8-A architecture [4] and might be problematic for some software systems.

Because pages cannot speculatively be marked as Dirty, Arm recommends that a system designed for general-purpose software supports HTTU when PRI is used, so that the state of the page is marked Dirty only when a request for write access is made using ATS.

## 3.13.8 Hardware flag update for Cache Maintenance Operations and Destructive Reads

HTTU for Dirty state update is not performed for the following operations:

- Invalidate Cache Maintenance Operations.
- Destructive Reads.
- Destrutive Hints.

See also:

- 16.7.2.2 Permissions model for Cache Maintenance Operations
- 3.22.2 Permissions model

When these operations are performed to a writable-clean translation table descriptor, the descriptor is not updated to be writable-dirty. If the required Read or Execute permissions are available, but the descriptor is not writable-dirty, the operations are downgraded as described in the corresponding section.

This rule does not affect HTTU of the Access flag, which occurs if required. In this case, an update to the Dirty state of the stage 2 descriptor that translates the stage 1 table is performed.

Note: For the purposes of determining execute permission, a writable-clean descriptor is considered to be writable when HTTU is enabled, which is consistent with the Armv8-A architecture. As described in this section, this principle applies even when the descriptor is not updated to writable-dirty for an Invalidate, DR or DH.