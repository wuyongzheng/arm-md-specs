## 10.7 Support for Realm state

The presence of SMMU PMCG controls for Realm and Root states is indicated in SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL.

Arm strongly recommends that if an SMMU has SMMU\_ROOT\_IDR0.REALM\_IMPL = 1, then any SMMU PMCGs associated with that SMMU have SMMU\_PMCG\_ROOTCR.ROOTCR\_IMPL = 1.