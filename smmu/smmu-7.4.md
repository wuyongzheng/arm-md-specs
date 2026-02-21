## 7.4 Event queue overflow

An SMMU output queue is full if the consumer can observe that there are no free entries for the producer to add new entries to, see section 3.5.2 Queue entry visibility semantics . The Event queue is full if it can be observed that SMMU\_(*\_)EVENTQ\_PROD.WR == SMMU\_(*\_)EVENTQ\_CONS.RD and WRAP bits differ.

Note: If the SMMU can observe that a write it made for a new queue entry is visible in memory, but PROD.WR has not yet been updated to pass the position of the new entry, the new entry is not yet visible to software in terms of the queue visibility semantics.

Event queue overflow occurs when the Event queue is enabled (EVENTQEN == 1), the queue is full, and a pending event record is discarded because the queue is full. An Event queue overflow condition is entered to indicate that one or more event records have been lost:

- Fault information.
- Configuration errors.

It is not possible for an external agent to observe an Event queue overflow condition if it could not first observe the Event queue being full.

Note: An implementation must therefore prevent the overflow condition from being observable by software before an update to the PROD index is observable.

A configuration error record or fault record from a terminated transaction is discarded when the SMMU attempts to insert it into a full Event queue. However, a fault record from a stalled transaction is not discarded and an event is reported for the stalled transaction when the queue is next writable. In addition, as stall fault records are not discarded, stall fault records do not cause an overflow condition. Only discarded events cause overflow.

When EVENTQEN == 0, events are not delivered and non-stall event records might be discarded but do not cause an overflow condition.

The Event queue overflow condition is present when:

SMMU\_EVENTQ\_PROD.OVFLG != SMMU\_EVENTQ\_CONS.OVACKFLG

When an overflow occurs, the SMMU toggles the SMMU\_EVENTQ\_PROD.OVFLG flag if the overflow condition is not already present.

Note: Arm recommends that whenever software reads SMMU\_EVENTQ\_PROD, it checks OVFLG against its own copy. If different, the overflow condition arose. Arm recommends that software then updates its copy with the value of OVFLG, and processes the Event queue entries as quickly as possible, updating SMMU\_EVENTQ\_CONS in order to move on the RD pointer but also to acknowledge receipt of the overflow condition by setting OV ACKFLG to the same value read from OVFLG.

Note: In terms of delivering events, a queue in an unacknowledged overflow state does not behave any differently to normal queue state. If software were to consume events and free space but leave overflow unacknowledged, new events could be recorded. Because a second overflow condition cannot be indicated, a subsequent queue overflow would be invisible therefore Arm expects software to acknowledge overflow upon the first consumption of events after the condition arose.