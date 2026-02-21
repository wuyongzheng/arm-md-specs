## 7.2 Event queue recorded faults and events

Three categories of events might be recorded into the Event queue:

- Configuration errors.
- Faults from the translation process.
- Miscellaneous.

Configuration errors result from improper register, STE or CD contents and are associated with the translation of an incoming transaction. An improper configuration in memory is not reported until the data structures are used in response to a transaction. A fault from translation is reported only when a transaction attempts a translation. Any incoming transaction might cause at most one event report which might be a configuration error or, if configuration is all valid, one of several kinds of translation fault (which might be applicable to stage 1 or stage 2).

An SMMU implementation might prefetch configuration and TLB entries in an IMPLEMENTAITON SPECIFIC manner. A prefetched erroneous configuration does not record a configuration error (even if prefetched in response to an explicit CMD\_PREFETCH\_* command). A translation fault or configuration error is recorded only on receipt of a transaction.

Miscellaneous events are recorded asynchronously to incoming data transactions, for example E\_PAGE\_REQUEST.

## 7.2.1 Recording of events and conditions for writing to the Event queue

Events are delivered into an Event queue if the queue is 'writable'. The Event queue is writable when all of the following are true:

- The queue is enabled, through SMMU\_(*\_)CR0.EVENTQEN for the Security state of the queue.
- The queue is not full (see section 7.4 Event queue overflow regarding overflow).
- No unacknowledged GERROR.EVENTQ\_ABT\_ERR condition exists for the queue.

When the queue is not writable, events not associated with stalled faults are silently discarded. In addition, a queue overflow condition is triggered when events are discarded because the queue is unwritable because it is full, see section 7.4 Event queue overflow .

Events caused by stalled transactions are not discarded. A stalled faulting transaction that has not recorded an event because the queue is unwritable has one of the following behaviors:

- If the stalled transaction is affected by a configuration or translation invalidation and CMD\_SYNC, the transaction must be retried after the queue becomes writable again (non-full, enabled and without a queue abort condition). This either results in the transaction succeeding (because of a new configuration or translation) in which case no event is recorded for the transaction, or the generation of a new fault (reflecting new configuration or translation) which attempts to record an event into the queue, see section 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes) .
- -A transaction that was not affected by an invalidation or CMD\_SYNC is permitted but not required to be retried in the same way as a transaction that is affected. The transaction might be retried at the point that the queue becomes writable.
- Alternatively, the transaction retries while the queue is unwritable:
- -If the retry translates successfully, the original event is permitted, but not required, to be recorded.
- -A fault that is encountered during a retry replaces any previous faults for the transaction. If the new fault causes the transaction to stall again, the new stall event is recorded in the Event queue when the queue becomes writable again. If the new fault causes the transaction to be terminated while the queue is still unwritable, the recording of the terminate event is lost.
- If the transaction is not retried, the original fault event record is recorded into the queue when it becomes writable.

Refer also to the event delivery effects of CMD\_STALL\_TERM ( 4.7.2 CMD\_STALL\_TERM(StreamID, SSec) ), CMD\_SYNC ( 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes) ) and SMMUEN ( 6.3.9.6 SMMUEN ).

An external abort on write of the Event queue might cause written event data to be lost, including stall event records. See section 7.2.2 Event queue access external abort .

An event is permitted, but not required, to be recorded for a stalled faulting transaction when:

- The stalled transaction has early-retried and translated successfully before the SMMU has attempted to write out its event record, see section 3.12.2.2 Early retry of Stalled transactions .

Note: As the transaction has completed, there is no benefit in recording the original stall to software because software intervention is not required to progress the transaction.

Events arising from terminated faulting transactions commit to being recorded into the Event queue if it is writable. When EVENTQEN is transitioned to 0, committed events are written out and guaranteed to be visible by the time the update completes and all uncommitted events from terminated faulting transactions are discarded. If accesses to the Event queue aborted (see section 7.2.2 Event queue access external abort below), the condition is made visible in GERROR by the time the EVENTQEN update completes. See sections 6.3.9.4 EVENTQEN and 6.3.9.6 SMMUEN .

Note: There is no dependency required between EVENTQEN and visibility of any GERROR MSI that might arise from completion of outstanding queue writes that abort.

Some events are permitted to be recorded when SMMU\_(*\_)CR0.SMMUEN == 0 where explicitly stated in the event descriptions in this section. The remainder of events are related to the translation process and are not generated when translation is disabled with SMMUEN == 0.

Note: This means that SMMUEN == 0 does not imply EVENTQEN == 0.

## 7.2.2 Event queue access external abort

An external abort detected while accessing the Event queue, for example when writing a record, activates the SMMU\_(*\_)GERROR.EVENTQ\_ABT\_ERR Global Error. It is IMPLEMENTATION DEFINED as to whether the interconnect to the memory system can report transaction aborts. If EVENTQ\_ABT\_ERR is triggered, one or more events might have been lost, including stall fault event records.

An implementation is permitted to read any address within the bounds of the Event queue when the queue is enabled. In addition to writes of new records to the queue, such reads might also lead to an external abort.

The SMMU only writes to the Event queue when the queue is both enabled and writable, see section 7.2.1 Recording of events and conditions for writing to the Event queue .

It is IMPLEMENTATION DEFINED whether an external abort on write is synchronous or asynchronous:

- If a queue write abort is synchronous, queue entry validity semantics are maintained so that all entries up to the SMMU\_(*\_)EVENTQ\_PROD index are valid successfully-written event records. All outstanding queue writes are completed before the error is flagged in GERROR.EVENTQ\_ABT\_ERR. Where multiple outstanding record writes are performed simultaneously, records written at and beyond the queue location of the aborting record location are not visible to software even if they are written successfully, and are lost. The PROD index is not incremented for entries that caused a synchronous abort. In the scenario where a write of an event to an empty Event queue causes a synchronous abort, the PROD index is not incremented, the queue remains empty and the queue non-empty IRQ therefore is not triggered.

-Note: Software can consume and process all valid entries in the Event queue.

- If a queue write abort is asynchronous, queue validity semantics are broken. The PROD index is permitted to be incremented for entries that caused an asynchronous abort. Software must assume all Event queue entries are invalid at the point of receiving the Global Error, and Arm strongly recommends that the queue is made empty either by re-initialization or by the consumption or discarding of all (invalid) entries.

- -Note: An IRQ might be observed for the activation of the SMMU\_(*\_)GERROR.EVENTQ\_ABT\_ERR condition in any order relative to an IRQ relating to the Event queue going non-empty as a result of the SMMU incrementing the PROD index for a queue entry that experiences an asynchronous external abort.

If the stalling fault model is implemented and enabled, software must terminate all stalling transactions that could be present in the SMMU by using CMD\_STALL\_TERM or a transition of SMMU\_(*\_)CR0.SMMUEN through 0.

See section 8.2 Miscellaneous for similar PRI queue write abort behavior.

## 7.2.3 Secure and Non-secure Event queues

If Secure state is implemented, the Secure Event queue receives events relating to transactions from Secure streams.

The Non-secure Event queue receives events relating to transactions from Non-secure streams.

The Event queues for different Security states are independent.

Note: For example, this means that both:

- Non-secure faults or errors do not cause Secure event records.
- Secure faults or errors do not cause Non-secure event records.