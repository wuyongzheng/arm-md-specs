## H8.7 Cross-trigger interface registers

The Embedded Cross-Trigger Interface, CTI, is located within its own block of the external debug memory map. There must be one such block for each PE.

If the CTI of a PE does not implement the CTIDEVAFF0 or CTIDEVAFF1 registers it must be located 64KB above the debug registers in the external debug interface.

When FEAT\_Debugv8p4 is implemented, each debug component has a Secure and Non-secure view. The Secure view of a debug component is mapped into Secure physical memory and the Non-secure view of a debug component is mapped into Non-secure memory. Apart from access conditions, the Non-secure and Secure views of the debug components are identical.

Table H8-5 shows the CTI register map.

Table H8-5 Summary of the Embedded Cross-Trigger Interface, CTI, registers

| Offset       | Name             | Description                                          | Access   |
|--------------|------------------|------------------------------------------------------|----------|
| 0x000        | CTICONTROL       | CTI Control register                                 | RW       |
| 0x010        | CTIINTACK        | CTI Output Trigger Acknowledge register              | WO       |
| 0x014        | CTIAPPSET        | CTI Application Trigger Set register                 | RW       |
| 0x018        | CTIAPPCLEAR      | CTI Application Trigger Clear register               | WO       |
| 0x01C        | CTIAPPPULSE      | CTI Application Pulse register                       | WO       |
| 0x020 + (4 * | CTIINEN<n>       | CTI Input Trigger to Output Channel Enable registers | RW       |
| 0x0A0 + (4 * | CTIOUTEN<n>      | CTI Input Channel to Output Trigger Enable registers | RW       |
| 0x130        | CTITRIGINSTATUS  | CTI Trigger In Status register                       | RO       |
| 0x134        | CTITRIGOUTSTATUS | CTI Trigger Out Status register                      | RO       |
| 0x138        | CTICHINSTATUS    | CTI Channel In Status register                       | RO       |
| 0x13C        | CTICHOUTSTATUS   | CTI Channel Out Status register                      | RO       |
| 0x140        | CTIGATE          | CTI Channel Gate Enable register                     | RW       |
| 0x144        | ASICCTL          | CTI External Multiplexer Control register            | RO       |
| 0x150        | CTIDEVCTL        | CTI Device Control register                          | RW       |
| 0xF00        | CTIITCTRL        | CTI Integration mode Control register                | RW       |
| 0xFA0        | CTICLAIMSET      | CTI CLAIM Tag Set register                           | RW       |
| 0xFA4        | CTICLAIMCLR      | CTI CLAIM Tag Clear register                         | RW       |
| 0xFA8        | CTIDEVAFF0       | CTI Device Affinity register 0                       | RO       |
| 0xFAC        | CTIDEVAFF1       | CTI Device Affinity register 1                       | RO       |
| 0xFB0        | CTILAR           | CTI Lock Access Register                             | WO       |
| 0xFB4        | CTILSR           | CTI Lock Status Register                             | RO       |
| 0xFB8        | CTIAUTHSTATUS    | CTI Authentication Status register                   | RO       |
| 0xFBC        | CTIDEVARCH       | CTI Device Architecture register                     | RO       |
| 0xFC0        | CTIDEVID2        | CTI Device ID register 2                             | RO       |
| 0xFC4        | CTIDEVID1        | CTI Device ID register 1                             | RO       |
| 0xFC8        | CTIDEVID         | CTI Device ID register 0                             | RO       |
| 0xFCC        | CTIDEVTYPE       | CTI Device Type register                             | RO       |
| 0xFD0        | CTIPIDR4         | CTI Peripheral Identification Register 4             | RO       |

| Offset   | Name     | Description                              | Access   |
|----------|----------|------------------------------------------|----------|
| 0xFE0    | CTIPIDR0 | CTI Peripheral Identification Register 0 | RO       |
| 0xFE4    | CTIPIDR1 | CTI Peripheral Identification Register 1 | RO       |
| 0xFE8    | CTIPIDR2 | CTI Peripheral Identification Register 2 | RO       |
| 0xFEC    | CTIPIDR3 | CTI Peripheral Identification Register 3 | RO       |
| 0xFF0    | CTICIDR0 | CTI Component Identification Register 0  | RO       |
| 0xFF4    | CTICIDR1 | CTI Component Identification Register 1  | RO       |
| 0xFF8    | CTICIDR2 | CTI Component Identification Register 2  | RO       |
| 0xFFC    | CTICIDR3 | CTI Component Identification Register 3  | RO       |

Table H8-6 shows the access permissions for the CTI registers in an Arm A-profile Debug implementation. For a definition of the terms used, see External debug interface registers.

Table H8-6 Access permissions for the CTI registers

|             |                  | Conditions (priority from left to   | Conditions (priority from left to   | Conditions (priority from left to   | Conditions (priority from left to   | Conditions (priority from left to   | Conditions (priority from left to   | Conditions (priority from left to   |
|-------------|------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|-------------------------------------|
| Offset      | Register         | Domain                              | Off                                 | DLK                                 | OSLK                                | EDAD                                | Default                             | SLK                                 |
| 0x000       | CTICONTROL       | Debug                               | -                                   | -                                   | -                                   | -                                   | RW                                  | RO                                  |
| 0x010       | CTIINTACK        | Debug                               | -                                   | -                                   | -                                   | -                                   | WO                                  | WI                                  |
| 0x014       | CTIAPPSET        | Debug                               | -                                   | -                                   | -                                   | -                                   | RW                                  | RO                                  |
| 0x018       | CTIAPPCLEAR      | Debug                               | -                                   | -                                   | -                                   | -                                   | WO                                  | WI                                  |
| 0x01C       | CTIAPPPULSE      | Debug                               | -                                   | -                                   | -                                   | -                                   | WO                                  | WI                                  |
| 0x020+4 × n | CTIINEN<n>       | Debug                               | -                                   | -                                   | -                                   | -                                   | RW                                  | RO                                  |
| 0x0A0+4 × n | CTIOUTEN<n>      | Debug                               | -                                   | -                                   | -                                   | -                                   | RW                                  | RO                                  |
| 0x130       | CTITRIGINSTATUS  | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0x134       | CTITRIGOUTSTATUS | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0x138       | CTICHINSTATUS    | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0x13C       | CTICHOUTSTATUS   | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0x140       | CTIGATE          | Debug                               | -                                   | -                                   | -                                   | -                                   | RW                                  | RO                                  |
| 0xFC0       | CTIDEVID2        | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0xFC4       | CTIDEVID1        | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |
| 0xFC8       | CTIDEVID         | Debug                               | -                                   | -                                   | -                                   | -                                   | RO                                  | RO                                  |

For the reset values of the CTI registers, see Table H8-8.