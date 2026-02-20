## H8.6 External debug interface registers

The external debug interface register map is described by:

- Summary of external debug registers.
- Cross-trigger interface registers.
- Performance Monitors external register views.

## Table H8-2 Summary of external debug registers

| Offset      | Name          | Description                                         | Access   |
|-------------|---------------|-----------------------------------------------------|----------|
| 0x020       | EDESR         | External Debug Event Status Register                | RW       |
| 0x024       | EDECR         | External Debug Execution Control Register           | RW       |
| 0x028       | EDSCR2        | External Debug Status and Control Register 2        | RW       |
| 0x030       | EDWAR         | External Debug Watchpoint Address Register          | RO       |
| 0x038       | EDHSR         | External Debug Halting Syndrome Register            | RO       |
| 0x080       | DBGDTRRX_EL0  | Debug Data Transfer Register, Receive               | RW       |
| 0x084       | EDITR         | External Debug Instruction Transfer Register        | WO       |
| 0x088       | EDSCR         | External Debug Status and Control Register          | RW       |
| 0x08C       | DBGDTRTX_EL0  | Debug Data Transfer Register, Transmit              | RW       |
| 0x090       | EDRCR         | External Debug Reserve Control Register             | WO       |
| 0x094       | EDACR         | External Debug Auxiliary Control Register           | RW       |
| 0x098       | EDECCR        | External Debug Exception Catch Control Register     | RW       |
| 0x0A0       | EDPCSR        | External Debug Program Counter Sample Register      | RO       |
| 0x0A0       | EDPCSR        | External Debug Program Counter Sample Register      | RO       |
| 0x0A4       | EDCIDSR       | External Debug Context ID Sample Register           | RO       |
| 0x0A8       | EDVIDSR       | External Debug Virtual Context Sample Register      | RO       |
| 0x0AC       | EDPCSR        | External Debug Program Counter Sample Register      | RO       |
| 0x0AC       | EDPCSR        | External Debug Program Counter Sample Register      | RO       |
| 0x300       | OSLAR_EL1     | OS Lock Access Register                             | WO       |
| 0x310       | EDPRCR        | External Debug Power/Reset Control Register         | RW       |
| 0x314       | EDPRSR        | External Debug Processor Status Register            | RO       |
| 0x400 + (16 | DBGBVR<n>_EL1 | Debug Breakpoint Value Registers                    | RW       |
| 0x408 + (16 | DBGBCR<n>_EL1 | Debug Breakpoint Control Registers                  | RW       |
| 0x800 + (16 | DBGWVR<n>_EL1 | Debug Watchpoint Value Registers                    | RW       |
| 0x808 + (16 | DBGWCR<n>_EL1 | Debug Watchpoint Control Registers                  | RW       |
| 0xD00       | MIDR_EL1      | Main ID Register                                    | RO       |
| 0xD20       | EDPFR         | External Debug Processor Feature Register           | RO       |
| 0xD28       | EDDFR         | External Debug Feature Register                     | RO       |
| 0xD48       | EDDFR1        | External Debug Feature Register 1                   | RO       |
| 0xD60       | EDAA32PFR     | External Debug Auxiliary Processor Feature Register | RO       |
| 0xF00       | EDITCTRL      | External Debug Integration mode Control register    | RW       |

| Offset   | Name              | Description                                         | Access   |
|----------|-------------------|-----------------------------------------------------|----------|
| 0xFA0    | DBGCLAIMSET_EL1   | Debug CLAIM Tag Set Register                        | RW       |
| 0xFA4    | DBGCLAIMCLR_EL1   | Debug CLAIM Tag Clear Register                      | RW       |
| 0xFA8    | EDDEVAFF0         | External Debug Device Affinity register 0           | RO       |
| 0xFAC    | EDDEVAFF1         | External Debug Device Affinity register 1           | RO       |
| 0xFB0    | EDLAR             | External Debug Lock Access Register                 | WO       |
| 0xFB4    | EDLSR             | External Debug Lock Status Register                 | RO       |
| 0xFB8    | DBGAUTHSTATUS_EL1 | Debug Authentication Status Register                | RO       |
| 0xFBC    | EDDEVARCH         | External Debug Device Architecture Register         | RO       |
| 0xFC0    | EDDEVID2          | External Debug Device ID register 2                 | RO       |
| 0xFC4    | EDDEVID1          | External Debug Device ID Register 1                 | RO       |
| 0xFC8    | EDDEVID           | External Debug Device ID register 0                 | RO       |
| 0xFCC    | EDDEVTYPE         | External Debug Device Type register                 | RO       |
| 0xFD0    | EDPIDR4           | External Debug Peripheral Identification Register 4 | RO       |
| 0xFE0    | EDPIDR0           | External Debug Peripheral Identification Register 0 | RO       |
| 0xFE4    | EDPIDR1           | External Debug Peripheral Identification Register 1 | RO       |
| 0xFE8    | EDPIDR2           | External Debug Peripheral Identification Register 2 | RO       |
| 0xFEC    | EDPIDR3           | External Debug Peripheral Identification Register 3 | RO       |
| 0xFF0    | EDCIDR0           | External Debug Component Identification Register 0  | RO       |
| 0xFF4    | EDCIDR1           | External Debug Component Identification Register 1  | RO       |
| 0xFF8    | EDCIDR2           | External Debug Component Identification Register 2  | RO       |
| 0xFFC    | EDCIDR3           | External Debug Component Identification Register 3  | RO       |

## H8.6.1 Access permissions for the External debug interface registers

Table H8-3 and Table H8-4 show the access permissions for the external debug interface registers in an Arm A-profile Debug implementation. The terms are defined as follows:

## Domain

## Conditions

This describes the power domain in which the register is logically implemented. Registers described as implemented in the Core power domain might be implemented in the Debug power domain, as long as they exhibit the required behavior.

If FEAT\_DoPD is implemented, most External debug interface registers are in the Core power domain, as shown in Table H8-3.

If FEAT\_DoPD is not implemented, most of the registers are in the Debug Power Domain, as shown in Table H8-4.

This lists the conditions under which the access is attempted.

To determine the access permissions for a register, read these columns from left to right, and stop at first column that lists the condition as being true.

The conditions are:

## Off

The Core power domain is completely off, or in low-power state. In these cases the Core power domain registers cannot be accessed, and if FEAT\_DoPD is not implemented, EDPRSR.PU will read as 0.

Note

When the Core power domain is off, or in a low-power state, a debugger is permitted to access a debug register that is implemented in the external Debug power domain. When the Debug power domain is off, all accesses to the registers in the external Debug power domain return an error.

| DLK     | FEAT_DoubleLock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked. If FEAT_DoPD is implemented, FEAT_DoubleLock is not implemented and so Table H8-3 does not include this column.                                                                                                                                                                                                                   |
|---------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OSLK    | OSLSR.OSLK == 1. The OS Lock is locked.                                                                                                                                                                                                                                                                                                                                                                                        |
| EDAD    | AllowExternalDebugAccess() == FALSE. External debug access is disabled for the access. See also Behavior of a not permitted access.                                                                                                                                                                                                                                                                                            |
| EPMAD   | AllowExternalPMUAccess() == FALSE. Access to the external Performance Monitors is disabled for the access. See also Behavior of a not permitted access.                                                                                                                                                                                                                                                                        |
| SLK     | The Software Lock is implemented and SoftwareLockStatus() == TRUE. This provides the modified default access permissions for OPTIONAL memory-mapped accesses to the external debug interface if the OPTIONAL Software Lock is locked for the access. See Register access permissions for memory-mapped accesses. If FEAT_DoPD is implemented, the Software Lock is not locked or not implemented, then this column is ignored. |
| Default | This provides the default access permissions, if there are no conditions that prevent access to the register.                                                                                                                                                                                                                                                                                                                  |

The access permissions are:

| -      | This means that the default access permission applies. See the Default column, or the SLK column, if applicable.                                                                     |
|--------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| RO     | This means that the register or field is read-only, and:                                                                                                                             |
| RW     | This means that the register or field is read/write. Individual fields within the register might be ROor WO. See the relevant register description for details.                      |
| RC     | This means that a read of the register bit clears the field to 0.                                                                                                                    |
| WO     | This means that the register or field is write-only. Unless the register description states otherwise, a WOfield in a RWregister returns an UNKNOWN value on a read of the register. |
| WI     | This means that the register or field ignores writes.                                                                                                                                |
| IMPDEF | This means that the access permissions are IMPLEMENTATION DEFINED.                                                                                                                   |

DBGBVR&lt;n&gt;\_EL1 and DBGWVR&lt;n&gt;\_EL1, and if FEAT\_Debugv8p9 is implemented, DBGBCR&lt;n&gt;\_EL1 and DBGWCR&lt;n&gt;\_EL1, are 64-bit registers mapped to pairs of 32-bit locations in the external debug interface. Doubleword accesses to these register are not guaranteed to be 64-bit single copy atomic. Software must take care before altering the values of DBGBVR&lt;n&gt;\_EL1, DBGWVR&lt;n&gt;\_EL1, DBGBCR&lt;n&gt;\_EL1, and DBGWCR&lt;n&gt;\_EL1 to prevent UNPREDICTABLE behavior. See Endianness and supported access sizes for more information.

If FEAT\_Debugv8p9 is not implemented, DBGBCR&lt;n&gt;\_EL1 and DBGWCR&lt;n&gt;\_EL1 are 32-bit registers in the external debug interface, and accesses to DBGBCR&lt;n&gt;\_EL1[63:32] and DBGWCR&lt;n&gt;\_EL1[63:32] are RES0.

If OPTIONAL memory-mapped access to the external debug interface is supported, there might be additional constraints on memory-mapped accesses. See Register access permissions for memory-mapped accesses.

For the reset values for the external debug interface registers, see Table H8-7.

## Table H8-3 Access permissions for the external debug interface registers if FEAT\_DoPD is implemented

|                       |                                                | Domain         | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   |         |
|-----------------------|------------------------------------------------|----------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|---------|
| Offset                | Register                                       |                | Off                                        | OSLK                                       | EDAD                                       | Default |
| 0x020                 | EDESR                                          | Core           | Error                                      | -                                          | -                                          | RW      |
| 0x024                 | EDECR                                          | Core           | Error                                      | -                                          | -                                          | RW      |
| 0x028                 | EDSCR2                                         | Core           | Error                                      | Error                                      | -                                          | RW      |
| 0x030 0x034           | EDWAR[31:0] EDWAR[63:32]                       | Core Core      | Error Error                                | Error Error                                | - -                                        | RO RO   |
| 0x038 0x03C           | EDHSR[31:0] EDHSR[63:32]                       | Core Core      | Error Error                                | Error Error                                | - -                                        | RO RO   |
| 0x080                 | DBGDTRRX_EL0                                   | Core           | Error                                      | Error                                      | -                                          | RW      |
| 0x084                 | EDITR                                          | Core           | Error                                      | Error                                      | -                                          | WO      |
| 0x088                 | EDSCR                                          | Core           | Error                                      | Error                                      | -                                          | RW      |
| 0x08C                 | DBGDTRTX_EL0                                   | Core           | Error                                      | Error                                      | -                                          | RW      |
| 0x090                 | EDRCR                                          | Core           | Error                                      | Error                                      | -                                          | WO      |
| 0x094                 | EDACR                                          | Core           | Error                                      | IMP DEF                                    | -                                          | RW      |
| 0x098                 | EDECCR                                         | Core           | Error                                      | Error                                      | -                                          | RW      |
| 0x0A0                 | EDPCSR[31:0] a                                 | Core           | Error                                      | Error                                      | -                                          | RO      |
| 0x0A4                 | EDCIDSR a                                      | Core           | Error                                      | Error                                      | -                                          | RO      |
| 0x0A8                 | EDVIDSR a                                      | Core           | Error Error                                | Error                                      | - -                                        | RO      |
| 0x0AC                 | EDPCSR[63:32] a                                | Core           |                                            | Error                                      |                                            | RO      |
| 0x300                 | OSLAR_EL1                                      | Core           | Error                                      | -                                          | Error                                      | WO      |
| 0x310                 | EDPRCR                                         | Core           | Error                                      | -                                          | -                                          | RW      |
| 0x408+16*n 0x40C+16*n | DBGBCR<n>_EL1[31:0] b DBGBCR<n>_EL1[63:32] b,c | Core Core      | Error Error                                | Error Error                                | Error Error                                | RW RW   |
| 0x800+16*n 0x804+16*n | DBGWVR<n>_EL1[31:0] b DBGWVR<n>_EL1[63:32] b   | Core           | Error Error                                | Error                                      | Error Error                                | RW RW   |
| 0x808+16*n 0x80C+16*n | DBGWCR<n>_EL1[31:0] b DBGWCR<n>_EL1[63:32] b,c | Core Core Core | Error Error                                | Error Error Error                          | Error Error                                | RW RW   |
| 0xD00                 | MIDR_EL1                                       | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD20                 | EDPFR[31:0]                                    | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD24                 | EDPFR[63:32]                                   | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD28                 | EDDFR[31:0]                                    | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD2C                 |                                                | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD48                 | EDDFR[63:32] EDDFR1[31:0]                      | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD4C                 | EDDFR1[63:32]                                  | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD60                 | EDAA32PFR[31:0]                                | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xD64                 | EDAA32PFR[63:32]                               | Core           | Error                                      | -                                          | -                                          | RO      |
| 0xFA0                 | DBGCLAIMSET_EL1                                | Core           | Error                                      | Error                                      | -                                          | RW      |

|        |                   | Domain   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   |         |
|--------|-------------------|----------|--------------------------------------------|--------------------------------------------|--------------------------------------------|---------|
| Offset | Register          |          | Off                                        | OSLK                                       | EDAD                                       | Default |
| 0xFA4  | DBGCLAIMCLR_EL1   | Core     | Error                                      | Error                                      | -                                          | RW      |
| 0xFA8  | EDDEVAFF0         | Core     | Error                                      | -                                          | -                                          | RO      |
| 0xFAC  | EDDEVAFF1         | Core     | Error                                      | -                                          | -                                          | RO      |
| 0xFB8  | DBGAUTHSTATUS_EL1 | Core     | Error                                      | -                                          | -                                          | RO      |
| 0xFC0  | EDDEVID2          | Core     | Error                                      | -                                          | -                                          | RO      |
| 0xFC4  | EDDEVID1          | Core     | Error                                      | -                                          | -                                          | RO      |
| 0xFC8  | EDDEVID           | Core     | Error                                      | -                                          | -                                          | RO      |

Table H8-4 Access permissions for the external debug interface registers if FEAT\_DoPD is not implemented

|                       |                                              | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   |
|-----------------------|----------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Offset                | Register                                     | Domain                                     | Off                                        | DLK                                        | OSLK                                       | EDAD                                       | Default                                    | SLK                                        |
| 0x020                 | EDESR                                        | Core                                       | Error                                      | Error                                      | -                                          | -                                          | RW                                         | RO                                         |
| 0x024                 | EDECR                                        | Debug                                      | -                                          | -                                          | -                                          | -                                          | RW                                         | RO                                         |
| 0x028                 | EDSCR2                                       | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0x030 0x034           | EDWAR[31:0] EDWAR[63:32]                     | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | - -                                        | RO RO                                      | - -                                        |
| 0x038 0x03C           | EDHSR[31:0] EDHSR[63:32]                     | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | - -                                        | RO RO                                      | RO RO                                      |
| 0x080                 | DBGDTRRX_EL0                                 | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0x084                 | EDITR                                        | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | WO                                         | WI                                         |
| 0x088                 | EDSCR                                        | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0x08C                 | DBGDTRTX_EL0 EDRCR                           | Core                                       | Error Error                                | Error Error                                | Error                                      | -                                          | RW WO                                      | RO WI                                      |
| 0x090                 |                                              | Core                                       |                                            |                                            | Error                                      | -                                          |                                            |                                            |
| 0x094                 | EDACR                                        | IMP DEF                                    | IMP DEF                                    | IMP DEF                                    | IMP DEF                                    | -                                          | RW                                         | RO                                         |
| 0x098                 | EDECCR                                       | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0x0A0                 | EDPCSR[31:0] a                               | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RO                                         | RO                                         |
| 0x0A4                 | EDCIDSR a                                    | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RO                                         | RO                                         |
| 0x0A8                 | EDVIDSR a                                    | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RO                                         | RO                                         |
| 0x0AC                 | EDPCSR[63:32]                                | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RO                                         | RO                                         |
| 0x300                 | OSLAR_EL1                                    | Core                                       | Error                                      | Error                                      | -                                          | IMP DEF b                                  | WO                                         | WI                                         |
| 0x310                 | EDPRCR                                       | Core and Debug c                           | -                                          | -                                          | -                                          | -                                          | RW                                         | RO                                         |
| 0x314                 | EDPRSR                                       | Core and Debug c                           | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0x400+16*n 0x404+16*n | DBGBVR<n>_EL1[31:0] d DBGBVR<n>_EL1[63:32] d | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | Error Error                                | RW RW                                      | RO RO                                      |

|                       |                                                | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   | Conditions (priority from left to right)   |
|-----------------------|------------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|--------------------------------------------|
| Offset                | Register                                       | Domain                                     | Off                                        | DLK                                        | OSLK                                       | EDAD                                       | Default                                    | SLK                                        |
| 0x408+16*n 0x40C+16*n | DBGBCR<n>_EL1[31:0] d DBGBCR<n>_EL1[63:32] d,e | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | Error Error                                | RW RW                                      | RO RO                                      |
| 0x800+16*n 0x804+16*n | DBGWVR<n>_EL1[31:0] d DBGWVR<n>_EL1[63:32] d   | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | Error Error                                | RW RW                                      | RO RO                                      |
| 0x808+16*n 0x80C+16*n | DBGWCR<n>_EL1[31:0] d DBGWCR<n>_EL1[63:32] d,e | Core Core                                  | Error Error                                | Error Error                                | Error Error                                | Error Error                                | RW RW                                      | RO RO                                      |
| 0xD00                 | MIDR_EL1                                       | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD20                 | EDPFR[31:0]                                    | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD24                 | EDPFR[63:32]                                   | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD28                 | EDDFR[31:0]                                    | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD2C                 | EDDFR[63:32]                                   | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD48                 | EDDFR1[31:0]                                   | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD48                 | EDDFR1[63:32]                                  | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD60                 | EDAA32PFR[31:0]                                | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xD64                 | EDAA32PFR[63:32]                               | IMP DEF                                    | IMP DEF f                                  | IMP DEF f                                  | -                                          | -                                          | RO                                         | RO                                         |
| 0xFA0                 | DBGCLAIMSET_EL1                                | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0xFA4                 | DBGCLAIMCLR_EL1                                | Core                                       | Error                                      | Error                                      | Error                                      | -                                          | RW                                         | RO                                         |
| 0xFA8                 | EDDEVAFF0                                      | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0xFAC                 | EDDEVAFF1                                      | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0xFB8                 | DBGAUTHSTATUS_EL1                              | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0xFC0                 | EDDEVID2                                       | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0xFC4                 | EDDEVID1                                       | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |
| 0xFC8                 | EDDEVID                                        | Debug                                      | -                                          | -                                          | -                                          | -                                          | RO                                         | RO                                         |

b. If FEAT\_Debugv8p2 is not implemented, it is IMPLEMENTATION DEFINED whether an error is returned. See External access disabled. If no error is returned, the access is permitted.

c. Some bits are in the Debug power domain and some bits are in the Core power domain. See register field descriptions for information.

d. Implemented breakpoints and watchpoints only. n is the breakpoint or watchpoint number.

e. When FEAT\_Debugv8p9 is implemented.

f. It is IMPLEMENTATION DEFINED whether an error is returned. See External debug over powerdown and locks. If no error is returned, the access is permitted.