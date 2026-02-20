## D14.2 The PMU event number space and common events

In Armv8.0, the event number space is 10 bits. Armv8.1 extends the event number space, and therefore the PMEVTYPER&lt;n&gt;\_EL0.evtCount field, to 16 bits, and is allocated as Table D14-2 shows. For more information about the entries in the Allocation column see the text that follows this table:

Table D14-2 Allocation of the PMU event number space

| Event numbers                     | Allocation                                                                                                                                                           |
|-----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x0000 - 0x003F                   | Common architectural and microarchitectural events.                                                                                                                  |
| 0x0040 - 0x00BF                   | When FEAT_PMUv3p8 is implemented, common architectural and microarchitectural events. Previously Arm-recommended common architectural and microarchitectural events. |
| 0x00C0 - 0x03FF                   | IMPLEMENTATION DEFINED events.                                                                                                                                       |
| When FEAT_PMUv3p1 is implemented: | When FEAT_PMUv3p1 is implemented:                                                                                                                                    |
| 0x0400 - 0x3FFF                   | IMPLEMENTATION DEFINED events.                                                                                                                                       |
| 0x4000 - 0x403F                   | Common architectural and microarchitectural events.                                                                                                                  |
| 0x4040 - 0x40BF                   | When FEAT_PMUv3p8 is implemented, common architectural and microarchitectural events. Previously Arm-recommended common architectural and microarchitectural events. |
| 0x40C0 - 0x7FFF                   | IMPLEMENTATION DEFINED events.                                                                                                                                       |
| 0x8000 - 0x8FFF                   | Common architectural and microarchitectural events.                                                                                                                  |
| 0x9000 - 0xC0BF                   | Reserved.                                                                                                                                                            |
| 0xC0C0 - 0xFFFF                   | IMPLEMENTATION DEFINED events.                                                                                                                                       |

See PMEVTYPER&lt;n&gt;.evtCount for details of the PE behavior when an event number for a reserved or unimplemented PMUevent is written to evtCount.

Table D14-3 lists the number, mnemonic, and description of PMU events.

## Table D14-3 Event index

| Number   | Mnemonic         | Description                                                                          |
|----------|------------------|--------------------------------------------------------------------------------------|
| 0x0000   | SW_INCR          | Instruction architecturally executed, Condition code check pass, software increment. |
| 0x0001   | L1I_CACHE_REFILL | Level 1 instruction cache refill.                                                    |
| 0x0002   | L1I_TLB_REFILL   | Level 1 instruction TLB refill.                                                      |
| 0x0003   | L1D_CACHE_REFILL | Level 1 data cache refill.                                                           |
| 0x0004   | L1D_CACHE        | Level 1 data cache access.                                                           |
| 0x0005   | L1D_TLB_REFILL   | Level 1 data TLB refill.                                                             |
| 0x0006   | LD_RETIRED       | Instruction architecturally executed, Condition code check pass, load.               |
| 0x0007   | ST_RETIRED       | Instruction architecturally executed, Condition code check pass, store.              |
| 0x0008   | INST_RETIRED     | Instruction architecturally executed.                                                |

| Number   | Mnemonic               | Description                                                                                 |
|----------|------------------------|---------------------------------------------------------------------------------------------|
| 0x0009   | EXC_TAKEN              | Exception taken.                                                                            |
| 0x000A   | EXC_RETURN             | Instruction architecturally executed, Condition code check pass, exception return.          |
| 0x000B   | CID_WRITE_RETIRED      | Instruction architecturally executed, Condition code check pass, write to CONTEXTIDR.       |
| 0x000C   | PC_WRITE_RETIRED       | Instruction architecturally executed, Condition code check pass, Software change of the PC. |
| 0x000D   | BR_IMMED_RETIRED       | Branch instruction architecturally executed, immediate.                                     |
| 0x000E   | BR_RETURN_RETIRED      | Branch instruction architecturally executed, procedure return, taken.                       |
| 0x000F   | UNALIGNED_LDST_RETIRED | Instruction architecturally executed, Condition code check pass, unaligned load or store.   |
| 0x0010   | BR_MIS_PRED            | Branch instruction speculatively executed, mispredicted or not predicted.                   |
| 0x0011   | CPU_CYCLES             | Cycle.                                                                                      |
| 0x0012   | BR_PRED                | Predictable branch instruction speculatively executed.                                      |
| 0x0013   | MEM_ACCESS             | Data memory access.                                                                         |
| 0x0014   | L1I_CACHE              | Level 1 instruction cache access.                                                           |
| 0x0015   | L1D_CACHE_WB           | Level 1 data cache write-back.                                                              |
| 0x0016   | L2D_CACHE              | Level 2 data cache access.                                                                  |
| 0x0017   | L2D_CACHE_REFILL       | Level 2 data cache refill.                                                                  |
| 0x0018   | L2D_CACHE_WB           | Level 2 data cache write-back.                                                              |
| 0x0019   | BUS_ACCESS             | Bus access.                                                                                 |
| 0x001A   | MEMORY_ERROR           | Local memory error.                                                                         |
| 0x001B   | INST_SPEC              | Operation speculatively executed.                                                           |
| 0x001C   | TTBR_WRITE_RETIRED     | Instruction architecturally executed, Condition code check pass, write to TTBR.             |
| 0x001D   | BUS_CYCLES             | Bus cycle.                                                                                  |
| 0x001E   | CHAIN                  | Chain a pair of event counters.                                                             |
| 0x001F   | L1D_CACHE_ALLOCATE     | Level 1 data cache allocation without refill.                                               |
| 0x0020   | L2D_CACHE_ALLOCATE     | Level 2 data cache allocation without refill.                                               |
| 0x0021   | BR_RETIRED             | Instruction architecturally executed, branch.                                               |
| 0x0022   | BR_MIS_PRED_RETIRED    | Branch instruction architecturally executed, mispredicted.                                  |
| 0x0023   | STALL_FRONTEND         | No operation sent for execution due to the frontend.                                        |

| Number   | Mnemonic               | Description                                                      |
|----------|------------------------|------------------------------------------------------------------|
| 0x0024   | STALL_BACKEND          | No operation sent for execution due to the backend.              |
| 0x0025   | L1D_TLB                | Level 1 data TLB access.                                         |
| 0x0026   | L1I_TLB                | Level 1 instruction TLB access.                                  |
| 0x0027   | L2I_CACHE              | Level 2 instruction cache access.                                |
| 0x0028   | L2I_CACHE_REFILL       | Level 2 instruction cache refill.                                |
| 0x0029   | L3D_CACHE_ALLOCATE     | Level 3 data cache allocation without refill.                    |
| 0x002A   | L3D_CACHE_REFILL       | Level 3 data cache refill.                                       |
| 0x002B   | L3D_CACHE              | Level 3 data cache access.                                       |
| 0x002C   | L3D_CACHE_WB           | Level 3 data cache write-back.                                   |
| 0x002D   | L2D_TLB_REFILL         | Level 2 data TLB refill.                                         |
| 0x002E   | L2I_TLB_REFILL         | Level 2 instruction TLB refill.                                  |
| 0x002F   | L2D_TLB                | Level 2 data TLB access.                                         |
| 0x0030   | L2I_TLB                | Level 2 instruction TLB access.                                  |
| 0x0031   | REMOTE_ACCESS          | Access to a remote device.                                       |
| 0x0032   | LL_CACHE               | Last level cache access.                                         |
| 0x0033   | LL_CACHE_MISS          | Last level cache miss.                                           |
| 0x0034   | DTLB_WALK              | Data TLB access with at least one translation table walk.        |
| 0x0035   | ITLB_WALK              | Instruction TLB access with at least one translation table walk. |
| 0x0036   | LL_CACHE_RD            | Last level cache access, read.                                   |
| 0x0037   | LL_CACHE_MISS_RD       | Last level cache miss, read.                                     |
| 0x0038   | REMOTE_ACCESS_RD       | Access to a remote device, read.                                 |
| 0x0039   | L1D_CACHE_LMISS_RD     | Level 1 data cache long-latency read miss.                       |
| 0x003A   | OP_RETIRED             | Micro-operation architecturally executed.                        |
| 0x003B   | OP_SPEC                | Micro-operation speculatively executed.                          |
| 0x003C   | STALL                  | No operation sent for execution.                                 |
| 0x003D   | STALL_SLOT_BACKEND     | No operation sent for execution on a Slot due to the backend.    |
| 0x003E   | STALL_SLOT_FRONTEND    | No operation sent for execution on a Slot due to the frontend.   |
| 0x003F   | STALL_SLOT             | No operation sent for execution on a Slot.                       |
| 0x0040   | L1D_CACHE_RD           | Level 1 data cache access, read.                                 |
| 0x0041   | L1D_CACHE_WR           | Level 1 data cache access, write.                                |
| 0x0042   | L1D_CACHE_REFILL_RD    | Level 1 data cache refill, read.                                 |
| 0x0043   | L1D_CACHE_REFILL_WR    | Level 1 data cache refill, write.                                |
| 0x0044   | L1D_CACHE_REFILL_INNER | Level 1 data cache refill, inner.                                |

| Number   | Mnemonic               | Description                                                       |
|----------|------------------------|-------------------------------------------------------------------|
| 0x0045   | L1D_CACHE_REFILL_OUTER | Level 1 data cache refill, outer.                                 |
| 0x0046   | L1D_CACHE_WB_VICTIM    | Level 1 data cache write-back, victim.                            |
| 0x0047   | L1D_CACHE_WB_CLEAN     | Level 1 data cache write-back, cleaning and coherency.            |
| 0x0048   | L1D_CACHE_INVAL        | Level 1 data cache invalidate.                                    |
| 0x004C   | L1D_TLB_REFILL_RD      | Level 1 data TLB refill, read.                                    |
| 0x004D   | L1D_TLB_REFILL_WR      | Level 1 data TLB refill, write.                                   |
| 0x004E   | L1D_TLB_RD             | Level 1 data TLB access, read.                                    |
| 0x004F   | L1D_TLB_WR             | Level 1 data TLB access, write.                                   |
| 0x0050   | L2D_CACHE_RD           | Level 2 data cache access, read.                                  |
| 0x0051   | L2D_CACHE_WR           | Level 2 data cache access, write.                                 |
| 0x0052   | L2D_CACHE_REFILL_RD    | Level 2 data cache refill, read.                                  |
| 0x0053   | L2D_CACHE_REFILL_WR    | Level 2 data cache refill, write.                                 |
| 0x0056   | L2D_CACHE_WB_VICTIM    | Level 2 data cache write-back, victim.                            |
| 0x0057   | L2D_CACHE_WB_CLEAN     | Level 2 data cache write-back, cleaning and coherency.            |
| 0x0058   | L2D_CACHE_INVAL        | Level 2 data cache invalidate.                                    |
| 0x005C   | L2D_TLB_REFILL_RD      | Level 2 data TLB refill, read.                                    |
| 0x005D   | L2D_TLB_REFILL_WR      | Level 2 data TLB refill, write.                                   |
| 0x005E   | L2D_TLB_RD             | Level 2 data TLB access, read.                                    |
| 0x005F   | L2D_TLB_WR             | Level 2 data TLB access, write.                                   |
| 0x0060   | BUS_ACCESS_RD          | Bus access, read.                                                 |
| 0x0061   | BUS_ACCESS_WR          | Bus access, write.                                                |
| 0x0062   | BUS_ACCESS_SHARED      | Bus access, Normal, Cacheable, Shareable.                         |
| 0x0063   | BUS_ACCESS_NOT_SHARED  | Bus access, not Normal, Cacheable, Shareable.                     |
| 0x0064   | BUS_ACCESS_NORMAL      | Bus access, normal.                                               |
| 0x0065   | BUS_ACCESS_PERIPH      | Bus access, peripheral.                                           |
| 0x0066   | MEM_ACCESS_RD          | Data memory access, read.                                         |
| 0x0067   | MEM_ACCESS_WR          | Data memory access, write.                                        |
| 0x0068   | UNALIGNED_LD_SPEC      | Unaligned access, read.                                           |
| 0x0069   | UNALIGNED_ST_SPEC      | Unaligned access, write.                                          |
| 0x006A   | UNALIGNED_LDST_SPEC    | Unaligned access.                                                 |
| 0x006C   | LDREX_SPEC             | Exclusive operation speculatively executed, Load-Exclusive.       |
| 0x006D   | STREX_PASS_SPEC        | Exclusive operation speculatively executed, Store-Exclusive pass. |
| 0x006E   | STREX_FAIL_SPEC        | Exclusive operation speculatively executed, Store-Exclusive fail. |
| 0x006F   | STREX_SPEC             | Exclusive operation speculatively executed, Store-Exclusive.      |

| Number   | Mnemonic         | Description                                                              |
|----------|------------------|--------------------------------------------------------------------------|
| 0x0070   | LD_SPEC          | Operation speculatively executed, load.                                  |
| 0x0071   | ST_SPEC          | Operation speculatively executed, store.                                 |
| 0x0072   | LDST_SPEC        | Operation speculatively executed, load or store.                         |
| 0x0073   | DP_SPEC          | Operation speculatively executed, integer data processing.               |
| 0x0074   | ASE_SPEC         | Operation speculatively executed, Advanced SIMD data processing.         |
| 0x0075   | VFP_SPEC         | Operation speculatively executed, scalar floating-point data processing. |
| 0x0076   | PC_WRITE_SPEC    | Operation speculatively executed, Software change of the PC.             |
| 0x0077   | CRYPTO_SPEC      | Operation speculatively executed, cryptographic data processing.         |
| 0x0078   | BR_IMMED_SPEC    | Branch speculatively executed, immediate branch.                         |
| 0x0079   | BR_RETURN_SPEC   | Branch speculatively executed, procedure return.                         |
| 0x007A   | BR_INDIRECT_SPEC | Branch speculatively executed, indirect branch.                          |
| 0x007C   | ISB_SPEC         | Barrier speculatively executed, ISB.                                     |
| 0x007D   | DSB_SPEC         | Barrier speculatively executed, DSB.                                     |
| 0x007E   | DMB_SPEC         | Barrier speculatively executed, DMB.                                     |
| 0x007F   | CSDB_SPEC        | Barrier speculatively executed, CSDB.                                    |
| 0x0081   | EXC_UNDEF        | Exception taken, other synchronous.                                      |
| 0x0082   | EXC_SVC          | Exception taken, Supervisor Call.                                        |
| 0x0083   | EXC_PABORT       | Exception taken, Instruction Abort.                                      |
| 0x0084   | EXC_DABORT       | Exception taken, Data Abort or SError.                                   |
| 0x0086   | EXC_IRQ          | Exception taken, IRQ.                                                    |
| 0x0087   | EXC_FIQ          | Exception taken, FIQ.                                                    |
| 0x0088   | EXC_SMC          | Exception taken, Secure Monitor Call.                                    |
| 0x008A   | EXC_HVC          | Exception taken, Hypervisor Call.                                        |
| 0x008B   | EXC_TRAP_PABORT  | Exception taken, Instruction Abort not Taken locally.                    |
| 0x008C   | EXC_TRAP_DABORT  | Exception taken, Data Abort or SError not Taken locally.                 |
| 0x008D   | EXC_TRAP_OTHER   | Exception taken, other traps not Taken locally.                          |
| 0x008E   | EXC_TRAP_IRQ     | Exception taken, IRQ not Taken locally.                                  |
| 0x008F   | EXC_TRAP_FIQ     | Exception taken, FIQ not Taken locally.                                  |

| Number   | Mnemonic                   | Description                                                                                               |
|----------|----------------------------|-----------------------------------------------------------------------------------------------------------|
| 0x0090   | RC_LD_SPEC                 | Release consistency operation speculatively executed, Load-Acquire.                                       |
| 0x0091   | RC_ST_SPEC                 | Release consistency operation speculatively executed, Store-Release.                                      |
| 0x0092   | L3D_CACHE_HIT_WR_FEXT_PROP | Level 3 data cache demand access first hit, write, fetched by external propagating transaction.           |
| 0x00A0   | L3D_CACHE_RD               | Level 3 data cache access, read.                                                                          |
| 0x00A1   | L3D_CACHE_WR               | Level 3 data cache access, write.                                                                         |
| 0x00A2   | L3D_CACHE_REFILL_RD        | Level 3 data cache refill, read.                                                                          |
| 0x00A3   | L3D_CACHE_REFILL_WR        | Level 3 data cache refill, write.                                                                         |
| 0x00A6   | L3D_CACHE_WB_VICTIM        | Level 3 data cache write-back, victim.                                                                    |
| 0x00A7   | L3D_CACHE_WB_CLEAN         | Level 3 data cache write-back, cleaning and coherency.                                                    |
| 0x00A8   | L3D_CACHE_INVAL            | Level 3 data cache invalidate.                                                                            |
| 0x00A9   | L2D_CACHE_HIT_RD_FEXT_PROP | Level 2 data cache demand access first hit, read, fetched by external propagating transaction.            |
| 0x00AA   | L2D_CACHE_HIT_WR_FEXT_PROP | Level 2 data cache demand access first hit, write, fetched by external propagating transaction.           |
| 0x00AB   | L2D_CACHE_HIT_RW_FEXT_PROP | Level 2 data cache demand access first hit, fetched by external propagating transaction.                  |
| 0x00AC   | L3D_CACHE_EXT_PROP         | Level 3 data cache allocation due to external propagating transaction.                                    |
| 0x00AD   | L3D_CACHE_EXT_PROP_PRFM_IR | Level 3 data cache allocation due to external propagating transaction after prefetch with intent to read. |
| 0x00AE   | L3D_CACHE_HIT_RW_FEXT_PROP | Level 3 data cache demand access first hit, fetched by external propagating transaction.                  |
| 0x00AF   | L3D_CACHE_HIT_RD_FEXT_PROP | Level 3 data cache demand access first hit, read, fetched by external propagating transaction.            |
| 0x00B0   | STSHH_SPEC                 | Store shared hint instruction speculatively executed.                                                     |
| 0x00B1   | STSHH_KEEP_SPEC            | Store shared hint instruction speculatively executed with KEEP policy.                                    |
| 0x00B2   | STSHH_STRM_SPEC            | Store shared hint instruction speculatively executed withSTRM policy.                                     |
| 0x00B3   | PRFM_IR_SPEC               | Prefetch with intent to read instruction speculatively executed.                                          |
| 0x00B4   | MEM_ACCESS_WR_STSHH        | Memory write with store shared hint.                                                                      |

| Number   | Mnemonic                      | Description                                                                                               |
|----------|-------------------------------|-----------------------------------------------------------------------------------------------------------|
| 0x00B5   | MEM_ACCESS_WR_STSHH_KEEP      | Memory write with store shared hint with keep policy.                                                     |
| 0x00B6   | MEM_ACCESS_WR_STSHH_STRM      | Memory write with store shared hint with stream policy.                                                   |
| 0x00B7   | MEM_ACCESS_WR_STSHH_KEEP_NEAR | Memory write with store shared hint with keep policy performed near.                                      |
| 0x00B8   | MEM_ACCESS_WR_STSHH_KEEP_FAR  | Memory write with store shared hint with keep policy performed far.                                       |
| 0x00B9   | L1D_CACHE_EXT_PROP            | Level 1 data cache allocation due to external propagating transaction.                                    |
| 0x00BA   | L1D_CACHE_EXT_PROP_PRFM_IR    | Level 1 data cache allocation due to external propagating transaction after prefetch with intent to read. |
| 0x00BB   | L1D_CACHE_HIT_RD_FEXT_PROP    | Level 1 data cache demand access first hit, read, fetched by external propagating transaction.            |
| 0x00BC   | L1D_CACHE_HIT_WR_FEXT_PROP    | Level 1 data cache demand access first hit, write, fetched by external propagating transaction.           |
| 0x00BD   | L1D_CACHE_HIT_RW_FEXT_PROP    | Level 1 data cache demand access first hit, fetched by external propagating transaction.                  |
| 0x00BE   | L2D_CACHE_EXT_PROP            | Level 2 data cache allocation due to external propagating transaction.                                    |
| 0x00BF   | L2D_CACHE_EXT_PROP_PRFM_IR    | Level 2 data cache allocation due to external propagating transaction after prefetch with intent to read. |
| 0x4000   | SAMPLE_POP                    | Statistical Profiling sample population.                                                                  |
| 0x4001   | SAMPLE_FEED                   | Statistical Profiling sample taken.                                                                       |
| 0x4002   | SAMPLE_FILTRATE               | Statistical Profiling sample taken and not removed by filtering.                                          |
| 0x4003   | SAMPLE_COLLISION              | Statistical Profiling sample collided with previous sample.                                               |
| 0x4004   | CNT_CYCLES                    | Constant frequency cycles.                                                                                |
| 0x4005   | STALL_BACKEND_MEM             | Memory stall cycles.                                                                                      |
| 0x4006   | L1I_CACHE_LMISS               | Level 1 instruction cache long-latency miss.                                                              |
| 0x4009   | L2D_CACHE_LMISS_RD            | Level 2 data cache long-latency read miss.                                                                |
| 0x400A   | L2I_CACHE_LMISS               | Level 2 instruction cache long-latency miss.                                                              |
| 0x400B   | L3D_CACHE_LMISS_RD            | Level 3 data cache long-latency read miss.                                                                |
| 0x400C   | TRB_WRAP                      | Trace buffer current write pointer wrapped.                                                               |
| 0x400D   | PMU_OVFS                      | PMUoverflow, counters accessible to EL1 and EL0.                                                          |
| 0x400E   | TRB_TRIG                      | Trace buffer Trigger Event.                                                                               |

| Number   | Mnemonic              | Description                                                         |
|----------|-----------------------|---------------------------------------------------------------------|
| 0x400F   | PMU_HOVFS             | PMUoverflow, counters reserved for use by EL2.                      |
| 0x4010   | TRCEXTOUT0            | Trace unit external output 0.                                       |
| 0x4011   | TRCEXTOUT1            | Trace unit external output 1.                                       |
| 0x4012   | TRCEXTOUT2            | Trace unit external output 2.                                       |
| 0x4013   | TRCEXTOUT3            | Trace unit external output 3.                                       |
| 0x4018   | CTI_TRIGOUT4          | Cross-trigger Interface output trigger 4.                           |
| 0x4019   | CTI_TRIGOUT5          | Cross-trigger Interface output trigger 5.                           |
| 0x401A   | CTI_TRIGOUT6          | Cross-trigger Interface output trigger 6.                           |
| 0x401B   | CTI_TRIGOUT7          | Cross-trigger Interface output trigger 7.                           |
| 0x4020   | LDST_ALIGN_LAT        | Access with additional latency from alignment.                      |
| 0x4021   | LD_ALIGN_LAT          | Load with additional latency from alignment.                        |
| 0x4022   | ST_ALIGN_LAT          | Store with additional latency from alignment.                       |
| 0x4024   | MEM_ACCESS_CHECKED    | Checked data memory access.                                         |
| 0x4025   | MEM_ACCESS_CHECKED_RD | Checked data memory access, read.                                   |
| 0x4026   | MEM_ACCESS_CHECKED_WR | Checked data memory access, write.                                  |
| 0x8000   | SIMD_INST_RETIRED     | Instruction architecturally executed, SIMD.                         |
| 0x8001   | ASE_INST_RETIRED      | Instruction architecturally executed, Advanced SIMD.                |
| 0x8002   | SVE_INST_RETIRED      | Instruction architecturally executed, SVE.                          |
| 0x8003   | ASE_SVE_INST_RETIRED  | Instruction architecturally executed, Advanced SIMD or SVE.         |
| 0x8004   | SIMD_INST_SPEC        | Operation speculatively executed, SIMD.                             |
| 0x8005   | ASE_INST_SPEC         | Operation speculatively executed, Advanced SIMD.                    |
| 0x8006   | SVE_INST_SPEC         | Operation speculatively executed, SVE.                              |
| 0x8007   | ASE_SVE_INST_SPEC     | Operation speculatively executed, Advanced SIMD or SVE.             |
| 0x8008   | UOP_SPEC              | Microarchitectural operation speculatively executed.                |
| 0x8009   | ASE_UOP_SPEC          | Microarchitectural operation speculatively executed, Advanced SIMD. |
| 0x800A   | SVE_UOP_SPEC          | Microarchitectural operation speculatively executed, SVE.           |

| Number   | Mnemonic           | Description                                                                                              |
|----------|--------------------|----------------------------------------------------------------------------------------------------------|
| 0x800B   | ASE_SVE_UOP_SPEC   | Microarchitectural operation speculatively executed, Advanced SIMD or SVE.                               |
| 0x800C   | SIMD_UOP_SPEC      | Microarchitectural operation speculatively executed, SIMD.                                               |
| 0x800E   | SVE_MATH_SPEC      | Operation speculatively executed, SVE math accelerator.                                                  |
| 0x8010   | FP_SPEC            | Floating-point operation speculatively executed, including SIMD.                                         |
| 0x8011   | ASE_FP_SPEC        | Floating-point operation speculatively executed, Advanced SIMD.                                          |
| 0x8012   | SVE_FP_SPEC        | Floating-point operation speculatively executed, SVE.                                                    |
| 0x8013   | ASE_SVE_FP_SPEC    | Floating-point operation speculatively executed, Advanced SIMD or SVE.                                   |
| 0x8014   | FP_HP_SPEC         | Floating-point operation speculatively executed, half-precision.                                         |
| 0x8015   | ASE_FP_HP_SPEC     | Floating-point operation speculatively executed, Advanced SIMD half-precision, data-processing.          |
| 0x8016   | SVE_FP_HP_SPEC     | Floating-point operation speculatively executed, SVE half-precision, data-processing.                    |
| 0x8017   | ASE_SVE_FP_HP_SPEC | Floating-point operation speculatively executed, Advanced SIMD or SVE half-precision.                    |
| 0x8018   | FP_SP_SPEC         | Floating-point operation speculatively executed, single-precision.                                       |
| 0x8019   | ASE_FP_SP_SPEC     | Floating-point operation speculatively executed, Advanced SIMD single-precision, data-processing.        |
| 0x801A   | SVE_FP_SP_SPEC     | Floating-point operation speculatively executed, SVE single-precision, data-processing.                  |
| 0x801B   | ASE_SVE_FP_SP_SPEC | Floating-point operation speculatively executed, Advanced SIMD or SVE single-precision, data-processing. |
| 0x801C   | FP_DP_SPEC         | Floating-point operation speculatively executed, double-precision, data-processing.                      |
| 0x801D   | ASE_FP_DP_SPEC     | Floating-point operation speculatively executed, Advanced SIMD double-precision, data-processing.        |
| 0x801E   | SVE_FP_DP_SPEC     | Floating-point operation speculatively executed, SVE double-precision, data-processing.                  |
| 0x801F   | ASE_SVE_FP_DP_SPEC | Floating-point operation speculatively executed, Advanced SIMD or SVE double-precision, data-processing. |
| 0x8020   | FP_DIV_SPEC        | Floating-point operation speculatively executed, divide.                                                 |

| Number   | Mnemonic               | Description                                                                             |
|----------|------------------------|-----------------------------------------------------------------------------------------|
| 0x8021   | ASE_FP_DIV_SPEC        | Floating-point operation speculatively executed, Advanced SIMD divide.                  |
| 0x8022   | SVE_FP_DIV_SPEC        | Floating-point operation speculatively executed, SVE divide.                            |
| 0x8023   | ASE_SVE_FP_DIV_SPEC    | Floating-point operation speculatively executed, Advanced SIMD or SVE divide.           |
| 0x8024   | FP_SQRT_SPEC           | Floating-point operation speculatively executed, square root.                           |
| 0x8025   | ASE_FP_SQRT_SPEC       | Floating-point operation speculatively executed, Advanced SIMD square root.             |
| 0x8026   | SVE_FP_SQRT_SPEC       | Floating-point operation speculatively executed, SVE square root.                       |
| 0x8027   | ASE_SVE_FP_SQRT_SPEC   | Floating-point operation speculatively executed, Advanced SIMD or SVE square-root.      |
| 0x8028   | FP_FMA_SPEC            | Floating-point operation speculatively executed, FMA.                                   |
| 0x8029   | ASE_FP_FMA_SPEC        | Floating-point operation speculatively executed, Advanced SIMD FMA.                     |
| 0x802A   | SVE_FP_FMA_SPEC        | Floating-point operation speculatively executed, SVE FMA.                               |
| 0x802B   | ASE_SVE_FP_FMA_SPEC    | Floating-point operation speculatively executed, Advanced SIMD or SVE FMA.              |
| 0x802C   | FP_MUL_SPEC            | Floating-point operation speculatively executed, multiply.                              |
| 0x802D   | ASE_FP_MUL_SPEC        | Floating-point operation speculatively executed, Advanced SIMD multiply.                |
| 0x802E   | SVE_FP_MUL_SPEC        | Floating-point operation speculatively executed, SVE multiply.                          |
| 0x802F   | ASE_SVE_FP_MUL_SPEC    | Floating-point operation speculatively executed, Advanced SIMD or SVE multiply.         |
| 0x8030   | FP_ADDSUB_SPEC         | Floating-point operation speculatively executed, add or subtract.                       |
| 0x8031   | ASE_FP_ADDSUB_SPEC     | Floating-point operation speculatively executed, Advanced SIMD add or subtract.         |
| 0x8032   | SVE_FP_ADDSUB_SPEC     | Floating-point operation speculatively executed, SVE add or subtract.                   |
| 0x8033   | ASE_SVE_FP_ADDSUB_SPEC | Floating-point operation speculatively executed, Advanced SIMD or SVE add or subtract . |
| 0x8034   | FP_RECPE_SPEC          | Floating-point operation speculatively executed, reciprocal estimate.                   |
| 0x8035   | ASE_FP_RECPE_SPEC      | Floating-point operation speculatively executed, Advanced SIMD reciprocal estimate.     |

| Number   | Mnemonic                | Description                                                                                               |
|----------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| 0x8036   | SVE_FP_RECPE_SPEC       | Floating-point operation speculatively executed, SVE reciprocal estimate.                                 |
| 0x8037   | ASE_SVE_FP_RECPE_SPEC   | Floating-point operation speculatively executed, Advanced SIMD or SVE reciprocal estimate.                |
| 0x8038   | FP_CVT_SPEC             | Floating-point operation speculatively executed, convert.                                                 |
| 0x8039   | ASE_FP_CVT_SPEC         | Floating-point operation speculatively executed, Advanced SIMD convert.                                   |
| 0x803A   | SVE_FP_CVT_SPEC         | Floating-point operation speculatively executed, SVE convert.                                             |
| 0x803B   | ASE_SVE_FP_CVT_SPEC     | Floating-point operation speculatively executed, Advanced SIMD or SVE convert.                            |
| 0x803C   | SVE_FP_AREDUCE_SPEC     | Floating-point operation speculatively executed, SVE accumulating reduction.                              |
| 0x803D   | ASE_FP_PREDUCE_SPEC     | Floating-point operation speculatively executed, Advanced SIMD pairwise add step or pairwise reduce step. |
| 0x803E   | SVE_FP_VREDUCE_SPEC     | Floating-point operation speculatively executed, SVE pairwise or reduction.                               |
| 0x803F   | ASE_SVE_FP_VREDUCE_SPEC | Floating-point operation speculatively executed, Advanced SIMD or SVE vector reduction.                   |
| 0x8040   | INT_SPEC                | Integer operation speculatively executed.                                                                 |
| 0x8041   | ASE_INT_SPEC            | Integer operation speculatively executed, Advanced SIMD.                                                  |
| 0x8042   | SVE_INT_SPEC            | Integer operation speculatively executed, SVE.                                                            |
| 0x8043   | ASE_SVE_INT_SPEC        | Integer operation speculatively executed, Advanced SIMD or SVE.                                           |
| 0x8044   | INT_DIV_SPEC            | Integer operation speculatively executed, divide.                                                         |
| 0x8045   | INT_DIV64_SPEC          | Integer operation speculatively executed, 64-bit divide.                                                  |
| 0x8046   | SVE_INT_DIV_SPEC        | Integer operation speculatively executed, SVE divide.                                                     |
| 0x8047   | SVE_INT_DIV64_SPEC      | Integer operation speculatively executed, SVE 64-bit divide.                                              |
| 0x8048   | INT_MUL_SPEC            | Integer operation speculatively executed, multiply.                                                       |
| 0x8049   | ASE_INT_MUL_SPEC        | Integer operation speculatively executed, Advanced SIMD multiply.                                         |
| 0x804A   | SVE_INT_MUL_SPEC        | Integer operation speculatively executed, SVE multiply.                                                   |
| 0x804B   | ASE_SVE_INT_MUL_SPEC    | Integer operation speculatively executed, Advanced SIMD or SVE multiply.                                  |

| Number   | Mnemonic                 | Description                                                                                      |
|----------|--------------------------|--------------------------------------------------------------------------------------------------|
| 0x804C   | INT_MUL64_SPEC           | Integer operation speculatively executed, 64 × 64 multiply.                                      |
| 0x804D   | SVE_INT_MUL64_SPEC       | Integer operation speculatively executed, SVE 64 × 64 multiply.                                  |
| 0x804E   | INT_MULH64_SPEC          | Integer operation speculatively executed, 64 × 64 multiply returning high part.                  |
| 0x804F   | SVE_INT_MULH64_SPEC      | Integer operation speculatively executed, SVE 64 × 64 multiply high part.                        |
| 0x8051   | ASE_FP_BF16_SPEC         | Floating-point operation speculatively executed, Advanced SIMD BFloat16, data-processing.        |
| 0x8052   | SVE_FP_BF16_SPEC         | Floating-point operation speculatively executed, SVE BFloat16, data-processing.                  |
| 0x8053   | ASE_SVE_FP_BF16_SPEC     | Floating-point operation speculatively executed, SVE or Advanced SIMD BFloat16, data-processing. |
| 0x8054   | FP_BF16_SPEC             | Floating-point operation speculatively executed, BFloat16, data-processing.                      |
| 0x8056   | SVE_SPEC                 | Operation speculatively executed, SVE data processing.                                           |
| 0x8057   | ASE_SVE_SPEC             | Operation speculatively executed, Advanced SIMD data processing or SVE data processing.          |
| 0x8058   | NONFP_SPEC               | Non-floating-point operation speculatively executed.                                             |
| 0x8059   | ASE_NONFP_SPEC           | Non-floating-point operation speculatively executed, Advanced SIMD.                              |
| 0x805A   | SVE_NONFP_SPEC           | Non-floating-point operation speculatively executed, SVE.                                        |
| 0x805B   | ASE_SVE_NONFP_SPEC       | Non-floating-point operation speculatively executed, Advanced SIMD or SVE.                       |
| 0x805D   | ASE_INT_VREDUCE_SPEC     | Integer operation speculatively executed, Advanced SIMD reduction.                               |
| 0x805E   | SVE_INT_VREDUCE_SPEC     | Integer operation speculatively executed, SVE reduction.                                         |
| 0x805F   | ASE_SVE_INT_VREDUCE_SPEC | Integer operation speculatively executed, Advanced SIMD or SVE reduction.                        |
| 0x8060   | SVE_PERM_SPEC            | Operation speculatively executed, SVE permute.                                                   |
| 0x8061   | SVE_PERM_IGRANULE_SPEC   | Operation speculatively executed, SVE intra-granule permute.                                     |
| 0x8062   | SVE_PERM_XGRANULE_SPEC   | Operation speculatively executed, SVE cross-granule permute.                                     |

| Number   | Mnemonic               | Description                                                                       |
|----------|------------------------|-----------------------------------------------------------------------------------|
| 0x8063   | SVE_PERM_VARIABLE_SPEC | Operation speculatively executed, SVE programmable permute.                       |
| 0x8064   | SVE_XPIPE_SPEC         | Operation speculatively executed, SVE cross-pipe.                                 |
| 0x8065   | SVE_XPIPE_Z2R_SPEC     | Operation speculatively executed, SVE vector to scalar cross-pipe.                |
| 0x8066   | SVE_XPIPE_R2Z_SPEC     | Operation speculatively executed, SVE scalar to vector cross-pipe.                |
| 0x8067   | SVE_PGEN_NVEC_SPEC     | Operation speculatively executed, SVE predicate-only.                             |
| 0x8068   | SVE_PGEN_SPEC          | Operation speculatively executed, SVE predicate generating.                       |
| 0x8069   | SVE_PGEN_FLG_SPEC      | Operation speculatively executed, SVE predicate flag setting.                     |
| 0x806A   | SVE_PGEN_CMP_SPEC      | Operation speculatively executed, SVE vector compare.                             |
| 0x806B   | SVE_PGEN_FCM_SPEC      | Floating-point operation speculatively executed, SVE vector compare.              |
| 0x806C   | SVE_PGEN_LOGIC_SPEC    | Operation speculatively executed, SVE predicate logical.                          |
| 0x806D   | SVE_PPERM_SPEC         | Operation speculatively executed, SVE predicate permute.                          |
| 0x806E   | SVE_PSCAN_SPEC         | Operation speculatively executed, SVE predicate scan.                             |
| 0x806F   | SVE_PCNT_SPEC          | Operation speculatively executed, SVE predicate count.                            |
| 0x8070   | SVE_PLOOP_WHILE_SPEC   | Operation speculatively executed, SVE predicate loop while.                       |
| 0x8071   | SVE_PLOOP_TEST_SPEC    | Operation speculatively executed, SVE predicate loop test.                        |
| 0x8072   | SVE_PLOOP_ELTS_SPEC    | Operation speculatively executed, SVE predicate loop elements.                    |
| 0x8073   | SVE_PLOOP_TERM_SPEC    | Operation speculatively executed, SVE predicate loop termination.                 |
| 0x8074   | SVE_PRED_SPEC          | Operation speculatively executed, SIMD predicated.                                |
| 0x8075   | SVE_PRED_EMPTY_SPEC    | Operation speculatively executed, SIMD predicated with no active elements.        |
| 0x8076   | SVE_PRED_FULL_SPEC     | Operation speculatively executed, SIMD predicated with all active elements.       |
| 0x8077   | SVE_PRED_PARTIAL_SPEC  | Operation speculatively executed, SIMD predicated with partially active elements. |
| 0x8078   | SVE_UNPRED_SPEC        | Operation speculatively executed, SVE unpredicated.                               |

| Number   | Mnemonic               | Description                                                                          |
|----------|------------------------|--------------------------------------------------------------------------------------|
| 0x8079   | SVE_PRED_NOT_FULL_SPEC | Operation speculatively executed, SVE predicated with at least one inactive element. |
| 0x807C   | SVE_MOVPRFX_SPEC       | Operation speculatively executed, SVE MOVPRFX.                                       |
| 0x807D   | SVE_MOVPRFX_Z_SPEC     | Operation speculatively executed, SVE MOVPRFXzeroing predication.                    |
| 0x807E   | SVE_MOVPRFX_M_SPEC     | Operation speculatively executed, SVE MOVPRFXmerging predication.                    |
| 0x807F   | SVE_MOVPRFX_U_SPEC     | Operation speculatively executed, SVE MOVPRFXunfused.                                |
| 0x8080   | SVE_LDST_SPEC          | Operation speculatively executed, SVE load, store, or prefetch.                      |
| 0x8081   | SVE_LD_SPEC            | Operation speculatively executed, SVE load.                                          |
| 0x8082   | SVE_ST_SPEC            | Operation speculatively executed, SVE store.                                         |
| 0x8083   | SVE_PRF_SPEC           | Operation speculatively executed, SVE prefetch.                                      |
| 0x8084   | ASE_SVE_LDST_SPEC      | Operation speculatively executed, Advanced SIMD or SVE load or store.                |
| 0x8085   | ASE_SVE_LD_SPEC        | Operation speculatively executed, Advanced SIMD or SVE load.                         |
| 0x8086   | ASE_SVE_ST_SPEC        | Operation speculatively executed, Advanced SIMD or SVE store.                        |
| 0x8087   | PRF_SPEC               | Operation speculatively executed, prefetch.                                          |
| 0x8088   | BASE_LDST_REG_SPEC     | Operation speculatively executed, general-purpose register load, store, or prefetch. |
| 0x8089   | BASE_LD_REG_SPEC       | Operation speculatively executed, general-purpose register load.                     |
| 0x808A   | BASE_ST_REG_SPEC       | Operation speculatively executed, general-purpose register store.                    |
| 0x808B   | BASE_PRF_SPEC          | Operation speculatively executed, general-purpose register prefetch.                 |
| 0x808C   | FPASE_LDST_REG_SPEC    | Operation speculatively executed, SIMD&FP register load or store.                    |
| 0x808D   | FPASE_LD_REG_SPEC      | Operation speculatively executed, SIMD&FP register load.                             |
| 0x808E   | FPASE_ST_REG_SPEC      | Operation speculatively executed, SIMD&FP register store.                            |
| 0x8090   | SVE_LDST_REG_SPEC      | Operation speculatively executed, SVE unpredicated load or store register.           |
| 0x8091   | SVE_LDR_REG_SPEC       | Operation speculatively executed, SVE unpredicated load register.                    |

| Number   | Mnemonic                | Description                                                                                      |
|----------|-------------------------|--------------------------------------------------------------------------------------------------|
| 0x8092   | SVE_STR_REG_SPEC        | Operation speculatively executed, SVE unpredicated store register.                               |
| 0x8094   | SVE_LDST_PREG_SPEC      | Operation speculatively executed, SVE load or store predicate register.                          |
| 0x8095   | SVE_LDR_PREG_SPEC       | Operation speculatively executed, SVE load predicate register.                                   |
| 0x8096   | SVE_STR_PREG_SPEC       | Operation speculatively executed, SVE store predicate register.                                  |
| 0x8098   | SVE_LDST_ZREG_SPEC      | Operation speculatively executed, SVE load or store vector register.                             |
| 0x8099   | SVE_LDR_ZREG_SPEC       | Operation speculatively executed, SVE load vector register.                                      |
| 0x809A   | SVE_STR_ZREG_SPEC       | Operation speculatively executed, SVE store vector register.                                     |
| 0x809C   | SVE_LDST_CONTIG_SPEC    | Operation speculatively executed, SVE contiguous load, store, or prefetch element.               |
| 0x809D   | SVE_LD_CONTIG_SPEC      | Operation speculatively executed, SVE single vector contiguous load element.                     |
| 0x809E   | SVE_ST_CONTIG_SPEC      | Operation speculatively executed, SVE contiguous store element.                                  |
| 0x809F   | SVE_PRF_CONTIG_SPEC     | Operation speculatively executed, SVE contiguous prefetch element.                               |
| 0x80A0   | SVE_LDSTNT_CONTIG_SPEC  | Operation speculatively executed, SVE non-temporal contiguous load or store element.             |
| 0x80A1   | SVE_LDNT_CONTIG_SPEC    | Operation speculatively executed, SVE non-temporal contiguous load element.                      |
| 0x80A2   | SVE_STNT_CONTIG_SPEC    | Operation speculatively executed, SVE non-temporal contiguous store element.                     |
| 0x80A4   | ASE_SVE_LDST_MULTI_SPEC | Operation speculatively executed, Advanced SIMD or SVE contiguous load or store multiple vector. |
| 0x80A5   | ASE_SVE_LD_MULTI_SPEC   | Operation speculatively executed, Advanced SIMD or SVE contiguous load multiple vector.          |
| 0x80A6   | ASE_SVE_ST_MULTI_SPEC   | Operation speculatively executed, Advanced SIMD or SVE contiguous store multiple vector.         |
| 0x80A8   | SVE_LDST_MULTI_SPEC     | Operation speculatively executed, SVE contiguous load or store multiple vector.                  |
| 0x80A9   | SVE_LD_MULTI_SPEC       | Operation speculatively executed, SVE contiguous load multiple vector.                           |
| 0x80AA   | SVE_ST_MULTI_SPEC       | Operation speculatively executed, SVE contiguous store multiple vector.                          |

| Number   | Mnemonic                           | Description                                                                                                       |
|----------|------------------------------------|-------------------------------------------------------------------------------------------------------------------|
| 0x80AC   | SVE_LDST_NONCONTIG_SPEC            | Operation speculatively executed, SVE non-contiguous load, store, or prefetch.                                    |
| 0x80AD   | SVE_LD_GATHER_SPEC                 | Operation speculatively executed, SVE gather-load.                                                                |
| 0x80AE   | SVE_ST_SCATTER_SPEC                | Operation speculatively executed, SVE scatter-store.                                                              |
| 0x80AF   | SVE_PRF_GATHER_SPEC                | Operation speculatively executed, SVE gather-prefetch.                                                            |
| 0x80B0   | SVE_LDST64_NONCONTIG_SPEC          | Operation speculatively executed, SVE 64-bit non-contiguous load, store, or prefetch.                             |
| 0x80B1   | SVE_LD64_GATHER_SPEC               | Operation speculatively executed, SVE 64-bit gather-load.                                                         |
| 0x80B2   | SVE_ST64_SCATTER_SPEC              | Operation speculatively executed, SVE 64-bit scatter-store.                                                       |
| 0x80B3   | SVE_PRF64_GATHER_SPEC              | Operation speculatively executed, SVE 64-bit gather-prefetch.                                                     |
| 0x80B4   | ASE_SVE_UNALIGNED_LDST_SPEC        | Advanced SIMD or SVE unaligned access.                                                                            |
| 0x80B5   | ASE_SVE_UNALIGNED_LD_SPEC          | Advanced SIMD or SVE unaligned read.                                                                              |
| 0x80B6   | ASE_SVE_UNALIGNED_ST_SPEC          | Advanced SIMD or SVE unaligned write.                                                                             |
| 0x80B8   | ASE_SVE_UNALIGNED_CONTIG_LDST_SPEC | Advanced SIMD or SVE unaligned contiguous access.                                                                 |
| 0x80B9   | ASE_SVE_UNALIGNED_CONTIG_LD_SPEC   | Advanced SIMD or SVE unaligned contiguous read.                                                                   |
| 0x80BA   | ASE_SVE_UNALIGNED_CONTIG_ST_SPEC   | Advanced SIMD or SVE unaligned contiguous write.                                                                  |
| 0x80BC   | SVE_LDFF_SPEC                      | Operation speculatively executed, SVE first-fault load.                                                           |
| 0x80BD   | SVE_LDFF_FAULT_SPEC                | Operation speculatively executed, SVE first-fault load which set FFR bit to 0.                                    |
| 0x80C0   | FP_SCALE_OPS_SPEC                  | Scalable element arithmetic operations speculatively executed, floating-point.                                    |
| 0x80C1   | FP_FIXED_OPS_SPEC                  | Non-scalable element arithmetic operations speculatively executed, floating-point.                                |
| 0x80C2   | FP_HP_SCALE_OPS_SPEC               | Scalable element arithmetic operations speculatively executed, largest type is half-precision floating-point.     |
| 0x80C3   | FP_HP_FIXED_OPS_SPEC               | Non-scalable element arithmetic operations speculatively executed, largest type is half-precision floating-point. |

| Number   | Mnemonic                | Description                                                                                                         |
|----------|-------------------------|---------------------------------------------------------------------------------------------------------------------|
| 0x80C4   | FP_SP_SCALE_OPS_SPEC    | Scalable element arithmetic operations speculatively executed, largest type is single-precision floating-point.     |
| 0x80C5   | FP_SP_FIXED_OPS_SPEC    | Non-scalable element arithmetic operations speculatively executed, largest type is single-precision floating-point. |
| 0x80C6   | FP_DP_SCALE_OPS_SPEC    | Scalable element arithmetic operations speculatively executed, largest type is double-precision floating-point.     |
| 0x80C7   | FP_DP_FIXED_OPS_SPEC    | Non-scalable element arithmetic operations speculatively executed, largest type is double-precision floating-point. |
| 0x80C8   | INT_SCALE_OPS_SPEC      | Scalable element arithmetic operations speculatively executed, integer.                                             |
| 0x80C9   | INT_FIXED_OPS_SPEC      | Non-scalable element arithmetic operations speculatively executed, integer.                                         |
| 0x80CA   | LDST_SCALE_OPS_SPEC     | Scalable load or store element operations speculatively executed.                                                   |
| 0x80CB   | LDST_FIXED_OPS_SPEC     | Non-scalable load or store element operations speculatively executed.                                               |
| 0x80CC   | LD_SCALE_OPS_SPEC       | Scalable load element operations speculatively executed.                                                            |
| 0x80CD   | LD_FIXED_OPS_SPEC       | Non-scalable load element operations speculatively executed.                                                        |
| 0x80CE   | ST_SCALE_OPS_SPEC       | Scalable store element operations speculatively executed.                                                           |
| 0x80CF   | ST_FIXED_OPS_SPEC       | Non-scalable store element operations speculatively executed.                                                       |
| 0x80D0   | FP_SCALE2_OPS_SPEC      | Scalable tile arithmetic operations speculatively executed, floating-point.                                         |
| 0x80D2   | FP_HP_SCALE2_OPS_SPEC   | Scalable tile arithmetic operations speculatively executed, largest type is half-precision floating-point.          |
| 0x80D3   | FP_BF16_SCALE2_OPS_SPEC | Scalable tile arithmetic operations speculatively executed, largest type is BFloat16 floating-point.                |
| 0x80D4   | FP_SP_SCALE2_OPS_SPEC   | Scalable tile arithmetic operations speculatively executed, largest type is single-precision floating-point.        |
| 0x80D6   | FP_DP_SCALE2_OPS_SPEC   | Scalable tile arithmetic operations speculatively executed, largest type is double-precision floating-point.        |
| 0x80D8   | INT_SCALE2_OPS_SPEC     | Scalable tile arithmetic operations speculatively executed, integer.                                                |

| Number   | Mnemonic               | Description                                                                                             |
|----------|------------------------|---------------------------------------------------------------------------------------------------------|
| 0x80DA   | LDST_SCALE_BYTES_SPEC  | Scalable load and store bytes speculatively executed.                                                   |
| 0x80DB   | LDST_FIXED_BYTES_SPEC  | Non-scalable load and store bytes speculatively executed.                                               |
| 0x80DC   | LD_SCALE_BYTES_SPEC    | Scalable load bytes speculatively executed.                                                             |
| 0x80DD   | LD_FIXED_BYTES_SPEC    | Non-scalable load bytes speculatively executed.                                                         |
| 0x80DE   | ST_SCALE_BYTES_SPEC    | Scalable store bytes speculatively executed.                                                            |
| 0x80DF   | ST_FIXED_BYTES_SPEC    | Non-scalable store bytes speculatively executed.                                                        |
| 0x80E1   | ASE_INT8_SPEC          | Integer operation speculatively executed, Advanced SIMD 8-bit.                                          |
| 0x80E2   | SVE_INT8_SPEC          | Integer operation speculatively executed, SVE 8-bit.                                                    |
| 0x80E3   | ASE_SVE_INT8_SPEC      | Integer operation speculatively executed, Advanced SIMD or SVE 8-bit.                                   |
| 0x80E5   | ASE_INT16_SPEC         | Integer operation speculatively executed, Advanced SIMD 16-bit.                                         |
| 0x80E6   | SVE_INT16_SPEC         | Integer operation speculatively executed, SVE 16-bit.                                                   |
| 0x80E7   | ASE_SVE_INT16_SPEC     | Integer operation speculatively executed, Advanced SIMD or SVE 16-bit.                                  |
| 0x80E8   | FP_BF16_SCALE_OPS_SPEC | Scalable element arithmetic operations speculatively executed, largest type is BFloat16 floating-point. |
| 0x80E9   | ASE_INT32_SPEC         | Integer operation speculatively executed, Advanced SIMD 32-bit.                                         |
| 0x80EA   | SVE_INT32_SPEC         | Integer operation speculatively executed, SVE 32-bit.                                                   |
| 0x80EB   | ASE_SVE_INT32_SPEC     | Integer operation speculatively executed, Advanced SIMD or SVE 32-bit.                                  |
| 0x80ED   | ASE_INT64_SPEC         | Integer operation speculatively executed, Advanced SIMD 64-bit.                                         |
| 0x80EE   | SVE_INT64_SPEC         | Integer operation speculatively executed, SVE 64-bit.                                                   |
| 0x80EF   | ASE_SVE_INT64_SPEC     | Integer operation speculatively executed, Advanced SIMD or SVE 64-bit.                                  |
| 0x80F1   | ASE_FP_DOT_SPEC        | Floating-point operation speculatively executed, Advanced SIMD dot-product.                             |
| 0x80F2   | SVE_FP_DOT_SPEC        | Floating-point operation speculatively executed, SVE dot-product.                                       |

| Number   | Mnemonic                  | Description                                                                                  |
|----------|---------------------------|----------------------------------------------------------------------------------------------|
| 0x80F3   | ASE_SVE_FP_DOT_SPEC       | Floating-point operation speculatively executed, Advanced SIMD or SVE dot-product.           |
| 0x80F5   | ASE_FP_MMLA_SPEC          | Floating-point operation speculatively executed, Advanced SIMD matrix multiply.              |
| 0x80F6   | SVE_FP_MMLA_SPEC          | Floating-point operation speculatively executed, SVE matrix multiply.                        |
| 0x80F7   | ASE_SVE_FP_MMLA_SPEC      | Floating-point operation speculatively executed, Advanced SIMD or SVE matrix multiply.       |
| 0x80F9   | ASE_INT_DOT_SPEC          | Operation speculatively executed, Advanced SIMD integer dot-product.                         |
| 0x80FA   | SVE_INT_DOT_SPEC          | Integer operation speculatively executed, SVE dot-product.                                   |
| 0x80FB   | ASE_SVE_INT_DOT_SPEC      | Integer operation speculatively executed, Advanced SIMD or SVE dot-product.                  |
| 0x80FD   | ASE_INT_MMLA_SPEC         | Integer operation speculatively executed, Advanced SIMD matrix multiply.                     |
| 0x80FE   | SVE_INT_MMLA_SPEC         | Integer operation speculatively executed, SVE matrix multiply.                               |
| 0x80FF   | ASE_SVE_INT_MMLA_SPEC     | Integer operation speculatively executed, Advanced SIMD or SVE matrix multiply.              |
| 0x8107   | BR_SKIP_RETIRED           | Branch instruction architecturally executed, not taken.                                      |
| 0x8108   | BR_IMMED_TAKEN_RETIRED    | Branch instruction architecturally executed, immediate, taken.                               |
| 0x8109   | BR_IMMED_SKIP_RETIRED     | Branch instruction architecturally executed, immediate, not taken.                           |
| 0x810A   | BR_IND_TAKEN_RETIRED      | Branch instruction architecturally executed, indirect, taken.                                |
| 0x810B   | BR_IND_SKIP_RETIRED       | Branch instruction architecturally executed, indirect, not taken.                            |
| 0x810C   | BR_INDNR_TAKEN_RETIRED    | Branch instruction architecturally executed, indirect excluding procedure return, taken.     |
| 0x810D   | BR_INDNR_SKIP_RETIRED     | Branch instruction architecturally executed, indirect excluding procedure return, not taken. |
| 0x810E   | BR_RETURN_ANY_RETIRED     | Branch instruction architecturally executed, procedure return.                               |
| 0x810F   | BR_RETURN_SKIP_RETIRED    | Branch instruction architecturally executed, procedure return, not taken.                    |
| 0x8110   | BR_IMMED_PRED_RETIRED     | Branch instruction architecturally executed, predicted immediate.                            |
| 0x8111   | BR_IMMED_MIS_PRED_RETIRED | Branch instruction architecturally executed, mispredicted immediate.                         |

| Number   | Mnemonic                   | Description                                                                                    |
|----------|----------------------------|------------------------------------------------------------------------------------------------|
| 0x8112   | BR_IND_PRED_RETIRED        | Branch instruction architecturally executed, predicted indirect.                               |
| 0x8113   | BR_IND_MIS_PRED_RETIRED    | Branch instruction architecturally executed, mispredicted indirect.                            |
| 0x8114   | BR_RETURN_PRED_RETIRED     | Branch instruction architecturally executed, predicted procedure return.                       |
| 0x8115   | BR_RETURN_MIS_PRED_RETIRED | Branch instruction architecturally executed, mispredicted procedure return.                    |
| 0x8116   | BR_INDNR_PRED_RETIRED      | Branch instruction architecturally executed, predicted indirect excluding procedure return.    |
| 0x8117   | BR_INDNR_MIS_PRED_RETIRED  | Branch instruction architecturally executed, mispredicted indirect excluding procedure return. |
| 0x8118   | BR_TAKEN_PRED_RETIRED      | Branch instruction architecturally executed, predicted branch, taken.                          |
| 0x8119   | BR_TAKEN_MIS_PRED_RETIRED  | Branch instruction architecturally executed, mispredicted branch, taken.                       |
| 0x811A   | BR_SKIP_PRED_RETIRED       | Branch instruction architecturally executed, predicted branch, not taken.                      |
| 0x811B   | BR_SKIP_MIS_PRED_RETIRED   | Branch instruction architecturally executed, mispredicted branch, not taken.                   |
| 0x811C   | BR_PRED_RETIRED            | Branch instruction architecturally executed, predicted branch.                                 |
| 0x811D   | BR_IND_RETIRED             | Instruction architecturally executed, indirect branch.                                         |
| 0x811E   | BR_INDNR_RETIRED           | Branch instruction architecturally executed, indirect excluding procedure return.              |
| 0x811F   | BRB_FILTRATE               | Branch Record captured.                                                                        |
| 0x8120   | INST_FETCH_PERCYC          | Instruction fetches in progress.                                                               |
| 0x8121   | MEM_ACCESS_RD_PERCYC       | Data memory reads in progress.                                                                 |
| 0x8122   | SAMPLE_FEED_DS             | Statistical Profiling sample taken, selected Data Source.                                      |
| 0x8123   | SAMPLE_BUFFER_FULL         | Profiling Buffer full.                                                                         |
| 0x8124   | INST_FETCH                 | Instruction memory access.                                                                     |
| 0x8125   | BUS_REQ_RD_PERCYC          | Bus read transactions in progress.                                                             |
| 0x8126   | BUS_REQ_WR_PERCYC          | Bus write transactions in progress.                                                            |
| 0x8127   | PMU_SNAPSHOT               | Successful PMUcapture event.                                                                   |
| 0x8128   | DTLB_WALK_PERCYC           | Data translation table walks in progress.                                                      |
| 0x8129   | ITLB_WALK_PERCYC           | Instruction translation table walks in progress.                                               |
| 0x812A   | SAMPLE_FEED_BR             | Statistical Profiling sample taken, branch.                                                    |

| Number   | Mnemonic          | Description                                                                  |
|----------|-------------------|------------------------------------------------------------------------------|
| 0x812B   | SAMPLE_FEED_LD    | Statistical Profiling sample taken, load.                                    |
| 0x812C   | SAMPLE_FEED_ST    | Statistical Profiling sample taken, store.                                   |
| 0x812D   | SAMPLE_FEED_OP    | Statistical Profiling sample taken, matching type.                           |
| 0x812E   | SAMPLE_FEED_EVENT | Statistical Profiling sample taken, matching events.                         |
| 0x812F   | SAMPLE_FEED_LAT   | Statistical Profiling sample taken, exceeding minimum latency.               |
| 0x8130   | L1D_TLB_RW        | Level 1 data TLB access, demand access.                                      |
| 0x8131   | L1I_TLB_RD        | Level 1 instruction TLB access, demand access.                               |
| 0x8132   | L1D_TLB_PRFM      | Level 1 data TLB access, software prefetch.                                  |
| 0x8133   | L1I_TLB_PRFM      | Level 1 instruction TLB access, software prefetch.                           |
| 0x8134   | DTLB_HWUPD        | Data TLB hardware update of translation table.                               |
| 0x8135   | ITLB_HWUPD        | Instruction TLB hardware update of translation table.                        |
| 0x8136   | DTLB_STEP         | Data TLB translation table walk, step.                                       |
| 0x8137   | ITLB_STEP         | Instruction TLB translation table walk, step.                                |
| 0x8138   | DTLB_WALK_LARGE   | Data TLB large page translation table walk.                                  |
| 0x8139   | ITLB_WALK_LARGE   | Instruction TLB large page translation table walk.                           |
| 0x813A   | DTLB_WALK_SMALL   | Data TLB small page translation table walk.                                  |
| 0x813B   | ITLB_WALK_SMALL   | Instruction TLB small page translation table walk.                           |
| 0x813C   | DTLB_WALK_RW      | Data TLB demand access, with at least one translation table walk.            |
| 0x813D   | ITLB_WALK_RD      | Instruction TLB demand access, with at least one translation table walk.     |
| 0x813E   | DTLB_WALK_PRFM    | Data TLB software prefetch, with at least one translation table walk.        |
| 0x813F   | ITLB_WALK_PRFM    | Instruction TLB software prefetch, with at least one translation table walk. |
| 0x8140   | L1D_CACHE_RW      | Level 1 data cache demand access.                                            |
| 0x8141   | L1I_CACHE_RD      | Level 1 instruction cache demand fetch.                                      |
| 0x8142   | L1D_CACHE_PRFM    | Level 1 data cache software prefetch.                                        |
| 0x8143   | L1I_CACHE_PRFM    | Level 1 instruction cache software prefetch.                                 |

| Number   | Mnemonic                      | Description                                           |
|----------|-------------------------------|-------------------------------------------------------|
| 0x8144   | L1D_CACHE_MISS                | Level 1 data cache demand access miss.                |
| 0x8145   | L1I_CACHE_HWPRF               | Level 1 instruction cache hardware prefetch.          |
| 0x8146   | L1D_CACHE_REFILL_PRFM         | Level 1 data cache refill, software prefetch.         |
| 0x8147   | L1I_CACHE_REFILL_PRFM         | Level 1 instruction cache refill, software prefetch.  |
| 0x8148   | L2D_CACHE_RW                  | Level 2 data cache demand access.                     |
| 0x8149   | L2I_CACHE_RD                  | Level 2 instruction cache demand fetch.               |
| 0x814A   | L2D_CACHE_PRFM                | Level 2 data cache software prefetch.                 |
| 0x814B   | L2I_CACHE_PRFM                | Level 2 instruction cache software prefetch.          |
| 0x814C   | L2D_CACHE_MISS                | Level 2 data cache demand access miss.                |
| 0x814D   | L2I_CACHE_HWPRF               | Level 2 instruction cache hardware prefetch.          |
| 0x814E   | L2D_CACHE_REFILL_PRFM         | Level 2 data cache refill, software prefetch.         |
| 0x814F   | L2I_CACHE_REFILL_PRFM         | Level 2 instruction cache refill, software prefetch.  |
| 0x8150   | L3D_CACHE_RW                  | Level 3 data cache demand access.                     |
| 0x8151   | L3D_CACHE_PRFM                | Level 3 data cache software prefetch.                 |
| 0x8152   | L3D_CACHE_MISS                | Level 3 data cache demand access miss.                |
| 0x8153   | L3D_CACHE_REFILL_PRFM         | Level 3 data cache refill, software prefetch.         |
| 0x8154   | L1D_CACHE_HWPRF               | Level 1 data cache hardware prefetch.                 |
| 0x8155   | L2D_CACHE_HWPRF               | Level 2 data cache hardware prefetch.                 |
| 0x8156   | L3D_CACHE_HWPRF               | Level 3 data cache hardware prefetch.                 |
| 0x8157   | LL_CACHE_HWPRF                | Last level cache hardware prefetch.                   |
| 0x8158   | STALL_FRONTEND_MEMBOUND       | Frontend stall cycles, memory bound.                  |
| 0x8159   | STALL_FRONTEND_L1I            | Frontend stall cycles, level 1 instruction cache.     |
| 0x815A   | STALL_FRONTEND_L2I            | Frontend stall cycles, level 2 instruction cache.     |
| 0x815B   | STALL_FRONTEND_MEM            | Frontend stall cycles, last level PE cache or memory. |
| 0x815C   | STALL_FRONTEND_TLB            | Frontend stall cycles, TLB.                           |
| 0x815D   | STALL_BACKEND_BUSY_SMCU       | Backend stall cycles, SMCUbusy.                       |
| 0x815E   | STALL_BACKEND_BUSY_SMCU_UNALL | Backend stall cycles, awaitingSMCU allocation.        |
| 0x8160   | STALL_FRONTEND_CPUBOUND       | Frontend stall cycles, processor bound.               |
| 0x8161   | STALL_FRONTEND_FLOW           | Frontend stall cycles, flow control.                  |

| Number   | Mnemonic                 | Description                                                                                                  |
|----------|--------------------------|--------------------------------------------------------------------------------------------------------------|
| 0x8162   | STALL_FRONTEND_FLUSH     | Frontend stall cycles, flush recovery.                                                                       |
| 0x8163   | STALL_FRONTEND_RENAME    | Frontend stall cycles, rename full.                                                                          |
| 0x8164   | STALL_BACKEND_MEMBOUND   | Backend stall cycles, memory bound.                                                                          |
| 0x8165   | STALL_BACKEND_L1D        | Backend stall cycles, level 1 data cache.                                                                    |
| 0x8166   | STALL_BACKEND_L2D        | Backend stall cycles, level 2 data cache.                                                                    |
| 0x8167   | STALL_BACKEND_TLB        | Backend stall cycles, TLB.                                                                                   |
| 0x8168   | STALL_BACKEND_ST         | Backend stall cycles, store.                                                                                 |
| 0x816A   | STALL_BACKEND_CPUBOUND   | Backend stall cycles, processor bound.                                                                       |
| 0x816B   | STALL_BACKEND_BUSY       | Backend stall cycles, backend busy.                                                                          |
| 0x816C   | STALL_BACKEND_ILOCK      | Backend stall cycles, input dependency.                                                                      |
| 0x816D   | STALL_BACKEND_RENAME     | Backend stall cycles, rename full.                                                                           |
| 0x816E   | STALL_BACKEND_ATOMIC     | Backend stall cycles, atomic operation.                                                                      |
| 0x816F   | STALL_BACKEND_MEMCPYSET  | Backend stall cycles, Memory Copy or Set operation.                                                          |
| 0x8170   | CAS_NEAR_FAIL            | Atomic memory Operation speculatively executed, Compare and Swap fail.                                       |
| 0x8171   | CAS_NEAR_PASS            | Atomic memory Operation speculatively executed, Compare and Swap pass.                                       |
| 0x8172   | CAS_NEAR_SPEC            | Atomic memory Operation speculatively executed, Compare and Swap near.                                       |
| 0x8173   | CAS_FAR_SPEC             | Atomic memory Operation speculatively executed, Compare and Swap far.                                        |
| 0x8174   | CAS_SPEC                 | Atomic memory Operation speculatively executed, Compare and Swap.                                            |
| 0x8175   | LSE_LD_SPEC              | Atomic memory Operation speculatively executed, load.                                                        |
| 0x8176   | LSE_ST_SPEC              | Atomic memory Operation speculatively executed, store.                                                       |
| 0x8177   | LSE_LDST_SPEC            | Atomic memory Operation speculatively executed, load or store.                                               |
| 0x8178   | REMOTE_ACCESS_WR         | Access to a remote device, write.                                                                            |
| 0x8179   | BRNL_INDNR_TAKEN_RETIRED | Branch instruction architecturally executed, indirect branch without link excluding procedure return, taken. |
| 0x817A   | BL_TAKEN_RETIRED         | Branch instruction architecturally executed, branch with link, taken.                                        |
| 0x817B   | BRNL_TAKEN_RETIRED       | Branch instruction architecturally executed, branch without link, taken.                                     |

| Number   | Mnemonic                      | Description                                                                       |
|----------|-------------------------------|-----------------------------------------------------------------------------------|
| 0x817C   | BL_IND_TAKEN_RETIRED          | Branch instruction architecturally executed, indirect branch with link, taken.    |
| 0x817D   | BRNL_IND_TAKEN_RETIRED        | Branch instruction architecturally executed, indirect branch without link, taken. |
| 0x817E   | BL_IMMED_TAKEN_RETIRED        | Branch instruction architecturally executed, direct branch with link, taken.      |
| 0x817F   | BRNL_IMMED_TAKEN_RETIRED      | Branch instruction architecturally executed, direct branch without link, taken.   |
| 0x8180   | BR_UNCOND_RETIRED             | Branch instruction architecturally executed, unconditional branch.                |
| 0x8181   | BR_COND_RETIRED               | Branch instruction architecturally executed, conditional branch.                  |
| 0x8182   | BR_COND_TAKEN_RETIRED         | Branch instruction architecturally executed, conditional branch, taken.           |
| 0x8183   | BR_HINT_COND_RETIRED          | Branch instruction architecturally executed, hinted conditional.                  |
| 0x8184   | BR_HINT_COND_PRED_RETIRED     | Branch instruction architecturally executed, predicted hinted conditional.        |
| 0x8185   | BR_HINT_COND_MIS_PRED_RETIRED | Branch instruction architecturally executed, mispredicted hinted conditional.     |
| 0x8186   | UOP_RETIRED                   | Micro-operation architecturally executed.                                         |
| 0x8188   | DTLB_WALK_BLOCK               | Data TLB block translation table walk.                                            |
| 0x8189   | ITLB_WALK_BLOCK               | Instruction TLB block translation table walk.                                     |
| 0x818A   | DTLB_WALK_PAGE                | Data TLB page translation table walk.                                             |
| 0x818B   | ITLB_WALK_PAGE                | Instruction TLB page translation table walk.                                      |
| 0x818D   | BUS_REQ_RD                    | Bus request, read.                                                                |
| 0x818E   | BUS_REQ_WR                    | Bus request, write.                                                               |
| 0x818F   | BUS_REQ                       | Bus request.                                                                      |
| 0x8190   | ISNP_HIT_RD                   | Snoop hit, demand instruction fetch.                                              |
| 0x8191   | ISNP_HIT_NEAR_RD              | Snoop hit in near local cache, demand instruction fetch.                          |
| 0x8192   | ISNP_HIT_FAR_RD               | Snoop hit in far local cache, demand instruction fetch.                           |
| 0x8193   | ISNP_HIT_REMOTE_RD            | Snoop hit in remote cache, demand instruction fetch.                              |
| 0x8194   | DSNP_HIT_RD                   | Snoop hit, demand data read.                                                      |
| 0x8195   | DSNP_HIT_NEAR_RD              | Snoop hit in near local cache, demand data read.                                  |

| Number   | Mnemonic              | Description                                                   |
|----------|-----------------------|---------------------------------------------------------------|
| 0x8196   | DSNP_HIT_FAR_RD       | Snoop hit in far local cache, demand data read.               |
| 0x8197   | DSNP_HIT_REMOTE_RD    | Snoop hit in remote cache, demand data read.                  |
| 0x8198   | DSNP_HIT_WR           | Snoop hit, demand data write.                                 |
| 0x8199   | DSNP_HIT_NEAR_WR      | Snoop hit in near local cache, demand data write.             |
| 0x819A   | DSNP_HIT_FAR_WR       | Snoop hit in far local cache, demand data write.              |
| 0x819B   | DSNP_HIT_REMOTE_WR    | Snoop hit in remote cache, demand data write.                 |
| 0x819C   | DSNP_HIT_RW           | Snoop hit, demand data access.                                |
| 0x819D   | DSNP_HIT_NEAR_RW      | Snoop hit in near local cache, demand data access.            |
| 0x819E   | DSNP_HIT_FAR_RW       | Snoop hit in far local cache, demand data access.             |
| 0x819F   | DSNP_HIT_REMOTE_RW    | Snoop hit in remote cache, demand data access.                |
| 0x81A0   | DSNP_HIT_PRFM         | Snoop hit, software data prefetch.                            |
| 0x81A1   | DSNP_HIT_NEAR_PRFM    | Snoop hit in near local cache, software data prefetch.        |
| 0x81A2   | DSNP_HIT_FAR_PRFM     | Snoop hit in far local cache, software data prefetch.         |
| 0x81A3   | DSNP_HIT_REMOTE_PRFM  | Snoop hit in remote cache, software data prefetch.            |
| 0x81A4   | DSNP_HIT_HWPRF        | Snoop hit, hardware data prefetch.                            |
| 0x81A5   | DSNP_HIT_NEAR_HWPRF   | Snoop hit in near local cache, hardware data prefetch.        |
| 0x81A6   | DSNP_HIT_FAR_HWPRF    | Snoop hit in far local cache, hardware data prefetch.         |
| 0x81A7   | DSNP_HIT_REMOTE_HWPRF | Snoop hit in remote cache, hardware data prefetch.            |
| 0x81A8   | ISNP_HIT_PRFM         | Snoop hit, software instruction prefetch.                     |
| 0x81A9   | ISNP_HIT_NEAR_PRFM    | Snoop hit in near local cache, software instruction prefetch. |
| 0x81AA   | ISNP_HIT_FAR_PRFM     | Snoop hit in far local cache, software instruction prefetch.  |
| 0x81AB   | ISNP_HIT_REMOTE_PRFM  | Snoop hit in remote cache, software instruction prefetch.     |
| 0x81AC   | ISNP_HIT_HWPRF        | Snoop hit, hardware instruction prefetch.                     |
| 0x81AD   | ISNP_HIT_NEAR_HWPRF   | Snoop hit in near local cache, hardware instruction prefetch. |
| 0x81AE   | ISNP_HIT_FAR_HWPRF    | Snoop hit in far local cache, hardware instruction prefetch.  |
| 0x81AF   | ISNP_HIT_REMOTE_HWPRF | Snoop hit in remote cache, hardware instruction prefetch.     |

| Number   | Mnemonic               | Description                                          |
|----------|------------------------|------------------------------------------------------|
| 0x81B0   | ISNP_HIT               | Snoop hit, instruction.                              |
| 0x81B1   | ISNP_HIT_NEAR          | Snoop hit in near local cache, instruction access.   |
| 0x81B2   | ISNP_HIT_FAR           | Snoop hit in far local cache, instruction access.    |
| 0x81B3   | ISNP_HIT_REMOTE        | Snoop hit in remote cache, instruction access.       |
| 0x81B4   | DSNP_HIT               | Snoop hit, data.                                     |
| 0x81B5   | DSNP_HIT_NEAR          | Snoop hit in near local cache, data access.          |
| 0x81B6   | DSNP_HIT_FAR           | Snoop hit in far local cache, data access.           |
| 0x81B7   | DSNP_HIT_REMOTE        | Snoop hit in remote cache, data access.              |
| 0x81B8   | L1I_CACHE_REFILL_HWPRF | Level 1 instruction cache refill, hardware prefetch. |
| 0x81B9   | L2I_CACHE_REFILL_HWPRF | Level 2 instruction cache refill, hardware prefetch. |
| 0x81BC   | L1D_CACHE_REFILL_HWPRF | Level 1 data cache refill, hardware prefetch.        |
| 0x81BD   | L2D_CACHE_REFILL_HWPRF | Level 2 data cache refill, hardware prefetch.        |
| 0x81BE   | L3D_CACHE_REFILL_HWPRF | Level 3 data cache refill, hardware prefetch.        |
| 0x81BF   | LL_CACHE_REFILL_HWPRF  | Last level cache refill, hardware prefetch.          |
| 0x81C0   | L1I_CACHE_HIT_RD       | Level 1 instruction cache demand fetch hit.          |
| 0x81C1   | L2I_CACHE_HIT_RD       | Level 2 instruction cache demand fetch hit.          |
| 0x81C4   | L1D_CACHE_HIT_RD       | Level 1 data cache demand access hit, read.          |
| 0x81C5   | L2D_CACHE_HIT_RD       | Level 2 data cache demand access hit, read.          |
| 0x81C6   | L3D_CACHE_HIT_RD       | Level 3 data cache demand access hit, read.          |
| 0x81C7   | LL_CACHE_HIT_RD        | Last level cache demand access hit, read.            |
| 0x81C8   | L1D_CACHE_HIT_WR       | Level 1 data cache demand access hit, write.         |
| 0x81C9   | L2D_CACHE_HIT_WR       | Level 2 data cache demand access hit, write.         |
| 0x81CA   | L3D_CACHE_HIT_WR       | Level 3 data cache demand access hit, write.         |
| 0x81CB   | LL_CACHE_HIT_WR        | Last level cache demand access hit, write.           |
| 0x81CC   | L1D_CACHE_HIT_RW       | Level 1 data cache demand access hit.                |
| 0x81CD   | L2D_CACHE_HIT_RW       | Level 2 data cache demand access hit.                |

| Number   | Mnemonic                | Description                                                                       |
|----------|-------------------------|-----------------------------------------------------------------------------------|
| 0x81CE   | L3D_CACHE_HIT_RW        | Level 3 data cache demand access hit.                                             |
| 0x81CF   | LL_CACHE_HIT_RW         | Last level cache demand access hit.                                               |
| 0x81D0   | L1I_CACHE_HIT_RD_FPRFM  | Level 1 instruction cache demand fetch first hit, fetched by software prefetch.   |
| 0x81D1   | L2I_CACHE_HIT_RD_FPRFM  | Level 2 instruction cache demand fetch first hit, fetched by software prefetch.   |
| 0x81D4   | L1D_CACHE_HIT_RD_FPRFM  | Level 1 data cache demand access first hit, read, fetched by software prefetch.   |
| 0x81D5   | L2D_CACHE_HIT_RD_FPRFM  | Level 2 data cache demand access first hit, read, fetched by software prefetch.   |
| 0x81D6   | L3D_CACHE_HIT_RD_FPRFM  | Level 3 data cache demand access first hit, read, fetched by software prefetch.   |
| 0x81D7   | LL_CACHE_HIT_RD_FPRFM   | Last level cache demand access first hit, read, fetched by software prefetch.     |
| 0x81D8   | L1D_CACHE_HIT_WR_FPRFM  | Level 1 data cache demand access first hit, write, fetched by software prefetch.  |
| 0x81D9   | L2D_CACHE_HIT_WR_FPRFM  | Level 2 data cache demand access first hit, write, fetched by software prefetch.  |
| 0x81DA   | L3D_CACHE_HIT_WR_FPRFM  | Level 3 data cache demand access first hit, write, fetched by software prefetch.  |
| 0x81DB   | LL_CACHE_HIT_WR_FPRFM   | Last level cache demand access first hit, write, fetched by software prefetch.    |
| 0x81DC   | L1D_CACHE_HIT_RW_FPRFM  | Level 1 data cache demand access first hit, fetched by software prefetch.         |
| 0x81DD   | L2D_CACHE_HIT_RW_FPRFM  | Level 2 data cache demand access first hit, fetched by software prefetch.         |
| 0x81DE   | L3D_CACHE_HIT_RW_FPRFM  | Level 3 data cache demand access first hit, fetched by software prefetch.         |
| 0x81DF   | LL_CACHE_HIT_RW_FPRFM   | Last level cache demand access first hit, fetched by software prefetch.           |
| 0x81E0   | L1I_CACHE_HIT_RD_FHWPRF | Level 1 instruction cache demand fetch first hit, fetched by hardware prefetcher. |
| 0x81E1   | L2I_CACHE_HIT_RD_FHWPRF | Level 2 instruction cache demand fetch first hit, fetched by hardware prefetcher. |
| 0x81E4   | L1D_CACHE_HIT_RD_FHWPRF | Level 1 data cache demand access first hit, read, fetched by hardware prefetcher. |
| 0x81E5   | L2D_CACHE_HIT_RD_FHWPRF | Level 2 data cache demand access first hit, read, fetched by hardware prefetcher. |

| Number   | Mnemonic                | Description                                                                        |
|----------|-------------------------|------------------------------------------------------------------------------------|
| 0x81E6   | L3D_CACHE_HIT_RD_FHWPRF | Level 3 data cache demand access first hit, read, fetched by hardware prefetcher.  |
| 0x81E7   | LL_CACHE_HIT_RD_FHWPRF  | Last level cache demand access first hit, read, fetched by hardware prefetcher.    |
| 0x81E8   | L1D_CACHE_HIT_WR_FHWPRF | Level 1 data cache demand access first hit, write, fetched by hardware prefetcher. |
| 0x81E9   | L2D_CACHE_HIT_WR_FHWPRF | Level 2 data cache demand access first hit, write, fetched by hardware prefetcher. |
| 0x81EA   | L3D_CACHE_HIT_WR_FHWPRF | Level 3 data cache demand access first hit, write, fetched by hardware prefetcher. |
| 0x81EB   | LL_CACHE_HIT_WR_FHWPRF  | Last level cache demand access first hit, write, fetched by hardware prefetcher.   |
| 0x81EC   | L1D_CACHE_HIT_RW_FHWPRF | Level 1 data cache demand access first hit, fetched by hardware prefetcher.        |
| 0x81ED   | L2D_CACHE_HIT_RW_FHWPRF | Level 2 data cache demand access first hit, fetched by hardware prefetcher.        |
| 0x81EE   | L3D_CACHE_HIT_RW_FHWPRF | Level 3 data cache demand access first hit, fetched by hardware prefetcher.        |
| 0x81EF   | LL_CACHE_HIT_RW_FHWPRF  | Last level cache demand access first hit, fetched by hardware prefetcher.          |
| 0x81F0   | L1I_CACHE_HIT_RD_FPRF   | Level 1 instruction cache demand fetch first hit, fetched by prefetch.             |
| 0x81F1   | L2I_CACHE_HIT_RD_FPRF   | Level 2 instruction cache demand fetch first hit, fetched by prefetch.             |
| 0x81F4   | L1D_CACHE_HIT_RD_FPRF   | Level 1 data cache demand access first hit, read, fetched by prefetch.             |
| 0x81F5   | L2D_CACHE_HIT_RD_FPRF   | Level 2 data cache demand access first hit, read, fetched by prefetch.             |
| 0x81F6   | L3D_CACHE_HIT_RD_FPRF   | Level 3 data cache demand access first hit, read, fetched by prefetch.             |
| 0x81F7   | LL_CACHE_HIT_RD_FPRF    | Last level cache demand access first hit, read, fetched by prefetch.               |
| 0x81F8   | L1D_CACHE_HIT_WR_FPRF   | Level 1 data cache demand access first hit, write, fetched by prefetch.            |
| 0x81F9   | L2D_CACHE_HIT_WR_FPRF   | Level 2 data cache demand access first hit, write, fetched by prefetch.            |
| 0x81FA   | L3D_CACHE_HIT_WR_FPRF   | Level 3 data cache demand access first hit, write, fetched by prefetch.            |
| 0x81FB   | LL_CACHE_HIT_WR_FPRF    | Last level cache demand access first hit, write, fetched by prefetch.              |

| Number   | Mnemonic              | Description                                                      |
|----------|-----------------------|------------------------------------------------------------------|
| 0x81FC   | L1D_CACHE_HIT_RW_FPRF | Level 1 data cache demand access first hit, fetched by prefetch. |
| 0x81FD   | L2D_CACHE_HIT_RW_FPRF | Level 2 data cache demand access first hit, fetched by prefetch. |
| 0x81FE   | L3D_CACHE_HIT_RW_FPRF | Level 3 data cache demand access first hit, fetched by prefetch. |
| 0x81FF   | LL_CACHE_HIT_RW_FPRF  | Last level cache demand access first hit, fetched by prefetch.   |
| 0x8200   | L1I_CACHE_HIT         | Level 1 instruction cache hit.                                   |
| 0x8201   | L2I_CACHE_HIT         | Level 2 instruction cache hit.                                   |
| 0x8204   | L1D_CACHE_HIT         | Level 1 data cache hit.                                          |
| 0x8205   | L2D_CACHE_HIT         | Level 2 data cache hit.                                          |
| 0x8206   | L3D_CACHE_HIT         | Level 3 data cache hit.                                          |
| 0x8207   | LL_CACHE_HIT          | Last level cache hit.                                            |
| 0x8208   | L1I_CACHE_HIT_PRFM    | Level 1 instruction cache software prefetch hit.                 |
| 0x8209   | L2I_CACHE_HIT_PRFM    | Level 2 instruction cache software prefetch hit.                 |
| 0x820C   | L1D_CACHE_HIT_PRFM    | Level 1 data cache software prefetch hit.                        |
| 0x820D   | L2D_CACHE_HIT_PRFM    | Level 2 data cache software prefetch hit.                        |
| 0x820E   | L3D_CACHE_HIT_PRFM    | Level 3 data cache software prefetch hit.                        |
| 0x820F   | LL_CACHE_HIT_PRFM     | Last level cache software prefetch hit.                          |
| 0x8214   | L1D_CACHE_HITM_RD     | Level 1 data cache demand access hit modified, read.             |
| 0x8215   | L2D_CACHE_HITM_RD     | Level 2 data cache demand access hit modified, read.             |
| 0x8216   | L3D_CACHE_HITM_RD     | Level 3 data cache demand access hit modified, read.             |
| 0x8217   | LL_CACHE_HITM_RD      | Last level cache demand access hit modified, read.               |
| 0x8218   | L1D_CACHE_HITM_WR     | Level 1 data cache demand access hit modified, write.            |
| 0x8219   | L2D_CACHE_HITM_WR     | Level 2 data cache demand access hit modified, write.            |
| 0x821A   | L3D_CACHE_HITM_WR     | Level 3 data cache demand access hit modified, write.            |
| 0x821B   | LL_CACHE_HITM_WR      | Last level cache demand access hit modified, write.              |
| 0x821C   | L1D_CACHE_HITM_RW     | Level 1 data cache demand access hit modified.                   |
| 0x821D   | L2D_CACHE_HITM_RW     | Level 2 data cache demand access hit modified.                   |
| 0x821E   | L3D_CACHE_HITM_RW     | Level 3 data cache demand access hit modified.                   |

| Number   | Mnemonic               | Description                                                                                   |
|----------|------------------------|-----------------------------------------------------------------------------------------------|
| 0x821F   | LL_CACHE_HITM_RW       | Last level cache demand access hit modified.                                                  |
| 0x8224   | DSNP_HITM_RD           | Snoop hit, demand data read, modified.                                                        |
| 0x8225   | DSNP_HITM_NEAR_RD      | Snoop hit in near local cache, demand data read, modified.                                    |
| 0x8226   | DSNP_HITM_FAR_RD       | Snoop hit in far local cache, demand data read, modified.                                     |
| 0x8227   | DSNP_HITM_REMOTE_RD    | Snoop hit in remote cache, demand data read, modified.                                        |
| 0x8228   | DSNP_HITM_WR           | Snoop hit, demand data write, modified.                                                       |
| 0x8229   | DSNP_HITM_NEAR_WR      | Snoop hit in near local cache, demand data write, modified.                                   |
| 0x822A   | DSNP_HITM_FAR_WR       | Snoop hit in far local cache, demand data write, modified.                                    |
| 0x822B   | DSNP_HITM_REMOTE_WR    | Snoop hit in remote cache, demand data write, modified.                                       |
| 0x822C   | DSNP_HITM_RW           | Snoop hit, demand data access, modified.                                                      |
| 0x822D   | DSNP_HITM_NEAR_RW      | Snoop hit in near local cache, demand data access, modified.                                  |
| 0x822E   | DSNP_HITM_FAR_RW       | Snoop hit in far local cache, demand data access, modified.                                   |
| 0x822F   | DSNP_HITM_REMOTE_RW    | Snoop hit in remote cache, demand data access, modified.                                      |
| 0x8230   | LOCAL_MEM              | Access to memory attached to this device.                                                     |
| 0x8231   | LOCAL_MEM_RD           | Access to memory attached to this device, demand access, read.                                |
| 0x8232   | LOCAL_MEM_WR           | Access to memory attached to this device, demand access, write.                               |
| 0x8233   | LOCAL_MEM_RW           | Access to memory attached to this device, demand access.                                      |
| 0x8234   | LOCAL_MEM_PRFM         | Access to memory attached to this device, software prefetch.                                  |
| 0x8235   | LOCAL_MEM_LD_RETIRED   | Load instruction architecturally executed, access to memory attached to this device.          |
| 0x8236   | LOCAL_MEM_ST_RETIRED   | Store instruction architecturally executed, access to memory attached to this device.         |
| 0x8237   | LOCAL_MEM_LDST_RETIRED | Load or store instruction architecturally executed, access to memory attached to this device. |
| 0x8238   | REMOTE_MEM             | Access to memory attached to a remote device.                                                 |
| 0x8239   | REMOTE_MEM_RD          | Access to memory attached to a remote device, demand access, read.                            |

| Number   | Mnemonic                | Description                                                                                               |
|----------|-------------------------|-----------------------------------------------------------------------------------------------------------|
| 0x823A   | REMOTE_MEM_WR           | Access to memory attached to a remote device, demand access, write.                                       |
| 0x823B   | REMOTE_MEM_RW           | Access to memory attached to a remote device, demand access.                                              |
| 0x823C   | REMOTE_MEM_PRFM         | Access to memory attached to a remote device, software prefetch.                                          |
| 0x823D   | REMOTE_MEM_LD_RETIRED   | Load instruction architecturally executed, access to memory attached to a remote device.                  |
| 0x823E   | REMOTE_MEM_ST_RETIRED   | Store instruction architecturally executed, access to memory attached to a remote device.                 |
| 0x823F   | REMOTE_MEM_LDST_RETIRED | Load or store instruction architecturally executed, access to memory attached to a remote device.         |
| 0x8240   | L1I_LFB_HIT_RD          | Level 1 instruction cache demand fetch line-fill buffer hit.                                              |
| 0x8241   | L2I_LFB_HIT_RD          | Level 2 instruction cache demand fetch line-fill buffer hit.                                              |
| 0x8244   | L1D_LFB_HIT_RD          | Level 1 data cache demand access line-fill buffer hit, read.                                              |
| 0x8245   | L2D_LFB_HIT_RD          | Level 2 data cache demand access line-fill buffer hit, read.                                              |
| 0x8246   | L3D_LFB_HIT_RD          | Level 3 data cache demand access line-fill buffer hit, read.                                              |
| 0x8247   | LL_LFB_HIT_RD           | Last level cache demand access line-fill buffer hit, read.                                                |
| 0x8248   | L1D_LFB_HIT_WR          | Level 1 data cache demand access line-fill buffer hit, write.                                             |
| 0x8249   | L2D_LFB_HIT_WR          | Level 2 data cache demand access line-fill buffer hit, write.                                             |
| 0x824A   | L3D_LFB_HIT_WR          | Level 3 data cache demand access line-fill buffer hit, write.                                             |
| 0x824B   | LL_LFB_HIT_WR           | Last level cache demand access line-fill buffer hit, write.                                               |
| 0x824C   | L1D_LFB_HIT_RW          | Level 1 data cache demand access line-fill buffer hit.                                                    |
| 0x824D   | L2D_LFB_HIT_RW          | Level 2 data cache demand access line-fill buffer hit.                                                    |
| 0x824E   | L3D_LFB_HIT_RW          | Level 3 data cache demand access line-fill buffer hit.                                                    |
| 0x824F   | LL_LFB_HIT_RW           | Last level cache demand access line-fill buffer hit.                                                      |
| 0x8250   | L1I_LFB_HIT_RD_FPRFM    | Level 1 instruction cache demand fetch line-fill buffer first hit, recently fetched by software prefetch. |
| 0x8251   | L2I_LFB_HIT_RD_FPRFM    | Level 2 instruction cache demand fetch line-fill buffer first hit, recently fetched by software prefetch. |

| Number   | Mnemonic              | Description                                                                                                 |
|----------|-----------------------|-------------------------------------------------------------------------------------------------------------|
| 0x8254   | L1D_LFB_HIT_RD_FPRFM  | Level 1 data cache demand access line-fill buffer first hit, read, recently fetched by software prefetch.   |
| 0x8255   | L2D_LFB_HIT_RD_FPRFM  | Level 2 data cache demand access line-fill buffer first hit, read, recently fetched by software prefetch.   |
| 0x8256   | L3D_LFB_HIT_RD_FPRFM  | Level 3 data cache demand access line-fill buffer first hit, read, recently fetched by software prefetch.   |
| 0x8257   | LL_LFB_HIT_RD_FPRFM   | Last level cache demand access line-fill buffer first hit, read, recently fetched by software prefetch.     |
| 0x8258   | L1D_LFB_HIT_WR_FPRFM  | Level 1 data cache demand access line-fill buffer first hit, write, recently fetched by software prefetch.  |
| 0x8259   | L2D_LFB_HIT_WR_FPRFM  | Level 2 data cache demand access line-fill buffer first hit, write, recently fetched by software prefetch.  |
| 0x825A   | L3D_LFB_HIT_WR_FPRFM  | Level 3 data cache demand access line-fill buffer first hit, write, recently fetched by software prefetch.  |
| 0x825B   | LL_LFB_HIT_WR_FPRFM   | Last level cache demand access line-fill buffer first hit, write, recently fetched by software prefetch.    |
| 0x825C   | L1D_LFB_HIT_RW_FPRFM  | Level 1 data cache demand access line-fill buffer first hit, recently fetched by software prefetch.         |
| 0x825D   | L2D_LFB_HIT_RW_FPRFM  | Level 2 data cache demand access line-fill buffer first hit, recently fetched by software prefetch.         |
| 0x825E   | L3D_LFB_HIT_RW_FPRFM  | Level 3 data cache demand access line-fill buffer first hit, recently fetched by software prefetch.         |
| 0x825F   | LL_LFB_HIT_RW_FPRFM   | Last level cache demand access line-fill buffer first hit, recently fetched by software prefetch.           |
| 0x8260   | L1I_LFB_HIT_RD_FHWPRF | Level 1 instruction cache demand fetch line-fill buffer first hit, recently fetched by hardware prefetcher. |
| 0x8261   | L2I_LFB_HIT_RD_FHWPRF | Level 2 instruction cache demand fetch line-fill buffer first hit, recently fetched by hardware prefetcher. |
| 0x8264   | L1D_LFB_HIT_RD_FHWPRF | Level 1 data cache demand access line-fill buffer first hit, read, recently fetched by hardware prefetcher. |
| 0x8265   | L2D_LFB_HIT_RD_FHWPRF | Level 2 data cache demand access line-fill buffer first hit, read, recently fetched by hardware prefetcher. |
| 0x8266   | L3D_LFB_HIT_RD_FHWPRF | Level 3 data cache demand access line-fill buffer first hit, read, recently fetched by hardware prefetcher. |

| Number   | Mnemonic              | Description                                                                                                  |
|----------|-----------------------|--------------------------------------------------------------------------------------------------------------|
| 0x8267   | LL_LFB_HIT_RD_FHWPRF  | Last level cache demand access line-fill buffer first hit, read, recently fetched by hardware prefetcher.    |
| 0x8268   | L1D_LFB_HIT_WR_FHWPRF | Level 1 data cache demand access line-fill buffer first hit, write, recently fetched by hardware prefetcher. |
| 0x8269   | L2D_LFB_HIT_WR_FHWPRF | Level 2 data cache demand access line-fill buffer first hit, write, recently fetched by hardware prefetcher. |
| 0x826A   | L3D_LFB_HIT_WR_FHWPRF | Level 3 data cache demand access line-fill buffer first hit, write, recently fetched by hardware prefetcher. |
| 0x826B   | LL_LFB_HIT_WR_FHWPRF  | Last level cache demand access line-fill buffer first hit, write, recently fetched by hardware prefetcher.   |
| 0x826C   | L1D_LFB_HIT_RW_FHWPRF | Level 1 data cache demand access line-fill buffer first hit, recently fetched by hardware prefetcher.        |
| 0x826D   | L2D_LFB_HIT_RW_FHWPRF | Level 2 data cache demand access line-fill buffer first hit, recently fetched by hardware prefetcher.        |
| 0x826E   | L3D_LFB_HIT_RW_FHWPRF | Level 3 data cache demand access line-fill buffer first hit, recently fetched by hardware prefetcher.        |
| 0x826F   | LL_LFB_HIT_RW_FHWPRF  | Last level cache demand access line-fill buffer first hit, recently fetched by hardware prefetcher.          |
| 0x8270   | L1I_LFB_HIT_RD_FPRF   | Level 1 instruction cache demand fetch line-fill buffer first hit, recently fetched by prefetch.             |
| 0x8271   | L2I_LFB_HIT_RD_FPRF   | Level 2 instruction cache demand fetch line-fill buffer first hit, recently fetched by prefetch.             |
| 0x8274   | L1D_LFB_HIT_RD_FPRF   | Level 1 data cache demand access line-fill buffer first hit, read, recently fetched by prefetch.             |
| 0x8275   | L2D_LFB_HIT_RD_FPRF   | Level 2 data cache demand access line-fill buffer first hit, read, recently fetched by prefetch.             |
| 0x8276   | L3D_LFB_HIT_RD_FPRF   | Level 3 data cache demand access line-fill buffer first hit, read, recently fetched by prefetch.             |
| 0x8277   | LL_LFB_HIT_RD_FPRF    | Last level cache demand access line-fill buffer first hit, read, recently fetched by prefetch.               |
| 0x8278   | L1D_LFB_HIT_WR_FPRF   | Level 1 data cache demand access line-fill buffer first hit, write, recently fetched by prefetch.            |
| 0x8279   | L2D_LFB_HIT_WR_FPRF   | Level 2 data cache demand access line-fill buffer first hit, write, recently fetched by prefetch.            |

| Number   | Mnemonic             | Description                                                                                       |
|----------|----------------------|---------------------------------------------------------------------------------------------------|
| 0x827A   | L3D_LFB_HIT_WR_FPRF  | Level 3 data cache demand access line-fill buffer first hit, write, recently fetched by prefetch. |
| 0x827B   | LL_LFB_HIT_WR_FPRF   | Last level cache demand access line-fill buffer first hit, write, recently fetched by prefetch.   |
| 0x827C   | L1D_LFB_HIT_RW_FPRF  | Level 1 data cache demand access line-fill buffer first hit, recently fetched by prefetch.        |
| 0x827D   | L2D_LFB_HIT_RW_FPRF  | Level 2 data cache demand access line-fill buffer first hit, recently fetched by prefetch.        |
| 0x827E   | L3D_LFB_HIT_RW_FPRF  | Level 3 data cache demand access line-fill buffer first hit, recently fetched by prefetch.        |
| 0x827F   | LL_LFB_HIT_RW_FPRF   | Last level cache demand access line-fill buffer first hit, recently fetched by prefetch.          |
| 0x8280   | L1I_CACHE_PRF        | Level 1 instruction cache, prefetch hit.                                                          |
| 0x8281   | L2I_CACHE_PRF        | Level 2 instruction cache, prefetch hit.                                                          |
| 0x8284   | L1D_CACHE_PRF        | Level 1 data cache, prefetch hit.                                                                 |
| 0x8285   | L2D_CACHE_PRF        | Level 2 data cache, prefetch hit.                                                                 |
| 0x8286   | L3D_CACHE_PRF        | Level 3 data cache, prefetch hit.                                                                 |
| 0x8287   | LL_CACHE_PRF         | Last level cache, prefetch hit.                                                                   |
| 0x8288   | L1I_CACHE_REFILL_PRF | Level 1 instruction cache refill, prefetch hit.                                                   |
| 0x8289   | L2I_CACHE_REFILL_PRF | Level 2 instruction cache refill, prefetch hit.                                                   |
| 0x828C   | L1D_CACHE_REFILL_PRF | Level 1 data cache refill, prefetch hit.                                                          |
| 0x828D   | L2D_CACHE_REFILL_PRF | Level 2 data cache refill, prefetch hit.                                                          |
| 0x828E   | L3D_CACHE_REFILL_PRF | Level 3 data cache refill, prefetch hit.                                                          |
| 0x828F   | LL_CACHE_REFILL_PRF  | Last level cache refill, prefetch hit.                                                            |
| 0x8290   | ISNP_HIT_PRF         | Snoop hit, instruction prefetch.                                                                  |
| 0x8291   | ISNP_HIT_NEAR_PRF    | Snoop hit in near local cache, instruction prefetch.                                              |
| 0x8292   | ISNP_HIT_FAR_PRF     | Snoop hit in far local cache, instruction prefetch.                                               |
| 0x8293   | ISNP_HIT_REMOTE_PRF  | Snoop hit in remote cache, instruction prefetch.                                                  |
| 0x8294   | DSNP_HIT_PRF         | Snoop hit, data prefetch.                                                                         |
| 0x8295   | DSNP_HIT_NEAR_PRF    | Snoop hit in near local cache, data prefetch.                                                     |
| 0x8296   | DSNP_HIT_FAR_PRF     | Snoop hit in far local cache, data prefetch.                                                      |
| 0x8297   | DSNP_HIT_REMOTE_PRF  | Snoop hit in remote cache, data prefetch.                                                         |
| 0x8298   | LL_CACHE_RW          | Last level cache demand access.                                                                   |

| Number   | Mnemonic                  | Description                                                                                 |
|----------|---------------------------|---------------------------------------------------------------------------------------------|
| 0x8299   | LL_CACHE_PRFM             | Last level cache software prefetch.                                                         |
| 0x829A   | LL_CACHE_REFILL           | Last level cache refill.                                                                    |
| 0x829B   | LL_CACHE_REFILL_PRFM      | Last level cache refill, software prefetch.                                                 |
| 0x829C   | LL_CACHE_WB               | Last level cache write-back.                                                                |
| 0x829D   | LL_CACHE_WR               | Last level cache access, write.                                                             |
| 0x829F   | LL_CACHE_REFILL_WR        | Last level cache refill, write.                                                             |
| 0x82A0   | MEM_ACCESS_RW             | Data memory access, demand access.                                                          |
| 0x82A1   | INST_FETCH_RD             | Instruction memory access, demand fetch.                                                    |
| 0x82A2   | MEM_ACCESS_PRFM           | Data memory access, software prefetch.                                                      |
| 0x82A3   | INST_FETCH_PRFM           | Instruction memory access, software prefetch.                                               |
| 0x82A4   | ASE_SVE_RETIRED           | Instruction architecturally executed, Advanced SIMD data processing or SVE data processing. |
| 0x82A8   | LD_ANY_RETIRED            | Instruction architecturally executed, load.                                                 |
| 0x82A9   | ST_ANY_RETIRED            | Instruction architecturally executed, store.                                                |
| 0x82AA   | LDST_ANY_RETIRED          | Instruction architecturally executed, load or store.                                        |
| 0x82AB   | DP_RETIRED                | Instruction architecturally executed, integer data processing.                              |
| 0x82AC   | ASE_RETIRED               | Instruction architecturally executed, Advanced SIMD data processing.                        |
| 0x82AD   | VFP_RETIRED               | Instruction architecturally executed, scalar floating-point data processing.                |
| 0x82AE   | SVE_RETIRED               | Instruction architecturally executed, SVE data processing.                                  |
| 0x82AF   | CRYPTO_RETIRED            | Instruction architecturally executed, cryptographic data processing.                        |
| 0x82B0   | L1I_CACHE_MISS_RETIRED    | Instruction architecturally executed, miss in Level 1 instruction cache.                    |
| 0x82B1   | L2I_CACHE_MISS_RETIRED    | Instruction architecturally executed, miss in Level 2 instruction cache.                    |
| 0x82B3   | PRF_RETIRED               | Instruction architecturally executed, prefetch.                                             |
| 0x82B4   | L1D_CACHE_MISS_LD_RETIRED | Load instruction architecturally executed, miss in Level 1 data cache.                      |
| 0x82B5   | L2D_CACHE_MISS_LD_RETIRED | Load instruction architecturally executed, miss in Level 2 data cache.                      |
| 0x82B6   | L3D_CACHE_MISS_LD_RETIRED | Load instruction architecturally executed, miss in Level 3 data cache.                      |
| 0x82B7   | LL_CACHE_MISS_LD_RETIRED  | Load instruction architecturally executed, miss in Last level cache.                        |

| Number   | Mnemonic                    | Description                                                                                  |
|----------|-----------------------------|----------------------------------------------------------------------------------------------|
| 0x82B8   | L1D_CACHE_MISS_ST_RETIRED   | Store instruction architecturally executed, miss in Level 1 data cache.                      |
| 0x82B9   | L2D_CACHE_MISS_ST_RETIRED   | Store instruction architecturally executed, miss in Level 2 data cache.                      |
| 0x82BA   | L3D_CACHE_MISS_ST_RETIRED   | Store instruction architecturally executed, miss in Level 3 data cache.                      |
| 0x82BB   | LL_CACHE_MISS_ST_RETIRED    | Store instruction architecturally executed, miss in Last level cache.                        |
| 0x82BC   | L1D_CACHE_MISS_LDST_RETIRED | Load or store instruction architecturally executed, miss in Level 1 data cache.              |
| 0x82BD   | L2D_CACHE_MISS_LDST_RETIRED | Load or store instruction architecturally executed, miss in Level 2 data cache.              |
| 0x82BE   | L3D_CACHE_MISS_LDST_RETIRED | Load or store instruction architecturally executed, miss in Level 3 data cache.              |
| 0x82BF   | LL_CACHE_MISS_LDST_RETIRED  | Load or store instruction architecturally executed, miss in Last level cache.                |
| 0x82C4   | L1D_CACHE_HITM_LD_RETIRED   | Load instruction architecturally executed, hit modified data in Level 1 data cache.          |
| 0x82C5   | L2D_CACHE_HITM_LD_RETIRED   | Load instruction architecturally executed, hit modified data in Level 2 data cache.          |
| 0x82C6   | L3D_CACHE_HITM_LD_RETIRED   | Load instruction architecturally executed, hit modified data in Level 3 data cache.          |
| 0x82C7   | LL_CACHE_HITM_LD_RETIRED    | Load instruction architecturally executed, hit modified data in Last level cache.            |
| 0x82C8   | L1D_CACHE_HITM_ST_RETIRED   | Store instruction architecturally executed, hit modified data in Level 1 data cache.         |
| 0x82C9   | L2D_CACHE_HITM_ST_RETIRED   | Store instruction architecturally executed, hit modified data in Level 2 data cache.         |
| 0x82CA   | L3D_CACHE_HITM_ST_RETIRED   | Store instruction architecturally executed, hit modified data in Level 3 data cache.         |
| 0x82CB   | LL_CACHE_HITM_ST_RETIRED    | Store instruction architecturally executed, hit modified data in Last level cache.           |
| 0x82CC   | L1D_CACHE_HITM_LDST_RETIRED | Load or store instruction architecturally executed, hit modified data in Level 1 data cache. |
| 0x82CD   | L2D_CACHE_HITM_LDST_RETIRED | Load or store instruction architecturally executed, hit modified data in Level 2 data cache. |

| Number   | Mnemonic                    | Description                                                                                     |
|----------|-----------------------------|-------------------------------------------------------------------------------------------------|
| 0x82CE   | L3D_CACHE_HITM_LDST_RETIRED | Load or store instruction architecturally executed, hit modified data in Level 3 data cache.    |
| 0x82CF   | LL_CACHE_HITM_LDST_RETIRED  | Load or store instruction architecturally executed, hit modified data in Last level cache.      |
| 0x82D0   | L1I_LFB_HIT_RETIRED         | Instruction architecturally executed, line-fill buffer hit in Level 1 instruction cache.        |
| 0x82D1   | L2I_LFB_HIT_RETIRED         | Instruction architecturally executed, line-fill buffer hit in Level 2 instruction cache.        |
| 0x82D4   | L1D_LFB_HIT_LD_RETIRED      | Load instruction architecturally executed, line-fill buffer hit in Level 1 data cache.          |
| 0x82D5   | L2D_LFB_HIT_LD_RETIRED      | Load instruction architecturally executed, line-fill buffer hit in Level 2 data cache.          |
| 0x82D6   | L3D_LFB_HIT_LD_RETIRED      | Load instruction architecturally executed, line-fill buffer hit in Level 3 data cache.          |
| 0x82D7   | LL_LFB_HIT_LD_RETIRED       | Load instruction architecturally executed, line-fill buffer hit in Last level cache.            |
| 0x82D8   | L1D_LFB_HIT_ST_RETIRED      | Store instruction architecturally executed, line-fill buffer hit in Level 1 data cache.         |
| 0x82D9   | L2D_LFB_HIT_ST_RETIRED      | Store instruction architecturally executed, line-fill buffer hit in Level 2 data cache.         |
| 0x82DA   | L3D_LFB_HIT_ST_RETIRED      | Store instruction architecturally executed, line-fill buffer hit in Level 3 data cache.         |
| 0x82DB   | LL_LFB_HIT_ST_RETIRED       | Store instruction architecturally executed, line-fill buffer hit in Last level cache.           |
| 0x82DC   | L1D_LFB_HIT_LDST_RETIRED    | Load or store instruction architecturally executed, line-fill buffer hit in Level 1 data cache. |
| 0x82DD   | L2D_LFB_HIT_LDST_RETIRED    | Load or store instruction architecturally executed, line-fill buffer hit in Level 2 data cache. |
| 0x82DE   | L3D_LFB_HIT_LDST_RETIRED    | Load or store instruction architecturally executed, line-fill buffer hit in Level 3 data cache. |
| 0x82DF   | LL_LFB_HIT_LDST_RETIRED     | Load or store instruction architecturally executed, line-fill buffer hit in Last level cache.   |
| 0x82E0   | L1I_CACHE_HIT_RETIRED       | Instruction architecturally executed, hit in Level 1 instruction cache.                         |
| 0x82E1   | L2I_CACHE_HIT_RETIRED       | Instruction architecturally executed, hit in Level 2 instruction cache.                         |

| Number   | Mnemonic                   | Description                                                                              |
|----------|----------------------------|------------------------------------------------------------------------------------------|
| 0x82E4   | L1D_CACHE_HIT_LD_RETIRED   | Load instruction architecturally executed, hit in Level 1 data cache.                    |
| 0x82E5   | L2D_CACHE_HIT_LD_RETIRED   | Load instruction architecturally executed, hit in Level 2 data cache.                    |
| 0x82E6   | L3D_CACHE_HIT_LD_RETIRED   | Load instruction architecturally executed, hit in Level 3 data cache.                    |
| 0x82E7   | LL_CACHE_HIT_LD_RETIRED    | Load instruction architecturally executed, hit in Last level cache.                      |
| 0x82E8   | L1D_CACHE_HIT_ST_RETIRED   | Store instruction architecturally executed, hit in Level 1 data cache.                   |
| 0x82E9   | L2D_CACHE_HIT_ST_RETIRED   | Store instruction architecturally executed, hit in Level 2 data cache.                   |
| 0x82EA   | L3D_CACHE_HIT_ST_RETIRED   | Store instruction architecturally executed, hit in Level 3 data cache.                   |
| 0x82EB   | LL_CACHE_HIT_ST_RETIRED    | Store instruction architecturally executed, hit in Last level cache.                     |
| 0x82EC   | L1D_CACHE_HIT_LDST_RETIRED | Load or store instruction architecturally executed, hit in Level 1 data cache.           |
| 0x82ED   | L2D_CACHE_HIT_LDST_RETIRED | Load or store instruction architecturally executed, hit in Level 2 data cache.           |
| 0x82EE   | L3D_CACHE_HIT_LDST_RETIRED | Load or store instruction architecturally executed, hit in Level 3 data cache.           |
| 0x82EF   | LL_CACHE_HIT_LDST_RETIRED  | Load or store instruction architecturally executed, hit in Last level cache.             |
| 0x82F0   | ITLB_HIT_RETIRED           | Instruction architecturally executed, no translation table walk.                         |
| 0x82F1   | DTLB_HIT_LD_RETIRED        | Load instruction architecturally executed, no translation table walk.                    |
| 0x82F2   | DTLB_HIT_ST_RETIRED        | Store instruction architecturally executed, no translation table walk.                   |
| 0x82F3   | DTLB_HIT_LDST_RETIRED      | Load or store instruction architecturally executed, no translation table walk.           |
| 0x82F4   | ITLB_WALK_RETIRED          | Instruction architecturally executed, at least one translation table walk.               |
| 0x82F5   | DTLB_WALK_LD_RETIRED       | Load instruction architecturally executed, at least one translation table walk.          |
| 0x82F6   | DTLB_WALK_ST_RETIRED       | Store instruction architecturally executed, at least one translation table walk.         |
| 0x82F7   | DTLB_WALK_LDST_RETIRED     | Load or store instruction architecturally executed, at least one translation table walk. |
| 0x82F8   | DTLB_WALK_PRF              | Data TLB prefetch, with at least one translation table walk.                             |

| Number   | Mnemonic                      | Description                                                                      |
|----------|-------------------------------|----------------------------------------------------------------------------------|
| 0x82F9   | ITLB_WALK_PRF                 | Instruction TLB prefetch, with at least one translation table walk.              |
| 0x82FA   | DTLB_WALK_HWPRF               | Data TLB hardware prefetch, with at least one translation table walk.            |
| 0x82FB   | ITLB_WALK_HWPRF               | Instruction TLB hardware prefetch, with at least one translation table walk.     |
| 0x82FC   | L1D_TLB_PRF                   | Level 1 data TLB access, prefetch.                                               |
| 0x82FD   | L1I_TLB_PRF                   | Level 1 instruction TLB access, prefetch.                                        |
| 0x82FE   | L1D_TLB_HWPRF                 | Level 1 data TLB access, hardware prefetch.                                      |
| 0x82FF   | L1I_TLB_HWPRF                 | Level 1 instruction TLB access, hardware prefetch.                               |
| 0x8304   | DSNP_HITM_LD_RETIRED          | Load instruction architecturally executed, snoop hit.                            |
| 0x8305   | DSNP_HITM_NEAR_LD_RETIRED     | Load instruction architecturally executed, snoop hit in near cache.              |
| 0x8306   | DSNP_HITM_FAR_LD_RETIRED      | Load instruction architecturally executed, snoop hit in far cache.               |
| 0x8307   | DSNP_HITM_REMOTE_LD_RETIRED   | Load instruction architecturally executed, snoop hit in remote cache.            |
| 0x8308   | DSNP_HITM_ST_RETIRED          | Store instruction architecturally executed, snoop hit.                           |
| 0x8309   | DSNP_HITM_NEAR_ST_RETIRED     | Store instruction architecturally executed, snoop hit in near cache.             |
| 0x830A   | DSNP_HITM_FAR_ST_RETIRED      | Store instruction architecturally executed, snoop hit in far cache.              |
| 0x830B   | DSNP_HITM_REMOTE_ST_RETIRED   | Store instruction architecturally executed, snoop hit in remote cache.           |
| 0x830C   | DSNP_HITM_LDST_RETIRED        | Load or store instruction architecturally executed, snoop hit.                   |
| 0x830D   | DSNP_HITM_NEAR_LDST_RETIRED   | Load or store instruction architecturally executed, snoop hit in near cache.     |
| 0x830E   | DSNP_HITM_FAR_LDST_RETIRED    | Load or store instruction architecturally executed, snoop hit in far cache.      |
| 0x830F   | DSNP_HITM_REMOTE_LDST_RETIRED | Load or store instruction architecturally executed, snoop hit in remote cache.   |
| 0x8310   | ISNP_HIT_RETIRED              | Instruction architecturally executed, instruction fetch snoop hit.               |
| 0x8311   | ISNP_HIT_NEAR_RETIRED         | Instruction architecturally executed, instruction fetch snoop hit in near cache. |
| 0x8312   | ISNP_HIT_FAR_RETIRED          | Instruction architecturally executed, instruction fetch snoop hit in far cache.  |

| Number   | Mnemonic                     | Description                                                                        |
|----------|------------------------------|------------------------------------------------------------------------------------|
| 0x8313   | ISNP_HIT_REMOTE_RETIRED      | Instruction architecturally executed, instruction fetch snoop hit in remote cache. |
| 0x8314   | DSNP_HIT_LD_RETIRED          | Load instruction architecturally executed, snoop hit.                              |
| 0x8315   | DSNP_HIT_NEAR_LD_RETIRED     | Load instruction architecturally executed, snoop hit in near cache.                |
| 0x8316   | DSNP_HIT_FAR_LD_RETIRED      | Load instruction architecturally executed, snoop hit in far cache.                 |
| 0x8317   | DSNP_HIT_REMOTE_LD_RETIRED   | Load instruction architecturally executed, snoop hit in remote cache.              |
| 0x8318   | DSNP_HIT_ST_RETIRED          | Store instruction architecturally executed, snoop hit.                             |
| 0x8319   | DSNP_HIT_NEAR_ST_RETIRED     | Store instruction architecturally executed, snoop hit in near cache.               |
| 0x831A   | DSNP_HIT_FAR_ST_RETIRED      | Store instruction architecturally executed, snoop hit in far cache.                |
| 0x831B   | DSNP_HIT_REMOTE_ST_RETIRED   | Store instruction architecturally executed, snoop hit in remote cache.             |
| 0x831C   | DSNP_HIT_LDST_RETIRED        | Load or store instruction architecturally executed, snoop hit.                     |
| 0x831D   | DSNP_HIT_NEAR_LDST_RETIRED   | Load or store instruction architecturally executed, snoop hit in near cache.       |
| 0x831E   | DSNP_HIT_FAR_LDST_RETIRED    | Load or store instruction architecturally executed, snoop hit in far cache.        |
| 0x831F   | DSNP_HIT_REMOTE_LDST_RETIRED | Load or store instruction architecturally executed, snoop hit in remote cache.     |
| 0x8320   | L1D_CACHE_REFILL_PERCYC      | Level 1 data or unified cache refills in progress.                                 |
| 0x8321   | L2D_CACHE_REFILL_PERCYC      | Level 2 data or unified cache refills in progress.                                 |
| 0x8322   | L3D_CACHE_REFILL_PERCYC      | Level 3 data or unified cache refills in progress.                                 |
| 0x8324   | L1I_CACHE_REFILL_PERCYC      | Level 1 instruction or unified cache refills in progress.                          |
| 0x8325   | L2I_CACHE_REFILL_PERCYC      | Level 2 instruction or unified cache refills in progress.                          |
| 0x8328   | REMOTE_CACHE_HIT_RD          | Remote cache demand access hit, read.                                              |
| 0x8329   | REMOTE_CACHE_HITM_RD         | Remote cache demand access hit modified, read.                                     |
| 0x832A   | REMOTE_LFB_HIT_RD            | Remote cache demand access line-fill buffer hit, read.                             |
| 0x832B   | REMOTE_CACHE_HIT_PRFM        | Remote cache software prefetch hit.                                                |

| Number   | Mnemonic                  | Description                                                                                              |
|----------|---------------------------|----------------------------------------------------------------------------------------------------------|
| 0x832C   | STALL_BACKEND_ATOMIC_FP   | Backend stall cycles, atomic in-memory floating-point load or store.                                     |
| 0x832D   | LSE_FP_LD_SPEC            | Atomic in-memory floating-point Operation speculatively executed, load.                                  |
| 0x832E   | LSE_FP_ST_SPEC            | Atomic in-memory floating-point Operation speculatively executed, store.                                 |
| 0x832F   | LSE_FP_LDST_SPEC          | Atomic in-memory floating-point Operation speculatively executed, load or store.                         |
| 0x8330   | L1GCS_CACHE               | Level 1 GCS cache access.                                                                                |
| 0x8331   | L1GCS_CACHE_RW            | Level 1 GCS cache demand access.                                                                         |
| 0x8332   | L1GCS_CACHE_HWPRF         | Level 1 GCS cache hardware prefetch.                                                                     |
| 0x8334   | L1GCS_CACHE_MISS          | Level 1 GCS cache demand access miss.                                                                    |
| 0x8335   | L1GCS_CACHE_MISS_RD       | Level 1 GCS cache demand access read miss.                                                               |
| 0x8336   | L1GCS_CACHE_HIT_RW        | Level 1 GCS cache demand access hit.                                                                     |
| 0x8337   | L1GCS_CACHE_HIT_RW_FHWPRF | Level 1 GCS cache demand access first hit, fetched by GCS hardware prefetcher.                           |
| 0x8338   | L1GCS_CACHE_REFILL        | Level 1 GCS cache refill.                                                                                |
| 0x8339   | L1GCS_CACHE_REFILL_HWPRF  | Level 1 GCS cache refill, hardware prefetch.                                                             |
| 0x833A   | L1GCS_CACHE_REFILL_PERCYC | Level 1 GCS cache refills in progress.                                                                   |
| 0x833C   | L1GCS_LFB_HIT_RW          | Level 1 GCS cache demand access line-fill buffer hit.                                                    |
| 0x833D   | L1GCS_LFB_HIT_RW_FHWPRF   | Level 1 GCS cache demand access line-fill buffer first hit, recently fetched by GCS hardware prefetcher. |
| 0x833E   | L1GCS_CACHE_INVAL         | Level 1 GCS cache invalidate.                                                                            |
| 0x8340   | L1GCS_TLB                 | Level 1 GCS TLB access.                                                                                  |
| 0x8341   | L1GCS_TLB_RW              | Level 1 GCS demand TLB access.                                                                           |
| 0x8342   | L1GCS_TLB_HWPRF           | Level 1 GCS demand TLB access, GCS hardware prefetch.                                                    |
| 0x8344   | GCSTLB_WALK               | GCS TLB access with at least one translation table walk.                                                 |
| 0x8345   | GCSTLB_WALK_RW            | GCS TLB demand access with at least one translation table walk.                                          |
| 0x8346   | GCSTLB_WALK_PERCYC        | Translation table walks in progress.                                                                     |
| 0x8347   | GCSTLB_WALK_STEP          | GCS TLB translation table walk, step.                                                                    |
| 0x8348   | SAMPLE_FEED_FP            | Statistical Profiling sample taken, floating-point.                                                      |

| Number   | Mnemonic              | Description                                                                                                |
|----------|-----------------------|------------------------------------------------------------------------------------------------------------|
| 0x8349   | SAMPLE_FEED_SIMD      | Statistical Profiling sample taken, SIMD.                                                                  |
| 0x8350   | STALL_BACKEND_L1GCS   | Backend stall cycles, Level 1 GCS cache.                                                                   |
| 0x8351   | STALL_BACKEND_GCSTLB  | Backend stall cycles, GCS TLB.                                                                             |
| 0x8352   | SME_FP_SPEC           | Operation speculatively executed, SMEfloating-point, data-processing.                                      |
| 0x8353   | SE_FP_SPEC            | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD floating-point, data-processing.          |
| 0x8354   | SVE_CMP_IGRANULE_SPEC | Operation speculatively executed, SVE in-granule compare.                                                  |
| 0x8355   | SVE_CMP_XGRANULE_SPEC | Operation speculatively executed, SVE cross-granule compare.                                               |
| 0x8356   | SVE_BITPERM_SPEC      | Operation speculatively executed, SVE in-element permute.                                                  |
| 0x8358   | SME_RETIRED           | Instruction architecturally executed, SMEdata processing.                                                  |
| 0x8359   | SE_RETIRED            | Instruction architecturally executed, Advanced SIMD, SVE, or SMEdata processing.                           |
| 0x835A   | SME_INST_RETIRED      | Instruction architecturally executed, SME.                                                                 |
| 0x835B   | SE_INST_RETIRED       | Instruction architecturally executed, Advanced SIMD, SVE, or SME.                                          |
| 0x835C   | SME_SPEC              | Operation speculatively executed, SMEdata processing.                                                      |
| 0x835D   | SE_SPEC               | Operation speculatively executed, Advanced SIMD, SVE, or SMEdata processing.                               |
| 0x835E   | SME_INST_SPEC         | Operation speculatively executed, SME.                                                                     |
| 0x835F   | SE_INST_SPEC          | Operation speculatively executed, Advanced SIMD, SVE, or SME.                                              |
| 0x8360   | SME_INT8_SPEC         | Operation speculatively executed, SME8-bit integer, data-processing.                                       |
| 0x8361   | SE_INT8_SPEC          | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD 8-bit integer, data-processing.           |
| 0x8362   | SME_FP_BF16_SPEC      | Operation speculatively executed, SMEBFloat16 floating-point, data-processing.                             |
| 0x8363   | SE_FP_BF16_SPEC       | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD BFloat16 floating-point, data-processing. |
| 0x8364   | SME_INT16_SPEC        | Operation speculatively executed, SME16-bit integer, data-processing.                                      |

| Number   | Mnemonic           | Description                                                                                                        |
|----------|--------------------|--------------------------------------------------------------------------------------------------------------------|
| 0x8365   | SE_INT16_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD 16-bit integer, data-processing.                  |
| 0x8366   | SME_FP_HP_SPEC     | Operation speculatively executed, SMEhalf-precision floating-point, data-processing.                               |
| 0x8367   | SE_FP_HP_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD half-precision floating-point, data-processing.   |
| 0x8368   | SME_INT32_SPEC     | Operation speculatively executed, SME32-bit integer, data-processing.                                              |
| 0x8369   | SE_INT32_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD 32-bit integer, data-processing.                  |
| 0x836A   | SME_FP_SP_SPEC     | Operation speculatively executed, SMEsingle-precision floating-point, data-processing.                             |
| 0x836B   | SE_FP_SP_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD single-precision floating-point, data-processing. |
| 0x836C   | SME_INT64_SPEC     | Operation speculatively executed, SME64-bit integer, data-processing.                                              |
| 0x836D   | SE_INT64_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD 64-bit integer, data-processing.                  |
| 0x836E   | SME_FP_DP_SPEC     | Operation speculatively executed, SMEdouble-precision floating-point, data-processing.                             |
| 0x836F   | SE_FP_DP_SPEC      | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD double-precision floating-point, data-processing. |
| 0x8370   | SME_FP_ADDSUB_SPEC | Operation speculatively executed, SMEfloating-point addition or subtraction.                                       |
| 0x8371   | SE_FP_ADDSUB_SPEC  | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD floating-point addition or subtraction.           |
| 0x8372   | SME_FP_FMA_SPEC    | Operation speculatively executed, SMEfloating-point multiply-add or multiply-subtract.                             |
| 0x8373   | SE_FP_FMA_SPEC     | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD floating-point multiply-add or multiply-subtract. |
| 0x8374   | SME_FP_DOT_SPEC    | Operation speculatively executed, SMEfloating-point dot product.                                                   |

| Number   | Mnemonic                | Description                                                                                                      |
|----------|-------------------------|------------------------------------------------------------------------------------------------------------------|
| 0x8375   | SE_FP_DOT_SPEC          | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD floating-point dot product.                     |
| 0x8376   | SME_FP_MOPA_SPEC        | Operation speculatively executed, SMEfloating-point outer product and accumulate, or outer product and subtract. |
| 0x8378   | SME_INT_SPEC            | Operation speculatively executed, SMEinteger, data-processing.                                                   |
| 0x8379   | SE_INT_SPEC             | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD integer, data-processing.                       |
| 0x837A   | SME_INT_MUL_SPEC        | Operation speculatively executed, SMEinteger multiply or multiply-accumulate.                                    |
| 0x837B   | SE_INT_MUL_SPEC         | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD integer multiply or multiply-accumulate.        |
| 0x837C   | SME_INT_DOT_SPEC        | Operation speculatively executed, SMEinteger dot product.                                                        |
| 0x837D   | SE_INT_DOT_SPEC         | Operation speculatively executed, Advanced SIMD, SVE, orSME SIMD integer dot product.                            |
| 0x837E   | SME_INT_MOPA_SPEC       | Operation speculatively executed, SMEinteger outer product and accumulate, or outer product and subtract.        |
| 0x8380   | ZA_ACTIVE               | CPU cycles, ZAenabled.                                                                                           |
| 0x8381   | SME_PRED2_NOT_FULL_SPEC | Operation speculatively executed, SME2Dpredicated with at least one inactive element.                            |
| 0x8384   | SME_PRED2_SPEC          | Operation speculatively executed, SME2Dpredicated.                                                               |
| 0x8385   | SME_PRED2_EMPTY_SPEC    | Operation speculatively executed, SME2Dpredicated with no active elements.                                       |
| 0x8386   | SME_PRED2_FULL_SPEC     | Operation speculatively executed, SME2Dpredicated with all active elements.                                      |
| 0x8387   | SME_PRED2_PARTIAL_SPEC  | Operation speculatively executed, SME2Dpredicated with partially active elements.                                |
| 0x8388   | SME_LDST_ZAREG_SPEC     | SMEZAunpredicated load/store.                                                                                    |
| 0x8389   | SME_LD_ZAREG_SPEC       | SMEZAunpredicated load.                                                                                          |
| 0x838A   | SME_ST_ZAREG_SPEC       | SMEZAunpredicated store.                                                                                         |
| 0x838C   | SME_LDST_ZTREG_SPEC     | SMEZTunpredicated load/store.                                                                                    |
| 0x838D   | SME_LD_ZTREG_SPEC       | SMEZTunpredicated load.                                                                                          |
| 0x838E   | SME_ST_ZTREG_SPEC       | SMEZTunpredicated store.                                                                                         |
| 0x8390   | SME_LDST_REG_SPEC       | SMEunpredicated load/store.                                                                                      |

| Number   | Mnemonic           | Description                                                                               |
|----------|--------------------|-------------------------------------------------------------------------------------------|
| 0x8391   | SME_LD_REG_SPEC    | SMEunpredicated load.                                                                     |
| 0x8392   | SME_ST_REG_SPEC    | SMEunpredicated store.                                                                    |
| 0x8394   | SME_LDST_TILE_SPEC | SMEpredicated tile load/store.                                                            |
| 0x8395   | SME_LD_TILE_SPEC   | SMEpredicated tile load.                                                                  |
| 0x8396   | SME_ST_TILE_SPEC   | SMEpredicated tile store.                                                                 |
| 0x8398   | ASE_LUT_SPEC       | Lookup table operation speculatively executed, Advanced SIMD data processing.             |
| 0x8399   | SVE_LUT_SPEC       | Lookup table operation speculatively executed, SVE data processing.                       |
| 0x839A   | SME_LUT_SPEC       | Lookup table operation speculatively executed, SMEdata processing.                        |
| 0x839B   | SE_LUT_SPEC        | Lookup table operation speculatively executed, Advanced SIMD, SVE, or SMEdata processing. |
| 0x83A0   | N1_CACHE_HIT_RD    | Cache at distance 1, demand access hit, read.                                             |
| 0x83A1   | N2_CACHE_HIT_RD    | Cache at distance 2, demand access hit, read.                                             |
| 0x83A2   | N3_CACHE_HIT_RD    | Cache at distance 3, demand access hit, read.                                             |
| 0x83A3   | N4_CACHE_HIT_RD    | Cache at distance 4, demand access hit, read.                                             |
| 0x83A4   | N1_CACHE_HIT_PRFM  | Cache at distance 1, software prefetch hit.                                               |
| 0x83A5   | N2_CACHE_HIT_PRFM  | Cache at distance 2, software prefetch hit.                                               |
| 0x83A6   | N3_CACHE_HIT_PRFM  | Cache at distance 3, software prefetch hit.                                               |
| 0x83A7   | N4_CACHE_HIT_PRFM  | Cache at distance 4, software prefetch hit.                                               |
| 0x83A8   | N1_CACHE1_HIT_RD   | Cache type 1 at distance 1 demand access hit, read.                                       |
| 0x83A9   | N2_CACHE1_HIT_RD   | Cache type 1 at distance 2 demand access hit, read.                                       |
| 0x83AA   | N3_CACHE1_HIT_RD   | Cache type 1 at distance 3 demand access hit, read.                                       |
| 0x83AB   | N4_CACHE1_HIT_RD   | Cache type 1 at distance 4 demand access hit, read.                                       |
| 0x83AC   | N1_CACHE1_HIT_PRFM | Cache type 1 at distance 1 software prefetch hit.                                         |
| 0x83AD   | N2_CACHE1_HIT_PRFM | Cache type 1 at distance 2 software prefetch hit.                                         |
| 0x83AE   | N3_CACHE1_HIT_PRFM | Cache type 1 at distance 3 software prefetch hit.                                         |
| 0x83AF   | N4_CACHE1_HIT_PRFM | Cache type 1 at distance 4 software prefetch hit.                                         |

| Number   | Mnemonic           | Description                                                   |
|----------|--------------------|---------------------------------------------------------------|
| 0x83B0   | N1_CACHE2_HIT_RD   | Cache type 2 at distance 1 demand access hit, read.           |
| 0x83B1   | N2_CACHE2_HIT_RD   | Cache type 2 at distance 2 demand access hit, read.           |
| 0x83B2   | N3_CACHE2_HIT_RD   | Cache type 2 at distance 3 demand access hit, read.           |
| 0x83B3   | N4_CACHE2_HIT_RD   | Cache type 2 at distance 4 demand access hit, read.           |
| 0x83B4   | N1_CACHE2_HIT_PRFM | Cache type 2 at distance 1 software prefetch hit.             |
| 0x83B5   | N2_CACHE2_HIT_PRFM | Cache type 2 at distance 2 software prefetch hit.             |
| 0x83B6   | N3_CACHE2_HIT_PRFM | Cache type 2 at distance 3 software prefetch hit.             |
| 0x83B7   | N4_CACHE2_HIT_PRFM | Cache type 2 at distance 4 software prefetch hit.             |
| 0x83B8   | N1_CACHE3_HIT_RD   | Cache type 3 at distance 1 demand access hit, read.           |
| 0x83B9   | N2_CACHE3_HIT_RD   | Cache type 3 at distance 2 demand access hit, read.           |
| 0x83BA   | N3_CACHE3_HIT_RD   | Cache type 3 at distance 3 demand access hit, read.           |
| 0x83BB   | N4_CACHE3_HIT_RD   | Cache type 3 at distance 4 demand access hit, read.           |
| 0x83BC   | N1_CACHE3_HIT_PRFM | Cache type 3 at distance 1 software prefetch hit.             |
| 0x83BD   | N2_CACHE3_HIT_PRFM | Cache type 3 at distance 2 software prefetch hit.             |
| 0x83BE   | N3_CACHE3_HIT_PRFM | Cache type 3 at distance 3 software prefetch hit.             |
| 0x83BF   | N4_CACHE3_HIT_PRFM | Cache type 3 at distance 4 software prefetch hit.             |
| 0x83C0   | N1_CACHE_HITM_RD   | Cache at distance 1, demand access hit modified, read.        |
| 0x83C1   | N2_CACHE_HITM_RD   | Cache at distance 2, demand access hit modified, read.        |
| 0x83C2   | N3_CACHE_HITM_RD   | Cache at distance 3, demand access hit modified, read.        |
| 0x83C3   | N4_CACHE_HITM_RD   | Cache at distance 4, demand access hit modified, read.        |
| 0x83C4   | N1_LFB_HIT_RD      | Cache at distance 1 demand access line-fill buffer hit, read. |
| 0x83C5   | N2_LFB_HIT_RD      | Cache at distance 2 demand access line-fill buffer hit, read. |
| 0x83C6   | N3_LFB_HIT_RD      | Cache at distance 3 demand access line-fill buffer hit, read. |
| 0x83C7   | N4_LFB_HIT_RD      | Cache at distance 4 demand access line-fill buffer hit, read. |

| Number   | Mnemonic          | Description                                                          |
|----------|-------------------|----------------------------------------------------------------------|
| 0x83C8   | N1_CACHE1_HITM_RD | Cache type 1 at distance 1 demand access hit modified, read.         |
| 0x83C9   | N2_CACHE1_HITM_RD | Cache type 1 at distance 2 demand access hit modified, read.         |
| 0x83CA   | N3_CACHE1_HITM_RD | Cache type 1 at distance 3 demand access hit modified, read.         |
| 0x83CB   | N4_CACHE1_HITM_RD | Cache type 1 at distance 4 demand access hit modified, read.         |
| 0x83CC   | N1_LFB1_HIT_RD    | Cache type 1 at distance 1 demand access line-fill buffer hit, read. |
| 0x83CD   | N2_LFB1_HIT_RD    | Cache type 1 at distance 2 demand access line-fill buffer hit, read. |
| 0x83CE   | N3_LFB1_HIT_RD    | Cache type 1 at distance 3 demand access line-fill buffer hit, read. |
| 0x83CF   | N4_LFB1_HIT_RD    | Cache type 1 at distance 4 demand access line-fill buffer hit, read. |
| 0x83D0   | N1_CACHE2_HITM_RD | Cache type 2 at distance 1 demand access hit modified, read.         |
| 0x83D1   | N2_CACHE2_HITM_RD | Cache type 2 at distance 2 demand access hit modified, read.         |
| 0x83D2   | N3_CACHE2_HITM_RD | Cache type 2 at distance 3 demand access hit modified, read.         |
| 0x83D3   | N4_CACHE2_HITM_RD | Cache type 2 at distance 4 demand access hit modified, read.         |
| 0x83D4   | N1_LFB2_HIT_RD    | Cache type 2 at distance 1 demand access line-fill buffer hit, read. |
| 0x83D5   | N2_LFB2_HIT_RD    | Cache type 2 at distance 2 demand access line-fill buffer hit, read. |
| 0x83D6   | N3_LFB2_HIT_RD    | Cache type 2 at distance 3 demand access line-fill buffer hit, read. |
| 0x83D7   | N4_LFB2_HIT_RD    | Cache type 2 at distance 4 demand access line-fill buffer hit, read. |
| 0x83D8   | N1_CACHE3_HITM_RD | Cache type 3 at distance 1 demand access hit modified, read.         |
| 0x83D9   | N2_CACHE3_HITM_RD | Cache type 3 at distance 2 demand access hit modified, read.         |
| 0x83DA   | N3_CACHE3_HITM_RD | Cache type 3 at distance 3 demand access hit modified, read.         |
| 0x83DB   | N4_CACHE3_HITM_RD | Cache type 3 at distance 4 demand access hit modified, read.         |
| 0x83DC   | N1_LFB3_HIT_RD    | Cache type 3 at distance 1 demand access line-fill buffer hit, read. |
| 0x83DD   | N2_LFB3_HIT_RD    | Cache type 3 at distance 2 demand access line-fill buffer hit, read. |
| 0x83DE   | N3_LFB3_HIT_RD    | Cache type 3 at distance 3 demand access line-fill buffer hit, read. |
| 0x83DF   | N4_LFB3_HIT_RD    | Cache type 3 at distance 4 demand access line-fill buffer hit, read. |

| Number   | Mnemonic     | Description                                                 |
|----------|--------------|-------------------------------------------------------------|
| 0x83E0   | N1_MEM_RD    | Access to memory at distance 1, demand access, read.        |
| 0x83E1   | N2_MEM_RD    | Access to memory at distance 2, demand access, read.        |
| 0x83E2   | N3_MEM_RD    | Access to memory at distance 3, demand access, read.        |
| 0x83E3   | N4_MEM_RD    | Access to memory at distance 4, demand access, read.        |
| 0x83E4   | N1_MEM_PRFM  | Access to memory at distance 1, software prefetch.          |
| 0x83E5   | N2_MEM_PRFM  | Access to memory at distance 2, software prefetch.          |
| 0x83E6   | N3_MEM_PRFM  | Access to memory at distance 3, software prefetch.          |
| 0x83E7   | N4_MEM_PRFM  | Access to memory at distance 4, software prefetch.          |
| 0x83E8   | N1_MEM1_RD   | Access to type 1 memory at distance 1, demand access, read. |
| 0x83E9   | N2_MEM1_RD   | Access to type 1 memory at distance 2, demand access, read. |
| 0x83EA   | N3_MEM1_RD   | Access to type 1 memory at distance 3, demand access, read. |
| 0x83EB   | N4_MEM1_RD   | Access to type 1 memory at distance 4, demand access, read. |
| 0x83EC   | N1_MEM1_PRFM | Access to type 1 memory at distance 1, software prefetch.   |
| 0x83ED   | N2_MEM1_PRFM | Access to type 1 memory at distance 2, software prefetch.   |
| 0x83EE   | N3_MEM1_PRFM | Access to type 1 memory at distance 3, software prefetch.   |
| 0x83EF   | N4_MEM1_PRFM | Access to type 1 memory at distance 4, software prefetch.   |
| 0x83F0   | N1_MEM2_RD   | Access to type 2 memory at distance 1, demand access, read. |
| 0x83F1   | N2_MEM2_RD   | Access to type 2 memory at distance 2, demand access, read. |
| 0x83F2   | N3_MEM2_RD   | Access to type 2 memory at distance 3, demand access, read. |
| 0x83F3   | N4_MEM2_RD   | Access to type 2 memory at distance 4, demand access, read. |
| 0x83F4   | N1_MEM2_PRFM | Access to type 2 memory at distance 1, software prefetch.   |
| 0x83F5   | N2_MEM2_PRFM | Access to type 2 memory at distance 2, software prefetch.   |
| 0x83F6   | N3_MEM2_PRFM | Access to type 2 memory at distance 3, software prefetch.   |
| 0x83F7   | N4_MEM2_PRFM | Access to type 2 memory at distance 4, software prefetch.   |

| Number   | Mnemonic       | Description                                                 |
|----------|----------------|-------------------------------------------------------------|
| 0x83F8   | N1_MEM3_RD     | Access to type 3 memory at distance 1, demand access, read. |
| 0x83F9   | N2_MEM3_RD     | Access to type 3 memory at distance 2, demand access, read. |
| 0x83FA   | N3_MEM3_RD     | Access to type 3 memory at distance 3, demand access, read. |
| 0x83FB   | N4_MEM3_RD     | Access to type 3 memory at distance 4, demand access, read. |
| 0x83FC   | N1_MEM3_PRFM   | Access to type 3 memory at distance 1, software prefetch.   |
| 0x83FD   | N2_MEM3_PRFM   | Access to type 3 memory at distance 2, software prefetch.   |
| 0x83FE   | N3_MEM3_PRFM   | Access to type 3 memory at distance 3, software prefetch.   |
| 0x83FF   | N4_MEM3_PRFM   | Access to type 3 memory at distance 4, software prefetch.   |
| 0x8400   | ISNP_HIT_N1_RD | Snoop hit in cache at distance 1, demand instruction fetch. |
| 0x8401   | ISNP_HIT_N2_RD | Snoop hit in cache at distance 2, demand instruction fetch. |
| 0x8402   | ISNP_HIT_N3_RD | Snoop hit in cache at distance 3, demand instruction fetch. |
| 0x8403   | ISNP_HIT_N4_RD | Snoop hit in cache at distance 4, demand instruction fetch. |
| 0x8404   | DSNP_HIT_N1_RD | Snoop hit in cache at distance 1, demand data read.         |
| 0x8405   | DSNP_HIT_N2_RD | Snoop hit in cache at distance 2, demand data read.         |
| 0x8406   | DSNP_HIT_N3_RD | Snoop hit in cache at distance 3, demand data read.         |
| 0x8407   | DSNP_HIT_N4_RD | Snoop hit in cache at distance 4, demand data read.         |
| 0x8408   | DSNP_HIT_N1_WR | Snoop hit in cache at distance 1, demand data write.        |
| 0x8409   | DSNP_HIT_N2_WR | Snoop hit in cache at distance 2, demand data write.        |
| 0x840A   | DSNP_HIT_N3_WR | Snoop hit in cache at distance 3, demand data write.        |
| 0x840B   | DSNP_HIT_N4_WR | Snoop hit in cache at distance 4, demand data write.        |
| 0x840C   | DSNP_HIT_N1_RW | Snoop hit in cache at distance 1, demand data access.       |
| 0x840D   | DSNP_HIT_N2_RW | Snoop hit in cache at distance 2, demand data access.       |
| 0x840E   | DSNP_HIT_N3_RW | Snoop hit in cache at distance 3, demand data access.       |
| 0x840F   | DSNP_HIT_N4_RW | Snoop hit in cache at distance 4, demand data access.       |

| Number   | Mnemonic          | Description                                                      |
|----------|-------------------|------------------------------------------------------------------|
| 0x8410   | DSNP_HIT_N1_PRFM  | Snoop hit in cache at distance 1, software data prefetch.        |
| 0x8411   | DSNP_HIT_N2_PRFM  | Snoop hit in cache at distance 2, software data prefetch.        |
| 0x8412   | DSNP_HIT_N3_PRFM  | Snoop hit in cache at distance 3, software data prefetch.        |
| 0x8413   | DSNP_HIT_N4_PRFM  | Snoop hit in cache at distance 4, software data prefetch.        |
| 0x8414   | DSNP_HIT_N1_HWPRF | Snoop hit in cache at distance 1, hardware data prefetch.        |
| 0x8415   | DSNP_HIT_N2_HWPRF | Snoop hit in cache at distance 2, hardware data prefetch.        |
| 0x8416   | DSNP_HIT_N3_HWPRF | Snoop hit in cache at distance 3, hardware data prefetch.        |
| 0x8417   | DSNP_HIT_N4_HWPRF | Snoop hit in cache at distance 4, hardware data prefetch.        |
| 0x8418   | ISNP_HIT_N1_PRFM  | Snoop hit in cache at distance 1, software instruction prefetch. |
| 0x8419   | ISNP_HIT_N2_PRFM  | Snoop hit in cache at distance 2, software instruction prefetch. |
| 0x841A   | ISNP_HIT_N3_PRFM  | Snoop hit in cache at distance 3, software instruction prefetch. |
| 0x841B   | ISNP_HIT_N4_PRFM  | Snoop hit in cache at distance 4, software instruction prefetch. |
| 0x841C   | ISNP_HIT_N1_HWPRF | Snoop hit in cache at distance 1, hardware instruction prefetch. |
| 0x841D   | ISNP_HIT_N2_HWPRF | Snoop hit in cache at distance 2, hardware instruction prefetch. |
| 0x841E   | ISNP_HIT_N3_HWPRF | Snoop hit in cache at distance 3, hardware instruction prefetch. |
| 0x841F   | ISNP_HIT_N4_HWPRF | Snoop hit in cache at distance 4, hardware instruction prefetch. |
| 0x8420   | DSNP_HIT_N1_PRF   | Snoop hit in cache at distance 1, data prefetch.                 |
| 0x8421   | DSNP_HIT_N2_PRF   | Snoop hit in cache at distance 2, data prefetch.                 |
| 0x8422   | DSNP_HIT_N3_PRF   | Snoop hit in cache at distance 3, data prefetch.                 |
| 0x8423   | DSNP_HIT_N4_PRF   | Snoop hit in cache at distance 4, data prefetch.                 |
| 0x8424   | ISNP_HIT_N1_PRF   | Snoop hit in cache at distance 1, instruction prefetch.          |
| 0x8425   | ISNP_HIT_N2_PRF   | Snoop hit in cache at distance 2, instruction prefetch.          |
| 0x8426   | ISNP_HIT_N3_PRF   | Snoop hit in cache at distance 3, instruction prefetch.          |
| 0x8427   | ISNP_HIT_N4_PRF   | Snoop hit in cache at distance 4, instruction prefetch.          |

| Number   | Mnemonic            | Description                                                                                     |
|----------|---------------------|-------------------------------------------------------------------------------------------------|
| 0x8428   | ISNP_HIT_N1         | Snoop hit in cache at distance 1, instruction access.                                           |
| 0x8429   | ISNP_HIT_N2         | Snoop hit in cache at distance 2, instruction access.                                           |
| 0x842A   | ISNP_HIT_N3         | Snoop hit in cache at distance 3, instruction access.                                           |
| 0x842B   | ISNP_HIT_N4         | Snoop hit in cache at distance 4, instruction access.                                           |
| 0x842C   | DSNP_HIT_N1         | Snoop hit in cache at distance 1, data access.                                                  |
| 0x842D   | DSNP_HIT_N2         | Snoop hit in cache at distance 2, data access.                                                  |
| 0x842E   | DSNP_HIT_N3         | Snoop hit in cache at distance 3, data access.                                                  |
| 0x842F   | DSNP_HIT_N4         | Snoop hit in cache at distance 4, data access.                                                  |
| 0x8431   | ASE_FP_VREDUCE_SPEC | Floating-point operation speculatively executed, Advanced SIMD pairwise or reduction.           |
| 0x8432   | SVE_FP_PREDUCE_SPEC | Floating-point operation speculatively executed, SVE pairwise add step or pairwise reduce step. |
| 0x8434   | DSNP_HITM_N1_RD     | Snoop hit in cache at distance 1, demand data read, modified.                                   |
| 0x8435   | DSNP_HITM_N2_RD     | Snoop hit in cache at distance 2, demand data read, modified.                                   |
| 0x8436   | DSNP_HITM_N3_RD     | Snoop hit in cache at distance 3, demand data read, modified.                                   |
| 0x8437   | DSNP_HITM_N4_RD     | Snoop hit in cache at distance 4, demand data read, modified.                                   |
| 0x8438   | DSNP_HITM_N1_WR     | Snoop hit in cache at distance 1, demand data write, modified.                                  |
| 0x8439   | DSNP_HITM_N2_WR     | Snoop hit in cache at distance 2, demand data write, modified.                                  |
| 0x843A   | DSNP_HITM_N3_WR     | Snoop hit in cache at distance 3, demand data write, modified.                                  |
| 0x843B   | DSNP_HITM_N4_WR     | Snoop hit in cache at distance 4, demand data write, modified.                                  |
| 0x843C   | DSNP_HITM_N1_RW     | Snoop hit in cache at distance 1, demand data access, modified.                                 |
| 0x843D   | DSNP_HITM_N2_RW     | Snoop hit in cache at distance 2, demand data access, modified.                                 |
| 0x843E   | DSNP_HITM_N3_RW     | Snoop hit in cache at distance 3, demand data access, modified.                                 |
| 0x843F   | DSNP_HITM_N4_RW     | Snoop hit in cache at distance 4, demand data access, modified.                                 |

| Number   | Mnemonic                 | Description                                                                                                                              |
|----------|--------------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| 0x8440   | ASE_FP_SP_MIN_SPEC       | Advanced SIMD data processing operation speculatively executed, smallest type is single-precision floating-point.                        |
| 0x8442   | ASE_FP_HP_MIN_SPEC       | Advanced SIMD data processing operation speculatively executed, smallest type is half-precision floating-point.                          |
| 0x8443   | ASE_FP_BF16_MIN_SPEC     | Advanced SIMD data processing operation speculatively executed, smallest type is BFloat16 floating-point.                                |
| 0x8444   | ASE_FP_FP8_MIN_SPEC      | Advanced SIMD data processing operation speculatively executed, smallest type is 8-bit floating-point.                                   |
| 0x8448   | ASE_SVE_FP_SP_MIN_SPEC   | Advanced SIMD data processing or SVE data processing operation speculatively executed, smallest type is single-precision floating-point. |
| 0x844A   | ASE_SVE_FP_HP_MIN_SPEC   | Advanced SIMD data processing or SVE data processing operation speculatively executed, smallest type is half-precision floating-point.   |
| 0x844B   | ASE_SVE_FP_BF16_MIN_SPEC | Advanced SIMD data processing or SVE data processing operation speculatively executed, smallest type is BFloat16 floating-point.         |
| 0x844C   | ASE_SVE_FP_FP8_MIN_SPEC  | Advanced SIMD data processing or SVE data processing operation speculatively executed, smallest type is 8-bit floating-point.            |
| 0x8450   | SE_FP_SP_MIN_SPEC        | Advanced SIMD, SVE, or SMEdata processing operation speculatively executed, smallest type is single-precision floating-point.            |
| 0x8452   | SE_FP_HP_MIN_SPEC        | Advanced SIMD, SVE, or SMEdata processing operation speculatively executed, smallest type is half-precision floating-point.              |
| 0x8453   | SE_FP_BF16_MIN_SPEC      | Advanced SIMD, SVE, or SMEdata processing operation speculatively executed, smallest type is BFloat16 floating-point.                    |
| 0x8454   | SE_FP_FP8_MIN_SPEC       | Advanced SIMD, SVE, or SMEdata processing operation speculatively executed, smallest type is 8-bit floating-point.                       |
| 0x8458   | SME_FP_SP_MIN_SPEC       | SMEdata processing operation speculatively executed, smallest type is single-precision floating-point.                                   |
| 0x845A   | SME_FP_HP_MIN_SPEC       | SMEdata processing operation speculatively executed, smallest type is half-precision floating-point.                                     |

| Number   | Mnemonic                   | Description                                                                                                          |
|----------|----------------------------|----------------------------------------------------------------------------------------------------------------------|
| 0x845B   | SME_FP_BF16_MIN_SPEC       | SMEdata processing operation speculatively executed, smallest type is BFloat16 floating-point.                       |
| 0x845C   | SME_FP_FP8_MIN_SPEC        | SMEdata processing operation speculatively executed, smallest type is 8-bit floating-point.                          |
| 0x8460   | SVE_FP_SP_MIN_SPEC         | SVE data processing operation speculatively executed, smallest type is single-precision floating-point.              |
| 0x8462   | SVE_FP_HP_MIN_SPEC         | SVE data processing operation speculatively executed, smallest type is half-precision floating-point.                |
| 0x8463   | SVE_FP_BF16_MIN_SPEC       | SVE data processing operation speculatively executed, smallest type is BFloat16 floating-point.                      |
| 0x8464   | SVE_FP_FP8_MIN_SPEC        | SVE data processing operation speculatively executed, smallest type is 8-bit floating-point.                         |
| 0x846B   | FP_BF16_FIXED_OPS_SPEC     | Non-scalable element arithmetic operations speculatively executed, largest type is BFloat16 floating-point.          |
| 0x8470   | FP_SP_MIN_SPEC             | Floating-point operation speculatively executed, smallest type is single-precision floating-point.                   |
| 0x8472   | FP_HP_MIN_SPEC             | Floating-point operation speculatively executed, smallest type is half-precision floating-point.                     |
| 0x8473   | FP_BF16_MIN_SPEC           | Floating-point operation speculatively executed, smallest type is BFloat16 floating-point.                           |
| 0x8474   | FP_FP8_MIN_SPEC            | Floating-point operation speculatively executed, smallest type is 8-bit floating-point.                              |
| 0x8480   | FP_SP_FIXED_MIN_OPS_SPEC   | Non-scalable element arithmetic operations speculatively executed, smallest type is single-precision floating-point. |
| 0x8482   | FP_HP_FIXED_MIN_OPS_SPEC   | Non-scalable element arithmetic operations speculatively executed, smallest type is half-precision floating-point.   |
| 0x8483   | FP_BF16_FIXED_MIN_OPS_SPEC | Non-scalable element arithmetic operations speculatively executed, smallest type is BFloat16 floating-point.         |
| 0x8484   | FP_FP8_FIXED_MIN_OPS_SPEC  | Non-scalable element arithmetic operations speculatively executed, smallest type is 8-bit floating-point.            |
| 0x8488   | FP_SP_SCALE_MIN_OPS_SPEC   | Scalable element arithmetic operations speculatively executed, smallest type is single-precision floating-point.     |

| Number   | Mnemonic                    | Description                                                                                                    |
|----------|-----------------------------|----------------------------------------------------------------------------------------------------------------|
| 0x848A   | FP_HP_SCALE_MIN_OPS_SPEC    | Scalable element arithmetic operations speculatively executed, smallest type is half-precision floating-point. |
| 0x848B   | FP_BF16_SCALE_MIN_OPS_SPEC  | Scalable element arithmetic operations speculatively executed, smallest type is BFloat16 floating-point.       |
| 0x848C   | FP_FP8_SCALE_MIN_OPS_SPEC   | Scalable element arithmetic operations speculatively executed, smallest type is 8-bit floating-point.          |
| 0x8490   | FP_SP_SCALE2_MIN_OPS_SPEC   | Scalable tile arithmetic operations speculatively executed, smallest type is single-precision floating-point.  |
| 0x8492   | FP_HP_SCALE2_MIN_OPS_SPEC   | Scalable tile arithmetic operations speculatively executed, smallest type is half-precision floating-point.    |
| 0x8493   | FP_BF16_SCALE2_MIN_OPS_SPEC | Scalable tile arithmetic operations speculatively executed, smallest type is BFloat16 floating-point.          |
| 0x8494   | FP_FP8_SCALE2_MIN_OPS_SPEC  | Scalable tile arithmetic operations speculatively executed, smallest type is 8-bit floating-point.             |