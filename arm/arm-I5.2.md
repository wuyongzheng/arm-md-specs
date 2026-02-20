## I5.2 External Performance Monitors registers summary

When an implementation provides access to the Performance Monitors registers through the External debug interface, that interface provides access to:

- Performance Monitors System registers.
- Aread-only configuration register, PMCFGR.
- The OPTIONAL CoreSight registers for the Performance Monitors, if they are implemented.

The locations of the registers are defined as offsets from a system-defined base address. Performance Monitors external register views defines this memory map.

## I5.2.1 Performance Monitors external register views

The following tables show the external view of the Performance Monitors registers:

- Table I5-1 when FEAT\_PMUv3\_EXT64, the 64-bit external PMU programmers' model extension is implemented.
- Table I5-2 when FEAT\_PMUv3\_EXT32 is implemented.

All other entries are reserved.

## Note

- Counters that are reserved because HDCR.HPMN has been changed from its reset value remain visible in any external view.
- The registers that relate to an implemented event counter, PMN x , are PMEVCNTR&lt;n&gt; and PMEVTYPER&lt;n&gt;.
- Tables in this section only list the Armv8 registers. For encoding information of the registers introduced by Armv9, see the individual register descriptions in this chapter.

Each entry in the Name column links to the register description in Performance Monitors external register descriptions.

Table I5-1 Performance Monitors external register views when FEAT\_PMUv3\_EXT64 is implemented

| Name              | Type   | Description                                                 | Offset        |
|-------------------|--------|-------------------------------------------------------------|---------------|
| PMEVCNTR<n>_EL0   | RW     | Performance Monitors Event Counter Register                 | 0x000+8xn     |
| PMCCNTR_EL0       | RW     | Performance Monitors Cycle Counter Register                 | 0x0F8         |
| PMICNTR_EL0       | RW     | Performance Monitors Instruction Counter Register           | 0x100         |
| PMPCSR a          | RW     | Program Counter Sample Register                             | 0x200         |
| PMVCIDSR a        | RW     | CONTEXTIDR_EL1 and VMIDSample Register                      | 0x208         |
| PMPCSR a          | RW     | Program Counter Sample Register, alias                      | 0x220         |
| PMCCIDSR a        | RW     | CONTEXTIDR_ELx Sample Register                              | 0x228         |
| PMEVTYPER<n>_EL0  | RW     | Performance Monitors Event Type and Filter Register         | 0x400+8xn     |
| PMCCFILTR_EL0     | RW     | Performance Monitors Cycle Counter Filter Register          | 0x4F8         |
| PMICFILTR_EL0     | RW     | Performance Monitors Instruction Counter Filter Register    | 0x500         |
| PMEVCNTSVR<n>_EL1 | RO     | Performance Monitors Event Count Saved Value Register<n>    | 0x600+8xn b   |
| PMCCNTSVR_EL1     | RO     | Performance Monitors Cycle Count Saved Value Register       | 0x6F8 b       |
| PMICNTSVR_EL1     | RO     | Performance Monitors Instruction Count Saved Value Register | 0x700 b       |
| -                 | -      | Reserved                                                    | 0x708 - 0x7FC |

| Name                          | Type   | Description                                                 | Offset            |
|-------------------------------|--------|-------------------------------------------------------------|-------------------|
| PMEVFILT2R<n>                 | RW     | Performance Monitors Event Filter Register                  | 0800+8xn          |
| PMCNTENSET_EL0                | RW     | Performance Monitors Count Enable Set Register              | 0xC00             |
| PMCNTEN                       | RW     | Performance Monitors Count Enable Register                  | 0xC10             |
| PMCNTENCLR_EL0                | RW     | Performance Monitors Count Enable Clear Register            | 0xC20             |
| PMINTENSET_EL1                | RW     | Performance Monitors Interrupt Enable Set Register          | 0xC40             |
| PMINTEN                       | RW     | Performance Monitors Interrupt Enable Register              | 0xC50             |
| PMINTENCLR_EL1                | RW     | Performance Monitors Interrupt Enable Clear Register        | 0xC60             |
| PMOVSCLR_EL0                  | RW     | Performance Monitors Overflow Flag Status Clear Register    | 0xC80             |
| PMOVS                         | RW     | Performance Monitors Overflow Flag Status Register          | 0xC90             |
| PMZR_EL0                      | WO     | Performance Monitors Zero with Mask                         | 0xCA0             |
| PMOVSSET_EL0                  | RW     | Performance Monitors Overflow Flag Status Set Register      | 0xCC0             |
| PMCGCR0                       | RO     | Counter Group Configuration Register 0                      | 0xCE0             |
| -                             | -      | IMPLEMENTATION DEFINED                                      | 0xD80 - 0xDFC     |
| PMCFGR                        | RO     | Performance Monitors Configuration Register                 | 0xE00             |
| PMIIDR                        | RO     | Performance Monitors Implementation Identification Register | 0xE08             |
| PMCR_EL0                      | RW     | Performance Monitors Control Register                       | 0xE10             |
| PMSSCR_EL1                    | RO     | Performance Monitors Snapshot Status and Capture Register   | 0xE30 b           |
| -                             | -      | IMPLEMENTATION DEFINED                                      | 0xE38 - 0xE3C     |
| PMMIR                         | RO     | Performance Monitors Machine Identification Register        | 0xE40             |
| PMPCSCTL                      | RW     | PC Sample-based Profiling Control Register                  | 0xE50             |
| -                             | -      | IMPLEMENTATION DEFINED                                      | 0xE80 - 0xEFC     |
| PMITCTRL c                    | RW     | Integration Model Control registers                         | 0xF00             |
| PMDEVAFF c                    | RO     | Device Affinity Register                                    | 0xFA8             |
| PMLAR c, d                    | WO     | Lock Access Register                                        | 0xFB0             |
| PMLSR c, d                    | RO     | Lock Status Register                                        | 0xFB4             |
| PMAUTHSTATUS c                | RO     | Authentication Status Register                              | 0XFB8             |
| PMDEVARCH c                   | RO     | Device Architecture Register                                | 0xFBC             |
| PMDEVID a                     | RO     | Performance Monitors Device ID Register                     | 0xFC8             |
| PMDEVTYPE c                   | RO     | Device Type Register                                        | 0xFCC             |
| PMPIDR4 c PMPIDR0 c PMPIDR1 c | RO     | Peripheral ID registers                                     | 0xFD0 0xFE0 0xFE4 |
| PMPIDR2 c                     |        |                                                             |                   |
|                               |        |                                                             | 0xFE8             |
| PMPIDR3 c                     |        |                                                             | 0xFEC             |
| PMCIDR0 c                     | RO     | Component ID registers                                      | 0xFF0             |
| PMCIDR1 c                     |        |                                                             | 0xFF4             |
| PMCIDR2 c                     |        |                                                             | 0xFF8             |
| PMCIDR3 c                     |        |                                                             | 0xFFC             |

Before Armv8.2. the PC Sample-based Profiling Extension can, instead, be implemented in the memory-mapped debug registers space, see The PC Sample-based Profiling Extension.

b. If FEAT\_PMUv3\_SS is implemented, then 0x600 -0x7FC are defined or reserved. Otherwise, these locations are IMPLEMENTATION DEFINED.

c. CoreSight interface registers, see Management registers and CoreSight compliance.

d. The Software lock registers are defined as part of CoreSight compliance, but their contents depend on the type of access that is made and whether the OPTIONAL Software lock is implemented. See the register description for details.

Table I5-2 Performance Monitors external register views when FEAT\_PMUv3\_EXT32 is implemented

| Name                                             | Type   | Description                                                 | Offset                  |
|--------------------------------------------------|--------|-------------------------------------------------------------|-------------------------|
| PMEVCNTR<n>_EL0[31:0] PMEVCNTR<n>_EL0[63:32]     | RW     | Performance Monitors Event Counter Register                 | 0x000+8xn 0x004+8xn     |
| PMCCNTR_EL0[31:0] PMCCNTR_EL0[63:32]             | RW     | Performance Monitors Cycle Counter Register a               | 0x0F8 0x0FC             |
| PMICNTR_EL0[31:0] PMICNTR_EL0[63:32]             | RW     | Performance Monitors Instruction Counter Register           | 0x100 0x104             |
| PMPCSR[31:0] b PMPCSR[63:32] b                   | RW     | Program Counter Sample Register                             | 0x200 0x204             |
| PMCID1SR b                                       | RW     | CONTEXTIDR_EL1 Sample Register                              | 0x208                   |
| PMVIDSR b                                        | RW     | VMIDSample Register                                         | 0x20C                   |
| PMPCSR[31:0] b PMPCSR[63:32] b                   | RW     | Program Counter Sample Register, alias                      | 0x220 0x224             |
| PMCID1SR b                                       | RW     | CONTEXTIDR_EL1 Sample Register (alias)                      | 0x228                   |
| PMCID2SR b                                       | RW     | CONTEXTIDR_EL2 Sample Register                              | 0x22C                   |
| PMEVTYPER<n>_EL0 [31:0]                          | RW     | Performance Monitors Event Type and Filter Register         | 0x400+4xn               |
| PMCCFILTR_EL0 [31:0]                             | RW     | Performance Monitors Cycle Counter Filter Register          | 0x47C                   |
| PMICFILTR_EL0[31:0]                              | RW     | Performance Monitors Instruction Counter Filter Register    | 0x480                   |
| PMEVCNTSVR<n>_EL1[31:0] PMEVCNTSVR<n>_EL1[63:32] | RO     | Performance Monitors Event Count Saved Value Register       | 0x600+8xn c 0x604+8xn c |
| PMCCNTSVR_EL1[31:0] PMCCNTSVR_EL1[63:32]         | RO     | Performance Monitors Cycle Count Saved Value Register       | 0x6F8 c 0x6FC c         |
| PMICNTSVR_EL1[31:0] PMICNTSVR_EL1[63:32]         | RO     | Performance Monitors Instruction Count Saved Value Register | 0x700 c 0x704 c         |
| -                                                | -      | Reserved                                                    | 0x708 - 0x7FC c         |
| PMEVFILT2R<n>                                    | RW     | Performance Monitors Event Filter Registers                 | 0x800+8xn               |
| PMEVTYPER<n>_EL0 [63:32]                         | RW     | Performance Monitors Event Type and Filter Register         | 0xA00+4xn d             |
| PMCCFILTR_EL0 [63:32]                            | RW     | Performance Monitors Cycle Counter Filter Register          | 0xA7C d                 |
| PMICFILTR_EL0[63:32]                             | RW     | Performance Monitors Instruction Counter Filter Register    | 0xA80 d                 |
| -                                                | -      | Reserved                                                    | 0xA84 - 0xAFC d         |
| -                                                | -      | IMPLEMENTATION DEFINED                                      | 0xB00 - 0xBFC           |
| PMCNTENSET_EL0[31:0] e PMCNTENSET_EL0[63:32] h   | RW     | Performance Monitors Count Enable Set Register              | 0xC00 0xC04             |
| PMCNTENCLR_EL0[31:0] e PMCNTENCLR_EL0[63:32] e   | RW     | Performance Monitors Count Enable Clear Register            | 0xC20 0xC24             |
| PMINTENSET_EL1[31:0] e PMINTENSET_EL1[63:32] e   | RW     | Performance Monitors Interrupt Enable Set Register          | 0xC40 0xC44             |

| Name                                              | Type   | Description                                                            | Offset                        |
|---------------------------------------------------|--------|------------------------------------------------------------------------|-------------------------------|
| PMINTENCLR_EL1[31:0] e PMINTENCLR_EL1[63:32] e    | RW     | Performance Monitors Interrupt Enable Clear Register                   | 0xC60 0xC64                   |
| PMOVSCLR_EL0[31:0] e PMOVSCLR_EL0[63:32] e        | RW     | Performance Monitors Overflow Flag Status Clear Register               | 0xC80 0xC84                   |
| PMSWINC_EL0 f                                     | WO     | Performance Monitors Software Increment Register                       | 0xCA0                         |
| PMZR_EL0[31:0] PMZR_EL0[63:32]                    | WO     | Performance Monitors Zero with Mask                                    | 0xCA0 0xCA4                   |
| PMOVSSET_EL0[31:0] e PMOVSSET_EL0[63:32] e        | RW     | Performance Monitors Overflow Flag Status Set Register                 | 0xCC0 0xCC4                   |
| PMCGCR0                                           | RO     | Counter Group Configuration Register 0                                 | 0xCE0                         |
| -                                                 | -      | IMPLEMENTATION DEFINED                                                 | 0xD80 - 0xDFC                 |
| PMCFGR                                            | RO     | Performance Monitors Configuration Register                            | 0xE00                         |
| PMCR_EL0                                          | RW     | Performance Monitors Control Register                                  | 0xE04                         |
| PMIIDR                                            | RO     | Performance Monitors Implementation Identification Register            | 0xE08                         |
| PMCEID0 PMCEID1 PMCEID2 PMCEID3                   | RO     | Performance Monitors Common Event Identification Registers             | 0xE20 0xE24 0xE28 0xE2C       |
| PMSSCR_EL1[31:0] PMSSCR_EL1[63:32]                | RO     | Performance Monitors Snapshot Status and Capture Register, bits [31:0] | 0xE30 c 0xE34 c               |
| -                                                 | -      | IMPLEMENTATION DEFINED                                                 | 0xE38 - 0xE3C                 |
| PMMIR[31:0] e PMMIR[63:32] e                      | RO     | Performance Monitors Machine Identification Register, bits [31:0]      | 0xE40 0xE44                   |
| PMPCSCTL[31:0] e PMPCSCTL[63:32] e                | RW     | PC Sample-based Profiling Control Register, bits [31:0]                | 0xE50 0xE54                   |
| -                                                 | -      | IMPLEMENTATION DEFINED                                                 | 0xE80 - 0xEFC                 |
| PMITCTRL g                                        | RW     | Integration Model Control registers                                    | 0xF00                         |
| PMDEVAFF0 g PMDEVAFF1 g                           | RO     | Device Affinity registers                                              | 0xFA8 0xFAC                   |
| PMLAR g , h                                       | WO     | Lock Access Register                                                   | 0xFB0                         |
| PMLSR g , h                                       | RO     | Lock Status Register                                                   | 0xFB4                         |
| PMAUTHSTATUS g                                    | RO     | Authentication Status Register                                         | 0XFB8                         |
| PMDEVARCH g                                       | RO     | Device Architecture Register                                           | 0xFBC                         |
| PMDEVID b                                         | RO     | Performance Monitors Device ID Register                                | 0xFC8                         |
| PMDEVTYPE g                                       | RO     | Device Type Register                                                   | 0xFCC                         |
| PMPIDR4 g PMPIDR0 g PMPIDR1 g PMPIDR2 g PMPIDR3 g | RO     | Peripheral ID registers                                                | 0xFD0 0xFE0 0xFE4 0xFE8 0xFEC |
| PMCIDR0 g PMCIDR1 g g                             | RO     |                                                                        | 0xFF0 0xFF4 0xFF8             |
| PMCIDR2                                           |        | Component ID registers                                                 |                               |

PMDEVID is required regardless of whether FEAT\_PCSRv8p2 is implemented.

Before Armv8.2. the PC Sample-based Profiling Extension can, instead, be implemented in the memory-mapped debug registers space, see The PC Sample-based Profiling Extension.

c. If FEAT\_PMUv3\_SS is implemented, then 0x600 -0x7FC are defined or reserved. Otherwise, these locations are IMPLEMENTATION DEFINED.

d. If any of FEAT\_PMUv3\_TH, FEAT\_PMUv3p8, or FEAT\_PMUv3\_SME is implemented, then 0xA00 -0xAFC are defined or reserved for top halves of the TYPER/FILTR registers. Otherwise, these locations are IMPLEMENTATION DEFINED.

e. If FEAT\_PMUv3p9 is implemented, then the register is 64-bits in the external debug interface to the PMU, even if FEAT\_PMUv3\_EXT64 is not implemented. 64-bit accesses to the registers must be supported, however, these are not required to be atomic at more than a 32-bit granularity. When AllowExternalPMUAccess() == FALSE, the behavior of 32-bit accesses to the top half of these registers is well-defined.

f. OPTIONAL if FEAT\_PMUv3p9 is not implemented. Not permitted if FEAT\_PMUv3p9 is implemented.

g. CoreSight interface registers, see Management registers and CoreSight compliance.

h. The Software lock registers are defined as part of CoreSight compliance, but their contents depend on the type of access that is made and whether the OPTIONAL Software lock is implemented. See the register description for details.