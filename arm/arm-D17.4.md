## D17.4 Enabling profiling

RTWFRY

RWXXFL

IBRTKK

ISBQVZ

If and only if any of the following are true, then profiling is stopped :

- PMBSR\_EL1.S is 1.
- FEAT\_SPE\_EXC is implemented and all of the following are true:
- -EL2 is implemented and any of the following applies:
- -The Effective value of SCR\_EL3.NS is 1.
- -The Effective value of SCR\_EL3.{NS, EEL2} is {0, 1}.
- -EL3 is not implemented or MDCR\_EL3.PMSEE is not 0b00 .
- -PMSCR\_EL2.EE is either 0b10 or 0b11 .
- -PMBSR\_EL2.S is 1.

FEAT\_SPE\_EXC is implemented and all of the following are true:

- -EL3 is implemented.
- -MDCR\_EL3.PMSEE is either 0b10 or 0b11 .
- -PMBSR\_EL3.S is 1

The pseudocode function SPEProfilingStopped() shows this.

When all of the following are true, profiling is enabled :

- The PE is in AArch64 state.
- PMBLIMITR\_EL1.E is 1. The Profiling Buffer is enabled .
- Profiling is not stopped.
- The PE is executing at either the Profiling Buffer owning Exception level or any lower Exception level.
- Either the Profiling Buffer owning Exception level is EL2 or the Effective value of HCR\_EL2.TGE is 0.
- The PE is executing in the Profiling Buffer owning Security state.
- The PE is in Non-debug state.
- PMSCR\_EL1.{E1SPE, E0SPE} and PMSCR\_EL2.{E2SPE, E0HSPE} enable profiling at the current Exception level.

Otherwise, profiling is disabled .

The pseudocode functions ProfilingBufferEnabled() and StatisticalProfilingEnabled() show this.

When the Profiling Buffer is disabled or profiling is stopped:

- Any sample records that have been collected but not written to memory are discarded.
- PMBPTR\_EL1 and PMSICR\_EL1 are not updated by the SPU.

Note

The owning Security state is controlled by MDCR\_EL3.{NSPBE, NSPB} and the owning Exception level is controlled by MDCR\_EL2.E2PB. See The owning translation regime.

If the Profiling Buffer is enabled and the PE is in Non-debug state and using AArch64 state, Table D17-1 defines the valid combinations of the following that define when profiling is enabled:

- The Effective value of SCR\_EL3.NSE. · The Effective value of SCR\_EL3.NS. · The Effective value of SCR\_EL3.EEL2. · The Effective value of MDCR\_EL3.NSPBE. · The Effective value of MDCR\_EL3.NSPB. · The Effective value of MDCR\_EL2.E2PB. · The Effective value of HCR\_EL2.TGE. In Table D17-1: D Disabled. E2SPE Enabled if PMSCR\_EL2.E2SPE == 1, disabled otherwise. E1SPE Enabled if PMSCR\_EL1.E1SPE == 1, disabled otherwise. E0HSPE Enabled if PMSCR\_EL2.E0HSPE == 1, disabled otherwise. E0SPE Enabled if PMSCR\_EL1.E0SPE == 1, disabled otherwise.
- •

IJHPHD

Table D17-1 Enabling by Exception level and Security state (for all Exception levels)

| Controls   |    |       |      |      |      |     | Profiling enabled at   | Profiling enabled at   | Profiling enabled at   | Profiling enabled at   |
|------------|----|-------|------|------|------|-----|------------------------|------------------------|------------------------|------------------------|
| NSE        | NS | NSPBE | NSPB | E2PB | EEL2 | TGE | EL3                    | EL2                    | EL1                    | EL0                    |
| 0          | 1  | 1     | 0b0x | x    | x    | x   | D                      | D                      | D                      | D                      |
| 0          |    | 0     | 0b1x | 0b1x | x    | 0   | D                      | D                      | E1SPE                  | E0SPE                  |
| 0          |    |       |      | 0b1x | x    | 1   | D                      | D                      | n/a                    | D                      |
| 0          |    |       |      | 0b00 | x    | 0   | D                      | E2SPE                  | E1SPE                  | E0SPE                  |
| 0          |    |       |      | 0b00 | x    | 1   | D                      | E2SPE                  | n/a                    | E0HSPE                 |
| 0          | 0  | 0     | 0b1x | x    | x    | x   | D                      | D                      | D                      | D                      |
| 0          |    |       | 0b0x | x    | 0    | x   | D                      | n/a                    | E1SPE                  | E0SPE                  |
| 0          |    |       |      | 0b1x | 1    | 0   | D                      | D                      | E1SPE                  | E0SPE                  |
| 0          |    |       |      | 0b1x | 1    | 1   | D                      | D                      | n/a                    | D                      |
| 0          |    |       |      | 0b00 | 1    | 0   | D                      | E2SPE                  | E1SPE                  | E0SPE                  |
| 0          |    |       |      | 0b00 | 1    | 1   | D                      | E2SPE                  | n/a                    | E0HSPE                 |
| 1          | 1  | 1     | 0b0x | x    | x    | x   | D                      | D                      | D                      | D                      |
| 1          |    |       | 0b1x | 0b1x | x    | 0   | D                      | D                      | E1SPE                  | E0SPE                  |
| 1          |    |       |      | 0b1x | x    | 1   | D                      | D                      | n/a                    | D                      |
| 1          |    |       |      | 0b00 | x    | 0   | D                      | E2SPE                  | E1SPE                  | E0SPE                  |
| 1          |    |       |      | 0b00 | x    | 1   | D                      | E2SPE                  | n/a                    | E0HSPE                 |

This is described in the pseudocode function StatisticalProfilingEnabled() .

Table D17-2 shows whether profiling is stopped . Each column in the left side of the table refers to the Effective value of a field in a System register.

## Table D17-2 Profiling stopped

| PMBSR_EL1.S   | MDCR_EL3.PMSEE   | PMBSR_EL3.S   | PMSCR_EL2.EE   | PMBSR_EL2.S   | Profiling stopped   |
|---------------|------------------|---------------|----------------|---------------|---------------------|
| 0b0           | 0b00             | X             | XX             | X             | True                |
| 0b0           | 0b01             | X             | 0b0X           | X             | True                |
| 0b0           | 0b01             | X             | 0b1X           | 0b0           | True                |
| 0b0           | 0b01             | X             | 0b1X           | 0b1           | False               |
| 0b0           | 0b1X             | 0b0           | 0b0X           | X             | True                |
| 0b0           | 0b1X             | 0b0           | 0b1X           | 0b0           | True                |
| 0b0           | 0b1X             | 0b0           | 0b1X           | 0b1           | False               |
| 0b0           | 0b1X             | 0b1           | XX             | X             | False               |
| 0b1           | XX               | X             | XX             | X             | False               |