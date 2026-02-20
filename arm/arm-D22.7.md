## D22.7 Security and power considerations

## D22.7.1 Security considerations

| I DXRGG   | All SMEload and store instructions adhere to the memory access permissions model in The AArch64 Virtual Memory System Architecture.                                            |
|-----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| I MGLWR   | SMEarchitectural state can be access-controlled, meaning that higher levels of privilege can trap access to the state from the same or lower levels of privilege.              |
| I CYPJJ   | System software has controls available to save and restore state between unrelated pieces of software, and must ensure that steps are taken to preserve isolation and privacy. |
| I TDPHC   | Operations performed in Streaming SVE mode respect the requirements of PSTATE.DIT. FEAT_DIT requires data-independent timing when enabled.                                     |

## D22.7.2 Power considerations

IVGWQW

An implementation might use the activity of PSTATE.{SM, ZA} to influence the choice of power-saving states for both functional units and retention of architected state. A PE might consume less power when PSTATE.{SM, ZA} are {0, 0}.

## Chapter D23 AArch64 System Register Encoding

This chapter describes the AArch64 System register encoding space. It contains the following sections:

- The System register encoding space.
- Moves to and from debug and trace System registers.
- Moves to and from non-debug System registers, Special-purpose registers.