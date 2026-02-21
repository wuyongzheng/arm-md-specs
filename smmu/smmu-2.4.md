## 2.4 SMMUv3.2 features

SMMUv3.2 extends the SMMUv3.1 architecture with the following features:

- Support for PEs implementing Armv8.4-A [2]:
- -Support for Memory System Resource Partitioning and Monitoring (MPAM) [3].
* Note: Support for MPAM is optional in SMMUv3.2.
- -Secure EL2 and Secure stage 2 translation.
* All previous rules about Secure streams being stage 1 only are removed.
- -Stage 2 control of memory types and cacheability.
- -Small translation tables support.
- -Range-based TLB invalidation and Level Hint.
- -Translation table updates without break-before-make.
- Introduction of a Virtual Machine Structure for describing some per-VM configuration.

| SMMUfeature name              | Description                                                                         | A-profile feature name   |
|-------------------------------|-------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.2-BBML1 SMMUv3.2-BBML2 | Support for change in size of translation table mappings, see SMMU_IDR3.BBML.       | FEAT_BBM                 |
| SMMUv3.2-RIL                  | Support for range-based TLB invalidation and level hint, see SMMU_IDR3.RIL.         | FEAT_TTL, FEAT_TLBIRANGE |
| SMMUv3.2-SecEL2               | Support for Secure EL2 and Secure stage 2 translations, see SMMU_S_IDR1.SEL2.       | FEAT_SEL2                |
| SMMUv3.2-STT                  | Support for small translation tables, see SMMU_IDR3.STT.                            | FEAT_TTST                |
| SMMUv3.2-MPAM                 | Support for Memory System Resource Partitioning and Monitoring, see SMMU_IDR3.MPAM. | FEAT_MPAM                |
| SMMUv3.2-S2FWB                | Support for stage 2 forced Write-Back, see SMMU_IDR3.FWB.                           | FEAT_S2FWB               |

SMMUv3.2 also introduces the following optional features to the PMCG extension:

| SMMUPMCGfeature name   | Description                                                                                                     |
|------------------------|-----------------------------------------------------------------------------------------------------------------|
| SMMU_PMCGv3.2-MPAM     | Support for associating PMCG-originated MSIs with specific MPAM PARTID and PMG values. See SMMU_PMCG_CFGR.MPAM. |