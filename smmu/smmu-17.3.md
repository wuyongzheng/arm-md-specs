## 17.3 PCIe ATS transactions

An ATS Translation Request causes configuration and translation table access using PARTID/PMG values the same as for an equivalent Untranslated transaction on that StreamID and SubstreamID.

The PARTID and PMG assigned to an ATS Translated transaction are as follows:

| SMMU_(R_)CR0.ATSCHK   | Configuration     | PARTID andPMG                                                                                                                |
|-----------------------|-------------------|------------------------------------------------------------------------------------------------------------------------------|
| 0 (Non-secure only)   | Any               | SMMU_GBPMPAM.GBP_{PARTID, PMG}                                                                                               |
| 1                     | Stage 1 only      | If UseS1MPAM == 0: PARTID = STE.PARTID PMG=STE.PMG If UseS1MPAM == 1 1 : PARTID = CD.PARTID PMG = CD.PMG                     |
| 1                     | Stage 1 + stage 2 | If UseS1MPAM == 0: PARTID = STE.PARTID PMG=STE.PMG If UseS1MPAM == 1 1 : PARTID = STE.VMS.PARTID_MAP[CD.PARTID] PMG = CD.PMG |
| 1                     | Stage 2 only      | PARTID = STE.PARTID PMG = STE.PMG                                                                                            |
| 1                     | Split Stage ATS   | If UseS1MPAM == 0: PARTID = STE.PARTID PMG=STE.PMG If UseS1MPAM == 1 1 : PARTID = STE.VMS.PARTID_MAP[CD.PARTID] PMG = CD.PMG |

- SMMU\_IDR3.PASIDTT == 1.
- SMMU\_IDR3.PASIDTT == 0 and the implementation uses PASID to determine MPAM attributes when a PASID is presented. The set of endpoints for which this behavior occurs is IMPLEMENTATION DEFINED.

Otherwise it is 0.

Note: When SMMU\_(R\_)CR0.ATSCHK == 1, the STE is fetched to verify whether Translated transactions are permitted. The STE.{PARTID, PMG} fields are therefore available for these transactions. The CD information is only available for an ATS Translated transaction when SMMU\_IDR3.PASIDTT is 1 and a PASID is provided.

Note: When translation is enabled for the Non-secure SMMU programming interface, that is SMMU\_CR0.SMMUEN == 1, the SMMU\_GBPMPAM.GBP\_{PARTID, PMG} configuration is not used for ordinary transactions because they are assigned PARTID and PMG using the STE fields. This configuration is used for ATS Translated transactions when SMMU\_CR0.ATSCHK == 0.

When SMMU\_(R\_)CR0.ATSCHK == 1, if a PASID is provided with a Translated transaction from an endpoint and SMMU\_IDR3.PASIDTT is 0, an implementation is permitted but not required to use the PASID to determine a PARTID or PMG from a CD as described for configurations with UseS1MPAM == 1, in the table above.

Note: Before PCIe 5.0, endpoints using the PCIe interconnect do not provide a PASID with Translated transactions. However, embedded endpoints that support ATS and PASIDs might be integrated in a way that provides a PASID with Translated transactions.