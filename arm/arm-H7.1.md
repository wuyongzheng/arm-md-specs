## H7.1 About the PC Sample-based Profiling Extension

The PC Sample-based Profiling Extension is an OPTIONAL extension that provides coarse-grained, non-invasive profiling by an external debugger. See also Non-invasive behavior.

When the PC Sample-based Profiling Extension is implemented, the PE implements a PC sample register and one or more context sample registers as external registers. Reads of the PC sample register return a PC sample value and capture the PE context in the context sample registers. For example, tools can use these samples to populate a statistical model of the performance of software executing on the PE.

Note

Data returned by periodic sampling of PC Sample-based Profiling registers is sufficient to allow tools to estimate the distribution of time spent executing software on the PE.

The delay between an instruction being executed by the PE and its address appearing in the PC Sample Register is not defined, and the architecture does not require that the sampled instruction was recently executed. For example, if a piece of software executes a load instruction that reads the PC Sample Register of the PE it is running on, there is no guaranteed relationship between the address of the load instruction and the value read. The PC Sample Register is intended only for use by an external agent to provide statistical information for software profiling.

It must be possible to sample references to branch targets. It is IMPLEMENTATION DEFINED whether references to other instructions can be sampled. The branch target for a conditional branch instruction that fails its condition check is the instruction that follows the conditional branch instruction. The branch target for an exception is the exception vector address.

FEAT\_PCSRv8p9 adds a mechanism to suspend PC Sample-based Profiling in systems where:

- It is required to be able to use PC Sample-based Profiling on an ad hoc basis.
- It is required to be able to disable or suspend PC Sample-based Profiling after use.
- It is not acceptable to reset or power down the PE in order to disable or suspend PC Sample-based Profiling.

To keep the implementation and validation cost low, a reasonable degree of inaccuracy in the sampled data is acceptable. Arm does not define a reasonable degree of inaccuracy but recommends the following guidelines:

- In exceptional circumstances, such as a change in Security state or other boundary condition, it is acceptable for the sample to represent an instruction that was not committed for execution.
- Under unusual non-repeating pathological cases, the sample can represent an instruction that was not committed for execution. These cases are likely to occur as a result of asynchronous exceptions, such as interrupts, where the chance of a systematic error in sampling is very unlikely.
- Under normal operating conditions, the sample must reference an instruction that was committed for execution, including its context, and must not reference instructions that are fetched but not committed for execution.
- Controlling the PC Sample-based Profiling Extension.
- Registers implemented by the PC Sample-based Profiling Extension.
- Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN.
- Pseudocode description of PC Sample-based Profiling.

Note

In the Armv7 PC Sample-based Profiling Extension, an offset was applied to the sampled Program Counter value and this offset and the instruction set state indicated in bits [1:0] of the sampled value. From the introduction of the Armv8 PC Sample-based Profiling Extension, the sampled value is the address of an instruction that has executed, with no offset and no indication of the instruction set state.

## H7.1.1 Controlling the PC Sample-based Profiling Extension

PC Sample-based Profiling is controlled by the IMPLEMENTATION DEFINED authentication interface ExternalNoninvasiveDebugEnabled() .

PC Sample-based Profiling is allowed if both of the following apply:

- ExternalNoninvasiveDebugEnabled() == TRUE.
- At least one of the following applies:
- -The PE is executing in Non-secure state.
- -EL3 is not implemented.
- -EL3 is implemented, the PE is executing in Secure state, and

ExternalSecureNoninvasiveDebugEnabled()

== TRUE.

- -The PE is executing in Realm state and ExternalRealmNoninvasiveDebugEnabled() == TRUE.
- -The PE is executing in Root state and ExternalRootNoninvasiveDebugEnabled() == TRUE.
- -EL3 or EL1 is using AArch32, the PE is executing at EL0 in Secure state, and the value of SDER.SUNIDEN is 1.

The state of the IMPLEMENTATION DEFINED authentication interface is visible through DBGAUTHSTATUS\_EL1. See Recommended authentication interface.

## H7.1.1.1 Suspending and activating PC Sample-based Profiling

If FEAT\_PCSRv8p9 is implemented and the value PMPCSCTL.IMP is 1, then all of the following apply:

- When PMPCSCTL.EN is 0, PC Sample-based Profiling is suspended unless otherwise stated.
- When PMPCSCTL.EN is 1, PC Sample-based Profiling is active .

Otherwise, all of the following apply:

- If FEAT\_PCSRv8p9 is not implemented, then PMPCSCTL.EN is RES0.
- The state of PC Sample-based Profiling at Warm reset is an IMPLEMENTATION DEFINED one of suspended or active.

When all of the following apply, reading PMPCSR[31:0] or PMPCSR[63:0] makes PC Sample-based Profiling active:

- PC Sample-based Profiling is suspended.
- PC sampling is allowed.
- Sampling on reads is enabled.

Asubsequent external read of PMPCSR will observe the updated state.

This means that if FEAT\_PCSRv8p9 is implemented and PMPCSCTL.IMP reads as 1, then PMPCSCTL.EN is set to 1 as a side-effect of the read of PMPCSR.

Note

If FEAT\_PCSRv8p9 is implemented and PMPCSCTL.IMP reads as 0, then there is no mechanism to return to suspended state, other than Warm reset.

When FEAT\_PMUv3\_SS is implemented and PMPCSCTL.SS is 1, all the following apply:

- PC Sample-based Profiling is active, regardless of the value of PMPCSCTL.EN, if implemented.
- Sampling on PMU snapshot Capture events is enabled.
- Sampling on reads is disabled.

Otherwise, sampling on PMU snapshot Capture events is disabled, and sampling on reads is enabled.

When sampling on reads is disabled, all of the following apply to reads of PMPCSR:

- The reads have none of the side-effects described in PMPCSR.
- Return the value of the PC when it was last sampled, or the Cold reset value of the register if the PC has not been sampled since the last Cold reset.

For more information on the operation of Capture events, see PMU snapshots.

## H7.1.2 Registers implemented by the PC Sample-based Profiling Extension

The PC Sample-based Profiling Extension is implemented by either FEAT\_PCSRv8 or FEAT\_PCSRv8p2:

- If FEAT\_PCSRv8 is implemented then the PC Sample-based Profiling Extension registers are implemented in the external debug register space. EDDEVID1.PCSample identifies when FEAT\_PCSRv8 is implemented and which PC Sample-based Profiling Extension registers are implemented.
- If FEAT\_PCSRv8p2 is implemented then the PC Sample-based Profiling Extension registers are implemented in the Performance Monitors memory-mapped register space. PMDEVID.PCSample identifies when FEAT\_PCSRv8p2 is implemented.

An implementation is not permitted to include both FEAT\_PCSRv8 and FEAT\_PCSRv8p2. FEAT\_PCSRv8 is not permitted from Armv8.2.

If FEAT\_PCSRv8 is implemented:

- The following external debug registers can be implemented:
- -EDCIDSR.
- -EDPCSR.
- -EDVIDSR.

See External debug interface registers.

- If FEAT\_VHE is implemented, EDSCR.SC2 controls what PC Sample-based Profiling samples.

If FEAT\_PCSRv8p2 is implemented and the 64-bit external PMU programmers' model extension is not implemented, the following PC Sample-based Profiling Extension registers can be implemented in the Performance Monitors memory-mapped register space:

- PMCID1SR and PMCID2SR.
- PMPCSR.
- PMVIDSR.

When the 64-bit external PMU programmers' model extension is implemented, the PC Sample-based Profiling Extension registers are:

- PMCCIDSR.
- PMPCSR.
- PMVCIDSR.

See Performance Monitors external register views.

If FEAT\_PCSRv8p2 is implemented but the Performance Monitors Extension is not implemented, then the PC Sample-based Profiling Extension registers are implemented in their own memory-mapped register space, within the area that is reserved for the Performance Monitors, see Table H7-1. If CoreSight compliance is required:

- The management registers are defined as in Table K5-4.
- The support for PC Sample-based profiling is defined in the following registers:
- -PMDEVTYPE.MAJOR has the value 0x0 .
- -PMDEVARCH.ARCHID has the value 0x0A10 or 0x0A20 .

For more information, see PMDEVARCH.

Table H7-1 PC Sample-based Profiling register map without the Performance Monitors Extension

| Offset        | Description                                     |
|---------------|-------------------------------------------------|
| 0x200         | PMPCSR[31:0]                                    |
| 0x204         | PMPCSR[63:32]                                   |
| 0x208         | PMCID1SR                                        |
| 0x20C         | PMVIDSR                                         |
| 0x220         | PMPCSR[31:0] (alias)                            |
| 0x224         | PMPCSR[63:32] (alias)                           |
| 0x228         | PMCID1SR (alias)                                |
| 0x22C         | PMCID2SR                                        |
| 0x600 - 0x6FC | IMPLEMENTATION DEFINED                          |
| 0xE80 - 0xEFC | IMPLEMENTATION DEFINED for CoreSight compliance |
| 0xFF0 - 0xFFc | Management and CoreSight compliance registers   |

## H7.1.3 Permitted behavior that might make the PC Sample-based profiling registers UNKNOWN

The architecture permits IMPLEMENTATION DEFINED extensions to external debug to define mechanisms that make the values of the PC Sample-based profiling registers UNKNOWN. However, it requires that any such mechanism is disabled by default. This means that powerup or a hard reset of the PE must leave the PE in a state where the PC Sample-based Profiling Extension, if implemented, exhibits its architecturally-defined behavior.

Note

A mechanism that, when enabled, makes the PC Sample-based profiling registers UNKNOWN might use other samplebased profiling events that are appropriate for a use that is independent of PC Sample-based Profiling.

If no branch instruction has been retired since the PE left Debug state, suspended state, or a state where PC Sample-based profiling is prohibited, then the sampled value is UNKNOWN.

If all of the following apply, then a read of PMPCSR[31:0] or PMPCSR[63:0] is permitted but not required to return 0xFFFF\_FFFF for PMPCSR[31:0].

- The PE has not retired any branch instruction since leaving a state where PC Sample-based Profiling was suspended.
- Sampling on reads is not disabled.

This includes a read of PMPCSR[31:0] or PMPCSR[63:0] that indirectly makes PC Sample-based Profiling active.

When FEAT\_MOPS and FEAT\_PCSRv8p2 are not implemented, if no branch instruction has been retired since the last read of PMPCSR[31:0], then the value of PMPCSR[31:0] is UNKNOWN.

## H7.1.4 Pseudocode description of PC Sample-based Profiling

When FEAT\_PCSRv8 is implemented, the functionality is described by the pseudocode functions:

- CreatePCSample() , which populates a variable of type PCSample .
- Read\_EDPCSRlo[] , which writes a PC sample to the EDPCSR and associated registers.

When FEAT\_PCSRv8p2 is implemented, the functionality is described by the pseudocode functions:

- CreatePCSample() , which populates a variable of type PCSample .
- Read\_PMPCSR[] , which writes a PC Sample to the PMPCSR and associated registers.

## Chapter H8 About the External Debug Registers

This chapter provides some additional information about the external debug registers. It contains the following sections:

- Relationship between external debug and System registers.
- Endianness and supported access sizes.
- Synchronization of changes to the external debug registers.
- Memory-mapped accesses to the external debug interface.
- External debug interface register access permissions.
- External debug interface registers.
- Cross-trigger interface registers.
- External debug register resets.

Note

Where necessary, Table K14-1 disambiguates the general register references used in this chapter.