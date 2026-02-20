## D13.6 Multithreaded implementations

If an implementation is multithreaded and the Effective value of PMEVTYPER&lt;n&gt;.MT is 1, then, unless otherwise stated, the counter counts the sum of all events across all PEs with the same level 1 Affinity. A pair of PEs have the same level 1 Affinity if they have the same values for all fields in MPIDR\_EL1or MPIDR except the Aff0 field.

See also Cycle event counting in multithreaded implementations for additional requirements for events that count cycles.

Events on other PEs are not counted when the Effective value of PMEVTYPER&lt;n&gt;.MT is 0.

If the CPU implements multithreading, and FEAT\_MTPMU is not implemented, for Armv8.5 and earlier, it is IMPLEMENTATION DEFINED whether PMEVTYPER&lt;n&gt;.MT is implemented as RW or RES0. From Armv8.6, if the optional FEAT\_MTPMU feature is not implemented, the Effective value of PMEVTYPER&lt;n&gt;.MT is RES0.

If FEAT\_MTPMU is implemented, EL3 is implemented, and MDCR\_EL3.MTPME is 0 or SDCR.MTPME is 0, FEAT\_MTPMU is disabled and the Effective value of PMEVTYPER&lt;n&gt;.MT is 0.

If FEAT\_MTPMU is implemented, EL3 is not implemented, EL2 is implemented, and MDCR\_EL2.MTPME is 0 or HDCR.MTPME is 0, FEAT\_MTPMU is disabled and the Effective value of PMEVTYPER&lt;n&gt;.MT is 0.

If FEAT\_MTPMU is disabled on a Processing Element PEA, it is IMPLEMENTATION DEFINED whether FEAT\_MTPMU is disabled on another Processing Element PEB, if all the following are true:

- FEAT\_MTPMU is implemented on PEA and PEB.
- PEA and PEB have the same values for Affinity level 1 and higher.
- PEA and PEB both have MPIDR\_EL1.MT or MPIDR.MT set to 1.

However, even when the Effective value of PMEVTYPER&lt;n&gt;.MT is 1, PEA does not count an event that is Attributable to Secure state on PEB if counting events Attributable to Secure state is prohibited on PEA. Similarly, PEA does not count an event that is Attributable to EL2 on PEB if counting events Attributable to EL2 is prohibited on PEA. See Counting events from shared components.

## Example D13-1 The effect of having PMEVTYPER&lt; n &gt;.MT == 1

If the value of MDCR\_EL3.SPME is 0, and n is less than PMCR.N on PEA, then event counter n on PEA does not count events Attributable to Secure state on PEB, even if one or both of the following applies:

- PEA is in Non-secure state.
- MDCR\_EL3.SPME==1 on PEB.

## Example D13-2 The effect of having PMEVTYPER&lt; n &gt;.MT == 1

WhenMDCR\_EL2.HPMNisnot0,ifthevalue of MDCR\_EL2.HPMD is 1 and n is less than MDCR\_EL2.HPMN on PEA, then event counter n on PEA does not count events Attributable to EL2 on PEB, even if one of the following applies:

- MDCR\_EL2.HPMD==0 on PEB.
- PEA is not executing at EL2.

When the current configuration is not multithreaded, and PEA prohibits counting of events Attributable to Secure state when PEA is in Secure state, it is IMPLEMENTATION DEFINED whether:

- Counting events Attributable to Secure state when PEA is in Non-secure state is permitted.
- Counting Unattributable events related to other Secure operations in the system when PEA is in Non-secure state is permitted.

Otherwise, counting events in Non-secure state is permitted.

When the current configuration is not multithreaded, and PEA prohibits counting of events Attributable to EL2 when PEA is at EL2, it is IMPLEMENTATION DEFINED whether:

- Counting events Attributable to EL2 when PEA is using another Exception level is permitted.
- Counting Unattributable events related to EL2 when PEA is using another Exception level is permitted.

Otherwise, counting events at another Exception level is permitted.

When the current configuration is not multithreaded, and PEA prohibits counting of events Attributable to a Security state and an Exception level when FEAT\_PMUv3p7 is implemented, it is IMPLEMENTATION DEFINED whether:

- Counting events Attributable to EL2 when PEA is using another Exception level is permitted.
- Counting Unattributable events related to EL2 when PEA is using another Exception level is permitted.

See Time as measured by the Performance Monitors cycle counter.