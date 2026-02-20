## D17.2 Defining the sample population

All samples are taken from a population of operations . The population is dynamic rather than static. That is, if a program executes the same operation multiple times (for example, because of loops and subroutines) then that operation appears multiple times in the population.

The operations are one of the following:

- If FEAT\_SPE\_ArchInst is implemented, architecture instructions.
- If FEAT\_SPE\_ArchInst is not implemented, IMPLEMENTATION DEFINED microarchitectural operations (micro-ops).

Architecture instruction means a single instruction that is defined by the A-profile instruction set architecture in AArch64 state.

An architecture instruction might create one or more micro-ops at any point in the execution pipeline. The definition of a micro-op is IMPLEMENTATION SPECIFIC. An architecture instruction might create more than one micro-op for each instruction. A micro-op might also be removed or merged with another micro-op in the Execution stream, so an architecture instruction might create no micro-ops for an instruction.

Any arbitrary translation of architecture instructions to an equivalent sequence of micro-ops is permitted. In some implementations, the relationship between architecture instructions and micro-ops might vary over time.

Note

Sampling from architecture instructions does not require that the instruction is architecturally executed.

## D17.2.1 Operations that might be excluded from the sample population

It is IMPLEMENTATION DEFINED whether each of the following operations is part of the sample population:

- Operations on misspeculated paths.
- Operations (specifically micro-ops) that do not relate to any architecture instruction.
- Operations that generate non-architectural exceptions.

If the operation is not part of the sample population, the operation does not cause the sample interval counter to decrement, is not counted by the SAMPLE\_POP event and therefore is never sampled.

If the operation is part of the sample population, the operation causes the sample interval counter to decrement, is counted by the SAMPLE\_POP event, and might be sampled and counted by the SAMPLE\_FEED event. However, it is IMPLEMENTATION DEFINED whether the sample record for such a sampled operation is captured in the Profiling Buffer. For more information, see Sample operation records for misspeculated and non-architectural operations and Non-architectural exceptions.

If such a sample record is not captured into the Profiling Buffer, then no packets are output and the sample is not counted by the SAMPLE\_FILTRATE event.

Note

If the owning Exception level passes this data to less privileged software for processing, it can set PMSFCR\_EL1.FE to 1 and PMSEVFR\_EL1[1] to 1 to prevent speculative instructions from being recorded in the Profiling Buffer.