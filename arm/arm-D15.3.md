## D15.3 Accessing System PMUs

| I VXVXK   | ASystem PMU<s> is selected by setting SPMSELR_EL0.SYSPMUSEL to <s>, where 0 ≤ s ≤ 31. This determines which System PMUis being accessed by the System PMUregisters. If enabled, then the System PMUs are always monitoring.                                                                    |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I WYLYL   | The largest value of SPMSELR_EL0.SYSPMUSEL is identified by ID_AA64DFR1_EL1.SYSPMUID.                                                                                                                                                                                                          |
| I BWTWP   | Implemented System PMUs might not be contiguously accessible. That is, if System PMU<s> is not implemented, this does not imply System PMU<s+1> is not implemented. Therefore, the value of ID_AA64DFR1_EL1.SYSPMUID does not necessarily indicate the total number of accessible System PMUs. |
| R JJNZK   | Accesses to System PMU<s> are controlled by SPMACCESSR_EL1.P<s>, SPMACCESSR_EL2.P<s>, SPMACCESSR_EL3.P<s>, and if implemented by the System PMU, SPMSCR_EL1 and SPMROOTCR_EL3.                                                                                                                 |
| I FKZLR   | FEAT_SPMU does not provide an equivalent of the fine-grained EL0 controls provided for thePEPMUby PMUSERENR_EL0 and PMUACR_EL1.                                                                                                                                                                |

## D15.3.1 Accessing System PMU registers

RNKSGW

ITZFBD

ASystem PMU that is shared by multiple PEs implements multi-copy atomicity for writes to the System PMU registers, with each of those PEs being observers of writes to the registers:

- All writes to the same System PMU register are serialized, meaning they are observed in the same order by all observers, although some observers might not observe all of the writes.
- Aread of a System PMU register does not observe a direct write until all observers observe that direct write.

Example D15-2 Observing a write to System PMU registers

When observing a write to System PMU registers, this means observing all effects of the write. For example:

- The effect writing to SPMEVCNTR&lt;n&gt;\_EL0 is to set the value of the counter to the value that was written.
- The effect writing a 1 to SPMOVSCLR\_EL0[n] is to clear both SPMOVSCLR\_EL0[n] and SPMOVSSET\_EL0[n] to 0.

| R TVFHH   | The System PMUis also an observer of writes to the System PMUregisters that makes indirect reads and indirect writes of the registers when counting events.                                                                                             |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R XFHMP   | Adirect write to a System PMUregister that has been synchronized by a Context synchronization event on the PE performing the direct write will be observable to all observers in finite time.                                                           |
| R BXJVP   | A DSB instruction ordered after a direct write to a System PMUregister does not complete until all observers observe the direct write. AContext synchronization event is required to create the order between the direct write and the DSB instruction. |
| I YPSBB   | Because a direct read from a System register in program order following a direct write to the same System register will observe the write to the register, reading back from that register also guarantees that all observers observe the direct write. |

## D15.3.2 Accessing System PMU counters

IZWVKD

ASystem PMU counter &lt;n&gt; is selected by setting SPMSELR\_EL0.BANK to &lt;n DIV 16&gt;, where 0 ≤ n ≤ 63.

IRHHZC

There are no mechanisms to trap accesses to individual counters, ranges of counters, or unimplemented counters in a System PMU. If not trapped by a higher priority exception, then accesses to unimplemented counters in a System PMU are RAZ/WI.

## D15.3.3 Zeroing System PMU counters

IGDKFB

If FEAT\_SPMU2 is implemented, then writing 1 to SPMZR\_EL0.P&lt;n&gt; sets System PMU counter &lt;n&gt; in System PMU &lt;s&gt; to zero.