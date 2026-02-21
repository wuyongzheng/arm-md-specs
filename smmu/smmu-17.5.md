## 17.5 Assignment of PARTID and PMG for PMCG-originated MSIs

A PMCG might independently support MPAM if the PMCG supports MSIs, so that MPAM information can be assigned to the MSI write.

Note: As a PMCG might be implemented separately to an SMMU, or in a distributed manner, the PMCG might generate MSI transactions in a different way to that of the SMMU queue/table accesses, so is configured separately.

Arm recommends that all PMCGs associated with an SMMU support the same MPAM facilities as the SMMU. This means that support for MPAM is recommended to be consistent amongst all PMCGs and SMMU, and that the components support PARTID and PMG sizes large enough to carry any valid system PARTID and PMG values.

Note: Because a PMCG might be implemented in a different component to the SMMU, or to other PMCGs, it is not an architectural requirement that a PMCG supports MPAM.

The PMCG has the following registers for MPAM discovery and configuration:

- SMMU\_PMCG\_MPAMIDR gives the maximum Non-secure PARTID and PMG values that can be configured for an MSI.
- SMMU\_PMCG\_S\_MPAMIDR gives the maximum Secure PARTID and PMG values that can be configured for an MSI.
- SMMU\_PMCG\_GMPAM configures the PARTID and PMG values for a PMCG MSI.
- -When the PMCG is configured to use a Non-secure attribute on an MSI, this register configures Non-secure PARTID and PMG values.
- -When the PMCG is configured to use a Secure attribute on an MSI, and SMMU\_PMCG\_SCR.MSI\_MPAM\_NS is 0 or RES0, this register configures Secure PARTID and PMG values.
- -When the PMCG is configured to use a Secure attribute on an MSI, and SMMU\_PMCG\_SCR.MSI\_MPAM\_NS is 1, this register configures Non-secure PARTID and PMG values.
- -Note: The target PA space of an MSI is determined by both SMMU\_PMCG\_SCR.NSMSI and SMMU\_PMCG\_SCR.NSRA.
- -Note: Arm expects that SMMU\_PMCG\_SCR.NSMSI is only set during the transition of a PMCG from Non-secure to Secure state, and therefore using the output PA space to select the MPAM Security state is consistent with the requirements of the MPAM specification.

See section 10.5.2 Register details for more information on these registers.

When a PMCG that does not support MPAM is integrated in an MPAM-aware system, Arm recommends that the following mapping is used for PMCG MSIs:

- PARTID = 0
- PMG = 0
- If both the system and the PMCG support Secure state, then:
- -If the MSI targets Secure PA space, then Secure PARTID space is used.
- -If the MSI targets Non-secure PA space, then Non-secure PARTID space is used.
- Otherwise, Non-secure PARTID space is used.