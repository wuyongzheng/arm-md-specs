## 16.8 Summary of SMMU transactions and their PCIe and AMBA equivalents

Table 16.6: SMMU AMBA PCIe transactions

| Transaction type           | Transaction type                                                                        | AXI/ACE-Lite   | AXI/ACE-Lite                                                           | DTI                            | LTI Transaction type (LATRANS)   |
|----------------------------|-----------------------------------------------------------------------------------------|----------------|------------------------------------------------------------------------|--------------------------------|----------------------------------|
| SMMU                       | PCIe equivalent 1                                                                       | Signal         | Opcode                                                                 | DTI                            | LTI Transaction type (LATRANS)   |
| Ordinary read request      | Memory read request                                                                     | ARSNOOP        | ReadNoSnoop ReadOnce                                                   | DTI_TBU_TRANS_REQ.PERM == R    | R                                |
| RCI                        | Not applicable                                                                          | ARSNOOP        | ReadOnceCleanInvalid                                                   | DTI_TBU_TRANS_REQ.PERM == R    | R-CMO                            |
| DR                         | Not applicable                                                                          | ARSNOOP        | ReadOnceMakeInvalid                                                    | DTI_TBU_TRANS_REQ.PERM == R    | R-DCMO                           |
| Speculative transaction 2  | Not applicable                                                                          | Not applicable | Not applicable                                                         | Not applicable                 | Not applicable                   |
| Far Atomic operations      | FetchAdd, Swap, CAS                                                                     | AWATOP         | AtomicStore AtomicLoad AtomicSwap AtomicCompare                        | DTI_TBU_TRANS_REQ.PERM ==RW    | RW                               |
| Ordinary write transaction | Memory write request                                                                    | AWSNOOP        | WriteNoSnoop WriteUniquePtl WriteNoSnoopFull WriteUniqueFull WriteZero | DTI_TBU_TRANS_REQ. PERM ==W    | W                                |
| W-DCP                      | Memory write request with TLP Processing Hint - with a non-zero Steering Tag (ST) field | AWSNOOP        | WriteUniquePtlStash WriteUniqueFullStash                               | DTI_TBU_TRANS_REQ.PERM ==W     | W-DCP                            |
| NW-DCP                     | Zero-length Write request with TLP Processing Hint - with a non-zero ST field           | AWSNOOP        | StashOnceShared StashOnceUnique                                        | DTI_TBU_TRANS_REQ.PERM == SPEC | DCP                              |
| DH                         | Not applicable                                                                          | AWSNOOP        | InvalidateHint                                                         | DTI_TBU_TRANS_REQ.PERM == SPEC | DHCMO                            |

Continued on next page

Table 16.6 Continued from previous page

| Transaction type                         | Transaction type        | AXI/ACE-Lite     | AXI/ACE-Lite                                | DTI                                                          | LTI Transaction type (LATRANS)   |
|------------------------------------------|-------------------------|------------------|---------------------------------------------|--------------------------------------------------------------|----------------------------------|
| SMMU                                     | PCIe equivalent         | Signal           | Opcode                                      |                                                              |                                  |
| Clean CleanInvalidate CleanToPersistence | Not applicable          | ARSNOOP          | CleanShared CleanInvalid CleanSharedPersist | DTI_TBU_TRANS_REQ.PERM == R                                  | CMO                              |
| Invalidate                               | Not applicable          | ARSNOOP          | MakeInvalid                                 | DTI_TBU_TRANS_REQ.PERM == R                                  | DCMO                             |
| Ordinary translation request             | Not applicable          | Not applicable   | Not applicable                              | DTI_TBU_TRANS_REQ.PERM depends on the request type 4         | Not applicable                   |
| Ordinary speculative translation request | Not applicable          | Not applicable 3 | Not applicable                              | DTI_TBU_TRANS_REQ.PERM == SPEC                               | Not applicable 3                 |
| ATS Translation Request                  | ATS Translation Request | Not applicable   | Not applicable                              | DTI_ATS_TRANS_REQ.nW depends on the request type 4           | Not applicable                   |
| ATS PRI                                  | ATS PRI                 | Not applicable   | Not applicable                              | DTI_ATS_PAGE_REQ.{READ, WRITE} depends on the request type 4 | Not applicable                   |