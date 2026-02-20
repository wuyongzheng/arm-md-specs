## K11.5 Cache and TLB maintenance instructions and barriers

The following sections describe the use of barriers with cache and TLB maintenance instructions:

- Data cache maintenance instructions.
- Instruction cache maintenance instructions.
- TLB maintenance instructions and barriers.

## K11.5.1 Data cache maintenance instructions

The following sections describe the use of barriers with data cache maintenance instructions:

- Message passing to non-caching observers.
- Multiprocessing message passing to non-caching observers.
- Invalidating DMA buffers, non-functional example.
- Invalidating DMA buffers, functional example with single PE.
- Invalidating DMA buffers, functional example with multiple coherent PEs.

## K11.5.1.1 Message passing to non-caching observers

The Armv8 and later architectures require the use of DMB instructions to ensure the ordering of data cache maintenance instructions and their effects. The Load-Acquire and Store-Release instructions have no effect on cache maintenance instruction. This means the following message passing approaches can be used when communicating between caching observers and non-caching observers:

AArch32

## P1

```
STR R5, [R1] ; updates data (assumed to be in P1 cache) DCCMVAC R1 ; cleans cache to point of coherency DMB ; ensures effects of the clean will be observed before the ; flag is set STR R0, [R4] ; sends flag to external agent (Non-cacheable location)
```

```
WAIT_ACQ ([R4] == 1) ; waits for the flag (with order) LDR R5, [R1] ; reads the data
```

## AArch64

## P1

```
STR W5, [X1] ; updates data (assumed to be in P1 cache) DC CVAC, X1 ; cleans cache to point of coherency DMB ISH ; ensures effects of the clean will be observed before the ; flag is set STR W0, [X4] ; sends flag to external agent (Non-cacheable location)
```

```
WAIT_ACQ ([X4] == 1) ; waits for the flag (with order) LDR W5, [X1] ; reads the data
```

In this example, it is required that E1:R5== 0x55 .

## E1

## E1

## K11.5.1.2 Multiprocessing message passing to non-caching observers

The broadcast nature of the cache maintenance instructions combined with properties of barriers, means that the message passing principle for non-caching observers is:

AArch32

## P1

STR R5, [R1]

; updates data (assumed to be in P1 cache)

STL R0, [R2]

; sends a flag for P2 (ordered by the store release)

WAIT

([R2] ==

1)

;

waits

for P1 flag

DMB

;

ensures cache

clean

is

observed

after

P1 flag

is observed

DCCMVAC R1

;

cleans

cache

to point

of coherency

- will

clean

P1

cache

DMB

;

ensures effects

of the

clean

will

be observed

before

the

;

flag

to E1

is set

STR

R0, [R4]

;

sends

flag

to E1

WAIT\_ACQ ([R4] == 1) ; waits for P2 flag (ordered)

LDR R5, [R1]

## AArch64

## P1

STR W5, [X1]

; updates data (assumed to be in P1 cache)

STLR W0, [X2]

; sends a flag for P2 (ordered)

| WAIT ([X2] ==   | ; waits sfor P1 flag                                       |
|-----------------|------------------------------------------------------------|
| DMB SY          | ; ensure cache clean is observed after P1 flag is observed |
| DC CVAC, X1     | ; cleans cache to point of coherency, will clean P1 cache  |
| DMB SY          | ; ensures effects of the clean will be observed before the |
|                 | ; flag to E1 is set                                        |
| STR W0, [X4]    | ; sends flag to E1                                         |

WAIT\_ACQ ([X4] == 1) ; waits for P2 flag

```
LDR W5, [X1] ; reads data
```

In this example, it is required that E1:R5== 0x55 . The clean operation executed by P2 affects the data location in the P1 cache. The cast-out from the P1 cache is guaranteed to be observed before P2 updates [R4].

Note

The cache maintenance instructions are not ordered by the Load-Acquire and Store-Release instructions.

## K11.5.1.3 Invalidating DMA buffers, non-functional example

The basic scheme for communicating with an external observer that is a process that passes data in to a Cacheable memory region must take account of the architectural requirement that regions with a Normal Cacheable attribute can be allocated into a cache at any time, for example as a result of speculation. The following example shows this possibility:

AArch32

## P1

```
DCIMVAC R1 ; ensures cache is not dirty. A clean operation could be used ; but as the DMA will subsequently overwrite this region an ; invalidate operation is sufficient and usually more efficient DMB ; ensures cache invalidation is observed before the next store
```

;

reads data

## P2

## E1

P2

## E1

## E1

## E1

## E1

; is observed

STR R0, [R3]

; sends flag to external agent

WAIT\_ACQ ([R4]==1)

; waits for a different flag from an external agent

LDR R5, [R1]

WAIT ([R3] == 1)

; waits for flag

STR R5, [R1]

; stores new data

STL R0, [R4]

; sends a flag

## AArch64

## P1

```
DC IVAC, X1 ; ensure cache is not dirty. A clean operation could be used ; but as the DMA will subsequently overwrite this region an ; invalidate operation is sufficient and usually more efficient DMB SY ; ensures cache invalidation is observed before the next store ; is observed STR W0, [X3] ; sends flag to external agent WAIT_ACQ ([X4]==1) ; waits for a different flag from an external agent
```

LDR W5, [X1]

WAIT ([X3] == 1)

; waits for flag

STR W5, [X1]

; stores new data

STLR W0, [X4]

; sends a flag

If a speculative access occurs, there is no guarantee that the cache line containing [R1] is not brought back into the cache after the cache invalidation, but before [R1] is written by E1. Therefore, the result P1:R5=0 is permissible.

## K11.5.1.4 Invalidating DMA buffers, functional example with single PE

## AArch32

## P1

| DCIMVAC R1     | ; ensures cache is not dirty. A clean operation could be used ; but as the DMA will subsequently overwrite this region an ; invalidate operation is sufficient and usually more efficient   |
|----------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| DMB            | ; ensures cache invalidation is observed before the next store ; is observed                                                                                                                |
| STR R0, [R3]   | ; sends flag to external agent                                                                                                                                                              |
| WAIT ([R4]==1) | ; waits for a different flag from an external agent                                                                                                                                         |
| DMB            | ; ensures that cache invalidate is observed after the flag                                                                                                                                  |
| DCIMVAC R1     | ; ensures cache discards stale copies before use                                                                                                                                            |

WAIT ([R3] == 1)

; waits for flag

STR R5, [R1]

; stores new data

STL R0, [R4]

; sends a flag

## AArch64

## P1

DC IVAC, X1

- ; ensures cache is not dirty. A clean operation could be used

; but as the DMA will subsequently overwrite this region an

- ; invalidate operation is sufficient and usually more efficient

DMB SY

- ; ensures cache invalidation is observed before the next store

; is observed

## E1

## P1

## E1

```
WAIT ([R3] == 1) ; waits for new data request STR R5, [R1] ; sends new [R1] DMB [ST] STR R0, [R4] ; indicates that new data is available to P1
```

## AArch64

## P0

```
(Use data from [X1], potentially using [X1] as scratch space) STLR W0, [X2] ; signals release of [X1] WAIT_ACQ ([X2] == 0) ; waits for new value from DMA LDR W5, [X1]
```

```
WAIT ([X2] == 1) ; waits for release of [R1] by P0 DC IVAC, X1 ; ensures caches are not dirty, an invalidate DMB SY STR W0, [X3] ; requests new data for [R1]
```

## P1

```
STR W0, [X3] ; sends flag to external agent WAIT ([X4]==1) ; waits for a different flag from an external agent DMB SY ; ensures that cache invalidate is observed after the flag ; from external agent is observed DC IVAC, X1 ; ensures cache discards stale copies before use LDR W5, [X1]
```

```
WAIT ([X3] == 1) ; waits for flag STR W5, [X1] ; stores new data STLR W0, [X4] ; sends a flag
```

In this example, the result P1:R5 == 0x55 is required. Including a cache invalidation after the store by E1 to [R1] is observed ensures that the line is fetched from external memory after it has been updated.

## K11.5.1.5 Invalidating DMA buffers, functional example with multiple coherent PEs

The broadcasting of cache maintenance instructions, and the use of DMB instructions to ensure their observability, means that the previous example extends naturally to a multiprocessor system. Typically this requires a transfer of ownership of the region that the external observer is updating.

AArch32

## P0

```
(Use data from [R1], potentially using [R1] as scratch space) STL R0, [R2] ; signals release of [R1] WAIT_ACQ ([R2] == 0) ; waits for new value from DMA LDR R5, [R1]
```

```
WAIT ([R2] == 1) ; waits for release of [R1] by P0 DCIMVAC R1 ; ensures caches are not dirty, an invalidate is sufficient DMB STR R0, [R3] ; requests new data for [R1] WAIT ([R4] == 1) ; waits for new data DMB DCIMVAC R1 ; ensures caches discard stale copies before use DMB MOV R0, #0 STR R0, [R2] ; signals availability of new [R1]
```

```
is sufficient
```

```
WAIT ([X4] == 1) ; waits for new data DMB SY DCIMVAC X1 ; ensures caches discard stale copies before DMB SY STR WZR, [X2] ; signals availability of new [R1]
```

```
use E1 WAIT ([X3] == 1) ; waits for new data request STR W5, [X1] ; sends new [R1] STR W0, [X4] ; indicates new data is available to P1
```

In this example, the result P0:R5 == 0x55 is required. The DMB issued by P1 after the first data cache invalidation ensures that effect of the cache invalidation on P0 is seen by E1 before the store by E1 to [R1]. The DMB issued by P1 after the second data cache invalidation ensures that its effects are seen before the store of 0 to the semaphore location in [R2].

## K11.5.2 Instruction cache maintenance instructions

The following sections describe the use of barriers with instruction cache maintenance instructions:

- Ensuring the visibility of updates to instructions for a uniprocessor.
- Ensuring the visibility of updates to instructions for a multiprocessor.

## K11.5.2.1 Ensuring the visibility of updates to instructions for a uniprocessor

On a single PE, the agent that causes instruction fetches, or instruction cache linefills, is a separate memory system observer from the agent that causes data accesses. Therefore, any operations to invalidate the instruction cache can rely only on seeing updates to memory that are complete. This must be ensured by the use of a DSB instruction.

Also, instruction cache maintenance instructions are only guaranteed to complete after the execution of a DSB , and an ISB is required to discard any instructions that might have been prefetched before the instruction cache invalidation completed. Therefore, on a uniprocessor, to ensure the visibility of an update to code and to branch to it, the following sequence is required:

AArch32

## P1

```
STR R11, [R1] ; R11 contains a new instruction to be stored in program memory DCCMVAU R1 ; clean to PoU makes the new instruction visible to the instruction cache DSB ICIMVAU R1 ; ensures instruction cache/branch predictor discards stale data BPIMVA R1 DSB ; ensures completion of the invalidation ISB ; ensures instruction fetch path sees new instruction cache state BX R1
```

In AArch64 state, the branch predictor maintenance is not required.

AArch64

## P1

```
STR W11, [X1] ; W11 contains a new instruction to be stored in program memory DC CVAU, X1 ; clean to PoU makes the new instruction visible to instruction cache DSB ISH IC IVAU, X1 ; ensures instruction cache/branch predictor discards stale data DSB ISH ; ensures completion of the invalidation ISB ; ensures instruction fetch path sees new instruction cache state BR X1
```

## Note

Where the changes to the instructions span multiple cache lines, then the data cache and instruction cache maintenance instructions can be duplicated to cover each of the lines to be cleaned and to be invalidated.

## K11.5.2.2 Ensuring the visibility of updates to instructions for a multiprocessor

The Armv8 and later architectures require a PE that executes an instruction cache maintenance instruction to execute a DSB instruction to ensure completion of the maintenance operation. This ensures that the cache maintenance instruction is complete on all PEs in the Inner Shareable shareability domain.

An ISB is not broadcast, and so does not affect other PEs. This means that any other PE must perform its own ISB synchronization after it knows that the update is visible, if it is necessary to ensure its synchronization with the update. The following example shows how this might be done:

AArch32

## P1

| STR R11, [R1] DCCMVAU R1 DSB ICIMVAU R1 BPIMVA R DSB   | ; R11 contains a new instruction to be stored in program memory ; clean to PoU makes the new instruction visible to the instruction cache ; ensures completion of the clean on all PEs ; ensures instruction cache discards stale data ; ensures branch predictor discards stale data ; ensures completion of the instruction cache and branch predictor   |
|--------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

## P2-P x

| WAIT ([R2] == 1)   | ; waits for flag signalling completion   |
|--------------------|------------------------------------------|
| ISB                | ; synchronizes context on this PE        |
| BX R1              | ; branches to new code                   |

## AArch64

## P1

| STR X11, [X1]   | ; X11 contains a new instruction to be stored in program memory           |
|-----------------|---------------------------------------------------------------------------|
| DC CVAU, X1     | ; clean to PoU makes the new instruction visible to the instruction cache |
| DSB ISH         | ; ensures completion of the clean on all PEs                              |
| IC IVAU, X1     | ; ensures instruction cache/branch predictor discards stale data          |
| DSB ISH         | ; ensures completion of the instruction cache/branch predictor            |
|                 | ; invalidation on all PEs                                                 |
| STR W0, [X2]    | ; sets flag to signal completion                                          |
| ISB             | ; synchronizes context on this PE                                         |
| BR R1           | ; branches to new code                                                    |

## P2-P x

| WAIT ([X2] == 1)   | ; waits for flag signalling completion   |
|--------------------|------------------------------------------|
| ISB                | ; synchronizes context on this PE        |
| BR X1              | ; branches to new code                   |

## K11.5.2.2.1 Nonfunctional approach

The following sequence does not have the same effect, because a DSB is not required to complete the instruction cache maintenance instructions that other PEs issue:

## AArch32

## P1

```
STR R11, [R1] ; R11 contains a new instruction to be stored in program memory DCCMVAU R1 ; clean to PoU makes the new instruction visible to the instruction cache DSB ; ensures completion of the clean on all PEs ICIMVAU R1 ; ensures instruction cache discards stale data BPIMVA R1 : ensures branch predictor discards stale data DMB ; ensures ordering of the store after the invalidation ; DOES NOT guarantee completion of instruction cache/branch ; predictor on other PEs
```

| STR R0,   | ; sets flag to signal completion                    |
|-----------|-----------------------------------------------------|
| DSB       | ; ensures completion of the invalidation on all PEs |
| ISB       | ; synchronizes context on this PE                   |
| BX R1     | ; branches to new code                              |

## P2-P x

WAIT ([R2] == 1)

; waits for flag signalling completion

DSB

; this DSB does not guarantee completion of P1

; ICIMVAU/BPIMVA

ISB

BX R1

## AArch64

## P1

| STR W11, [X1]   | ; W11 contains a new instruction to be stored in program memory       |
|-----------------|-----------------------------------------------------------------------|
| DC CVAU, X1     | ; clean to PoU makes the new instruction visible to instruction cache |
| DSB ISH         | ; ensures completion of the clean on all PEs                          |
| IC IVAU, X1     | ; ensures instruction cache/branch predictor discards stale data      |
| DMB ISH         | ; ensures ordering of the store after the invalidation                |
|                 | ; DOES NOT guarantee completion of instruction cache/branch           |
|                 | ; predictor on other PEs                                              |
| STR W0, [X2]    | ; sets flag to signal completion                                      |
| DSB ISH         | ; ensures completion of the invalidation on all PEs                   |
| ISB             | ; synchronizes context on this PE                                     |
| BR X1           | ; branches to new code                                                |

## P2-P x

WAIT ([X2] == 1)

; waits for flag signalling completion

DSB ISH

; this DSB does not guarantee completion of P1

; ICIMVAU/BPIMVA

ISB

BR X1

In this example, P2 . . . P x might not see the updated region of code at R1.

## K11.5.3 TLB maintenance instructions and barriers

The following sections describe the use of barriers with TLB maintenance instructions:

- Ensuring the visibility of updates to translation tables for a uniprocessor.
- Ensuring the visibility of updates to translation tables for a multiprocessor.
- Paging memory in and out.
- Using break-before-make when updating translation table entries.

## K11.5.3.1 Ensuring the visibility of updates to translation tables for a uniprocessor

On a single PE, the agent that causes translation table walks is a separate memory system observer from the agent that causes data accesses. Therefore, any operations to invalidate the TLB can only rely on seeing updates to memory that are complete. This must be ensured by the use of a DSB instruction.

The Armv8 and later architectures require that translation table walks look in the data or unified caches at L1, so such systems do not require data cache cleaning.

After the translation tables update, any old copies of entries that might be held in the TLBs must be invalidated. This operation is only guaranteed to affect all instructions, including instruction fetches and data accesses, after the execution of a DSB and an ISB . Therefore, the code for updating a translation table entry is:

AArch32

P1

```
STR R11, [R1] ; updates the translation table entry DSB ; ensures visibility of the update to translation table walks TLBIMVA R10 BPIALL DSB ; ensures completion of the BP and TLB invalidation ISB ; synchronises context on this PE ; new translation table entry can be relied upon at this point and all accesses ; generated by this observer using ; the old mapping have been completed
```

AArch64

## P1

```
STR X11, [X1] ; updates the translation table entry DSB ISH ; ensures visibility of the update to translation table walks TLBI VAE1, X10 ; assumes we are in the EL1 DSB ISH ; ensures completion of the TLB invalidation ISB ; synchronise context on this PE ; new translation table entry can be relied upon at this point and all accesses ; generated by this observer using ; the old mapping have been completed
```

Importantly, by the end of this sequence, all accesses that used the old translation table mappings have been observed by all observers.

An example of this is where a translation table entry is marked as invalid. Such a system must provide a mechanism to ensure that any access to a region of memory being marked as invalid has completed before any action is taken as a result of the region being marked as invalid.

## K11.5.3.2 Ensuring the visibility of updates to translation tables for a multiprocessor

The same code sequence can be used in a multiprocessing system. The Armv8 and later architectures require a PE that executes a TLB maintenance instruction to execute a DSB instruction to ensure completion of the maintenance operation. This ensures that the TLB maintenance instruction is complete on all PEs in the Inner Shareable shareability domain.

The completion of a DSB that completes a TLB maintenance instruction ensures that all accesses that used the old mapping have completed.

AArch32

P1

```
STR R11, [R1] ; updates the translation table entry DSB ; ensures visibility of the update to translation table walks TLBIMVAIS R10 BPIALLIS DSB ; ensures completion of the BP and TLB invalidation ISB ; Note ISB is not broadcast and must be executed locally ; on other PEs ; new translation table entry can be relied upon at this point and all accesses ; generated by any observers affected by the broadcast TLBIMVAIS operation using ; the old mapping have been completed
```

## AArch64

## P1

```
STR X11, [X1] ; updates the translation table entry DSB ISH ; ensures visibility of the update to translation table walks TLBI VAE1IS, X10 DSB ISH ; ensures completion of the TLB invalidation ISB ; Note ISB is not broadcast and must be executed locally ; on other PEs ; new translation table entry can be relied upon at this point and all accesses ; generated by any observers affected by the broadcast TLBIMVAIS operation using ; the old mapping have been completed
```

The completion of the TLB maintenance instruction is guaranteed only by the execution of a DSB by the observer that performed the TLB maintenance instruction. The execution of a DSB by a different observer does not have this effect, even if the DSB is known to be executed after the TLB maintenance instruction is observed by that different observer.

## K11.5.3.3 Paging memory in and out

In a multiprocessor system there is a requirement to ensure the visibility of translation table updates when paging regions of memory into RAM from a backing store. This might, or might not, also involve paging existing locations in memory from RAM to a backing store. In such situations, the operating system selects one or more pages of memory that might be in use but are suitable to discard, with or without copying to a backing store, depending on whether the region of memory is writable. Disabling the translation table mappings for a page, and ensuring the visibility of that update to the translation tables, prevents agents accessing the page.

For this reason, it is important that the DSB that is performed after the TLB invalidation ensures that no other updates to memory using those mappings are possible.

An example sequence for the paging out of an updated region of memory, and the subsequent paging in of memory, is as follows:

AArch32

## P1

```
STR R11, [R1] ; updates the translation table for the region being paged out DSB ; ensures visibility of the update to translation table walks TLBIMVAIS R10 ; invalidates the old entry DSB ; ensures completion of the invalidation on all PEs ISB ; ensures visibility of the invalidation BL SaveMemoryPageToBackingStore BL LoadMemoryFromBackingStore DSB ; ensures completion of the memory transfer (this could be part of ; LoadMemoryFromBackingStore) ICIALLUIS ; also invalidates the branch predictor DSB ; ensures completion of the instruction cache ; and branch predictor invalidation STR R9, [R1] ; creates a new translation table entry with a new mapping DSB ; ensures visibility of the new translation table mapping ISB ; ensures synchronisation of this instruction stream
```

AArch64

P1

```
STR X11, [X1] ; updates the translation table for the region being paged out DSB ISH ; ensures visibility of the update to translation table walks TLBI VAE1IS, X10 ; invalidates the old entry DSB ISH ; ensures completion of the invalidation on all PEs ISB ; ensures visibility of the invalidation BL SaveMemoryPageToBackingStore BL LoadMemoryFromBackingStore DSB ISH ; ensures completion of the memory transfer (this could be part of ; LoadMemoryFromBackingStore) IC IALLUIS ; also invalidates the branch predictor DSB ISH ; ensures completion of the instruction cache ; and branch predictor invalidation STR X9, [X1] ; creates a new translation table entry with a new mapping DSB ISH ; ensures visibility of the new translation table mapping ISB ; ensures synchronisation of this instruction stream
```

This example assumes the memory copies are performed by an observer that is coherent with the caches of PE P1. This observer might be P1 itself, using a specific paging mapping. For clarity, the example omits the functional descriptions of SaveMemoryPageToBackingStore and LoadMemoryFromBackingStore . LoadMemoryFromBackingStore is required to ensure that the memory updates that it makes are visible to instruction fetches.

In this example, the use of ICIALLUIS in AArch32 state and IC IALLUIS in AArch64 state to invalidate the entire instruction cache is a simplification that might not be optimal for performance. An alternative approach involves invalidating all of the lines in the caches using ICIMV AU in AArch32 state and IC IV AU operations in AArch64 state. This invalidation must be done when the mapping used for the ICIMVAU and IC IVAU operations is valid but not executable.

## K11.5.3.4 Using break-before-make when updating translation table entries

The Arm Architecture requires that reads to the same location are observed in order, and since application level software relies on this behavior, the operating system needs to maintain this illusion when it is changing a virtual to physical address mapping for a location, as is the case with copy on write or other memory management techniques. This illusion can be maintained provided that the software uses a break-before-make sequence when updating translation table entries whenever multiple threads of execution can use the same translation tables and the change to the translation entries involves any of:

- Changing the memory type.
- Changing the cacheability attributes
- Changing the output address (OA), if the OA of at least one of the old translation table entry and the new translation table entry is writable.

The architecture requires use of a break-before make sequence in these situations, see Using break-before-make when updating translation table entries for more information. However, if software did not use a break-before-make approach, an implementation might give a result that would occur if the two reads to the same virtual address did not occur in program order. An example of such an occurrence would be an implementation of copy-on-write, where one PE is performing two reads to the same virtual address at the same time as a second PE, running code associated with the operating system, is copying the data from one physical location that is mapped to by that virtual address, where the page was mapped as read-only, to a different physical location which will be mapped as read/write.

If the operating system changed the address mapping without going through an invalid entry, then it would be possible for a third PE to perform a write to the location that would be seen by the first load by the first PE, and not seen by the second load by the same PE.

The required break-before-make code sequence in this case is:

AArch32

P1

```
; R1, R2 contain an invalid translation table entry (that is, one with bit[0] == 0) ; R3 contains the address of the translation table entry ; R4 contains the Virtual Address and ASID of the VA being remapped ; R5, R6 contain the new valid translation table entry STRD R1, R2, [R3] ; stores invalid entry
```

```
DSB ISH ; ensures visibility of the update to translation table walks
```

```
TLBIMVAIS R4 ; invalidates the old entry DSB ISH ; ensures completion of the invalidation on all PEs ICIALLUIS ; also invalidates the branch predictor STRD R5, R6, [R3] ; store new mapping DSB ISH ; ensures visibility of the update to translation table walks ISB ; ensures synchronisation of this instruction stream
```

## Note

This example shows an update to an entry in a translation table that is using the long-descriptor format.

AArch64

## P1

```
; X1 contains an invalid translation table entry (that is, one with bit[0] == 0) ; X2 contains the address of the translation table entry ; X3 contains the Virtual Address and ASID of the VA being remapped ; X4 contains the new valid translation table entry STR X1, [X2] ; stores invalid entry DSB ISH ; ensures visibility of the update to translation table walks TLBI VAE1IS, X3 ; invalidates the old entry DSB ISH ; ensures completion of the invalidation on all PEs IC IALLUIS ; also invalidates the branch predictor STR X4, [X2] ; store new mapping DSB ISH ; ensures visibility of the update to translation table walks ISB ; ensures synchronisation of this instruction stream
```

If this sequence is correctly followed, then the architecture guarantees that the loads to a virtual address being remapped will be seen in the correct order.

The instruction cache maintenance is only required if the mapping from input address to output address has been changed as part of the change of the translation table entries, and the memory being moved is executable.

In this example, the use of ICIALLUIS in AArch32 state and IC IALLUIS in AArch64 state to invalidate the entire instruction cache is a simplification that might not be optimal for performance. An alternative approach involves invalidating all of the lines in the caches using ICIMVAU in AArch32 state, and IC IVAU in AArch64 state. This invalidation must be done when the mapping used for the ICIMVAU and IC IVAU operations is valid but not executable.

## K11.5.4 Ordering of Memory-mapped device control with payloads

With a Memory-mapped peripheral, such as a DMA, which can also access memory for its own use, it is common to have control or status registers which are Memory-mapped. These registers need to be accessed in an ordered manner with respect to the data that the Memory-mapped peripheral is handling.

Two simple examples of this are:

- When a processing element is writing a buffer of data, and then writing to a control register in the DMA peripheral to start that peripheral to access the buffer of data.
- When a DMA peripheral has written to a buffer of data in memory, and the processing element is reading a status register to determine that the DMA transfer has completed, and then is reading the data.

For the case of the processing element writing a buffer of data, before starting the DMA peripheral, the ordering requirements between the stores to the data buffer and the stores to the Memory-mapped a to the DMA peripheral can be met by the insertion of a DSB &lt;domain&gt; instruction between these sets of accesses as this ensures the global observation of the stores before the DMA is started. this is shown by the following code:

AArch32

P1

```
STR R5, [R2] ; data written to the data buffer DSB STR R0, [R4] ; R4 contains the address of the DMA control register
```

AArch64

## P1

| STR W5, [X2]   | ; data written to the data buffer                     |
|----------------|-------------------------------------------------------|
| DSB <domain>   |                                                       |
| STR W0, [X4]   | ; X4 contains the address of the DMA control register |

For the case of DMA peripheral writing the data buffer and then setting a status register when those stores are complete (and so globally observed) and then having this status register polled by the processing element before the processing element reads the data buffer, the processing element must insert a DSB &lt;domain&gt; between the load that reads the status register, and the read of the buffer. A DMB, or load-acquire, is not sufficient as this problem is not solely concerned with observation order, since the polling read is actually a read of a status register at a Completer, not the polling a data value that has been written by an observer.

For this case, the code is therefore:

AArch32

## P1

| WAIT ([R4] == 1)   | ; R4 contains the address of the status register, ; and the value '1' indicates completion of the DMA transfer   |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| DSB                |                                                                                                                  |
| LDR R5, [R2]       | ; reads data from the data buffer                                                                                |

## AArch64

## P1

| WAIT ([X4] == 1)   | ; X4 contains the address of the status register, ; and the value '1' indicates completion of the DMA transfer   |
|--------------------|------------------------------------------------------------------------------------------------------------------|
| DSB <domain>       |                                                                                                                  |
| LDR W5, [X2]       | ; reads data from the data buffer                                                                                |

## Appendix K12 Random Number Generation

This appendix provides further information on the generation of random numbers using FEAT\_RNG. It contains the following section:

- Properties of the generated random number.