## D11.8 Guarded Control Stack exceptions

| D WWXWR   | FEAT_GCS provides the GCS Data Check exception to report data mismatches in the comparison operations related to the Guarded Control Stack.                              |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I QXRVB   | For the comparison operations related to the Guarded Control Stack, seeR PCQXX ,R LWRMC , andR QHSGP .                                                                   |
| D PRYMV   | FEAT_GCS provides the EXLOCKException to report any exceptions due to an incompatible value in PSTATE.EXLOCK.                                                            |
| I RVKKZ   | For a GCS Data Check exception, an EXLOCKException, a trap on a GCSSTR instruction, or a trap on a GCSSTTR instruction, the syndrome information is captured in ESR_ELx. |
| I WLNVC   | PMUevents EXC_DABORT and EXC_TRAP_DABORT count occurrences of a GCS Data Check exception.                                                                                |
| I PHRFN   | Traps on the GCSSTR and GCSSTTR instructions are counted by the EXC_UNDEF and EXC_TRAP_OTHERPMU events.                                                                  |
| I YLMVR   | An EXLOCKException is counted by the EXC_UNDEF and EXC_TRAP_OTHER PMUevents, according to the existing definitions of those PMUevents.                                   |
| I MKLKV   | For more information on tracing GCS exceptions, see: • R LYGJZ .                                                                                                         |

- RGZQKS.