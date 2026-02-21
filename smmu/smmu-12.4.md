## 12.4 RAS fault handling/reporting

When RAS facilities are implemented, an implementation must provide at least one group of memory-mapped error recording registers in accordance with the RAS error record format defined in the RAS System Architecture [11].

The exact layout and operation of the RAS registers is IMPLEMENTATION DEFINED, including:

- Discovery and identification registers.
- The number of RAS error records and association to nodes.
- Whether Corrected error counters are implemented.

Error Recovery Interrupts and Fault Handling Interrupts must be provided.

Note: Interrupts in SMMUv3 are required to be edge-triggered or MSIs. However, interrupts for SMMUv3 RAS features comply with [11] which states it is IMPLEMENTATION DEFINED whether interrupt requests are edge-triggered or level-sensitive.

The mechanism for determining whether RAS facilities are implemented, base addresses for RAS registers and the extent of RAS register frames is IMPLEMENTATION DEFINED. Note: For example, IMPLEMENTATION DEFINED identification registers or firmware descriptions.

One RAS register interface might be provided for each supported Security state, or a subset of the Security states, subject to the constraints described in the RAS System Architecture [11].