## G3.3 Self-hosted trace timestamps

For EL1 using AArch64, see AArch64 Self-hosted Trace.

The trace timestamp is a value that represents the passage of time in real-time. It is calculated from a counter which increments all the time, when the PE is generating trace and when the PE is in a prohibited region.

While self-hosted trace is disabled, the external trace provides the trace timestamp. If the external trace is a standard CoreSight system, the relationship between CoreSight time and the Generic Timer counter is IMPLEMENTATION DEFINED.

When self-hosted trace is enabled, the trace time stamp is one of the following:

- Physical time, which is defined by the physical count value returned by PhysicalCountInt ().
- If FEAT\_ECV is implemented, offset physical time, which is defined as the value of PhysicalCountInt () minus a physical offset.

If any of the following are true the value of the physical offset is zero:

- -EL3 is using AArch32.
- -EL2 is using AArch32.
- -EL2 is not implemented.
- -FEAT\_ECV\_POFF is not implemented.
- -The Effective value of SCR\_EL3.{NSE, NS, RW} is {0, 1, 0}.
- -CNTHCTL\_EL2.ECV is 0.
- -EL3 is implemented and using AArch64, and SCR\_EL3.ECVEn is 0.

Otherwise the value of the physical offset is the value of CNTPOFF\_EL2.

- Virtual time, which is defined as the value of PhysicalCountInt () minus a virtual offset.

If any of the following are true, the virtual offset is zero:

- -EL2 is not implemented.

Otherwise, the virtual offset is always CNTVOFF, including when a read of CNTVCT at the current Exception level would treat the virtual offset as zero.

The following fields control which counter is used for self-hosted trace:

- TRFCR\_EL2.TS.
- HTRFCR.TS.
- TRFCR.TS.

The timestamp used for trace is shown in Table G3-1.

Table G3-1 Timestamp used for trace.

| SelfHostedTraceEnabled()   | TRFCR_EL2.TS or HTRFCR.TS   | TRFCR.TS   | Timestamp traced                     |
|----------------------------|-----------------------------|------------|--------------------------------------|
| FALSE                      | xx                          | xx         | CoreSight time                       |
| TRUE                       | 0b00                        | 0b01       | PhysicalCountInt() - virtual offset  |
|                            | 0b00                        | 0b10       | PhysicalCountInt() - physical offset |
|                            | 0b00                        | 0b11       | PhysicalCountInt()                   |
|                            | 0b01                        | xx         | PhysicalCountInt() - virtual offset  |
|                            | 0b10 a                      | xx         | PhysicalCountInt() - physical offset |
|                            | 0b11                        | xx         | PhysicalCountInt()                   |

Note

The counter value used for the trace timestamp is not affected by the Effective value of HCR\_EL2.E2H, or whether EL2 is enabled or disabled in the current Security state.