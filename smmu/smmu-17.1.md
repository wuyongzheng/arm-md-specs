## 17.1 Discovery and global configuration

Support for MPAM is optional in SMMUv3.2 or later. Support can be discovered using SMMU\_IDR3.MPAM and the SMMU\_(*\_)MPAMIDR register in the programming interface of each Security state. If the SMMU supports MPAM, it might not be supported in all Security states.

When SMMU\_IDR3.MPAM == 1, the SMMU\_(*\_)MPAMIDR registers are present. The PMG and PARTID capabilities of a given Security state can be discovered using SMMU\_(*\_)MPAMIDR. MPAM is supported for a Security state when SMMU\_IDR3.MPAM == 1 and either of the corresponding SMMU\_(*\_)MPAMIDR.PARTID\_MAX or SMMU\_(*\_)MPAMIDR.PMG\_MAX fields are not zero.

The SMMU\_(*\_)GMPAM registers provide Global MPAM configuration used for some types of SMMU-originated transactions. See section 17.4 Assignment of PARTID and PMG for SMMU-originated transactions .

The SMMU\_(S\_)GBPMPAM registers provide MPAM configuration for client transactions that globally bypass the SMMU. When translation is enabled for a Security state, via SMMU\_(*\_)CR0.SMMUEN == 1, the MPAM configuration for a client transaction is determined from the corresponding STE.