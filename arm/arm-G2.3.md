## G2.3 The debug exception enable controls

The enable controls for each debug exception are as follows:

## Breakpoint Instruction exceptions

None. Breakpoint Instruction exceptions are always enabled.

## Breakpoint exceptions

DBGDSCRext.MDBGen, plus an enable control for each breakpoint, DBGBCR&lt;n&gt;.E.

## Watchpoint exceptions

DBGDSCRext.MDBGen, plus an enable control for each watchpoint, DBGWCR&lt;n&gt;.E.

## Vector Catch exceptions

DBGDSCRext.MDBGen.

In addition, for all debug exceptions other than Breakpoint Instruction exceptions, software must configure the controls that enable debug exceptions from the current Exception level and Security state. See Enabling debug exceptions.

The PE cannot take a debug exception if debug exceptions are disabled from either the current Exception level or the current Security state.

Breakpoint Instruction exceptions are always enabled from the current Exception level and Security state.

There is no mechanism to access the extended breakpoints and watchpoints in AArch32 state.

## G2.3.1 Enabling debug exceptions

Adebug exception can only be taken if all of the following are true:

- The OS Lock is unlocked.
- DoubleLockStatus() == FALSE.
- The debug exception is enabled from the current Privilege level.
- The debug exception is enabled from the current Security state.

Table G2-5 shows when debug exceptions are enabled from the current Privilege level.

## Table G2-5 Whether debug exceptions are enabled from the current Privilege level

| Current Privilege level   | Breakpoint Instruction exceptions   | All other debug exceptions   |
|---------------------------|-------------------------------------|------------------------------|
| PL2                       | Enabled                             | Disabled                     |
| PL1                       | Enabled                             | Enabled                      |
| PL0                       | Enabled                             | Enabled                      |

Table G2-6 shows when debug exceptions are enabled from the current Security state.

Table G2-6 Whether debug exceptions are enabled from the current Security state

| Current Security state   | Breakpoint Instruction exceptions   | All other debug exceptions                                                             |
|--------------------------|-------------------------------------|----------------------------------------------------------------------------------------|
| Non-secure               | Enabled                             | Enabled from PL1 and PL0 only.                                                         |
| Secure                   | Enabled                             | Depends on SDCR.SPD and SDER.SUIDEN. See Disabling debug exceptions from Secure state. |

## G2.3.2 Disabling debug exceptions from Secure state

If EL3 is implemented, software executing at EL3 can enable or disable all debug exceptions taken from Secure PL1 other than Breakpoint Instruction exceptions, by using one of:

- The Secure Privileged Debug field, SDCR.SPD, if EL3 is using AArch32.
- The AArch32 Secure Privileged Debug field, MDCR\_EL3.SPD32, if EL3 is using AArch64.

If debug exceptions are disabled from Secure PL1, software executing at Secure PL1 can set the Secure User Invasive Debug Enable bit, SDER.SUIDEN, to 1 to enable all debug exceptions taken from Secure PL0 other than Breakpoint Instruction exceptions.

Note

Breakpoint Instruction exceptions are always enabled.

The architecture does not support disabling debug in Non-secure state.

Note

If the boot software that is executed when reset is deasserted programs SUIDEN and SPD so that all debug exceptions are disabled from Secure state, software operating at EL3 never has to switch any of the debug registers between the Security states.

## G2.3.3 Pseudocode description of enabling debug exceptions

AArch64.GenerateDebugExceptions() determines whether debug exceptions are enabled from the current Exception level and Security state. AArch64.GenerateDebugExceptionsFrom() determines whether debug exceptions are enabled from the specified Exception level and Security state.