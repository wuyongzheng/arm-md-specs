## D19.5 Programmers' model

| R BNGTH   | Reads from an unimplemented Branch record return the value zero.                                                                                                                                                                                                                                                                       |
|-----------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R PKZCF   | All Branch records captured while generation of Branch records is not paused, must represent a continuous block of execution for all BRBE Non-prohibited regions.                                                                                                                                                                      |
| I XSBPR   | The captured Branch records might not represent a continuous block if generation of Branch records is paused at any time. To avoid this non-continuous nature, the BRB IALL instruction can be used to invalidate all Branch records while generation is paused.                                                                       |
| R PMRRL   | If a Branch record cannot be captured for a branch instruction or exception that is not prohibited and has been selected to generate a record, then all the Branch records must be invalidated. The reasons for a PE being unable to capture a Branch record are IMPLEMENTATION DEFINED and Arm recommends that such reasons are rare. |
| I QJFSV   | When a process is migrated to a PE with a smaller number of Branch records implemented then the information from the older Branch records will be lost.                                                                                                                                                                                |
| I BDKJJ   | When FEAT_BRBE is implemented, the following fields are provided in System registers to control access to the Branch record buffer functionality:                                                                                                                                                                                      |

- When EL2 is implemented:
- -HDFGRTR\_EL2.nBRBIDR.
- -HDFGRTR\_EL2.nBRBCTL.
- -HDFGWTR\_EL2.nBRBCTL.
- -HDFGRTR\_EL2.nBRBDATA.
- -HDFGWTR\_EL2.nBRBDATA.
- -HFGITR\_EL2.nBRBINJ.
- -HFGITR\_EL2.nBRBIALL.
- When EL3 is implemented:
- -MDCR\_EL3.SBRBE.

When self-hosted EL3 branch recording is enabled, the following registers must be programmed:

- BRBCR\_EL1 and BRBCR\_EL2. Software must program these registers to control the following:
- -Recording of exceptions taken to EL1 and EL2.
- -Recording of exception returns from EL1 and EL2.
- -Branch recording at EL0, EL1, and EL2.
- -Occurrence of BRBE freeze events on PMU overflows.
- -Timestamp source.
- -Misprediction information.
- -Cycle count information.
- BRBFCR\_EL1. Software must program this register to control the following:
- -Selection of Branch record buffer bank.
- -Selection of branch types to record at all Exception levels.
- -Pausing of Branch recording.

Software should also consider how MDCR\_EL3.SBRBE should be programmed to either allow or prohibit access to the captured branch records from lower Exception levels. Even if self-hosted EL3 branch recording is not being used, software should consider whether a BRB IALL instruction should be executed before executing software at lower Exception levels.

Software must invalidate the Branch records after a PE reset to ensure that details of execution before the reset event are not leaked.

MDCR\_EL3.E3BREC resets to 0 on a Cold reset, and MDCR\_EL3.E3BREW resets to 0 on a Warm reset. This allows software to program MDCR\_EL3.E3BREC and MDCR\_EL3.E3BREW such that the BRBE continues recording after Warm reset, or stops recording at Warm reset.

When FEAT\_BRBEv1p1 is implemented, certain fields in the following registers are reset to an architecturally UNKNOWN value on a Cold reset and unchanged on a Warm reset:

SGCYTK

SYLMQQ

IFPJPQ

INZMWQ

- BRBCR\_EL1.
- BRBCR\_EL2.
- BRBFCR\_EL1.

## D19.5.1 Manual injection of Branch records

| I DXNLX   | The Branch Record Buffer Extension supports the ability to manually create Branch records and inject them in to the Branch record buffer storage. The primary purpose of the injection functionality is to support the restore of the Branch record buffer storage contents, particularly during software context switch events, including migration of software between PEs. The Branch record buffer storage contents are read out using direct reads of BRBSRC<n>_EL1, BRBTGT<n>_EL1, and BRBINF<n>_EL1.   |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R FYXNL   | The Branch Record Injection data registers are: • BRBSRCINJ_EL1. • BRBTGTINJ_EL1. • BRBINFINJ_EL1.                                                                                                                                                                                                                                                                                                                                                                                                            |
| I FJHMP   | Branch record injection consists of creating a single Branch record using direct writes to the Branch Record Injection data registers, then injecting the record into the Branch record buffer storage using BRB INJ . This process injects a single Branch record as the youngest entry in the Branch record buffer storage. This process is repeated for each Branch record to be added to the Branch record buffer storage.                                                                                |
| I BCZRK   | When BRB INJ is executed outside of a BRBE Prohibited region, it is CONSTRAINED UNPREDICTABLE whether a Branch record is injected and it is CONSTRAINED UNPREDICTABLE whether the cycle count value in the next Branch record to be generated is Branch cycle count unknown.                                                                                                                                                                                                                                  |
| R XVDNN   | When BRB INJ is executed inside a BRBE Prohibited region, the contents of the Branch Record Injection data registers are used to create a Branch record which is added to the Branch record buffer storage as the youngest entry.                                                                                                                                                                                                                                                                             |
| R SMBVK   | When a BRB INJ instruction is executed inside a BRBE Prohibited region and the contents of the Branch Record Injection data registers indicates an invalid record, it is CONSTRAINED UNPREDICTABLE whether a Branch record is injected to the Branch record buffer. An invalid record is one with BRBINFINJ_EL1.VALID set to 0b00 .                                                                                                                                                                           |
| R HNCSX   | For a BRB INJ instruction, it is CONSTRAINED UNPREDICTABLE whether a Branch record is injected to the Branch record buffer when all of the following are true: • The BRB INJ instruction is executed inside a BRBE Prohibited region. • The contents of the Branch Record Injection data registers indicates a valid record. • The other contents of the Branch Record Injection data registers indicate an incorrectly formatted record.                                                                     |
| I JLVPS   | An example of an incorrectly formatted record is one where BRBINFINJ_EL1.VALID is 0b01 and BRBINFINJ_EL1.MPRED is 0b1 .                                                                                                                                                                                                                                                                                                                                                                                       |
| R PWKFJ   | Execution of BRB INJ does not require explicit synchronization to use the result of direct writes to the Branch Record Injection data registers in program order before BRB INJ .                                                                                                                                                                                                                                                                                                                             |
| I TVDMK   | The creation of a Branch record as a result of execution of BRB INJ does not use the result of direct writes to the Branch Record Injection data registers in program order after BRB INJ . Explicit synchronization is not required to ensure this ordering. For more information, see Synchronization requirements for AArch64 System registers.                                                                                                                                                            |
| R LKDTJ   | After the execution of BRB INJ , the contents of the Branch Record Injection data registers are UNKNOWN.                                                                                                                                                                                                                                                                                                                                                                                                      |
| I CPBKF   | Changes to the BRBregisters are subject to the rules for synchronization for System registers. See Synchronization requirements for AArch64 System registers.                                                                                                                                                                                                                                                                                                                                                 |

## Chapter D20 RAS PE Architecture

This chapter describes the RAS Extension PE Architecture. It contains the following sections:

- About the RAS Extension.
- PE error handling.
- Generating error exceptions.
- Taking error exceptions.
- Error synchronization event.
- Virtual SError exceptions and delegated SError exceptions.
- Error records in the PE.