## D8.12 Memory Encryption Contexts extension

IYTBSD

The Memory Encryption Contexts extension (MEC extension) introduces memory encryption contexts (MECs) to all physical address (PA) spaces. Multiple memory encryption contexts are provided to the Realm physical address space for assignment to Realm virtual machines, with policy controlled by Realm EL2. The Root, Secure and Non-Secure physical address spaces each have one context.

RLFYSJ

All statements in this section and subsections require implementation of FEAT\_MEC.

## D8.12.1 Effect of MEC on PA spaces

| R GKRVJ   | PAs in the Root PA space are associated with the default MECID of zero.                                                                                                                                                             |
|-----------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R YJVST   | PAs in the Secure PA space are associated with the default MECID of zero.                                                                                                                                                           |
| R MRKMQ   | PAs in the Non-secure PA space are associated with the default MECID of zero.                                                                                                                                                       |
| R WGBXM   | Root, Secure and Non-Secure PA spaces do not support multiple encryption contexts.                                                                                                                                                  |
|           | D8.12.1.1 Effect on the EL3 translation regime                                                                                                                                                                                      |
| I HHCPS   | If FEAT_MEC is implemented, then FEAT_RME is also implemented and therefore execution in EL3 uses the Root Security state.                                                                                                          |
| R FMLTL   | For EL3 stage 1 translated addresses, if SCTLR2_EL3.EMEC is 0, then accesses to the Realm PA space use the default MECID of zero.                                                                                                   |
| R CCSND   | For EL3 stage 1 translated addresses, if SCTLR2_EL3.EMEC is 1, then accesses to the Realm PA space use the Realm PA space Alternate MECID for EL3, configured in MECID_RL_A_EL3.                                                    |
| R LPNPC   | MECID_RL_A_EL3 is not permitted to be cached in a TLB.                                                                                                                                                                              |
| I TZYKP   | EL3 software can only access the Realm PA space using translated addresses. The {NSE, NS} fields within the Block or Page descriptors must equal {1, 1} to access the Realm PA space.                                               |
|           | D8.12.1.2 Effect on the Realm EL2 and Realm EL2&0 translation regimes                                                                                                                                                               |
| R CBJVF   | If SCTLR2_EL2.EMEC is 0, then Realm EL2 and EL2&0 accesses to Realm PA space use the default MECID of zero.                                                                                                                         |
| R FCSBF   | If SCTLR_EL2.M is 0 and SCTLR2_EL2.EMEC is 1, then Realm EL2 and EL2&0 accesses to Realm PA space use the EL2&0 Primary 0 MECID, configured in MECID_P0_EL2.                                                                        |
| R RXMFG   | For Realm EL2 stage 1 translations, if SCTLR_EL2.M is 1, SCTLR2_EL2.EMEC is 1, and the Effective value of HCR_EL2.E2H is 0, then all lookup levels use the EL2&0 Primary 0 MECID, configured in MECID_P0_EL2.                       |
| R XBDTH   | For Realm EL2&0 stage 1 TTBR0 and TTBR1 translations, if SCTLR_EL2.M is 1, SCTLR2_EL2.EMEC is 1, and the Effective value of HCR_EL2.E2H is 1, then all lookup levels use the MECID determined by the value of the TCR_EL2.A1 field. |

|   TCR_EL2.A1 | Translation lookup MECID   |
|--------------|----------------------------|
|            0 | MECID_P1_EL2               |
|            1 | MECID_P0_EL2               |

ITSRTP

TCR\_EL2.A1 is not permitted to be cached in a TLB, and MECID values are not permitted to be cached in a TLB. However, the choice of which MECID register is used for translation table walks is permitted to be cached in a TLB, as long as it is only cached in TLB entries that are associated with the ASID that is also selected by the A1 field.

RLZGSD

For Realm EL2 and EL2&amp;0 stage 1 TTBR0 translated addresses to Realm PA space, if SCTLR\_EL2.M is 1, SCTLR2\_EL2.EMEC is 1, and TCR2\_EL2.AMEC0 is 0, then the translation validity and MECID selection is determined by the AMEC field in the Block or Page descriptor used for that translation.

|   TTD.AMEC | Translation validity   | Output MECID   |
|------------|------------------------|----------------|
|          0 | Valid                  | MECID_P0_EL2   |
|          1 | Translation fault      | N/A            |

RVWKVQ

For Realm EL2&amp;0 stage 1 TTBR1 translated addresses to Realm PA space, if SCTLR\_EL2.M is 1, SCTLR2\_EL2.EMEC is 1, TCR2\_EL2.AMEC1 is 0, and the Effective value of HCR\_EL2.E2H is 1, then the translation validity and MECID selection is determined by the AMEC field in the Block or Page descriptor used for that translation.

|   TTD.AMEC | Translation validity   | Output MECID   |
|------------|------------------------|----------------|
|          0 | Valid                  | MECID_P1_EL2   |
|          1 | Translation fault      | N/A            |

IPDRGM

Changing the state of either TCR2\_EL2.AMEC0 or TCR2\_EL2.AMEC1 from 1 to 0 requires TLB maintenance operations for the update to be visible.

RTHGCP

For Realm EL2 and EL2&amp;0 stage 1 TTBR0 translated addresses to Realm PA space, if SCTLR\_EL2.M is 1, SCTLR2\_EL2.EMEC is 1, and TCR2\_EL2.AMEC0 is 1, then MECID selection is determined by the AMEC field in the Block or Page descriptor used for that translation.

|   TTD.AMEC | Output MECID   |
|------------|----------------|
|          0 | MECID_P0_EL2   |
|          1 | MECID_A0_EL2   |

RMQHXQ

For Realm EL2&amp;0 stage 1 TTBR1 translated addresses to Realm PA space, if SCTLR\_EL2.M is 1, SCTLR2\_EL2.EMEC is 1, TCR2\_EL2.AMEC1 is 1, and the Effective value of HCR\_EL2.E2H is 1, then MECID selection is determined by the AMEC field in the Block or Page descriptor used for that translation.

|   TTD.AMEC | Output MECID   |
|------------|----------------|
|          0 | MECID_P1_EL2   |
|          1 | MECID_A1_EL2   |

RXVLMT

If NS is 1 in a Realm EL2 and EL2&amp;0 stage 1 Block or Page descriptor, then the AMEC field is RES0 and does not affect MECID selection.

RVKDBG

MECID\_P0\_EL2, MECID\_P1\_EL2, MECID\_A0\_EL2, and MECID\_A1\_EL2 are not permitted to be cached in a TLB.

## D8.12.1.3 Effect on the Realm EL1&amp;0 translation regime

RHDGTR

If SCTLR2\_EL2.EMEC is 0, then Realm EL1&amp;0 accesses to Realm PA space use the default MECID of zero.

RYSNHS

If SCTLR2\_EL2.EMEC is 1 and HCR\_EL2.VM is 0, then Realm EL1&amp;0 accesses to Realm PA space use the EL1&amp;0 Primary MECID, configured in VMECID\_P\_EL2.

| R FQFXK   | For Realm EL1&0 stage 1 translations, if SCTLR2_EL2.EMEC is 1, HCR_EL2.VM is 0, and SCTLR_EL1.M is 1, then all lookup levels use the EL1&0 Primary MECID, configured in VMECID_P_EL2.                                       |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R PDCWV   | For Realm EL1&0 stage 2 translations, if SCTLR2_EL2.EMEC is 1 and HCR_EL2.VM is 1, then all lookup levels use the EL1&0 Primary MECID, configured in VMECID_P_EL2.                                                          |
| R XMTZH   | For Realm EL1&0 stage 2 translated addresses to Realm PA space, if SCTLR2_EL2.EMEC is 1 and HCR_EL2.VM is 1, then MECID selection is determined by the AMECfield in the Block or Page descriptor used for that translation. |

|   TTD.AMEC | Output MECID   |
|------------|----------------|
|          0 | VMECID_P_EL2   |
|          1 | VMECID_A_EL2   |

RDQZTR

If NS is 1 within a Realm EL1&amp;0 stage 2 Block or Page descriptor, then the AMEC field is RES0 and does not affect MECID selection.

RJQSMC

VMECID\_P\_EL2 and VMECID\_A\_EL2 are not permitted to be cached in a TLB.