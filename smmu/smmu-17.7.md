## 17.7 Determination of PARTID space values

MPAM PARTID and PMG values are qualified with a PARTID space.

In systems without support for RME, PARTID space is determined by the memory system attribute MPAM\_NS.

In systems with support for RME, PARTID space is determined by the memory system attribute MPAM\_SP.

For the purposes of assigning MPAM attributes, an SMMU with the Realm programming interface and support for MPAM is a four-space MPAM component.

The encodings of MPAM\_NS and MPAM\_SP in the memory system are as follows:

| RME supported   | Identifier   | Encoding                                                                                                     |
|-----------------|--------------|--------------------------------------------------------------------------------------------------------------|
| No              | MPAM_NS      | 0: Secure PARTID space 1: Non-secure PARTID space                                                            |
| Yes             | MPAM_SP      | 0b00 : Secure PARTID space 0b01 : Non-secure PARTID space 0b10 : Root PARTID space 0b11 : Realm PARTID space |

Note: Some SMMU register and configuration structure fields have the name MPAM\_NS. These fields determine the target PARTID space of the accesses they govern, regardless of whether the memory system uses MPAM\_NS or MPAM\_SP.

All SMMU-originated and client-originated transactions for Non-secure state are issued with Non-secure PARTID space.

If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 0, all SMMU-originated and client-originated transactions for Secure state are issued with Secure PARTID space.

If SMMU\_S\_MPAMIDR.HAS\_MPAM\_NS == 1, some transactions for Secure state might be issued with Non-secure PARTID space, according to the rules in this section.

If SMMU\_R\_MPAMIDR.HAS\_MPAM\_NS == 1, some accesses for Realm state use Non-secure PARTID space, according to the configuration of SMMU\_R\_GMPAM.MPAM\_NS or STE.MPAM\_NS as appropriate.

For MPAM PARTID and PMG register and structure fields that control MPAM for the Secure programming interface, the associated MPAM\_NS field determines whether accesses are issued with Secure PARTID space or Non-secure PARTID space.

PARTID and PMG values for accesses for Secure state are determined from the register and structure fields specified in section 17.2 Assignment of PARTID and PMG for client transactions and section 17.4 Assignment of PARTID and PMG for SMMU-originated transactions . Only the selection of PARTID space and the determination of maximum PARTID and PMG values are affected by this feature.

The full list of MPAM\_NS bits for Secure state, which each describe the Secure accesses they apply to are:

- SMMU\_S\_GBPMPAM.MPAM\_NS
- SMMU\_S\_GMPAM.MPAM\_NS
- STE.MPAM\_NS
- SMMU\_PMCG\_SCR.MSI\_MPAM\_NS

Note: There is no MPAM\_NS bit in CD or VMS. They inherit the choice of PARTID space from the STE that led to them.

In systems that support RME, the MPAM\_NS or MPAM\_SP values used for NoStreamID accesses, and GPT walks caused by NoStreamID accesses, are independently an IMPLEMENTATION DEFINED choice between:

- The value provided by the device. This option must be used if the PARTID and PMG values used are the values provided by the device.
- The MPAM\_NS or MPAM\_SP value corresponding to the target PA space of the NoStreamID access.

For an SMMU that does not support MPAM\_SP, then it is permitted to map MPAM\_SP to MPAM\_NS as follows:

- NoStreamID accesses to Root PA space use the Secure MPAM\_NS value of 0.
- NoStreamID accesses to Realm PA space use the Non-secure MPAM\_NS value of 1.

Any IMPLEMENTATION DEFINED determination of MPAM attributes must comply with the requirements of the MPAM architecture [3].