## D11.9 Guarded Control Stack data accesses

| R ZMNSV   | AGuarded Control Stack data access that is not aligned to size of a Guarded Control Stack procedure return record generates an Alignment fault.                                                                                                                                                                                                                                                                                                                                                 |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I RYLTG   | If a Guarded Control Stack data access causes an Alignment fault, the resulting fault is reported with the ESR_ELx.EC code 0b100100 or 0b100101 .                                                                                                                                                                                                                                                                                                                                               |
| R VDJXL   | Unless otherwise specified, a Guarded Control Stack data access is single-copy atomic at 64-bit granularity.                                                                                                                                                                                                                                                                                                                                                                                    |
| I BFHQY   | For more information on atomicity, see Requirements for single-copy atomicity.                                                                                                                                                                                                                                                                                                                                                                                                                  |
| I KNXKG   | AGuarded Control Stack data access might clear the state of the local Exclusives monitor if the local monitor is in the Exclusive Access state. For more information on the effects on the local monitor, see Exclusive access instructions and Non-shareable memory locations.                                                                                                                                                                                                                 |
| R FFJDX   | When a Guarded Control Stack data access accesses a memory type that is not one of the following, it is CONSTRAINED UNPREDICTABLE whether: • AData Abort for unsupported access, using ESR_ELx.DFSC value 0b110101 , is generated. - In this case, it is IMPLEMENTATION DEFINED whether the Data Abort is generated according to the memory type after all stages of translation, or at each stage of translation. • The access proceeds using the specified memory type. The memory types are: |
| S JBQRL   | If translation or data caches are disabled, then Guarded Control Stack data access use Device or Normal Non-cacheable memory types respectively. To avoid use of mismatched memory attributes or generation of a Data Abort for an unsupported access, software should use the following sequence when disabling translation or data caches: 1. Disable GCS using GCSCR_ELx and GCSCRE0_EL1.                                                                                                    |
| R KSTSV   | For the purpose of Memory Partitioning and Monitoring, a Guarded Control Stack data access is treated in the same way as any other load/store access at that Exception level.                                                                                                                                                                                                                                                                                                                   |
| R CYLYV   | The endianness of a Guarded Control Stack data access is same as the endianness of any other load/store access at that                                                                                                                                                                                                                                                                                                                                                                          |
|           | Exception level.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
| I QJRGN   | There are no controls in the watchpoint control registers to select or deselect a Guarded Control Stack data access independently of any other load/store access.                                                                                                                                                                                                                                                                                                                               |
| I WBHHX   | When FEAT_MTE is implemented, a Guarded Control Stack data access is a Tag Unchecked accesses as defined by R DRGYL .                                                                                                                                                                                                                                                                                                                                                                           |
| I         | If a Guarded Control Stack data access causes a synchronous Data Abort exception, the resulting fault is reported as a Data Abort from the current Exception level with the ESR_ELx.EC code 0b100100 or 0b100101 .                                                                                                                                                                                                                                                                              |
| WLNYQ     |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I JGYZS   | If a Guarded Control Stack data access causes a Granule Protection Check exception, the resulting fault is reported as the Granule Protection Check exception. For more information on the ISS encoding, see ISS encoding for a Granule Protection Check exception.                                                                                                                                                                                                                             |
| I BQPPZ   | If a Guarded Control Stack data access causes a watchpoint exception, the resulting fault is reported as a watchpoint exception from the current Exception level with the ESR_ELx.EC code 0b110100 or 0b110101 .                                                                                                                                                                                                                                                                                |

| I YMCFF   | For more information on The Access flag when there is a GCS Data Check exception generated from an instruction, see Hardware management of the Access flag.                                                                                                                     |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I KDWGR   | When hardware management of the Access flag is enabled and if there is a GCS Data Check exception caused by a GCSSS2 instruction, it is CONSTRAINED UNPREDICTABLE whether translations for the store part of the GCSSS2 instruction update the Access flag.                     |
| I LKVJG   | When hardware management of the dirty state mechanism is enabled and if there is a GCS Data Check exception generated from a GCSSS1 instruction, it is CONSTRAINED UNPREDICTABLE whether translations for Guarded Control Stack data access update the dirty state information. |
| R CQXHQ   | When hardware management of the dirty state mechanism is enabled and if there is a GCS Data Check exception generated from a GCSSS2 instruction, translations for Guarded Control Stack data access do not update the dirty state information.                                  |
| I HGNJQ   | For the purposes of generating PMUevents, Guarded Control Stack data accesses are:                                                                                                                                                                                              |
| I VTQSX   | If FEAT_SPE is implemented, for information on sampling a Guarded Control Stack data access, see The Statistical Profiling Extension.                                                                                                                                           |
| I NPBWN   | An Overshooting GCS Memory effect that is not associated with any instruction is not sampled.                                                                                                                                                                                   |
| I QRDQX   |                                                                                                                                                                                                                                                                                 |
|           | For information on the Events packet in the Statistical Profiling Extension sample record, see Events packet.                                                                                                                                                                   |

## D11.9.1 Guarded Control Stack data access behaviors

DNFPLW

AGCSMemory Read effect is a Memory Read effect produced by any of the following instructions:

- Aprocedure return instruction; to read the data addressed by the current GCS pointer plus any applicable offset.
- GCSPOPM ; to read the data addressed by the current GCS pointer plus any applicable offset.
- GCSSS2 ; to read the data addressed by the current GCS pointer plus any applicable offset.
- GCSPOPCX ; to read the data addressed by the current GCS pointer plus any applicable offset.
- GCSPOPX ; to read the data addressed by the current GCS pointer plus any applicable offset.

AGCSMemory Write effect is a Memory Write effect produced by any of the following:

- Abranch with link instruction; to write the data addressed by the current GCS pointer plus any applicable offset.
- GCSSS2 ; to write the data addressed by a calculation from the data read by the same GCSSS2 instruction.
- GCSPUSHM ; to write the data addressed by the current GCS pointer plus any applicable offset.
- GCSPUSHX ; to write the data addressed by the current GCS pointer plus any applicable offset.
- GCSSTR ; to write the data addressed by the Xn|SP operand of the instruction, plus any applicable offset.
- GCSSTTR ; to write the data addressed by the Xn|SP operand of the instruction, plus any applicable offset.
- An Overshooting GCS Memory effect; to write the data addressed by the current GCS pointer plus any applicable offset.

AGCSMemory effect is one of the following:

- AGCSMemory Read effect.
- AGCSMemory Write effect.

DMYKCM

DMVQYZ

DNHBBP

DQQLCF

RYJHMB

A GCSSS1 Memory effect is a Memory effect generated by a GCSSS1 instruction, to access the data addressed by the Xt operand. A GCSSS1 Memory effect is one of the following:

- A GCSSS1 Memory Read effect, which occurs when reading the data.
- A GCSSS1 Memory Write effect, which occurs when writing the data.

A GCSB effect is generated by any of the following instructions:

- GCSB .
- GCSSS2 .

A GCSB effect provides the ability to manage the ordering and coherency of GCS Memory effects in relation to other Memory effects.

AGuarded Control Stack data access is one of the following:

- AGCSMemory effect.
- A GCSSS1 Memory effect.

AGCSeffect is one of the following:

- GCS Memory effect.
- A GCSSS1 Memory effect.
- A GCSB effect.

DCHDJM A GCSB instruction causes a GCSB effect.

A GCSSS2 instruction causes a GCSB effect.

A GCSB effect provides the ability to manage the ordering and coherency of GCS Memory effects in relation to other Memory effects.

RFZRGP Two effects E1 and E2 to the Same Location follow the same ordering requirements as two Explicit Memory effects to the Same Location if one of the following applies:

- E1 and E2 are both GCS Memory effects.
- E1 is a GCS Memory effect, E2 is an Explicit Memory effect, and there exists a GCSB effect E3 such that E1 appears in program-order before E3, and E3 appears in program order before E2.
- E1 is an Explicit Memory effect, E2 is a GCS Memory effect, and there exists a GCSB effect E3 such that E1 appears in program-ordered before E3, and E3 appears in program order before E2.
- E1 is a GCS Memory effect and E2 is a GCSSS1 Memory effect.
- E1 is a GCSSS1 Memory effect and E2 is a GCS Memory effect.
- E1 and E2 are both GCSSS1 Memory effects.
- E1 is a GCSSS1 Memory effect and E2 is an Explicit Memory effect.
- E1 is an Explicit Memory effect and E2 is a GCSSS1 Memory effect.

RTDLVW AGCSeffect E1 is Hardware-required-ordered-before another GCS effect E2 if one of the following applies:

- E1 is a GCSB effect and E2 is a GCS Memory effect. E1 appears in program order before E2.
- E1 is a GCS Memory effect and E2 is a GCSB effect. E1 appears in program order before E2.
- RZRZQM AGCSeffect E1 is Barrier-ordered-before an Explicit Memory effect E2, or conversely an Explicit Memory effect E1 is Barrier-ordered-before a GCS effect E2, if the GCS effect is a GCSB or a GCSSS1 Memory effect, E1 appears in program order before E2, and if and only if one of the following applies:
- E1 appears in program order before a DMB FULL effect E3 and E3 appears in program order before E2.
- E1 is the Memory Write effect generated by an atomic instruction with both Acquire and Release semantics.
- E1 is a Memory Read effect (R1) which appears in program order before a DMB LD that appears in program order before E2.
- E1 is a Memory Read effect (R1), except an Implicit Tag Memory Read effect, generated by an instruction with Acquire or AcquirePC semantics.
- E2 is a Memory Write effect (W2) generated by an instruction with Release semantics.
- E1 is a Memory Write effect (W1) which appears in program order before a DMB ST that appears in program order before E2.

GCSSS1 performs a read-modify-write and is therefore subjected to the Atomic-ordered-before ordering requirements and the Atomic axiom.

RBGSJM GCSSS2 performs a Memory Read effect to access the data addressed by the current GCS pointer, which returns address X, and is Intrinsically-ordered-before a Memory Write effect to X by the same GCSSS2 instruction.

RRCNPD The GCS Memory Write effect performed by a GCSSS2 instruction is Intrinsically-ordered-before the GCSB effect from the same GCSSS2 instruction.

IYJSDD As GCSSS2 causes a GCSB effect, migrating a Guarded Control Stack between PEs does not require an explicit GCSB instruction if the Guarded Control Stack is switched using the GCSSS1 and GCSSS2 instruction pair.

IWFDGZ Entry to Debug state or exit from Debug state is not required to cause a GCSB effect which means that a debugger needs to manually cause such an event should such synchronization be required, for example by executing a GCSB instruction.

GCXFHZ To allow efficient usage of cache lines, FEAT\_GCS permits invalidating the dirty cache line contents that are already consumed by the procedure return instructions.

RSJPKS On execution of a GCS Memory effect that is a read access R1 to a Location M and is produced by any of the following instructions, without any exception caused by those instructions, a Memory Write effect is induced to the Location M and the write value is a CONSTRAINED UNPREDICTABLE choice of the following:

- Avalue that is written to the same Location M, by a GCS Memory effect that is a write access W2 and all of the following are true:
- -W2is in program order before R1.
- -There is no Memory Write effect W3 to the same Location M, that is not a GCS Memory effect, that exists in Coherence order after W2.
- -There is no write access W4 to the same Location M, and all of the following are true for W4:
- -W4is a Guarded Control Stack data access.
- -W4is in program order after W2 and in program order before R1.
- -There is a GCSB effect that appears in program order after W4 and appears in program order before R1.
- Avalue that is written to the same Location M, by a Memory Write effect W2 that is not a Guarded Control Stack data access and all of the following are true:
- -W2is in program order before R1.
- -There is no write access W3 to the same Location M, that is not a Guarded Control Stack data access, that exists in Coherence order after W2.
- -There is no write access W4 to the same Location M, and all of the following are true for W4:
- -W4is a Guarded Control Stack data access.
- -W4is in program order after W2 and in program order before R1.
- -There is a GCSB effect that appears in program order after W4 and appears in program order before R1.

The induced Memory Write effect is not the same as the one generated by a store instruction or one generated by a Branch with Link instruction. For example, the Memory Write effect:

- Does not cause any exceptions.
- Does not cause the side effects due to the translation.
- Does not affect the state of the local Exclusives monitor.
- Is transparent to translations and watchpoints.

The Memory Write effect is single-copy-atomic at doubleword granularity.

The Memory Write effect is part of the transactional write set if R1 is executed in Transactional state.

If R1 is not executed in Transactional state then one of the following must be true for W2 and W3:

- The Memory Write effect is executed outside Transactional state.
- The Memory Write effect is executed inside Transactional state and the transaction commits.

The instructions that can produce the Memory Read effect R1 mentioned above are:

- All procedure return instructions
- GCSPOPM .
- GCSPOPX .
- GCSPOPCX .
- GCSSS2 .

IXFLPD

RGZNKD

Example D11-1

For example, the LDR instruction in the following sequence is permitted to read any one of the following values:

- 0x114 .
- 0x110 .
- 0x10C .
- 0x300 .
- 0x000 .

| PC          | Instruction    |                                                                                    |
|-------------|----------------|------------------------------------------------------------------------------------|
| 0x0F0       | STR            | ;store 0x200 to an address 0x1000                                                  |
| 0x0F4 0x0F8 | GCSB DSYNC BL  | ;store 0xFC to the address 0x1000                                                  |
| 0x200       | RET            | ;load from the address 0x1000                                                      |
| 0x0FC 0x100 | GCSB DSYNC STR | ;store 0x300 to the address 0x1000                                                 |
| 0x104       | GCSB DSYNC     | ;make STR visible to subsequent load/stores from ;BL/RET instructions              |
| 0x108       | BL             | ;store 0x10C to the address 0x1000                                                 |
| 0x200       | RET            | ;load from the address 0x1000                                                      |
| 0x10C       | BL             | ;store 0x110 to the address 0x1000                                                 |
| 0x200       | RET            | ;load from the address 0x1000                                                      |
| 0x110       | BL             | ;store 0x114 to the address 0x1000                                                 |
| 0x200       | RET            | ;load from the address 0x1000                                                      |
| 0x114       | GCSB DSYNC     | ;make load/stores from BL/RET instructions visible ;to subsequent LDR instructions |
| 0x118       | LDR            | ;load from the address 0x1000                                                      |

RSJPKS provides implementation flexibility with respect to partial cache line transfer by permitting zeros to be written to entries below the current value of the GCS pointer.

An Overshooting GCS Memory effect is defined as the following:

- As a GCS Memory Write effect.
- With a write value of 0.
- As a write to a location M whose virtual address is lower than the current Guarded Control Stack pointer register. An Overshooting GCS Memory effect S1 is only permitted when all of the following are true:
- When the Guarded Control Stack is GCS Enabled at the current Exception level.
- An Overshooting GCS Memory effect has occurred to all Locations whose virtual address is greater than the virtual address of Location M and less than the current Guarded Control Stack pointer register.
- If S1 was any other GCS Memory effect it would have updated Location M.
- When hardware management of dirty state mechanism is enabled, S1 updates the dirty state information like any other GCS Memory effect.

RQQTVL Any transition of the local Exclusives monitor to the Open Access state caused by the Overshooting GCS Memory effect must not indefinitely delay forward progress of execution.

SYTYHX

It is anticipated that software uses guard pages between the Guarded Control Stacks of any two threads so that the contents of a Guarded Control Stack that is not currently in use are not overwritten by speculative accesses.

SQDQQQ

RRRBKD

The Overshooting GCS Memory effect can cause potential race conditions when a GCSSTR or GCSSTTR instruction accesses an address that is less than the address present in the applicable Guarded Control Stack register. Software is expected to maintain appropriate values in the applicable Guarded Control Stack registers.

No more Overshooting GCS Memory effects are generated for the Guarded Control Stack of an Exception level if any of the following are true:

- A GCSB effect occurs at that Exception level while the Guarded Control Stack is disabled for that Exception level, and the Guarded Control Stack remains disabled while PE is executing at that Exception Level.
- A GCSB effect is executed at a different Exception level and PE continues to execute at a different Exception level.

RLDSNT

The meaning of completion for a Guarded Control Stack data access is as following:

- AMemory Read effect R1 that is a GCS Memory effect or GCSSS1 Memory effect to a Location is complete for a shareability domain when all of the following are true:
- -Any write to the same Location by an Observer within the shareability domain, that is not a GCS Memory effect or GCSSS1 Memory effect, will be Coherence-after R1.
- -Any write W1 to the same Location by an Observer within the shareability domain, that is a GCS Memory effect or GCSSS1 Memory effect, will be Coherence-after R1 if a GCSB effect appears in program order before W1 and R1 is Ordered-before the GCSB effect using a DSB instruction.
- -Any translation table walks associated with R1 are complete for that shareability domain.
- AMemory Write effect W1 that is a GCS Memory effect or GCSSS1 Memory effect to a Location is complete for a shareability domain when all of the following are true:
- -Any write to the same Location by an Observer within the shareability domain, that is not a GCS Memory effect or GCSSS1 Memory effect, will be Coherence-after W1.
- -Any write W2 to the same Location by an Observer within the shareability domain, that is a GCS Memory effect or GCSSS1 Memory effect, will be Coherence-after W1 if a GCSB effect appears in program order before W2 and W1 is Ordered-before the GCSB effect using a DSB instruction.
- -Any read to the same Location by an Observer within the shareability domain, that is not a GCS Memory effect or GCSSS1 Memory effect, will either Reads-from W1 or Reads-from a Memory Write effect that is Coherence-after W1.
- -Any read R1 to the same Location by an Observer within the shareability domain, that is a GCS Memory effect or GCSSS1 Memory effect, will either Reads-from W1 or Reads-from a Memory Write effect that is Coherence-after W1 if a GCSB effect appears in program order before R1 and W1 is Ordered-before the GCSB effect using a DSB instruction.
- -Any translation table walks associated with the write are complete for that shareability domain.

RNKPMR In a TLB maintenance operation, for the purpose of completion requirements of memory accesses, a GCS Memory effect or GCSSS1 Memory effect is treated in the same way as a Memory effect produced by a regular load/store instruction.

RFKQCQ

When a GCS Memory effect or GCSSS1 Memory effect A1 appears in program order before a data cache maintenance instruction A2, for the purpose of creating ordering relationship between A1 and A2, A1 is treated as a Memory effect produced by a regular load/store instruction.

RHLTYS When a data cache maintenance instruction A1 appears in program order before a GCS Memory effect or GCSSS1 Memory effect A2, for the purpose of creating ordering relationship between A1 and A2, A2 is treated as a Memory effect produced by a regular load/store instruction.

RNLNHL For the purpose of creating ordering relationship between a data cache maintenance instruction A1 on PE1 and a GCS Memory effect or GCSSS1 Memory effect A2 on PE2, A2 is treated as a Memory effect produced by a regular load/store instruction if all of the following are true:

- A1 is Ordered-before a GCSB effect executed on PE2.
- A GCSB effect appears in program order before A2.

There is no ordering relationship defined between A1 and A2 if above conditions are not met.

RHZDQD For the purpose of creating ordering relationship between a GCS Memory effect or GCSSS1 Memory effect A1 on PE1 and a data cache maintenance instruction A2 on PE2, A1 is treated as a Memory effect produced by a regular load/store instruction if all of the following are true:

- A GCSB effect appears in program order after A1.
- A GCSB effect is Ordered-before A2.

There is no ordering relationship defined between A1 and A2 if above conditions are not met.

SXRJSB Context switching software is expected to use a GCSB effect as appropriate. For example code sequences, see Switching EL0 Guarded Control Stacks from EL1.