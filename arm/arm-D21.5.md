## D21.5 Effect of the MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls on PE Secure state execution

RRFBMQ

The MPAM3\_EL3.{SDEFLT, FORCE\_NS} controls only affect Secure state execution.

RSHYXR

In MPAM v0p1 and from MPAMv1p1, if the Secure Default control MPAM3\_EL3.SDEFLT is implemented, the PARTID and PMG that Secure state execution produces depends on the value of that control:

| MPAM3_EL3.SDEFLT   | PARTID and PMG that Secure state execution produces                                 |
|--------------------|-------------------------------------------------------------------------------------|
| 0b0                | MPAMn_ELx.{PARTID_D, PMG_D} or {PARTID_I, PMG_I}. This is compatible with MPAMv1p0. |
| 0b1                | The Default PARTID and Default PMG.                                                 |

RXFCWV

In MPAMv0p1, the Force Non-secure PARTID space control MPAM3\_EL3.FORCE\_NS is implemented. If MPAM3\_EL3.SDEFLT is also implemented, the PARTID space, PARTID, and PMG that Secure state execution produces are as follows:

| MPAM3_EL3 control   | MPAM3_EL3 control   | PARTID space, PARTID, and PMG that Secure state execution produces                      |
|---------------------|---------------------|-----------------------------------------------------------------------------------------|
| SDEFLT              | FORCE_NS            |                                                                                         |
| 0b0                 | 0b0                 | • Secure physical PARTID space. • MPAMn_ELx.{PARTID_D, PMG_D} or {PARTID_I, PMG_I}.     |
|                     |                     | This is compatible with MPAMv1p0.                                                       |
|                     | 0b1                 | • Non-secure physical PARTID space. • MPAMn_ELx.{PARTID_D, PMG_D} or {PARTID_I, PMG_I}. |
| 0b1                 | 0b0                 | • Secure physical PARTID space. • Default PARTID and Default PMG.                       |
|                     | 0b1                 | • Non-secure physical PARTID space. • Default PARTID and Default PMG.                   |

RMSGKT

IQJPCV

RTRNQL

In MPAMv0p1, it is IMPLEMENTATION DEFINED whether MPAM3\_EL3.FORCE\_NS is implemented as:

- RAO/WI, and Secure PARTIDs are not implemented.
- RW.

In MPAMv0p1, software can discover whether MPAM3\_EL3.FORCE\_NS is implemented as RAO/WI or RW by testing whether it is writable to zero.

In MPAM for RME, implementation of MPAM3\_EL3.FORCE\_NS is not permitted and implementation of the alternative PARTID space controls, that select whether a primary or alternative PARTID space is produced, is required. The effect of MPAM3\_EL3.SDEFLT if it is implemented is:

| Alternative PARTID space selected?   | MPAM3_EL3.SDEFLT PARTID space, PARTID, and PMG that Secure state execution produces                                       |
|--------------------------------------|---------------------------------------------------------------------------------------------------------------------------|
| No                                   | 0b0 • Secure physical PARTID space. • MPAMn_ELx.{PARTID_D, PMG_D} or {PARTID_I, PMG_I}. This is compatible with MPAMv1p0. |
|                                      | 0b1 • Secure physical PARTID space. • Default PARTID and Default PMG.                                                     |
| Yes                                  | 0b0 • Non-secure physical PARTID space. • MPAMn_ELx.{PARTID_D, PMG_D} or {PARTID_I, PMG_I}.                               |

| Alternative PARTID space selected?   | MPAM3_EL3.SDEFLT PARTID space, PARTID, and PMG that Secure state execution produces   |
|--------------------------------------|---------------------------------------------------------------------------------------|
|                                      | 0b1 • Non-secure physical PARTID space. • Default PARTID and Default PMG.             |

## D21.5.1 Interaction of MPAM3\_EL3.SDEFLT and the MPAM enable control

RCBRSV

In MPAMv0p1 and from MPAMv1p1, if the Secure Default control MPAM3\_EL3.SDEFLT is implemented:

- When The MPAM enable control, MPAMEN, is 0, the MPAM PE Requester sends The Default physical PARTID and The Default PMG with all requests to the memory system.
- When MPAMEN is 1 and SDEFLT is 0, all requests from all Security states produce the PARTID and PMG from the MPAMn\_ELx registers.
- When MPAMEN is 1 and SDEFLT is 1:
- -All requests from Secure state produce the Default PARTID and the Default PMG.
- -All requests from all other Security states produce the PARTID and PMG from the MPAMn\_ELx registers.