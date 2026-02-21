## 4.3 Configuration structure invalidation

After an SMMU configuration structure is altered in any way, an invalidation command must be issued to ensure that any cached copies of stale configuration are discarded. The following commands allow invalidation of L1STDs, Stream table entries, L1CDs and CDs by StreamID and by StreamID and SubstreamID. All configuration structures must be considered to be individually cached and the agent controlling the SMMU cannot assume that invalidation of one type of structure affects those of another type unless explicitly specified, regardless of the implementation properties of a particular SMMU. See section 16.2 Caching .

Modifications of translation tables require separate invalidation of SMMU TLBs, using broadcast TLB invalidation or explicit TLB invalidation commands. See section 4.4 TLB invalidation .

Where a StreamID parameter is provided, it corresponds directly with an STE or L1STD. The StreamID parameter indicates that an STE is to be invalidated, or a CD that has been located directly via the indicated STE. The SSec parameter indicates whether the invalidation applies to configuration related to the Secure or Non-secure Stream table.

A structure invalidation command, at a minimum, invalidates all cached copies of structures directly indicated by the command parameters. The commands are permitted to over-invalidate by invalidating other entries.

Note: Arm recommends that implementations limit over-invalidation to avoid a negative performance impact.

When issued from the Secure Command queue, a command might indicate a Secure or Non-secure Stream table entry and associated CD, using SSec. If over-invalidation occurs, it is permitted to affect either Security state.

Over-invalidation is permitted for non-locked configuration cache entries, but when issued from the Non-secure Command queue, Arm strongly recommends that a command only causes invalidation of cached copies of structures associated with Non-secure streams. Where IMPLEMENTATION DEFINED configuration cache locking is used, the IMPLEMENTATION DEFINED configuration cache invalidation semantics might restrict the effects of over-invalidation on locked configuration cache entries.

Note: Arm recommends that implementations choosing to allow over-invalidation consider the impact of Non-secure software being able to invalidate structures for Secure streams.

## 4.3.1 CMD\_CFGI\_STE(StreamID, SSec, Leaf)

<!-- image -->

Invalidate the STE indicated by StreamID and SSec.

This might be used for:

- Stream became invalid or valid.
- Enabling ATS.
- Enabling PASIDs.
- Changing stage 1 between bypass and translate.

Note: This command is not required to affect TLB contents. Separate TLB invalidation must be performed to clean up TLB entries resulting from a prior configuration.

When Leaf == 0, this command invalidates the STE for the specified StreamID, and all caching of the intermediate L1ST descriptor structures walked to locate the specified STE (as might be cached when multi-level Stream tables are used). When Leaf == 1, only the STE is invalidated and the intermediate L1ST descriptors are not required to be invalidated. An implementation is permitted to always invalidate the intermediate L1ST descriptors. STEs cached from linear Stream tables are invalidated with any value of Leaf.

This command invalidates all Context Descriptors (including L1CD) that were cached using the given StreamID.

This command invalidates all information cached from the VMS structure referenced using the given StreamID, for all configuration caches that are indexed by StreamID.

Arm recommends the use of the Leaf == 1 form of this command unless Leaf == 0 behavior is explicitly required. When a linear (single-level) Stream table is in use, the extra scope of the Leaf == 0 form is not required to be used.

Note: By avoiding Leaf == 0 invalidations unless cached intermediate pointers might exist from multi-level walks, invalidations might be faster and more power-efficient, depending on the implementation of STE caching.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.2 CMD\_CFGI\_STE\_RANGE(StreamID, SSec, Range)

<!-- image -->

Invalidate more than one STE, falling into the range of StreamIDs given by (inclusive):

<!-- formula-not-decoded -->

Invalidation is performed for an aligned range of 2 (Range+1) StreamIDs. The Range parameter encodes a value 0-31 corresponding to a range of 2 1 - 2 32 StreamIDs. The bottom Range+1 bits of the StreamID parameter are IGNORED, aligning the range to its size.

Note: Arm expects this command to be used for mass-invalidation when large sections of the Stream table are updated at the same time.

This command invalidates all caching of intermediate L1ST descriptors walked to locate the STEs in the given range (as might be cached when multi-level Stream tables are used). An implementation is permitted to over-invalidate these L1ST descriptors if required.

This command invalidates any Context Descriptors (including L1CD) that were cached using all StreamIDs in the given range.

This command invalidates all information cached from the VMS structure referenced using the given StreamID, for all configuration caches that are indexed by StreamID.

Note: CMD\_CFGI\_STE\_RANGE(n, SSec, 31) is the encoding for CMD\_CFGI\_ALL.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.3 CMD\_CFGI\_CD(StreamID, SSec, SubstreamID, Leaf)

<!-- image -->

Invalidate one CD.

This might be used when:

- Changing TTBRx/ASID (software must also invalidate TLBs using the old ASID).
- Enabling TBI.

The SubstreamID parameter indicates the Context Descriptor to be invalidated. When a cached Context Descriptor was fetched from index x of the CD table indicated by StreamID, then it is invalidated by this command when issued with SubstreamID == x. This includes the case where the STE indicates one CD which is equivalent to a CD table with one entry at index 0.

Note:

- Where substreams have been used with StreamID, that is when the STE located a CD table with multiple entries, the SubstreamID parameter indicates the CD to be invalidated as an index into the CD table.
- -STE.S1DSS might alter the translation behavior of the CD at index 0 (which might be used with SubstreamID 0, or transactions without a SubstreamID) but when issued with SubstreamID == 0, this command invalidates caching of the CD read from index 0 independent of its role in translation through S1DSS.
- Where substreams are not used with the given StreamID, this command invalidates the CD when it is issued with SubstreamID == 0.

When the SubstreamID parameter is outside of the range of implemented SubstreamIDs, including the case where SMMU\_IDR1.SSIDSIZE == 0 and the SubstreamID parameter is greater than 0, the behavior is consistent with the out-of-range parameter CONSTRAINED UNPREDICTABLE behavior described in section 4.1.7 Out-of-range parameters .

Note: An out-of-range SubstreamID parameter might cause this command to have no effect, or to operate on a different SubstreamID. In the case that SMMU\_IDR1.SSIDSIZE == 0, a non-zero SubstreamID parameter might invalidate the single cached CD or have no effect.

Note: In the case where STE.S1DSS == 0b10 , non-SubstreamID traffic uses CD table entry 0, which would be invalidated using this command with the SubstreamID parameter equal to 0, although SubstreamID == 0 traffic is terminated (therefore is not associated with CD table entry 0), see STE.S1DSS for more information.

Note: The SubstreamID parameter is interpreted as a CD table index to invalidate. As such, a configuration with one CD can be thought of as a one-entry table. To invalidate the CD cached from this configuration, the SubstreamID parameter to this command would be 0.

When Leaf == 0, this command invalidates all caching of an intermediate L1CD descriptor that locates the CD in a 2-level CD table (see STE.S1Fmt). When Leaf == 1, intermediate L1CD descriptors are not required to be invalidated. An implementation is permitted to always invalidate the intermediate descriptors.

This command raises CERROR\_ILL when stage 1 is not implemented.

A cached copy of CD data is treated as being local to the StreamID that locates the CD, because the CDs are indexed using SubstreamIDs whose scope is local to the StreamID. If multiple StreamIDs use a shared CD or table of CDs, the CD might be cached multiple times, having been fetched through any of the STEs. An invalidation command must be performed that affects all StreamIDs whose STEs point to the CD to be invalidated.

Note: This means that, when cached, CDs do not have to be located by address and might be indexed by StreamID and SubstreamID.

Note: For example, multiple CMD\_CFGI\_CD or CMD\_CFGI\_STE commands for each StreamID can be performed, or a wider-scope CMD\_CFGI\_STE\_RANGE or CMD\_CFGI\_ALL covering all StreamIDs.

Arm recommends the use of the Leaf == 1 form of this command unless Leaf == 0 behavior is explicitly required. When a linear (single-level) CD table is in use, the extra scope of the Leaf == 0 form is not required to be used.

Note: Avoiding Leaf == 0 invalidations unless cached intermediate pointers might exist from multi-level walks might have power and performance benefits.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.4 CMD\_CFGI\_CD\_ALL(StreamID, SSec)

<!-- image -->

Invalidate all CDs referenced by StreamID, for example when decommissioning a device. A separate command must also be issued to invalidate TLB entries for any ASIDs used, either by ASID or all.

Note: When STE configuration has enabled substreams, this command affects all CDs cached for the StreamID substreams. When STE configuration has disabled substreams and used a single CD for stage 1, this command affects that single CD.

This command must also invalidate caches of all intermediate L1CD descriptors that locate CDs using the given StreamID.

This command raises CERROR\_ILL when stage 1 is not implemented.

See 4.3.3 CMD\_CFGI\_CD(StreamID, SSec, SubstreamID, Leaf) , when a CD table is shared by multiple STEs this can give rise to multiple caches of each CD table entry. This command, or similar for STE or ALL scope, must be performed for all StreamIDs that could have cached the CD table contents.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.5 CMD\_CFGI\_VMS\_PIDM(SSec, VMID)

<!-- image -->

This command invalidates cached VMS.PARTID\_MAP information that is stored in a cache that is not affected by CMD\_CFGI\_STE*.

The SSec parameter is encoded the same as for other CMD\_CFGI\_* commands and indicates the Security state associated with the VMID parameter.

The validity and usage of the VMID parameter is consistent with the behavior of VMID in the CMD\_TLBI\_* commands. See section 4.4.2 TLB invalidation of stage 1 .

A CERROR\_ILL is raised in any of the following conditions:

- SMMU\_IDR3.MPAM == 0.
- MPAM is not supported by the programming interface indicated by SSec or the VMS is not supported by the programming interface indicated by SSec.
- SSec is used improperly, consistent with the common definition of SSec.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.5.1 Usage

The PARTID\_MAP might be cached in either of a configuration cache or a separate PARTID\_MAP cache. This means that a change to the PARTID\_MAP requires invalidation of both configuration that could have used that PARTID\_MAP and of a separate PARTID\_MAP cache. The following invalidation procedure can be used:

1. CMD\_CFGI\_VMS\_PIDM(s, VMID)
2. CMD\_SYNC
3. STE configuration cache invalidations for all StreamIDs associated with the VMS holding the PARTID\_MAP (for example, CMD\_CFGI\_STE\_RANGE).
4. CMD\_SYNC

Note: The VMID required for invalidation is the STE.S2VMID value that is used by the STEs that reference the VMS.

## 4.3.6 CMD\_CFGI\_ALL(SSec)

<!-- image -->

This command is encoded as CMD\_CFGI\_STE\_RANGE with Range == 31. This command invalidates:

- The cached configuration for all possible StreamIDs that are associated with the Security state given by SSec. Because Range == 31, the StreamID parameter is IGNORED.
- All information cached from all VMS structures associated with the Security state given by SSec, including from caches that are indexed by VMID.

The common behaviors for SSec apply. See 4.1.6 Common command fields .

Note: Behavior for caches indexed by StreamID is as described in CMD\_CFGI\_STE\_RANGE and invalidates caches of all configuration structures relevant to the Security state indicated by SSec. This includes caches of:

- Stream Table Entries.
- Intermediate or L1ST descriptor multi-level Stream Table Entries.
- Context Descriptors.
- Intermediate or L1CD multi-level Context Descriptor table entries.
- VMS structures.

Note: Arm recommends that an implementation explicitly detects this case and performs an invalidate-all operation instead of using an invalidate-range, if invalidate-all would be faster or more efficient.

Note: If it is required that TLB entries are also invalidated (such as reset-time initialization of the SMMU), Arm recommends that this command is followed by a command sequence to invalidate all TLB entries. A sequence in which TLB invalidations precede a CMD\_CFGI\_ALL might lead to a race in which TLB entries are pre-loaded using prefetch with possibly-stale cached configuration structures.

When issued to a Realm command queue, this command always applies to Realm StreamIDs only.

## 4.3.7 Action of VM guest OS structure invalidations by hypervisor

Note: When a guest issues structure invalidation commands on its Command queue, the hypervisor must perform maintenance on its behalf. In particular, StreamIDs might need to be mapped from the guest view into real system StreamIDs. Arm recommends the following behavior:

| Guest S1 command   | Hypervisor action                                                  | Notes                                                                                 |
|--------------------|--------------------------------------------------------------------|---------------------------------------------------------------------------------------|
| CMD_CFGI_STE       | Re-shadow STE, CMD_CFGI_STE                                        | Map guest StreamID to host StreamID. Note: SubstreamID is the same in guest and host. |
| CMD_CFGI_STE_RANGE | Re-shadow STEs, CMD_CFGI_STE or CMD_CFGI_STE_RANGE as appropriate. | Map guest StreamID to host StreamID. Note: SubstreamID is the same in guest and host. |
| CMD_CFGI_CD        | CMD_CFGI_CD                                                        | Map guest StreamID to host StreamID. Note: SubstreamID is the same in guest and host. |

| Guest S1 command   | Hypervisor action                                                    | Notes                                                                                                                                                                                 |
|--------------------|----------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| CMD_CFGI_CD_ALL    | CMD_CFGI_CD_ALL                                                      |                                                                                                                                                                                       |
| CMD_CFGI_ALL       | CMD_CFGI_ALL, or, For each S in (GUEST_STREAMS) { CMD_CFGI_STE(S); } | CMD_CFGI_ALL might over-invalidate and affect performance of other guests. An alternative is to explicitly invalidate structures for each StreamID assigned to the guest in question. |

## 4.3.8 Configuration structure invalidation semantics/rules

Stalled transactions are unaffected by structure or TLB invalidation commands and must be dealt with either by using CMD\_RESUME to retry or terminate them individually, or flushed using CMD\_STALL\_TERM for affected StreamIDs.

Note: When a stalled transaction is retried, it is re-translated as though it had just arrived, using newly-updated structures that might have been made visible to the SMMU with prior structure or TLB invalidation operations.

Translation of a transaction through the SMMU might not be a single atomic step and an invalidation command might be received while the transaction is in progress inside the SMMU. An invalidation of a structure that is used by a transaction that is in progress is not required to affect the transaction, if the transaction looked up the structure before it was invalidated. However, invalidation of any given structure must be seen as atomic so that a transaction must never see a partially-valid structure. A subsequent CMD\_SYNC ensures that the transaction, having used a structure that was affected by an invalidation command, is visible to the system before the CMD\_SYNC completes.

The consumption of structure and TLB invalidation commands does not guarantee invalidation completion. A subsequent CMD\_SYNC is consumed when all prior invalidations of both structure and TLB have completed.

Refer to section 3.21 Structure access rules and update procedures for structure update procedure and information about invalidation completion.