## C6.2.501 WFE

## Wait for event

This instruction is a hint instruction that indicates that the PE can enter a low-power state and remain there until a wakeup event occurs. Wakeup events include the event signaled as a result of executing the SEV instruction on any PE in the multiprocessor system. For more information, see Wait For Event mechanism and Send event.

As described in Wait For Event mechanism and Send event, the execution of a WFE instruction that would otherwise cause entry to a low-power state can be trapped to a higher Exception level.

<!-- image -->

<!-- image -->

## Encoding

WFE

## Decode for this encoding

// Empty.

## Operation

Hint\_WFE();
