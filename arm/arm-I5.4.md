## I5.4 External Activity Monitors Extension registers summary

The memory-mapped interface to the Activity Monitors Extension registers provides read-only access to:

- Read-only copies of the Activity Monitors Extension System registers, with the exception of AMUSERENR.
- An implementation identification register, AMIIDR.
- If they are implemented, the OPTIONAL Activity Monitors CoreSight and ID registers.

The locations of the registers are defined as offsets from a base address. The base address of the memory-mapped view must be aligned to a 4KB boundary, but is otherwise IMPLEMENTATION DEFINED. Activity Monitors external register views defines this memory map.

## I5.4.1 Activity Monitors external register views

The following tables show the external view of the Activity Monitors registers. All implemented registers are RO. Offsets within the 4KB regions not defined in these tables are RAZ/WI.

- Table I5-161 shows the external view of the Activity Monitors registers when FEAT\_AMU\_EXT32 is implemented.
- Table I5-162 shows the external view of the Activity Monitors registers when FEAT\_AMU\_EXT64 is implemented.
- Table I5-163 shows the Peripheral and Component Identification Registers AMPIDR&lt;n&gt;, and AMCIDR&lt;n&gt;. The offsets of these registers are the same in both FEAT\_AMU\_EXT32 and FEAT\_AMU\_EXT64.

Each entry in the Name column links to the register description in Activity Monitors external register descriptions, and:

- If the System register? column of the table shows that the register is a System register, the memory-mapped interface provides a view of the System register described in:
- -Activity Monitors registers, for the AArch64 System register.
- -Activity Monitors registers, for the AArch32 System register.
- Otherwise, the register is accessible only using the external memory-mapped interface.

Table I5-161 Activity Monitors external register views when FEAT\_AMU\_EXT32 is implemented

| Name                                   | Description                                            | System register?   |   Size | Offset            |
|----------------------------------------|--------------------------------------------------------|--------------------|--------|-------------------|
| AMEVCNTR0<n>[31:0] AMEVCNTR0<n>[63:32] | Activity Monitor Event Counter registers 0             | Yes                |     64 | 0x000+8n 0x004+8n |
| AMEVCNTR1<n>[31:0] AMEVCNTR1<n>[63:32] | Activity Monitor Event Counter registers 1             | Yes                |     64 | 0x100+8n 0x104+8n |
| AMEVTYPER0<n>                          | Activity Monitor Event Type registers 0                | Yes                |     32 | 0x400+4n          |
| AMEVTYPER1<n>                          | Activity Monitor Event Type registers 1                | Yes                |     32 | 0x480+4n          |
| AMCNTENSET0                            | Activity Monitors Counter Enable Set register 0        | Yes                |     32 | 0xC00             |
| AMCNTENSET1                            | Activity Monitors Counter Enable Set register 1        | Yes                |     32 | 0xC04             |
| AMCNTENCLR0                            | Activity Monitors Counter Enable Clear register 0      | Yes                |     32 | 0xC20             |
| AMCNTENCLR1                            | Activity Monitors Counter Enable Clear register 1      | Yes                |     32 | 0xC24             |
| AMCGCR                                 | Activity Monitors Counter Group Configuration Register | Yes                |     32 | 0xCE0             |
| AMCFGR                                 | Activity Monitors Configuration Register               | Yes                |     32 | 0xE00             |
| AMCR                                   | Activity Monitors Control Register                     | Yes                |     32 | 0xE04             |

| Name        | Description                                              | System register?   |   Size | Offset   |
|-------------|----------------------------------------------------------|--------------------|--------|----------|
| AMIIDR      | Activity Monitors Implementation Identification Register | No                 |     32 | 0xE08    |
| AMDEVAFF0 a | Device Affinity registers                                | No                 |     32 | 0xFA8    |
| AMDEVAFF1 a |                                                          | No                 |     32 | 0xFAC    |
| AMDEVARCH a | Device Architecture register                             | No                 |     32 | 0xFBC    |
| AMDEVTYPE a | Device Type register                                     | No                 |     32 | 0xFCC    |

Table I5-162 Activity Monitors external register views when FEAT\_AMU\_EXT64 is implemented

| Name               | Description                                              | System register?   |   Size | Offset   |
|--------------------|----------------------------------------------------------|--------------------|--------|----------|
| AMEVCNTR0<n>[63:0] | Activity Monitor Event Counter registers 0               | Yes                |     64 | 0x000+8n |
| AMEVCNTR1<n>[63:0] | Activity Monitor Event Counter registers 1               | Yes                |     64 | 0x100+8n |
| AMEVTYPER0<n>      | Activity Monitor Event Type registers 0                  | Yes                |     64 | 0x400+8n |
| AMEVTYPER1<n>      | Activity Monitor Event Type registers 1                  | Yes                |     64 | 0x500+8n |
| AMCNTENSET         | Activity Monitors Counter Enable Set register            | Yes                |     64 | 0xC00    |
| AMCNTEN            | Activity Monitors Counter Enable register                | Yes                |     64 | 0xC10    |
| AMCNTENCLR         | Activity Monitors Counter Enable Clear register          | Yes                |     64 | 0xC20    |
| AMCGCR             | Activity Monitors Counter Group Configuration Register   | Yes                |     64 | 0xCE0    |
| AMCFGR             | Activity Monitors Configuration Register                 | Yes                |     64 | 0xE00    |
| AMIIDR             | Activity Monitors Implementation Identification Register | No                 |     64 | 0xE08    |
| AMCR               | Activity Monitors Control Register                       | Yes                |     64 | 0xE10    |
| AMDEVAFF a         | Device Affinity registers                                | No                 |     64 | 0xFA8    |
| AMDEVARCH a        | Device Architecture register                             | No                 |     32 | 0xFBC    |
| AMDEVTYPE a        | Device Type register                                     | No                 |     32 | 0xFCC    |

Table I5-163 Activity Monitors external register views of Peripheral and Component Identification Registers

| Name      | Description             | System register?   |   Size | Offset   |
|-----------|-------------------------|--------------------|--------|----------|
| AMPIDR4 a | Peripheral ID registers | No                 |     32 | 0xFD0    |
| AMPIDR0 a | Peripheral ID registers | No                 |     32 | 0xFE0    |
| AMPIDR1 a | Peripheral ID registers | No                 |     32 | 0xFE4    |
| AMPIDR2 a | Peripheral ID registers | No                 |     32 | 0xFE8    |
| AMPIDR3 a | Peripheral ID registers | No                 |     32 | 0xFEC    |
| AMCIDR0 a | Component ID registers  | No                 |     32 | 0xFF0    |
| AMCIDR1 a | Component ID registers  | No                 |     32 | 0xFF4    |

| Name      | Description   | System register?   |   Size | Offset   |
|-----------|---------------|--------------------|--------|----------|
| AMCIDR2 a |               | No                 |     32 | 0xFF8    |
| AMCIDR3 a |               | No                 |     32 | 0xFFC    |