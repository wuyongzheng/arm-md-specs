## D14.6 Required events

When at least one event counter is implemented, the following common events are implemented:

- 0x0000 , SW\_INCR, Instruction architecturally executed, Condition code check pass, software increment.

- 0x0003 , L1D\_CACHE\_REFILL, Level 1 data cache refill.

Note

Event 0x0003 is only required if the implementation includes a Level 1 data or unified cache.

- 0x0004 , L1D\_CACHE, Level 1 data cache access.

Note

Event 0x0004 is only required if the implementation includes a Level 1 data or unified cache.

- 0x0010 , BR\_MIS\_PRED, Mispredicted or not predicted branch Speculatively executed.

Note

Event 0x0010 is only required if the implementation includes program-flow prediction. However, Arm strongly recommends that the event is implemented as described in Common microarchitectural events.

- 0x0011 , CPU\_CYCLES, Cycle.

- 0x0012 , BR\_PRED, Predictable branch Speculatively executed.

Note

Event 0x0012 is only required if the implementation includes program-flow prediction. However, Arm recommends that the event is implemented as described in Common microarchitectural events.

- When FEAT\_PMUv3\_ICNTR is implemented:

- 0x0008 , INST\_RETIRED, Instruction architecturally executed.

- When FEAT\_PMUv3\_ICNTR is not implemented, at least one of:

- 0x0008 , INST\_RETIRED, Instruction architecturally executed.

- 0x001B , INST\_SPEC, Operation Speculatively executed.

Note

Arm strongly recommends that event 0x0008 is implemented.

- When FEAT\_PMUv3p1 is implemented:

- 0x0023 , STALL\_FRONTEND, No operation issued due to the frontend.

- 0x0024 , STALL\_BACKEND, No operation issued due to the backend.

- When FEAT\_SVE or FEAT\_SME is implemented, at least one of:

- 0x8002 , SVE\_INST\_RETIRED, SVE instruction architecturally retired.

- 0x8006 , SVE\_INST\_SPEC, SVE operation speculatively executed.

- When FEAT\_SPE is implemented:

- 0x4000 , SAMPLE\_POP, Statistical Profiling sample population.

- 0x4001 , SAMPLE\_FEED, Statistical Profiling sample taken.

- 0x4002 , SAMPLE\_FILTRATE, Statistical Profiling sample filtered.

- 0x4003 , SAMPLE\_COLLISION, Statistical Profiling sample collision.

- When FEAT\_PMUv3p4 is implemented:

- 0x003C , STALL, No operation sent for execution.

- 0x0039 , L1D\_CACHE\_LMISS\_RD, Level 1 data cache long-latency read miss.

- 0x4006 , L1I\_CACHE\_LMISS, Level 1 instruction cache long-latency miss.

- 0x0040 , L1D\_CACHE\_RD, Level 1 data cache read.

- When FEAT\_SPEv1p2 is implemented:

- -0x812A , SAMPLE\_FEED\_BR, Statistical Profiling sample taken, branch.

- -0x812B , SAMPLE\_FEED\_LD, Statistical Profiling sample taken, load.
- -0x812C , SAMPLE\_FEED\_ST, Statistical Profiling sample taken, store.
- -0x812D , SAMPLE\_FEED\_OP, Statistical Profiling sample taken, matching operation type.
- -0x812E , SAMPLE\_FEED\_EVENT, Statistical Profiling sample taken, matching events.
- -0x812F , SAMPLE\_FEED\_LAT, Statistical Profiling sample taken, exceeding minimum latency.
- When FEAT\_ETE is implemented:
- -0x4010 , TRCEXTOUT0.
- -0x4011 , TRCEXTOUT1.
- -0x4012 , TRCEXTOUT2.
- -0x4013 , TRCEXTOUT3.
- -If TRCIDR5.NUMEXTINSEL &gt; 0, 0x4018 , CTI\_TRIGOUT4.
- -If TRCIDR5.NUMEXTINSEL &gt; 1, 0x4019 , CTI\_TRIGOUT5.
- -If TRCIDR5.NUMEXTINSEL &gt; 2, 0x401A , CTI\_TRIGOUT6.
- -If TRCIDR5.NUMEXTINSEL &gt; 3, 0x401B , CTI\_TRIGOUT7.
- When FEAT\_PMUv3p9 is implemented:
- -0x0014 , L1I\_CACHE, Level 1 instruction cache access.
- When FEAT\_PMUv3\_SS is implemented:
- -0x8127 , PMU\_SNAPSHOT, Successful PMU capture event.
- When FEAT\_SPE\_FDS is implemented:
- -0x8122 , SAMPLE\_FEED\_DS, Statistical Profiling sample taken, selected Data Source.
- When FEAT\_SPEv1p4 is implemented:
- -0x8123 , SAMPLE\_BUFFER\_FULL, Profiling Buffer full.
- When FEAT\_SPE\_EFT is implemented:
- -0x8348 , SAMPLE\_FEED\_FP, Statistical Profiling sample taken, floating-point.
- -0x8349 , SAMPLE\_FEED\_SIMD, Statistical Profiling sample taken, SIMD.
- When FEAT\_SME is implemented:
- -At least one of the following is implemented:
- -0x835A , SME\_INST\_RETIRED, Instruction architecturally executed, SME.
- -0x835E , SME\_INST\_SPEC, Operation speculatively executed, SME.
- -At least one of the following is implemented:
- -0x8358 , SME\_RETIRED, Instruction architecturally executed, SME data processing.
- -0x835C , SME\_SPEC, Operation speculatively executed, SME data processing.

When any of the following common events are implemented, all three of them are implemented:

- 0x003D , STALL\_SLOT\_BACKEND, No operation sent for execution on a Slot due to the backend.
- 0x003E , STALL\_SLOT\_FRONTEND, No operation sent for execution on a Slot due to the frontend.
- 0x003F , STALL\_SLOT, No operation sent for execution on a Slot.

Arm strongly recommends that the following events are implemented:

- 0x0021 , BR\_RETIRED.
- 0x0022 , BR\_MIS\_PRED\_RETIRED.
- 0x003A , OP\_RETIRED.
- 0x003B , OP\_SPEC.
- 0x003D , STALL\_SLOT\_BACKEND.
- 0x003E , STALL\_SLOT\_FRONTEND.
- 0x003F , STALL\_SLOT.