## D19.1 About the Branch Record Buffer Extension

ILQHFJ

The Branch Record Buffer Extension provides control path information for compiling and optimizing software. These directed optimizations extract information about hotspots and common control paths in the code.

FEAT\_BRBE provides a mechanism for capturing control path history in a low-cost manner.

FEAT\_BRBEv1p1 extends FEAT\_BRBE to enable branch recording at EL3.

## D19.1.1 Branch records

| I JBTBH   | Each Branch record consists of 3 registers: • BRBINF<n>_EL1. • BRBSRC<n>_EL1.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I GBCQW   | Taken branch instructions, as defined by Branches, Exception generating, and System instructions, generate a Branch record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| I LFVJR   | Exceptions generate a Branch record.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| R RPVXK   | A Half-source Branch record has BRBINF<n>_EL1.VALID set to 0b10 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| R LPLYK   | A Half-target Branch record has BRBINF<n>_EL1.VALID set to 0b01 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| R GSMRH   | A Full Branch record has BRBINF<n>_EL1.VALID set to 0b11 .                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| R XRHTY   | BRBINF<n>_EL1.VALID indicates the validity of a Branch record: • If BRBINF<n>_EL1.VALID is 0b00 , the Branch record is invalid. • Otherwise, the Branch record is valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| R MLGCF   | When a Branch record is generated for any branch or exception which does not transition between a BRBE Prohibited region and a BRBE Non-prohibited region, the Branch record is a Full Branch record . See Branch records for exceptions and Branch records for exception returns for more details on when a Half-source Branch record or a Half-target Branch record is generated.                                                                                                                                                                                                                                                                                                                                                            |
| I ZCHRF   | When an Instruction Synchronization Barrier instruction causes a Context synchronization event which synchronizes an update to one or more System registers which are indirectly read when generating a Branch record, the synchronization of those register updates occurs before the registers are indirectly read. Such order is generally consistent with indirect reads of System registers performed by events which cause a Context synchronization event.                                                                                                                                                                                                                                                                              |
| R ZHDCC   | When an exception or exception return instruction causes a Context synchronization event which synchronizes an update to one or more System registers which are used to determine whether the source of the Branch record is from a BRBE Prohibited region, indirect reads of those System registers are permitted to occur before the Context synchronization event. Specifically, the registers indirectly read by BranchRecordAllowed().All other indirect reads of System registers used for creation of a Branch record occur after the Context synchronization event, including those for determining whether the Branch record is filtered or not, and those used for determining whether Branch recording is prohibited at the target. |
| R TWYWS   | Where an operation such as an exception or exception return causes a Context synchronization event and that synchronizes a System register update which permits a BRBE freeze event to occur, and the same operation also changes the PE state to prevent a BRBE freeze event from occurring, it is IMPLEMENTATION SPECIFIC whether the BRBE freeze event occurs.                                                                                                                                                                                                                                                                                                                                                                              |
| R CBHRY   | The reason for the Branch record is captured in BRBINF<n>_EL1.TYPE.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |

## D19.1.2 Cycle counting

IRRBFF

Each Branch record contains a cycle count value which is representative of the time taken between each Branch record being generated. The cycle count value can be used to determine the relative performance of the program between each Branch record. For large cycle count values, the value stored in each Branch record is encoded to use less storage, with a small loss of precision in the value.

RHQXNW The size of the cycle counter used to generate cycle count values is IMPLEMENTATION DEFINED, from one of the sizes indicated in BRBIDR0\_EL1.CC.

RKVRBB

Each Branch record contains a cycle count value which indicates the number of PE clock cycles that occurred between the previous Branch record being generated and this Branch record being generated.

RSBXCF In a multithreaded implementation, the cycle counter only counts cycles on which the thread was active.

IVPPYW

The Branch record counts cycles in the same way as the CPU\_CYCLES PMU event counts cycles when PMEVTYPER&lt;n&gt;\_EL0.MT is 0. For more information, see Cycle event counting.

RPGXMB For the purposes of the cycle count, a Branch record is generated only when the corresponding branch instruction or exception is guaranteed to be architecturally executed and the target address has been calculated. Arm recommends that the Branch record is generated as soon after this point as possible.

IKBDLR When a branch target address contains an address tag, the target address captured in the Branch record is the virtual address with the address tag removed.

RMJDLC

RPBJTJ

RXGSSZ

RJZWPG

The cycle count value in a Branch record is Branch cycle count unknown when any of the following are true:

- If EL2 is implemented, BRBCR\_EL2.CC is 0.
- BRBCR\_EL1.CC is 0.
- This is the first Branch record after the PE exited a BRBE Prohibited region.
- This is the first Branch record after cycle counting has been enabled.
- This is the first Branch record after BRBFCR\_EL1.PAUSED is cleared from 1 to 0.
- This is the first Branch record after execution of a BRB IALL instruction.

Note

This applies even when EL2 is disabled in the current Security state.

When the cycle count value in a Branch record is Branch cycle count unknown:

- BRBINF&lt;n&gt;\_EL1.CCU has the value 1.
- BRBINF&lt;n&gt;\_EL1.CC contains a value which is all zeros.

The number of cycles indicated by this Branch record is UNKNOWN.

If the cycle count value in a Branch record would exceed the maximum value of the cycle counter, then:

- BRBINF&lt;n&gt;\_EL1.CCU has the value 0.
- BRBINF&lt;n&gt;\_EL1.CC contains a value which is all ones.

If the cycle count value in a Branch record is not UNKNOWN and would not exceed the maximum value of the cycle counter, then:

- BRBINF&lt;n&gt;\_EL1.CCU has the value 0.
- BRBINF&lt;n&gt;\_EL1.CC contains the cycle count value, encoded as defined in BRBINF&lt;n&gt;\_EL1.CC.

## D19.1.3 Mispredicted branches

IQHGFW

Each Branch record generated for a branch instruction contains an indication of whether the branch was correctly or incorrectly predicted by the PE. Branch prediction behavior is IMPLEMENTATION DEFINED and this is an indication of whether such prediction succeeded, or not.

RXHWRB

For a Branch record of a branch instruction, one of the following occurs:

RDHNPJ

RLBRGV

RRDLQF

- If EL2 is implemented and BRBCR\_EL2.MPRED is 0, then BRBINF&lt;n&gt;\_EL1.MPRED is set to 0.
- Else if BRBCR\_EL1.MPRED is 0, then BRBINF&lt;n&gt;\_EL1.MPRED is set to 0.
- Otherwise:
- -BRBINF&lt;n&gt;\_EL1.MPRED is 0 for a correctly predicted branch.
- -BRBINF&lt;n&gt;\_EL1.MPRED is 1 for an incorrectly predicted branch.

Note: This applies even when EL2 is disabled in the current Security state.

For a Branch record of an exception, BRBINF&lt;n&gt;\_EL1.MPRED has the value 0.

An incorrectly predicted branch is when any of the following is true:

- The direction of a conditional branch was incorrectly predicted at least once during the execution of the instruction.
- The target of a branch was incorrectly predicted at least once during the execution of the instruction.
- The branch was not predicted by a branch predictor.

Acorrectly predicted branch is one that is not incorrectly predicted.

## D19.1.4 BRBE Prohibited regions

INVWPM

An executable program might contain regions of code that are prohibited to generate Branch records, and these regions are called BRBE Prohibited regions. These regions are usually associated with a different Security state or Exception level.

IDMPQZ

IHPZWM

RFHGJN

RLPYBQ

RJWWFY

RGLKGW

RSFZQD

RYPHYG

BRBE Prohibited regions are controlled by the following:

- BRBCR\_EL1.E0BRE.
- BRBCR\_EL1.E1BRE.
- BRBCR\_EL2.E0HBRE.
- BRBCR\_EL2.E2BRE.
- MDCR\_EL3.SBRBE.

While executing outside a BRBE Prohibited region, Branch records might not be generated because the Branch Record Buffer Extension has a number of filtering functions.

Execution in AArch32 state is a BRBE Prohibited region.

Execution in Debug state is a BRBE Prohibited region.

When FEAT\_BRBEv1p1 and EL3 are implemented:

- When MDCR\_EL3.{E3BREC, E3BREW} is { 0b0 , 0b1 } or MDCR\_EL3.{E3BREC, E3BREW} is { 0b1 , 0b0 }, self-hosted EL3 branch recording is enabled.
- When MDCR\_EL3.{E3BREC, E3BREW} is { 0b0 , 0b0 } or MDCR\_EL3.{E3BREC, E3BREW} is { 0b1 , 0b1 }, self-hosted EL3 branch recording is disabled.

Execution at EL3 is a BRBE Prohibited region when any of the following are true:

- FEAT\_BRBEv1p1 is not implemented.
- Self-hosted EL3 branch recording is disabled.

Execution at EL2 is a BRBE Prohibited region when any of the following are true:

- BRBCR\_EL2.E2BRE is 0.
- MDCR\_EL3.SBRBE is 0b00 .
- MDCR\_EL3.SBRBE is 0b01 and the PE is in Secure state.

Execution at EL1 is a BRBE Prohibited region when any of the following are true:

- BRBCR\_EL1.E1BRE is 0.
- MDCR\_EL3.SBRBE is 0b00 .

RDBPCP

RYGGSC

- MDCR\_EL3.SBRBE is 0b01 and the PE is in Secure state.

Execution at EL0 is a BRBE Prohibited region when any of the following are true:

- EL2 is disabled in the current Security state or HCR\_EL2.TGE is 0, and BRBCR\_EL1.E0BRE is 0.
- EL2 is enabled in the current Security state and HCR\_EL2.TGE is 1, and BRBCR\_EL2.E0HBRE is 0.
- MDCR\_EL3.SBRBE is 0b00 .
- MDCR\_EL3.SBRBE is 0b01 and the PE is in Secure state.

While the PE is executing code from a BRBE Prohibited region, no data is captured in Branch records that might provide information about execution in the BRBE Prohibited region.

## D19.1.5 Branch records for exceptions

RYSKQK

When an exception is taken from a BRBE Prohibited region to a BRBE Prohibited region, no Branch record is generated.

RKRJQC

RYBJDJ

When an exception is taken from a BRBE Non-prohibited region, or an exception is taken to a BRBE Non-prohibited region:

- If the target Exception level is EL1, a Branch record is generated only if BRBCR\_EL1.EXCEPTION is 1.
- If the target Exception level is EL2, a Branch record is generated only if BRBCR\_EL2.EXCEPTION is 1.
- If the target Exception level is EL3, a Branch record is generated only if FEAT\_BRBEv1p1 is implemented and self-hosted EL3 branch recording is enabled.

When a Branch record is generated for an exception:

- If the exception is taken from a BRBE Prohibited region, then a Half-target Branch record is generated.
- If the exception is taken from a BRBE Non-prohibited region to a BRBE Prohibited region, then a Half-source Branch record is generated.
- If the exception is taken from a BRBE Non-prohibited region to a BRBE Non-prohibited region, then a Full Branch record is generated.

## RLLCTG When entering Debug state:

- If the entry is from a BRBE Prohibited region, no Branch record is generated.
- If the entry is from a BRBE Non-prohibited region, then a Half-source Branch record is generated.

When a Half-source Branch record or a Full Branch record is generated for an Illegal Execution state exception, the source information in the Branch record indicates where the exception was taken from, in the same way as all other exceptions.

ABranch record for an exception which contains a valid source address has the source address set to the preferred exception return address for the exception.

IMZNRY

RBZCRW

RFYLTC

ABranch record for an exception which contains a valid target address has the target address set to the address of the exception vector.

## D19.1.6 Branch records for exception returns

RLMXHS

When an exception return instruction is executed in a BRBE Prohibited region and branches to a BRBE Prohibited region, no Branch record is generated.

RZSHDL

When an exception return instruction is executed in a BRBE Non-prohibited region, or an exception return instruction branches to a BRBE Non-prohibited region:

- If the exception return instruction is executed at EL3, a Branch record is generated only if FEAT\_BRBEv1p1 is implemented and self-hosted EL3 branch recording is enabled.
- If the exception return instruction is executed at EL2, a Branch record is generated only if BRBCR\_EL2.ERTN is 1.
- If the exception return instruction is executed at EL1, a Branch record is generated only if BRBCR\_EL1.ERTN is 1.

RZTGMW

RRBCFP

INGWPR

IJCYHD

When a Branch record is generated for an exception return instruction:

- If the exception return instruction is executed in a BRBE Prohibited region, then a Half-target Branch record is generated.
- If the exception return instruction is executed in a BRBE Non-prohibited region and branches to a BRBE Prohibited region, then a Half-source Branch record is generated.
- If the exception return instruction is executed in a BRBE Non-prohibited region and branches to a BRBE Non-prohibited region, then a Full Branch record is generated.

When exiting from Debug state:

- If the exit is to a BRBE Prohibited region, no Branch record is generated.
- If the exit is to a BRBE Non-prohibited region, then a Half-target Branch record is generated.

When a Half-target Branch record or a Full Branch record is generated for an exception return instruction which is an illegal return or a legal return which sets PSTATE.IL to 1, the target information in the Branch record indicates the target of the branch:

- BRBTGT&lt;n&gt;\_EL1.ADDRESS contains the target of the branch.
- BRBINF&lt;n&gt;\_EL1.EL contains the value that is loaded in to PSTATE.EL.

When a Half-target Branch record or a Full Branch record is generated for an exception return instruction which is an illegal return or a legal return which sets PSTATE.IL to 1, for the purposes of determining whether the target is a BRBE Prohibited region the value that is loaded in to PSTATE.EL is used as the target Exception level.

PSTATE.EL is unchanged on an illegal return, so the current Exception level is the target of the illegal return, regardless of where the return was attempting to return to.

## D19.1.7 The Branch Record Buffer Extension and the Transactional Memory Extension

| R GVCJH   | When an entire transaction is executed in a BRBE Non-prohibited region and the transaction fails or is canceled then BRBFCR_EL1.LASTFAILED is set to 1.                                                                                                     |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R JMSZF   | When an entire transaction is executed in a BRBE Prohibited region and the transaction fails or is canceled then BRBFCR_EL1.LASTFAILED is unchanged.                                                                                                        |
| R CBTBH   | When a transaction is executed partially in a BRBE Prohibited region and partially in a BRBE Non-prohibited region and the transaction fails or is canceled then it is CONSTRAINED UNPREDICTABLE whether BRBFCR_EL1.LASTFAILED is set to 1 or is unchanged. |
| R KBSZM   | When a Branch record is generated, other than through the injection mechanism, the value of BRBFCR_EL1.LASTFAILED is copied to the LASTFAILED field in the Branch record and BRBFCR_EL1.LASTFAILED is set to 0.                                             |
| I HJZWG   | When a transaction fails or is canceled, a Branch record is not generated.                                                                                                                                                                                  |
| I JBPHS   | When a transaction fails or is canceled, Branch records generated in the transaction are not removed from the Branch record buffer.                                                                                                                         |
| I TFKNW   | Attempting to execute the BRB IALL or BRB INJ instructions in Transactional state results in the transaction failing with ERR cause.                                                                                                                        |

## D19.1.8 PE speculation

RKXTKS

The Branch records only contain information for a branch, exception, or exception return that is architecturally executed.