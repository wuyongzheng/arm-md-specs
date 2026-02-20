## B2.7 Caches and memory hierarchy

The implementation of a memory system depends heavily on the microarchitecture and therefore many details of the memory system are IMPLEMENTATION DEFINED. The Arm architecture defines the application level interface to the memory system, including a hierarchical memory system with multiple levels of cache. This section describes an application level view of this system. It contains the subsections:

- Introduction to caches.
- Memory hierarchy.
- Application level access to functionality related to caches
- Implication of caches for the application programmer.
- Prefetching into cache.

## B2.7.1 Introduction to caches

Acache is a block of high-speed memory that contains a number of entries, each consisting of:

- Main memory address information, commonly known as a tag .
- The associated data.

Caches increase the average speed of a memory access. Caching takes account of two principles of locality:

## Spatial locality

An access to one Location is likely to be followed by accesses to adjacent Locations. Examples of this principle are:

- Sequential instruction execution.
- Accessing a data structure.

## Temporal locality

An access to an area of memory is likely to be repeated in a short time period. An example of this principle is the execution of a software loop.

To minimize the quantity of control information stored, the spatial locality property groups several locations together under the same tag. This logical block is commonly known as a cache line . When data is loaded into a cache, access times for subsequent loads and stores are reduced, resulting in overall performance benefits. An access to information already in a cache is known as a cache hit , and other accesses are called cache misses .

Normally, caches are self-managing, with the updates occurring automatically. Whenever the PE accesses a cacheable memory location, the cache is checked. If the access is a cache hit, the access occurs in the cache. Otherwise, the access is made to memory. Typically, when making this access, a cache location is allocated and the cache line loaded from memory. The Arm architecture permits different cache topologies and access policies, provided they comply with the memory coherency model described in this manual.

Caches introduce a number of potential problems, mainly because:

- Memory accesses can occur at times other than when the programmer would expect them.
- Adata item can be held in multiple physical locations.

## B2.7.2 Memory hierarchy

Typically memory close to a PE has very low latency, but is limited in size and expensive to implement. Further from the PE it is common to implement larger blocks of memory but these have increased latency. To optimize overall performance, an Armv8 memory system can include multiple levels of cache in a hierarchical memory system that exploits this trade-off between size and latency. Figure B2-1 shows an example of such a system in an Armv8-A system that supports virtual addressing.

Figure B2-1 Multiple levels of cache in a memory hierarchy

<!-- image -->

Note

In this manual, in a hierarchical memory system, Level 1 refers to the level closest to the processing element, as shown in Figure B2-1.

Instructions and data can be held in separate caches or in a unified cache. A cache hierarchy can have one or more levels of separate instruction and data caches, with one or more unified caches that are located at the levels closest to the main memory. Memory coherency for cache topologies can be defined using the conceptual points Point of Unification (PoU), Point of Coherency (PoC), Point of Persistence (PoP), and Point of Deep Persistence (PoDP).

For more information, including the definitions of PoU, PoC, PoP, and PoDP, see About cache maintenance in AArch64 state.

If FEAT\_MTE2 is implemented, the behavior of cache maintenance instructions is modified. For more information, see Allocation Tags.

## B2.7.2.1 The cacheability and shareability memory attributes

Cacheability and shareability are two attributes that describe the memory hierarchy in a multiprocessing system:

- Cacheability

This attribute defines whether memory locations are allowed to be allocated into a cache or not. Cacheability is defined independently for Inner and Outer Cacheability locations.

- Shareability This attribute defines whether memory locations are shareable between different agents in a system. Marking a memory location as shareable for a particular domain requires hardware to ensure that the location is coherent for all agents in that domain. Shareability is defined independently for Inner and Outer Shareability domains.

For more information about Cacheability and Shareability, see Memory types and attributes.

## B2.7.3 Application level access to functionality related to caches

As indicated in About the Application level programmers' model, the application level corresponds to execution at EL0. The architecture defines a set of cache maintenance instructions that software can use to manage cache coherency. Software executing at a higher Exception level can enable use of some of this functionality from EL0, as follows:

## When the value of SCTLR\_EL1.UCI is 1

Software executing at EL0 can access:

- The data cache maintenance instructions, DC CVAU , DC CVAC , DC CVAP , DC CVADP , and DC CIVAC . See The data cache maintenance instruction ( DC ).
- The instruction cache maintenance instruction IC IVAU . See The instruction cache maintenance instruction ( IC ).

Attempted execution of these instructions might generate a Permission fault as described in Permission fault.

## When the value of SCTLR\_EL1.UCT is 1

Software executing at EL0 can access the cache type register. See CTR\_EL0.

## When the value of SCTLR\_EL1.DZE is 1

Software executing at EL0 can access the data cache zero instruction DC ZVA . See Data cache zero instruction.

The SCTLR\_EL1.{UCI, UCT, DZE} control fields are accessible only by software executing at EL1 or higher.

When the Effective value of HCR\_EL2.{E2H, TGE} is {1, 1}, the controls {UCI, UCT and DZE} are found in SCTLR\_EL2.

This functionality is UNDEFINED at EL0 when the value of the corresponding SCTLR\_EL1 control field is 0.

## B2.7.4 Implication of caches for the application programmer

In normal operation, the caches are largely invisible to the application programmer. However they can become visible when there is a breakdown in the coherency of the caches. Such a breakdown can occur:

- When memory locations are updated by other agents in the system that do not use hardware management of coherency.
- When memory updates made from the application software must be made visible to other agents in the system, without the use of hardware management of coherency.

## For example:

- In the absence of hardware management of coherency of DMA accesses, in a system with a DMA controller that reads memory locations that are held in the data cache of a PE, a breakdown of coherency occurs when the PE has written new data in the data cache, but the DMA controller reads the old data held in memory.
- In a Harvard cache implementation, where there are separate instruction and data caches, a breakdown of coherency occurs when new instruction data has been written into the data cache, but the instruction cache still contains the old instruction data.

## B2.7.4.1 Data coherency issues

Software can ensure the data coherency of caches in the following ways:

- By not using the caches in situations where coherency issues can arise. This can be achieved by:
- -Using Non-cacheable or, in some cases, Write-Through Cacheable memory.
- -Not enabling caches in the system.
- By using cache maintenance instructions to manage the coherency issues in software. See Application level access to functionality related to caches.
- By using hardware coherency mechanisms to ensure the coherency of data accesses to memory for cacheable locations by observers within the different shareability domains, see Non-shareable Normal memory and Shareable, Inner Shareable, and Outer Shareable Normal memory.

Note

The performance of these hardware coherency mechanisms is highly IMPLEMENTATION SPECIFIC. In some implementations, the mechanism suppresses the ability to cache shareable locations. In other implementations, cache coherency hardware can hold data in caches while managing coherency between observers within the shareability domains.

Note

Not all these mechanisms are directly available to software operating at EL0 and might involve interaction with software operating at a higher Exception level.

## B2.7.4.2 Synchronization and coherency issues between data and instruction accesses

How far ahead of the current point of execution instructions are fetched from is IMPLEMENTATION DEFINED. Such prefetching can be either a fixed or a dynamically varying number of instructions, and can follow any or all possible future execution paths. For all types of memory:

- The PE might have fetched the instructions from memory at any time since the last Context Synchronization event on that PE.
- Any instructions fetched in this way might be executed multiple times, if this is required by the execution of the program, without being refetched from memory. In the absence of a Context Synchronization event, there is no limit on the number of times such an instruction might be executed without being refetched from memory.

The Arm architecture requires the hardware to ensure coherency between instruction caches and memory, even for locations of shared memory. A write has been made coherent with an instruction fetch of a shareability domain when:

- CTR\_EL0.{DIC, IDC} == {0, 0} The location written to has been cleaned to the Point of unification (PoU) from the data cache, and that clean is complete for the shareability domain. Subsequently the location has been invalidated to the Point of unification (PoU) from the instruction cache, and that invalidation is complete for the shareability domain.
- CTR\_EL0.{DIC, IDC} == {0, 1} The write is complete for the shareability domain. Subsequently the location has been invalidated to the Point of unification (PoU) from the instruction cache, and that invalidation is complete for the shareability domain.
- CTR\_EL0.{DIC, IDC} == {1, 1} The write is complete for the shareability domain.

Note

Microarchitecturally, this means that these situations cannot both be true in an implementation:

- After delays in fetching from memory, the instruction queue can have entries written into it out of order.
- For an implementation:
- -When CTR\_EL0.DIC == 0, if there is an outstanding entry in the instruction queue, then later entries in the instruction queue are not impacted by the IC IV AU instructions of a different core.
- -When CTR\_EL0.DIC == 1, if there is a write to the location that is held in the queue when there is an outstanding entry in the instruction queue for an older entry, then the instruction queue does not have entries invalidated from it.

The full definition of the ordering implications of CTR\_EL0.{DIC, IDC} is covered formally in the Ordering requirements defined by the formal concurrency model and the information in this section is not intended to contradict that section.

If software requires coherency between instruction execution and memory, it must manage this coherency using Context Synchronization events and cache maintenance instructions. The following code sequence can be used to allow a PE to execute code that the same PE has written.

```
; Coherency example for data and instruction accesses within the same Inner Shareable domain. ; Enter this code with <Wt> containing a new 32-bit instruction, ; to be held in Cacheable space at a location pointed to by Xn. STR Wt, [Xn] DC CVAU, Xn ; Clean data cache by VA to point of unification (PoU) DSB ISH ; Ensure visibility of the data cleaned from cache IC IVAU, Xn ; Invalidate instruction cache by VA to PoU DSB ISH ; Ensure completion of the invalidations ISB ; Synchronize the fetched instruction stream
```

Note

- If this sequence is not executed between writing data to a location and executing the instruction at that location, the lack of coherency between instruction caches and memory means that the instructions that are executed might be the old instruction or the updated instruction, and which is used can arbitrarily vary during execution. It must not be assumed by software, before the synchronization sequence is executed, that when the updated instruction has been seen, the old instruction will not be seen again.
- For Non-cacheable or Write-Through accesses, the clean data cache by V A instruction is not required. However, the invalidate instruction cache instruction is required because the Armv8 AArch64 architecture allows Noncacheable accesses to be held in an instruction cache. See Non-cacheable accesses and instruction caches.
- This code can be used when the thread of execution modifying the code is the same thread of execution that is executing the code. The Arm architecture limits the set of instructions that can be executed by one thread of execution as they are being modified by another thread of execution without requiring explicit synchronization. See Concurrent modification and execution of instructions.
- The system software controls whether these cache maintenance instructions are available to the application level by setting SCTLR\_EL1.UCI.

## B2.7.5 Prefetching into cache

The Arm architecture provides memory system hints PRFM , PRFUM , LDNP , and STNP that software can use to communicate the expected use of memory locations to the hardware. The memory system can respond by taking actions that are expected to speed up the memory accesses if they occur. The effect of these memory system hints is IMPLEMENTATION DEFINED. Typically, implementations use this information to bring the data or instruction locations into caches.

The Prefetch instructions are hints, and so implementations can treat them as NOP s without affecting the functional behavior of the device. The instructions cannot generate synchronous Data Abort exceptions, but the resulting memory system operations might, under exceptional circumstances, generate an asynchronous External abort, which is taken using an SError exception. For more information, see ISS encoding for an exception from a Data Abort.

PrefetchHint {} defines the prefetch hint types.

The Hint\_Prefetch() function signals to the memory system that memory accesses of the type hint to or from the specified address are likely to occur in the near future. The memory system might take some action to speed up the memory accesses when they do occur, such as prefetching the specified address into one or more caches as indicated by the innermost cache level target and non-temporal hint stream .

For more information on PRFM , PRFUM and load/store instructions that provide hints to the memory system, see Prefetch memory and Load/store SIMD and floating-point non-temporal pair. For more information on SVE PRF * instructions that provide hints to the memory system, see Predicated non-contiguous element accesses.