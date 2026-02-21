## 3.20 TLB and configuration cache conflict

## 3.20.1 TLB conflict

A programming error might cause overlapping or otherwise conflicting TLB entries to be generated in the SMMU. When an incoming transaction matches more than one TLB entry, this is an error. An implementation is not required to detect any or all TLB conflict conditions, but Arm recommends that an implementation detects TLB conflict conditions wherever possible.

If an implementation detects a TLB conflict, all of the following apply:

- It aborts the transaction that caused the lookup that resulted in conflict.
- It attempts to record a F\_TLB\_CONFLICT event. The F\_TLB\_CONFLICT event contains IMPLEMENTATION DEFINED fields that might include diagnostic information that exposes IMPLEMENTATION SPECIFIC TLB layout.

If an implementation does not detect a TLB conflict experienced by a transaction, behavior is UNPREDICTABLE, with the restriction that a transaction cannot access a physical address to which the configuration of a stream does not explicitly grant access.

A TLB conflict never enables transactions to do any of the following:

- Match a TLB entry tagged with a different VMID to that under which the lookup is performed.
- Match a TLB entry tagged with a different Security state to that under which the lookup is performed.
- Match a TLB entry tagged with a different StreamWorld to that under which the lookup is performed.
- When stage 2 is enabled, access any physical address outside of the set of PAs configured in the stage 2 translation tables that a given transaction is configured to use.

Any failure to invalidate the TLB by code running at a particular level of privilege does not give rise to the possibility of a device under control of that level of privilege accessing regions of memory with permissions or attributes that could not be achieved at that same level of privilege.

Note: For example, a stream configured with StreamWorld == NS-EL1 must never be able to access addresses using TLB entries tagged with a different VMID, or tagged as Non-secure EL2, Secure EL2, EL3, or Secure.

A TLB conflict caused by a transaction from one stream must not cause traffic for different streams with other VMID, StreamWorld, or Security configurations to be terminated. Arm recommends that an implementation does not cause a TLB conflict to affect traffic for other ASIDs within the same VMID configuration.

## 3.20.2 Configuration cache conflicts

All configuration structures match a fixed-size lookup span of one entry with the exception of the STE, which contains a CONT field allowing a contiguous span of STEs to be represented by one cache entry.

A programming error might cause an STE to be cached with a span that covers an existing cached STE, which results in an STE lookup matching more than one STE.

An implementation is not required to detect any or all configuration cache conflict conditions but Arm recommends that an implementation detects conflict conditions wherever possible.

If an implementation detects a configuration cache conflict, all of the following apply:

- The transaction that caused the lookup that resulted in conflict is aborted.
- The SMMU attempts to record a F\_CFG\_CONFLICT event. The F\_CFG\_CONFLICT event contains IMPLEMENTATION DEFINED fields that might include diagnostic information that exposes IMPLEMENTATION SPECIFIC cache layout.

If an implementation does not detect a conflict experienced by a transaction, behavior is UNPREDICTABLE.

A configuration cache conflict cannot cause an STE to be treated as though it is associated with a different Security state.