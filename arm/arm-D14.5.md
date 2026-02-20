## D14.5 Meaningful combinations of common events

The architecture highlights some meaningful combinations of common events. The following tables list the highlighted combinations:

- Refill events and associated access events.
- Latency events.
- Cache hit events and associated data source events.
- Cache line state tracking events.
- TLB events.
- At-retirement events.
- Speculatively executed operation events.
- Bytes loaded and stored events.
- Overall vector utilization events.
- Vector loop efficiency events.

## D14.5.1 Refill events and associated access events

IGSMLS

The following are meaningful combinations of refill events and associated access events:

## Table D14-4 Meaningful combinations of refill events and associated access events

| Numerator                  | Denominator          | Ratio                                                                 |
|----------------------------|----------------------|-----------------------------------------------------------------------|
| 0x0001 L1I_CACHE_REFILL    | 0x0014 L1I_CACHE     | Attributable Level 1 instruction cache refill rate                    |
| 0x0002 L1I_TLB_REFILL      | 0x0026 L1I_TLB       | Attributable Level 1 instruction TLB refill rate                      |
| 0x0003 L1D_CACHE_REFILL    | 0x0004 L1D_CACHE     | Attributable Level 1 data or unified cache refill rate                |
| 0x0005 L1D_TLB_REFILL      | 0x0025 L1D_TLB       | Attributable Level 1 data or unified TLB refill rate                  |
| 0x0017 L2D_CACHE_REFILL    | 0x0016 L2D_CACHE     | Attributable Level 2 data or unified cache refill rate                |
| 0x0028 L2I_CACHE_REFILL    | 0x0027 L2I_CACHE     | Attributable Level 2 instruction cache refill rate                    |
| 0x002A L3D_CACHE_REFILL    | 0x002B L3D_CACHE     | Attributable Level 3 data or unified cache refill rate                |
| 0x002D L2D_TLB_REFILL      | 0x002F L2D_TLB       | Attributable Level 2 data or unified TLB refill rate                  |
| 0x002E L2I_TLB_REFILL      | 0x0030 L2I_TLB       | Attributable Level 2 instruction TLB refill rate                      |
| 0x0019 BUS_ACCESS          | 0x001D BUS_CYCLES    | Attributable Bus accesses per cycle                                   |
| 0x0033 LL_CACHE_MISS       | 0x0032 LL_CACHE      | Attributable Last Level data or unified cache refill rate             |
| 0x0034 DTLB_WALK           | 0x0025 L1D_TLB       | Attributable data TLB miss rate                                       |
| 0x0035 ITLB_WALK           | 0x0026 L1I_TLB       | Attributable instruction TLB miss rate                                |
| 0x0037 LL_CACHE_MISS_RD    | 0x0036 LL_CACHE_RD   | Attributable memory read operation miss rate                          |
| 0x0038 REMOTE_ACCESS_RD    | 0x0031 REMOTE_ACCESS | Attributable read accesses to another socket in a multi-socket system |
| 0x0042 L1D_CACHE_REFILL_RD | 0x0040 L1D_CACHE_RD  | Attributable Level 1 cache refill rate, read                          |
| 0x0043 L1D_CACHE_REFILL_WR | 0x0041 L1D_CACHE_WR  | Attributable Level 1 cache refill rate, write                         |
| 0x004C L1D_TLB_REFILL_RD   | 0x004E L1D_TLB_RD    | Attributable Level 1 TLB refill rate, read                            |
| 0x004D L1D_TLB_REFILL_WR   | 0x004F L1D_TLB_WR    | Attributable Level 1 TLB refill rate, write                           |

| Numerator                  | Denominator         | Ratio                                              |
|----------------------------|---------------------|----------------------------------------------------|
| 0x0052 L2D_CACHE_REFILL_RD | 0x0050 L2D_CACHE_RD | Attributable Level 2 data cache refill rate, read  |
| 0x0053 L2D_CACHE_REFILL_WR | 0x0051 L2D_CACHE_WR | Attributable Level 2 data cache refill rate, write |
| 0x005C L2D_TLB_REFILL_RD   | 0x005E L2D_TLB_RD   | Attributable Level 2 data TLB refill rate, read    |
| 0x005D L2D_TLB_REFILL_WR   | 0x005F L2D_TLB_WR   | Attributable Level 2 data TLB refill rate, write   |
| 0x00A2 L3D_CACHE_REFILL_RD | 0x00A0 L3D_CACHE_RD | Attributable Level 3 data cache refill rate, read  |
| 0x00A3 L3D_CACHE_REFILL_WR | 0x00A1 L3D_CACHE_WR | Attributable Level 3 data cache refill rate, write |

## D14.5.2 Latency events

IZHFDC

The following are meaningful combination of latency events:

Table D14-5 Meaningful combinations of latency events

| Numerator                        | Denominator               | Ratio                                                                |
|----------------------------------|---------------------------|----------------------------------------------------------------------|
| 0x8120 INST_FETCH_PERCYC         | 0x8124 INST_FETCH         | Mean duration of instruction fetch events in processor cycles        |
| 0x8121 MEM_ACCESS_RD_PERCYC      | 0x0066 MEM_ACCESS_RD      | Mean duration of memory read access events in processor cycles       |
| 0x8125 , BUS_REQ_RD_PERCYC       | 0x818D , BUS_REQ_RD       | Bus read transaction average latency                                 |
| 0x8128 DTLB_WALK_PERCYC          | 0x0034 DTLB_WALK          | Mean duration of data or unified TLB walk events in processor cycles |
| 0x8129 ITLB_WALK_PERCYC          | 0x0035 ITLB_WALK          | Mean duration of instruction TLB walk events in processor cycles     |
| 0x8320 , L1D_CACHE_REFILL_PERCYC | 0x0003 , L1D_CACHE_REFILL | Level 1 data cache refill average duration                           |

## D14.5.3 Cache hit events and associated data source events

IHMZQY

The following are meaningful combination of cache hit events:

## Table D14-6 Meaningful combinations of cache hit events and associated data source events

| Numerator                     | Denominator                 | Ratio                                                       |
|-------------------------------|-----------------------------|-------------------------------------------------------------|
| 0x820C , L1D_CACHE_HIT_PRFM a | 0x8142 , L1D_CACHE_PRFM a   | Level 1 data or unified cache software prefetch hit ratio a |
| 0x81CC , L1D_CACHE_HIT_RW a   | 0x82A0 ,MEM_ACCESS_RW       | Level 1 data or unified cache demand cache hit rate a       |
| 0x81CF , LL_CACHE_HIT_RW      | 0x82A0 ,MEM_ACCESS_RW       | Last level cache demand cache hit rate                      |
| 0x8232 ,LOCAL_MEM_RW          | 0x82A0 ,MEM_ACCESS_RW       | Local memory demand access rate                             |
| 0x823B ,REMOTE_MEM_RW         | 0x82A0 ,MEM_ACCESS_RW       | Remote memory demand access rate                            |
| 0x821D , L2D_CACHE_HITM_RW a  | 0x81CD , L2D_CACHE_HIT_RW a | Level 2 data or unified cache demand cache hit rate a       |

## D14.5.4 Cache line state tracking events

ILGBBR

The following are meaningful combination of cache line stake tracking events:

Table D14-7 Meaningful combinations of cache line state tracking events

| Ratio                                                                | Meaning                                                                      |
|----------------------------------------------------------------------|------------------------------------------------------------------------------|
| 1 - ( 0x81EC , L1D_CACHE_HIT_RW_FHWPRF ÷ 0x8154 , L1D_CACHE_HWPRF) a | Level 1 data or unified cache data fetched by hardware prefetcher not used a |
| 1 - ( 0x81DC , L1D_CACHE_HIT_RW_FPRFM ÷ 0x8142 , L1D_CACHE_PRFM) a   | Level 1 data or unified cache data fetched by software prefetch not used a   |
| 0x825C , L1D_LFB_HIT_RW_FPRFM ÷ 0x8142 , L1D_CACHE_PRFM a            | Level 1 data or unified cache data fetched late by software prefetch a       |

## D14.5.5 TLB events

IPHZQV

The following are meaningful combination of TLB events:

## Table D14-8 Meaningful combinations of TLB events

| Numerator                  | Denominator         | Ratio                                            |
|----------------------------|---------------------|--------------------------------------------------|
| 0x8188 , DTLB_WALK_BLOCK a | 0x0034 ,DTLB_WALK a | Data TLB block translation table walk fraction a |
| 0x818A , DTLB_WALK_PAGE a  | 0x0034 ,DTLB_WALK a | Data TLB page translation table walk fraction a  |

## D14.5.6 At-retirement events

ICYQZJ

The following are meaningful combinations of at-retirement events:

Table D14-9 Meaningful combinations of at-retirement events

| Numerator                           | Denominator           | Ratio                                                                              |
|-------------------------------------|-----------------------|------------------------------------------------------------------------------------|
| 0x82B0 , L1I_CACHE_HIT_RETIRED      | 0x0008 , INST_RETIRED | Architecturally executed instruction hit Level 1 instruction cache                 |
| 0x82E0 , L2I_CACHE_MISS_RETIRED     | 0x0008 , INST_RETIRED | Architecturally executed instruction missed Level 2 instruction cache              |
| 0x82EC , L1D_CACHE_HIT_LDST_RETIRED | 0x0008 , INST_RETIRED | Architecturally executed load or store instruction hit in Level 1 data cache       |
| 0x82C9 , L2D_CACHE_HITM_ST_RETIRED  | 0x0008 , INST_RETIRED | Architecturally executed store instruction hit modified data in Level 2 data cache |
| 0x82B7 , LL_CACHE_MISS_LD_RETIRED   | 0x0008 , INST_RETIRED | Architecturally executed load instruction missed in Last level cache               |

| Numerator                       | Denominator               | Ratio                                                           |
|---------------------------------|---------------------------|-----------------------------------------------------------------|
| 0x82F0 , ITLB_HIT_RETIRED       | 0x0008 , INST_RETIRED     | Architecturally executed instruction which hit in the ITLB      |
| 0x82F7 , DTLB_WALK_LDST_RETIRED | 0x82AA , LDST_ANY_RETIRED | Architecturally executed LDST instructions DTLB miss fraction   |
| 0x82AF , CRYPTO_RETIRED         | 0x0008 , INST_RETIRED     | Architecturally executed cryptographic data processing fraction |

## D14.5.7 Speculatively executed operation events

IRDHPB

The number of speculatively executed operations performed on individual scalar values, assuming that all SVE vector elements are Active, can be determined from a pair of event counters. Combined multiply-add and multiply-subtract instructions are counted as two operations per element.

Table D14-10 Meaningful combinations of speculatively executed operation events

| Ratio                                                                  | Meaning                                                                         |
|------------------------------------------------------------------------|---------------------------------------------------------------------------------|
| 0x80C0 , FP_SCALE_OPS_SPEC × VL÷128 + 0x80C1 , FP_FIXED_OPS_SPEC       | Total number of individual floating-point operations (any precision) performed  |
| 0x80C2 , FP_HP_SCALE_OPS_SPEC × VL÷128 + 0x80C3 , FP_HP_FIXED_OPS_SPEC | Total number of individual half-precision floating-point operations performed   |
| 0x80C4 , FP_SP_SCALE_OPS_SPEC × VL÷128 + 0x80C5 , FP_SP_FIXED_OPS_SPEC | Total number of individual single-precision floating-point operations performed |
| 0x80C6 , FP_DP_SCALE_OPS_SPEC × VL÷128 + 0x80C7 , FP_DP_FIXED_OPS_SPEC | Total number of individual double-precision floating-point operations performed |
| 0x80C8 , INT_SCALE_OPS_SPEC × VL÷128 + 0x80C9 INT_FIXED_OPS_SPEC       | Total number of individual integer operations performed                         |
| 0x80CA , LDST_SCALE_OPS_SPEC × VL÷128 + 0x80CB , LDST_FIXED_OPS_SPEC   | Total number of individual load/store accesses performed                        |
| 0x80CC , LD_SCALE_OPS_SPEC × VL÷128 + 0x80CD , LD_FIXED_OPS_SPEC       | Total number of individual load accesses performed                              |
| 0x80CE , ST_SCALE_OPS_SPEC × VL÷128 + 0x80CF , ST_FIXED_OPS_SPEC       | Total number of individual store accesses performed                             |

## D14.5.8 Bytes loaded and stored events

INYJRH

The number of bytes speculatively loaded from memory or stored to memory, assuming that all SVE vector elements are Active, can be determined from a pair of event counters.

Table D14-11 Meaningful combinations of speculative load or store events

| Ratio                                                                    | Meaning                                                       |
|--------------------------------------------------------------------------|---------------------------------------------------------------|
| 0x80DA , LDST_SCALE_BYTES_SPEC × VL÷128 + 0x80DB , LDST_FIXED_BYTES_SPEC | Total number of bytes loaded from memory and stored to memory |

| Ratio                                                                | Meaning                                  |
|----------------------------------------------------------------------|------------------------------------------|
| 0x80DC , LD_SCALE_BYTES_SPEC × VL÷128 + 0x80DD , LD_FIXED_BYTES_SPEC | Total number of bytes loaded from memory |
| 0x80DE , ST_SCALE_BYTES_SPEC × VL÷128 + 0x80DF , ST_FIXED_BYTES_SPEC | Total number of bytes stored to memory   |

## D14.5.9 Overall vector utilization events

IMVTZM

Vector utilization rates for SVE events which ignore the number of Active elements can be estimated by adjusting them using the following ratios:

Table D14-12 Meaningful combinations of speculative predicated events

| Numerator                      | Denominator            | Meaning                   |
|--------------------------------|------------------------|---------------------------|
| 0x8076 , SVE_PRED_FULL_SPEC    | 0x8074 , SVE_PRED_SPEC | All predicates active     |
| 0x8077 , SVE_PRED_PARTIAL_SPEC | 0x8074 , SVE_PRED_SPEC | Partial predicates active |
| 0x8075 , SVE_PRED_EMPTY_SPEC   | 0x8074 , SVE_PRED_SPEC | No predicates active      |

## D14.5.10 Vector loop efficiency events

IMXYQS

The effectiveness with which sequential or scalar source loops are vectorized can be estimated using ratios of the SVE\_PLOOP\_*\_SPEC predicated loop events, as shown in the following table:

Table D14-13 Meaningful combinations of speculative sequential or scalar source loops events

| Numerator                    | Denominator                  | Meaning                          |
|------------------------------|------------------------------|----------------------------------|
| 0x8072 , SVE_PLOOP_ELTS_SPEC | 0x8073 , SVE_PLOOP_TERM_SPEC | Source level iterations per loop |
| 0x8071 , SVE_PLOOP_TEST_SPEC | 0x8073 , SVE_PLOOP_TERM_SPEC | Vectorized iterations per loop   |
| 0x8072 , SVE_PLOOP_ELTS_SPEC | 0x8071 , SVE_PLOOP_TEST_SPEC | Parallelism per vector loop      |