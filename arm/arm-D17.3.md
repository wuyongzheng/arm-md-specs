## D17.3 Controlling when an operation is sampled

The sample interval counter, PMSICR\_EL1.COUNT controls when an operation is selected for sampling. In some implementations, a secondary sample interval counter, PMSICR\_EL1.ECOUNT, is also used.

The following sections describe the operation of the sample interval counters.

Details of the random or pseudorandom number generator used when PMSIRR\_EL1.RND is set to 1 are IMPLEMENTATION DEFINED. See Generating random numbers for sampling.

## D17.3.1 Operation sampling

Asample operation is as follows:

1. Software writes a sampling interval to PMSIRR\_EL1.COUNT, and sets PMSICR\_EL1 to zero. The interval is measured in operations.
2. The sample interval counter is decremented by hardware for each operation when profiling is enabled.
3. When the sample interval counter reaches zero, then:
- a. If random perturbation is enabled, the PE continues to count for a random number of further operations while profiling is enabled.
- b. An operation is chosen for profiling. The choice of operation around the sampling point is IMPLEMENTATION SPECIFIC, but does not introduce sampling bias.
4. The sample interval counter is reloaded and the process loops to step 2. It is IMPLEMENTATION DEFINED whether the sample interval counter is reloaded before step 3.a) or at step 3.b). That is, before or after counting the random number of further operations.
5. The chosen operation is marked as the sampled operation. The PE collects information about the sampled operation as it executes by a profiling operation.
6. The sample record is created when the sampled operation has finished execution.

## D17.3.2 Generating random numbers for sampling

The random number generator is IMPLEMENTATION DEFINED. Implementations might use a pseudorandom number. The random number generator must be reset into a useable state. An implementation might include IMPLEMENTATION DEFINED registers to further configure the random number generator.

It is IMPLEMENTATION DEFINED whether the PE adds the random number to the sample interval counter prior to counting down the interval, or after the counter reaches zero and the counter has been reloaded.

## D17.3.3 Initializing the sample interval counters

When the PE moves from a state where profiling is disabled to a state where profiling is enabled:

- If PMSICR\_EL1 is nonzero, then sampling restarts from the current values in PMSICR\_EL1.
- If PMSICR\_EL1 is zero, then it is loaded with an initial value. The behavior depends on PMSIRR\_EL1.RND and whether FEAT\_SPE\_ERnd is implemented.
- -If PMSIRR\_EL1.RND is 0:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to 0x00 .
- If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is not implemented:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to a random or pseudorandom value in the range 0x00 to 0xFF inclusive.
- -If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is implemented:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to 0x00 .

-

## D17.3.4 Behavior of the sample interval counter while profiling is enabled

While profiling is enabled, the counters control when an operation is selected for sampling. The behavior depends on PMSIRR\_EL1.RND and whether FEAT\_SPE\_ERnd is implemented.

## D17.3.4.1 If PMSIRR\_EL1.RND is 0

While nonzero, the sample interval counter decrements by 1 for each member of the sample population. When the counter reaches zero:

- Amember of the sampling population is selected for sampling.
- The counter is set as follows:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to 0x00 .

Note

Because the counter counts down to zero, when PMSIRR\_EL1.RND is 0 the interval between operations being selected for sampling is ( INTERVAL × 256+1).

## D17.3.4.2 If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is not implemented

While nonzero, the sample interval counter decrements by 1 for each member of the sample population. When the counter reaches zero:

- Amember of the sampling population is selected for sampling.
- The counter is set as follows:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to a random or pseudorandom value in the range 0x00 to 0xFF inclusive.

Note

When PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is not implemented, the mean interval between operations being selected for sampling is ( INTERVAL × 256+128), if the random number generator is uniform.

## D17.3.4.3 If PMSIRR\_EL1.RND is 1 and FEAT\_SPE\_ERnd is implemented

While nonzero, the primary sample interval counter decrements by 1 for each member of the sample population. When the primary counter reaches zero:

- The primary sample interval counter is set as follows:
- -PMSICR\_EL1.COUNT[31:8] is set to PMSIRR\_EL1.INTERVAL.
- -PMSICR\_EL1.COUNT[7:0] is set to 0x00 .
- The secondary sample interval counter, PMSICR\_EL1.ECOUNT, is set to a random or pseudorandom value in the range 0x00 to 0xFF inclusive. If this value is zero, then an operation is selected for sampling. Otherwise:
- -While the secondary sample interval counter is nonzero, the secondary sample interval counter decrements by 1 for each member of the sample population. The primary sample interval counter also continues to decrement because it is also nonzero.
- -When the secondary sample interval counter reaches zero, an operation is selected for sampling.

Note

When PMSIRR\_EL1.RND is set to 1 and FEAT\_SPE\_ERnd is implemented, the mean interval between operations being selected for sampling is ( INTERVAL × 256+1), if the random number generator is uniform.

## D17.3.5 Behavior of the sample interval counter while profiling is disabled

When profiling is disabled:

- No operations are selected for sampling.
- No sample records are collected.
- The sample interval counters retain their values and do not decrement.

## D17.3.6 Where operations are sampled

The exact point in the sampled lifespan of operations at which operations are chosen for profiling is IMPLEMENTATION DEFINED.

Note

Arm recommends that the point at which operations are sampled is linked to the definition of the Performance Monitors Extension (PMU) STALL\_FRONTEND and STALL\_BACKEND events, so that sampling records information for STALL\_BACKEND stalls.

## D17.3.7 Sample collisions

RQWTQB

The maximum number of sampled operations that a PE can support simultaneously is IMPLEMENTATION DEFINED.

IQYCRM

IDBJXM

IRCCQG

RLTMKQ

If the maximum number of simultaneous sampled operations has been reached at the point when a new operation must be sampled, the new sample is said to have collided with a previous sampled operation.

The PE records the fact that a sampled operation has collided with another sampled operation. Software can also count the number of collisions and gauge the impact of the collisions.

On a sample collision:

- The PMU event SAMPLE\_COLLISION is generated.
- PMBSR\_ELx.COLL is set to 1, where ELx is the value in the Other event column of Table D17-7. The other fields in PMBSR\_ELx and the other PMBSR\_ELy registers are unchanged.
- The new operation is not sampled.

Sample collisions are likely to increase with shorter sampling intervals. Samples might not be representative of the overall workload if statistically significant numbers of sample collisions occur.

When all of the following are true, the direct read C of PMBSR\_ELx.COLL will return 1:

- An instruction or operation A is selected for sampling.
- Asample collision occurs for sampled operation A . The PE sets PMBSR\_ELx.COLL to 1. This is an indirect write to PMBSR\_ELx.
- AContext synchronization event B is in program order after A .
- Adirect read C of PMBSR\_ELx is in program order after B .

ELx is the value in the Other event column of Table D17-7. The other fields in PMBSR\_ELx and the other PMBSR\_ELy registers are unchanged. For more information, see Synchronization and Statistical Profiling.