## D20.2 PE error handling

## D20.2.1 PE error detection

| I KRYQW   | When a PE accesses memory or other state, an error might be detected in that memory or state, and corrected, deferred, or signaled to the PE as a Detected error with an in-band error response. Note:                                                                                                                                                                                                                                                                                                                                                                          |
|-----------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I SLYLK   | The response from memory or other state is defined by Detecting and consuming errors. For more information, see Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).                                                                                                                                                                                                                                                                                                                                       |
| I DWWQJ   | When an error is detected by a component on a read or a cache maintenance operation from the PE: • If the error can be corrected, it is corrected and corrected data is returned. • If the error cannot be corrected and can be deferred, it is deferred. For example, on a load by poisoning the PE state, if this is supported by the PE implementation. • If the error cannot be corrected and if implemented and enabled at the component, the Detected error is signaled to the PE as an in-band error response.                                                           |
| I BKVQP   | When an error is detected by a component consuming a write from the PE:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| I PDDNB   | The component might record the Detected error and generate a Fault handling interrupt and/or Error recovery interrupt.                                                                                                                                                                                                                                                                                                                                                                                                                                                          |
| I VRYFF   | If the component implements the RASSystem Architecture, its behavior is defined by the RASSystem Architecture, and                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| I FLXTY   | An in-band error response is sometimes referred to as an External abort . To avoid confusion with the External abort exception , the RAS sections in this Manual use in-band error response to describe the response to the PE for a memory access. For more information, see Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for                                                                                                                                                                                                                |
| R WLTPV   | A-profile architecture (ARM IHI 0100). The size of the protection granule for any implemented error detection mechanism in memory is IMPLEMENTATION                                                                                                                                                                                                                                                                                                                                                                                                                             |
|           | DEFINED and might vary from moment to moment and instruction to instruction. For example, the size of the protection granule might depend on one or more of the following: • The physical address of the Location being accessed. • Whether a copy of the Location held in a cache is being accessed, and the cache it is held in. • The type of access being made. • If FEAT_SME is implemented, whether the PE is in Streaming SVE mode or is not in Streaming SVE mode. Asystem might implement multiple error detection mechanisms with differing protection granule sizes. |
| I JJJGW   |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I YBRSM   | For a Deferred error, Clearing Deferred errors from poisoned Locations describes mechanisms to remove poison and clear the error. The architecture also permits IMPLEMENTATION DEFINED mechanisms for clearing an error or poison from memory.                                                                                                                                                                                                                                                                                                                                  |

## D20.2.2 PE error propagation

INTXKV

RXMBNW

The program-visible architectural state of the PE, referred to as the PE state, includes:

- General-purpose, SIMD&amp;FP, and SVE registers.
- SMEand SME2 registers.
- System registers.
- Special-purpose registers.
- PSTATE.

An error is consumed by the PE by any of the following:

- An instruction commits the corruption into the PE state.
- The error is on an instruction fetch and the corrupt instruction is committed for execution.
- The error is on a translation table walk for a committed load, store, or instruction fetch.

IHVFKW For a PE, Error propagation applies to the propagation of Detected error by the PE between the PE state, and any other

PE state or memory.

Note: Memory includes structures that cache the contents of memory, such as an instruction cache, data cache, or TLB.

- RVGXBJ An error is propagated by the PE by one or more of the following occurring that would not have been permitted to occur had the fault not been activated:
- Consumption of the corrupt value by any instruction, propagating the error to the target(s) of the instruction. This includes:
- -Astore of a corrupt value.
- -Awrite of a corrupt value to a System register, Special-purpose register, or PSTATE. Infecting a System register state might mean that the PE generates transactions that would not otherwise be permitted.
- Any operation occurring that should not have occurred, including:
- -Aload, translation table walk, or instruction fetch that would not have been permitted, including those from hardware speculation or prefetching.
- -Astore to an incorrect address, or a store that would not have been made or not permitted.
- -Adirect or indirect write to a Special-purpose or System register that would not have been made or not permitted.
- -Assertion of any signal, such as an interrupt, that would not have been asserted.
- Any operation not occurring that should have occurred.
- Causing the PE to take an imprecise exception, other than an Error exception in response to the error itself. For more information, see Definition of a precise exception and imprecise exception.
- The PE discarding data that it holds in a modified state.
- Any other loss of required uniprocessor semantics, ordering, or coherency.

In RVGXBJ, not have been permitted to occur means that the observable behavior of the PE is a deviation from the correct service of the PE, as defined by the architecture. Deviations from the normal behavior of the PE implementation that would otherwise be permitted by the architecture are not deviations from correct service.

Example D20-4

IRMZNK

APEtakes an Error exception asynchronously as follows, in program order:

1. Aload returns a corrupt value from a first location to a general-purpose register.
2. The PE suppresses a store of the register to a second memory location. In particular, the location is not updated and so retains its previous value.
3. The Error exception is taken.
4. At the point when the Error exception is taken, the ordering constraints imposed by the architecture have not been violated, in particular those relating to the observability of the store at step 2.

Although the error has not been propagated, the PE state is not consistent with the PE having executed all of the instructions up to the point when the Error exception is taken, and so it would be unlikely that software would be able to recover execution.

An error propagated by the PE is silently propagated by the PE only if all of the following are true:

IBRBFF

RDTRFQ

DYQQLJ

1. The propagation is not part of the required operation of the PE in taking an Error exception generated by the error.
2. The propagation is not part of the required operation of the PE executing an ESB instruction that synchronizes the error.
3. The error is not signaled to the consumer as a Detected error or Deferred error.
4. Any of the following are true:
- The corrupt value is held in other than the general-purpose, SIMD&amp;FP, SVE, SME, and SME2 registers.
- The error is propagated by an instruction in program order before either taking an Error exception generated by the error or executing an ESB instruction that synchronizes the error, and is propagated to outside of the general-purpose, SIMD&amp;FP, SVE, SME, and SME2 registers.
- The error is propagated other than by an instruction that consumes the corrupt value as an input operand but otherwise behaves correctly.

In RNQDWB, item 4 means that after taking the Error exception generated by the error, or an ESB , propagating an error by, for example, storing the corrupt value to memory, is not considered as silent propagation of the error by the PE.

Example D20-5

APE takes an Error exception in response to a load that returns a corrupt value to a general-purpose register. The error is not silently propagated to outside of the general-purpose registers before the Error exception is taken.

Neither of the following are considered silent propagation of the error by the PE:

- Taking the Error exception causes the ESR\_ELx, ELR\_ELx, and SPSR\_ELx registers to be updated. This is part of the required operation of the PE.
- After taking the Error exception, software stores the contents of the general-purpose register to memory, and this is not signaled to memory as a Deferred error. This happens in program order after the exception is taken.

The error is not silently propagated by the PE.

Example D20-6

Further to Example D20-4, if either of the following example additional operations occur between 2 and 3, then the PE has silently propagated the error:

- Asecond store to a third location is performed by the PE, and the architecture requires that the first store is ordered-before the second store. For example, the second store is a store-release operation. In this case, the PE violates the external ordering constraints for the two stores, and the error is silently propagated to any observer of the second store.
- A second load from the second location returns the previous value, and a second store writes that value to a third location. In this case, the PE violates the requirements of the Coherence-before relation because the second load cannot be Coherence-before the first store. The error silently propagates to any observer of the second store.

If instead of the PE suppressing the store at 2, the PE poisons the second memory location, and in the second example propagates that poison through the second load and second store, then the error is not silently propagated.

The features that a PE includes to prevent silent propagation of an error are IMPLEMENTATION DEFINED.

Example D20-7

An implementation ensures that a corrupt value in a general-purpose, SIMD&amp;FP, SVE, or SME register is not silently propagated, by signalling a Deferred error on any write of data to any memory location, such that the memory location is poisoned.

## D20.2.3 Clearing Deferred errors from poisoned Locations

## D20.2.3.1 Poison-atomicity of Memory Write Effects

AMemory Write Effect is poison-atomic if the Memory Write Effect removes a Deferred error (poison) at all Locations written to by the Memory Write Effect.

| R XVFDG   | For each store instruction with Explicit Memory Write Effects, it is IMPLEMENTATION DEFINED whether the Memory Write Effects are poison-atomic for a region of physical memory. This includes the DC ZVA and/or DC GZVA instructions.                                                                                                                                                                                                          |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R QSBKL   | If a Location in a region of physical memory supports the poison-atomic property for a store instruction, then all Locations in the same naturally-aligned region support this for the same store instruction, where the size of the region is the largest translation granule that the PE supports.                                                                                                                                           |
| I CSJLP   | Support for the poison-atomic property for a store instruction is a property of both the PE as well as the system. That is, if the system includes a PE that supports the poison-atomic property for the instruction, then both the PE and the system support this instruction such that it is guaranteed to be poison-atomic. For example, the system should not split cache line writes of data to be smaller than the poison granule of the |
| I ZRSSM   | There is no architected means to discover the poison-atomic property for DC ZVA or DC GZVA for any region of physical memory.                                                                                                                                                                                                                                                                                                                  |
| I NXNTY   | When a Memory Write Effect to a Location is not poison-atomic, the Memory Write Effect propagates a Deferred error previously at the Location to the new value being written.                                                                                                                                                                                                                                                                  |

Example D20-8

A region of physical memory uses Error Correction Codes (ECC) to provide error detection and correction. The protection granule for this region of memory is the size of a range covered by a single ECC. The ECC is also used to encode a poison value. This means the poison granule is the same size as the protection granule, for this region of physical memory.

A write that is smaller than the protection granule to this region of physical memory must read the protection granule containing the Location being written in order to compute a new ECC for the protection granule. If the protection granule contains poison, then a poisoned value is written back, meaning the write is not poison-atomic.

If a write overwrites the entire protection granule, then the system can compute a new ECC for the protection granule without reading the previous contents, meaning the write can be poison-atomic.

| I GLFCV   | Asystem might require software to stop using the protection granule until the Deferred error can be removed.                                                                                                                                                                      |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I HPJFJ   | The size of the poison granule is IMPLEMENTATION DEFINED and might vary from moment to moment, instruction to instruction, and by Location. The size of the poison granule might be the same as the size of the protection granule, but this is not guaranteed. See alsoR WLTPV . |
| I CBCMK   | The regions of physical memory that support the poison-atomic property are IMPLEMENTATION DEFINED. Systems might have multiple physical memory types, including multiple physical memory regions used for bulk memory.                                                            |
|           | D20.2.3.2 Removing poison                                                                                                                                                                                                                                                         |
| I VZRKL   | For guidance on mechanisms that software can use to remove poison from a Location, see Use of the RAS Extension.                                                                                                                                                                  |
| I PSLGW   | In order to test that poison has been removed from a Location, after the Location has been overwritten by a known-good value, software must be able to read back the Location from physical memory to check that the poison has been removed and the error is not persistent.     |
|           | To do this, software must ensure that the Location has been cleaned and invalidated from all caches, so that the read returns a value from the Point of Physical Storage for the Location, and not any intermediate cache.                                                        |
|           | The Point of Coherency might be before a transparent unified cache, meaning that it might be before the Point of Physical Storage for a Location.                                                                                                                                 |
|           | For more information on the Point of Physical Storage, see A64 Cache maintenance instructions.                                                                                                                                                                                    |

## D20.2.4 Other errors

IKRQMR

The RAS Extension deals mostly with errors detected by components outside of the PE, such as memory, and consumed by the PE.

Other errors might be detected from within the processor that implements the PE. If the error is not an error in the PE state then the error might be treated as an error detected by another component.

In the following examples, the component reports these errors to a RAS System Architecture node that implements Error records and records the errors, and might generate one or more of a Fault handling interrupt, Error recovery interrupt, or Critical Error interrupt depending on the features and configuration of the node.

Example D20-9

Aprocessor cache can be treated as a component outside the PE.

The cache detects an error in the cache state that cannot be corrected:

- If the error is detected in dirty cache data being evicted from the cache when the PE makes an access, then the error might be deferred by the cache writing poison in the evicted cache data.
- If the PE is performing a partial write that does not completely overwrite the protection granule, then the error might be deferred by the cache writing poisoned to the cache location, and/or evicting the cache line with poison. Deferring the error means the error is not consumed by the PE.

Otherwise, the cache component generates the in-band error response to the PE.

|         | Example D20-10                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I VNTWD | An implementation might include error detection logic within the PE state itself. When the PE detects an error in the PE state, the instruction that uses that state consumes the error, and the PE generates an IMPLEMENTATION DEFINED Error exception, taken as an SError exception. SeeR FNVVJ . In this case, the processor that implements the PE includes a RAS System Architecture node that implements Error                                                                                                                                                                                                                                                                                         |
| I JRQDM | An implementation might support poisoning within the PE state. When the PE consumes a Deferred error, for example poisoned value, from memory into the PE state, the PE state becomes poisoned. Subsequent operations that read the poisoned value can continue to defer the error by poisoning the result of the operation. However, if the PE attempts to execute an operation that reads the poisoned value and cannot defer the error further, the PE generates an IMPLEMENTATION DEFINED Error exception, taken as an SError exception. SeeR FNVVJ . In this case, the processor that implements the PE includes a RAS System Architecture node that implements Error records that record these errors. |
| I JHQVK | Components outside of the PE might detect errors that are not consumed by the PE. These components might report such errors to a PE using Error recovery interrupts.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| R XJNNT | For implementations that include the Statistical Profiling Extension, the Statistical Profiling Extension behaves like a separate component.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| I MJQQZ | Errors from software faults are outside the scope of the RAS Extension. For more information, see Arm ® Reliability, Availability, and Serviceability (RAS) System Architecture, for A-profile architecture (ARM IHI 0100).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |