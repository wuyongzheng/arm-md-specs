## 2.3 SMMUv3.1 features

SMMUv3.1 extends the base SMMUv3.0 architecture with the following features:

- Support for PEs implementing Armv8.2-A:
- -Support for 52-bit VA, IPA, and PA.
* Note: An SMMUv3.1 implementation is not required to support 52-bit addressing, but the SMMUv3.1 architecture extends fields to allow an implementation the option of doing so.
- -Page-Based Hardware Attributes (PBHA).
- -EL0 vs EL1 execute-never controls in stage 2 translation tables.
- -Note: Armv8.2 introduces a Common not Private (CnP) concept to the PE which does not apply to the SMMUarchitecture, because all SMMU translations are treated as common.
- Support for transactions that perform cache-stash or destructive read side effects.
- Performance Monitor Counter Group (PMCG) error status.

| SMMUfeature name   | Description                                                                                   | A-profile feature name   |
|--------------------|-----------------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.1-XNX       | Provides support for translation table stage 2 Unprivileged Execute-never, see SMMU_IDR3.XNX. | FEAT_XNX                 |
| SMMUv3.1-TTPBHA    | Provides support for translation table page-based hardware attributes, see SMMU_IDR3.PBHA.    | FEAT_HPDS2               |
| SMMUv3.1-VAX       | Support for large Virtual Address space, see SMMU_IDR5.VAX.                                   | FEAT_LVA                 |
| SMMUv3.1-LPA       | Support for large Physical Address space, see SMMU_IDR5.OAS.                                  | FEAT_LPA                 |