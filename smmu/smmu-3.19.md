## 3.19 Power control

An implementation might support IMPLEMENTATION SPECIFIC automatic power saving techniques, for example, power and clock gating, retention states during idle periods of normal operation. All use of these techniques is functionally invisible to devices and software. If implemented, these automatic powerdown or retention states:

- Might retain all valid cache contents or might cause loss of cached information.
- Do not allow undefined cache contents to become valid, valid cache contents to change, or otherwise corrupt any SMMU state.
- Seamlessly operate with wake on demand behavior in the event of incoming device transactions.

Alternatively, a system might allow an SMMU to be powered off at the request of system software, in an IMPLEMENTATION DEFINED manner. This state is requested when no further SMMU operation is required by the system. Software must not make accesses to the SMMU programming interface in this state. If more than one Security state is supported, this power off state is not entered unless privileged software from all Security states which either configure or use the SMMU request for or agree to a powerdown.

Because such a power off represents a complete loss of state and functionality, this state must only be used when all client devices and interconnect are quiescent. Software must disable client device DMA and ensure any SMMU commands, invalidations and transactions from client devices that are in progress are complete before requesting powerdown. If any existing transactions are in a stalled state at the time of the powerdown, they must be terminated with an abort. The behavior when a transaction arrives at the SMMU after the powerdown state is entered is UNPREDICTABLE.

On an IMPLEMENTATION DEFINED wakeup event, the SMMU must be reset and the return of the SMMU to software control is signaled through an IMPLEMENTATION DEFINED mechanism. The SMMU is then in a state consistent with a full reset and the SMMU registers are required to be re-initialized before client devices can be enabled.

## 3.19.1 Dormant state

Implementations might provide automatic powerdown modes during idle periods in which SMMU registers are accessible but internal structures might be powered down. An implementation might provide a hint to software, through the SMMU\_STATUSR.DORMANT flag, that it contains no cached configuration or translation information, possibly because of cache powerdown. Software can use this flag to determine that no structure or TLB invalidation is required and avoid issuing maintenance commands.

When SMMU\_STATUSR.DORMANT == 1, the SMMU guarantees that:

- No caches of any structures or translations are present.
- Any required configuration or translation information will access the information in the configuration structures or translation tables in memory.
- No pre-fetch of any configuration or translation data is in progress.
- If any structures or translations were altered in memory, no stale version will be used by the SMMU.

Software can make use of this flag by:

1. Altering translations or configuration structure data.
2. Testing the flag
- If the flag is 0, issuing invalidation commands or broadcast invalidation messages to invalidate any potentially-cached copies.
- If the flag is 1, avoiding invalidation of the altered structure.

An implementation is not required to support this hint, and software is not required to take note of this hint.