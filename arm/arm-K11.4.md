## K11.4 Using a mailbox to send an interrupt

In some message passing systems, it is common for one observer to update memory and then notify a second observer of the update by sending an interrupt, using a mailbox.

Although a memory access might be made to initiate the sending of the mailbox interrupt, a DSB instruction is required to ensure the completion of previous memory accesses.

Therefore, the following sequence is required to ensure that P2 observes the updated value:

AArch32

## P1

| STR R5, [R1] DSB ST STR R0, [R4]         | ; message stored to shared memory location ; R4 contains the address of a mailbox   |
|------------------------------------------|-------------------------------------------------------------------------------------|
| P2                                       | P2                                                                                  |
| ; interrupt service routine LDR R5, [R1] | ; interrupt service routine LDR R5, [R1]                                            |
| AArch64 P1                               | AArch64 P1                                                                          |
| STR W5, [X1] DSB ST STR W0, [X4]         | ; message stored to shared memory location ; R4 contains the address of a mailbox   |
| P2                                       | P2                                                                                  |
| ; interrupt service routine              | ; interrupt service routine                                                         |