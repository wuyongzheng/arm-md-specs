## 7.1 Command queue errors

The Command queue entry formats are described in Chapter 4 Commands , which defines what is considered to be a valid command. Commands are consumed in-order and when a command error or command fetch abort is detected:

- Command consumption stops.
- Older commands (prior to the erroneous command in the queue) have been consumed.

Note: By definition, earlier commands must have been consumed for a later invalid command to be indicated using CMDQ\_CONS.

Note: See also section 4.8 Command Consumption summary .

- SMMU\_(*\_)CMDQ\_CONS.RD remains pointing to the erroneous command in the Command queue. The CONS index is not permitted to increment in the case where a command fetch experiences an external abort, meaning that external aborts on command read are synchronous.
- The SMMU\_(*\_)CMDQ\_CONS.ERR field is updated to provide an error code.
- The global Command queue Error is triggered: SMMU\_(*\_)GERROR.CMDQ\_ERR is activated (indicating that SMMU\_(*\_)CMDQ\_CONS.ERR has been updated). Commands are not consumed from the affected queue while this error is active, see 7.5 Global error recording and SMMU\_GERROR.
- Commands newer than the erroneous command have no effect, and if they have been fetched they are discarded.

Note: A GPC fault on a Command queue is reported here as an external abort. See 3.25.5 SMMU behavior if a GPC fault is active for details on how other aspects of the GPC fault are reported.

Arm recommends that software rectifies the cause of the command error, then restarts command processing by acknowledging the CMDQ\_ERR by writing an appropriate value to SMMU\_(*\_)GERRORN. Software is not required to write SMMU\_(*\_)CMDQ\_PROD to re-trigger command processing.

While the error is active, additional commands might be submitted and CMDQ\_PROD might be moved backwards as far as the CMDQ\_CONS position so that previously-submitted but non-consumed commands are removed from the queue. This is the only condition in which it is permissible to change CMDQ\_PROD in a manner that is not an increment/wrap while the queue is enabled, see section 3.21.2 Queues .

Commands at or after the CMDQ\_CONS.RD position are fetched or re-fetched after command processing is restarted by acknowledging CMDQ\_ERR.

Note: A Command queue error is completely recoverable and, when the erroneous command is fixed or replaced with a valid command, consumption can be restarted. Older commands are unaffected by a later Command queue error. It is acceptable for software to change the contents of the erroneous command and newer commands while the error is active, as such commands are re-fetched when command processing is restarted.

The SMMU\_(*\_)CMDQ\_CONS.ERR field is updated with the error reason code after detecting a command error. The error reason code is made visible to software before the SMMU makes the global error visible.

Note: It is not possible for software to observe that an error has occurred through GERROR without being able to observe the error code.

Note: If software polls SMMU\_(*\_)CMDQ\_CONS waiting for prior commands to complete, Arm recommends that GERROR.CMDQ\_ERR is also be checked to avoid an infinite loop in the event of a command error.

A Command queue error can be raised for the following reasons:

| SMMU_(*_)CMDQ_CONS.ERR value   | Error name   | Cause                                                                                                    |
|--------------------------------|--------------|----------------------------------------------------------------------------------------------------------|
| 0x00                           | CERROR_NONE  | No error. This value is defined for completeness only, and is not provided by the SMMUin any error case. |

| SMMU_(*_)CMDQ_CONS.ERR value   | Error name          | Cause                                                                                                                                                                                                                                                                                                                                                                                                        |
|--------------------------------|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0x01                           | CERROR_ILL          | Command illegal and cannot be correctly consumed because of an: • Unknown command opcode, including architecture-defined commands irrelevant to an implementation without certain feature or Security state. For example, stage 1 invalidation commands on an SMMUwithout stage 1, Secure invalidation commands from the Non-secure command queue. • Command valid but Reserved field or invalid value used. |
| 0x02                           | CERROR_ABT          | Abort on command fetch: an external abort was returned for a read of the command queue, if an interconnect can detect and report such an event.                                                                                                                                                                                                                                                              |
| 0x03                           | CERROR_ATC_INV_SYNC | A CMD_SYNC failed to successfully complete one or more previous CMD_ATC_INV commands. This is the result of an ATS Invalidation Completion timeout. See section 3.9.1.4 ATS Invalidation timeout .                                                                                                                                                                                                           |