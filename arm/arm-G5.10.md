## G5.10 Caches in VMSAv8-32

The Arm architecture describes the required behavior of an implementation of the architecture. As far as possible it does not restrict the implemented microarchitecture, or the implementation techniques that might achieve the required behavior.

Maintaining this level of abstraction is difficult when describing the relationship between memory address translation and caches, especially regarding the indexing and tagging policy of caches. This section:

- Summarizes the architectural requirements for the interaction between caches and memory translation.
- Gives some information about the likely implementation impact of the required behavior.

The following sections give this information:

- Data and unified caches.
- Instruction caches.

In addition Cache maintenance requirement created by changing translation table attributes describes the cache maintenance required after updating the translation tables to change the attributes of an area of memory.

For more information about cache maintenance see:

- AArch32 cache and branch predictor support. This section describes the Arm cache maintenance instructions.
- Cache maintenance system instructions. This section summarizes the System register encodings used for these operations when executing in AArch32 state.

## G5.10.1 Data and unified caches

For data and unified caches, the use of memory address translation is entirely transparent to any data access other than as described in Mismatched memory attributes.

This means that the behavior of accesses from the same observer to different V As, that are translated to the same PA with the same memory attributes, is fully coherent. This means these accesses behave as follows, regardless of which V A is accessed:

- Two writes to the same PA occur in program order.
- Aread of a PA returns the value of the last successful write to that PA.
- Awrite to a PA that occurs, in program order, after a read of that PA, has no effect on the value returned by that read.

The memory system behaves in this way without any requirement to use barrier or cache maintenance instructions.

In addition, if cache maintenance is performed on a memory location, the effect of that cache maintenance is visible to all aliases of that physical memory location.

These properties are consistent with implementing all caches that can handle data accesses as Physically-indexed, physically-tagged (PIPT) caches.

## G5.10.2 Instruction caches

In the Arm architecture, an instruction cache is a cache that is accessed only as a result of an instruction fetch. Therefore, an instruction cache is never written to by any load or store instruction executed by the PE.

The Arm architecture permits different behaviors for instruction caches. These are identified by descriptions of the associated expected implementation. The following subsections describe the behavior associated with these cache types, including any occasions where explicit cache maintenance is required to make the use of memory address translation transparent to the instruction cache:

- Physically-indexed, physically-tagged instruction caches.
- Virtually-indexed, physically-tagged instruction caches.

- The IVIPT architecture Extension.

In AArch32 state, the CTR.L1Ip field identifies the form of the instruction caches.

Note

For software to be portable between implementations that might use any of PIPT instruction caches or VIPT instruction caches, software must invalidate the instruction cache whenever any condition occurs that would require instruction cache maintenance for at least one of the instruction cache types.

## G5.10.2.1 Physically-indexed, physically-tagged instruction caches

For a Physically-indexed, physically-tagged (PIPT) instruction cache:

- The use of memory address translation is entirely transparent to all instruction fetches other than as described in Mismatched memory attributes.

- If cache maintenance is performed on a memory location, the effect of that cache maintenance is visible to all aliases of that physical memory location.

An implementation that provides PIPT instruction caches implements the IVIPT Extension, see The IVIPT architecture Extension.

## G5.10.2.2 Virtually-indexed, physically-tagged instruction caches

For a Virtually-indexed, physically-tagged (VIPT) instruction cache:

- The use of memory address translation is transparent to all instruction fetches other than for the effect of memory address translation on instruction cache invalidate by address operations or as described in Mismatched memory attributes.

Note

Cache invalidation is the only cache maintenance instruction that can be performed on an instruction cache.

- If instruction cache invalidation by address is performed on a memory location, the effect of that invalidation is visible only to the V A supplied with the operation. The effect of the invalidation might not be visible to any other VAaliases of that physical memory location.

The only architecturally-guaranteed way to invalidate all aliases of a PA from a VIPT instruction cache is to invalidate the entire instruction cache.

An implementation that provides VIPT instruction caches implements the IVIPT Extension, see The IVIPT architecture Extension.

## G5.10.2.3 The IVIPT architecture Extension

Any permitted instruction cache implementation can be described as implementing the IVIPT Extension to the Arm architecture.

The formal definition of the Arm IVIPT Extension is that it reduces the instruction cache maintenance requirement to the following condition:

- Instruction cache maintenance is required only after writing new data to a PA that holds an instruction.

Note

Previous versions of the Arm architecture have permitted an instruction cache option that does not implement the Arm IVIPT Extension.

## G5.10.3 Cache maintenance requirement created by changing translation table attributes

Any change to the translation tables to change the attributes of an area of memory can require maintenance of the translation tables, as described in General TLB maintenance requirements. If the change affects the cacheability attributes of the area of memory, including any change between Write-Through and Write-Back attributes, software must ensure that any cached copies of affected locations are removed from the caches, typically by cleaning and invalidating the locations from the levels of cache that might hold copies of the locations affected by the attribute change. Any of the following changes to the inner cacheability or outer cacheability attribute creates this maintenance requirement:

- Write-Back to Write-Through.
- Write-Back to Non-cacheable.
- Write-Through to Non-cacheable.
- Write-Through to Write-Back.

The cache clean and invalidate avoids any possible coherency errors caused by mismatched memory attributes.

Similarly, to avoid possible coherency errors caused by mismatched memory attributes, the following sequence must be followed when changing the Shareability attributes of a cacheable memory location:

1. Make the memory location Non-cacheable, Outer Shareable.
2. Clean and invalidate the location from them cache.
3. Change the Shareability attributes to the required new values.