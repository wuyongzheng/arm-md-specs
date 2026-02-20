## G2.2 Routing debug exceptions

Debug exceptions are usually routed to Abort mode. However, if EL2 is implemented, the routing of debug exceptions depends on the Effective values of HDCR.TDE and HCR.TGE:

If the Effective value of {HDCR.TDE, HCR.TGE} is not {0, 0}

Debug exceptions taken from Non-secure state are routed to Hyp mode.

If EL2 is using AArch64 and FEAT\_SEL2 is implemented, debug exceptions taken from Secure EL0 and Secure EL1 may be routed to Secure EL2. For more information, see Routing debug exceptions.

In Non-secure state debug exceptions behave as follows:

- Debug exceptions taken from Non-secure EL1 and Non-secure EL0 are routed to Non-secure Abort mode.
- Breakpoint Instruction exceptions taken from Hyp mode are routed to Hyp mode.
- All other debug exceptions are disabled from Hyp mode.

## Otherwise

Note

If EL2 is not implemented, the Effective value of HCR.TGE is 0 and the Effective value of HDCR.TDE is 0.

Table G2-2, Table G2-3, and Table G2-4 show the routing of debug exceptions taken from an Exception level that is using AArch32 to an Exception level that is using AArch32. In these tables:

TDE

Means the logical OR of HDCR.TDE and HCR.TGE.

(Hyp mode) Means:

- All debug exceptions other than Breakpoint Instruction exceptions are disabled from this Privilege level.
- Breakpoint Instruction exceptions taken from this Privilege level are taken to Hyp mode.

Table G2-2 Routing when both EL3 and EL2 are implemented

| TDE   | Target AArch32 mode when executing in:   | Target AArch32 mode when executing in:   | Target AArch32 mode when executing in:   | Secure state      |
|-------|------------------------------------------|------------------------------------------|------------------------------------------|-------------------|
|       | PL0                                      | PL1                                      | PL2                                      |                   |
| 0     | Non-secure Abort mode                    | Non-secure Abort mode                    | (Hyp mode)                               | Secure Abort mode |
| 1     | Hyp mode                                 | Hyp mode                                 | (Hyp mode)                               | Secure Abort mode |

Table G2-3 Routing when EL3 is implemented and EL2 is not implemented

| Target AArch32 mode when executing in:   | Target AArch32 mode when executing in:   |
|------------------------------------------|------------------------------------------|
| Non-secure state                         | Secure state                             |
| Non-secure Abort mode                    | Secure Abort mode                        |

| TDE   | Target AArch32 mode when executing in Non-secure:   | Target AArch32 mode when executing in Non-secure:   |            |
|-------|-----------------------------------------------------|-----------------------------------------------------|------------|
|       | PL0                                                 | PL1                                                 | PL2        |
| 0     | Non-secure Abort mode                               | Non-secure Abort mode                               | (Hyp mode) |
| 1     | Hyp mode                                            | Hyp mode                                            | (Hyp mode) |

## G2.2.1 Pseudocode description of routing debug exceptions

DebugTarget() returns the current debug target Exception level. DebugTargetFrom() returns the debug target Exception level for the specified Security state.