## 3.22 Destructive reads and directed cache prefetch transactions

Some interconnect architectures might support the following types of transaction input to the SMMU:

1. RCI: Read with clean and invalidate:
- A read transaction containing a hint side effect of clean and invalidate.
- Note: The AMBA AXI5 interface [8] ReadOnceCleanInvalid transaction is an example of this class of transaction.
2. DR: Destructive read:
- A read transaction with a data-destructive side effect that intentionally causes addressed cache lines to be invalidated, without writeback, even if they are dirty.
- Note: The AMBA AXI5 interface [8] ReadOnceMakeInvalid transaction is an example of this class of transaction.
3. W-DCP: Write with directed cache prefetch:
- Awrite transaction containing a hint that changes the cache allocation in a part of the cache hierarchy that is not on the direct path to memory. This class of operation does not include those with data-destructive side effects.
- Note: The following AMBA AXI5 interface [8] transactions are examples of this class of transaction: WriteUniquePtlStash, WriteUniqueFullStash.
4. NW-DCP: A directed cache prefetch without write data:
- A transaction that is neither a read nor a write, but performs a cache prefetch in a similar way to a write with directed cache prefetch, without the written data.
- Note: The following AMBA AXI5 interface [8] transactions are examples of this class of transaction: StashOnceShared, StashOnceUnique.

The side effects of these transactions are hints and are therefore distinct from, and treated differently to, Cache Maintenance Operations. See section 16.7.2 Non-data transfer transactions .

In SMMUv3.0, the architecture does not support these transactions, which are unconditionally converted on output as specified by the interconnect architecture.

In SMMUv3.1 and later, these transactions are permitted to pass into the system unmodified when the transaction bypasses all implemented stages of translation, see section 3.22.3 Memory types and Shareability for permitted memory types. This happens when:

- SMMU\_(*\_)CR0.SMMUEN == 0 for the Security state of the stream:
- -These transactions are affected by SMMU\_(*\_)GBPA overrides in the same way as the implementation treats ordinary transactions.
- SMMU\_(*\_)CR0.SMMUEN == 1 for the Security state of the stream, but the valid STE of the stream has STE.Config == 0b100 .
- The valid STE for the transaction has STE.S1DSS == 0b01 and STE.Config == 0b101 , and the transaction is supplied without a SubstreamID.

When the output interconnect does not support these types of transaction, or when the conditions described in sections 3.22.1 Control of transaction downgrade , 3.22.2 Permissions model and 3.22.3 Memory types and Shareability apply, these classes of transaction are downgraded with the following transformations:

| Input Transaction Class              | Output/downgraded transaction class                          |
|--------------------------------------|--------------------------------------------------------------|
| Read with clean and invalidate (RCI) | No downgrade, or downgrade to ordinary read transaction. (1) |

| Input Transaction Class                             | Output/downgraded transaction class                                                                   |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------|
| Destructive read (DR)                               | Non-destructive read: An ordinary transaction, or a read with a clean and invalidate side effect. (2) |
| Write with directed cache prefetch (W-DCP)          | Ordinary write transaction.                                                                           |
| Directed cache prefetch without write data (NW-DCP) | No-op: Transaction completes successfully with no effect on the memory system.                        |

- (1) It is IMPLEMENTATION DEFINED whether an implementation downgrades a RCI into a read, or whether this transaction remains unchanged. An implementation might only downgrade the RCI into a read if the output interconnect supports read but not RCI transactions.
- (2) It is IMPLEMENTATION DEFINED whether a downgrade of a destructive read to a non-destructive read chooses to downgrade to an ordinary read or a RCI.

The RCI and DR transactions are read transactions with an additional hint. These transactions are not permitted to be issued speculatively.

The W-DCP transaction is a write transaction with an additional hint. The NW-DCP transaction is a hint without data transfer and is issued speculatively.

An implementation is permitted to downgrade the transaction as described in this section, for any reason. The data transfer portion of these transactions, if present, is not a hint, and is treated in the same way as an ordinary read or write.

Note: Unless the SMMU has been explicitly configured to do so, Arm recommends that the common behavior of an implementation is to avoid downgrading these transactions.

## 3.22.1 Control of transaction downgrade

An implementation of SMMUv3.1 or later supporting these classes of transactions provides STE.{DRE,DCP} controls to permit these classes of transaction to pass into the system without transformation when one or more stages of translation are applied. This does not include the case where the only stage of translation is skipped because of the value of STE.S1DSS.

When these controls are disabled, the respective class of transactions is downgraded as described in the previous section:

| Input transaction class                             | Requirement to be eligible to pass into the system without class downgrade                                     |
|-----------------------------------------------------|----------------------------------------------------------------------------------------------------------------|
| Read with clean and invalidate (RCI)                | No additional requirements                                                                                     |
| Destructive read (DR)                               | STE.DRE == 1. If STE.DRE == 0, downgraded into non-destructive read (read, or read with clean and invalidate). |
| Write with directed cache prefetch (W-DCP)          | STE.DCP == 1. If STE.DCP == 0, downgraded into ordinary write.                                                 |
| Directed cache prefetch without write data (NW-DCP) | STE.DCP == 1. If STE.DCP == 0, downgraded into no-op.                                                          |

A read with clean and invalidate is non-destructive and is not required to be transformed into a different class of transaction by the SMMU. The SMMU evaluates permissions for this type of transaction the same way it does for an ordinary read, see section 3.22.3 Memory types and Shareability . A read with clean and invalidate might be transformed as required by the final memory type or Shareability.

If a transaction is enabled to progress without downgrade, it can only progress if the required translation table permissions are present, as described in the next section. If the required permissions are not present, but sufficient permissions exist to downgrade the transaction, then it is downgraded. Otherwise it causes a fault.

## 3.22.2 Permissions model

When one or more stages of translation are applied to these transactions, the interaction with the permissions determined from translations is shown below. The behaviors listed here assume that translation for the given address has progressed up to permission checking, and that no higher-priority fault, for example a Translation fault or an Access flag fault, has occurred.

| Transaction type                                    | Required permissions                                                                                                                                                                                                                                                                                                                                                                      | Behavior if permissions not met                                                                                                                                                         |
|-----------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Read with clean and invalidate (RCI) (1)            | Identical to ordinary read: Requires Read or Execute permission, (depending on input InD and STE.INSTCFG) at a privilege appropriate to PnU input and STE.PRIVCFG.                                                                                                                                                                                                                        | Identical to ordinary read.                                                                                                                                                             |
| Destructive read (DR)                               | Requires Read or Execute permission (depending on input InD and STE.INSTCFG), and Write permission that does not result in HTTU update of Dirty state, at a privilege appropriate to PnU input and STE.PRIVCFG.                                                                                                                                                                           | If write access is not granted, then downgraded as above into a read or read with clean and invalidate. (2) If no Read/Execute permission (as appropriate), identical to ordinary read. |
| Write with directed cache prefetch (W-DCP)          | Identical to ordinary write: Requires Write permission at privilege appropriate to PnU input and STE.PRIVCFG. Always Data.(3)                                                                                                                                                                                                                                                             | Identical to ordinary write.                                                                                                                                                            |
| Directed cache prefetch without write data (NW-DCP) | Requires either Read permission or Write permission that does not result in HTTU update of Dirty state, or Execute at privilege appropriate to PnU input and STE.PRIVCFG, at each enabled stage of translation. It is IMPLEMENTATION SPECIFIC whether this permission is evaluated as the effective combination of permissions at all stages, or evaluated at each stage separately (5) . | Prefetch does not occur. (4)                                                                                                                                                            |

See section 3.13.8 Hardware flag update for Cache Maintenance Operations and Destructive Reads for information on the behavior of HTTU for Destructive Reads. HTTU for RCI and W-DCP behaves the same as for an ordinary read or write, respectively.

Adirected cache prefetch without write data (NW-DCP) does not cause faults in the SMMU. Where the interconnect

architecture requires a response to an NW-DCP, and where the SMMU terminates an NW-DCP, the SMMU does not cause abort responses to be returned.

If RCI or DR ultimately lead to a fault, they are recorded as reads (data or instruction, as appropriate to input InD/INSTCFG).

If W-DCP ultimately leads to a fault, it is recorded as a write.

If the RCI, DR and W-DCP transactions lead to a fault, they stall in the same way as an ordinary read or write transaction if the SMMU is configured for stalling fault behavior. Retry and termination behave the same as for an ordinary read or write transaction. If these transactions are stalled and retried, they are retried as the same transaction type.

## 3.22.3 Memory types and Shareability

The interconnect architecture of an implementation might impose constraints on the memory type or Shareability that output DR, RCI, W-DCP and NW-DCP operations can take.

At the point of final output the SMMU downgrades these operations, as described in 3.22 Destructive reads and directed cache prefetch transactions , if the operations are not valid for output with the determined output attribute.

This rule applies to all such operations in all translation and bypass configurations, including:

- Global bypass (attribute set from GBPA).
- STE bypass (the only stage of translation is skipped because of STE.Config == 0b100 or STE.S1DSS == 0b01 and STE.Config == 0b101 ).
- Translation.

Note: On AMBA AXI5 interfaces [8], the W-DCP operations (WriteUniquePtlStash, WriteUniqueFullStash) are not permitted to be emitted with a Non-shareable or Sys Shareability. The NW-DCP operations (StashOnceShared, StashOnceUnique) are not permitted to be emitted with Sys Shareability. RCI and DR operations (ReadOnceCleanInvalid and ReadOnceMakeInvalid) are not permitted to be emitted with NSH or Sys Shareability.