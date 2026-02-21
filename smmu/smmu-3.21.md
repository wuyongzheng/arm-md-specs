## 3.21 Structure access rules and update procedures

## 3.21.1 Translation tables and TLB invalidation completion behavior

Translation table walks, caching, TLB invalidation, and invalidation completion semantics match those of Armv8-A [2], including rules on prefetch and caching of valid translations only. If intermediate translation table data is cached in the SMMU (a walk cache) this is invalidated during appropriate TLB maintenance operations in the same way as it would be on a PE.

Explicit TLB invalidation maintains TLB entries when the translation configuration has changed, to ensure visibility of the new configuration. Translation configuration is the collective term for translation table descriptors and the set of SMMU configuration information that is permitted to be cached in the TLB. This maintenance is performed from a PE using TLBI broadcast invalidation or using explicit CMD\_TLBI\_* commands.

A broadcast TLB invalidation operation becomes visible to the SMMU after a Shareable TLBI instruction is executed by a PE in a common Shareability domain. A command TLB invalidation operation becomes visible to the SMMU after it is consumed from the Command queue.

A TLB invalidation operation is complete after all of the following become true:

- All TLB entries targeted by the scope of the invalidation have been invalidated.
- Any relevant HTTUs are globally visible to their Shareability domain as set out in section 3.13.4 HTTU behavior summary .
- No accesses can become visible to their Shareability domain using addresses or attributes that are not described by the translation configuration, as observed after the invalidation operation became visible. This means that invalidation completes after:
- -All translation table walks that could, prior to the start of the invalidation, have formed TLB entries that were targeted by the invalidation are complete, so that all accesses to any fetched levels of the translation table are globally visible to their Shareability domain. This applies to a translation table walk performed for any reason, including:
* A translation table walk that makes use of walk caches that are targeted by the invalidation.
* A stage 2 translation table walk that are performed because of a stage 1 descriptor fetch, CD fetch or L1CD fetch.

Note: To achieve this, a translation table walk might be stopped early and the partial result discarded.

- -SMMU-originated accesses that were translated using TLB entries that were targeted by the invalidation are globally visible to their Shareability domain. These accesses are stage 1 descriptor accesses, CD fetches or L1CD fetches.
- -Where a stage 2 invalidation targets TLB entries that might have translated a stage 1 descriptor access, the stage 1 descriptor access is required to be globally visible by the time of the invalidation completion, but neither the overall stage 1 translation table walk or the operation that caused the stage 1 translation table walk are required to be globally visible. Otherwise, for stage 1 and stage 1and stage 2 scopes of invalidation, all client device transactions that were translated using any of the TLB entries that were targeted by the invalidation are globally visible to their Shareability domain.
- -The result of an ATOS operation cannot be based on addresses or attributes that are not described by translation configuration that could have been observed after the invalidation operation became visible.

Note: An in-progress translation table walk (performed for any reason, including prefetch) can be affected by a TLB invalidation, if the TLB invalidation could have invalidated a cached intermediate descriptor that was previously referenced as part of the walk. The completion of a TLB invalidation ensures that a translation table walk that could have been affected by the TLB invalidate is either:

- Fully complete by the time the TLB invalidation completes.
- Stopped and restarted from the beginning.

Note: This ensures that old or invalid pointers to translation sub-tables are never followed after a TLB invalidation (whether broadcast or CMD\_TLBI\_*) is complete. Completion of a TLB invalidation means the point at which a broadcast invalidation sync completion is returned to the system (for example, on AMBA interconnect, completion of a DVM Sync), or, for CMD\_TLBI\_* invalidations, the completion of a later CMD\_SYNC command.

Note: The architecture states that where a translation table walk is affected by a TLB invalidation, one option is that the walk is stopped by the completion of the invalidation. An implementation must give this appearance, which means no observable side effects of doing otherwise could ever be observed. However, after an invalidation completion that affects prior translation table reads made before the invalidation, an implementation is permitted to make further fetches of a translation table walk if, and only if, it is guaranteed that these reads have no effect on the SMMU or the rest of the system, are not made to addresses with read side effects and will not affect the architectural behavior of the system.

Translation cache entries (pertinent to a Security state) are not inserted when SMMU\_(*\_)CR0.SMMUEN == 0.

## 3.21.1.1 Translation tables update procedure

When altering a translation table descriptor, the A-profile architecture[2] before v8.4-A, and SMMUv3 architectures before SMMUv3.2, require a break-before-make procedure for:

- Changes to memory type.
- Changes to Cacheability attributes.
- Changes to output address.
- Changes to block or page size.
- Creating a global entry where there might be non-global entries in a TLB that overlap the global entry.

Note: For example, to split a block into constituent granules (or to merge a span of granules into an equivalent block), the A-profile architecture[2] requires the region to be made invalid, a TLB invalidate performed, then to make the region take the new configuration.

Note: The requirement for a break-before-make sequence can cause problems for unrelated I/O streams that might use addresses overlapping a region of interest, because the I/O streams cannot always be conveniently stopped and might not tolerate translation faults. It is advantageous to perform live update of a block into smaller translations, or a set of translations into a larger block size.

The Armv8.4 [2] architecture offers 3 levels of support when changing block size without changing any other parameters that are listed as requiring use of break-before-make. These are described as Level 0, 1 and 2, where Level 0 is equivalent to the pre-Armv8.4 requirements.

Implementations of SMMUv3.2 or later are required to support Level 1 or Level 2 behavior, as indicated by SMMU\_IDR3.BBML.

Note: Arm recommends that an implementation supports Level 2 behavior for performance reasons.

Note: Armv8.4 permits the PE to report a TLB conflict abort in a wider range of scenarios than are permitted by SMMUv3.2.

Note: The requirement for support of Level 1 or 2 and the stricter requirements regarding TLB conflict abort means that an implementation of SMMUv3.2 or later guarantees that a mechanism is available to change block or page size without interrupting I/O streams with a fault.

The Armv8.4 architecture adds a new bit, 'nT', at bit [16] in Block translation descriptors, which is supported by an implementation of SMMUv3.2 or later in the same way as for the PE, depending on the BBML level as described below. The nT bit allows a valid Block descriptor to be used for translation but prevents it from being cached in a way that can cause a TLB conflict with existing TLB entries.

For VMSAv9-128, an 'nT' bit is added to stage 1 and stage 2 Table descriptors which have SKL != 0b00 , in order to support changing between larger and smaller table sizes.

In an SMMU with SMMU\_IDR5.D128 == 1, the BBM level support indicated in SMMU\_IDR3.BBML also applies to the SMMU's support for changing the size of translation tables.

The SMMUv3 architecture requirements in a TLB conflict scenario are not affected by BBML level.

Note: When multiple system components, whether SMMU, PE or other, are sharing one translation table then behavior according to the lowest common break-before-make Level must be used when updating the table.

## 3.21.1.2 When SMMU\_IDR3.BBML == 1 (Level 1)

The implementation requires software to use the nT bit when changing translation size without using a break-before-make procedure. An F\_TLB\_CONFLICT fault might occur if a translation table update is made without using break-before-make or the nT bit.

Setting nT == 1 does not cause a fault.

Note: A Translation Fault is a permitted behavior for a level 1 Armv8.4 PE with nT == 1, but this is prohibited in a level 1 SMMU.

A Block descriptor having nT == 1 is not cached in a way that will cause a TLB conflict.

Note: One interpretation of the nT bit is to prevent the caching of a translation when nT == 1. This might significantly impact translation performance for the lifetime of the translation table entry.

In a Level 1 SMMU a change to only the Contiguous bit, bit 52 in the descriptor, at either block or page level and with other properties unchanged, does not lead to a TLB conflict fault. When the Armv8-A requirements for use of the Contiguous bit are followed, a change to the Contiguous bit can be performed without using a break-before-make procedure and without using the nT bit in the case of a Block descriptor.

Note: Example implementation styles include ignoring the Contiguous bit at all levels, or reconciling the output of any overlapping TLB entries that might result.

Note: A change from a block translation to an equivalent span of page translations can be performed by changing the nT bit of the Block descriptor from 0 to 1, followed by TLB invalidation of the block, followed by replacement of the Block descriptor with a Table descriptor to a next-level table containing equivalent page translations, followed by TLB invalidation of the affected range.

Note: A change from a span of page translations to an equivalent block translation can be performed by changing a mid-level Table descriptor to a Block descriptor having nT == 1, followed by TLB invalidation of the affected range, followed by an update of the nT bit of the Block descriptor from 1 to 0, followed by TLB invalidation of the block.

Note: The use of the nT bit in these procedures ensures that a TLB multi-match scenario cannot arise.

## 3.21.1.3 When SMMU\_IDR3.BBML == 2 (Level 2)

The implementation ignores the nT bit in the Block descriptor and a change to a translation size can be performed without using break-before-make and without using the nT bit. The implementation automatically resolves any TLB multi-hit scenarios and an F\_TLB\_CONFLICT fault does not occur.

If a change is made to the size of a valid translation without first making the translation invalid, then:

- A TLB conflict does not occur and F\_TLB\_CONFLICT is never reported.
- All of the following apply for translations that might discover multiple matching TLB entries for an address:
- -They are translated using information from at most one of the matching entries.
- -They do not experience a fault that would not otherwise be possible using the translation table descriptor state from either before or after the update.
- The result of a translation:
- -Does not combine information from multiple matching TLB entries.
- -Does not combine information from the state of a descriptor both before and after the update.
- -Does not contain information that was not present in a valid tdescriptor.

Note: An implementation might achieve this behavior by resolving a TLB lookup that has multiple matches by choosing zero or one of the results, or by causing an invalidation of all of the matching entries followed by a re-fetch of the translation.

A TLB invalidation operation removes all matching TLB entries even if overlapping entries exist for a given address.

The rules on TLB invalidation or the atomicity of a descriptor are not affected by BBML level.

The behavior and usage requirements of the Contiguous bit in a Level 2 implementation is the same as in a Level 1 implementation. A change to the Contiguous bit can be performed without using break-before-make and without using the nT bit, and does not lead to a TLB conflict fault.

Note: Arm expects that a Level 2 implementation will also automatically resolve TLB multi-hit scenarios that might arise from a change to a Contiguous bit and recommends that the Contiguous bit is not ignored.

Note: Arm expects that the only change that is made to a valid translation table descriptor is that of changing the page or block size of a range of addresses. A change to memory type, Cacheability, nG or output address might impair coherency or ordering semantics of accesses using the translation.

Note: A change from one set of translations to another equivalent set by changing the translation size can be performed by replacing a block or range of pages with equivalent translations of a different size, followed by TLB invalidation of the affected range.

## 3.21.2 Queues

The SMMU does not write to the Command queue. The SMMU writes to the PRI and Event queues. Arm expects the PRI queue and Event queue to be read but not modified by the agent controlling the SMMU. Writes to the Command queue do not require any SMMU action to ensure that the SMMU observes the values written, other than a write of the PROD register of the Command that causes the written command entries to be considered valid for SMMUconsumption. If the SMMU internally caches Command queue entries, no other explicit maintenance of this cache is required. Arm expects that the SMMU is configured to read the queue from the required Shareability domain in at least an IO-coherent manner, or that both the SMMU and other entities make non-cached accesses to the queue so that Cache Maintenance Operations are not required.

To issue commands to the SMMU, the agent submitting the commands:

1. Determines (using PROD/CONS indexes) that there is space to insert commands.
2. Writes one or more commands to the appropriate location in the queue.
3. Performs a DSB operation to ensure observability of data written in step (2) before the update in step (4).
4. Updates the Command queue's PROD index register to publish the new commands to the SMMU.

Software is permitted to write any entry of the Command queue that is in an empty location between CONS and PROD indexes.

The SMMU might read and internally cache any command that is in a full location between PROD and CONS indexes If a command is cached, the cache is not required to be coherent with PE caches but if it is not coherent the following rules apply:

- When the SMMU stops processing commands because of a Command queue error, or when the queue is disabled, the SMMU invalidates all commands that it might have cached.
- A cached command must only be consumed one time and no stale cached value can be used instead of a new value when the queue location is later reused for a new command.

Note: The first rule means software can fix up or replace commands in the queue after an error, or while the queue is disabled, without performing any other synchronization other than restarting command processing.

Software must not alter memory locations representing commands previously submitted to the queue until those commands have been consumed, as indicated by the CONS index, and must not assume that any alteration to a command in a full location will be observed by the SMMU.

Software must only write the CONS index of an output queue (Event queue or PRI queue) in a consistent manner, with the appropriate incrementing and wrapping, unless the queue is disabled. If this rule is broken, for example by writing the CONS index with a smaller value, or incorrectly-wrapped index, the queue contents are UNKNOWN.

Software must only write the PROD index of the Command queue in a consistent manner, with the appropriate incrementing and wrapping, unless the queue is disabled or a command error is active, see section 7.1 Command queue errors . If this rule is broken, one of the following CONSTRAINED UNPREDICTABLE behaviors occurs:

- The SMMU executes one or more UNPREDICTABLE commands.
- The SMMU stops consuming commands from the Command queue until the queue is disabled and re-enabled.

## 3.21.3 Configuration structures and configuration invalidation completion

The entries of the configuration structures, the Stream table and Context Descriptors, all contain fields that determine their validity. An SMMU might read any entry at any time, for any reason.

STEs and CDs contain a valid flag, V. A structure is considered valid only when the SMMU observes it contains V == 1 and no configuration inconsistency in its fields causes it to be considered ILLEGAL.

Some structures contain pointers to subsequent tables of structures (STE.S1ContextPtr, (L1STD.L2Ptr) and L1CD.L2Ptr). If a structure is invalid, the pointers within it are invalid. The SMMU does not follow invalid pointers, whether speculatively or in response to an incoming transaction.

STEs in a linear Stream table and L1ST descriptors in a multi-level Stream table are located through the SMMU\_(*\_)STRTAB\_BASE address. Entries in these tables are not fetched if SMMU\_(*\_)CR0.SMMUEN == 0, because the base pointer is not guaranteed to be valid. These base pointers must be valid when the corresponding SMMUEN == 1. Configuration cache entries associated with a Security state are not inserted when, for that Security state, SMMU\_(*\_)CR0.SMMUEN == 0.

Similarly, CDs or L1CDs are located through the STE.S1ContextPtr and L1CD.L2Ptr pointers. A CD must never be fetched or prefetched unless indicated from a valid STE, meaning that the STE S1ContextPtr is valid and therefore the STE enables stage 1.

Note: A particular area of memory is only considered to be an STE or CD because a valid pointer of a certain type points to it (the SMMU\_(*\_)STRTAB\_BASE or L1STD.L2Ptr or STE.S1ContextPtr or L1CD.L2Ptr pointers respectively). A CD cannot be prefetched from an address that is not derived directly from the CD table configuration in a valid STE, as an area of memory is not a CD unless a valid STE or L1CD.L2Ptr points to it. Similarly, an L1CD is not actually an L1CD structure unless a valid STE points to it.

A structure is said to be reachable if a valid pointer is available to locate the structure. Depending on the structure type, the pointer might be a register base address or a pointer within a precursor structure (either in memory or cached). When SMMUEN == 0, no configuration structures are reachable. Otherwise:

- An STE is reachable if it is within the table given by the base and size indicated in the SMMU\_(*\_)STRTAB\_BASE\_* registers for a linear Stream table, or if it is within the 2 nd -level table indicated by a valid L1STD base and span for a two-level Stream table.
- A L1ST descriptor in a two-level Stream table is reachable if it is within the first-level table indicated by the base and size set in the SMMU\_(*\_)STRTAB\_BASE\_* registers.
- A CD is reachable if it is within the table given by the base and size indicated by a valid stage 1 S1ContextPtr and S1CDMax of a valid STE for a linear CD table, or if it is within the 2nd-level table indicated by a valid L1CD base and span for a two-level CD table.
- A VMS is reachable if the VMS is enabled for an STE.

An implementation does not fetch an unreachable structure. Walk of the tree of configuration tables does not progress beyond any invalid structure.

An implementation is permitted to fetch or prefetch any reachable structure at any time, as long as the generated address lies within the bounds of the table containing the structure. An implementation is permitted to cache any successfully fetched or prefetched configuration structure, whether marked as valid or not, in its entirety or partially. That is:

- Any STE or L1STD within the STE table (given by the base, size and intermediate table spans if appropriate) can be fetched and cached.
- Any CD or L1CD within a CD table can be fetched and cached.

When fetching a structure in response to a transaction, an implementation might read and cache more data than the required structures, as long as the limits of the tables are respected.

Note: Any change to a structure must be followed by the appropriate structure invalidation command to the SMMU, even if the structure was initially marked invalid.

Note: An unreachable structure cannot be fetched, because there is no valid pointer to it. However, a structure might be cached if it was fetched while the structure was reachable, even if it is subsequently made unreachable. For example, a valid STE could remain cached and later used after the SMMU\_(*\_)STRTAB\_BASE* registers are altered. Software must perform configuration cache maintenance upon changing configuration that might make structures unreachable.

A structure that is not actually fetched, such as a CD/L1CD, STE/L1STD or VMS that experiences an external abort (F\_CD\_FETCH, F\_STE\_FETCH or F\_VMS\_FETCH) or a CD/L1CD that fails stage 2 translation, does not cause knowledge of the failure to be cached. A future access of the structure must attempt to re-fetch the structure without requiring an explicit configuration structure invalidation command before retrying the operation that caused the initial structure fetch.

Note: For example, where stage 2 is configured to stall, to progress a transaction that causes a CD fetch that in turn causes a stage 2 Translation-related fault (an event with Stall == 1), it is sufficient to:

1. Resolve the cause of the translation fault, for example by writing a Translation table entry.
2. Issue a TLB invalidation operation, if required by the translation table alteration.
3. Issue a CMD\_RESUME, giving the StreamID and STAG appropriate to the event record.

An implementation must not:

- Read any address outside of the configured range of any table.
- -Speculative access of reachable structures is permitted, but address speculation outside of configured structures is not permitted.
- Cache any structure under a different type to the table from which it was read. For example, it must not follow the pointer of an STE to a CD and cache that CD (or any adjacent CD in the CD table) as anything non-CD, for example a translation table entry.

Software must ensure it only configures tables that are wholly contained in Normal memory.

A configuration invalidation operation completes after all of the following become true:

- All configuration cache entries targeted by the invalidation have been invalidated.
- No accesses can become visible to their Shareability domain using addresses or attributes that could not result from the configuration structures as observed after the invalidation operation became visible. This means that invalidation completes after:
- -Any client device transactions that used configuration cache entries that were targeted by the invalidation are globally visible to their Shareability domain.
- -Any configuration structure walks that used configuration cache entries that were targeted by the invalidation are complete so that all accesses to any fetched levels of the structures are globally visible to their Shareability domain. This applies to a configuration structure walk performed for any reason, including a configuration structure walk performed because of a prefetch, command, incoming transaction, ATOS or Translation Request.

An in-progress configuration structure walk (performed for any reason, including prefetch) can be affected by a configuration invalidation command (CMD\_CFGI\_*) if a cached intermediate structure that was previously referenced as part of the walk could have been invalidated. The completion of a configuration invalidation command (as determined by the completion of a subsequent CMD\_SYNC) ensures that any configuration structure walk that could be affected by the invalidate is either:

- Fully completed by the time the CMD\_SYNC completes.
- Stopped and restarted from the beginning after the CMD\_SYNC completes.

Note: This ensures that old or invalid pointers to subsequent configuration structures are never followed after an invalidation is complete. For example, when an SMMU has an STE pointing to a two-stage CD table and is prefetching a CD, then on reading the L1CD pointer, a CMD\_CFGI\_STE is processed that invalidates the STE that located the L1CD table. If the STE is made invalid, the pointer to the CD table is no longer valid and the SMMU must not continue to fetch the second-level CD after acknowledging to software that it considers the STE invalid. Software is free to re-use the memory used for the CD tables after receiving this acknowledgment, so continuing the prefetch after this point risks loading now-unrelated data. The SMMU must abort the fetch and not read the second-level CD, or must read the second-level CD before signaling the CMD\_CFGI\_STE/CMD\_SYNC as complete to software.

Note: Refer to the note in section 3.21.1 Translation tables and TLB invalidation completion behavior regarding observability of whether a translation table walk is stopped. For a configuration table walk that is stopped by an affected invalidation completion, an implementation is permitted to perform further fetches of a configuration structure walk after the completion, based on affected prior configuration structure reads that were made before the invalidation if, and only if, it is guaranteed that these reads have no effect on the SMMU or the rest of the system, are not made to addresses with read side effects, and will thus not affect the architectural behavior of the system.

The size of single-copy atomic reads made by the SMMU ( single-copy atomicity size ) is IMPLEMENTATION DEFINED but must comply with the following:

- If an SMMU is integrated in a system with PEs that implement FEAT\_LSE2, then the single-copy atomicity size for fetches of configuration structures issued by the SMMU is 128-bit.
- -Note: The SMMU is still permitted to issue smaller transactions where required. For example, the single-copy atomicity size of fetches and updates of VMSAv8-64 translation table descriptors is 64-bit.
- -Note: The single-copy atomicity size for fetches and updates of VMSAv9-128 translation table descriptors is 128-bit.
- Otherwise, the single-copy atomicity size must be at least 64-bit.

For a single-copy atomicity size that corresponds to a given structure, any single field within an aligned span of that size can be altered without first making the structure invalid. For example, to change the ASID in a CD, the ASID field can be written directly, followed by CMD\_CFGI\_CD and CMD\_SYNC. However, if there are two fields separated so that one single-copy atomic write cannot atomically alter both at the same time, the structure cannot be modified in this way. Non-single copy atomic writes might be visible to the SMMU separately and an inconsistent state might be cached (in which one field update has been read but another missed). The structure must, in this case, be made invalid, modified, then made valid, using the procedures described in section 3.21.3.1 Configuration structure update procedure .

Note: In some systems, 64-bit single-copy atomicity is only guaranteed to addresses backed by certain memories. If software requires such atomicity, it must locate SMMU configuration structures in these memories. For example, in LPAE ARMv7 systems, main memory is expected to be used to contain translation tables, and is therefore required to support 64-bit single-copy atomicity.

When a structure is fetched, the constituent 64-bit double-words of a structure are permitted to be accessed by the SMMUnon-atomically with respect to the structure as a whole and in any temporal sequence (maintaining the relative address sequence of the read portions).

## 3.21.3.1 Configuration structure update procedure

Note: The SMMU is not required to observe the structure word that contains the V flag in a particular order with respect to the other data in the structure. This gives rise to a requirement for an additional invalidation when transitioning a structure from V == 0 to V == 1.

Because the SMMU can read any reachable structure at any time, and is not required to read the double-words of the structure in order, Arm recommends that the following procedure is used to initialize structures:

1. Structure starts invalid, having V == 0.
2. Fill in all fields, leaving V == 0, then perform a DSB operation to ensure written data is observable from the SMMU.
3. Issue a CMD\_CFGI\_&lt;STRUCT&gt;, as appropriate.

4. Issue a CMD\_SYNC, and wait for completion.
5. Set V to 1, then perform a DSB operation to ensure write is observable by the SMMU.
6. Issue CMD\_CFGI\_&lt;STRUCT&gt;, as appropriate.
7. Optionally issue a CMD\_SYNC, and wait for completion. This must be done if a subsequent software operation, such as enabling device DMA, depends on the SMMU using the new structure.

To make a structure invalid, Arm recommends that this procedure is used:

1. Structure starts valid, having V == 1.
2. Set V == 0, then perform a DSB operation to ensure write is observable from the SMMU.
3. Issue a CMD\_CFGI\_&lt;STRUCT&gt;, as appropriate.
4. Issue a CMD\_SYNC, and wait for completion.

If software modifies the structure while it is valid, it must not allow the structure to enter an invalid intermediate state.

Note: Because the rules in section 3.21.3 Configuration structures and configuration invalidation completion disallow prefetch of a structure that is not directly reachable using a valid pointer, structures might be fully initialized (including with V == 1) prior to a pointer to the structure becoming observable by the SMMU. For example, a stage 1 translation can be set up with this procedure:

1. Allocate memory for a CD, initialize all fields including setting CD.V to 1.
2. Select an STE, initialize all fields and point to the CD, but leave STE.V == 0.
3. Perform a DSB operation to ensure writes are observable from the SMMU.
4. Issue a CMD\_CFGI\_STE and a CMD\_SYNC and wait for completion.
5. Set STE.V to 1, then perform a DSB operation to ensure write is observable from the SMMU.
6. Issue a CMD\_CFGI\_STE and CMD\_SYNC and wait for completion.

Note: No CMD\_CFGI\_CD is required because it is impossible for the CD to have been prefetched in an invalid state. However, a CMD\_CFGI\_CD must be issued as part of a procedure that subsequently makes the CD invalid.