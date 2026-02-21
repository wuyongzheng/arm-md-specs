## 17.6 SMMU support for partitioning and monitoring of internal resources

SMMU-internal resources are permitted to be affected by the PARTID of a client device transaction. The behavior of and control interface for this facility is IMPLEMENTATION DEFINED.

Note: For example, the SMMU might use this facility to implement a TLB-partitioning scheme.

The SMMU might use the PMG of the PARTID to provide monitoring facilities. The behavior of and control interface for this monitor facility is IMPLEMENTATION DEFINED.

Arm recommends that an implementation uses the MPAM MMR interface as defined in [3] for partitioning and monitoring of internal resources. The base address of these registers is IMPLEMENTATION DEFINED.