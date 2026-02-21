## 4.5 ATS and PRI

These commands issue outgoing requests on the SMMU ATS port, to a connected Root Complex.

Software must not use these commands if ATS and PRI are not fully supported by all system components beyond the SMMU, such as a Root Complex or Endpoint, even if SMMU ID registers indicate support within the SMMU. An SMMU and system remain fully functional even if these commands are used without full system ATS and PRI support and do not deadlock. In this scenario these commands are IGNORED.

Note: The StreamID is either Non-secure or Realm. ATS and PRI are supported only for Non-secure streams and Realm streams.

## 4.5.1 CMD\_ATC\_INV(StreamID, SubstreamID, SSV, Global, Address, Size)

<!-- image -->

Sends an invalidation request to StreamID, and SubstreamID when SSV == 1, for translations spanned by Address plus span of 4096 * 2 Size . The Address span is aligned to its size by the SMMU. The effective value of Address[11 + Size:0] is taken as zero.

All bits of Address[63:N] are conveyed to the endpoint, where N == 12 + Size.

A Size value of 52 corresponds to a 2 64 byte span, meaning invalidate all. Use of values greater than 52 in an otherwise valid CMD\_ATC\_INV are permitted, but not required, to raise a CERROR\_ILL, or might cause an UNKNOWN span to be used, which might mean no invalidation occurs.

In systems that do not support PASIDs, SubstreamID is IGNORED and SSV must be 0. If SSV == 1, one of the following CONSTRAINED UNPREDICTABLE behaviors occurs:

- The command behaves as though SSV == 0, issuing an invalidate to the given StreamID without a PASID TLP prefix.
- The command has no effect.

In systems that support PASIDs, a PCIe PASID TLP prefix containing SubstreamID is used on the ATS Invalidation Request message when SSV is set to 1. In addition, setting the Global (G) parameter to 1 when SSV == 1 sets the Global Invalidate flag in the Invalidation Request. The Global parameter is IGNORED when SSV == 0.

Note: In the PCIe ATS protocol, the Global Invalidate flag in the Invalidation Request message is Reserved when no PASID prefix is used.

Note: When SSV == 1, SubstreamID is always used as the PASID in the PASID TLP prefix. Global has no effect on this property.

Note: If the SMMU is configured, through STE.S1DSS == 0b10 , to treat non-PASID (non-SubstreamID) Translation Requests as using the CD at index 0 of a table of CDs, the request is internally treated similar to a request with Substream 0 in an STE.S1DSS == 0b00 configuration, but as with the request, the response is given without PASID. For correct invalidation of ATC entries to occur in this configuration, software must issue CMD\_ATC\_INV with SSV == 0.

This command is ILLEGAL if any of the following are true:

- SMMU\_IDR0.ATS == 0 and this command is issued on a Non-secure or Secure Command queue.
- SMMU\_IDR0.ATS == 1, SMMU\_S\_IDR3.SAMS == 1, and this command is issued on a Secure Command queue.
- SMMU\_R\_IDR0.ATS == 0 and this command is issued on a Realm Command queue.

This command is IGNORED if it is not ILLEGAL and any of the following are true:

- SMMU\_IDR0.ATS == 1 but ATS is not supported by the rest of the system.
- SMMUEN is 0 for the Security state corresponding to the Command queue that the command is issued on.

If this command is issued on a Secure Command queue and it is not ILLEGAL, the StreamID is considered to be Non-secure.

If this command is issued on a Realm Command queue and it is not ILLEGAL, the StreamID is considered to be Realm.

The Consumption of CMD\_ATC\_INV does not guarantee invalidation completion. Completion is ensured by the completion of a subsequent CMD\_SYNC. In a similar way to a TLBI operation, transactions that could have been translated using TLB entries targeted by the invalidation must all be visible to their Shareability domain before the ATS Invalidation is considered complete.

Note: In a system with separate Root Complex and SMMU components, the protocol between the two must enforce this ordering, for example, the Root Complex signals that an ATS Invalidation is complete only when affected transactions have been pushed to the SMMU and the SMMU then ensures this ordering is maintained, so that the completion signal is not observed before the affected transactions can be observed.

To invalidate a translation from an ATC, software must first invalidate SMMU caches of the translation (whether by explicit command or using broadcast invalidation) and then, after ensuring completion of the SMMU translation invalidate, issue a CMD\_ATC\_INV to invalidate ATC translations.

Note: For example, to alter and invalidate the last-level (leaf) translation table descriptor for a Non-secure EL1 translation of address V A using explicit SMMU operations:

1. Change translation table entry (and barrier to make visible to Shareability domain).
2. CMD\_TLBI\_NH\_VA(VMID, ASID, VA, Leaf == 1).
3. CMD\_SYNC.
4. CMD\_ATC\_INV(SID, SSID, SSV, Global == 0, VA).
5. CMD\_SYNC (and wait for completion)
6. The new translation table entry at V A is guaranteed to be in use.

Note: System software is expected to associate a device with a translation context and translation table and, when changes to the translation table are made, perform SMMU TLB maintenance using the translation table's associated ASID/VMID and ATC maintenance of all devices associated with that translation table using the StreamID/SubstreamIDs of the devices.

Note: Software must not provide a Size parameter that is lower than the system STU, as invalidation is not guaranteed if this is done. If a request is made with a span smaller than the STU, the PCIe specification [1] for ATS permits an endpoint to respond using a UR, or to round up the span and perform the invalidate with STU size.

Note: If this command results in a UR response from the endpoint, the command completes without error but invalidation is not guaranteed, see section 3.9.1.5 ATS Invalidation errors .

## 4.5.2 CMD\_PRI\_RESP(StreamID, SubstreamID, SSV, PRGIndex, Resp)

<!-- image -->

Notifies a device corresponding to StreamID, and SubstreamID when SSV == 1, that page request group indicated by PRGIndex has completed with given response, Resp.

PRGIndex: Page Request Group Index from page requests

Resp: 0b00 : ResponseFailure: Permanent non-paging error (for example ATS or PRI is disabled for the device)

- 0b01 : InvalidRequest: Page-in unsuccessful for one or more pages in the group
- 0b10 : Success: Page request group was paged in successfully
- 0b11 : Reserved: ILLEGAL

In systems that do not support PASIDs, SubstreamID is IGNORED and SSV must be 0. If SSV == 1, one of the following CONSTRAINED UNPREDICTABLE behaviors occurs:

- The command behaves as though SSV == 0, issuing a response to the given StreamID without a PASID TLP prefix.
- The command has no effect.

In systems that support PASIDs, SSV == 1 results in a PCIe PASID TLP prefix.

The command is ILLEGAL if any of the following are true:

- SMMU\_IDR0.PRI == 0
- SMMU\_IDR0.PRI == 1, and SMMU\_S\_IDR3.SAMS == 1 and this command is issued on a Secure Command queue.

This command is IGNORED if it is not ILLEGAL and any of the following are True:

- SMMU\_IDR0.PRI == 1, but PRI is not supported by the rest of the system.
- SMMUEN is 0 for the Security state corresponding to the Command queue that the command is issued on.

If the command is issued on a Secure Command queue and it is not ILLEGAL, the StreamID is considered to be Non-secure.

When issued to a Realm command queue, this command always applies to Realm StreamIDs.