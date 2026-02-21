## Chapter 9

## Address Translation Operations

The SMMU optionally supports a software-accessible Address Translation Operations (ATOS) facility. The presence of this facility is reported by SMMU\_IDR0.ATOS. The ATOS facility allows software to perform an address lookup to determine the output address that a transaction would take, given an input address, stream, substream and access properties. The requested lookup can be the full end-to-end, with all configured stages, or only a part of the configuration for the stream. The result of the request is either the output address or a fault status code, if a translation is unable to complete. Unlike transactions, ATOS requests are not affected by fault configuration bits in the STE or CD, and do not record fault events or stall.

If ATOS is supported, an optional virtual ATOS (VATOS) page might also be supported. This is reported by SMMU\_IDR0.VATOS. The VATOS page can be mapped through to a chosen software entity so that it might perform a limited set of stage 1-only ATOS lookups directly. The V ATOS interface can make stage 1-only ATOS lookups for stage 1 and stage 2 nested configurations, or for stage 1-only configurations. The V ATOS interface can only make lookups for configurations associated with the NS-EL1 StreamWorld.

Note: Arm expects VATOS to be used with stage 1 and stage 2 nested configurations.

When ATOS is supported, a group of SMMU\_GATOS\_SID, SMMU\_GATOS\_ADDR and SMMU\_GATOS\_PAR registers are available in the memory map. When SMMU\_S\_IDR1.SECURE\_IMPL == 1, a second group is present in SMMU\_S\_GATOS\_SID, SMMU\_S\_GATOS\_ADDR, SMMU\_S\_GATOS\_PAR. If VATOS is supported, a third group, SMMU\_VATOS\_SID, SMMU\_VATOS\_ADDR and SMMU\_VATOS\_PAR, are present in a distinct VATOS page, see Chapter 6 Memory map and registers . If both VATOS and Secure stage 2 are supported, a fourth group SMMU\_S\_VATOS\_SID, SMMU\_S\_VATOS\_ADDR and SMMU\_S\_VATOS\_PAR, are present in a distinct S\_VATOS page.

When Secure stage 2 is supported, the SMMU\_S\_GATOS interface can be used to issue stage 1+2 and stage 2 ATOS lookups to Secure streams, that is, when SMMU\_S\_GATOS\_SID.SSEC == 1. These lookups are subject to the same validity checks with respect to configured and enabled stages of translation as would be performed using the Non-secure GATOS interface.

Each group of registers might perform one lookup at a time, but all implemented sets of registers might perform independent lookups simultaneously. Access to a register that affects ATOS behavior only affects the group that is accessed, and programming of the registers (whether correct or incorrect) does not affect other groups.

Apart from differences in scope the groups of registers are equivalent and are referred to generically using ATOS\_ prefixes in this chapter. The difference in scope between the ATOS registers is that the V ATOS registers can only access stage 1 translations, the GATOS registers cannot access Secure stream information, and the S\_GATOS registers can access Secure stream information.

The ATOS registers might perform address lookups with the following properties as though a transaction were received through a given StreamID and SubstreamID:

- Read/Write.
- Unprivileged/Privileged.
- Instruction/Data.

The types of translations available are:

- VA to PA for a stage 1 and stage 2 configuration.
- VA to IPA for a stage 1 of a stage 1 and stage 2 configuration.
- VA to IPA or PA for a stage 1-only configuration.
- IPA to PA for a configuration with stage 2.

The lookup procedure is:

1. Ensure the ATOS interface is idle (ATOS\_CTRL.RUN == 0) and claimed for exclusive use in case several agents share the interface.
2. Ensure ATOS\_SID identifies the StreamID and SubstreamID that will be used for the lookup.
3. Write the source address and lookup action to ATOS\_ADDR.
4. Ensure the prior register writes are observed by the SMMU before the following write.
5. Write ATOS\_CTRL.RUN == 1 to initiate the lookup.
6. Poll ATOS\_CTRL.RUN; the SMMU clears the RUN flag when the result is ready.
7. The result appears in ATOS\_PAR. This might be a result address or a fault code, determined in the same way as for an ordinary input transaction.

The translation process for an ATOS request is not required to begin immediately when ATOS\_CTRL.RUN is written to 1, and will begin in finite time. Arm expects that any delay will be small.

An ATOS translation interacts with configuration and TLB invalidation in the same way as a translation that is performed for a transaction. The result of an ATOS translation that completes after an invalidation completes is not based on any stale data that was targeted by the invalidation. See section 3.21 Structure access rules and update procedures for more information.

Note: A CMD\_SYNC depends upon the visibility of HTTU updates performed by completed ATOS translations.

The completion of an invalidation operation is permitted, but not required, to depend on either of the following:

- The completion of an ATOS translation that has been requested by writing RUN to 1 but has not begun before the invalidation completion operation was observed.
- The completion of an ATOS translation that is unaffected by the invalidation.

The domain of the lookup, in Secure, Non-secure, hypervisor, EL3 or Monitor terms, is determined by the stream configuration. Translations from a Secure stream are only returned through the S\_ATOS interface. A Non-secure stream might be queried by either interface. The S\_ATOS interface contains a SSEC flag to indicate whether the requested StreamID is to be treated as Secure or Non-secure.

The lookup action provided in the write to ATOS\_ADDR determines the read/write, instruction/data and privilege attributes of the request.

The treatment of the input address that is provided by ATOS\_ADDR is governed by the same rules that affect an ordinary translation, in terms of range checks according to TxSZ, IPS, and PS SMMU properties. See section 3.4 Address sizes . ATOS\_ADDR.ADDR provides an input 64-bit address.

Note: As the full address is provided, a translation lookup could fail with a Translation fault because it is outside the configured input range for the initial stage or stages of lookup. This includes consideration of the Top Byte Ignore (TBI) configuration.

With respect to memory attributes, responses to ATOS requests reflect the attributes assigned in the translation table descriptors and STE memory attribute overrides do not have an effect on ATOS requests. See Table 13.5.

The permissions model used by an ATOS translation is the same as is used for an ordinary transaction, except that the read/write, instruction/data and privileged/unprivileged properties of the translation are taken directly from ATOS\_ADDR instead of coming from an input transaction or overrides in STE.{INSTCFG, PRIVCFG}. See Table 13.4.

Note: The ATOS permission attributes are not affected by the STE.INSTCFG or STE.PRIVCFG overrides.

In the case where an ATOS operation explicitly performs translation at only one stage when a stream is configured for stage 1 and stage 2 translation, only the permission configuration that is applicable to the requested translation stage is used.

Note: This means that CD-based permission controls such as PAN, UWXN and WXN are not used when an ATOS translation does not translate using stage 1. When stage 1 is in use, all of the CD-based permission controls are used by ATOS, in the same way as would be done for an ordinary transaction. These are CD.PAN, CD.UWXN, CD.WXN and CD.HAD{0,1}.

When ATOS\_ADDR.HTTUI == 0, ATOS operations perform HTTU when supported by the SMMU and configured for any of the translation regimes used to perform the lookup, in the same way as would occur for a read or write transaction to the same address of the same StreamID/SubstreamID, including fetch of CD and Stage 1 translation table descriptors through stage 2 translations.

When ATOS\_ADDR.HTTUI == 1, the request inhibits HTTU and the behavior is as follows:

- When an Access flag update is enabled for a stage of translation, the SMMU is permitted but not required to set the Access flags in translation table descriptors for the requested address. If AF == 0, then the ATOS translation behaves as though AF == 1, even if the Access flag is not updated. If a translation-related fault or external abort occurs as a result of performing the Access flag update, it is IMPLEMENTATION DEFINED whether the ATOS operation reports the fault or whether the operation continues as though the Access flag was successfully updated. Note: This applies to AF updates to Page and Block descriptors, if either (STE.S2HA == 1 or CD.HA == 1), as well as to Table descriptors, if either (STE.S2HAFT == 1 or CD.HAFT == 1).
- When update of the dirty state of a page is enabled for a stage of translation (STE.S2HD == 1 or CD.HD == 1), a translation table descriptor that is writable-clean is considered to be writable by the ATOS mechanism but the descriptor is not updated to writable-dirty.

Setting ATOS\_ADDR.HTTUI == 1 has no effect when updates to both the Access flag and dirty state of the page are disabled.

Note: The behavior of an ATOS operation with HTTUI == 1 matches that of address translation operations in the PE, with respect to AF and dirty state of the page permissions.

Note: If HTTU is inhibited in order to translate without changing the translation table state, this inhibition includes stage 2 translation tables that back the stage 1 translation table in nested configurations.

An implementation is allowed to update stage 1 AF when ATOS\_ADDR.HTTUI == 1 only if the associated stage 2 descriptor is already marked as writable-dirty.

When HTTU is enabled at stage 2 in a nested stage 1 and stage 2 configuration, and ATOS performs a stage 1-only VA to IPA translation and HTTU is enabled for ATOS, the SMMU does not mark the final IPA's page as dirty and is permitted but not required to mark the final IPA's page as accessed.

ATOS requests using SMMU\_GATOS\_* or SMMU\_VATOS\_* require SMMU\_CR0.SMMUEN == 1 and ATOS requests using SMMU\_S\_GATOS\_* or SMMU\_S\_VATOS\_* require SMMU\_S\_CR0.SMMUEN == 1. When an ATOS request is issued on the Secure SMMU\_S\_GATOS\_* interface and SMMU\_S\_GATOS\_SID.SSEC == 0, the translation also requires SMMU\_CR0.SMMUEN == 1. See SMMU\_GATOS\_CTRL and SMMU\_S\_GATOS\_CTRL for more information.

An ATOS request is permitted to use and insert cached configuration structures and translations, consistent with any caches that are provided for transaction translation. Regardless of the value of ATOS\_ADDR.HTTUI , an ATOS request that uses a configuration that has HTTU enabled, that is a configuration with STE.S2HA == 1, CD.HA == 1, STE.S2HD == 1, or CD.HD == 1, does not insert or update TLB entries that would be marked as Accessed or Dirty when their associated translation table descriptors in memory are not.

When SMMU\_S\_IDR1.SECURE\_IMPL == 1, the SMMU does not allow:

- Secure information to be used to form a Non-secure ATOS\_PAR result
- A Non-secure ATOS request to affect SMMU\_S\_GATOS\_* register values, including PAR, or active Secure ATOS translation requests.