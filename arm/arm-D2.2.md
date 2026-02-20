## D2.2 Routing debug exceptions

Debug exceptions are routed to the debug target Exception level , ELD, according to the following controls:

- HCR\_EL2.TGE.
- MDCR\_EL2.TDE.
- The Security state when the exception is taken.
- The Exception level where the exception is taken.

This means that, for all debug exceptions, ELD is either EL1 or EL2.

Note

If EL2 is not implemented, the Effective value of HCR\_EL2.TGE is 0 and the Effective value of MDCR\_EL2.TDE is 0. Throughout this section, references to the values of these fields are to the Effective values of the fields.

The routing of debug exceptions is as follows:

## Debug exceptions taken when EL2 is implemented and enabled in the current Security state

The routing of debug exceptions taken depends on the values of MDCR\_EL2.TDE and HCR\_EL2.TGE:

If the Effective value of {MDCR\_EL2.TDE, HCR\_EL2.TGE} is not {0, 0}

Debug exceptions are routed to EL2, ELD is EL2.

## Otherwise

## When EL3 is implemented

Breakpoint Instruction exceptions taken from EL3 are routed to EL3.

All other debug exceptions are disabled from EL3 using AArch64.

## Otherwise

Debug exceptions are routed to EL1. ELD is EL1.

This means that, for all debug exceptions, the debug target Exception level , ELD, is either EL1 or EL2.

Table D2-2, Table D2-3, and Table D2-4 show the routing of debug exceptions. In these tables:

NSE

Means the Effective value of SCR\_EL3.NSE. If FEAT\_RME is not implemented, this is 0.

NS

Means the Effective value of SCR\_EL3.NS. If Secure state is not implemented, this is 1.

EEL2

Means the Effective value of SCR\_EL3.EEL2. If FEAT\_SEL2 is not implemented, this is 0.

TDEor TGE

Means the logical OR of the Effective value of MDCR\_EL2.TDE and the Effective value of HCR\_EL2.TGE.

(EL x )

Means ELD is EL x . However:

- All debug exceptions other than Breakpoint Instruction exceptions are disabled from this Exception level.
- Breakpoint Instruction exceptions taken when executing in this Exception level are routed to the same Exception level. This may not be the same as the ELD Exception level.

Debug exceptions behave as follows:

- Debug exceptions taken from EL1 and EL0 are routed to EL1. ELD is EL1.
- Breakpoint Instruction exceptions taken from EL2 are routed to EL2.
- All other debug exceptions are disabled from EL2 using AArch64.

EL x

Means ELD is EL x .

## Table D2-2 Routing when both EL3 and EL2 are implemented

| NSE   | NS   | EEL2   | TDE or TGE   | EL D when executing in:   | EL D when executing in:   | EL D when executing in:   | EL D when executing in:   |
|-------|------|--------|--------------|---------------------------|---------------------------|---------------------------|---------------------------|
|       |      |        |              | EL0                       | EL1                       | EL2                       | EL3                       |
| 0     | 0    | 0      | X            | EL1                       | EL1                       | n/a                       | (EL1)                     |
| 0     | 0    | 1      | 0            | EL1                       | EL1                       | (EL1)                     | (EL1)                     |
| 0     | 0    | 1      | 1            | EL2                       | EL2                       | EL2                       | (EL2)                     |
| X     | 1    | X      | 0            | EL1                       | EL1                       | (EL1)                     | (EL1)                     |
| X     | 1    | X      | 1            | EL2                       | EL2                       | EL2                       | (EL2)                     |

## Table D2-3 Routing when EL3 is implemented and EL2 is not implemented

| EL D when executing in: EL0   | EL1   | EL3   |
|-------------------------------|-------|-------|
| EL1                           | EL1   | (EL1) |

## Table D2-4 Routing of exceptions

| TDE or TGE   | EL D when executing in:   | EL D when executing in:   | EL D when executing in:   |
|--------------|---------------------------|---------------------------|---------------------------|
|              | EL0                       | EL1                       | EL2                       |
| 0            | EL1                       | EL1                       | (EL1)                     |
| 1            | EL2                       | EL2                       | EL2                       |

## D2.2.1 Pseudocode description of routing debug exceptions

DebugTarget() returns the current debug target Exception level.

DebugTargetFrom() returns the debug target Exception level for the specified Security state.

These functions are described in A-profile Architecture Pseudocode.