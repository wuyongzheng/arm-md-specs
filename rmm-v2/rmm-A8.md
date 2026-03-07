## Chapter A8 Realm debug and performance monitoring

This section describes the debug and performance monitoring features which are available to a Realm.


## A8.1 Realm PMU

This section describes the programming model for usage of PMU by a Realm.

- Realm-assigned PMU counters means PMU counters in the range [0 .. realm.num\_pmu\_ctrs) .
- Host state for Realm-assigned PMU counters is not guaranteed to be preserved during Realm execution.
- On REC entry, the state of all Realm-assigned PMU counters is restored from the REC object.
- On REC exit, the state of all Realm-assigned PMU counters is saved to the REC object.
- On REC exit, exit.pmu\_ovf\_status indicates the level of the PMU overflow interrupt which results from the state of the Realm-assigned PMU counters.
- Realm access to the following registers should be emulated by the RMM.
- PMCR\_EL0
- PMINTEN{CLR,SET}\_EL0
- PMOVS{CLR,SET}\_EL0
- On REC exit with exit.pmu\_ovf\_status == RMI\_PMU\_OVERFLOW\_ACTIVE , the Host is not required to change the state of the physical PMU overflow interrupt before the next REC entry. Consequently, the RMM should disable overflow interrupts for Realm-assigned PMU counters on Realm entry, to avoid an active physical PMU overflow interrupt resulting in an immediate Realm exit.
- Host-retained PMU counters means PMU counters in the range [realm.num\_pmu\_ctrs .. 31) .
- During Realm execution, PMCNTENSET\_EL0.C behaves according to its architectural specification. If the Host has enabled the processor Cycle Counter, it continues to count during Realm execution.
- During Realm execution, PMCNTENSET\_EL0.P&lt;m&gt; behaves as 0 for all Host-retained PMU counters. All Host-retained PMU counters are disabled during Realm execution.
- The following diagram illustrates how overflows are handled for Realm-assigned PMU counters.


Figure A8.1: Realm PMU overflow

<!-- image -->

## See also:

- [A3.6 Realm support for Performance Monitors Extension](rmm-A3.md#a36-realm-support-for-performance-monitors-extension)
- [A4.3 REC exit](rmm-A4.3.md)
- [B4.6.66 RmiRecExit type](rmm-B4.6.md#b4666-rmirecexit-type)

## Chapter A9 Realm device assignment

This section describes how devices are assigned to Realms, attested and granted permission to access Realm-owned memory.

