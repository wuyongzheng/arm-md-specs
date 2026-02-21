## 10.6 Support for Secure state

Support for Secure state in a PMCG is optional. If supported, it comprises of:

- Whether the PMCG registers can be accessed by both Non-secure and Secure accesses, or only Secure accesses.
- Whether the counters can observe events associated with Secure StreamIDs or Secure state.
- Whether an MSI targets the Secure or Non-secure PA space.

The SMMU\_PMCG\_SCR.NSRA flag controls whether Non-secure accesses can be made to the registers of a given group. Secure accesses can always be made to the registers.

Note: As counter groups might exist in separate components, the SMMU does not contain a centralized mechanism for assigning counter groups to a Security state.

The SMMU\_PMCG\_SCR.SO flag controls whether counters can observe events associated with Secure state or Secure StreamIDs.

When SMMU\_PMCG\_SCR.SO == 1, Secure observation is enabled and:

- Counters using event types that can be filtered by StreamID might count events that are associated with a Secure or Non-secure StreamID. See section 10.4 StreamIDs and filtering and the SMMU\_PMCG\_EVTYPERn .FILTER\_SEC\_SID bit.
- Counters using other event types are able to count events that are associated with Secure or Non-secure state, as appropriate for the event.

Note: IMPLEMENTATION DEFINED events might be associated with StreamIDs or a Security state even if they might not be directly associated with a specific StreamID. The architected global events are not specific to a Security state.

When SMMU\_PMCG\_SCR.SO == 0, Secure observation is disabled and:

- Counters using event types that can be filtered by StreamID only count events associated with Non-secure StreamIDs.
- Counters using other event types only count events that are associated with the Non-secure state.

When a counter uses an event type able to be filtered by StreamID but the StreamID filter matches all, events from all StreamIDs associated with the Security state selected by the SMMU\_PMCG\_EVTYPERn.FILTER\_SECSID bit are counted, if permitted by the 'SO' flag.

If a counter group supports MSIs:

- If Secure state is not supported in the PMCG, the target PA space of the MSI is Non-secure.
- If Secure state is supported in the PMCG, the target PA space of the MSI is given by:

NS = SMMU\_PMCG\_SCR.NSMSI | SMMU\_PMCG\_SCR.NSRA

See section SMMU\_PMCG\_SCR.

If a PMCG does not support Secure state but the system does, then the PMCG only observes events that are associated with Non-secure streams. If a PMCG supports Secure state but the system does not, then all streams are considered to be Non-secure.