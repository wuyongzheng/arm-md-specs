## 17.2 Assignment of PARTID and PMG for client transactions

When the system uses MPAM, the SMMU assigns the PARTID and PMG for all client transactions. There is no support for pass-through or modification of a PARTID or PMG that are provided with a request by a client device.

The determination of the PARTID and PMG for all client transactions follows this procedure:

1. If the corresponding programming interface is disabled, SMMU\_(*\_)CR0.SMMUEN == 0, the transaction bypasses and the MPAM attributes are given by the corresponding SMMU\_(S\_)GBPMPAM.GBP\_{PMG,PARTID} fields.
2. Otherwise, when translation is enabled by SMMU\_(*\_)CR0.SMMUEN == 1, the STE configures the MPAM attributes of the given stream.

When SMMU\_(*\_)CR0.SMMUEN == 1, the STE configures the MPAM behavior. The transaction PARTID and PMG are assigned as follows:

| STE.Config[2:0]                      | STE.S1MPAM   | Final transaction access                              |
|--------------------------------------|--------------|-------------------------------------------------------|
| 0b100 (Bypass)                       | X            | PARTID = STE.PARTID, PMG = STE.PMG.                   |
| 0b110 (Stage 2) (1)                  | X            | PARTID = STE.PARTID, PMG = STE.PMG.                   |
| 0b101 (stage 1)                      | 0            | PARTID = STE.PARTID, PMG = STE.PMG.                   |
| 0b101 (stage 1)                      | 1            | PARTID = CD.PARTID, PMG = CD.PMG.                     |
| 0b111 (Nested stage 1 + stage 2) (2) | 0            | PARTID = STE.PARTID, PMG = STE.PMG.                   |
| 0b111 (Nested stage 1 + stage 2) (2) | 1            | PARTID = STE.VMS.PARTID_MAP[CD.PARTID], PMG = CD.PMG. |

In nested configurations that enable stage 1 control of MPAM with STE.S1MPAM == 1, the CD.PARTID[4:0] value is a virtual PARTID and is translated to a physical PARTID using the VMS.PARTID\_MAP structure located through the stream's STE.VMSPtr field. See section 5.6 Virtual Machine Structure for information on the VMS. The VMS.PARTID\_MAP is not used when translation configuration is stage 1-only or stage 2-only, or when STE.S1MPAM == 0, because the PARTID in use is a physical ID in these configurations.

Note: STE.S1MPAM provides backward compatibility for software that is unaware of MPAM, allowing it to operate without requiring a VMS to be allocated.

In an SMMU with RME, the MPAM PARTID and PMG values used for NoStreamID accesses is an IMPLEMENTATION DEFINED choice between:

- Values provided by the device.
- Zero.