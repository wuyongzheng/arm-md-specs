## K5.4 Management registers and CoreSight compliance

The CoreSight architecture requires the implementation of a set of management registers that occupy the memory map from 0xF00 upwards in each of the debug components.

CoreSight compliance and complete implementation of the management registers is OPTIONAL, but Arm recommends that the registers are implemented.

The CoreSight architecture specification recommends that any integration test registers are implemented starting from 0xEFC downwards. Each of the debug components has an IMPLEMENTATION DEFINED region from 0xE80 to 0xEFC for this purpose.

## K5.4.1 CoreSight interface register map

Table K5-4 shows the external management register maps for the following registers:

| ED   | These are the external debug register.           |
|------|--------------------------------------------------|
| CTI  | These are the Cross-trigger interface registers. |
| PMU  | These are the Performance Monitors registers.    |

## Table K5-4 CoreSight interface register map

| Offset      | Mnemonic ED         | CTI           | PMU          | Name                                |
|-------------|---------------------|---------------|--------------|-------------------------------------|
| 0xF00       | EDITCTRL            | CTIITCTRL     | PMITCTRL     | Integration Model Control registers |
| 0xF04-0xF9C | -                   | -             | -            | Reserved, RES0                      |
| 0xFA0       | DBGCLAIMSET_EL1 a   | CTICLAIMSET b | -            | CLAIM Tag Set registers             |
| 0xFA4       | DBGCLAIMCLR_EL1 a   | CTICLAIMCLR b | -            | CLAIM Tag Clear registers           |
| 0xFA8       | EDDEVAFF0 a         | CTIDEVAFF0 c  | PMDEVAFF0    | Device Affinity registers           |
| 0xFAC       | EDDEVAFF1 a         | CTIDEVAFF1 c  | PMDEVAFF1    |                                     |
| 0xFB0       | EDLAR d             | CTILAR d      | PMLAR d      | Lock Access register                |
| 0xFB4       | EDLSR d             | CTILSR d      | PMLSR d      | Lock Status register                |
| 0XFB8       | DBGAUTHSTATUS_EL1 a | CTIAUTHSTATUS | PMAUTHSTATUS | Authentication Status register      |
| 0xFBC       | EDDEVARCH           | CTIDEVARCH    | PMDEVARCH    | Device Architecture register        |
| 0xFC0       | EDDEVID2 a          | CTIDEVID2 a   | -            | Device ID register                  |
| 0xFC4       | EDDEVID1 a          | CTIDEVID1 a   | -            |                                     |
| 0xFC8       | EDDEVID a           | CTIDEVID a    | PMDEVID a,e  |                                     |
| 0xFCC       | EDDEVTYPE           | CTIDEVTYPE    | PMDEVTYPE    | Device Type register                |
| 0xFD0       | EDPIDR4             | CTIPIDR4      | PMPIDR4      | Peripheral ID registers             |
| 0xFD4-0xFDC | -                   | -             | -            | Reserved, RES0                      |
| 0xFE0       | EDPIDR0             | CTIPIDR0      | PMPIDR0      | Peripheral ID registers             |
| 0xFE4       | EDPIDR1             | CTIPIDR1      | PMPIDR1      |                                     |
| 0xFE8       | EDPIDR2             | CTIPIDR2      | PMPIDR2      |                                     |
| 0xFEC       | EDPIDR3             | CTIPIDR3      | PMPIDR3      |                                     |
| 0xFF0       | EDCIDR0             | CTICIDR0      | PMCIDR0      | Component ID registers              |
| 0xFF4       | EDCIDR1             | CTICIDR1      | PMCIDR1      |                                     |

| Offset   | Mnemonic   | CTI      |         |
|----------|------------|----------|---------|
|          | ED         |          | PMU     |
| 0xFF8    | EDCIDR2    | CTICIDR2 | PMCIDR2 |
| 0xFFC    | EDCIDR3    | CTICIDR3 | PMCIDR3 |

## K5.4.2 Management register access permissions

Access to the OPTIONAL Integration Control register (ITCTRL) is IMPLEMENTATION DEFINED.

Table K5-5, Table K5-6, Table K5-7, Table K5-8, and Table K5-9 show the response to accesses by the external debug interface to the CoreSight management registers.

Note

Access to the CoreSight management registers is not affected by the values of EDAD and EPMAD.

Table K5-5, Table K5-6, Table K5-7, Table K5-8, and Table K5-9 include reserved management registers, because the CoreSight architecture requires that these registers are always RES0. The descriptions in Reserved and unallocated registers do not apply to reserved management registers if the implementation is CoreSight compliant.

If OPTIONAL memory-mapped access to the external debug interface is supported, there are additional constraints on memory-mapped accesses. See Register access permissions for memory-mapped accesses.

When FEAT\_Debugv8p4 is implemented, each debug component has a Secure and Non-secure view. The Secure view of a debug component is mapped into Secure physical memory and the Non-secure view of a debug component is mapped into Non-secure memory. Apart from access conditions, the Non-secure and Secure views of the debug components are identical.

The terms in Table K5-5, Table K5-6, Table K5-7, Table K5-8, and Table K5-9 are defined as follows:

## Domain

Conditions

This describes the power domain in which the register is logically implemented. Registers described as implemented in the Core power domain might be implemented in the Debug power domain, as long as they exhibit the required behavior.

If FEAT\_DoPD is implemented, most External debug interface registers are in the Core power domain, as shown in Table K5-5 and Table K5-8.

If FEAT\_DoPD is not implemented, most of the registers are in the Debug Power Domain, as shown in Table K5-6 and Table K5-9.

This lists the conditions under which the access is attempted.

To determine the access permissions for a register, read these columns from left to right, and stop at first column that lists the condition as being true.

The conditions are:

## Off

EDPRSR.PU == 0. The Core power domain is completely off, or in low-power state. In these cases, the Core power domain registers cannot be accessed.

Note

When the Debug power domain is off, all accesses to the registers in the external Debug power domain return an error.

DLK

If the OS Double Lock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked.

OSLK

OSLSR.OSLK == 1. The OS Lock is locked.

Default

This provides the default access permissions, if there are no conditions that prevent access to the register.

SLK

This provides the modified default access permissions for OPTIONAL memory-mapped accesses to the external debug interface if the OPTIONAL Software Lock is locked. See Register access permissions for memory-mapped accesses. If FEAT\_DoPD is implemented, the Software Lock is not locked, or not implemented, this column is ignored.

## The access permissions are:

- This means that the default access permission applies. See the Default column, or the SLK column, if applicable.

- RO

This means that the register or field is read-only.

- RW This means that the register or field is read/write. Individual fields within the register might be RO. See the relevant register description for details.

- RC This means that the bit clears to 0 after a read.

- (SE) This means that accesses to this register have indirect write side effects. A side effect occurs when a direct read or a direct write of a register creates an indirect write to the same register or to another register.

- WO

This means that the register or field is write-only.

- WI

This means that the register or field ignores writes.

IMP DEF

This means that the access permissions are IMPLEMENTATION DEFINED.

Table K5-5 External debug interface access permissions, CoreSight registers (debug) if FEAT\_DoPD is implemented

| Offset      | Register          | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   |
|-------------|-------------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|
|             |                   |          | Off                                   | DLK                                   | OSLK                                  |           |
| 0xF00       | EDITCTRL          | IMP DEF  | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMP DEF   |
| 0xF04-0xF8C | Reserved          |          | -                                     | -                                     | -                                     | RES0      |
| 0xFA0       | DBGCLAIMSET_EL1   | Core     | Error                                 | Error                                 | Error                                 | RW(SE)    |
| 0xFA4       | DBGCLAIMCLR_EL1   | Core     | Error                                 | Error                                 | Error                                 | RW(SE)    |
| 0xFA8       | EDDEVAFF0         | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFAC       | EDDEVAFF1         | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFB0       | EDLAR             | Core     | Error                                 | -                                     | -                                     | WO(SE)    |
| 0xFB4       | EDLSR             | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFB8       | DBGAUTHSTATUS_EL1 | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFBC       | EDDEVARCH         | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFC0       | EDDEVID2          | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFC4       | EDDEVID1          | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFC8       | EDDEVID           | Core     | Error                                 | -                                     | -                                     | RO        |

| Offset      | Register   | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   |
|-------------|------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|
| Offset      | Register   | Domain   | Off                                   | DLK                                   | OSLK                                  | Default   |
| 0xFCC       | EDDEVTYPE  | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFD0       | EDPIDR4    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFD4-0xFDC | Reserved   |          | -                                     | -                                     | -                                     | RES0      |
| 0xFE0-0xFEC | EDPIDR0    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFE4       | EDPIDR1    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFE8       | EDPIDR2    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFEC       | EDPIDR3    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF0       | EDCIDR0    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF4       | EDCIDR1    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF8       | EDCIDR2    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFFC       | EDCIDR3    | Core     | Error                                 | -                                     | -                                     | RO        |

Table K5-6 External debug interface access permissions, CoreSight registers (debug) if FEAT\_DoPD is not implemented

| Offset      | Register          | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   | SLK   |
|-------------|-------------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|-------|
|             |                   |          | Off                                   | DLK                                   | OSLK                                  |           |       |
| 0xF00       | EDITCTRL          | IMP DEF  | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMP DEF   | RO/WI |
| 0xF04-0xF8C | Reserved          | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFA0       | DBGCLAIMSET_EL1   | Core     | Error                                 | Error                                 | Error                                 | RW(SE)    | RO    |
| 0xFA4       | DBGCLAIMCLR_EL1   | Core     | Error                                 | Error                                 | Error                                 | RW(SE)    | RO    |
| 0xFA8       | EDDEVAFF0         | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFAC       | EDDEVAFF1         | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB0       | EDLAR             | Debug    | -                                     | -                                     | -                                     | WO(SE)    | -     |
| 0xFB4       | EDLSR             | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB8       | DBGAUTHSTATUS_EL1 | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFBC       | EDDEVARCH         | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC0       | EDDEVID2          | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC4       | EDDEVID1          | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC8       | EDDEVID           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFCC       | EDDEVTYPE         | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD0       | EDPIDR4           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD4-0xFDC | Reserved          | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFE0-0xFEC | EDPIDR0           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE4       | EDPIDR1           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE8       | EDPIDR2           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFEC       | EDPIDR3           | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF0       | EDCIDR0           | Debug    | -                                     | -                                     | -                                     | RO        | -     |

| Offset   | Register   | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   | SLK   |
|----------|------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|-------|
|          |            |          | Off                                   | DLK                                   | OSLK                                  |           |       |
| 0xFF4    | EDCIDR1    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF8    | EDCIDR2    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFFC    | EDCIDR3    | Debug    | -                                     | -                                     | -                                     | RO        | -     |

Table K5-7 External debug interface access permissions, CoreSight registers (CTI)

| Offset      | Register      | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   | SLK   |
|-------------|---------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|-------|
|             |               |          | Off                                   | DLK                                   | OSLK                                  |           |       |
| 0xF00       | CTIITCTRL     | IMP DEF  | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMP DEF   | RO/WI |
| 0xF04-0xF8C | Reserved      | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFA0       | CTICLAIMSET   | Debug    | -                                     | -                                     | -                                     | RW(SE)    | RO    |
| 0xFA4       | CTICLAIMCLR   | Debug    | -                                     | -                                     | -                                     | RW(SE)    | RO    |
| 0xFA8       | CTIDEVAFF0    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFAC       | CTIDEVAFF1    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB0       | CTILAR        | Debug    | -                                     | -                                     | -                                     | WO(SE)    | -     |
| 0xFB4       | CTILSR        | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB8       | CTIAUTHSTATUS | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFBC       | CTIDEVARCH    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC0       | CTIDEVID2     | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC4       | CTIDEVID1     | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC8       | CTIDEVID      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFCC       | CTIDEVTYPE    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD0       | CTIPIDR4      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD4-0xFDC | Reserved      | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFE0       | CTIPIDR0      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE4       | CTIPIDR1      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE8       | CTIPIDR2      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFEC       | CTIPIDR3      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF0       | CTICIDR0      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF4       | CTICIDR1      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF8       | CTICIDR2      | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFFC       | CTICIDR3      | Debug    | -                                     | -                                     | -                                     | RO        | -     |

Table K5-8 External debug interface access permissions, CoreSight registers (PMU) if FEAT\_DoPD is implemented

| Offset      | Register     | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   |
|-------------|--------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|
|             |              |          | Off                                   | DLK                                   | OSLK                                  |           |
| 0xF00       | PMITCTRL     | IMP DEF  | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMP DEF   |
| 0xF04-0xFA4 | Reserved     |          | -                                     | -                                     | -                                     | RES0      |
| 0xFA8       | PMDEVAFF0    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFAC       | PMDEVAFF1    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFB0       | PMLAR        | Core     | Error                                 | -                                     | -                                     | WO(SE)    |
| 0xFB4       | PMLSR        | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFB8       | PMAUTHSTATUS | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFBC       | PMDEVARCH    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFC0-0xFC4 | Reserved     |          | -                                     | -                                     | -                                     | RES0      |
| 0xFC8       | PMDEVID a    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFCC       | PMDEVTYPE    | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFD0       | PMPIDR4      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFD4-0xFDC | Reserved     |          | -                                     | -                                     | -                                     | RES0      |
| 0xFE0       | PMPIDR0      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFE4       | PMPIDR1      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFE8       | PMPIDR2      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFEC       | PMPIDR3      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF0       | PMCIDR0      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF4       | PMCIDR1      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFF8       | PMCIDR2      | Core     | Error                                 | -                                     | -                                     | RO        |
| 0xFFC       | PMCIDR3      | Core     | Error                                 | -                                     | -                                     | RO        |

Table K5-9 External debug interface access permissions, CoreSight registers (PMU) if FEAT\_DoPD is not implemented

| Offset      | Register     | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   | SLK   |
|-------------|--------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|-------|
|             |              |          | Off                                   | DLK                                   | OSLK                                  |           |       |
| 0xF00       | PMITCTRL     | IMP DEF  | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMPLEMENTATION DEFINED                | IMP DEF   | RO/WI |
| 0xF04-0xFA4 | Reserved     | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFA8       | PMDEVAFF0    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFAC       | PMDEVAFF1    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB0       | PMLAR        | Debug    | -                                     | -                                     | -                                     | WO(SE)    | -     |
| 0xFB4       | PMLSR        | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFB8       | PMAUTHSTATUS | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFBC       | PMDEVARCH    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFC0-0xFC4 | Reserved     | Debug    | -                                     | -                                     | -                                     | RES0      | -     |

| Offset      | Register   | Domain   | Conditions (priority left to right)   | Conditions (priority left to right)   | Conditions (priority left to right)   | Default   | SLK   |
|-------------|------------|----------|---------------------------------------|---------------------------------------|---------------------------------------|-----------|-------|
| Offset      | Register   | Domain   | Off                                   | DLK                                   | OSLK                                  | Default   | SLK   |
| 0xFC8       | PMDEVID a  | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFCC       | PMDEVTYPE  | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD0       | PMPIDR4    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFD4-0xFDC | Reserved   | Debug    | -                                     | -                                     | -                                     | RES0      | -     |
| 0xFE0       | PMPIDR0    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE4       | PMPIDR1    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFE8       | PMPIDR2    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFEC       | PMPIDR3    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF0       | PMCIDR0    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF4       | PMCIDR1    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFF8       | PMCIDR2    | Debug    | -                                     | -                                     | -                                     | RO        | -     |
| 0xFFC       | PMCIDR3    | Debug    | -                                     | -                                     | -                                     | RO        | -     |

## K5.4.3 Management register resets

Table K5-10 shows the management register resets. This table does not include:

- Read-only identification registers that have a fixed value from reset. These registers include those with the DEVAFFn, DEVARCH, DEVID{n}, DEVTYPE, PIDRn, and CIDRn mnemonics.
- Registers that have the AUTHSTATUS mnemonic. This is a read-only status register that reflects the status outside of the reset domain of the register.
- Registers that have the LAR mnemonic. These are write-only registers that only have an effect on writes.

All other fields in the management registers are reset to an IMPLEMENTATION DEFINED value which can be UNKNOWN. The registers are in the reset domain specified in the table.

Table K5-10 shows a summary of the management register resets.

Table K5-10 Management register resets

| Register                    | Reset domain                                                                | Field   | Value       | Description             |
|-----------------------------|-----------------------------------------------------------------------------|---------|-------------|-------------------------|
| CTIITCTRL EDITCTRL PMITCTRL | IMPLEMENTATION DEFINED                                                      | IME     | 0           | Integration mode enable |
| DBGCLAIMCLR_EL1             | Cold reset                                                                  | CLAIM   | 0x00        | CLAIM tags              |
| CTICLAIMCLR                 | External debug                                                              | CLAIM   | 0x0000_0000 | CLAIM tags              |
| CTILSR a EDLSR a PMLSR a    | If FEAT_DoPD is implemented, reset by Cold reset, otherwise External debug. | SLK     | 1           | Software Lock           |

a. Only if the OPTIONAL Software Lock is implemented

## K5.4.4 About the Peripheral identification scheme

The Peripheral Identification scheme provides the standard information required by all components that conform to the Arm ® Debug Interface Architecture Specification, ADIv5.0 to ADIv5.2 , that implements the CoreSight identification scheme. They identify a peripheral in a particular namespace. For more information, see the Arm ® CoreSight™ Architecture Specification .

Table K5-11 lists the Peripheral ID Registers that make up the Peripheral Identification scheme for each component.

Table K5-11 Peripheral Identification Registers

| Register offset   | Description                 | Reference External Debug   | CTI      | Performance Monitors   |
|-------------------|-----------------------------|----------------------------|----------|------------------------|
| 0xFD0             | Peripheral ID4              | EDPIDR4                    | CTIPIDR4 | PMPIDR4                |
| 0xFD4             | Reserved for Peripheral ID5 | -                          | -        | -                      |
| 0xFD8             | Reserved for Peripheral ID6 | -                          | -        | -                      |
| 0xFDC             | Reserved for Peripheral ID7 | -                          | -        | -                      |
| 0xFE0             | Peripheral ID0              | EDPIDR0                    | CTIPIDR0 | PMPIDR0                |
| 0xFE4             | Peripheral ID1              | EDPIDR1                    | CTIPIDR1 | PMPIDR1                |
| 0xFE8             | Peripheral ID2              | EDPIDR2                    | CTIPIDR2 | PMPIDR2                |
| 0xFEC             | Peripheral ID3              | EDPIDR3                    | CTIPIDR3 | PMPIDR3                |

Figure K5-2 shows the register field allocation scheme for the Peripheral ID Registers.

Figure K5-2 Peripheral ID register format

<!-- image -->

Software can consider the eight Peripheral ID Registers as defining a single 64-bit Peripheral ID, as shown in Figure K5-3.

Figure K5-3 Mapping between Peripheral ID Registers and a 64-bit Peripheral ID Value

<!-- image -->

Figure K5-4 shows the fields in the 64-bit Peripheral ID value, and includes the field values for fields that:

- Have fixed values, including the bits that are reserved.
- Have fixed values in an implementation that is designed by Arm.

For more information about the fields and their values, see Table K5-12.

Figure K5-4 Peripheral ID fields, with values for a implementation designed by ARM

<!-- image -->

Table K5-12 shows the fields in the Peripheral ID.

## Table K5-12 Fields in the Peripheral Identification Registers

| Name                | Size     | Description                                                                                                                                                                                                                                                                                | Registers                                                                        |
|---------------------|----------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------------------------------|
| 4KB count           | 4 bits   | Log2 of the number of 4KB blocks occupied by the implementation.                                                                                                                                                                                                                           | EDPIDR4 CTIPIDR4 PMPIDR4                                                         |
| JEP106 code         | 4+7 bits | Identifies the designer of the implementation. This value consists of: • A4-bit continuation code, also described as the bank number. • A7-bit identification code. For implementations designed by Arm, the continuation code is 0x4 , indicating bank 5, and the identity code is 0x3B . | EDPIDR1, EDPIDR2, EDPIDR4 CTIPIDR1, CTIPIDR2, CTIPIDR4 PMPIDR1, PMPIDR2, PMPIDR4 |
| RevAnd              | 4 bits   | Manufacturing revision number. Indicates a late modification to the implementation, usually as a result of an Engineering Change Order (ECO). This field starts at 0x0 and is incremented by the integrated circuit manufacturer on metal fixes.                                           | EDPIDR3 CTIPIDR3 PMPIDR3                                                         |
| Customer modified   | 4 bits   | Indicates an endorsed modification to the implementation. If the system designer cannot modify the implementation supplied by the implementation designer, then this field is RES0.                                                                                                        | EDPIDR3 CTIPIDR3 PMPIDR3                                                         |
| Revision            | 4 bits   | Revision number for the implementation. Starts at 0x0 and increments by 1 at both major and minor revisions.                                                                                                                                                                               | EDPIDR2 CTIPIDR2 PMPIDR2                                                         |
| Uses JEP106 ID code | 1 bit    | This bit is set to 1 when a JEP106 identification code is used. This bit must be 1 on all Arm implementations from the introduction of Armv8 onwards.                                                                                                                                      | EDPIDR2 CTIPIDR2 PMPIDR2                                                         |
| Part number         | 12 bits  | Part number for the implementation. Each organization designing to the Arm Debug architecture specification keeps its own part number list.                                                                                                                                                | EDPIDR0, EDPIDR1 CTIPIDR0, CTIPIDR1 PMPIDR0, PMPIDR1                             |

Acomponent is identified uniquely by the combination of the following fields:

- JEP106 continuation code.
- JEP106 identity code.
- Part number.
- Revision.
- Customer Modified.
- RevAnd.

For components with a Component class of 0x9 , Debug component, indicated by the Component Identification Registers, multiple components can have the same Part number, provided each component has a different CoreSight Device type . However, Arm strongly recommends that each device has a unique Part number. For more information:

- About the Component Identification Registers, see About the Component Identification scheme.
- About the CoreSight Device type, see EDDEVTYPE, CTIDEVTYPE, or PMDEVTYPE.
- About CoreSight components and their identification, see the Arm ® Debug Interface Architecture Specification .

## K5.4.4.1 Allocating revisions and part numbers

Within the Peripheral Identification registers, the allocation of major and minor revisions, part numbers, and customer-modified fields is IMPLEMENTATION DEFINED, with the following set of restrictions so that:

- The REVISION field must increase monotonically with revisions.

Note

Arm recommends that the REVISION field is updated for each update to the RTL, regardless of whether this is a major or minor update.

- The REVAND field should increase monotonically with revisions.

Note

Arm recommends that the REVAND field is used only for post-release changes. For example, those due to engineering change order (ECO) fixes related to the debug component of the processor.

- The PART field must have a degree of uniqueness:
- -Two component designs can have the same part number so long as they are sub-components of the same part and the programmers' model for the part has the means to disambiguate sub-components.
- -Otherwise, two component designs must have unique part numbers.

The DEVARCH (if implemented) or DEVTYPE (otherwise) register provides the means to disambiguate sub-components of the Debug Architecture.

AROMtable has no DEVTYPE or DEVARCH register. However, if it is the only CLASS 0x1 component in a processor cluster, it can still be disambiguated.

Multiple instances of the same component design have the same part number.

## K5.4.5 About the Component Identification scheme

The Component Identification Registers identify the processor as an Arm Debug Interface v5 component. For more information, see the Arm ® Debug Interface Architecture Specification and the Arm ® CoreSight™ Architecture Specification .

The Component Identification Registers occupy the last four words of the 4KB block of debug registers.

Table K5-13 Component Identification Registers

| Register offset   | Description   | External debug   | CTI      | Performance Monitors   | Trace    |
|-------------------|---------------|------------------|----------|------------------------|----------|
| 0xFF0             | Component ID0 | EDCIDR0          | CTICIDR0 | PMCIDR0                | TRBCIDR0 |
| 0xFF4             | Component ID1 | EDCIDR1          | CTICIDR1 | PMCIDR1                | TRBCIDR1 |

Figure K5-5 shows the register field allocation scheme for the Component ID Registers.

| Register offset   | Description   | External debug   | CTI      | Performance Monitors   | Trace    |
|-------------------|---------------|------------------|----------|------------------------|----------|
| 0xFF8             | Component ID2 | EDCIDR2          | CTICIDR2 | PMCIDR2                | TRBCIDR2 |
| 0xFFC             | Component ID3 | EDCIDR3          | CTICIDR3 | PMCIDR3                | TRBCIDR3 |

Figure K5-5 Component ID Register format

<!-- image -->

Software can consider the eight Component ID Registers as defining a single 32-bit Component ID, as shown in Figure K5-6.

Figure K5-6 Mapping between Component ID Registers and a 32-bit Component ID Value

<!-- image -->

## Appendix K6 Additional Information for Implementations of the Generic Timer

This appendix gives additional information about implementations of the Generic Timer. It contains the following sections:

- Providing a complete set of features in a system level implementation.
- Gray count scheme for timer distribution scheme.