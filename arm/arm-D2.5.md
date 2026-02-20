## D2.5 Summary of the routing and enabling of debug exceptions

Behavior is as follows:

## Breakpoint Instruction exceptions

These are always enabled, regardless of the current Exception level and Security state. A Breakpoint Instruction exception taken from EL3 is always routed to EL3. A Breakpoint Instruction exception taken from EL2 is routed to EL2. A Breakpoint Instruction exception taken from EL0 or EL1 is always routed to ELD.

## All other debug exceptions

Table D2-6 shows the valid combinations of MDCR\_EL3.SDD, MDCR\_EL2.TDE, MDSCR\_EL1.KDE, and PSTATE.D, and for each combination shows where these exceptions are enabled from and where they are taken to. The table does not include the case when executing at EL1, ELD is EL2, and FEAT\_NV2 is implemented that is described in Enabling debug exceptions from the current Exception level and Security state.

## In the table:

Lock

Means the value of (OSLSR\_EL1.OSLK == '1' || DoubleLockStatus() ).

NSE

Means the Effective value of SCR\_EL3.NSE. If FEAT\_RME is not implemented, this is 0.

NS

Means the Effective value of SCR\_EL3.NS. If Secure state is not implemented, this is 1.

SDD

Means the Effective value of MDCR\_EL3.SDD. See Disabling debug exceptions from Secure state.

EEL2

Means the Effective value of SCR\_EL3.EEL2. If FEAT\_SEL2 is not implemented, this is 0.

TGE

Means the Effective value of HCR\_EL2.TGE. If EL2 is not implemented, the PE behaves as if this is 0.

TDE

Means the Effective value of MDCR\_EL2.TDE. If EL2 is not implemented, the PE behaves as if this is 0.

KDE

Means the value of MDSCR\_EL1.KDE.

D

Means the value of PSTATE.D.

n/a

Means not applicable. The PE cannot be executing at this Exception level.

-

Means that debug exceptions are disabled from that Exception level.

## Table D2-6 Routing of Breakpoint, Watchpoint, Software Step, and Vector Catch exceptions

| Debug state   | Lock   | NSE   | NS   | SDD   | EEL2   | TGE   | TDE   | KDE   | D   | EL D when enabled from:   | EL D when enabled from:   | EL D when enabled from:   | EL D when enabled from:   |
|---------------|--------|-------|------|-------|--------|-------|-------|-------|-----|---------------------------|---------------------------|---------------------------|---------------------------|
|               |        |       |      |       |        |       |       |       |     | EL0                       | EL1                       | EL2                       | EL3                       |
| Yes           | X      | X     | X    | X     | X      | X     | X     | X     | X   | -                         | -                         | -                         | -                         |
| No            | TRUE   | X     | X    | X     | X      | X     | X     | X     | X   | -                         | -                         | -                         | -                         |
|               | FALSE  | 0     | 0    | 1     | X      | X     | X     | X     | X   | -                         | -                         | -                         | -                         |
|               |        |       |      | 0     | 0      | X     | X     | 0     | X   | EL1                       | -                         | n/a                       | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL1                       | EL1                       | n/a                       | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL1                       | -                         | n/a                       | -                         |

| Debug state   | Lock   | NSE   | NS   | SDD   | EEL2   | TGE   | TDE   | KDE   | D   | EL D when enabled from:   | EL D when enabled from:   | EL D when enabled from:   | EL D when enabled from:   |
|---------------|--------|-------|------|-------|--------|-------|-------|-------|-----|---------------------------|---------------------------|---------------------------|---------------------------|
| Debug state   | Lock   | NSE   | NS   | SDD   | EEL2   | TGE   | TDE   | KDE   | D   | EL0                       | EL1                       | EL2                       | EL3                       |
|               |        |       |      |       | 1      | 0     | 0     | 0     | X   | EL1                       | -                         | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL1                       | EL1                       | -                         | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL1                       | -                         | -                         | -                         |
| No            | FALSE  | 0     | 0    | 0     | 1      | 0     | 1     | 0     | X   | EL2                       | EL2                       | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL2                       | EL2                       | EL2                       | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL2                       | EL2                       | -                         | -                         |
|               |        |       |      |       |        | 1     | X     | 0     | X   | EL2                       | n/a                       | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL2                       | n/a                       | EL2                       | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL2                       | n/a                       | -                         | -                         |
|               |        | X     | 1    | X     | X      | 0     | 0     | 0     | X   | EL1                       | -                         | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL1                       | EL1                       | -                         | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL1                       | -                         | -                         | -                         |
|               |        |       |      |       |        |       | 1     | 0     | X   | EL2                       | EL2                       | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL2                       | EL2                       | EL2                       | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL2                       | EL2                       | -                         | -                         |
|               |        |       |      |       |        | 1     | X     | 0     | X   | EL2                       | n/a                       | -                         | -                         |
|               |        |       |      |       |        |       |       | 1     | 0   | EL2                       | n/a                       | EL2                       | -                         |
|               |        |       |      |       |        |       |       |       | 1   | EL2                       | n/a                       | -                         | -                         |