## 8.1 PRI queue overflow

The PRI queue enters an overflow condition when the following conditions apply:

- The PRI queue is enabled, as indicated by the effective value of SMMU\_CR0.PRIQEN == 1.
- One or more PRI messages are received by the SMMU while the PRI queue is full, as determined by the general queue semantics.

The SMMU indicates that this has happened by toggling the SMMU\_PRIQ\_PROD.OVFLG flag, provided that an overflow condition is not already present. The overflow condition is acknowledged by writing the SMMU\_PRIQ\_CONS.OVACKFLG flag to the same value as OVFLG.

An active overflow condition inhibits new entries from being written to the PRI queue.

Note: This behavior differs from the active overflow condition on an Event queue. See also section 7.4 Event queue overflow .

Note: On detection of overflow, Arm recommends that software processes the received PRI queue entries as quickly as possible, and follows this with a single write of SMMU\_PRIQ\_CONS to simultaneously move on the RD pointer and acknowledge receipt of the overflow condition by setting OVACKFLG to the value read from OVFLG.

When an overflow condition is active, incoming PRI messages are discarded and:

- An automatic PRG Response is generated for Page Request messages having Last == 1, including the PRGI of the PPR that caused the overflow condition to become active. This response is returned to the endpoint that originated the PPR. The ResponseCode is defined below.

Note: This behavior occurs only for a Page Request message and does not occur when a Stop Marker is discarded in an overflow condition.

- PPRs having Last == 0 are silently ignored.

Note: The auto-response behavior can maintain safe operation when PCIe endpoints fail to fully adhere to the PRI credit mechanism.

Note: Although in an overflow condition the system software will not have addressed the cause of the PPR, on receipt of the automatic successful response Arm expects that the device will gracefully attempt an ATS request and PRI request again. On subsequent requests, system software might have had time to process the PRI queue contents and free space for the retries.

Note: Auto-responses might be sent because of an overflow condition, or for other reasons. See section 8.2 Miscellaneous .

When the SMMU supports PASIDs, an automatic PRG Response that is sent in response to a PRI queue overflow condition has the following properties:

- If the associated Page Request message did not have a PASID, the response has no PASID and the ResponseCode field of the response is Success ( 0b0000 ). SMMU\_IDR3.PPS and STE.PPAR do not affect this case.
- If the associated Page Request message had a PASID:
- -If SMMU\_IDR3.PPS == 1, then the response has the same PASID and the ResponseCode is Success ( 0b0000 ). STE.PPAR is not checked and its value is ignored.
- -If SMMU\_IDR3.PPS == 0, the STE.PPAR field associated with the StreamID of the PPR is checked. The PASID depends on the associated STE:
* If the associated STE is valid, the response has the same PASID if STE.PPAR == 1 and it has no PASID if STE.PPAR == 0. In both cases, ResponseCode is Success ( 0b0000 ).
* If the associated STE is inaccessible or invalid, such that STE.PPAR cannot be checked, no PASID is used and the ResponseCode is Failure ( 0b1111 ). This occurs if SMMU\_CR0.SMMUEN == 0, or

the StreamID is out of range of the Stream table, or an External Abort was encountered during the STE fetch or VMS fetch, or the STE is ILLEGAL.

Note: In SMMUv3.2 or later, an STE access is permitted to also access the VMS if the VMS is enabled, which means that VMS access is permitted to occur as part of an STE.PPAR check and that access might give rise to this response failure case.

If SMMU\_CR2.RECINVSID == 1 and SMMU\_CR2.REC\_CFG\_ATS == 1, and the SMMU encounters C\_BAD\_STREAMID while attempting to check STE.PPAR, the event is recorded in the Event queue. If SMMU\_CR2.REC\_CFG\_ATS == 1, and the SMMU encounters F\_STE\_FETCH, F\_VMS\_FETCH, C\_BAD\_STE or F\_CFG\_CONFLICT while attempting to check STE.PPAR, the event is recorded in the Event queue. Otherwise, no event is recorded.

Note: For a normal transaction, the same conditions lead to C\_BAD\_STREAMID, F\_STE\_FETCH, and C\_BAD\_STE, respectively.

When PASIDs are not supported, an automatic response does not have a PASID prefix and the STE.PPAR field is not used. In this case, an implementation is permitted, but not required, to attempt to locate a valid STE and return either ResponseCode == Success or Failure in the manner described in this chapter even though STE.PPAR is not required. If the implementation does not perform this STE check, the ResponseCode == Success.

Note: A PRI-capable endpoint advertises whether it expects a PASID prefix to be present on a PRG response returned to it in response to a Page Request made with a PASID prefix, through the PRG Response PASID Required flag in the PRI Status register of the endpoint. Arm expects the STE.PPAR field associated with an endpoint to be programmed to the same value as this flag in the endpoint.

Stop PASID markers that arrive in an overflow condition are discarded and no auto-response is generated.

Note: The PCIe specification [1] does not consider PRI Stop PASID markers to be credited in the same way as PPRs. If endpoints disrespect Page Request allocation and credits, Stop PASID markers cannot be guaranteed to be visible to the system, given this rule. Software must use other means to determine PASID stop status in the presence of non-compliant PCIe endpoints.

## 8.1.1 Recovery procedure

At the time that an overflow is detected, the PRI queue might contain several groups of page requests that are legitimate, but might contain one or more groups of requests that have been truncated so that their 'Last' event was among those lost when overflow occurred, and these groups have had a 'Success' auto-response sent when the 'Last' event was discarded.

Note: To re-synchronize and regain normal processing of page requests, one possible method is:

- Process the entire queue: Entries are read from the SMMU\_PRIQ\_CONS.RD index up to the SMMU\_PRIQ\_PROD.WR index, sending Page Request Group Response commands using the Command queue as appropriate, when 'Last' entries are encountered.
- The PRI queue might contain the start of groups of page requests whose Last requests were lost, having been received and auto-responded to after overflow. A group must be ignored by software if no Last event has been found for it up to the point that the SMMU last wrote (the SMMU\_PRIQ\_PROD.WR index).
- Update SMMU\_PRIQ\_CONS.RD, including OVACKFLG, to clear the overflow condition and mark the entire queue as empty or processed.

Note: After an overflow condition has been resolved, a PRGIndex value might be used in PPRs that later become visible, associated with a semantically different PRG to that of a PRG with entries in the pre-overflow PRI queue. This would occur when the queue enters overflow state before the Last PPR of the initial PRG can be recorded. The Last PPR has a successful auto-response sent, meaning the endpoint is free to re-use the PRGIndex value.