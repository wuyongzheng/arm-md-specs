## 4.8 Command Consumption summary

| Command Type                                        | Consumption means                                                                       |
|-----------------------------------------------------|-----------------------------------------------------------------------------------------|
| TLB and ATS Invalidation commands                   | Nothing                                                                                 |
| Configuration invalidation commands CMD_CFGI_*      | Nothing                                                                                 |
| Prefetch commands CMD_PREFETCH_*                    | Nothing                                                                                 |
| PRI responses CMD_PRI_RESP                          | Nothing                                                                                 |
| Stall resume/termination CMD_RESUME, CMD_STALL_TERM | CMD_RESUME and CMD_STALL_TERM have individual completion guarantees that have been met. |
| Synchronization commands CMD_SYNC                   | The completion guarantees of CMD_SYNC have been met.                                    |