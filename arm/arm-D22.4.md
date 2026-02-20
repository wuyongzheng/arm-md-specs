## D22.4 Streaming execution priority

| D DXMSW   | Streaming execution refers to the execution of instructions by a PE when that PE is in Streaming SVE mode .                                                                              |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I CMRVS   | Arm expects a variety of implementation styles for SME, including styles where more than one PE shares SMEand Streaming SVE compute resources.                                           |
| I PQNJS   | Shared SMEand Streaming SVE compute resources are called a Streaming Mode Compute Unit (SMCU).                                                                                           |
| I MZXWD   | For implementations that share an SMCU, this architecture provides per-PE mechanisms that software can use to dynamically prioritize performance characteristics experienced by each PE. |

## D22.4.1 Streaming execution priority for shared implementations

IYYRZQ

Execution of certain instructions by a PE in Streaming SVE mode might experience a performance dependency on other PEs in the system that are also executing instructions in Streaming SVE mode . For example, this might occur when an SMCUis shared between PEs.

IWPQVV

IKTYTD

IHQXBH

DDGRTS

DYQFWM

RWPVQK

The architecture provides a mechanism to control the streaming execution priority of a PE, in SMPRI\_EL1. The streaming execution priority of a PE is relative to the streaming execution priority of other PEs, when a performance dependency exists between PEs executing in Streaming SVE mode .

An implementation that does not share SMCUs or has no performance dependency between PEs might not need to limit or prioritize execution of one PE relative to another.

The streaming execution priority mechanism is optional.

All PEs that share a given SMCU form a Priority domain .

Different Priority domains represent unrelated SMCUs.

All PEs in a Priority domain have the same value of SMIDR\_EL1.Affinity and SMIDR\_EL1.Affinity2.

RCVLSF PEs in different Priority domains

RGGDRC

have different values of SMIDR\_EL1.Affinity or SMIDR\_EL1.Affinity2.

The streaming execution priority in SMPRI\_EL1 affects execution of a PE relative to all other PEs in the same Priority domain.

RSBCRG

RRQXFC

IBLMYK

- IYBQNW

IPRNMJ

All SMCUs in the system have a consistent interpretation of the streaming execution priority values.

The streaming execution priority mechanism affects the execution of instructions by a shared SMCU when the PE is in Streaming SVE mode and does not directly control the execution of other types of instruction.

If system software does not support differentiation of streaming execution priority of threads, it is safe to use a value of 0 for all threads.

The architecture considers Priority domain to be non-overlapping sets, meaning that in a shared-SMCU system, a PE is associated with at most one SMCU.

## D22.4.1.1 Streaming execution context management

Arm expects that the SVE and SME instructions used by save, restore, and clear routines for the Streaming SVE mode SVE registers, the ZA storage, and the ZT0 register when FEAT\_SME2 is implemented, are limited to using the following SME and SVE instructions:

- SME LDR (array vector) and STR (array vector) instructions.
- SME2 LDR (table) and STR (table) instructions.
- SVE LDR (vector) and STR (vector) instructions.
- SVE LDR (predicate) and STR (predicate) instructions.

ISQBCZ

- SME ZERO (tiles) instruction.
- SME2 ZERO (table) instruction.
- SVE DUP (immediate) instruction with zero immediate.
- SVE PFALSE instruction.

For implementations with a shared SMCU, PEs are expected to execute these instructions in a way that experiences a reduced effect of contention for the SMCU from other PEs, compared to other SME and SVE instructions executed in Streaming SVE mode .

## D22.4.1.2 Streaming execution priority control

IRMDCP

The streaming execution priority is controlled by a 4-bit priority value. When the streaming execution priority mechanism is not supported, the priority value is ignored.

IFJQRG

Ahigher priority value corresponds to a higher streaming execution priority. Priority value 15 is the highest priority.

IQHKWP

The behavior of any given priority value relative to that of another PE is IMPLEMENTATION DEFINED.

## D22.4.1.3 Streaming execution priority virtualization

The Effective streaming execution priority is either the value configured in SMPRI\_EL1 or, if EL2 is implemented and enabled in the current Security state, the value of SMPRI\_EL1 mapped into a new value by indexing the fields in SMPRIMAP\_EL2. This choice is affected by the current Exception level, and the HCRX\_EL2.SMPME configuration.