## I3.1 About the external interface to the Performance Monitors registers

Arm recommends that:

- An implementation provides the OPTIONAL external debug interface to the Performance Monitors registers, FEAT\_PMUv3\_EXT.

Note

Adebugger can use this interface to access counters in the Performance Monitors.

- The implementation includes the OPTIONAL support for memory-mapped access to the External debug interface.

- [ ] Note

- [ ] - Software running on any PE in a system can use this interface to access counters in the Performance Monitors.

- [ ] - Privileged software should use the MMU to control access to this interface.

- The external debug interface is implemented as defined in Recommended External Debug Interface.

When FEAT\_PMUv3\_EXT64, the 64-bit external PMU programmers' model extension is implemented, all Performance Monitors registers are 64-bit except the 32-bit CoreSight management registers.

The following sections describe the memory-mapped views of the Performance Monitors registers:

- Differences in the external views of the Performance Monitors registers.
- Synchronization of changes to the memory-mapped views.
- Access permissions for external views of the Performance Monitors.

In this section, unless the context explicitly indicates otherwise, any reference to a memory-mapped view applies equally to a register view using:

- An access through an external debug interface.
- Amemory-mapped access.

## I3.1.1 Endianness and supported access sizes

When an implementation supports memory-mapped access to the external debug interface the interface is accessed as a little-endian memory-mapped peripheral. External Performance Monitors registers summary gives the memory map of these registers.

The memory access sizes supported by any peripheral is IMPLEMENTATION DEFINED by the peripheral. For accesses to the external interface to the Performance Monitors registers implementations must:

- Comply with the requirements of Supported access sizes.
- When FEAT\_PMUv3\_EXT32 is implemented, support word-aligned 32-bit accesses to access 32-bit registers or either half of a 64-bit register that is mapped to a doubleword-aligned pair of adjacent 32-bit locations, even if all components with direct memory access to the PMU support making 64-bit accesses.

Permitted word-aligned 32-bit accesses are single-copy atomic at word granularity. When FEAT\_PMUv3\_EXT64 is implemented, permitted doubleword-aligned 64-bit accesses are single-copy atomic at doubleword granularity.

## I3.1.2 Differences in the external views of the Performance Monitors registers

An external view of the Performance Monitors registers accesses the same registers as the System registers interface described in Performance Monitors Extension registers, except that:

- The PMSELR is accessible only in the System registers interface.
- The following registers are accessible only in external views:

I3.1 About the external interface to the Performance Monitors registers

- PMAUTHSTATUS.

- PMCCR.

- PMCFGR.

- PMCIDR0.

- PMCIDR1.

- PMCIDR2.

- PMCIDR3.

- PMDEVARCH.

- PMDEVTYPE.

- PMEVFILT2R&lt;n&gt;.

- PMIIDR.

- PMLAR.

- PMLSR.

- PMPCSCTL.

- PMPCSR.

- PMPIDR0.

- PMPIDR1.

- PMPIDR2.

- PMPIDR3.

- PMPIDR4.

Performance Monitors external register descriptions describes these registers.

- The following registers are accessible only in the external view when FEAT\_PMUv3\_EXT64 is implemented:

- PMCCIDSR.

- PMCNTEN.

- PMDEVAFF.

- PMINTEN.

- PMOVS.

- PMVCIDSR.

Performance Monitors external register descriptions describes these registers.

- The following registers are accessible only in the external view when FEAT\_PMUv3\_EXT32 is implemented:

- PMCID1SR.

- PMCID2SR.

- PMDEVAFF0.

- PMDEVAFF1.

- PMVIDSR.

Performance Monitors external register descriptions describes these registers.

- The following controls do not affect the external views:

- PMSELR.

- PMUSERENR.

- HDCR.{TPM, TPMCR, HPMN}.

Instead, see the register descriptions in External System Control Register Descriptions.

- The PMSWINC\_EL0 register is OPTIONAL in the external view when FEAT\_PMUv3\_EXT32 is implemented. It is not implemented in the external view when FEAT\_PMUv3\_EXT64 is implemented.

## I3.1.3 Synchronization of changes to the memory-mapped views

ICJJNX

Synchronization complies with Synchronization of memory-mapped registers.

In particular, if a Performance Monitor is visible in both System register and an external view, and is accessed simultaneously through these two mechanisms, the behavior must be as if the accesses occurred atomically and in any order. For more information, see Synchronization of changes to the external debug registers.

IYWTNH

If FEAT\_PMUv3\_EXTPMN is implemented, then external accesses to PMCCR.OSLO are required to be observable to the indirect reads made in determining the response to subsequent external accesses without explicit synchronization.

## I3.1.4 Access permissions for external views of the Performance Monitors

IDZGKJ

IYMBZZ

For more information, see External debug interface register access permissions.

The following tables show the access permissions for the Performance Monitors registers in a Debug implementation for Armv8 or later architectures:

- Table I3-1 when the 64-bit external PMU programmers' model extension, FEAT\_PMUv3\_EXT64, is implemented.
- Table I3-2 when FEAT\_PMUv3\_EXT32 is implemented.

These tables use the following terms:

DLK

When FEAT\_DoubleLock is implemented and locked, DoubleLockStatus() == TRUE, accesses to some registers produce an error. Applies to both interfaces.

EPMAD

When AllowExternalPMUAccess() == FALSE, external debug access is disabled for the access. See also Behavior of a not permitted memory-mapped access.

EPMSSAD

If FEAT\_PMUv3\_SS is implemented, when AllowExternalPMSSAccess() == FALSE, external debug access is disabled for the access. See also Behavior of a not permitted memory-mapped access.

Error

Indicates that the access gives an error response.

Def

This shows the default access permissions, if none of the conditions in this list prevent access to the register. See ISCSWJ.

Off

The Core power domain is completely off, or in a low-power state where the Core power domain registers cannot be accessed, and EDPRSR.PU will read as zero.

Note

If debug power is off, then all external debug interface accesses return an error.

OSLK

When the OS Lock is locked, OSLSR\_EL1.OSLK is 1, accesses to some registers produces an error.

If FEAT\_PMUv3\_EXTPMN is implemented, the access is a Most secure access, and the Effective value of PMCCR.OSLO is 1, then the value of OSLSR\_EL1.OSLK is treated as 0 for the access. This column shows the effect of this control on accesses using the external debug interface.

SLK This indicates the modified default access permissions for OPTIONAL memory-mapped accesses to the external debug interface if the optional Software Lock is locked. See Register access permissions for memory-mapped accesses.

For all other accesses, this column is ignored.

Note

When FEAT\_PMUv3\_EXT64 is implemented, the Software Lock is not implemented.

- -Indicates that the control has no effect on the behavior of the access:
- If no other control affects the behavior, the Default access behavior applies.
- However, another control might determine the behavior.

Table I3-1 Access permissions for the Performance Monitors registers when FEAT\_PMUv3\_EXT64 is implemented

| Offset    | Register          | Domain   | Off   | DLK   | OSLK   | EPMAD   | EPMSSAD   | Def   |
|-----------|-------------------|----------|-------|-------|--------|---------|-----------|-------|
| 0x000+8xn | PMEVCNTR<n>_EL0 a | Core     | Error | Error | Error  | Error   | -         | RW    |
| 0x0F8     | PMCCNTR_EL0       | Core     | Error | Error | Error  | Error   | -         | RW    |
| 0x100     | PMICNTR_EL0       | Core     | Error | Error | Error  | Error   | -         | RW    |
| 0x200     | PMPCSR            | Core     | Error | Error | Error  | -       | -         | RO    |
| 0x208     | PMVCIDSR          | Core     | Error | Error | Error  | -       | -         | RO    |
| 0x220     | PMPCSR            | Core     | Error | Error | Error  | -       | -         | RO    |
| 0x228     | PMCCIDSR          | Core     | Error | Error | Error  | -       | -         | RO    |

| Offset        | Register                                      | Domain                                        | Off                                           | DLK                                           | OSLK                                          | EPMAD                                         | EPMSSAD                                       | Def                                           |
|---------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| 0x400+8xn     | PMEVTYPER<n>_EL0 a                            | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0x4F8         | PMCCFILTR_EL0                                 | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0x500         | PMICFILTR_EL0                                 | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0x600+8xn b   | PMEVCNTSVR<n>_EL1 a                           | Core                                          | Error                                         | Error                                         | -                                             | -                                             | Error                                         | RO                                            |
| 0x6F8 b       | PMCCNTSVR_EL1                                 | Core                                          | Error                                         | Error                                         | -                                             | -                                             | Error                                         | RO                                            |
| 0x700 b       | PMICNTSVR_EL1                                 | Core                                          | Error                                         | Error                                         | -                                             | -                                             | Error                                         | RO                                            |
| 0x708-0x7FC b | Reserved                                      | -                                             |                                               |                                               |                                               |                                               |                                               |                                               |
| 0x800+8xn     | PMEVFILT2R<n>                                 | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC00         | PMCNTENSET_EL0                                | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC10         | PMCNTEN                                       | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC20         | PMCNTENCLR_EL0                                | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC40         | PMINTENSET_EL1                                | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC50         | PMINTEN                                       | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC60         | PMINTENCLR_EL1                                | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC80         | PMOVSCLR_EL0                                  | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xC90         | PMOVS                                         | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xCA0         | PMZR_EL0                                      | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | WO                                            |
| 0xCC0         | PMOVSSET_EL0                                  | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xCE0         | PMCGCR0                                       | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            |
| 0xD80 - 0xDFC | -                                             | -                                             | IMPLEMENTATION                                |                                               | DEFINED registers                             | c                                             |                                               |                                               |
| 0xE00         | PMCFGR                                        | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            |
| 0xE08         | PMIIDR                                        | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            |
| 0xE10         | PMCR_EL0                                      | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            |
| 0xE30 b       | PMSSCR_EL1                                    | Core                                          | Error                                         | Error                                         | -                                             | -                                             | Error                                         | RO                                            |
| 0xE38 - 0xE3C | -                                             | -                                             | IMPLEMENTATION                                |                                               | DEFINED registers                             | c                                             |                                               |                                               |
| 0xE44         | PMMIR                                         | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            |
| 0xE50         | PMPCSCTL                                      | Core                                          | Error                                         | Error                                         | Error                                         | -                                             | -                                             | RW                                            |
| 0xE58 d       | PMCCR                                         | Core                                          | Error                                         | Error                                         | -                                             | -                                             | -                                             | RW                                            |
| 0xE80 - 0xEFC | Integration registers                         | -                                             | IMPLEMENTATION                                |                                               | DEFINED registers                             | c                                             |                                               |                                               |
| 0xF00 - 0xFFC | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance |

Table I3-2 Access permissions for the Performance Monitors registers when FEAT\_PMUv3\_EXT32 is implemented

| Offset    | Register                  | Domain   | Off   | DLK   | OSLK   | EPMAD   | EPMSSAD   | Def   | SLK   |
|-----------|---------------------------|----------|-------|-------|--------|---------|-----------|-------|-------|
| 0x000+8xn | PMEVCNTR<n>_EL0[31:0] a a | Core     | Error | Error | Error  | Error   | -         | RW    | RO    |
| 0x004+8xn | PMEVCNTR<n>_EL0[63:32]    |          |       |       |        |         |           |       |       |

| Offset                  | Register                                         | Domain   | Off   | DLK            | OSLK              | EPMAD   | EPMSSAD   | Def   | SLK   |
|-------------------------|--------------------------------------------------|----------|-------|----------------|-------------------|---------|-----------|-------|-------|
| 0x0F8 0x0FC             | PMCCNTR_EL0[31:0] PMCCNTR_EL0[63:32]             | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0x100 0x104             | PMICNTR_EL0[31:0] PMICNTR_EL0[63:32]             | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0x200 0x204             | PMPCSR[31:0] PMPCSR[63:32]                       | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x208                   | PMCID1SR                                         | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x20C                   | PMVIDSR                                          | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x220 0x224             | PMPCSR[31:0] PMPCSR[63:32]                       | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x228                   | PMCID1SR                                         | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x22C                   | PMCID2SR                                         | Core     | Error | Error          | Error             | -       | -         | RO    | RO    |
| 0x400+4xn               | PMEVTYPER<n>_EL0 a [31:0]                        | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0x47C                   | PMCCFILTR_EL0[31:0]                              | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0x480                   | PMICFILTR_EL0[31:0]                              | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0x600+8xn b 0x604+8xn b | PMEVCNTSVR<n>_EL1[31:0] PMEVCNTSVR<n>_EL1[63:32] | Core     | Error | Error          | -                 | -       | Error     | RO    | RO    |
| 0x6F8 b 0x6FC b         | PMCCNTSVR_EL1[31:0] PMCCNTSVR_EL1[63:32]         | Core     | Error | Error          | -                 | -       | Error     | RO    | RO    |
| 0x700 b 0x704 b         | PMICNTSVR_EL1[31:0] PMICNTSVR_EL1[63:32]         | Core     | Error | Error          | -                 | -       | Error     | RO    | RO    |
| 0x708 - 0x7FC b         | Reserved                                         | -        |       |                |                   |         |           |       |       |
| 0x800+4xn               | PMEVFILT2R<n>                                    | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xA00+4xn c             | PMEVTYPER<n>_EL0 [63:32]                         | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xA7C c                 | PMCCFILTR_EL0[63:32]                             | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xA80 c                 | PMICFILTR_EL0[63:32]                             | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xA84 - 0xAFC c         | Reserved                                         | -        |       |                |                   |         |           |       |       |
| 0xB00 - 0xBFC           | -                                                | -        |       | IMPLEMENTATION | DEFINED registers | d       |           |       |       |
| 0xC00 0xC04             | PMCNTENSET_EL0[31:0] PMCNTENSET_EL0[63:32]       | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xC20 0xC24             | PMCNTENCLR_EL0[31:0] PMCNTENCLR_EL0[63:32]       | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xC40 0xC44             | PMINTENSET_EL1[31:0] PMINTENSET_EL1[63:32]       | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xC60 0xC64             | PMINTENCLR_EL1[31:0] PMINTENCLR_EL1[63:32]       | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xC80 0xC84             | PMOVSCLR_EL0[31:0] PMOVSCLR_EL0[63:32]           | Core     | Error | Error          | Error             | Error   | -         | RW    | RO    |
| 0xCA0                   | PMSWINC_EL0                                      | Core     | Error | Error          | Error             | Error   | -         | WO    | WI    |
| 0xCA0 0xCA4             | PMZR_EL0[31:0] PMZR_EL0[63:32]                   | Core     | Error | Error          | Error             | Error   | -         | WO    | WI    |

| Offset                  | Register                                      | Domain                                        | Off                                           | DLK                                           | OSLK                                          | EPMAD                                         | EPMSSAD                                       | Def                                           | SLK                                           |
|-------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|-----------------------------------------------|
| 0xCC0 0xCC4             | PMOVSSET_EL0[31:0] PMOVSSET_EL0[63:32]        | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            | RO                                            |
| 0xCE0                   | PMCGCR0                                       | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            | RO                                            |
| 0xD80 - 0xDFC           | -                                             | -                                             | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            |                                               |                                               |                                               |
| 0xE00                   | PMCFGR                                        | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            | RO                                            |
| 0xE04                   | PMCR_EL0                                      | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RW                                            | RO                                            |
| 0xE08                   | PMIIDR                                        | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            | RO                                            |
| 0xE20 0xE24 0xE28 0xE2C | PMCEID0 PMCEID1 PMCEID2 PMCEID3               | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            | RO                                            |
| 0xE30 b 0xE34 b         | PMSSCR_EL1[31:0] PMSSCR_EL1[63:32]            | Core                                          | Error                                         | Error                                         | -                                             | -                                             | Error                                         | RO                                            | RO                                            |
| 0xE38 - 0xE3C           |                                               | -                                             | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            |                                               |                                               |                                               |
| 0xE40 0xE44             | PMMIR[31:0] PMMIR[63:32]                      | Core                                          | Error                                         | Error                                         | Error                                         | Error                                         | -                                             | RO                                            | RO                                            |
| 0xE50 0xE54             | PMPCSCTL[31:0] PMPCSCTL[63:32]                | Core                                          | Error                                         | Error                                         | Error                                         | -                                             | -                                             | RW                                            | RW                                            |
| 0xE58 e                 | PMCCR                                         | Core                                          | Error                                         | Error                                         | -                                             | -                                             | -                                             | RW                                            | RW                                            |
| 0xE80 - 0xEFC           | Integration registers                         | -                                             | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            | IMPLEMENTATION DEFINED registers d            |                                               |                                               |                                               |
| 0xF00 - 0xFFC           | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance | Management registers and CoreSight compliance |

An external access to a register is a Most secure access, if it is one of the following:

- Root access, when FEAT\_RME is implemented.
- Secure access, when FEAT\_RME is not implemented and Secure state is implemented.
- Non-secure access, when both FEAT\_RME and Secure state are not implemented.

IMWDRP The pseudocode functions AllowExternalPMUAccess() and AllowExternalPMSSAccess() always return True for a Most secure access.

ISCSWJ

Table I3-3 shows how the counter range affects the behavior of permitted accesses to the event counter registers.

## Table I3-3 Result of PMEVCNTR&lt;n&gt;\_EL0 event counter external access

| Counter range   | External access Most secure access   | Not Most secure access   |
|-----------------|--------------------------------------|--------------------------|
| First range     | Succeeds                             | Succeeds                 |

ILQFWT

| Counter range           | External access Most secure access   | Not Most secure access   |
|-------------------------|--------------------------------------|--------------------------|
| Second range            | Succeeds                             | Succeeds                 |
| Third range             | Succeeds                             | No access                |
| Counter not implemented | No access                            | No access                |

RDQYGL

IWYJGF

Where Table I3-3 shows no access for an event counter n due to the access not being a Most secure access, all of the following apply for permitted accesses:

- The following registers are RAZ/WI:
- -PMEVCNTR&lt;n&gt;\_EL0.
- -PMEVTYPER&lt;n&gt;\_EL0.
- -PMEVFILT2R&lt;n&gt;
- -If FEAT\_PMUv3\_SS is implemented, PMEVCNTSVR&lt;n&gt;\_EL1.
- The following register fields are RAZ/WI:
- -PMOVSCLR\_EL0[n].
- -PMOVSSET\_EL0[n].
- -PMCNTENSET\_EL0[n].
- -PMCNTENCLR\_EL0[n].
- -PMINTENSET\_EL1[n].
- -PMINTENCLR\_EL1[n].
- -If FEAT\_PMUv3\_EXT64 is implemented:
- -PMOVS[n].
- -PMCNTEN[n].
- -PMINTEN[n].
- -If FEAT\_PMUv3p9 is implemented, PMZR\_EL0[n].
- -If PMSWINC\_EL0 is implemented in the external interface, PMSWINC\_EL0[n].
- Awrite of 1 to PMCR\_EL0.P does not reset PMEVCNTR&lt;n&gt;\_EL0.

When FEAT\_PMUv3\_EXTPMN is implemented, for an external access that is not a Most secure access, all of the following apply:

- If FEAT\_PMUv3\_ICNTR is implemented, then PMCFGR.N and PMCGCR0.CG0NC reads as the Effective value of PMCCR.EPMN plus one.
- If FEAT\_PMUv3\_ICNTR is not implemented, then PMCFGR.N reads as the Effective value of PMCCR.EPMN.

## Chapter I4 Recommended External Interface to the Activity Monitors

This chapter describes the optional external interface to the Activity Monitors Extension registers. It contains the following section:

- About the external interface to the Activity Monitors registers

Note

Activity Monitors external register descriptions describes the external view of the Activity Monitors Extension registers.