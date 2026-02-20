## D15.2 System PMU configuration

IXCMGX

IYKJXW

ASystem PMU is identified to software by the following registers:

- SPMIIDR\_EL1 uniquely identifies the component implementor and provides a part number code specific to that implementation. This register is OPTIONAL, and if the register is not implemented, it is RAZ.
- SPMDEVARCH\_EL1 describes a generic programmers' model for the System PMU that might be shared by multiple implementations. This register is OPTIONAL, and if the register is not implemented, it is RAZ.
- SPMDEVAFF\_EL1 describes which PEs the System PMU is shared with, if any.
- SPMCFGR\_EL1 describes the capabilities of the System PMU, including, but not limited to, the number and size of counters implemented by the System PMU.
- If SPMCFGR\_EL1.NCG indicates the System PMU implements more than one Counter Group, then SPMCGCR&lt;n&gt;\_EL1 indicates the number of counters in each Counter Group. Otherwise, SPMCGCR&lt;n&gt;\_EL1 are RAZ and all the counters are in the first Counter Group.

When these registers are implemented by a System PMU, software can use these registers along with pre-existing knowledge to determine configuration information about the System PMU, as follows:

1. If software recognizes the identity of the System PMU in SPMIIDR\_EL1, it can load a configuration for the System PMU.
2. Otherwise, if software recognizes the architecture in SPMDEV ARCH\_EL1, it can load a generic configuration for the System PMU.
3. Otherwise, software can use the capabilities described by SPMCFGR\_EL1 to define a generic configuration for the System PMU.

The configuration contains, for instance, details of how the event configuration registers SPMEVTYPER&lt;n&gt;\_EL0, SPMEVFILTR&lt;n&gt;\_EL0, and SPMEVFILT2R&lt;n&gt;\_EL0, are programmed, including but not limited to the following IMPLEMENTATION DEFINED information:

- Field assignments.
- Whether additional features are implemented, such as threshold and edge detection.
- Whether an interrupt on counter overflow is implemented.
- Assignment of event codes to events.
- Definitions of events.
- Details of any fixed-function counters.
- Useful metrics derived from events.
- Security policies for allowing access to the System PMU from lower Exception levels.

ASystem PMU might statically divide its counters into an IMPLEMENTATION DEFINED number of Counter Groups. The number of Counter Groups is identified to software by SPMCFGR\_EL1.NCG. At most 15 Counter Groups can be implemented. If SPMCFGR\_EL1.NCG is 0b0000 , then only one Counter Group is implemented, and all counters are in the first Counter Group.

Each Counter Group has an IMPLEMENTATION DEFINED number of counters in that group, from zero to the value max . The number of counters in Counter Group &lt;n × 8 + m&gt;, is identified to software by SPMCGCR&lt;n&gt;\_EL1.N&lt;m&gt;. The first counter in Counter Group &lt;n&gt; is SPMEVCNTR&lt;n × max&gt;\_EL0.

The value max depends on the number of Counter Groups implemented, and is defined by the following table:

## Table D15-1 Value of max when determining the first counter in a Counter Group

| Number of Counter Groups   |   max |
|----------------------------|-------|
| 2                          |    32 |
| 3 or 4                     |    16 |
| Between 5 and 8            |     8 |
| Between 9 and 15           |     4 |

Example D15-1 Determining the number of counters in a System PMU

The number of counters in a System PMU can be determined as described in the following example:

- SPMCFGR\_EL1.NCG reads as 0b0001 , indicating 2 Counter Groups.
- SPMCGCR0\_EL1 reads as 0x0000\_0604 , indicating:
- -Group 0 has four counters: SPMEVCNTR0\_EL0 to SPMEVCNTR3\_EL0.
- -Group 1 has six counters: SPMEVCNTR32\_EL0 to SPMEVCNTR37\_EL0.
- SPMCFGR\_EL1.N reads as 0x09 , indicating 10 counters are implemented overall.