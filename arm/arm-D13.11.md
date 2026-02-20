## D13.11 Counter access

| I VYCGK   | All implemented event counters are accessible in EL3 and EL2. If EL2 is implemented the hypervisor uses HDCR.HPMN to reserve an event counter, with the effect that if EL2 is enabled in the current Security state, software cannot access that counter and its associated state from EL0 or EL1.   |
|-----------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R SRPKH   | When FEAT_FGT is implemented, if PMSELR.SEL or n indicates an unimplemented event counter, access to PMXEVTYPER, PMXEVCNTR, PMEVTYPER<n>, or PMEVCNTR<n> is UNDEFINED.                                                                                                                               |
| I SDHCP   | Whether software can access an event counter at an Exception level does not affect whether the counter counts events at that Exception level. For more information, see Controlling the PMUcounters and Enabling PMUcounters.                                                                        |

## D13.11.1 PMEVCNTR&lt; n &gt; event counters

DYBKKV

Table D13-11 shows how the counter range affects the behavior of permitted accesses to the event counter registers.

Table D13-11 Result of event counter System register access

| Counter range           | EL2 enabled in current Security state   | Access at Exception level   | Access at Exception level   |           |           |
|-------------------------|-----------------------------------------|-----------------------------|-----------------------------|-----------|-----------|
|                         |                                         | EL3                         | EL2                         | EL1       | EL0       |
| First range             | -                                       | Succeeds                    | Succeeds                    | Succeeds  | Succeeds  |
| Second range            | False                                   | Succeeds                    | Succeeds                    | Succeeds  | Succeeds  |
| Second range            | True                                    | Succeeds                    | Succeeds                    | No access | No access |
| Third range             | -                                       | No access                   | No access                   | No access | No access |
| Counter not implemented | -                                       | No access                   | No access                   | No access | No access |

IMWZHC

Where Table D13-11 shows access succeeds for an event counter n , the access might be UNDEFINED or generate a trap exception. See the descriptions of PMEVCNTR&lt;n&gt; and PMXEVCNTR for details.

IDXWRB

Where Table D13-11 shows no access for an event counter n , all of the following apply:

- When PMSELR.SEL is n , the PE prevents direct reads and direct writes of PMXEVTYPER or PMXEVCNTR.
- The PE prevents direct reads and direct writes of PMEVTYPER&lt;n&gt; and PMEVCNTR&lt;n&gt;.
- If FEAT\_PMUv3\_SS is implemented, then the PE prevents direct reads and direct writes of PMEVCNTSVR&lt;n&gt;\_EL1.
- Direct reads and direct writes of the following register bits are RAZ/WI:
- -PMOVSCLR[ n ].
- -PMOVSSET[ n ].
- -PMCNTENSET[ n ].
- -PMCNTENCLR[ n ].
- -PMINTENSET[ n ].
- -PMINTENCLR[ n ].
- -PMOVSCLR[ n ].
- -PMOVSSET[ n ].
- -PMCNTENSET[ n ].
- -PMCNTENCLR[ n ].
- -When FEAT\_PMUv3p9 is implemented, PMUACR\_EL1[ n ].
- Direct writes to PMSWINC[ n ] are ignored.
- When FEAT\_PMUv3p9 is implemented, direct writes to PMZR\_EL0[ n ] are ignored.
- Adirect write of 1 to PMCR.P does not reset PMEVCNTR&lt;n&gt;.

## D13.11.2 Cycle and instruction counters

The PMU does not provide any control that a hypervisor can use to reserve the cycle counter for its own use. If FEAT\_FGT is implemented, then controls to trap EL1 and EL0 accesses of the cycle counter to EL2 are provided. However, access to the PMU registers are subject to the access permissions described in Configurable instruction controls.

PMICNTR\_EL0 counts in both AArch32 and AArch64 states. However, PMICNTR\_EL0 and PMICFILTR\_EL0 can only be accessed as a System register in AArch64 state. If FEAT\_FGT2 is implemented, then controls to trap EL1 and EL0 accesses of the instruction counter to EL2 are provided.

## D13.11.3 EL0 access controls

IDXSHB

PMUSERENRcontrols EL0 access to the Performance Monitors. When FEAT\_PMUv3p9 is implemented, PMUACR\_EL1 provides fine-grained control over EL0 access to the Performance Monitors. PMUSERENR\_EL0.UEN enables use of PMUACR\_EL1. The behavior of other PMUSERENR\_EL0 controls also depend on the value of PMUSERENR\_EL0.UEN.

IKPPZZ

Table D13-12 summarizes the behavior of accesses to at EL0 to PMEVCNTR&lt;n&gt;, PMCCNTR, PMSWINC, and, if FEAT\_PMUv3\_ICNTR is implemented and the PE is executing in AArch64 state, PMICNTR\_EL0. In this table:

UEN

Means PMUSERENR\_EL0.UEN. If FEAT\_PMUv3p9 is not implemented, or EL1 is using AArch32, then the Effective value of this bit is 0.

EN

Means PMUSERENR.EN.

xR/W

Means:

- PMUSERENR.ER for PMEVCNTR&lt;n&gt;.
- PMUSERENR.CR for PMCCNTR.
- PMUSERENR\_EL0.IR for PMICNTR\_EL0.
- PMUSERENR\_EL0.SW for PMSWINC.P&lt;n&gt;.

## PMUACR\_EL1.y Means:

- PMUACR\_EL1.P&lt;n&gt; for PMEVCNTR&lt;n&gt;\_EL0 and PMSWINC\_EL0.
- PMUACR\_EL1.C for PMCCNTR\_EL0.
- PMUACR\_EL1.F0 for PMICNTR\_EL0.

This table assumes that all the following apply:

- Event counter &lt;n&gt; is implemented.
- EL2 is not implemented or disabled in the current Security state, or n is less-than HDCR.HPMN.
- FEAT\_PMUv3\_ICNTR is implemented.

## Table D13-12 Summary of counter accesses at EL0

| UEN   | EN   | xR/W   | PMUACR_EL1.y   | Access to PMEVCNTR<n> or PMCCNTR   | Access to PMICNTR_EL0   | Access to PMSWINC.P   |
|-------|------|--------|----------------|------------------------------------|-------------------------|-----------------------|
| 0b0   | 0b0  | 0b0    | x              | UNDEFINED                          | UNDEFINED               | UNDEFINED             |
| 0b0   | 0b0  | 0b1    | x              | RO                                 | UNDEFINED               | WO                    |
| 0b0   | 0b1  | x      | x              | R/W                                | UNDEFINED               | WO                    |
| 0b1   | x    | 0b0    | 0b0            | RAZ/WI                             | RAZ/WI                  | WI                    |
| 0b1   | x    | 0b1    | 0b0            | RAZ/WI                             | RAZ/WI                  | WO                    |
| 0b1   | x    | 0b0    | 0b1            | R/W                                | R/W                     | WO                    |
| 0b1   | x    | 0b1    | 0b1            | RO                                 | RO                      | WO                    |

In Table D13-12, where the column Access to PMEVCNTR&lt;n&gt; or PMCCNTR or the column Access to PMICNTR\_EL0 shows access is RO or RAZ/WI, this also includes ignoring writes to PMZR\_EL0[y].