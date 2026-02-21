## 2.5 SMMUv3.3 features

SMMUv3.3 extends the SMMUv3.2 architecture with the following features:

- Support for features of PEs implementing Armv8.5 [2]:
- -E0PD feature, equivalent to FEAT\_E0PD introduced in Armv8.5.
- -Protected Table Walk (PTW) behavior alignment with Armv8.
- -MPAM\_NS mechanism, for alignment with FORCE\_NS feature [3].
- -Requirements for interaction with the Memory Tagging Extension [2].
- Enhanced Command queue interface for reducing contention when submitting Commands to the SMMU.
- Support for recording non-Translation-related events for ATS Translation Requests.
- Guidelines for RAS error recording.

| SMMUfeature name            | Description                                                                                                 | A-profile feature name   |
|-----------------------------|-------------------------------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.3-E0PD Mandatory     | Support for preventing EL0 access to halves of address maps. See SMMU_IDR3.E0PD.                            | FEAT_E0PD                |
| SMMUv3.3-PTWNNC Mandatory   | Support for treating table walks to Device memory as Normal Non- cacheable. See SMMU_IDR3.PTWNNC.           | FEAT_E0PD                |
| SMMUv3.3-MPAM_NS Optional   | Support for Secure transactions using Non-secure PARTID space. See SMMU_S_MPAMIDR.HAS_MPAM_NS.              | FEAT_E0PD                |
| SMMUv3.3-ECMDQ Optional     | Support for Enhanced Command queue interfaces. See SMMU_IDR1.ECMDQ.                                         | FEAT_E0PD                |
| SMMUv3.3-SEC_ECMDQ Optional | Support for Enhanced Command queue interfaces for Secure state. See SMMU_S_IDR0.ECMDQ.                      | FEAT_E0PD                |
| SMMUv3.3-ATSRECERR Optional | Support for recording events on configuration errors for ATS translation requests. See SMMU_IDR0.ATSRECERR. | FEAT_E0PD                |

SMMUv3.3 also introduces the following optional features to the PMCG extension:

| SMMUPMCGfeature name      | Description                                                                                                                    |
|---------------------------|--------------------------------------------------------------------------------------------------------------------------------|
| SMMU_PMCGv3.3-FILTER_MPAM | Support for filtering event counts by MPAM attributes. See SMMU_PMCG_CFGR.FILTER_PARTID_PMG.                                   |
| SMMU_PMCGv3.3-MPAM_NS     | Support for issuing PMCG MSIs for Secure state, associated with a Non-secure MPAM PARTID. See SMMU_PMCG_S_MPAMIDR.HAS_MPAM_NS. |