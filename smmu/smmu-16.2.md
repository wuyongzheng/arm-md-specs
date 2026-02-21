## 16.2 Caching

An SMMU implementation is not required to implement caching of any kind, but Arm expects that performance requirements will require caching of at least some configuration or translation information.

Caching of configuration or translations might manifest as separate caches for each type of structure, or some combination of structures into a smaller number of caches. When architected structure types are cached together as one combined entry, the invalidation and lookup semantics remain identical to many specialized per-structure caches.

For example, an implementation with caches of each structure and translation stage implemented separately would contain:

- An STE cache
- -Indexed by StreamID.
- -Invalidated by StreamID, StreamID-span, or all.
- -Might contain a Level 1 Stream table cache of pointers to 2nd-level Stream table.
* Identical index/invalidation requirements.
- A CD cache
- -Indexed by StreamID and SubstreamID, or address.
* Note: Address index could be used, calculated from the STE.S1ContextPtr of a prior STE lookup plus the incoming SubstreamID. This arrangement might be useful where many STEs share a common table of CDs.
- -Invalidated by StreamID and SubstreamID, StreamID, or all.
- -Might contain a Level 1 CD table cache of pointers to 2nd-level CD table.
* Identical index and invalidation requirements.
- A VMS PARTID\_MAP cache
- -Indexed by VMID, or StreamID.
* Note: A VMS cache might be indexed by StreamID, but this would be no different to storing VMS data as part of an STE cache.
- -Invalidated by VMID, or StreamID.
- A stage 1 TLB (VA to IPA).
- -Indexed by VA, ASID, VMID and EL.
* EL is the Exception level or StreamWorld on whose behalf the TLB entry was inserted.
- -Invalidated by VA, ASID, VMID and EL, or ASID, VMID and EL, or VMID and EL, or EL.
- -Might contain or be paired with a walk cache (invalidated under the same conditions as PE translation walk caches).
- A stage 2 TLB (IPA to PA)
- -Indexed by IPA , VMID and EL.
- -Invalidated by IPA and VMID, or VMID, or all.
- -Might contain or be paired with a walk cache.

In this example, consistency is maintained by looking up cache entries in order from STE through CD, then using the parameters determined from that stream configuration to lookup in the TLBs. That is, given a StreamID, SubstreamID and VA input, convert StreamID and SubstreamID into ASID, VMID and Exception level, then use VA, ASID, VMID and EL to lookup in the TLBs.

## 16.2.1 Caching combined structures

Note: In the example given in 16.2 Caching , a stage 1 TLB is implemented separately to the stage 2 TLB. While this layout mimics the two stages of translation table, it might not provide optimal performance. A designer might determine that a combined stage 1 and stage 2 TLB is better, where each entry would translate V A to PA directly but would inherit invalidation requirements from both original structures.

For translations and TLBs, the SMMU invalidation rules for combined TLBs directly match those of Armv8-A.

Note: For example, an invalidation by IPA is not required to invalidate entries in a combined S1 and S2 TLB but is required to be paired with a second invalidation by V A or stage 1-all that would affect S1 and S2 TLB entries.

Combined structure caches maintain the same invalidation semantics as discrete structures. An entry of a combined cache is invalidated if any part of the entry would have been invalidated in an equivalent operation, with the same parameters, on a discrete cache.

Note: For example, a particular SMMU implementation maintains only two hardware caches, a combined cache of STE and CD, and a translation cache or TLB. In this layout, a StreamID and SubstreamID and VA input looks up StreamID and SubstreamID in the combined cache and determines the ASID, VMID, and StreamWorld at the same time. The translation is then looked up using V A, ASID, VMID and StreamWorld to determine the PA. The invalidation requirements of the combined STE and CD cache are the union of the requirements of the separate structures. STE invalidation operations invalidate every combined cache entry that contains data loaded using a given StreamID. This covers all CDs fetched from a given STE, which is implied anyway by the CMD\_CFGI\_STE to invalidate CDs subordinate to the STE. Conversely, every entry that contains data from a CD to be invalidated must be invalidated even if the STE portion is still valid.

An implementation might combine a TLB with configuration caching so that a single cache is looked up by StreamID and SubstreamID and VA and results in a PA output. Entries in this cache are invalidated when any part of an entry would match (or cannot be proven to not match) a required invalidation for STE, CD or translation.

Note: Implementations must balance a trade-off between over-invalidation that might be necessary to cover all required entries, and the cost of adding extra tagging. For example, a single cache might tag entries by V A, ASID, VMID, and StreamID so that broadcast TLB invalidations can remove only relevant entries, or so that an STE invalidation removes only entries that could have been constructed from the given StreamID.

## 16.2.2 Data dependencies between structures

The configuration structures logically make a tree or graph by indicating subsequent structures (and onwards, indicating translation tables). The structures contain fields to locate the next structure in the chain but might also modify interpretation of subsequent structures.

The dependencies between structures are:

- STE to CD to TT (stage 1)
- STE to TT (stage 2)

(Here, 'STE' might be composed of multi-level L1STD to STE lookups and CD might be composed of multi-level L1CD to CD lookups.)

The STE contains fields that determine how to locate a CD and stage 2 translations (whichever are relevant to STE.Config) but also contains fields that modify the behavior of a CD and translation table walks performed through it. For example:

- The STE StreamWorld (STRW plus STE Security state) determines the translation regime, which:
- -Tags caches of translations subsequently inserted, to separate lookup and match on invalidation
- -Determines which translation table formats are valid for use by the CD.
- STE.S1STALLD modifies CD.S behavior upon stage 1 fault.
- VMSAv8-32 LPAE stage 2 translation (STE.Config[1] == 1 and STE.S2AA64 selects VMSAv8-32 LPAE) causes a 64-bit stage 1 CD (CD.AA64 == 1) to be ILLEGAL.

Note: A change to an STE field requires an STE invalidation. An STE invalidation also invalidates all CDs that were cached through the STE.

The CD contains fields that determine how to locate translation tables but also contains fields that modify the behavior of a translation table walk through it:

- CD.{AA64, EPDx, SHx, ORx, IRx, TGx, TxSZ, ENDI, NSCFGx} govern walks of the translation table itself. In addition, NSCFGx can influence the NS attribute output from stage 1, because a translation table walk made to memory that is marked as Non-secure at stage 1 can never provide an output address that is Secure at the output of stage 1.
- CD.{UWXN, WXN, PAN, AFFD, HADx} govern permission checking with the translation table descriptors.
- CD.{ASID, ASET} govern ASID-tagged translation cache entries.
- CD.{MAIR, AMAIR} modify the attribute determined from translation.
- CD.{HA,HD} determines HTTU configuration for walks performed through TTB{0,1}.

Some STE and CD fields are permitted to be cached as part of a translation or TLB entry (therefore requiring invalidation of TLB entries that might contain the old value when the fields are changed). These fields are noted in sections 5.2 Stream Table Entry and 5.4.1 CD notes . With the exception of these fields, no other information is expected to be 'carried forward' between structures.

Some configuration register fields are, where indicated, permitted to be cached in a TLB. Changes to these fields require invalidation of any TLB entries that might cache a previous value of the field.