## 2.2 SMMUv3.0 features

SMMUv3 provides feature to complement PCI Express [1] Root Complexes and other potentially large I/O systems by supporting large numbers of concurrent translation contexts.

- Memory-based configuration structures to support large numbers of streams.
- Implementations might support only stage 1, only stage 2 or both stages of translation. This capability, and other IMPLEMENTATION SPECIFIC options, can be discovered from the register interface.
- Up to 16-bit ASIDs.
- Up to 16-bit VMIDs [2].
- Address translation and protection according to Armv8.1 [2] Virtual Memory System Architecture. SMMU translation tables shareable with PEs, allowing software the choice of sharing an existing table or creating an SMMU-private table.
- 49-bit VA, matching Armv8-A's 2×48-bit translation table input sizes.

Support for the following is optional in an implementation:

- Either stage 1 or stage 2.
- Stage 1 and 2 support for the VMSAv8-32 LPAE and VMSAv8-64 translation table format.
- Secure stream support.
- Broadcast TLB invalidation.
- Hardware Translation Table Update (HTTU) of Access flag and dirty state of a page. An implementation might support update of the Access flag only, update of both the Access flag and the dirty state of the page, or no HTTU.
- PCIe ATS [1] and PRI, when used with compatible Root Complex.
- 16KB and 64KB page granules. However, the presence of 64KB page granules at both stage 1 and stage 2 is suggested to align with the PE requirements in the Server Base System Architecture.

Because the support of large numbers of streams using in-memory configuration causes the SMMUv3 programming interface to be significantly different to that of SMMUv2 [4], SMMUv3 is not designed to be backward-compatible with SMMUv2.

| SMMUfeature name              | Description                                                                             | A-profile feature name   |
|-------------------------------|-----------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.0-ASID16               | Support for 16-bit ASIDs, see SMMU_IDR0.ASID16.                                         |                          |
| SMMUv3.0-ATS                  | Support for PCIe ATS, see SMMU_IDR0.ATS and [1].                                        |                          |
| SMMUv3.0-BTM                  | Support for broadcast of TLB maintenance, see SMMU_IDR0.BTM.                            |                          |
| SMMUv3.0-HAD                  | Support for disabling hierarchical attributes in translation tables, see SMMU_IDR3.HAD. | FEAT_HPDS                |
| SMMUv3.0-HTTUA SMMUv3.0-HTTUD | Support for hardware translation table Access and dirty state, see SMMU_IDR0.HTTU.      | FEAT_HAFDBS              |
| SMMUv3.0-Hyp                  | Hypervisor stage 1 contexts supported, see SMMU_IDR0.HYP.                               | FEAT_VHE EL2             |
| SMMUv3.0-GRAN4K               | Support for 4KB translation granule, see SMMU_IDR5.GRAN4K.                              |                          |
| SMMUv3.0-GRAN16K              | Support for 16KB translation granule, see SMMU_IDR5.GRAN16K.                            |                          |
| SMMUv3.0-GRAN64K              | Support for 64KB translation granule, see SMMU_IDR5.GRAN64K.                            |                          |

| SMMUfeature name     | Description                                                                            | A-profile feature name   |
|----------------------|----------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.0-PRI         | Support for PCIe Page Request Interface, see SMMU_IDR0.PRI and [1].                    |                          |
| SMMUv3.0-S1P         | Support for Stage 1 translations, see SMMU_IDR0.S1P.                                   |                          |
| SMMUv3.0-S2P         | Support for Stage 2 translations, see SMMU_IDR0.S2P.                                   |                          |
| SMMUv3.0-SECURE_IMPL | Support for Secure and Non-secure streams, see SMMU_S_IDR1.SECURE_IMPL.                |                          |
| SMMUv3.0-TTFAA32     | Support for VMSAv8-32 LPAE format translation tables.                                  |                          |
| SMMUv3.0-TTFAA64     | Support for VMSAv8-64 format translation tables.                                       |                          |
| SMMUv3.0-VMID16      | Support for 16-bit VMID, see SMMU_IDR0.VMID16.                                         | FEAT_VMID16              |
| SMMUv3.0-ATOS        | Support for address translation operation registers, see SMMU_IDR0.ATOS.               |                          |
| SMMUv3.0-VATOS       | Support for stage 1-only address translation operation registers, see SMMU_IDR0.VATOS. |                          |

SMMUv3.0 also includes a Performance Monitor Counter Group extension, with the following optional features:

| SMMUPMCGfeature name              | Description                                                                                                 |
|-----------------------------------|-------------------------------------------------------------------------------------------------------------|
| SMMU_PMCGv3.0-SID_FILTER_TYPE_ALL | Support for filtering of event counts on a global or per-event basis. See SMMU_PMCG_CFGR.SID_FILTER_TYPE.   |
| SMMU_PMCGv3.0-CAPTURE             | Support for software-initiated capture of counter values. See SMMU_PMCG_CFGR.CAPTURE.                       |
| SMMU_PMCGv3.0-MSI                 | Support for PMCG-originated MSIs. See SMMU_PMCG_CFGR.MSI.                                                   |
| SMMU_PMCGv3.0-RELOC_CTRS          | Support for exposing PMCG event counts in independent page of address space. See SMMU_PMCG_CFGR.RELOC_CTRS. |
| SMMU_PMCGv3.0-SECURE_IMPL         | Support for counting events from more than one Security state. See SMMU_PMCG_SCR bit [31].                  |