## K11.3 Load-Acquire Exclusive, Store-Release Exclusive and barriers

The Armv8 architecture adds the acquire and release semantics to Load-Exclusive and Store-Exclusive instructions, which allows them to gain ordering acquire and/or release semantics.

The Load-Exclusive instruction can be specified to have acquire semantics, and the Store-Exclusive instruction can be specified to have release semantics. These can be arbitrarily combined to allow the atomic update created by a successful Load-Exclusive and Store-Exclusive pair to have any of:

- No Ordering semantics (using LDREX and STREX ).
- Acquire only semantics (using LDAEX and STREX ).
- Release only semantics (using LDREX and STLEX ).
- Sequentially consistent semantics (using LDAEX and STLEX ).

In addition, the Armv8 and later specifications require that the clearing of a global monitor will generate an event for the PE associated with the global monitor, which can simplify the use of WFE , by removing the need for a DSB barrier and SEV instruction.

## K11.3.1 Acquiring a lock

Acommon use of Load-Exclusive and Store-Exclusive instructions is to claim a lock to permit entry into a critical region. This is typically performed by testing a lock variable that indicates 0 for a free lock and some other value, commonly 1 or an identifier of the process holding the lock, for a taken lock.

Note

The inclusion of AArch32 PLDW instructions or AArch64 PRFM PST* instructions in these examples is not a functional requirement, but will improve performance on many implementations. The performance benefit of adding these instructions will vary between different implementations of the architecture.

For a critical region, the requirement on taking a lock is usually for acquire semantics, while the clearing of a lock requires release semantics:

AArch32

## Px

```
PLDW[R1] ; preload into cache in unique state Loop LDAEX R5, [R1] ; read lock with acquire CMP R5, #0 ; check if 0 STREXEQ R5, R0, [R1] ; attempt to store new value CMPEQ R5, #0 ; test if store suceeded BNE Loop ; retry if not ; loads and stores in the critical region can now be performed
```

AArch64

## Px

```
PRFM PSTL1KEEP, [X1] ; preload into cache in unique state Loop LDAXR W5, [X1] ; read lock with acquire CBNZ W5, Loop ; check if 0 STXR W5, W0, [X1] ; attempt to store new value CBNZ W5, Loop ; test if store succeeded and retry if not ; loads and stores in the critical region can now be performed
```

The acquire associated with the load is sufficient to ensure the required ordering in a lock situation. The Store-Exclusive will fail (and so be retried) if there is a store to the location being monitored between the Load-Exclusive and the Store-Exclusive.

## K11.3.2 Releasing a lock

The converse operation of releasing a lock does not require the use of Load-Exclusive and Store-Exclusive instructions, because only a single observer is able to write to the lock. However, often it is necessary for any observer to observe any memory updates, or any values that are loaded into memory, before they observe the release of the lock. Therefore, the lock release needs release semantics:

AArch32

## Px

```
; loads and stores in the critical region MOV R0, #0 STL R0, [R1] ; clear the lock with release semantics
```

AArch64

## Px

```
; loads and stores in the critical region STLR WZR, [X1] ; clear the lock with release
```

## K11.3.3 Ticket locks

When a lock is free, in order to avoid a rush to get the lock by many PEs, the use of ticket locks is common in more advanced systems. When the use is requested, the ticket locks determine the order of the users of the critical sections, in order to avoid starvation that can occur with a simple contention-based spin-lock.

Aticket lock allocates each thread a ticket number when it first requests the lock, and then compares that number with the current number for the lock. If they are the same, then the critical section can be entered. Otherwise the thread waits until the current number is equal to the ticket number for that thread.

The reading of the current number of the lock needs acquire semantics for the lock to be acquired.

## Note

- The code in this section is little-endian code, as it views the combined current and next values as a single combined quantity. The addresses of the current and next ticket values must be adjusted for a big-endian system.
- The inclusion of AArch32 PLDW instructions or AArch64 PRFM PST* instructions in these examples is not a functional requirement, but improves performance on many implementations. The performance benefit of adding these instructions varies between different implementations of the architecture.

This is shown in the implementation below:

AArch32

## Px

```
; R1 holds two 16 bit quantities ; the lower halfword holds the current ticket number ; the higher halfword holds the next ticket number PLDW[R1] ; preload into cache in unique state Loop1 LDAEX R5, [R1] ; read current and next ADD R3, R5, #0x10000 ; increment the next number STREX R6, R3, [R1] ; and update the value CMP R6, #0 ; did the exclusive pass BNE Loop1 ; retry if not CMP R5, R5, ROR #16 ; is the current ticket ours MOV R6, R5 BEQ block_start Loop2 LDAH R6, [R1] ; read current value CMP R6, R5, LSR #16 ; compare it with our allocated BNE Loop2 ; retry (spin) if it is not the same block_start
```

```
semantics
```

```
ticket
```

AArch64

## Px

```
; X1 holds 2 16 bit quantities ; the lower halfword holds the current ticket number ; the higher halfword holds the next ticket number PRFM PSTL1KEEP, [X1] ; preload into cache in unique state Loop1 LDAXR W5, [X1] ; read current and next ADD W3, W5, #0x10000 ; increment the next number STXR W6, W3, [X1] ; and update the value CBNZ W6, Loop1 ; did the exclusive pass - retry if not AND W6, W5, #0xFFFF CMP W6, W5, LSR #16 ; is the current ticket ours B.EQ block_start Loop2 LDARH W6, [X1] ; read current value CMP W6, W5, LSR #16 ; compare it with the our allocated B.NE Loop2 ; retry (spin) if it isn't the same block_start
```

```
ticket
```

Releasing the ticket lock simply involves incrementing the current ticket number, which is assumed in this example to be in R6, and doing a Store-Release:

## AArch32

```
ADD R6, R6, #1 STLH R6, [R1]
```

## AArch64

```
ADD W6, W6, #1 STLRH W6, [X1]
```

## K11.3.4 Use of Wait For Event (WFE) and Send Event (SEV) with locks

The Armv8 and later architectures can use the Wait For Event mechanism to minimize the energy cost of polling variables by putting the PE into a low-power state, suspending execution, until an asynchronous exception or an explicit event is seen by that PE. In Armv8 and later architectures, the event can be generated as a result of clearing the global monitor, so removing the need for a DSB barrier or an explicit send event message.This can be used with simple locks or with ticket locks.

```
Note
```

The inclusion of AArch32 PLDW instructions or AArch64 PRFM PST* instructions in these examples is not a functional requirement, but will improve performance on many implementations. The performance benefit of adding these instructions will vary between different implementations of the architecture.

## K11.3.4.1 Simple lock

The following is an example of lock acquire code using WFE :

AArch32

## Px

```
PLDW[R1] ; preload into cache in unique Loop LDAEX R5, [R1] ; read lock with acquire CMP R5, #0 ; check if 0 WFENE ; sleep if the lock is held STREXEQ R5, R0, [R1] ; attempt to store new value CMPEQ R5, #0 ; test if store succeeded BNE Loop ; retry if not
```

```
state
```

AArch64

## Px

```
SEVL ; invalidates the WFE on the first loop iteration PRFM PSTL1KEEP, [X1] ; allocate into cache in unique state Loop WFE LDAXR W5, [X1] ; read lock with acquire CBNZ W5, Loop ; check if 0 STXR W5, W0, [X1] ; attempt to store new value CBNZ W5, Loop ; test if store succeeded and retry if not ; loads and stores in the critical region can now be performed
```

And the following is an example of lock release code:

AArch32

## Px

```
; loads and stores in the critical region MOV R0, #0 STL R0, [R1] ; clear the lock
```

AArch64

## Px

```
; loads and stores in the critical region STLR WZR, [X1] ; clear the lock
```

## K11.3.4.2 Ticket lock

In the Ticket lock case, the Load-Exclusive instruction can be used to move the monitor into the exclusive state for the express purpose of creating an event when the monitor changes state:

AArch32

## Px

```
; R1 holds 2 16 bit quantities ; the lower halfword holds the current ticket number ; the higher halfword holds the next ticket number PLDW[R1] ; preload into cache in unique state Loop1 LDAEX R5, [R1] ; read current and next ADD R3, R5, #0x10000 ; increment the next number STREX R6, R3, [R1] ; and update the value CMP R6, #0 ; did the exclusive pass BNE Loop ; retry if not CMP R5, R5, ROR #16 ; is the current ticket ours MOV R6, R5 BEQ block_start SEVL Loop2 WFE ; wait if there has not been a change to the count since last ; read LDAEXH R6, [R1] ; check the current count CMP R6, R5, LSR #16 ; check if it is equal BNE Loop2 block_start
```

AArch64

Px

```
; X1 holds 2 16 bit quantities ; the lower halfword holds the current ticket number ; the higher halfword holds the next ticket number PRFM PSTL1KEEP, [X1] ; preload into cache in unique state Loop1 LDAXR W5, [X1] ; read current and next ADD W3, W5, #0x10000 ; increment the next number STXR W6, W3, [X1] ; and update the value CBNZ W6, Loop1 ; did the exclusive pass - retry if not AND W6, W5, 0xFFFF CMP W6, W5, LSR #16 ; is the current ticket ours B.EQ block_start SEVL Loop2 WFE LDAXRH W6, [X1] ; read current value CMP W6, W5, LSR #16 ; compare it with our allocated ticket B.NE Loop2 ; retry (spin) if it is not the same block_start
```