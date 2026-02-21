## 4.7 Fault response and synchronization commands

## 4.7.1 CMD\_RESUME(StreamID, SSec, STAG, Action, Abort)

<!-- image -->

Resumes processing of the stalled transaction identified with the given StreamID and STAG parameter, with the given action parameter, Ac:

| Action (Ac)   | Result                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |
|---------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 1             | Transaction is retried as though it had just arrived at the SMMU. Configuration and translations are                                                                                                                                                                                                                                                                                                                                                                                                  |
| (Retry)       | looked up, it might then progress into the system or fault again.                                                                                                                                                                                                                                                                                                                                                                                                                                     |
|               | The Abort parameter, Ab, is IGNORED.                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| 0:(Terminate) | Transaction is terminated in the manner given by the Abort parameter, Ab. When Ab == 0, the transaction is completed successfully with RAZ/WI semantics. When Ab == 1, an abort/bus error is reported to client.                                                                                                                                                                                                                                                                                      |
|               | If SMMU_IDR0.TERM_MODEL == 1, the Ab parameter is IGNORED: transaction is terminated with abort.                                                                                                                                                                                                                                                                                                                                                                                                      |
|               | Note: The Abort parameter is analogous to the CD.A configuration for non-stalled terminated transactions.                                                                                                                                                                                                                                                                                                                                                                                             |
|               | In response to a transaction experiencing a stage 2 fault, the STE configuration provides only two behaviors, whether the transaction is terminated by abort or becomes stalled, but a subsequent CMD_RESUME for the stall will (if supported, as indicated by SMMU_IDR0.TERM_MODEL) allow the stalled transaction to be terminated with RAZ/WI behavior. There is no dependency between STE.S2S and the behavior of the CMD_RESUME, and the Terminate parameter is not limited by STE configuration. |

When issued on an SMMU implementation that does not support the Stall model (or where the Stall model has been disabled with NSSTALLD for the Security state of the Command queue), indicated by SMMU\_(*\_)IDR0.STALL\_MODEL == 0b01 , a CERROR\_ILL is raised.

The STAG parameter is an opaque token that must be supplied exactly as provided in the corresponding fault event record from which the existence of the stalled transaction is determined.

The common behaviors for SSec apply. See 4.1.6 Common command fields .

Note: A CMD\_RESUME issued from the Non-secure Command queue does not affect a stalled transaction that originated from a Secure StreamID.

An SMMU must:

- Use the StreamID, SSec and STAG to locate the specific stalled transaction to be resumed.
- Differentiate individual transactions in the case of multiple stalled transactions from the same StreamID.
- Verify that a STAG value corresponds to the given StreamID.

If this command is issued with a STAG value that does not correspond to any stalled transaction, or if the transaction does not match the given StreamID, this command has no effect on any transaction (it is effectively a no-op). This can occur in any of these cases:

- There are no stalled transactions from the given StreamID.
- STAG indicates an SMMU resource that is not holding a stalled transaction.
- The STAG indicates an SMMU resource that does hold a stalled transaction, but it is not associated with the given StreamID.

Note: When SMMU\_S\_IDR1.SECURE\_IMPL == 1, the SMMU might be presented with transactions from a Secure stream and a Non-secure stream that have the same StreamID value. The Secure and Non-secure StreamID namespaces are independent so the streams and transactions are unrelated. It is therefore possible for two stalled transactions to exist, one from a Secure stream and the other from a Non-secure stream, which cause an event to be recorded in both Secure and Non-secure Event queues that coincidentally have the same StreamID and STAG value. Despite having the same numeric values, the two stall event records represent independent transactions, as the Security states of the streams are different.

Note: Event records from stalled transactions indicate the StreamID and SubstreamID of the transaction, the SubstreamID is not required to be supplied for this command as STAG locates the specific transaction.

Stalled transactions might be retried with CMD\_RESUME in any order, but IMPLEMENTATION DEFINED interconnect ordering rules must still be observed and these might not allow a retried transaction to progress into the system unless a prior stalled transaction is also resumed. For example, two stalled reads from the same StreamID might not be allowed to cross. If the later read is resumed with retry it might still stall until the first read is resumed with retry or terminated, at which point the later read might progress.

Arm expects software to respond to every recorded event record indicating a stall using a CMD\_RESUME or a CMD\_STALL\_TERM, and expects that a CMD\_RESUME is only issued in response to a stall event record visible in an Event queue. Software must only issue CMD\_RESUME with StreamID and STAG values that have directly been supplied in a stall event record that has not already been subject to a matching CMD\_RESUME or CMD\_STALL\_TERM operation.

The STAG value of a stall event record matched by CMD\_RESUME is returned to the set of values that the SMMU might use in future stall event records.

It is CONSTRAINED UNPREDICTABLE whether a matching transaction is affected by this command in the following cases:

- The indicated stalled transaction exists in the SMMU but, at the time of the CMD\_RESUME, an event has not yet been made visible to software.
- The encoding of STAG in an implementation allows a CMD\_RESUME to target a stalled transaction for which an event was not recorded because it was suppressed as a duplicate, see section 3.12.2 Stall model .
- The stalled transaction has already been subject to a prior CMD\_RESUME or CMD\_STALL\_TERM.

Note: Arm does not expect software to issue a CMD\_RESUME in these circumstances, but an implementation is not required to explicitly prevent an effect.

Consumption of CMD\_RESUME(Retry) does not guarantee that the given stalled transaction has already been retried, but does guarantee that, if it has not, it will be retried at a later time. The SMMU will retry the transaction in finite time.

4.7. Fault response and synchronization commands

Note: A stalled transaction that has no matching CMD\_RESUME response might never be retried.

A retried transaction behaves as though the transaction had just arrived at the SMMU.

Note: The transaction must respect configuration and translation cache invalidations and structure updates that occurred between the time of its original arrival and the retry.

Consumption of CMD\_RESUME(Terminate) does not guarantee that the given stalled transaction has already been terminated, but does guarantee that, if it has not, it will be terminated at a later time unless it retries (completing successfully) before being terminated. An implementation ensures that a transaction marked for termination with a CMD\_RESUME(Terminate) is terminated in finite time without unbounded delay, if it is not successfully retried before the termination occurs.

Note: If configuration remains in a state that would cause retries of the transaction to continue to fault, the transaction is guaranteed to be terminated. This also guarantees that a client device might wait for completion of the transaction, and will always eventually make forward progress.

Note: If the transaction is retried before the point of termination, it might complete successfully if its initial fault reason was resolved in the intervening time.

The SMMU does not guarantee response visibility by the client device.

Note: This means that software cannot guarantee that a given transaction has terminated without performing a synchronization involving the originating device originator or interconnect. This would need to be performed in a device- and system-specific manner before changing device configuration or translations in order to ensure that the transaction will not retry successfully with the new configuration. A similar scenario can exist where a system would need to ensure all transactions that are in progress that are buffered arrive at the SMMU (for termination) so that they do not later appear after new configuration or new translation state is applied.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.7.2 CMD\_STALL\_TERM(StreamID, SSec)

<!-- image -->

This command provides a mechanism to mark all stalled transactions originating from StreamID for termination.

Note: This command is equivalent to tracking individual stalls and issuing CMD\_RESUME(Terminate) separately.

This command must only be issued after the STE for the StreamID is updated to cause all new incoming transactions to immediately terminate with abort, including any required configuration cache invalidation and synchronization for the STE update. When issued in this condition, any transactions that are outstanding on the stream at the time that this command is observed by the SMMU are guaranteed to terminate with an abort, including the set of transactions that might have become stalled under a previous stream configuration, if the agent controlling the SMMUwaits for outstanding transactions to complete before altering the STE of the StreamID to a non-terminating configuration. The mechanism for this wait operation is IMPLEMENTATION DEFINED.

If no stalled transactions from the given stream exist before the command is observed and no transactions become stalled before the command is consumed, this command has no effect.

Consider the following cases:

- The STE is not configured to immediately terminate new transactions. This includes the case when configuration cache maintenance and synchronization for the STE update has not been performed.
- The STE is written in a way that changes such a configuration before all outstanding transactions have completed.

If the CMD\_STALL\_TERM command is issued when one of these cases apply, it is UNPREDICTABLE whether one of the following occurs:

- Stalled transactions related to the StreamID are terminated.
- Pending stall fault event records are prevented from being recorded.

The STAG values in stall event records associated with stalled transactions affected by CMD\_STALL\_TERM are returned to the set of values that the SMMU might use in future stall event records.

When issued on an SMMU implementation that does not support the Stall model, or where the Stall model has been disabled with NSSTALLD for the Non-secure Command queue, indicated by SMMU\_(*\_)IDR0.STALL\_MODEL == 0b01 , a CERROR\_ILL is raised.

The common behaviors for SSec apply. See 4.1.6 Common command fields .

Consumption of a CMD\_STALL\_TERM does not guarantee that matching stalled transactions have been terminated. When used as described in this section, consumption guarantees that the set of matching stalled transactions will be terminated at a future time. Transactions for the matching StreamID are not affected by this command if they become stalled after the command is consumed.

Note: This behavior matches CMD\_RESUME(Terminate).

Note: Early-retry cannot cause stalled transactions to complete successfully before termination occurs, because the STE configuration will terminate such early-retries, and therefore termination is guaranteed.

Issuing this command to the Realm Command queue results in CERROR\_ILL.

## 4.7.2.1 Notes and usage

Some matching stalled transactions might not record events because the events are suppressed, as described in 3.12.2.1 Suppression of duplicate Stall event records . Event queue record visibility semantics are covered in section 3.5.2 Queue entry visibility semantics .

This command is not intended to be used on a stream for which incoming transactions might become stalled during processing of this command because, in this scenario, the point in an ongoing sequence of transactions at which newly-faulting stalling transactions would no longer be matched by an ongoing CMD\_STALL\_TERM is UNPREDICTABLE. In addition, stall fault events might become visible to software for transactions that were matched and marked for termination by this command.

This command is intended to be used when forcibly de-commissioning or reclaiming a stream controlled by untrusted or unreliable software. It is intended to be issued after the stream has been explicitly configured to immediately terminate future incoming transactions without creating new stalled transactions.

Note: This sequence will shut down a device stream, including removal of stalled transactions:

1. Software stops the device from issuing transactions.
2. Transactions are terminated using:
- a) Set STE[i].Config to 0b000 and keep STE[i].V == 1
- b) Issuing a CMD\_CFGI\_STE(i, j, k) (or other configuration invalidation that covers relevant STE(s)).
- c) Issuing a CMD\_SYNC.
- d) At this point, any incoming transactions will terminate and no new transactions will enter stalled state. In addition, the completion of CMD\_SYNC ensures visibility of all stall fault event records related to STE[i], see 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes) . If a stall

event record cannot be written (for example, the queue is full), the transaction is either retried when the queue becomes writable and terminates given the new configuration or is marked for termination, if a retry does not happen before the CMD\_STALL\_TERM in the next step.

Note: A stall record (STALL == 1) is not written after this point. Any record that is written relates to new STE configuration, which terminates.

3. CMD\_STALL\_TERM (i, j):
- a) At this point, remaining stalled transactions are marked for termination, but might not have terminated yet.
4. Software waits for outstanding device transactions to complete.
- a) How this is achieved is IMPLEMENTATION DEFINED.
- b) This step waits for the stalled transactions to terminate and for transactions that are in progress to reach the SMMU and be terminated on arrival.
5. [Optional] CMD\_SYNC
- a) If the STE configuration causes incoming transactions to terminate in a non-silent manner (for example, if STE[i].V == 0 instead of STE[i].Config == 0b000 ), terminated fault events might have been generated because of the arrival of in-progress transactions during this procedure. This CMD\_SYNC ensures visibility (if the Event queue is writable) of the events related to terminated transactions for which an abort has been returned to the client device (see section 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes) ). If the Event queue is not writable, the completion of the CMD\_SYNC means that events for terminated transactions will not become visible after this point.
6. Software discards all event records relating to StreamID 'i' in the current set of Event queue records. Thereafter, all events relating to StreamID 'i' are from subsequent or newly-created configuration.

This sequence ensures that the Event queue will not subsequently receive any further stall event records associated with the stream and that there are no incomplete transactions still stalled in the SMMU.

## 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes)

<!-- image -->

This command provides a synchronization mechanism for the following:

- Preceding commands that were issued to the same Command queue as the CMD\_SYNC.
- Visibility of event records for client transactions terminated before the CMD\_SYNC.
- HTTU updates caused by completed translations.

When this command completes, it can raise a completion signal as an optional interrupt and an optional WFE wakeup event. The interrupt might take the form of an MSI (if supported by the implementation). Any operations made observable by the completion of the synchronization operation are observable before the interrupt or event is observable, and before the SMMU\_CMDQ\_CONS index indicates that the CMD\_SYNC has been consumed. Observation of the interrupt or event means that the consumption of the CMD\_SYNC is observable.

The ComplSignal parameter, CS, determines the signaling mechanism that notifies host software of the completion of a CMD\_SYNC, and can take the following values:

- 0b00 : SIG\_NONE:

The command takes no further action on its completion. The MSIAddress, MSIData, MSIWriteAttributes parameters are IGNORED.

- 0b01 : SIG\_IRQ:

The command signals its completion by raising an interrupt. On implementations supporting MSIs, a write containing MSIData is made to the physical address given by MSIAddress, if MSIAddress is non-zero, using memory type attributes from MSIAttr. On implementations that do not support MSIs, MSIAddress and MSIData are IGNORED. On implementations that support wired interrupts, an event on a unique wired interrupt output is asserted on this signal, regardless of the value of MSIAddress.

Note: This allows the choice of wired or MSIs on implementations that support both. Software can configure an MSI and ignore a wired output, or can disable MSIs and configure an interrupt controller for the wired output.

Note: See section 3.18 Interrupts and notifications . The MSI write might be directed towards an interrupt controller to generate an interrupt, or towards a shared memory location so that the PE can poll, or wait, on the location until the notification appears.

Note: Where an SMMU can send an MSI and the system allows the MSI write to coherently affect shared cached memory locations, an Armv8-A PE might use the loss of a reservation on a location as a WFE wakeup event, providing the same semantics as SIG\_SEV with SIG\_IRQ.

- 0b10 : SIG\_SEV:

The command sends an Event to the PE similar to SEV.

- Use of SIG\_SEV only sends an event when SMMU\_IDR0.SEV is set, otherwise, no event is available to a PE and SIG\_SEV is equivalent to SIG\_NONE, that is no completion signal is generated.
- Note: The PE might poll on the SMMU\_CMDQ\_CONS.RD register in a loop throttled by WFE.
- 0b11 : Reserved:

Causes a CERROR\_ILL.

The MSI configuration is given by the following parameters:

MSIAttr: Write attribute for MSI, encoded the same as the STE.MemAttr field

MSH: Shareability attribute for MSI write, encoded as:

- 0b00 : Non-shareable
- 0b01 : Reserved, treated as 0b00 .
- 0b10 : Outer Shareable.
- 0b11 : Inner Shareable.

Note: This field is IGNORED if MSIAttr specifies a memory type of any-Device or Normal-iNC-oNC, and Shareability is effectively Outer Shareable in these cases.

- MSIAddress[55:2]: If this field is non-zero, it configures the physical address that an MSI is sent to when SIG\_IRQ is used. Address bits above and below this field are treated as zero. The MSI is a 32-bit word-aligned write of MSIData.

The check for zero applies to the entire specified field span and is not limited to the physical address size (OAS) of an implementation.

If the OAS is smaller than this field, MSIAddress is truncated to the OAS, as described in section 3.4.3 Address sizes of SMMU-originated accesses .

MSI\_NS: On a Realm Command queue, this field indicates the target PA space of an MSI as following.

| Value   | Meaning                                               |
|---------|-------------------------------------------------------|
| 0b0     | MSIs are issued to Realm physical address space.      |
| 0b1     | MSIs are issued to Non-secure physical address space. |

This bit is RES0 for CMD\_SYNC commands issued to Non-secure and Secure Command queues

When a cacheable type is specified in MSIAttr, the allocation and transient hints are IMPLEMENTATION DEFINED.

This command waits for completion of all prior commands and ensures observability of any related transactions through and from the SMMU. Commands in the Command queue that are more recent than a CMD\_SYNC do not begin processing until the CMD\_SYNC completes.

When following a given command submitted to the SMMU, completion of a CMD\_SYNC makes the following guarantees:

| Command type                                               | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
|------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| TLB and ATS Invalidation commands: CMD_TLBI_*, CMD_ATC_INV | TLB invalidates and ATS Invalidations are guaranteed to be complete (all matching TLB entries are invalidated) and all transactions in progress that were translated using any of the TLB entries targeted by the invalidates are globally observable to their Shareability domain. The semantics of the completion of TLB invalidation match those of an Armv8-A PE. ATOS translations that were in progress at the time of the CMD_SYNC and used any of the TLB entries targeted by the invalidations are complete, or restart from the beginning after the CMD_SYNC completes (see section Translation tables and TLB invalidation completion behavior). Note: No dependency is required on completion of received broadcast TLB invalidation operations. The broadcast invalidation mechanism has its own synchronization and completion mechanisms (for example on AMBA interconnect, a DVMSync Operation). |
| Configuration invalidation commands: CMD_CFGI_*            | Configuration invalidations are guaranteed to be complete (matching cached configuration entries are invalidated) and all transactions that are in progress that were translated using any of the configuration cache entries targeted by the invalidates are globally observable to their Shareability domain. ATOS translations that were in progress at the time of the CMD_SYNC and used any of the configuration cache entries targeted by the invalidations are complete, or restart from the beginning after the CMD_SYNC completes (see section 3.21.3 Configuration structures and configuration invalidation completion).                                                                                                                                                                                                                                                                              |
| Prefetch commands: CMD_PREFETCH_*                          | Translation or configuration table walks initiated by any kind of prefetch, including CMD_PREFETCH_* , are affected by TLB or configuration cache invalidates in the same way as any other table walk and might therefore be transitively affected by the completion of a CMD_SYNC of a CMD_TLBI_* / CMD_CFGI_*. See section 3.21 Structure access rules and update procedures.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |

| Command type                                         | Action                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
|------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| PRI responses: CMD_PRI_RESP                          | Nothing. The SMMUcannot guarantee response visibility by the endpoint.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| Stall resume/termination: CMD_RESUME, CMD_STALL_TERM | Nothing. The CMD_RESUME and CMD_STALL_TERM commands complete by the time they are consumed.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Synchronization commands: CMD_SYNC                   | The guarantees of the prior CMD_SYNC have been met. CMD_SYNCs complete in order. The MSI writes of any prior CMD_SYNC are either visible to their Shareability domain or aborted and reported, where the commands are consumed from the same Command queue. If such an MSI write is aborted, it is guaranteed that the abort is reported in the relevant SMMU_(*_)GERROR.MSI_CMDQ_ABT_ERR associated with the security state of the Command queue. CMD_SYNC is not required to affect MSI writes originating from sources other than prior CMD_SYNC completion signals, or completion signals for CMD_SYNC commands related to a different Command queue. |

In addition, completion of a CMD\_SYNC ensures the following behavior:

- An unrecorded fault event record relating to a client transaction terminated by the SMMU (either immediately on a fault or after stalling) whose abort or termination response could have been observed by the client device before the start of the CMD\_SYNC, is guaranteed to have either:
- -Become visible in the relevant Event queue (given the visibility semantics of section 3.5.2 Queue entry visibility semantics ).
- -Been discarded, if it could not commit to write to the queue, because the queue is not writable. In this case the unrecorded fault event record will never become visible.
* Note: This rule ensures that if software performs a CMD\_SYNC after notification from a device that all of its outstanding transactions are complete, it is guaranteed that no termination fault records will later become visible from the device stream after the CMD\_SYNC completes.
* This rule applies however the termination of the transaction was performed, whether it was immediate because the Terminate fault model was used or whether the transaction originally stalled and was later terminated because a retry encountered a new configuration, or an update of SMMU\_(*\_)CR0.SMMUEN transitioned the field to 0. In the case of a retry encountering new configuration, any recorded event relates to the new configuration not the original stall.
- Where a particular interconnect does not return a response to a terminated client transaction, all committed unrecorded fault records corresponding to transactions internally terminated before the start of the CMD\_SYNC are made visible. Uncommitted fault records either commit to the Event queue and are made visible, or if they cannot be committed, are discarded and will not later become visible.
- Event records written to the Event queue after the completion of a CMD\_SYNC are guaranteed to be generated from configurations or translations visible to the SMMU after any invalidation completed by the CMD\_SYNC has taken effect. Event records relating to translations that were invalidated by broadcast TLBIs and the appropriate synchronization mechanism before the CMD\_SYNC was issued, are reported before completion of the CMD\_SYNC. No events relating to out-of-date configuration or translations will later become visible.
- When an unrecorded fault event record exists for a stalled transaction affected by TLBI or CFGI invalidations completed by a CMD\_SYNC, the completion also affects the event record in one of the following ways:

## Chapter 4. Commands

4.7.

- -The record commits to write and is made visible in the relevant Event queue.
- -If it cannot commit to write to the queue, because the queue is not writable, the transaction is retried when the queue is next writable, if it has not terminated or otherwise completed due to early retry before that time. If a retry leads to a new fault or error, a new event record is generated instead of the original one. If a retry completes successfully, no event is recorded for the transaction, because the original event is stale. This adheres to the previous rule. The original event record pertaining to prior invalidated configuration or translations must not be recorded after the CMD\_SYNC completes.
- HTTU caused by completed client transactions and completed ATOS translations is made visible, to the extent required to its Shareability domain, by completion of a CMD\_SYNC, see section 3.13.4 HTTU behavior summary .

There is no requirement for:

- A CMD\_SYNC submitted to the Non-secure Command queue to affect Secure traffic or event visibility. However, a CMD\_SYNC submitted to the Secure Command queue affects Non-secure traffic or event visibility when the CMD\_SYNC completes prior commands in the Secure Command queue that operate on Non-secure structures.
- -Note: Arm strongly recommends that a CMD\_SYNC issued on the Secure Command queue is not able to be blocked by actions of the Non-secure state, including Non-secure commands. When ATS is supported, Arm strongly recommends that a CMD\_SYNC issued on the Secure Command queue cannot be blocked by ATS Invalidation commands that were issued on the Non-secure Command queue.
- A CMD\_SYNC to affect any recorded stalled transaction, or to cause an unrecorded stalled transaction to be retried or recorded, except where necessary to record an event relating to newly-changed configuration or translations.

Note: A TLB or structure invalidation command has no explicit ordering against prior or subsequent non-CMD\_SYNC commands. If software requires one set of invalidations to be guaranteed complete before beginning a second set of invalidations, a CMD\_SYNC is required to separate the two sets.

If the completion of a prior CMD\_ATC\_INV cannot be guaranteed by a CMD\_SYNC because of a PCIe protocol error, such as a timeout, the CMD\_SYNC might cause a CERROR\_ATC\_INV\_SYNC command error to be raised, see sections 7.1 Command queue errors and 3.9.1.4 ATS Invalidation timeout . If a CMD\_SYNC raises a CERROR\_ATC\_INV\_SYNC error:

- The CMD\_SYNC is not complete and has not been consumed, that is, SMMU\_(*\_)CMDQ\_CONS.RD remains pointing at the CMD\_SYNC that raised the error. No completion signals are sent.
- The completion guarantees of the CMD\_SYNC have not been met.
- An outstanding CMD\_ATC\_INV command is one that was submitted to the command queue before the CMD\_SYNC and that has not been completed by a previous successful CMD\_SYNC, and:
- -An UNKNOWN set of outstanding CMD\_ATC\_INV commands has timed out and will never complete.
- -An UNKNOWN set of outstanding CMD\_ATC\_INV commands might be in the process of completing successfully, but are not guaranteed to have completed successfully.
- All other operations that the CMD\_SYNC would otherwise have completed are not guaranteed to have completed, but will be completed by a new CMD\_SYNC that is successfully consumed after being re-submitted to the queue after the error is resolved and command processing is resumed.

Note: For example, a CMD\_TLBI\_* command, that was processed prior to the CMD\_SYNC that caused the error, might still be being processed and is guaranteed to still take effect; a CERROR\_ATC\_INV\_SYNC does not cause such commands to be terminated and there is no requirement for them to be re-submitted after resolving the error.