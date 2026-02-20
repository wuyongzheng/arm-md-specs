## D6.4 Trace buffer External mode

## D6.4.1 The external Trace Buffer debug component

RRGHMG

The external Trace Buffer debug component is defined by the external views of all of the following:

- TRBBASER\_EL1.

- TRBIDR\_EL1.

- TRBLIMITR\_EL1.

- TRBMAR\_EL1.

- TRBMPAM\_EL1, if implemented.

- TRBPTR\_EL1.

- TRBSR\_EL1.

- TRBTRG\_EL1.

- Trace Buffer Management Registers, if implemented.

Where applicable, the external views are mapped to the equivalent System registers.

ILSZMG

The Trace Buffer Management Registers are those with offsets ranging from 0xF00 through 0xFFC , as defined by Management registers and CoreSight compliance.

IQSMXY

The external Trace Buffer debug component is a separate component in the external debug interface.

IDCWTT

An external access to a Trace Buffer Unit register might return an error response if one or more of the following apply:

Off

The Core power domain is powered down or is in low-power state where the registers cannot be accessed.

DLK

FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked.

Note

The implementation of FEAT\_DoubleLock in an Armv9 implementation is prohibited.

OSLK

OSLSR\_EL1.OSLK is 0b1 . The OS Lock is locked.

ETBAD

AllowExternalTraceBufferAccess == FALSE for the access. The access is disabled by MDCR\_EL3.ETBAD.

RMXBCY

For reserved accesses to the external Trace Buffer debug component:

- If the Core power domain is powered down or is in a low-power state where the registers cannot be accessed, then the access returns an error response.

- Otherwise:

- For addresses in the range 0xF00 through 0xFFC , the access is RES0H.

- For all other addresses, if any of the following conditions apply, then the access is either RES0H or returns an error response:

DLK

FEAT\_DoubleLock is implemented and DoubleLockStatus() == TRUE. The OS Double Lock is locked.

Note

The implementation of FEAT\_DoubleLock in an Armv9 implementation is prohibited.

OSLK

OSLSR\_EL1.OSLK is 0b1 . The OS Lock is locked.

ETBAD

AllowExternalTraceBufferAccess == FALSE for the access. The access is disabled by MDCR\_EL3.ETBAD.

## Otherwise, the access is RES0H.

IRFYXF

For more information on reserved accesses, see Access requirements for reserved and unallocated registers.

IZTKSS

Table D6-4 shows the external Trace Buffer debug register map.

## Table D6-4 Summary of external Trace Buffer debug registers

| Offset   | Name          | Description                               | Access   |
|----------|---------------|-------------------------------------------|----------|
| 0x000    | TRBBASER_EL1  | Trace Buffer Base Address Register        | RW       |
| 0x008    | TRBPTR_EL1    | Trace Buffer Write Pointer Register       | RW       |
| 0x010    | TRBLIMITR_EL1 | Trace Buffer Limit Address Register       | RW       |
| 0x018    | TRBSR_EL1     | Trace Buffer Status/syndrome Register     | RW       |
| 0x020    | TRBTRG_EL1    | Trace Buffer Trigger Counter Register     | RW       |
| 0x028    | TRBMAR_EL1    | Trace Buffer Memory Attribute Register    | RW       |
| 0x030    | TRBIDR_EL1    | Trace Buffer ID Register                  | RO       |
| 0x038    | TRBCR         | Trace Buffer Control Register             | RW       |
| 0x040    | TRBMPAM_EL1   | Trace Buffer MPAMConfiguration Register   | RW       |
| 0xF00    | TRBITCTRL     | Integration Mode Control Register         | RW       |
| 0xFA8    | TRBDEVAFF     | Device Affinity Register                  | RO       |
| 0xFB0    | TRBLAR        | Lock Access Register                      | WO       |
| 0xFB4    | TRBLSR        | Lock Status Register                      | RO       |
| 0xFB8    | TRBAUTHSTATUS | Authentication Status Register            | RO       |
| 0xFBC    | TRBDEVARCH    | Trace Buffer Device Architecture Register | RO       |
| 0xFC0    | TRBDEVID2     | Device Configuration Register 2           | RO       |
| 0xFC4    | TRBDEVID1     | Device Configuration Register 1           | RO       |
| 0xFC8    | TRBDEVID      | Device Configuration Register             | RO       |
| 0xFCC    | TRBDEVTYPE    | Device Type Register                      | RO       |
| 0xFD0    | TRBPIDR4      | Peripheral Identification Register 4      | RO       |
| 0xFD4    | TRBPIDR5      | Peripheral Identification Register 5      | RO       |
| 0xFD8    | TRBPIDR6      | Peripheral Identification Register 6      | RO       |
| 0xFDC    | TRBPIDR7      | Peripheral Identification Register 7      | RO       |
| 0xFE0    | TRBPIDR0      | Peripheral Identification Register 0      | RO       |
| 0xFE4    | TRBPIDR1      | Peripheral Identification Register 1      | RO       |
| 0xFE8    | TRBPIDR2      | Peripheral Identification Register 2      | RO       |
| 0xFEC    | TRBPIDR3      | Peripheral Identification Register 3      | RO       |
| 0xFF0    | TRBCIDR0      | Component Identification Register 0       | RO       |
| 0xFF4    | TRBCIDR1      | Component Identification Register 1       | RO       |
| 0xFF8    | TRBCIDR2      | Component Identification Register 2       | RO       |
| 0xFFC    | TRBCIDR3      | Component Identification Register 3       | RO       |

## D6.4.2 Behavior in External mode

RDFCSS The rules in this section apply only when the Trace Buffer Unit is enabled and using External mode.

RNHTSY The Base pointer , Limit pointer , and current write pointer are physical addresses.

- RXXFVW TRBMAR\_EL1 defines the memory type, and, as applicable, Cacheability, Shareability, and Device type attributes, and the physical address space for the physical addresses.

RWNCWG The IMPLEMENTATION DEFINED authentication interface controls which physical address spaces can be used.

RCMYYF

If the authentication interface prohibits invasive debug of the Security state corresponding to the physical address space selected by TRBMAR\_EL1.PAS, or TRBMAR\_EL1.PAS is set to a reserved value, then when the Trace Buffer Unit receives trace data from the trace unit, no trace is written to the trace buffer and all of the following occur:

- Atrace buffer management event is generated. This sets TRBSR\_EL1.IRQ to 1.
- If TRBSR\_EL1.S is 0, then all of the following occur:
- -TRBSR\_EL1.S is set to 1, collection is stopped.
- -TRBSR\_EL1.EC is set to 0x00 , other buffer management event.
- -TRBSR\_EL1.BSC is set to 0b000000 , access not allowed .
- The other fields in TRBSR\_EL1 are unchanged.

IPGLYR The trace unit defines the trace prohibited regions.

When the Trace Buffer Unit is using Self-hosted mode, EL3 is always a prohibited region. This is not the case when the Trace Buffer Unit is using External mode.

RWMPMV Awrite of 1 to TRBCR.ManStop generates a trace unit flush, and on completion of the trace unit flush all of the following apply:

- Atrace buffer management event is generated. This sets TRBSR\_EL1.IRQ to 1.
- If TRBSR\_EL1.S is 0, then all of the following occur:
- -TRBSR\_EL1.S is set to 1, collection is stopped.
- -TRBSR\_EL1.EC is set to 0x00 , other buffer management event.
- -TRBSR\_EL1.BSC is set to 0b000011 , Manual Stop event .
- The other fields in TRBSR\_EL1 are unchanged.

After the trace buffer management event is generated:

- The Trace Buffer Unit writes all trace data it has accepted from the trace unit to memory, adding padding data if necessary.
- The current write pointer points to one of the following:
- -If the last trace byte written to the trace buffer was the last byte in the trace buffer, then the Base pointer .
- -Otherwise, the first byte after the last trace byte written to the trace buffer.
- IYBKZD Setting TRBCR.ManStop to 1 has the effects described in RWMPMV even if collection is stopped. Other than a Trigger Event, other trace buffer management events do not guarantee a trace unit flush, and following any other management events, including a Trigger Event, setting TRBCR.ManStop to 1 is required to force the Trace Buffer Unit to write all trace data to memory.
- IKMQKF When stopping trace at the end of a trace session using External mode, software does the following:
1. Stops and disables the trace unit.
2. Sets TRBCR.ManStop to 1.
3. Polls for TRBSR\_EL1.{DAT, S} = {0, 1}.
4. Disables the Trace Buffer Unit.

To ensure the Trace Buffer Unit writes are Complete, the software is required to issue a DSB instruction. This might require an external debugger to halt the PE to execute the instruction. See Cross-halt trigger event.

## D6.4.3 External mode and the Realm Management Extension

RWGMTL

RTYJGF

ILJVQH

IBWDGK

When all of the following are true, each physically addressed access made by the Trace Buffer Unit is subject to Granule Protection Checks:

- FEAT\_RME is implemented.
- The Trace Buffer Unit is using Self-hosted mode or ExternalRootInvasiveDebugEnabled() is FALSE.
- GPCCR\_EL3.GPC is 1.

Otherwise, each physically addressed access made by the Trace Buffer Unit is not subject to Granule Protection Checks.

When all the following are true, the Trace Buffer Unit rejects trace:

- FEAT\_RME is implemented.
- The Trace Buffer Unit is using External mode and ExternalRootInvasiveDebugEnabled() is FALSE.
- GPCCR\_EL3.{TBGPCD, GPC} is {0, 0}.

If FEAT\_RME is implemented, ExternalRootInvasiveDebugEnabled() is FALSE, and the Trace Buffer Unit is using External mode, then on a Warm reset, the PE enters a trace prohibited region and trace remains prohibited until the PE has left Root state and entered a trace allowed region.

GPCCR\_EL3.TBGPCD provides firmware with a control to allow trace to be written to physically addressed memory without Granule Protection Checks even when ExternalRootInvasiveDebugEnabled() is FALSE and the Trace Buffer Unit is using External mode. For example, if the system firmware will not enable Granule Protection Checks. If GPCCR\_EL3.GPC is 1, ExternalRootInvasiveDebugEnabled() is TRUE or the Trace Buffer Unit is using Self-hosted mode, then GPCCR\_EL3.TBGPCD is ignored.

GPCCR\_EL3.TBGPCD is reset to 0 on a Cold reset and preserved on a Warm reset.

## D6.4.4 External mode and MEC

IYPPVQ

RRKSNW defines the interaction of Self-hosted mode and MEC.

RMVPSY

If FEAT\_MEC is implemented and the Trace Buffer Unit is using External mode, then accesses made by the Trace Buffer Unit to the trace buffer use the default MECID of zero.

## D6.4.5 External mode and MPAM

| R SFTXK   | If FEAT_MPAM is implemented, FEAT_TRBE_MPAM is not implemented, and the Trace Buffer Unit is using External mode, then accesses made by the Trace Buffer Unit to the trace buffer use the Default physical PARTID and Default PMGvalues, and the PARTID space corresponding to the trace physical address space defined by TRBMAR_EL1.PAS, regardless of the value of MPAMn_ELx.MPAMEN.                                                                                                                   |
|-----------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| R GJFRD   | If FEAT_MPAM and FEAT_TRBE_MPAM are implemented and the Trace Buffer Unit is using External mode, then accesses made by the Trace Buffer Unit to the trace buffer use one of the following: • If TRBMPAM_EL1.EN is 0, the Default physical PARTID and Default PMGvalues, and the PARTID space corresponding to the trace physical address space defined by TRBMAR_EL1.PAS, regardless of the value of MPAMn_ELx.MPAMEN. • If TRBMPAM_EL1.EN is 1, then the TRBMPAM_EL1.{PARTID, PMG, MPAM_SP} MPAMvalues. |
| I JRQWG   | The external debugger can choose any PARTID and PMGvalues from the selected the MPAM_SP PARTID space.                                                                                                                                                                                                                                                                                                                                                                                                     |
| I QSRZX   | System register access to TRBMPAM_EL1 is also provided, to allow software to save and restore the register over power-down. TRBMPAM_EL1 is not used in Self-hosted mode.                                                                                                                                                                                                                                                                                                                                  |
| R ZXFRR   | The IMPLEMENTATION DEFINED authentication interface controls which MPAM_SP PARTID spaces can be used.                                                                                                                                                                                                                                                                                                                                                                                                     |
| R VVWKG   | If the authentication interface prohibits invasive debug of the Security state corresponding to the MPAM_SP.PARTID space selected by TRBMPAM_EL1.MPAM_SP, or TRBMPAM_EL1.MPAM_SP is set to a reserved value, then when the Trace Buffer Unit receives trace data from the trace unit, no trace is written to the trace buffer and all of the following occur:                                                                                                                                             |

- Atrace buffer management event is generated. This sets TRBSR\_EL1.IRQ to 1.
- If TRBSR\_EL1.S is 0, then all of the following occur:
- -TRBSR\_EL1.S is set to 1, collection is stopped.
- -TRBSR\_EL1.EC is set to 0x00 , other buffer management event.
- -TRBSR\_EL1.BSC is set to 0b000000 , access not allowed .
- The other fields in TRBSR\_EL1 are unchanged.