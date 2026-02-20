## E2.2 Atomicity in the Arm architecture

Atomicity is a feature of memory accesses, described as atomic accesses. The Arm architecture description refers to two types of atomicity, single-copy atomicity and multi-copy atomicity . The atomicity requirements for memory accesses depend on the memory type, and whether the access is explicit or implicit. For more information, see:

- Requirements for single-copy atomicity.
- Properties of single-copy atomic accesses.
- Multi-copy atomicity.
- Requirements for multi-copy atomicity.
- Concurrent modification and execution of instructions.

For more information about the memory types, see Memory type overview.

## E2.2.1 Requirements for single-copy atomicity

In AArch32 state, the single-copy atomic PE accesses are:

- All byte accesses.
- All halfword accesses to halfword-aligned locations.
- All word accesses to word-aligned locations.
- Memory accesses caused by LDREXD and STREXD instructions to doubleword-aligned locations.

LDM , LDC , LDRD , STM , STC , STRD , PUSH , POP , RFE , SRS , VLDM , VLDR , VSTM , and VSTR instructions are executed as a sequence of word-aligned word accesses. Each 32-bit word access is guaranteed to be single-copy atomic. The architecture does not require subsequences of two or more word accesses from the sequence to be single-copy atomic.

LDRD and STRD accesses to 64-bit aligned locations are 64-bit single-copy atomic as seen by translation table walks and accesses to translation tables.

Note

This requirement has been added to avoid the need for complex measures to avoid atomicity issues when changing translation table entries, without creating a requirement that all locations in the memory system are 64-bit single-copy atomic. This addition means:

- The system designer must ensure that all writable memory locations that might be used to hold translations, such as bulk SDRAM, can be accessed with 64-bit single-copy atomicity.
- Software must ensure that translation tables are not held in memory locations that cannot meet this atomicity requirement, such as peripherals that are typically accessed using a narrow bus.

This requirement places no burden on read-only memory locations for which reads have no side effects, since it is impossible to detect the size of memory accesses to such locations.

Advanced SIMD element and structure loads and stores are executed as a sequence of accesses of the element or structure size. The architecture requires the element accesses to be single-copy atomic if and only if both:

- The element size is 32 bits, or smaller.
- The elements are naturally-aligned.

Accesses to 64-bit elements or structures that are 32-bit aligned are executed as a sequence of 32-bit accesses, each of which is single-copy atomic. The architecture does not require subsequences of two or more 32-bit accesses from the sequence to be single-copy atomic.

When an access is not single-copy atomic by the rules described in this section, it is executed as a sequence of one or more accesses that aggregate to the size of the original access. Each of the accesses in this sequence is single-copy atomic, at least at the byte level.

Note

In this section, the terms before the write operation and after the write operation mean before or after the write operation has had its effect on the coherence order of the bytes of the memory location accessed by the write operation.

If, according to these rules, an instruction is executed as a sequence of accesses, a synchronous Data Abort exception or Debug state entry can be taken during that sequence. This causes execution of the instruction to be abandoned. See Data Abort exception and, when FEAT\_LSMAOC is implemented, Taking an interrupt or other exception during a multiple-register load or store.

If the synchronous Data Abort exception is returned from using the preferred return address, the instruction that generated the sequence of accesses is re-executed and so any access that was performed before the exception was taken is repeated. This also applies to an exit from Debug state.

Note

The exception behavior for these multiple access instructions means they are not suitable for use for writes to memory for the purpose of software synchronization.

For implicit accesses:

- Cache linefills and evictions have no effect on the single-copy atomicity of explicit transactions or instruction fetches.
- Instruction fetches are single-copy atomic:
- -At 32-bit granularity in A32 state.
- -At 16-bit granularity in T32 state.

Concurrent modification and execution of instructions describes additional constraints on the behavior of instruction fetches.

- Translation table walks are performed using accesses that are single-copy atomic:
- -At 32-bit granularity when using Short-descriptor format translation tables.
- -At 64-bit granularity when using Long-descriptor format translation tables.

## E2.2.2 Properties of single-copy atomic accesses

Amemory access instruction that is single-copy atomic has the following properties:

1. For a pair of overlapping single-copy atomic store instructions, all of the overlapping writes generated by one of the stores are Coherence-after the corresponding overlapping writes generated by the other store.
2. For a single-copy atomic load instruction L1 that overlaps a single-copy atomic store instruction S2, if one of the overlapping reads generated by L1 Reads-from-memory one of the overlapping writes generated by S2, then none of the overlapping writes generated by S2 are Coherence-after the corresponding overlapping reads generated by L1.

For more information, see Definition of the memory model.

## E2.2.3 Multi-copy atomicity

In a multiprocessing system, writes to a memory location are multi-copy atomic if the following conditions are both true:

- All writes to the same location are serialized , meaning they are observed in the same order by all observers, although some observers might not observe all of the writes.
- Aread of a location does not return the value of a write until all observers observe that write.

Note

Writes that are not coherent are not multi-copy atomic.

## E2.2.4 Requirements for multi-copy atomicity

For Normal memory, writes are not required to be multi-copy atomic.

For Device memory, writes are not required to be multi-copy atomic.

The memory model is Other-multi-copy-atomic. For more information, see External visibility requirement.

## E2.2.5 Concurrent modification and execution of instructions

The architecture limits the set of instructions that can be executed by one thread of execution as they are being modified by another thread of execution without requiring explicit synchronization.

Concurrent modification and execution of instructions can lead to the resulting instruction performing any behavior that can be achieved by executing any sequence of instructions that can be executed from the same Exception level, except where the instruction before modification and the instruction after modification are:

- When executing the A32 instruction set, a B , BKPT , BL , HVC , ISB , NOP , SMC , or SVC instruction.
- When executing the T32 instruction set. a 16-bit B , BKPT , BLX , BX , NOP , or SVC instruction.

In addition, for the 32-bit T32 instructions, for which Instruction encodings describes the meaning of { hw1 , hw2 }:

- hw1 of a 32-bit BL (immediate) instruction can be concurrently modified to hw1 of another BL (immediate) instruction:
- -This means that some of the most significant bits of the immediate value can be modified.
- hw1 of a 32-bit BLX (immediate) instruction can be concurrently modified to hw1 of another BLX immediate instruction:
- -This means that some of the most significant bits of the immediate value can be modified.
- hw1 of a 32-bit BL (immediate) or BLX (immediate) instruction can be concurrently modified to a T32 16-bit B , BX , BLX , BKPT , or SVC instruction. This modification also works in reverse.
- hw2 of a 32-bit BL (immediate) instruction can be concurrently modified to hw2 of another BL (immediate) instruction with a different immediate:
- -This means that some bits of the immediate value, including the least significant bits, can be modified.
- hw2 of a 32-bit BLX (immediate) instruction can be concurrently modified to hw2 of another BLX (immediate) instruction with a different immediate:
- -This means that some bits of the immediate value, including the least significant bits, can be modified.
- hw2 of a 32-bit B (immediate) instruction with a condition field can be concurrently modified to hw2 of another 32-bit B (immediate) instruction with a condition field with a different immediate:
- -This means that some bits of the immediate value, including the least significant bits, can be modified.
- hw2 of a 32-bit B (immediate) instruction without a condition field can be concurrently modified to hw2 of another 32-bit B (immediate) instruction without a condition field:
- -This means that some bits of the immediate value, including the least significant bits, can be modified.

Note

- In the T32 instruction set:
- -The only encodings of BKPT and SVC are 16-bit.
- -The only encoding of BL is 32-bit.
- The ISB instruction can be concurrently modified and executed in the A32 and A64 instruction sets, but not in the T32 instruction set.

For the instructions explicitly identified in this section, the architecture guarantees that, after modification of the instruction, behavior is consistent with execution of either:

- The instruction originally fetched.
- Afetch of the modified instruction.

The instructions to which this applies are the B , BL , NOP , BKPT , SVC , HVC , and SMC instructions.

For both instruction sets, if one thread of execution changes a conditional branch instruction to another conditional branch instruction, and the change affects both the condition field and the branch target, execution of the changed instruction by another thread of execution before the change is synchronized can lead to either:

- The old condition being associated with the new target address.
- The new condition being associated with the old target address.

These possibilities apply regardless of whether the condition, either before or after the change to the branch instruction, is the always condition.

For all other instructions, to avoid UNPREDICTABLE or CONSTRAINED UNPREDICTABLE behavior, instruction modifications must be explicitly synchronized before they are executed. The required synchronization is as follows:

1. No PE must be executing an instruction when another PE is modifying that instruction.
2. To ensure that the modified instructions are observable, a PE that is writing the instructions must issue the following sequence of instructions and operations:

```
; Coherency example for self-modifying code ; Enter this code with <Rt> containing a new 32-bit instruction, ; to be held in Cacheable space at a location pointed to by Rn. Use STRH in the first ; line instead of STR for a 16-bit instruction. STR <Rt>, [Rn] DCCMVAU Rn ; Clean data cache by MVA to point of unification (PoU) DSB ; Ensure visibility of the data stored ICIMVAU Rn ; Invalidate instruction cache by VA to PoU BPIMVA Rn ; Invalidate branch predictor by MVA to PoU DSB
```

## Note

- The DCCMVAU operation is not required if the area of memory is either Non-cacheable or Write-Through Cacheable.
- If the contents of physical memory differ between the mappings, changing the mapping of VAs to PAs can cause the instructions to be concurrently modified by one PE and executed by another PE. If the modifications affect instructions other than those listed as being acceptable for modification, synchronization must be used to avoid UNPREDICTABLE or CONSTRAINED UNPREDICTABLE behavior.
3. In a multiprocessor system, the ICIMVAU and BPIMVA are broadcast to all PEs within the Inner Shareable domain of the PE running this sequence. However, once the modified instructions are observable, each PE that is executing the modified instructions must issue the following instruction to ensure execution of the modified instructions:

ISB ; Synchronize fetched instruction stream

For more information about the required synchronization operation, see Synchronization and coherency issues between data and instruction accesses.

For information about the Memory Effects generated by instruction fetches, see External visibility requirement.