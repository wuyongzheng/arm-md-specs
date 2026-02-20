## G2.5 Summary of permitted routing and enabling of debug exceptions

Behavior is as follows:

## Breakpoint Instruction exceptions

These are always enabled, regardless of the current Privilege level and Security state. Table G2-7 shows the routing of these. In the table, n/a means not applicable.

Table G2-7 Routing of Breakpoint Instruction exceptions

| Current Security state   | HDCR.TDE a :   | Target when enabled from:   | Target when enabled from:   |          |
|--------------------------|----------------|-----------------------------|-----------------------------|----------|
|                          |                | PL0                         | PL1                         | PL2      |
| Secure                   | X              | Secure Abort mode b         | Secure Abort mode b         | n/a      |
| Non-secure               | 0              | Non-secure Abort mode       | Non-secure Abort mode       | Hyp mode |
|                          | 1              | Hyp mode                    | Hyp mode                    | Hyp mode |

b. If EL3 is implemented and is using AArch32, Secure Abort mode is at EL3. Otherwise, Secure Abort mode is at EL1.

## All other debug exceptions

The enabling and permitted routing is controlled by all of the following:

- SDCR.SPD.
- SDER.SUIDEN.
- HDCR.TDE.
- The IMPLEMENTATION DEFINED authentication interface.

Table G2-8 shows the valid combinations of the values of SDCR.SPD, SDER.SUIDEN, HDCR.TDE, and, in the Auth column, the input from the IMPLEMENTATION DEFINED authentication interface described by the pseudocode function

AArch32.SelfHostedSecurePrivilegedInvasiveDebugEnabled() . For each combination, the table shows where debug exceptions are enabled from and where they are taken to.

In the table, n/a means not applicable and a dash, -, means that debug exceptions are disabled from that Exception level.

Table G2-8 Breakpoint, Watchpoint, and Vector Catch exceptions

| Debug state   | Lock a   | Current Security state   | SPD b   | Auth c   | SUIDEN b   | TDE d   | Target AArch32 mode when enabled from:   | Target AArch32 mode when enabled from:   | Target AArch32 mode when enabled from:   |
|---------------|----------|--------------------------|---------|----------|------------|---------|------------------------------------------|------------------------------------------|------------------------------------------|
| Debug state   | Lock a   | Current Security state   | SPD b   | Auth c   | SUIDEN b   | TDE d   | PL0                                      | PL1                                      | PL2                                      |
| Yes           | X        | X                        | 0bXX    | X        | X          | X       | -                                        | -                                        | -                                        |
| No            | TRUE     | X                        | 0bXX    | X        | X          | X       | -                                        | -                                        | -                                        |
| No            | FALSE    | Secure                   | 0b00    | FALSE    | 0          | X       | -                                        | -                                        | n/a                                      |
| No            | FALSE    | Secure                   | 0b00    | FALSE    | 1          | X       | Secure Abort mode e                      | -                                        | n/a                                      |
| No            | FALSE    | Secure                   | 0b00    | TRUE     | X          | X       | Secure Abort mode e                      | Secure Abort mode e                      | n/a                                      |

| Debug state   | Lock a   | Current Security state   | SPD b   | Auth c   | SUIDEN b   | TDE d   | Target AArch32 mode when enabled from:   | Target AArch32 mode when enabled from:   | Target AArch32 mode when enabled from:   |
|---------------|----------|--------------------------|---------|----------|------------|---------|------------------------------------------|------------------------------------------|------------------------------------------|
| Debug state   | Lock a   | Current Security state   | SPD b   | Auth c   | SUIDEN b   | TDE d   | PL0                                      | PL1                                      | PL2                                      |
| No            | FALSE    | Secure                   | 0b10    | X        | 0          | X       | -                                        | -                                        | n/a                                      |
| No            | FALSE    | Secure                   | 0b10    | X        | 1          | X       | Secure Abort mode e                      | -                                        | n/a                                      |
| No            | FALSE    | Secure                   | 0b11    | X        | X          | X       | Secure Abort mode e                      | Secure Abort mode e                      | n/a                                      |
| No            | FALSE    | Non-secure               | 0bXX    | X        | X          | 0       | Non-secure Abort mode                    | Non-secure Abort mode                    | -                                        |
| No            | FALSE    | Non-secure               | 0bXX    | X        | X          | 1       | Hyp mode                                 | Hyp mode                                 | -                                        |