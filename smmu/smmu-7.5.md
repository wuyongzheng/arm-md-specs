## 7.5 Global error recording

Global Errors pertaining to a programming interface are reported into the appropriate SMMU\_(*\_)GERROR register instead of into the memory-based Event queue.

SMMU\_(*\_)GERROR provides a one-bit flag for each of the following error conditions:

| Error flag         | Meaning                                                                                                                                                                                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMDQ_ERR           | Command queue error                                                                                                                                                                                                                                                                                                                                        |
| EVENTQ_ABT_ERR     | Event queue access aborted Delivery into the Event queue stops when an abort is flagged, see section 7.2 Event queue recorded faults and events .                                                                                                                                                                                                          |
| PRIQ_ABT_ERR       | PRI queue access aborted Delivery into the PRI queue stops when an abort is flagged, see section 8.2 Miscellaneous .                                                                                                                                                                                                                                       |
| MSI_CMDQ_ABT_ERR   | CMD_SYNC MSI write aborted                                                                                                                                                                                                                                                                                                                                 |
| MSI_EVENTQ_ABT_ERR | Event queue MSI write aborted                                                                                                                                                                                                                                                                                                                              |
| MSI_PRIQ_ABT_ERR   | PRI queue MSI write aborted (Non-secure GERROR only)                                                                                                                                                                                                                                                                                                       |
| MSI_GERROR_ABT_ERR | GERROR MSI write aborted                                                                                                                                                                                                                                                                                                                                   |
| SFM_ERR            | SMMUentered Service Failure Mode This error is common to both SMMU_GERROR and SMMU_S_GERROR, so that both Secure and Non-secure software are aware that the SMMUhas entered SFM.                                                                                                                                                                           |
| CMDQP_ERR          | Command queue control page error This error signals that there was an error while fetching or processing a command related to an ECMDQ instance. The presence of the error is also indicated in SMMU_ECMDQ_CONSn.ERR and the reason for the error is available in SMMU_ECMDQ_CONSn.ERR_REASON. See section 3.5.6.3 Errors relating to an ECMDQ interface . |
| DPT_ERR            | DPT Lookup fault This error indicates that one or more DPT lookup faults have occurred. The syndrome information is available in SMMU_(R_)DPT_CFG_FAR. See section 3.24.4 DPT lookup errors .                                                                                                                                                              |

When an error condition is triggered, the error is activated by toggling the corresponding flag in GERROR. In some cases, SMMU behavior changes while the error is active:

· Commands are not consumed from the Command queue while CMDQ\_ERR is active.

The presence of a Global Error is acknowledged by the agent controlling the SMMU by toggling the equivalent field in the GERRORN register.

An error is active when: SMMU\_(*\_)GERROR[x] != SMMU\_(*\_)GERRORN[x]

The SMMU does not toggle bit[x] if the error is already active. If one or more new errors occur while a previous error of the same type is active, the new error is not logged.

Note: This handshake avoids a race condition that could otherwise lead to loss of error events. It follows that an error flag indicates that one or more of the indicated errors has occurred since the last acknowledgment.

It is IMPLEMENTATION DEFINED whether the interconnect to the memory system of an implementation returns abort completions for writes, which lead to *\_ABT\_ERR global errors.

Note: A GPC fault can also result in reporting of *\_ABT\_ERR global errors. See 3.25.5 SMMU behavior if a GPC fault is active for details on how other aspects of the GPC fault are reported.

## 7.5.1 GERROR interrupt notification

A GERROR interrupt is triggered when the SMMU activates an error, with the exception of the following fields:

- MSI\_GERROR\_ABT\_ERR
- -Note: This error signifies that a prior attempt to raise a GERROR MSI had been aborted, and sending another to the same address might cause a second abort.

The GERROR interrupt is triggered only when SMMU\_(*\_)IRQ\_CTRL.GERROR\_IRQEN == 1. When MSIs are used, GERROR MSI notification is configured using SMMU\_(*\_)GERROR\_IRQ\_CFG{0,1,2}. If multiple errors activate at the same time, GERROR interrupts are permitted to be coalesced.

Where the architecture guarantees that a GERROR flag update is visible before the completion of an action that might have triggered an error, completion of such an action is not required to depend on the GERROR interrupt having been made visible.

Note: For example, an IRQ enable update from 1 to 0 does not complete until the abort of a prior MSI is recorded as GERROR.MSI\_*\_ABT\_ERR, but the update is permitted to complete before the GERROR interrupt is triggered.