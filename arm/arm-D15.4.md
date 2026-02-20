## D15.4 Generating System PMU overflow interrupt requests

RTCYDX

RNZHDW

RNBPGV

INJGBT

RPGYZY

IMZGZJ

It is IMPLEMENTATION DEFINED whether a System PMU implements a counter overflow flag for each counter SPMEVCNTR&lt;n&gt;\_EL0 implemented by the System PMU.

If the System PMU implements a counter overflow flag for SPMEVCNTR&lt;n&gt;\_EL0, then all of the following apply:

- When incrementing SPMEVCNTR&lt;n&gt;\_EL0 causes an unsigned overflow of the counter, the System PMU sets SPMOVSCLR\_EL0[n] to 1.
- SPMOVSCLR\_EL0[n] is R/W1C.
- SPMOVSSET\_EL0[n] is R/W1S.

Otherwise, SPMOVSCLR\_EL0[n] and SPMOVSSET\_EL0[n] are RAZ/WI.

Note

If an event can occur multiple times in a single clock cycle, then a counter overflow can occur without the counter registering a value of zero.

The size of each counter implemented by a System PMU is IMPLEMENTATION DEFINED, between 1 and 64 bits. Unimplemented bits in each counter register are RES0.

If a System PMU implements a counter overflow flag for any counter SPMEVCNTR&lt;n&gt;\_EL0 implemented by the System PMU, then it is IMPLEMENTATION DEFINED whether the System PMU implements an overflow interrupt request.

Each System PMU that implements an overflow interrupt request has its own interrupt request, and it is IMPLEMENTATION DEFINED whether the interrupts are implemented as a Shared Peripheral Interrupt (SPI) or a Private Peripheral Interrupt (PPI). A System PMU that is not shared with other PEs should use a PPI. Interrupt IDs are IMPLEMENTATION DEFINED.

When the overflow interrupt request is implemented, software can program SPMINTENSET\_EL1 and SPMINTENCLR\_EL1 such that an overflow interrupt request is generated when a counter overflow flag is 1. If the System PMU implements the overflow interrupt request and implements a counter overflow flag for SPMEVCNTR&lt;n&gt;\_EL0, then all of the following apply:

- SPMINTENCLR\_EL1[n] is R/W1C.
- SPMINTENSET\_EL1[n] is R/W1S.

Otherwise, SPMINTENCLR\_EL1[n] and SPMINTENSET\_EL1[n] are RAZ/WI.

If the overflow interrupt request is implemented as a level-sensitive request, then the System PMU signals an overflow interrupt request when all of the following are true for any implemented counter SPMEVCNTR&lt;n&gt;\_EL0:

- SPMCR\_EL0.E is 1.
- SPMOVSCLR\_EL0[n] is 1.
- SPMINTENCLR\_EL1[n] is 1.

For more information, see SPMINTENSET\_EL1 and SPMINTENCLR\_EL1.

The architecture does not provide any support for a System PMU interrupt implemented as a message-signaled interrupt (MSI). To support implementing the interrupt as an MSI, additional IMPLEMENTATION DEFINED registers must be defined.

## Chapter D16 The Activity Monitors Extension

This chapter describes version 1 of the Activity Monitor Unit (AMU) architecture, AMUv1, an optional non-invasive component. It contains the following sections:

- About the Activity Monitors Extension.
- Properties and behavior of the activity monitors.
- AMUevents and event numbers.