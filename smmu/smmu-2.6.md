## 2.6 SMMU for RME features

SMMUfor RME introduces support for Granule Protection Checks, for interoperability with PEs that implement FEAT\_RME [2].

There are two aspects to RME support for SMMU:

- Whether the SMMU has the Root programming interface and can perform Granule Protection Checks. This is advertised with SMMU\_ROOT\_IDR0.ROOT\_IMPL == 1.
- Whether the SMMU has RME-related changes exposed to the Secure and Non-secure programming interfaces. This is advertised with SMMU\_IDR0.RME\_IMPL == 1.

Any SMMU behaviors specified as applying to an SMMU with RME apply to an SMMU implementation with SMMU\_ROOT\_IDR0.ROOT\_IMPL == 1.

An SMMU with RME must have SMMU\_ROOT\_IDR0.ROOT\_IMPL == 1. It is permitted for an SMMU with RME to have SMMU\_IDR0.RME\_IMPL == 0.

An SMMU with RME also implements SMMUv3.2 or later.

An SMMU with SMMU\_IDR0.RME\_IMPL == 1 does not support the EL3 StreamWorld. This means that:

- An STE with STRW configured for EL3 is ILLEGAL and results in C\_BAD\_STE.
- The commands CMD\_TLBI\_EL3\_ALL, CMD\_TLBI\_EL3\_VA result in CERROR\_ILL.
- The SMMU is not required to perform any invalidation on receipt of a broadcast TLBI for EL3.

Note: The value of SMMU\_IDR0.RME\_IMPL does not affect support for other features associated with Secure state.

See also 3.25 Granule Protection Checks .

| SMMURMEfeature name    | Description                                                                                                                            | A-profile feature name   |
|------------------------|----------------------------------------------------------------------------------------------------------------------------------------|--------------------------|
| SMMUv3.3-RME_ROOT_IMPL | Support for the Root programming interface. See SMMU_ROOT_IDR0.ROOT_IMPL.                                                              | FEAT_RME                 |
| SMMUv3.3-RME_IMPL      | Support for visibility of GPC faults to the Non-secure, Secure and Realm programming interfaces, if supported. See SMMU_IDR0.RME_IMPL. | FEAT_RME                 |
| SMMUv3.3-RME_BGPTM     | Support for broadcast TLBI PA operations. See SMMU_ROOT_IDR0.BGPTM.                                                                    | FEAT_RME                 |
| SMMUv3.3-RME_RGPTM     | Support for register TLBI by PA. See SMMU_ROOT_IDR0.RGPTM.                                                                             |                          |

An SMMU with RME implements either SMMUv3.3-RME\_ROOT\_IMPL or SMMUv3.3-RME\_IMPL.