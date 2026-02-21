## 3.5 Command and Event queues

All SMMU queues for both input to, and output from the SMMU are arranged as circular buffers in memory. A programming interface has one Command queue for input and one Event queue (and optionally one PRI queue) for output. Each queue is used in a producer-consumer fashion so that an output queue contains data produced by the SMMU and consumed by software. An input queue contains data produced by software, consumed by the SMMU.

## 3.5.1 SMMU circular queues

A queue is arranged as a 2 n -items sized circular FIFO with a base pointer and two index registers, PROD and CONS, indicating the producer and consumer current positions in the queue. In each of the output and input roles, only one index is maintained by the SMMU, with the other is maintained by software.

For an input queue (Command queue), the PROD index is updated by software after inserting an item into the queue, and is read by the SMMU to determine new items. The CONS index is updated by the SMMU as items are consumed, and is read by software to determine that items are consumed and space is free. An output queue is the exact opposite.

PROD indicates the index of the location that can be written next, if the queue is not full, by the producer. CONS indicates the index of the location that can be read next, if the queue is not empty. The indexes must always increment and wrap to the bottom when they pass the top entry of the queue.

The queues use the mirrored circular buffer arrangement that allows all entries to be valid simultaneously (rather than N-1 valid entries in other circular buffer schemes). Each index has a wrap flag, represented by the next higher bit adjacent to the index value contained in PROD and CONS. This bit must toggle each time the index wraps off the high-end and back onto the low-end of the buffer. It is the responsibility of the owner of each index, producer or consumer, to toggle this bit when the owner updates the index after wrapping. It is intended that software reads the register, increments or wraps the index (toggling wrap when required), and writes back both wrap and index fields at the same time. This single update prevents inconsistency between index and wrap state.

- If the two indexes are equal and their wrap bits are equal, the queue is empty and nothing can be consumed from it.
- If the two indexes are equal and their wrap bits are different, the queue is full and nothing can be produced to it.
- If the two indexes differ or the wrap bits differ, the consumer consumes entries, incrementing the CONS index until the queue is empty (both indices and wrap bits are equal).

Therefore, the wrap bits differentiate the cases of an empty buffer and a full buffer where otherwise both indexes would indicate the same location in both full and empty cases.

On initialization, the queue indexes are written by the agent controlling the SMMU before enabling the queue. The queue indexes must be initialized into one of the following consistent states:

- PROD.WR == CONS.RD and PROD.WR\_WRAP == CONS.RD\_WRAP, representing an empty queue.
- -
- Note: Arm expects this to be the state on normal initialization.
- PROD.WR == CONS.RD and PROD.WR\_WRAP != CONS.RD\_WRAP, representing a full queue.
- PROD.WR &gt; CONS.RD and PROD.WR\_WRAP == CONS.RD\_WRAP, representing a partially-full queue.
- PROD.WR &lt; CONS.RD and PROD.WR\_WRAP != CONS.RD\_WRAP, representing a partially-full queue.

The agent controlling the SMMU must not write queue indexes to any of the following inconsistent states whether at initialization or after the queue is enabled:

- PROD.WR &gt; CONS.RD and PROD.WR\_WRAP != CONS.RD\_WRAP
- PROD.WR &lt; CONS.RD and PROD.WR\_WRAP == CONS.RD\_WRAP

If the queue indexes are written to an inconsistent state, one of the following CONSTRAINED UNPREDICTABLE behaviors is permitted:

- The SMMU consumes, or produces as appropriate to the given queue, queue entries at UNKNOWN locations in the queue.

- The SMMU does not consume, or produce as appropriate, queue entries while the queue indexes are in an inconsistent state.
- For a queue where the SMMU is the producer, the SMMU treats the queue as though it is full while the queue indexes are in an inconsistent state.

Each circular buffer is 2 n -items in size, where 0 &lt;= n &lt;= 19. An implementation might support fewer than 19 bits of index. Each PROD and CONS register is 20 bits to accommodate the maximum 19-bit index plus the wrap bit. The actual buffer size is determined by software, up to the discoverable SMMU IMPLEMENTATION DEFINED limit. The position of the wrap bit depends on the configured index size.

Note: For example, when a queue is configured with 128 entries it means:

- The queue indices are 7-bit.
- PROD.WR and CONS.RD fields are 7 bits large. The queue indexes are bits [6:0] of PROD and CONS.
- The wrap bit [7] of PROD and CONS registers. Bits [19:8] are ignored.

The lifecycle of a circular buffer is shown in Figure 3.8.

Figure 3.8: Circular buffer/queue operation

<!-- image -->

When producing or consuming entries, software must only increment an index (except when an increment will

cause a wrap to the start). The index must never otherwise be moved backwards. The SMMU makes the same guarantee, only incrementing or wrapping its index values.

There is one Command queue per implemented Security state. The SMMU commands are consumed in order from this queue.

The Event queues receive asynchronous events such as faults recorded from device traffic or configuration errors (which might be discovered only when device traffic causes the SMMU to traverse the structures). On the Non-secure side, there is one global Event queue which receives events from all Non-secure streams and configuration.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, there is also one Secure Event queue which receives events from all Secure streams and configuration, see section 3.10.2.1 Secure commands, events and configuration .

All output queues are appended to sequentially.

## 3.5.2 Queue entry visibility semantics

Any producer (whether the SMMU or software) must ensure that if an update to the PROD index value is observable by the consumer, all new queue entries are observable by the consumer. For output queues from the SMMU (Event and PRI queues), the SMMU writes queue data to memory and, when that data becomes visible with respect to the rest of the Shareability domain, the SMMU allows the updated PROD index value to be observed. This is the first point that a new queue entry is visible to the consumer.

A consumer must not assume presence of a new valid entry in a queue through any mechanism other than having first observed an updated PROD index that covers the entry position. If a consumer reads a queue entry beyond the point indicated by the last read of the PROD index, the entry contains UNKNOWN data.

Note: Interrupt ordering rules also exist, see section 3.18 Interrupts and notifications . The SMMU makes queue updates observable through the PROD index no later than at the point where it asserts the queue interrupt.

Note: Software must not assume a new queue item is present when an interrupt arrives, without first reading the PROD index. If, for example, a prior interrupt handler consumed all events including those of a second batch (with a second interrupt), the next interrupt handler invocation might find no new queue entries.

## 3.5.3 Event queue behavior

The SMMU might support configurable behavior on Translation-related faults, which enable a faulting transaction to be stalled , pending later resolution, or terminated which immediately aborts the transaction. See section 3.12 Fault models, recording and reporting for details on fault behavior.

Events are recorded into the Event queue in response to a configuration error or translation-related fault associated with an incoming transaction. A sequence of faults or errors caused by incoming transactions could fill the Event queue and cause it to overflow if the events are not consumed fast enough. Events resulting from stalled faulting transactions are never discarded if the Event queue is full, but are recorded when entries are consumed from the Event queue and space next becomes available. Other types of events are discarded if the Event queue is full.

Note: Arm expects that the classes of events that might be discarded are generally used for debug. Section 7.4 Event queue overflow covers the exact queue behavior upon overflow.

Arm recommends that system software consumes entries from the Event queue in a timely manner to avoid overflow during normal operation.

In all cases in this specification, when it is stated that an event is recorded, the meaning is that the event is recorded if room is available for a new entry in the Event queue and the queue is writable. A queue is writable if it is enabled, has no global error flagged and would not otherwise overflow, see section 7.2 Event queue recorded faults and events . Events that are not reported in response to a stalled transaction (for example where there is no Stall field, or Stall == 0) are permitted to be discarded if they cannot be recorded. Stall events are generally not discarded and are recorded when the Event queue is next writable, see section 7.2 Event queue recorded faults and events for details of exceptions to this rule. Software must consume events from the queue to free up space,

otherwise the pending stall events will not be recorded. Stall events are otherwise no different to any other event. The queue is filled in the same circular order and such events do not overwrite existing, unconsumed, events.

Where multiple pending events contend for a write to the Event queue, Arm recommends that an implementation does not unfairly prioritize non-stall events above events with Stall == 1, if it is possible to do so. This helps avoid the case of a steady stream of terminated transactions from a misbehaving device holding back the events of stalled transactions for an indeterminate time.

If an event is generated in response to a transaction that is terminated, there is no requirement for the event to be made visible in the Event queue before a transaction response is returned to the client. See CMD\_SYNC, section 4.7.3 CMD\_SYNC(ComplSignal, MSIAddress, MSIData, MSIWriteAttributes) , which enforces visibility of events relating to terminated transactions.

Note: This means that an event generated in response to a terminated transaction might be visible as an SMMU event before the point that the transaction termination is reported at the client device.

## 3.5.4 Definition of event record write 'Commit'

Generation of an event record can be abstracted into these steps:

1. A situation that triggers an event occurs, for example a translation fault.
2. An event record is assembled internally in the SMMU.
3. It is determined that it is possible to write a new queue entry.
4. The final event record is committed to be written to the Event queue entry.
5. The event record becomes visible in the Event queue:
- a. The update to the record data location is visible to the required Shareability domain.
- b. The PROD.WR index is updated to publish the new record to software. In terms of queue semantics, the record is not visible (even if it has been written to memory) until the write index is updated to cover the new entry.

The commit point, 4, represents the conceptual point after which the event will definitely be written to the queue and eventually become visible. Until commit, the event write might not happen (for example, if the queue is full and software never consumes any entries, the event write will never commit).

An event write that has committed is guaranteed to become visible in the Event queue, if the subsequent write does not experience an external abort, see section 7.2 Event queue recorded faults and events .

The write of a stall event record must not commit until the queue entry is deemed writable (the queue is enabled and not full). If it is not writable, the stall record is buffered until the queue is next writable, unless one of the exceptions in section 7.2 Event queue recorded faults and events causes the record to be discarded.

## 3.5.5 Event merging

Implementations are permitted to merge some event records together. This might happen where multiple identical events occurred, and can be used to reduce the volume of events recorded into the Event queue where individual events do not supply additional useful information.

Events can be merged where all of the following conditions are upheld:

- The event types and all fields are identical, except fields explicitly indicated in section 7.3 Event records .
- If present, the Stall field is 0. Stall fault records are not merged, see section 3.12.2 Stall model .

An implementation is not required to merge any events, but one that does is required to support the STE.MEV flag to enable or inhibit merging of events relating to a given stream.

Note: For debugging purposes, merging of some events can be disabled on a per-stream basis using the STE.MEV flag.

Software implementations (for example a virtual emulation of an SMMU) are not required to respect STE.MEV. A hypervisor might cause events to continue to be merged after a guest requests merging to be disabled, for example if it determines a misbehaving guest to be causing too many debug events.

See section 7.3.1 Event record merging for details.

## 3.5.6 Enhanced Command queue interfaces

An SMMU can implement multiple Command queues for the Non-secure or Secure SMMU programming interfaces. This is advertised in SMMU\_IDR1.ECMDQ and SMMU\_S\_IDR0.ECMDQ.

The components of the Enhanced Command queue feature are:

- Up to 256 Command queue control pages.
- Each Command queue control page contains the control interface for up to 256 queues.
- Each Command queue control page is implemented in registers in the SMMU.

The interface for each queue in a control page is similar to the SMMU\_CMDQ\_{BASE, CONS, PROD} registers.

The presence of Enhanced Command queue interfaces does not imply removal of the SMMU\_(*\_)CMDQ\_* interfaces.

A Command queue control page contains multiple instances of the base, producer and consumer controls for a Command queue. Each instance is referred to as an Enhanced Command queue, ECMDQ.

An implementation might have more than one Command queue control page. The number of Command queue control pages available to Non-secure state is advertised in SMMU\_IDR6.CMDQ\_CONTROL\_PAGE\_LOG2NUMP.

The Secure equivalent is SMMU\_S\_IDR6.CMDQ\_CONTROL\_PAGE\_LOG2NUMP.

The registers for each Command queue control page are:

- SMMU\_CMDQ\_CONTROL\_PAGE\_BASEn
- SMMU\_CMDQ\_CONTROL\_PAGE\_CFGn
- SMMU\_CMDQ\_CONTROL\_PAGE\_STATUSn

Within each Command queue control page are many ECMDQ controls. The ECMDQ is similar to the register interface for the Command queue in SMMUv3. Each ECMDQ occupies 16 bytes of address space.

| Offset   | Field            | Size     | Description                               |
|----------|------------------|----------|-------------------------------------------|
| 0x00     | SMMU_ECMDQ_BASEn | 64b / 8B | Pointer to queue base address, queue size |
| 0x08     | SMMU_ECMDQ_PRODn | 32b / 4B | Queue producer write index                |
| 0x0C     | SMMU_ECMDQ_CONSn | 32b / 4B | Queue consumer read index, error status   |

The SMMU reacts to updates of each SMMU\_ECMDQ\_PRODn in finite time.

For more information on the layout of the Command queue control pages, see:

- Section 6.1 Memory map
- Section 6.2.5 Registers in a Command queue control page

## 3.5.6.1 Behavior

The SMMU accesses the Command queues using the attributes configured in SMMU\_(*\_)CR1.{QUEUE\_SH, QUEUE\_OC, QUEUE\_IC}, and the MPAM attributes configured in SMMU\_(*\_)GMPAM.

If any Enhanced Command queue interface is enabled such that SMMU\_(*\_)CR1.{QUEUE\_SH, QUEUE\_OC, QUEUE\_IC} could be used when generating an access, then SMMU\_(*\_)CR1.{QUEUE\_SH, QUEUE\_OC, QUEUE\_IC} are read-only.

The conditions for a queue being empty , full and non-empty are the same as for the SMMU\_(*\_)CMDQ\_CONS and SMMU\_(*\_)CMDQ\_PROD registers as specified in section 3.5.1 SMMU circular queues .

The SMMU consumes commands from a queue if the queue is non-empty.

A CMD\_SYNC consumed from an ECMDQ in a Command queue control page guarantees that the effects of commands previously-consumed on that queue are complete, including the reporting of events relating to configuration and translation information invalidated by those commands.

The rules for consumption of commands other than CMD\_SYNC are the same as for the Command queue controlled by SMMU\_(*\_)CMDQ\_{PROD, CONS}.

The rules for consumption a CMD\_SYNC issued to the Command queue via SMMU\_(*\_)CMDQ\_PROD are independent of ECMDQ state. It is not required to synchronize commands and events relating to ECMDQ queues.

The SMMU is permitted to consume from many queues in parallel.

The SMMU does not give a guaranteed serialization or total order of Commands consumed across different queues.

For example, an implementation might consume from many queues in a round-robin or weighted round-robin schedule.

If SMMU\_IDR0.SEV == 1, the SMMU triggers a WFE wake-up event when any ECMDQ becomes non-full.

## 3.5.6.2 Enabling and disabling an ECMDQ interface

An ECMDQ interface is enabled when SMMU\_ECMDQ\_PRODn.EN == SMMU\_ECMDQ\_CONSn.ENACK == 1.

An ECMDQ interface is disabled when SMMU\_ECMDQ\_PRODn.EN == SMMU\_ECMDQ\_CONSn.ENACK == 0.

The same guarantees around being enabled, disabled and completing transitions between the two states apply as for SMMU\_(*\_)CR0.CMDQEN/ SMMU\_(*\_)CR0ACK.CMDQEN.

In the transition from enabled to disabled, once the SMMU has updated SMMU\_ECMDQ\_CONSn.ENACK to 0, it is guaranteed that errors have been reported and consumption of commands has stopped, and therefore that SMMU\_ECMDQ\_CONSn.{ERR\_REASON, ERR, RD\_WRAP, RD} are stable.

The SMMU updates SMMU\_ECMDQ\_CONSn.ENACK even if SMMU\_ECMDQ\_PRODn.ERRACK != SMMU\_ECMDQ\_CONSn.ERR.

## 3.5.6.3 Errors relating to an ECMDQ interface

If the SMMU encounters any error while fetching or processing a command, it toggles the value of SMMU\_ECMDQ\_CONSn.ERR and updates the reason in SMMU\_ECMDQ\_CONSn.ERR\_REASON.

The SMMU updates SMMU\_ECMDQ\_CONSn.RD and SMMU\_ECMDQ\_CONSn.RD\_WRAP to point at the command that produced ERR\_REASON, in the same manner as SMMU\_(*\_)CMDQ\_CONS.RD points at a failed command.

If SMMU\_ECMDQ\_PRODn.ERRACK != SMMU\_ECMDQ\_CONSn.ERR as the result of an error, the SMMU does not consume commands.

If software inappropriately configures SMMU\_ECMDQ\_PRODn.ERRACK to mismatch SMMU\_ECMDQ\_CONSn.ERR , it is CONSTRAINED UNPREDICTABLE whether the SMMU consumes commands from that ECMDQ and whether a subsequent error is correctly reported. This CONSTRAINED UNPREDICTABLE behavior additionally applies in the case when software transitions an ECMDQ from disabled to enabled while SMMU\_ECMDQ\_PRODn.ERRACK != SMMU\_ECMDQ\_CONSn.ERR.

Disabling the ECMDQ, making SMMU\_ECMDQ\_PRODn.ERRACK and SMMU\_ECMDQ\_CONSn.ERR consistent, then enabling the ECMDQ is sufficient to restore predictable behavior.

If the update of SMMU\_ECMDQ\_CONSn.ERR is visible then the updates of ERR\_REASON, RD and RD\_WRAP are visible, and fetches from the corresponding queue have completed.

The SMMU updates SMMU\_ECMDQ\_CONSn.ENACK even if SMMU\_ECMDQ\_PRODn.ERRACK != SMMU\_ECMDQ\_CONSn.ERR.

Errors relating to ECMDQs are additionally reported in SMMU\_GERROR.CMDQP\_ERR for Non-secure state. ECMDQ errors for Secure state are similarly also reported in SMMU\_S\_GERROR.CMDQP\_ERR.

ECMDQs operate independently of the error status of SMMU\_(*\_)GERROR.CMDQ\_ERR.

If an error to be reported in any Non-secure SMMU\_ECMDQ\_CONS.ERR field occurs, and SMMU\_GERROR.CMDQP\_ERR is inactive, the error is additionally reported in SMMU\_GERROR.CMDQP\_ERR. The equivalent is true for Secure state, reporting in SMMU\_S\_GERROR.CMDQP\_ERR.

The activation, deactivation and state of SMMU\_(*\_)GERROR.CMDQP\_ERR have no effect on the Command queue control page or ECMDQ interfaces reached through it.

If the activation of SMMU\_(*\_)GERROR.CMDQP\_ERR is observable then the SMMU\_ECMDQ\_CONSn.ERR field indicating the reason for the activation is observable.

When the SMMU activates SMMU\_(*\_)GERROR.CMDQP\_ERR, the GERROR interrupt is triggered, in the same manner as other GERROR conditions in SMMUv3.

If the MSI from a CMD\_SYNC issued through a Command queue control page experiences an external abort, the abort is reported in SMMU\_(*\_)GERROR.MSI\_CMDQ\_ABT\_ERR

in the same manner as for a CMD\_SYNC issued through the SMMU\_CMDQ\_* interface.