## 2.7 SMMU for RME DA features

SMMUfor RME DA introduces features that enable the association between devices and software executing in the Realm Security state. See [2].

Any SMMU behavior specified as applying to an SMMU with RME DA apply to an SMMU implementation with SMMU\_ROOT\_IDR0.REALM\_IMPL == 1. This means that in such implementations, Realm programming interface is supported.

| SMMURMEDAfeature name   | Description                                                                    | A-profile feature name   |
|-------------------------|--------------------------------------------------------------------------------|--------------------------|
| SMMUv3.3-RME_DA         | Support for the Realm programming interface. See SMMU_ROOT_IDR0.REALM_IMPL.    | FEAT_RME                 |
| SMMUv3.3-MEC_R          | Support for the RME Memory Encryption Contexts extension. See SMMU_R_IDR3.MEC. | FEAT_MEC                 |
| SMMUv3.3-DPT_R          | Support for Device Permission Table in Realm state. See SMMU_R_IDR3.DPT.       |                          |
| SMMUv3.3-DPT_NS         | Support for Device Permission Table in Non-secure state. See SMMU_IDR3.DPT.    |                          |

An SMMU with RME DA implements SMMUv3.3-RME\_DA.

## 2.7.1 Required features

An SMMU with SMMU\_ROOT\_IDR0.REALM\_IMPL == 1 implements all the mandatory features from SMMUv3.3, including the following requirements:

| Register field   |   Value | Notes                                        |
|------------------|---------|----------------------------------------------|
| SMMU_IDR3.PTWNNC |       1 | Mandatory from SMMUv3.3 onwards.             |
| SMMU_IDR3.E0PD   |       1 | Mandatory from SMMUv3.3 onwards.             |
| SMMU_IDR3.STT    |       1 | Mandatory because of Secure EL2 requirement. |
| SMMU_IDR3.FWB    |       1 | Mandatory from SMMUv3.2.                     |
| SMMU_IDR3.XNX    |       1 | Mandatory from SMMUv3.1.                     |
| SMMU_IDR3.HAD    |       1 | Mandatory from SMMUv3.1.                     |

An SMMU with SMMU\_ROOT\_IDR0.REALM\_IMPL == 1 additionally has the following features:

| Register field   | Value   | Notes                                    |
|------------------|---------|------------------------------------------|
| SMMU_IDR0.Hyp    | 1       | Required for EL2.                        |
| SMMU_IDR0.S1P    | 1       | Required for stage 1 translation.        |
| SMMU_IDR0.S2P    | 1       | Required for stage 2 translation.        |
| SMMU_IDR0.TTF    | 0b10    | VMSAv8-64 only.                          |
| SMMU_R_IDR3.DPT  | -       | Support for DPT is strongly recommended. |

| Register field           | Value   | Notes                                                                                 |
|--------------------------|---------|---------------------------------------------------------------------------------------|
| SMMU_IDR0.NS1ATS         | -       | If ATS is supported and DPT is not supported, then split-stage ATS must be supported. |
| SMMU_IDR0.COHACC         | 1       | Required for coherent access to RMM-managed tables.                                   |
| SMMU_IDR0.BTM            | -       | Support for broadcast TLB maintenance is strongly recommended.                        |
| SMMU_IDR0.HTTU           | -       | Support for Hardware update of Access Flag and Dirty state is strongly recommended.   |
| SMMU_IDR0.RME_IMPL       | 1       | Granule Protection Check faults are visible to Non-secure, Realm and Secure states.   |
| SMMU_IDR3.BBML           | 0b10    | Level 2 support is required.                                                          |
| SMMU_ROOT_IDR0.ROOT_IMPL | 1       | SMMUmust be able to perform Granule Protection Checks.                                |