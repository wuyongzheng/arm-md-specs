## D19.3 Branch record buffer operation

| R LKWNB   | The Branch Record Buffer Extension operation is controlled by the BRBCR_EL1, BRBCR_EL2, and BRBFCR_EL1 registers.                                                                                                                                                                                                                                                    |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R PYBRZ   | Generation of Branch records is paused when BRBFCR_EL1.PAUSED is 1.                                                                                                                                                                                                                                                                                                  |
| R YDZNK   | When generation of Branch records is paused, Branch records are not generated.                                                                                                                                                                                                                                                                                       |
| R NXCWF   | If EL2 is implemented, a BRBE freeze event occurs when all of the following are true: • BRBCR_EL1.FZP is 1. • Generation of Branch records is not paused. • PMOVSCLR_EL0[(MDCR_EL2.HPMN-1):0] is nonzero.                                                                                                                                                            |
| R GXGWY   | If EL2 is implemented, a BRBE freeze event occurs when all of the following are true: • BRBCR_EL2.FZP is 1. • Generation of Branch records is not paused.                                                                                                                                                                                                            |
| R PKTXQ   | If EL2 is not implemented, a BRBE freeze event occurs when all of the following are true: • BRBCR_EL1.FZP is 1. • Generation of Branch records is not paused. • PMOVSCLR_EL0[(PMCR_EL0.N-1):0] is nonzero.                                                                                                                                                           |
| R LDMVK   | If FEAT_PMUv3_ICNTR is implemented, then a BRBE freeze event occurs when all of the following are true: • BRBCR_EL1.FZP is 1. • Generation of Branch records is not paused.                                                                                                                                                                                          |
| R LBQZR   | If FEAT_PMUv3_SS is implemented, on a successful Capture event, then a BRBE freeze event occurs when all of the following are true: • FEAT_BRBE is implemented. • BRBCR_EL1.FZPSS is 1. • Either EL2 is not implemented or BRBCR_EL2.FZPSS is 1. This applies even when EL2 is disabled in the current Security state. • Generation of Branch records is not paused. |
|           | record generation is paused. This means the Branch record might or might not be captured before the BRBE freeze occurs. The BRBCR_EL1.FZP and BRBCR_EL2.FZP controls ignore the overflow status bits for PMUcounters in synchronous mode.                                                                                                                            |
| R VMSDM   |                                                                                                                                                                                                                                                                                                                                                                      |
| I BVSGF   | To ensure Branch records are captured only up to the point of taking a synchronous PMUexception, software should configure the BRBE Prohibited regions to prohibit the Exception level where the PMUexception is taken to, and higher Exception levels. This has the effect of stopping branch recording when the PMUexception is taken.                             |

RBHYTD

RQKQZL

Note

This mechanism can only be used when profiling software that only executes at lower Exception levels.

On a BRBE freeze event:

- BRBFCR\_EL1.PAUSED is set to 1.
- The current timestamp is captured in BRBTS\_EL1.

The source of value of the timestamp captured in BRBTS\_EL1 is selected by the combination of programming of BRBCR\_EL2.TS and BRBCR\_EL1.TS. See Table D19-11 and BRBETimeStamp() .

The timestamp is a choice between:

- Physical time, which is defined by the physical count value returned by PhysicalCountInt ().
- If FEAT\_ECV is implemented, offset physical time, which is defined as the value of PhysicalCountInt () minus a physical offset.

If any of the following are true, the physical offset is zero:

- -EL2 is not implemented.
- -FEAT\_ECV\_POFF is not implemented.
- -CNTHCTL\_EL2.ECV is 0.
- -EL3 is implemented and SCR\_EL3.ECVEn is 0.

Otherwise the physical offset is the value of CNTPOFF\_EL2.

- Virtual time, which is defined as the value of PhysicalCountInt () minus a virtual offset. If any of the following are true, the virtual offset is zero:
- -EL2 is not implemented.

Otherwise, the virtual offset is always CNTVOFF\_EL2, including when a read of CNTVCT\_EL0 at the current Exception level would treat the virtual offset as zero.

## Table D19-11 Captured timestamp

| BRBCR_EL2.TS           | BRBCR_EL1.TS           | Captured timestamp                   |
|------------------------|------------------------|--------------------------------------|
| 0b00 (delegate)        | 0b01 (virtual)         | PhysicalCountInt() - virtual offset  |
|                        | 0b10 (offset physical) | PhysicalCountInt() - physical offset |
|                        | 0b11 (physical)        | PhysicalCountInt()                   |
| 0b01 (virtual)         | 0bxx                   | PhysicalCountInt() - virtual offset  |
| 0b10 (offset physical) | 0bxx                   | PhysicalCountInt() - physical offset |
| 0b11 (physical)        | 0bxx                   | PhysicalCountInt()                   |

If EL2 is not implemented, the Effective value of BRBCR\_EL2.TS is 0b00 .

| R GWMZV   | When a valid Branch record is captured in the Branch record buffer storage, the BRB_FILTRATE event is generated.                                                                                                                                                                                                                                                    |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GMCHN   | When BRB_FILTRATE is generated for an exception or an exception return, it is an Exception-related event. For more information on PMUevent filtering, see Exception-related events.                                                                                                                                                                                 |
| I WGZSC   | It is CONSTRAINED UNPREDICTABLE whether a BRB_FILTRATE event is generated after a BRB INJ causes a Branch record to be injected.                                                                                                                                                                                                                                    |
| I SJDRW   | It is expected that the Branch record buffer storage is in a BRBE Prohibited region during software context switches. During software context switches, if the PMUevent counters are not prohibited from counting events, it is expected that event counters set to count the BRB_FILTRATE event are prohibited from counting.                                      |
| I RMGDV   | The architecture does not define when PMUevents are counted relative to the instructions that caused the event. Events generated by an instruction might be counted before or after the instruction becomes architecturally executed, and events might be counted for operations that do not become architecturally executed. This means that events can be counted |

speculatively and/or out-of-order regarding the simple sequential execution of the program. Events might also be counted simultaneously by other event counters when the overflow occurs, including events from different instructions. In addition, multiple instances of an event might occur simultaneously, meaning that an event counter unsigned overflow can yield a nonzero value in the event counter.

Furthermore, the Branch records are generated only for architecturally executed operations. See RKXTKS.

These properties mean that, unless otherwise stated, on a BRBE freeze event, it is CONSTRAINED UNPREDICTABLE whether the branches that define the basic block containing the instruction causing that event are captured in the Branch record buffer.

An exception to this relaxation applies for the BRB\_FILTRATE event.

- SJCHLT If a direct read of PMOVSCLR\_EL0 returns a nonzero value for a subset of the overflow flags, such that one of RNXCWF, RGXGWY, or RPKTXQ means that a BRBE freeze event should occur, then a direct read of BRBFCR\_EL1 ordered after the direct read of PMOVSCLR\_EL0 will return BRBFCR\_EL1.PAUSED is 1.
- IQNBDV Direct reads of System registers require explicit synchronization for following direct reads of other System registers to be ordered after the first direct read. For more information, see General behavior of accesses to the AArch64 System registers.
- RSRJND If a direct read of BRBFCR\_EL1.PAUSED returns 1, then no operations ordered after the direct read will generate further Branch records until BRBFCR\_EL1.PAUSED is cleared by software.

Note: The subsequent operations can be ordered by a Context synchronization event.