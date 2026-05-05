## C6.2.367 SEVL

## Send event local

This instruction is a hint instruction that causes an event to be signaled locally without requiring the event to be signaled to other PEs in the multiprocessor system. It can prime a wait-loop that starts with a WFE instruction.

<!-- image -->

<!-- image -->

## Encoding

SEVL

## Decode for this encoding

// Empty.

## Operation

SendEventLocal();
