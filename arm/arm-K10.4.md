## K10.4 Use of the FEAT\_PCDPHINT STSHH and PRFM IR (immediate) hint instructions

This section provides example uses of the STSHH and PRFM IR (immediate) hint instructions that FEAT\_PCDPHINT provides. It is not part of the Arm architecture definition.

## K10.4.1 Example ticket lock use of the STSHH hint instruction

FEAT\_PCDPHINT provides a STSHH hint instruction, that PE software can use to hint to the memory system that if the next instruction the PE executes generates an explicit write effect, it will be to a location being observed, and it might be beneficial if the memory system takes some action to propagate the updated value to the observers with minimal latency.

One example use of STSHH is in ticket lock code, where a thread currently holding the lock can use STSHH before it releases the lock, as shown in the following example. In the example:

- There are two counters in the system:
- -Ticket assignment. A counter holding the number of the next ticket in the queue.
- -Current ticket number. Holds the number currently being served.
- In the piece of code:
- -In the Consuming portion, the thread has already acquired a ticket from the ticket assignment counter and is waiting for its number to match the current ticket number. The current ticket number increments by one each time a thread holding the lock releases the lock.
- -In the Producing portion, the thread has already acquired the lock and finished the task it needed to do while it held the lock, and is now releasing the lock, by:
1. Incrementing the current ticket number.
2. Sending a STSHH hint that it is about to perform an explicit write effect, and that it might be beneficial if the memory system takes some action to propagate the updated current ticket number to the other observers as soon as possible.
3. Storing the updated current ticket number back to the memory system. This releases the lock, allowing the next thread in ticket-order to acquire the lock. The observing threads waiting for the current ticket number to match their assigned ticket number might be polling the current ticket counter, or might have executed a PRFM IR (immediate) targeting the current ticket counter.

<!-- image -->

In the example, STSHH uses the KEEP policy because if no other observer acquires the lock afterwards, and our thread needs to re-enter the task it was doing while it held the lock, it can quickly do so.

## K10.4.2 Example data sharing use of the STSHH and PRFM IR (immediate) instructions

The following is a common pattern for data sharing between two threads:

<!-- image -->

With STSHH and PRFM IR (immediate), the following can be used instead:

<!-- image -->

In Example K10-3, STSHH uses the STRM policy because the producing thread does not read from the locations, and there must be a consumption by another thread before the producing thread updates the locations again.