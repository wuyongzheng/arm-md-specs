## 13.8 Attributes for SMMU-originated accesses

This table provides a summary of memory attributes used for SMMU-originated accesses. This table is an informative summary of the fields used to determine the memory attributes and the normative requirements are captured in the register and structure fields referenced.

| Access       | Attributes determined by                                                                                                                         |
|--------------|--------------------------------------------------------------------------------------------------------------------------------------------------|
| STE fetch    | SMMU_(*_)CR1.{TABLE_IC, TABLE_OC, TABLE_SH}                                                                                                      |
| VMS fetch    | SMMU_(*_)CR1.{TABLE_IC, TABLE_OC, TABLE_SH}                                                                                                      |
| CD fetch     | STE.{S1CIR, S1COR, S1CSH}, combined with stage 2 attributes if stage 2 translation is enabled, including the effects of STE.S2FWB and STE.S2PTW. |
| Stage 1 walk | CD.{IRx, ORx, SHx}, combined with stage 2 attributes if stage 2 translation is enabled, including the effects of STE.S2FWB and STE.S2PTW.        |
| Stage 2 walk | STE.{S2IR0, S2OR0, S2SH0}                                                                                                                        |
| GPT walk     | SMMU_ROOT_GPT_BASE_CFG.{IRGN, ORGN, SH}                                                                                                          |
| DPT walk     | SMMU_(R_)CR1.{TABLE_IC, TABLE_OC, TABLE_SH}                                                                                                      |
| GERROR MSI   | SMMU_(*_)GERROR_IRQ_CFG2.{MemAttr, SH}                                                                                                           |
| EVENTQ MSI   | SMMU_(*_)EVENTQ_IRQ_CFG2.{MemAttr, SH}                                                                                                           |
| PRIQ MSI     | SMMU_PRIQ_IRQ_CFG2.{MemAttr, SH}                                                                                                                 |
| CMDQ MSI     | CMD_SYNC.{MSIAttr, MSH}                                                                                                                          |
| CMDQ fetch   | SMMU_(*_)CR1.{QUEUE_IC, QUEUE_OC, QUEUE_SH} and SMMU_(*_)CMDQ_BASE.RA                                                                            |
| PRIQ write   | SMMU_(R_)CR1.{QUEUE_IC, QUEUE_OC, QUEUE_SH} and SMMU_(R_)PRIQ_BASE.WA                                                                            |
| EVENTQ write | SMMU_(*_)CR1.{QUEUE_IC, QUEUE_OC, QUEUE_SH} and SMMU_(*_)EVENTQ_BASE.WA                                                                          |