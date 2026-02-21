## 13.7 PCIe permission attribute interpretation

PCIe-domain permissions are interpreted by the SMMU as described in this section.

Base PCIe interconnect expresses only a Read/Write access permission. The PASID TLP prefix adds the following access permissions:

- Execute (In the PASID, Execute\_Requested, hereafter referred to as 'Exe')
- Privileged (In the PASID, Privileged\_Mode\_Requested, hereafter referred to as 'Priv')

For normal transactions, the SMMU can use R/W and Privileged directly as incoming R/W and PRIV attributes. Note: The PASID TLP prefix can only encode an 'Execute' attribute for Memory Read Requests; this is compatible with the SMMU's behavior in considering all write transactions to be Data.

The SMMU interprets the INST and PRIV attributes of a normal transaction without a PASID TLP prefix as 'Data' and 'Unprivileged', respectively.

For an ATS Translation Request, base PCIe supplies:

- Read access is implied in all ATS Translation Requests
- -An ATS Translation Completion might grant per-page Read access, depending on page permissions.
- No-Write (NW)
- -NW== 0 signals the intention of the device to perform write accesses. When NW == 0, the Translation Completion sent by the SMMU grants Write permission if the page is currently marked as either:
* Writable-dirty.
* Writable-clean if HTTU is enabled.
- -When NW == 1, Write permission is permitted but not required to be granted if the page is already marked as writable-dirty.
- -If HTTU is not enabled, Write permission is not granted when the page is marked as writable-clean.
- -When HTTU is enabled, a request having NW == 0 to a page marked writable-clean updates the page to be marked Dirty and then grants Write permission in the response. See 3.13.7 ATS, PRI and translation table flag update .

Note: Referring to the above, a request with NW == 1 might grant write access if the page is already marked Dirty (as the page permissions contain write permission).

- -HTTU does not mark a page Dirty in response to a Translation Request with NW == 1.

The PASID TLP prefix adds the following to an ATS Translation Request:

- Execute (Exe)
- -This flag requests execute permission. If this flag is set, the response might grant execute permission. The response must not grant execute permission if this flag is not set in the request. A valid translation might or might not grant the requested Execute permission, depending on actual page 'X' permission. Note: A request might be made with Exe == 1 and NW == 0, meaning an endpoint requests access for write and execute. This does not imply that the endpoint will perform 'instruction writes' to the page.
- -Exe implies R in an ATS response.

Certain configurations of VMSAv8-64 translation tables allow an 'XO' execute-only permission. A translation that requests Exe permission through ATS is not compatible with an XO page and will result in no access, unless STE.INSTCFG == Instruction. Similarly, care must be taken when using the Stage 2 'XO' permission with ATS; a guest might map all executable pages as RX but a hypervisor Stage 2 can further modify this down to execute-only. See section 13.7.1 Permission attributes granted in ATS Translation Completions below for more information on ATS Exe permission.

- Privileged (Priv)

- -This flag marks the request as being made from a privileged or unprivileged entity in the endpoint. The Priv flag in an ATS Translation Completion Data Entry has the same value as the Priv flag provided with the corresponding ATS Translation Request and the entry contains permissions granted only to that entity/privilege level.

Note: The PCIe Specification [1] states: 'The ATC must not assume any correlation between the Privileged Mode and Unprivileged Mode permissions associated with a translation.'

For an ATS Translation Request without a PASID TLP prefix, the INST and PRIV attributes are treated by the SMMUas 'Data' and 'Unprivileged', respectively.

Translated transactions that do not have a PASID TLP prefix are treated by the SMMU as 'Data', 'Unprivileged'. This applies to all of the following:

- Implementations with SMMU\_IDR3.PASIDTT == 0.
- Implementations with SMMU\_IDR3.PASIDTT == 1, and the Translated transaction does not have a PASID TLP prefix.

The SMMU uses incoming Priv and Exe attributes if provided in the PASID TLP prefix if SMMU\_IDR3.PASIDTT == 1.

The following table of example ATS Translation Requests shows the access permissions granted for the request on several different page permission combinations:

| Example Request                | Page permissions                    | Response                                                                                                                                            |
|--------------------------------|-------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------|
| NW==1, Exe == 0, Priv == 0     | User-RO, Priv-RW, XN == 0           | R == 1, W==0, Exe == 0, Priv == 0                                                                                                                   |
| NW==0, Exe == 0, Priv == 0     | User-RW, Priv-RW, XN == 0           | R == 1, W==1, Exe == 0, Priv == 0                                                                                                                   |
| NW==0, Exe == 0, Priv == 0     | User-RO, Priv-RW, XN == 0           | R == 1, W==0, Exe == 0, Priv == 0                                                                                                                   |
| NW==0, Exe == 0, Priv == 1     | User-RO, Priv-RW, XN == 0           | R == 1, W==1, Exe == 0, Priv == 1                                                                                                                   |
| NW==1, Exe == 1, Priv == 0     | User-RW, Priv-RW, XN == 1           | R == 1, W==0or 1, Exe == 0, Priv == 0 Note: The SMMUis permitted to return Write permission if the page is writable, even if NW==1.                 |
| NW==0, Exe == 0, Priv == 0     | User-RW, Priv-RW, XN == 1           | R == 1, W==1, Exe == 0, Priv == 0                                                                                                                   |
| NW==0, Exe == 1, Priv == 0     | User-RW, Priv-RW, XN == 0           | R == 1, W==1, Exe == 1, Priv == 0                                                                                                                   |
| NW==0, Exe == 1, Priv == 0     | User-X, Priv-RW, UXN == 0 (AArch64) | R == 0, W==0, Exe == 0, Priv == 0                                                                                                                   |
| NW==any, Exe == any, Priv == p | Translation-related fault           | R == 0, W==0, Exe == 0, Priv == p Note: See 3.9.1 ATS Interface ; this Translation Completion is marked with 'Success' status, as opposed to UR/CA. |

When the STE.INSTCFG and STE.PRIVCFG override fields are supported (SMMU\_IDR1.ATTR\_PERMS\_OVR == 1), they affect ATS Translation Requests as described in 13.7.1 Permission attributes granted in ATS Translation Completions below.

Note: Arm recommends that an STE does not override INST and PRIV when the system supports PCIe PASID prefixes, in order for this attribute to be communicated from the device to the SMMU translation lookup. However, when a PASID TLP prefix is not used and the INST and PRIV attributes are treated by the SMMU as 'Data' and 'Unprivileged', as required above, software might override these attributes using the STE input overrides. For example, it might configure a stream to be privileged. When PASIDs/SubstreamIDs are configured for a translating Stage 1 configuration, traffic without a PASID is deemed unexpected if STE.S1DSS == 0b00 , and

aborted. If STE.S1DSS == 0b01 , traffic without a PASID skips Stage 1 and translation behaves as though the STE is configured for Stage 2-only translation. In this case, the PRIV attribute is ignored by Stage 2 and the 'Data' default is sensible.

When HTTU is in use, an ATS TR that generates a response with R == 1 || W == 1 || Exe == 1 also sets the AF flag in the descriptor to 1. When HTTU is enabled for dirty state update (using HD flags), an ATS TR having NW == 0 to a writable-clean page accessible at the requested permission level (permissions are read-only, with DBM == 1 when using the Direct Permission Scheme) will make the page permissions read/write (writable-dirty) and generates a response with W == 1. An ATS TR having NW == 1 must not mark a page as writable-dirty.

Note: TTW in nested stage 1+stage 2 scenarios might cause stage 2 pages to be marked writable-dirty where Stage 1 translation table descriptors are updated.

Note: As STE.{INSTCFG,PRIVCFG} overrides might affect the permissions granted in an ATS response, a change to these overrides must be accompanied by an invalidation of associated ATCs.

Note: When Split-stage ATS is in use, stage 2 translation is performed on incoming Translated transactions. A Translated transaction in implementations with SMMU\_IDR3.PASIDTT == 0 from PCIe is treated as Data, Unprivileged. This means that for such implementations, it is possible to configure stage 2 execute permissions so that the ATS Translation Request succeeds, but the subsequent Translated transactions not permitted. For example:

1. A Split-stage ATS Translation Request from a stream with STE.INSTCFG == Instruction is made to an address where stage 1 has RWX permissions and stage 2 has Privileged-XO permissions.
2. The ATS Translation Request succeeds because the combined stage 1+2 permission is Privileged-XO and the STE.INSTCFG configuration treats all accesses as execute.
3. The Translated transaction is translated at stage 2, but is treated by the SMMU as Unprivileged, which causes a stage 2 permission fault.

It is IMPLEMENTATION DEFINED whether STE.{INSTCFG, PRIVCFG} override fields affect an ATS Translated transaction when SMMU\_(R\_)CR0.ATSCHK == 1 for a stream configured with STE.EATS == 0bx1 . Arm recommends that an SMMU implementation applies the override fields to Translated transactions in the same manner as for Translation Requests.

For an ATS Translated transaction issued by a StreamID configured with STE.EATS == 0b10 , the overrides that are configured in STE.INSTCFG and STE.PRIVCFG are applied to the Translated transaction prior to stage 2 translation and permission checking.

Note: PRIVCFG only affects stage 2 permission checking if SMMU\_IDR3.XNX == 1.

Note: Use of Split-stage ATS with STE.INSTCFG, or stage 2 permissions that are not expressible in PCIe, can lead to unexpected results. Arm recommends that STE.INSTCFG is not used with ATS.

## 13.7.1 Permission attributes granted in ATS Translation Completions

The pseudocode below illustrates how the R, W, Exec, Priv attributes in a Translation Completion are calculated with respect to the input Translation Request, the translation table descriptor permissions and the STE INSTCFG/PRIVCFG overrides.

A PRIVCFG == Privileged or PRIVCFG == Unprivileged override calculates (R,W,X) attributes appropriate to the privilege level to which the request was overridden, but the 'Priv' field in the ATS Translation Completion returns the same privilege supplied in the associated Translation Request.

- For example, a TR with 'NW == 0, Exe == 0, Priv == 1' with PRIVCFG == Unprivileged, and page permissions of 'User-RO, Priv-RW', returns a Translation Completion with 'R == 1, W == 0, Exe == 0, Priv == 1'.

The INSTCFG override affects the interpretation of the TR's Exe and the translation table 'X' attributes.

```
// Here, TR is the incoming Translation Request, TC is the returned // Translation Completion and final_combined_translation is the // result of all enabled stages of translation for the given address. // HTTU is not shown; it is assumed final_combined_translation contains // post-HTTU permissions if relevant. (Note: HTTU for ATS is influenced
```

```
// by TR.NW.) if (!TR.PASID_present) { // The Priv and Exe fields of a Translation Completion without a // PASID are Reserved and set to 0. Effectively, there are no Priv // and Exe permission bits in a response without a PASID: TR.Priv = 0; TR.Exe = 0; } // The Translation Completion's Priv field is not affected by PRIVCFG and // is as the TR supplied: TC.Priv = TR.Priv; STE_effective_PRIVCFG = (SMMU_IDR1.ATTR_PERMS_OVR == 1) ? STE.PRIVCFG : Use_Incoming; STE_effective_INSTCFG = (SMMU_IDR1.ATTR_PERMS_OVR == 1) ? STE.INSTCFG : Use_Incoming; // Effective privilege that permissions will be checked against: effectivePriv = (STE_effective_PRIVCFG == Use_Incoming) ? TR.Priv : ((STE_effective_PRIVCFG == PRIVILEGED) ? 1 : 0)); ttd_R = final_combined_translation.readable_by_privlevel(effectivePriv); ttd_RX = ttd_R && final_combined_translation.executable_by_privlevel(effectivePriv); ttd_X = final_combined_translation.executable_by_privlevel(effectivePriv); // Grant of write permission is always governed by the translation's W // permission. Also note that, when enabled, HTTU only sets Dirty if // TR.NW == 0; the page is writable if this is the case, or if the page is // already Dirty (see text). // Note: An implementation is not *required* to return W == 1 if // TR.NW == 1 and translation table descriptor permissions include write, // but doing so can avoid the Endpoint having to make a second request if it // subsequently requires to write. TC.W = final_combined_translation.writable_by_privlevel(effectivePriv); if (STE_effective_INSTCFG == Use_Incoming) { TC.R = ttd_R; TC.Exe = TR.Exe && ttd_RX; // Granting X implies granting R // Note: An execute-only (XO) translation grants no access to ATS. // A normal (non-ATS) transaction for Exe == 1 will succeed // to an XO translation. } else if (STE_effective_INSTCFG == INST) { TC.R = ttd_X; TC.Exe = TR.Exe && ttd_X; // Note: An XO translation can grant R&Exe access to an ATS Request // because in this configuration all reads are considered // instruction fetches, therefore R&Exe are the same. } else { // STE.INSTCFG == DATA // This is effectively equivalent to assuming X=R; anything with 'R' // for the privilege level is accessible. TC.R = ttd_R; TC.Exe = TR.Exe && ttd_R; }
```