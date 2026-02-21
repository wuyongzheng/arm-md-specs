## 2.8 SMMUv3.4 features

SMMUv3.4 extends the SMMUv3.3 architecture with the following features:

- Support for features of PEs implementing Armv8.7 [2]:
- -52-bit virtual and physical address spaces when using 4KB and 16KB translation granule sizes.
- -Enhanced PAN mechanism.
- -Requirements for interoperability with PEs that implement FEAT\_XS. See 3.17.8 TLBInXS maintenance operations .
- Support for features of PEs implementing Armv8.9 [2]:
- -Stage 1 and Stage 2 permission indirections.
- -Stage 2 permission overlays.
- -Translation hardening.
- -Attribute Index Enhancement.
- -128-bit descriptors and 56-bit address spaces.
- -Table descriptor Access flag.
- -Stage 2 MemAttr NoTagAccess encodings.
- Support for the PASID TLP prefix for use on ATS Translated transactions.
- Deprecation of stashing translation information in ATS address fields.
- Deprecation of InD and PnU as output attributes.
- Deprecation of the SMMU\_PMCG\_PMAUTHSTATUS register.

| SMMUfeature name            | Description                                                                                                                        | A-profile feature name                          |
|-----------------------------|------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| SMMUv3.4-LPA2 Optional      | Support for 52-bits of virtual and physical address space when using the 4KB and 16KB translation granule sizes. See SMMU_IDR5.DS. | FEAT_LPA2                                       |
| SMMUv3.4-PAN3 Optional      | Support for the Enhanced PAN mechanism. See SMMU_IDR3.EPAN.                                                                        | FEAT_PAN3                                       |
| SMMUv3.4-THE Optional       | Support for translation hardening extension. See SMMU_IDR3.THE.                                                                    | FEAT_THE                                        |
| SMMUv3.4-S1PIE Optional     | Support for stage 1 permission indirections. See SMMU_IDR3.S1PI.                                                                   | FEAT_S1PIE                                      |
| SMMUv3.4-S2PIE Optional     | Support for stage 2 permission indirections. See SMMU_IDR3.S2PI.                                                                   | FEAT_S2PIE                                      |
| SMMUv3.4-S2POE Optional     | Support for stage 2 permission overlays. See SMMU_IDR3.S2PO.                                                                       | FEAT_S2POE                                      |
| SMMUv3.4-D128 Optional      | Support for 128-bit translation table descriptors. See SMMU_IDR5.D128, and SMMU_IDR5.{OAS, VAX}.                                   | FEAT_D128, FEAT_LVA3, 56-bit physical addresses |
| SMMUv3.4-AIE Optional       | Support for stage 1 Attribute Index Enhancement. See SMMU_IDR3.AIE.                                                                | FEAT_AIE                                        |
| SMMUv3.4-HAFT Optional      | Support for Table descriptor Access flags. See SMMU_IDR0.HTTU.                                                                     | FEAT_HAFT                                       |
| SMMUv3.4-MTE_PERM Mandatory | Support for stage 2 MemAttr NoTagAccess encodings. See SMMU_IDR3.MTEPERM.                                                          | FEAT_MTE_PERM                                   |
| SMMUv3.4-PASIDTT Optional   | Support for use of the PASID TLP prefix on ATS Translated transactions. See SMMU_IDR3.PASIDTT.                                     |                                                 |