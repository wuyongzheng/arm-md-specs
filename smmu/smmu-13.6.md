## 13.6 PCIe and ATS attribute/permissions handling

This section covers an area of system architecture that intersects with the SMMU operation. Integration of PCIe, particularly with ATS, requires consideration of the presentation of transactions to the SMMU from the Root Complex and the overall system architecture, including platform definitions such as Server Base System Architecture [12], in addition to that of the SMMU itself.

In many systems it will be typical to have a discrete Root Complex IP block connected to a downstream SMMU IP block by a standard piece of interconnect fabric, for example using AXI. This section considers the attributes provided to the SMMU by the Root Complex on such an upstream interconnect in relation to the output attributes provided by the SMMU downstream into the system.

## 13.6.1 PCIe memory type attributes

PCIe does not contain memory type attributes, and each transaction takes a system-defined memory type when it progresses into the system. The Server Base System Architecture [12] requires the base memory type to be cacheable shared (IO-coherent).

Note: When PCIe is used with an SMMU, the SMMU can assign a different attribute if necessary, but the common usage model is for PCIe DMA to remain cacheable shared and the SMMU is primarily used for address transformation/protection rather than attribute assignment.

Note: SBSA requires that, when no SMMU is present or an SMMU is present and in global or stream bypass mode, a transaction from a Root Complex targeted at memory is presented to the memory system with a fixed attribute of cached, shared. The exact attribute will be Normal-iWB-oWB-ISH or OSH and is system-dependent, but is considered fixed/static because PCIe does not encode different memory types. The system must treat transactions that are targeted at devices (such as MSIs) as Device type accesses.

When an SMMU is used with translation (i.e. not in bypass mode), its configuration might use Stage 1/Stage 2 translation and/or STE input overrides, determining an output attribute from a function of the input, translation table descriptor and override attributes as described previously in this chapter. The final attribute is defined by software configuration.

Note: See No\_snoop below, which might alter the output final attribute.

Note: See SMMU\_GBPA and STE.{MTCFG,ALLOCCFG,SHCFG}: it is IMPLEMENTATION DEFINED whether attribute overrides affect streams associated with PCIe devices or whether the incoming attribute is used. Arm does not expect attribute overrides to be required for PCIe devices.

## 13.6.1.1 No\_snoop

Note: In PCIe, No\_snoop is not guaranteed to be supported by a device or Root Complex, and if it is supported by a device, it might be disabled via configuration space. When a transaction includes a No\_snoop == 1 flag, it indicates that the transaction is allowed to 'opt-out' of hardware cache coherency; software cache coherency ensures the access would not hit in a cache, so the I/O access is permitted to avoid snooping caches.

In an Arm system, a No\_snoop access corresponds to Normal-iNC-oNC-OSH.

Support for No\_snoop is system-dependent and, if implemented, No\_snoop transforms a final access attribute of a Normal cacheable type to Normal-iNC-oNC-OSH downstream of (or appearing to be performed downstream of) the SMMU. No\_snoop does not transform a final access attribute of any-Device.

No\_snoop applies after the application of the STE.S2FWB bit.

Note: This is consistent with SBSA's requirements of No\_snoop.

Note: To achieve this 'pull-down' behavior, the No\_snoop flag might be carried through the SMMU and used to transform the SMMU output downstream.

## 13.6.2 ATS attribute overview

It is IMPLEMENTATION DEFINED whether an SMMU implementation assigns attributes (of memory type, Shareability and allocation hints) to ATS 'Translated' transactions consistent with the result of an 'Untranslated' transaction to the same address, or whether ATS Translated transactions have the fixed cached, shared attribute applied.

Note: An ATS client makes a Translation Request to the SMMU and caches the resulting Physical Address in its local Address Translation Cache (PCI terminology for a remote TLB). When a client has successfully received a translation, it might use it later to make direct physically-addressed ('Translated') accesses to the page, which are intended to bypass SMMU translation altogether. However, the PCIe [1] ATS protocol does not explicitly provide a field to convey a memory type/access attribute to the client in the completion of the Translation Request, therefore the subsequent Translated transaction is issued from the endpoint with no attributes (beyond R/W).

When a regular 'Untranslated' (non-ATS) transaction is forwarded to the SMMU by the Root Complex, the incoming attribute is constant, fixed at cacheable shareable as above. The SMMU applies an outgoing attribute determined from a function of input, input overrides and translation table descriptors, so the outgoing attribute is address-dependent.

When a Translated transaction (from ATS) is forwarded to the SMMU, it is intended to bypass address translation in the SMMU and, if ATS attributes are supported, the SMMU modifies the transaction's attributes as appropriate for the accessed page.

Note: If ATS attributes are not supported, the resulting output attribute from a Translated transaction might not match that of a non-ATS/Untranslated access to the same address. This is acceptable in systems for which an attribute mismatch does not present a loss of correctness, or where it is expected that the SMMU-assigned attribute will always be consistent with the fixed cached, shared attribute.

If ATS attributes are supported, the mechanism for assigning an attribute to a Translated transaction is IMPLEMENTATION SPECIFIC.

Note: In versions of the SMMU architecture up to and including SMMUv3.3, an SMMU implementation might store translation-specific attributes in the otherwise unused, most significant bits of the physical address fields in ATS Translation Completions and ATS Translated transactions. This is referred to as Attribute stashing. In SMMUv3.3 implementations, if SMMU\_ROOT\_IDR0.REALM\_IMPL == 1, the SMMU never performs Attribute stashing, and always returns zeros in the most significant bits of the physical address field above its implemented physical address size in ATS Translation Completions. From SMMUv3.4, Attribute stashing is forbidden.

## 13.6.2.1 Supporting No\_snoop with ATS

Arm recommends that, in systems that support No\_snoop, it behaves as though the flag passes through the SMMU to downgrade any output cacheable shareable type into non-cached post-SMMU, consistent with SBSA.

If the SMMU supports the encoding of attributes into ATS, the mechanism for determining the ATS Translated attribute in the SMMU is independent of the subsequent application of a No\_snoop non-cacheable/downgraded attribute.

The N field in ATS Translation Completions is always 0. The SMMU does not provide means to control No\_snoop per-page.

## 13.6.3 Split-stage (STE.EATS == 0b10 ) ATS behavior and responses

When Split-stage ATS is enabled for a stream (that is, when STE.EATS == 0b10 , SMMU\_CR0.ATSCHK == 1 and STE.Config == 0b111 ), the response to an ATS Translation Request contains an IPA. When a Translated transaction is emitted as a result of this response, its IPA then undergoes stage 2 translation in the SMMU.

Note: In effect, the stage 1 V A to IPA translation is held in the ATC but stage 2 IPA to PA translation is still performed in the SMMU. This can be used to increase security/isolation over regular nested EATS == 0b01 ATS, where the system does not trust the endpoint to use physical addresses directly.

The behavior of Split-stage ATS is the same as regular EATS == 0b01 ATS with nested translation, except:

- The completion contains the IPA result from the Stage 1 translation of the requested V A (instead of the output PA from stage 1+stage 2 translation of the requested V A).
- If the SMMU supports the encoding of attributes into ATS (see section 13.6.2 ATS attribute overview ), an attribute is returned that gives a final output equivalent to the Stage 1+Stage 2 combined attribute when the resulting ATS Translated transaction is subject to stage 2 translation in the SMMU.
- -Note: This might be implemented as returning a Stage 1 attribute which is later combined with that of stage 2 in the SMMU, or might be implemented as returning a stage 1+2 combined attribute which might later be passed through stage 2 (or combined with stage 2 a second time, which gives the same result).
- HTTU might be performed by the stage 2 translation that occurs as part of the ATS Translation Request, or it might be performed at the time of the stage 2 translation for a subsequent Translated transaction.

All other aspects are identical to regular EATS == 0b01 ATS with nested translation:

- Permissions are granted from the combination of the stage 1 and stage 2 translation permissions (see 13.7 PCIe permission attribute interpretation ), with respect to the permissions requested in the Translation Request.
- The maximum permissible translation size is derived from the intersection of stage 1 and stage 2 page/block sizes. Arm recommends that, for performance reasons, the maximum translation size is returned where possible.
- -Note: The largest translation size is the minimum of the stage 1 and stage 2 translation sizes for the given address, such that the returned translation represents a single span with constant permission and translation.

See 13.6.5 Split-stage ATS skipping stage 1 for behavior of STE.S1DSS skipping stage 1.

The behavior of an incoming Translated transaction differs when the EATS configuration of the StreamID presenting the transaction is 0b10 :

- When EATS == 0b01 , the Translated transaction is presented directly to the output. The given address is treated as a PA. If the SMMU supports the encoding of attributes into ATS, the attribute encoded in the Translated transaction is used as the output attribute, otherwise the (fixed) input attribute is output.
- When EATS == 0b10 , the Translated transaction provides an IPA. This IPA is subject to stage 2 translation (which might generate faults and events) and, if successful, provides the PA for output. If the SMMU supports the encoding of attributes into ATS, the attribute encoded in the Translated transaction is input to stage 2, otherwise the transaction's (fixed) input attribute is input to stage 2. The stage 2 translation's attribute combines with the input to stage 2 to form the output, in the same way as for any other stage 2 translation. The behavior for permission attributes overrides on ATS Translated transactions is described in 13.7 PCIe permission attribute interpretation .

EATS == 0b10 configuration is only usable when SMMU\_CR0.ATSCHK == 1.

Note: ATSCHK == 1 causes Translated transactions to look up and be checked against STE configuration, which for EATS == 0b10 provides the stage 2 with which to translate and for EATS == 0b01 allows the transaction to bypass without translation.

## 13.6.4 Full ATS skipping stage 1

When all of the following are true, transactions arriving without a PASID are configured to skip stage 1 translation:

| STE.Config == 0b1x1   | (Stage 1 translation enabled)           |
|-----------------------|-----------------------------------------|
| STE.EATS == 0b01      | ('Full ATS' enabled)                    |
| STE.S1CDMax != 0      | (Substreams/PASIDs enabled)             |
| STE.S1DSS == 0b01     | (non-PASID transactions bypass Stage 1) |

If stage 2 translation is enabled (STE.Config == 0b11x ), an ATS Translation Request without a PASID is translated stage 2-only as though STE.Config[1:0] == 0b10 . The Translation Completion returns a PA from the stage 2-only translation.

Where a stage 1 + stage 2 configuration has the first stage skipped due to STE.S1DSS == 0b01 , the translation process behaves as though stage 1 were not configured (corresponding to STE.Config == 0b1x0 ). If ATS attributes are supported, the final attribute is therefore determined by the (fixed) upstream input attribute, replaced by STE overrides where configured, and combined with the attribute from the stage 2 translation table descriptor.

If stage 2 is not enabled, an ATS Translation Request without a PASID made to this configuration skips the single translation stage and, if a fault or configuration error has not occurred, its Translation Completion returns a direct-mapped 'pass-through' of the stage. Responses to requests that lead to faults and configuration errors are described in section 3.9.1.2 Responses to ATS Translation Requests .

This is encoded as an identity-mapped Translation Completion containing:

- U == 0
- R == 1
- W==1
- TranslatedAddress 1:1/identity-mapped with Translation Request's Untranslated Address
- Translation size containing at least the requested Untranslated Address
- -Note: An implementation might return a larger identity-mapped region, as any address accessed under the same StreamID/configuration conditions will result in this type of response. A larger region might avoid future page-by-page translation requests.
- -The maximum permissible translation size is the same as the OAS (see section 3.4 Address sizes ).
- Note: As this response is made for an ATS Translation Request received without a PASID, the request cannot contain Execute\_Requested == 1 or Privileged\_Mode\_Requested == 1 as these fields are carried in a PASID. The response is made with Execute\_Permitted and Privileged\_Mode\_Access both 0.
- Note: This response causes the function to make 1:1 accesses to physical addresses, equivalent to the behavior of untranslated non-ATS transactions from the same stream.

The output attribute is a function of the (fixed) upstream input attribute replaced by STE overrides (where configured); this can be evaluated at the time of the Translation Request and encoded into the returned Translated Address as per section 13.6.2 ATS attribute overview .

## 13.6.5 Split-stage ATS skipping stage 1

Where all of the following are true, a Translation Request without a PASID is configured to skip stage 1 translation, but the ATS configuration is for stage 1-only:

- STE.Config[1:0] == 0b11 (Stage 1 and 2 translation enabled)
- STE.EATS == 0b10 (Split-stage ATS enabled)
- STE.S1CDMax &gt; 0 (Substreams/PASIDs enabled)
- STE.S1DSS == 0b01 , (non-PASID transactions bypass stage 1)

The Translation Request might lead to a fault or configuration error that triggers an ATS response as described in section 3.9.1.2 Responses to ATS Translation Requests .

Note: Even if stage 1 is effectively bypassed, a stage 1 Address Size Fault might occur if the input address supplied in the Translation Request is greater than the IAS.

Note: A Permission fault leads to one or more of R, W and X permissions being denied in the response, as shown in the next paragraph.

Where a Translation Request with a Split-stage ATS configuration skips stage 1, the Translation Request supplies an IPA address and, if a fault or configuration error does not occur, an identity-mapped Translation Completion is

returned, which contains:

- U == 0
- R and W permissions are granted from the stage 2 permissions for the IPA, with respect to the permissions requested in the Translation Request.
- TranslatedAddress 1:1/identity-mapped with the Translation Request's IPA.
- The maximum permissible translation size is that of the stage 2 translation. Arm recommends that, for performance reasons, the maximum translation size is returned where possible.
- Note: See 13.6.4 Full ATS skipping stage 1 ; this response is made with Execute\_Permitted and Privileged\_Mode\_Access both 0 as it is in response to a request made without a PASID.

If the SMMU supports the encoding of attributes into ATS (see 13.6.2 ATS attribute overview ), an attribute is returned that causes the resulting ATS Translated transaction to have a final output (after Stage 2 translation in the SMMU) equivalent to the (fixed) upstream input attribute, replaced by STE overrides (where configured), combined with the Stage 2 translation's attribute.

Note: This might be implemented by returning the constant input attribute (cached, shareable) replaced by STE overrides, and later combining that during stage 2 translation. Or, this might be implemented by returning the input (with STE overrides) combined with stage 2 translation and either passing the Translated transaction's attribute through or combining it with stage 2 translation again (which gives the same result).

The function then performs Translated accesses with IPAs and these are translated stage 2-only in the same way as described above for Split-stage ATS that does not skip stage 1.