## E2.10 Synchronization and semaphores

The architecture provides non-blocking synchronization of shared memory, using synchronization primitives . The information in this section about memory accesses by synchronization primitives applies to accesses to both Normal and Device memory.

Note

Use of the synchronization primitives scales for multiprocessing system designs.

Table E2-6 shows the synchronization primitives and the associated CLREX instruction.

Table E2-6 Synchronization primitives and associated instruction, T32 and A32 instruction sets

| Transaction size   | Additional semantics       | Load-Exclusive a   | Store-Exclusive a   | Other a   |
|--------------------|----------------------------|--------------------|---------------------|-----------|
| Byte               | -                          | LDREXB             | STREXB              | -         |
|                    | Load-Acquire/Store-Release | LDAEXB             | STLEXB              | -         |
| Halfword           | -                          | LDREXH             | STREXH              | -         |
|                    | Load-Acquire/Store-Release | LDAEXH             | STLEXH              | -         |
| Word               | -                          | LDREX              | STREX               | -         |
|                    | Load-Acquire/Store-Release | LDAEX              | STLEX               | -         |
| Doubleword         | -                          | LDREXD             | STREXD              | -         |
|                    | Load-Acquire/Store-Release | LDAEXD             | STLEXD              | -         |
| None               | Clear-Exclusive            | -                  | -                   | CLREX     |

Load-Exclusive/Store-Exclusive instruction pair. The model for the use of a Load-Exclusive/Store-Exclusive instruction

Except for the row showing the CLREX instruction, the two instructions in a single row are a pair accessing a non-aborting memory address x is:

- The Load-Exclusive instruction reads a value from memory address x .
- The corresponding Store-Exclusive instruction succeeds in writing back to memory address x only if no other observer, process, or thread has performed a more recent store to address x . The Store-Exclusive instruction returns a status bit that indicates whether the memory write succeeded.

ALoad-Exclusive instruction marks a small block of memory for exclusive access. The size of the marked block is IMPLEMENTATION DEFINED, see Marking and the size of the marked memory block. A Store-Exclusive instruction to any address in the marked block clears the marking.

Note

In this section, the term PE includes any observer that can generate a Load-Exclusive or a Store-Exclusive instruction.

The following sections give more information:

- Exclusive access instructions and Non-shareable memory locations.
- Exclusive access instructions and shareable memory locations.
- Marking and the size of the marked memory block.
- Context switch support.
- Load-Exclusive and Store-Exclusive instruction usage restrictions.
- Use of WFE and SEV instructions by spin-locks.

## E2.10.1 Exclusive access instructions and Non-shareable memory locations

For memory locations for which the Shareability attribute is Non-shareable, the exclusive access instructions rely on a local Exclusives monitor , or local monitor , that marks any address from which the PE executes a Load-Exclusive instruction. Any non-aborted attempt by the same PE to use a Store-Exclusive instruction to modify any address is guaranteed to clear the marking.

ALoad-Exclusive instruction performs a load from memory, and:

- The executing PE marks the physical memory address for exclusive access.
- The local monitor of the executing PE transitions to the Exclusive Access state.

AStore-Exclusive instruction performs a conditional store to memory that depends on the state of the local monitor:

## If the local monitor is in the Exclusive Access state

- If the address of the Store-Exclusive instruction is the same as the address that has been marked in the monitor by an earlier Load-Exclusive instruction, then the store occurs. Otherwise, it is IMPLEMENTATION DEFINED whether the store occurs.
- Astatus value is returned to a register:
- -If the store took place the status value is 0.
- -Otherwise, the status value is 1.
- The local monitor of the executing PE transitions to the Open Access state.

When an Exclusives monitor is in the Exclusive Access state the monitor is set.

## If the local monitor is in the Open Access state

- No store takes place.
- Astatus value of 1 is returned to a register.
- The local monitor remains in the Open Access state.

When an Exclusives monitor is in the Exclusive Access state the monitor is clear.

The Store-Exclusive instruction defines the register to which the status value is returned.

When a PE writes using any instruction other than a Store-Exclusive instruction:

- If the write is to a PA that is not marked as Exclusive Access by its local monitor and that local monitor is in the Exclusive Access state it is IMPLEMENTATION DEFINED whether the write affects the state of the local monitor.
- If the write is to a PA that is marked as Exclusive Access by its local monitor it is IMPLEMENTATION DEFINED whether the write affects the state of the local monitor.

It is IMPLEMENTATION DEFINED whether a store to a marked PA causes a mark in the local monitor to be cleared if that store is by an observer other than the one that caused the PA to be marked.

Figure E2-4 shows the state machine for the local monitor and the effect of each of the operations shown in the figure.

<!-- image -->

Figure E2-4 Local monitor state machine diagram

For more information about marking, see Marking and the size of the marked memory block.

Note

For the local monitor state machine, as shown in Figure E2-4:

- The IMPLEMENTATION DEFINED options for the local monitor are consistent with the local monitor being constructed so that it does not hold any PA, but instead treats any access as matching the address of the previous LoadExclusive instruction.
- A local monitor implementation can be unaware of Load-Exclusive and Store-Exclusive instructions from other PEs.
- The architecture does not require a load instruction, by another PE, that is not a Load-Exclusive instruction, to have any effect on the local monitor.
- It is IMPLEMENTATION DEFINED whether the transition from Exclusive Access to Open Access state occurs when the Store or StoreExcl is from another observer.

## E2.10.1.1 Changes to the local monitor state resulting from speculative execution

The architecture permits a local monitor to transition to the Open Access state as a result of speculation, or from some other cause. This is in addition to the transitions to Open Access state caused by the architectural execution of an operation shown in Figure E2-4.

An implementation must ensure that:

- The local monitor cannot be seen to transition to the Exclusive Access state except as a result of the architectural execution of one of the operations shown in Figure E2-4.
- Any transition of the local monitor to the Open Access state not caused by the architectural execution of an operation shown in Figure E2-4 must not indefinitely delay forward progress of execution.

## E2.10.2 Exclusive access instructions and shareable memory locations

In the context of this section, a shareable memory location is a memory location that has, or is treated as if it has, a Shareability attribute of Inner Shareable or Outer Shareable.

For shareable memory locations, exclusive access instructions rely on:

- A local monitor for each PE in the system, which marks any address from which the PE executes a Load-Exclusive. The local monitor operates as described in Exclusive access instructions and Non-shareable

memory locations, except that for shareable memory any Store-Exclusive is then subject to checking by the global monitor if it is described in that section as doing at least one of the following:

- Updating memory.

- Returning a status value of 0.

The local monitor can ignore accesses from other PEs in the system.

- A global monitor that marks a PA as exclusive access for a particular PE. This marking is used later to determine whether a Store-Exclusive to that address that has not been failed by the local monitor can occur. Any successful write to the marked block by any other observer in the Shareability domain of the memory location is guaranteed to clear the marking. For each PE in the system, the global monitor:

- Can hold at least one marked block.

- Maintains a state machine for each marked block it can hold.

Note

For each PE, the architecture only requires global monitor support for a single marked address. Any situation that might benefit from the use of multiple marked addresses on a single PE is CONSTRAINED UNPREDICTABLE, see Load-Exclusive and Store-Exclusive instruction usage restrictions.

Note

The global monitor can either reside in a block that is part of the hardware on which the PE executes or exist as a secondary monitor at the memory interfaces. The IMPLEMENTATION DEFINED aspects of the monitors mean that the global monitor and local monitor can be combined into a single unit, provided that the unit performs the global monitor and local monitor functions defined in this manual.

For shareable memory locations, in some implementations and for some memory types, the properties of the global monitor require functionality outside the PE. Some system implementations might not implement this functionality for all locations of memory. In particular, this can apply to:

- Any type of memory in the system implementation that does not support hardware cache coherency.

- Non-cacheable memory, or memory treated as Non-cacheable, in an implementation that does support hardware cache coherency.

In such a system, it is defined by the system:

- Whether the global monitor is implemented.

- If the global monitor is implemented, which address ranges or memory types it monitors.

Note

To support the use of the Load-Exclusive/Store-Exclusive mechanism when address translation is disabled, a system might define at least one location of memory, of at least the size of the translation granule, in the system memory map to support the global monitor for all PEs within a common Inner Shareable domain. However, this is not an architectural requirement. Therefore, architecturally-compliant software that requires mutual exclusion must not rely on using the Load-Exclusive/Store-Exclusive mechanism, and must instead use a software algorithm such as Lamport's Bakery algorithm to achieve mutual exclusion.

Because implementations can choose which memory types are treated as Non-cacheable, the only memory types for which it is architecturally guaranteed that a global Exclusives monitor is implemented are:

- Inner Shareable, Inner Write-Back, Outer Write-Back Normal memory.

- Outer Shareable, Inner Write-Back, Outer Write-Back Normal memory.

If the global monitor is not implemented for an address range or memory type, then performing a Load-Exclusive/Store-Exclusive instruction to such a location has one or more of the following effects:

- The instruction generates an External abort.

- The instruction generates an IMPLEMENTATION DEFINED MMU fault. This is reported using the Fault status code of:

- -DFSR.STATUS = 0b110101 when using the Long-descriptor translation table format. The fault can also be reported in the HSR.ISS[5:0] field for exceptions to Hyp mode.
- -DFSR.FS = 0b10101 when using the Short-descriptor translation table format.

If the IMPLEMENTATION DEFINED MMU fault is generated for the Non-secure PL1&amp;0 translation regime then:

- -If the fault is generated because of the memory type defined in the first stage of translation, or if the second stage of translation is disabled, then this is a first stage fault and the exception is taken to EL1.
- -Otherwise, the fault is a second stage fault and the exception is taken to EL2.

The priority of this fault is IMPLEMENTATION DEFINED.

- The instruction is treated as a NOP .
- The Load-Exclusive instruction is treated as if it were accessing a Non-shareable location, but the state of the local monitor becomes UNKNOWN.
- The Store-Exclusive instruction is treated as if it were accessing a Non-shareable location, but the state of the local monitor becomes UNKNOWN.
- The value held in the result register of the Store-Exclusive instruction becomes UNKNOWN.

In addition, for write transactions generated by non-PE observers that do not implement exclusive accesses or other atomic access mechanisms, the effect that writes have on the global and local monitors used by an Arm PE is IMPLEMENTATION DEFINED. The writes might not clear the global monitors of other PEs for:

- Some address ranges.
- Some memory types.

## E2.10.2.1 Operation of the global Exclusives monitor

ALoad-Exclusive instruction from shareable memory performs a load from memory, and causes the PA of the access to be marked as exclusive access for the requesting PE. This access can also cause the exclusive access mark to be removed from any other PA that has been marked by the requesting PE.

Note

The global monitor only supports a single outstanding exclusive access to shareable memory for each PE.

ALoad-Exclusive instruction by one PE has no effect on the global monitor state for any other PE.

AStore-Exclusive instruction performs a conditional store to memory:

- The store is guaranteed to succeed only if the PA accessed is marked as exclusive access for the requesting PE and both the local monitor and the global monitor state machines for the requesting PE are in the Exclusive Access state. In this case:
- -Astatus value of 0 is returned to a register to acknowledge the successful store.
- -The final state of the global monitor state machine for the requesting PE is IMPLEMENTATION DEFINED.
- -If the address accessed is marked for exclusive access in the global monitor state machine for any other PE then that state machine transitions to Open Access state.
- If no address is marked as exclusive access for the requesting PE, the store does not succeed:
- -Astatus value of 1 is returned to a register to indicate that the store failed.
- -The global monitor is not affected and remains in Open Access state for the requesting PE.
- If a different PA is marked as exclusive access for the requesting PE, it is IMPLEMENTATION DEFINED whether the store succeeds or not:
- -If the store succeeds a status value of 0 is returned to a register, otherwise a value of 1 is returned.
- -If the global monitor state machine for the PE was in the Exclusive Access state before the Store-Exclusive instruction it is IMPLEMENTATION DEFINED whether that state machine transitions to the Open Access state.

The Store-Exclusive instruction defines the register to which the status value is returned.

In a shared memory system, the global monitor implements a separate state machine for each PE in the system. The state machine for accesses to shareable memory by PE(n) can respond to all the shareable memory accesses visible to it. This means it responds to:

- Accesses generated by PE(n).
- Accesses generated by the other observers in the Shareability domain of the memory location. These accesses are identified as (!n).

In a shared memory system, the global monitor implements a separate state machine for each observer that can generate a Load-Exclusive or a Store-Exclusive instruction in the system.

## Aglobal monitor:

- In the Exclusive Access state is set .
- In the Open Access state is clear .

## E2.10.2.1.1 Clear global monitor event

Whenever the global monitor state for a PE changes from Exclusive access to Open access, an event is generated and held in the Event register for that PE. This register is used by the Wait for Event mechanism, see Wait For Event and Send Event.

Figure E2-5 shows the state machine for PE(n) in a global monitor.

<!-- image -->

Figure E2-5 Global monitor state machine diagram for PE(n) in a multiprocessor system

For more information about marking, see Marking and the size of the marked memory block.

Note

For the global monitor state machine, as shown in Figure E2-5:

- The architecture does not require a load instruction by another PE, that is not a Load-Exclusive instruction, to have any effect on the global monitor.
- Whether a Store-Exclusive instruction successfully updates memory or not depends on whether the address accessed matches the marked shareable memory address for the PE issuing the Store-Exclusive instruction, and whether the local and global monitors are in the exclusive state. For this reason, Figure E2-5 shows only how the operations by (!n) cause state transitions of the state machine for PE(n).
- A Load-Exclusive instruction can update only the marked shareable memory address for the PE issuing the Load-Exclusive instruction.
- When the global monitor is in the Exclusive Access state, it is IMPLEMENTATION DEFINED whether a CLREX instruction causes the global monitor to transition from Exclusive Access to Open Access state.
- It is IMPLEMENTATION DEFINED:
- -Whether a modification to a Non-shareable memory location can cause a global monitor to transition from Exclusive Access to Open Access state.
- -Whether a Load-Exclusive instruction to a Non-shareable memory location can cause a global monitor to transition from Open Access to Exclusive Access state.

## E2.10.3 Marking and the size of the marked memory block

When a Load-Exclusive instruction is executed, the resulting marked block ignores the least significant bits of the 64-bit memory address.

When a Load-Exclusive instruction is executed, a marked block of size 2 a bytes is created by ignoring the least significant bits of the memory address. A marked address is any address within this marked block. The size of the marked memory block is called the Exclusives reservation granule . The Exclusives reservation granule is IMPLEMENTATION DEFINED in the range 4 - 512 words.

Note

This definition means that the Exclusives reservation granule is:

- 4 words in an implementation where a is 4.
- 512 words in an implementation where a is 11.

For example, in an implementation where a is 4, a successful LDREXB of address 0x341B4 defines a marked block using bits[47:4] of the address. This means that the four words of memory from 0x341B0 to 0x341BF are marked for exclusive access.

In some implementations the CTR identifies the Exclusives reservation granule, see CTR. Otherwise, software must assume that the maximum Exclusives reservation granule, 512 words, is implemented.

## E2.10.4 Context switch support

An exception return clears the local monitor. As a result, performing a CLREX instruction as part of a context switch is not required in most situations.

Note

Context switching is not an application level operation. However, this information is included here to complete the description of the exclusive operations.

## E2.10.5 Load-Exclusive and Store-Exclusive instruction usage restrictions

The Load-Exclusive and Store-Exclusive instructions are intended to work together as a pair, for example a LDREX/STREX pair or a LDREXB/STREXB pair, executed as part of a loop that contains only a single Load-Exclusive and

Store-Exclusive pair. To support different implementations of these functions, software must follow the notes and restrictions given in this subsection.

The following notes describe use of a Load-Exclusive/ Store-Exclusive instruction pair, LoadExcl / StoreExcl , to indicate the use of any of the Load-Exclusive/Store-Exclusive instruction pairs shown in Table E2-6. In this context, a LoadExcl / StoreExcl pair comprises two instructions in the same thread of execution:

- The exclusives support a single outstanding exclusive access for each PE thread that is executed. The architecture makes use of this by not requiring an address or size check as part of the IsExclusiveLocal() function. If the target V A of a StoreExcl is different from the V A of the preceding LoadExcl instruction in the same thread of execution, behavior can be CONSTRAINED UNPREDICTABLE with the following behavior:

- The StoreExcl either passes or fails, the status value returned by the StoreExcl is UNKNOWN, and the states of the local and global monitors for that PE are UNKNOWN.

Note

This means the StoreExcl might pass for some instances of a LoadExcl / StoreExcl pair with mismatched addresses, and fail for other instances of a LoadExcl / StoreExcl pair with mismatched addresses.

- The data at the address accessed by the LoadExcl , and at the address accessed by the StoreExcl , is UNKNOWN.

This means software can rely on a LoadExcl / StoreExcl pair to eventually succeed only if the LoadExcl and the StoreExcl are executed with the same V A.

- An implementation of the Load-Exclusive and Store-Exclusive instructions can require that, in any thread of execution, the transaction size of a StoreExcl instruction is the same as the transaction size of the preceding LoadExcl instruction executed in that thread. If the transaction size of a StoreExcl instruction is different from the preceding LoadExcl instruction in the same thread of execution, behavior can be CONSTRAINED UNPREDICTABLE with the following behavior:

- The StoreExcl either passes or fails, and the status value returned by the StoreExcl is UNKNOWN.

Note

This means the StoreExcl might pass for some instances of a LoadExcl / StoreExcl pair with mismatched transaction sizes, and fail for other instances of a LoadExcl / StoreExcl pair with mismatched transaction sizes.

- The block of data of the size of the larger of the transaction sizes used by the LoadExcl / StoreExcl pair at the address accessed by the LoadExcl / StoreExcl pair, is UNKNOWN.

This means software can rely on a LoadExcl / StoreExcl pair to eventually succeed only if the LoadExcl and the StoreExcl have the same transaction size.

- If FEAT\_LSE is not implemented, LoadExcl / StoreExcl loops are guaranteed to make forward progress only if, for any LoadExcl / StoreExcl loop within a single thread of execution, the software meets all of the following conditions. If FEAT\_LSE is implemented, software can maximize the likelihood that LoadExcl / StoreExcl loops make forward progress, for any LoadExcl / StoreExcl loop within a single thread of execution, by meeting all of the following conditions:

1

- Between the Load-Exclusive and the Store-Exclusive, there are no explicit memory effects, software prefetches, direct or indirect System register writes, address translation instructions, cache or TLB maintenance instructions, exception generating instructions, exception returns, ISB barriers, indirect branches, or Branch with Link instructions.

- 2 Between the Store-Exclusive returning a failing result and the retry of the corresponding Load-Exclusive:

- There are no stores or PLDW instructions to any address within the Exclusives reservation granule accessed by the Store-Exclusive. This includes to V A aliases to those addresses.

- There are no loads or prefetches to any address within the Exclusives reservation granule accessed by the Store-Exclusive that use a different V A alias to that address.

- There are no other Store-Exclusive instructions to any other address.

- There are no direct or indirect System register writes, other than changes to the flag fields in the CPSR or FPSCR, caused by data processing or comparison instructions.

- There are no direct or indirect address translation instructions, cache or TLB maintenance instructions, exception generating instructions, exception returns, indirect branches, or Branch with Link instructions.

- All loads and stores are to a block of contiguous virtual memory of not more than 512 bytes in size.

The Exclusives monitor can be cleared at any time without an application-related cause, provided that such clearing is not systematically repeated so as to prevent the forward progress in finite time of at least one of the threads that is accessing the Exclusives monitor. However, it is permissible for the LoadExcl / StoreExcl loop not to make forward progress if a different thread is repeatedly doing any of the following in a tight loop:

- Performing stores to a PA covered by the Exclusives monitor.

- Prefetching with intent to write to a PA covered by the Exclusives monitor.

- Executing data cache clean, data cache invalidate, or data cache clean and invalidate instructions to a PA covered by the Exclusives monitor.

- Executing instruction cache invalidate all instructions.

- Executing instruction cache invalidate by V A instructions to a PA covered by the Exclusives monitor.

- Implementations can benefit from keeping the LoadExcl and StoreExcl operations close together in a single thread of execution. This minimizes the likelihood of the Exclusives monitor state being cleared between the LoadExcl instruction and the StoreExcl instruction. Therefore, for best performance, Arm strongly recommends a limit of 128 bytes between LoadExcl and StoreExcl instructions in a single thread of execution.

- The architecture sets an upper limit of 2048 bytes on the Exclusives reservation granule that can be marked as exclusive. For performance reasons, Arm recommends that objects that are accessed by exclusive accesses are separated by the size of the Exclusives reservation granule. This is a performance guideline rather than a functional requirement.

- After taking a Data Abort exception, the state of the Exclusives monitors is UNKNOWN.

- For the memory location accessed by a LoadExcl / StoreExcl pair, if the memory attributes for a StoreExcl instruction are different from the memory attributes for the preceding LoadExcl instruction in the same thread of execution, behavior is CONSTRAINED UNPREDICTABLE. Where this occurs because the translation of the accessed address changes between the LoadExcl instruction and the StoreExcl instruction, the CONSTRAINED UNPREDICTABLE behavior is as follows:

- The StoreExcl either passes or fails, and the status value returned by the StoreExcl is UNKNOWN.

Note

This means the StoreExcl might pass for some instances of a LoadExcl / StoreExcl pair with changed memory attributes, and fail for other instances of a LoadExcl / StoreExcl pair with changed memory attributes.

- The data at the address accessed by the StoreExcl is UNKNOWN.

Note

Another bullet point in this list covers the case where the memory attributes of a LoadExcl / StoreExcl pair differ as a result of using different V As with different attributes that point to the same PA.

- The effect of a data or unified cache invalidate, clean, or clean and invalidate instruction on a local or global Exclusives monitor that is in the Exclusive Access state is CONSTRAINED UNPREDICTABLE, and the instruction might clear the monitor, or it might leave it in the Exclusive Access state. For address-based maintenance instructions, this also applies to the monitors of other PEs in the same Shareability domain as the PE executing the cache maintenance instruction, as determined by the Shareability domain of the address being maintained.

Note

Arm strongly recommends that implementations ensure that the use of such maintenance instructions by a PE in the Non-secure state cannot cause a denial of service on a PE in the Secure state.

- If the mapping of the V A to PA is changed between the LoadExcl instruction and the StoreExcl instruction, and the change is performed using a break-before-make sequence as described in Using break-before-make when updating translation table entries, if the StoreExcl is performed after another write to the same PA as the StoreExcl , and that other write was performed after the old translation was properly invalidated and that invalidation was properly synchronized, then the StoreExcl will not pass its monitor check.

Note

Arm expects that, in many implementations, either:

- The TLB invalidation will clear either the local or global monitor.

- The PA will be checked between the LoadExcl and StoreExcl .

- The Exclusive Access state for an address accessed by a PE can be lost as a result of a PLDW instruction to the same PA executed by another PE. This means that a very high rate of repeated PLDW accesses to a memory location might impede the forward progress of another PE.

## E2.10.6 Use of WFE and SEV instructions by spin-locks

Note

In the event of repeatedly-contending LoadExcl / StoreExcl instruction sequences from multiple PEs, an implementation must ensure that forward progress is made by at least one PE.

The architecture provides Wait For Event, Send Event, and Send Event Local instructions, WFE , SEV , SEVL , that can assist with reducing power consumption and bus contention caused by PEs repeatedly attempting to obtain a spin-lock. These instructions can be used at the application level, but a complete understanding of what they do depends on a system level understanding of exceptions. They are described in Wait For Event and Send Event. However, when the global monitor for a PE changes from Exclusive Access state to Open Access state, an event is generated.

Note

This is equivalent to issuing an SEVL instruction on the PE for which the monitor state has changed. It removes the need for spinlock code to include an SEV instruction after clearing a spinlock.