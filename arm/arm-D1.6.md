## D1.6 Resets and power domains

IDQXXZ

The PE logic is split into a Debug power domain and a Core power domain. Cold and Warm resets, reset elements in the Core power domain. An External debug reset can reset the Debug power domain. Other resets might be implemented.

## D1.6.1 Power domains and reset domains

RJMTZY

IQBPTS

RPDMKB

RZDVQQ

RGTVLN

The architecture defines the following power domains:

- The Core power domain.
- The Debug power domain.
- The system counter power domain.
- If trace is implemented, a power domain for the Trace Unit.
- If FEAT\_RAS is implemented, there may be one or more IMPLEMENTATION DEFINED error recovery power domains. The relationship between these power domains and other power domains is IMPLEMENTATION DEFINED. For error records associated with the PE, this is the same as the Core power domain.
- If FEAT\_AMUv1 is implemented, the AMU power domain.
- For MPAMMemory System Components (MSC), a power domain for each MSC.

The power domains are described as logical because the architecture does not require two physical power domains.

It is IMPLEMENTATION DEFINED whether each power domain powers up and powers down separately or together.

The Core power domain contains:

- Non-debug registers and logic.
- Self-hosted debug registers and logic.
- Shared debug registers and logic.
- Some external debug registers and logic.

The Debug power domain contains:

- The interface between the PE and the external debugger.
- Some external debug registers.

RMLXWM

If an external debugger is connected to the PE, the Debug power domain is powered up.

IKTSWK

For more information on access permissions for the external debug interface registers, see Access permissions for the External debug interface registers or the individual register descriptions.

## D1.6.2 Reset types

IHDQLB

The architecture defines the following resets:

- Warm reset.
- Cold reset.
- External Debug reset.
- Trace unit reset. See Resetting the trace unit.
- Timer reset.
- If FEAT\_RAS is implemented, there may be one or more IMPLEMENTATION DEFINED error recovery resets. The relationship between this reset and other resets is IMPLEMENTATION DEFINED. For error records associated with the PE, the error recovery reset is the same as Warm reset.
- If the FEAT\_AMUv1 is implemented, AMU reset.
- For MPAMMemory System Components (MSC), a reset for each MSC.

IFMTCY

Other resets are IMPLEMENTATION DEFINED and can be mapped onto the architecturally-defined resets.

RPXXYQ

Mechanisms to assert resets, other than RMR\_ELx, are IMPLEMENTATION DEFINED. One such mechanism is EDPRCR.CWRR. Any reset-asserting mechanism that software can command, including hardware mechanisms directly exposed to software, must only be accessible at the highest Exception level.

RHLDGD

When a Cold reset is asserted, for each register in the Core power domain, the reset sets the register to its architecturally-defined reset value.

RPJXVL

When a Warm reset is asserted, registers and logic in the Core power domain that are affected by the Warm reset are reset to their architecturally-defined reset value. Registers and logic that are only reset by a Cold reset are unaffected by a Warm reset.

RNBKHK

When an External Debug reset is asserted, the External Debug reset domain is reset and affected registers are set to their architecturally-defined External debug reset values. The Cold reset domain is unaffected.

RRKSZM

When a Cold reset is asserted, a Warm reset is asserted.

IVBZBW

Every register field that has storage belongs to exactly one reset domain. Each System register field definition defines the reset domain and the reset value.

IMWTXK

If RMR\_ELx is implemented, writing 1 to RMR\_ELx.RR requests a Warm reset.

RSGXSW

Writing 1 to RMR\_ELx.RR is only a request for a Warm reset. The reset is not guaranteed to occur unless the following code sequence is executed:

```
execution,
```

```
; In addition, interrupts and debug requests for this PE should be disabled ; in the system before running this sequence to ensure the WFI suspends MOV Wy, #3 ; for AArch64, #2 for AArch32; y is any register DSB ; ensure all stores etc are complete MSR RMR_ELx, Wy ; request the reset ISB ; synchronize change to the RMR Loop WFI ; enter a quiescent state B Loop
```

RDDTVZ

It is IMPLEMENTATION DEFINED whether a Warm reset can be asserted without using RMR\_ELx.

ILWNDC

Arm recommends that a Warm reset can be asserted independently of a Cold reset.

IQLZGF

AWarmreset allows debugging across a reset of the PE logic in the Core power domain.

RSKGMH

It is IMPLEMENTATION DEFINED whether an External Debug reset and a Cold reset can be asserted independently.

IWTJYS

Arm recommends that when separate Core and Debug power domains are implemented, the External Debug reset and Cold reset can be asserted independently.

## D1.6.3 Reset behavior

ITWYCF

Immediately after a reset, much of the PE state is architecturally UNKNOWN. However, some of the PE state is defined, see the individual register descriptions for more information. The state that is reset to known values is sufficient to permit predictable initial execution at the highest Exception level, such that this execution is then capable of initializing the remaining state of the system where necessary before use.

RJYLQV

RZBHGJ

IQSCPY

When a Cold or Warm reset is asserted, all of the following occur:

- The PE enters the highest implemented Exception level.
- The stack pointer for the highest implemented Exception level, SP\_ELx, is selected.

When a Cold or Warm reset is deasserted, execution starts at an IMPLEMENTATION DEFINED address, anywhere in the Physical Address (PA) range. The RVBAR associated with the highest implemented Exception level RVBAR\_EL1, RVBAR\_EL2, or RVBAR\_EL3, holds the address at which the PE starts execution.

When a Cold or Warm reset is deasserted, the IMPLEMENTATION DEFINED address from which the PE starts execution is typically set either by a hardwired configuration of the PE or by configuration input signals.

| R RRJLM   | When a Warm reset is asserted, all of the following are architecturally UNKNOWN:                                                                                                                                     |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I KWHDG   | When a Cold or Warm reset is asserted, PSTATE.{SS, IL, nRW, EL, SP, D, A, I, F, DIT, EXLOCK, ZA, SM, PACM, UINJ} fields are set to known values.                                                                     |
| R BGSHC   | When a Cold or Warm reset is asserted, the TLBs and caches are in an IMPLEMENTATION DEFINED state.                                                                                                                   |
| R XNNNH   | When a Cold or Warm reset has been asserted and before the memory management system is enabled, the TLBs, caches or both might need to be invalidated by IMPLEMENTATION DEFINED invalidation sequences.              |
| R TZHFZ   | When a Cold or Warm reset has been asserted and before Normal memory accesses are permitted to be Cacheable, the TLBs, caches or both might need to be invalidated by IMPLEMENTATION DEFINED invalidation sequences. |
| R KMCGN   | If IMPLEMENTATION DEFINED resets are implemented, each IMPLEMENTATION DEFINED reset can treat the cache and TLB state differently.                                                                                   |
| R TJGFQ   | If IMPLEMENTATION DEFINED resets are implemented, for each IMPLEMENTATION DEFINED reset, the TLBs, caches, or both might require a different IMPLEMENTATION DEFINED invalidation sequence.                           |
| I PHDMZ   | The IMPLEMENTATION DEFINED invalidation sequence might be a NOP.                                                                                                                                                     |
| R VFMKQ   | D1.6.3.1 External debug access to registers in reset If External Debug reset is asserted, for each register that can be accessed by the external debug interface, a register access                                  |
| QHHMQ     | If either a Cold or Warm reset is asserted, accesses of registers or register fields might be direct accesses or indirect side-effects of an access.                                                                 |
| I         |                                                                                                                                                                                                                      |
| R YKRBF   | If either a Cold or Warm reset is asserted, external debug interface accesses of a register or register field have the following effects:                                                                            |

| Access   | Register or register field reset behavior   | Effect on register or register field                                             |
|----------|---------------------------------------------|----------------------------------------------------------------------------------|
| Write    | Reset by the reset signal                   | Set to CONSTRAINED UNPREDICTABLE choice of the reset value or the value written. |
| Write    | Not reset by the reset signal               | Set to the value written.                                                        |
| Read     | Reset by the reset signal                   | Returns an UNKNOWN value.                                                        |
| Read     | Not reset by the reset signal               | Returns the value of the register or register field.                             |