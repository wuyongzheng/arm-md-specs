## D24.2.89 ID\_AA64MMFR1\_EL1, AArch64 Memory Model Feature Register 1

The ID\_AA64MMFR1\_EL1 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch64 state.

For general information about the interpretation of the ID registers, see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64MMFR1\_EL1 are UNDEFINED.

## Attributes

ID\_AA64MMFR1\_EL1 is a 64-bit register.

## Field descriptions

| 63    | 60 59   | 56 55   | 52 51   | 48 47   | 44 43   | 40 39   | 36 35    |      | 32     |
|-------|---------|---------|---------|---------|---------|---------|----------|------|--------|
| ECBHB | CMOW    | TIDCP1  | nTLBPA  | AFP     | HCX     |         | ETS      | TWED |        |
| 31    | 28 27   | 24 23   | 20 19   | 16 15   | 12      | 11 8    | 7        | 4 3  | 0      |
| XNX   |         | SpecSEI | PAN     | LO      | HPDS    | VH      | VMIDBits |      | HAFDBS |

## ECBHB, bits [63:60]

Indicates support for restrictions on branch history speculation around exceptions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ECBHB   | Meaning                                                                                                                |
|---------|------------------------------------------------------------------------------------------------------------------------|
| 0b0000  | The implementation does not disclose whether restrictions are imposed on branch history speculation around exceptions. |
| 0b0001  | The implementation imposes restrictions on branch history speculation around exceptions.                               |

All other values are reserved.

FEAT\_ECBHB implements the functionality identified by the value 0b0001 .

From Armv8.9, the value 0b0000 is not permitted.

Access to this field is RO.

## CMOW,bits [59:56]

Indicates support for cache maintenance instruction permission.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| CMOW   | Meaning                                                                                                      |
|--------|--------------------------------------------------------------------------------------------------------------|
| 0b0000 | SCTLR_EL1.CMOW, SCTLR_EL2.CMOW, and HCRX_EL2.CMOW bits are not implemented.                                  |
| 0b0001 | SCTLR_EL1.CMOW is implemented. If EL2 is implemented, SCTLR_EL2.CMOW and HCRX_EL2.CMOW bits are implemented. |

All other values are reserved.

FEAT\_CMOWimplements the functionality identified by the value 0b0001 .

From Armv8.8, the value 0b0000 is not permitted.

Access to this field is RO.

## TIDCP1, bits [55:52]

Indicates whether SCTLR\_EL1.TIDCP and SCTLR\_EL2.TIDCP are implemented in AArch64 state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TIDCP1   | Meaning                                                                                        |
|----------|------------------------------------------------------------------------------------------------|
| 0b0000   | SCTLR_EL1.TIDCP and SCTLR_EL2.TIDCP bits are not implemented and are RES0.                     |
| 0b0001   | SCTLR_EL1.TIDCP bit is implemented. If EL2 is implemented, SCTLR_EL2.TIDCP bit is implemented. |

All other values are reserved.

FEAT\_TIDCP1 implements the functionality identified by the value 0b0001 .

From Armv8.8, the value 0b0000 is not permitted.

Access to this field is RO.

## nTLBPA, bits [51:48]

Indicates support for intermediate caching of translation table walks.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| nTLBPA   | Meaning                                                                                                        |
|----------|----------------------------------------------------------------------------------------------------------------|
| 0b0000   | The intermediate caching of translation table walks might include non-coherent physical translation caches.    |
| 0b0001   | The intermediate caching of translation table walks does not include non-coherent physical translation caches. |

Non-coherent physical translation caches are non-coherent caches of previous valid translation table entries since the last completed relevant TLBI applicable to the PE, where either:

- The caching is indexed by the physical address of the location holding the translation table entry.
- The caching is used for stage 1 translations and is indexed by the intermediate physical address of the location holding the translation table entry.

All other values are reserved.

FEAT\_nTLBPA implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## AFP, bits [47:44]

Indicates support for FPCR.{AH, FIZ, NEP}.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AFP    | Meaning                                           |
|--------|---------------------------------------------------|
| 0b0000 | The FPCR.{AH, FIZ, NEP} fields are not supported. |
| 0b0001 | The FPCR.{AH, FIZ, NEP} fields are supported.     |

All other values are reserved.

FEAT\_AFP implements the functionality identified by the value 0b0001 .

From Armv8.7, if Advanced SIMD and floating-point is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## HCX, bits [43:40]

Indicates support for HCRX\_EL2 and its associated EL3 trap.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HCX    | Meaning                                                 |
|--------|---------------------------------------------------------|
| 0b0000 | HCRX_EL2 and its associated EL3 trap are not supported. |
| 0b0001 | HCRX_EL2 and its associated EL3 trap are supported.     |

All other values are reserved.

FEAT\_HCX implements the functionality identified by the value 0b0001 .

From Armv8.7, if EL2 is implemented, the value 0b0000 is not permitted.

Access to this field is RO.

## ETS, bits [39:36]

Indicates support for Enhanced Translation Synchronization.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ETS    | Meaning                                                |
|--------|--------------------------------------------------------|
| 0b0000 | Enhanced Translation Synchronization is not supported. |
| 0b0001 | Enhanced Translation Synchronization is not supported. |
| 0b0010 | FEAT_ETS2 is implemented.                              |
| 0b0011 | FEAT_ETS3 is implemented.                              |

All other values are reserved.

FEAT\_ETS2 implements the functionality identified by the value 0b0010 .

FEAT\_ETS3 implements the functionality identified by the value 0b0011 .

From Armv8.8, the values 0b0000 and 0b0001 are not permitted.

From Armv9.5, the value 0b0010 is not permitted.

Access to this field is RO.

## TWED,bits [35:32]

Indicates support for the configurable delayed trapping of WFE and WFET.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TWED   | Meaning                                                        |
|--------|----------------------------------------------------------------|
| 0b0000 | Configurable delayed trapping of WFEand WFETare not supported. |
| 0b0001 | Configurable delayed trapping of WFEand WFETare supported.     |

All other values are reserved.

FEAT\_TWED implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## XNX, bits [31:28]

Indicates support for execute-never control distinction by Exception level at stage 2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| XNX    | Meaning                                                                         |
|--------|---------------------------------------------------------------------------------|
| 0b0000 | Distinction between EL0 and EL1 execute-never control at stage 2 not supported. |
| 0b0001 | Distinction between EL0 and EL1 execute-never control at stage 2 supported.     |

All other values are reserved.

FEAT\_XNX implements the functionality identified by the value 0b0001 .

From Armv8.2, the value 0b0000 is not permitted.

Access to this field is RO.

## SpecSEI, bits [27:24]

## When FEAT\_RAS is implemented:

Describes whether the PE can generate SError exceptions from speculative reads of memory, including speculative instruction fetches.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SpecSEI   | Meaning                                                                                    |
|-----------|--------------------------------------------------------------------------------------------|
| 0b0000    | The PE never generates an SError exception due to an External abort on a speculative read. |
| 0b0001    | The PE might generate an SError exception due to an External abort on a speculative read.  |

All other values are reserved.

FEAT\_SpecSEI implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## PAN, bits [23:20]

Privileged Access Never. Indicates support for the PAN bit in PSTATE, SPSR\_EL1, SPSR\_EL2, SPSR\_EL3, and DSPSR\_EL0.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PAN    | Meaning                                                                                                              |
|--------|----------------------------------------------------------------------------------------------------------------------|
| 0b0000 | PAN not supported.                                                                                                   |
| 0b0001 | PAN supported.                                                                                                       |
| 0b0010 | PAN supported and AT S1E1RP and AT S1E1WP instructions supported.                                                    |
| 0b0011 | PAN supported, AT S1E1RP and AT S1E1WP instructions supported, and SCTLR_EL1.EPAN and SCTLR_EL2.EPAN bits supported. |

All other values are reserved.

FEAT\_PAN implements the functionality identified by the value 0b0001 .

FEAT\_PAN2 implements the functionality added by the value 0b0010 .

FEAT\_PAN3 implements the functionality added by the value 0b0011 .

From Armv8.1, the value 0b0000 is not permitted.

From Armv8.2, the value 0b0001 is not permitted.

From Armv8.7, the value 0b0010 is not permitted.

Access to this field is RO.

## LO, bits [19:16]

LORegions. Indicates support for LORegions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| LO     | Meaning                  |
|--------|--------------------------|
| 0b0000 | LORegions not supported. |

All other values are reserved.

FEAT\_LOR implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## HPDS, bits [15:12]

Hierarchical Permission Disables. Indicates support for disabling hierarchical controls in translation tables.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HPDS   | Meaning                                                                                                                                                                     |
|--------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000 | Disabling of hierarchical controls not supported.                                                                                                                           |
| 0b0001 | Disabling of hierarchical controls supported with the TCR_EL1.{HPD1, HPD0}, TCR_EL2.HPD or TCR_EL2.{HPD1, HPD0}, and TCR_EL3.HPD bits.                                      |
| 0b0010 | As for value 0b0001 , and adds possible hardware allocation of bits[62:59] of the Translation table descriptors from the final lookup level for IMPLEMENTATION DEFINED use. |

All other values are reserved.

FEAT\_HPDS implements the functionality identified by the value 0b0001 .

FEAT\_HPDS2 implements the functionality identified by the value 0b0010 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## VH, bits [11:8]

Virtualization Host Extensions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VH     | Meaning                                       |
|--------|-----------------------------------------------|
| 0b0000 | Virtualization Host Extensions not supported. |
| 0b0001 | Virtualization Host Extensions supported.     |

All other values are reserved.

FEAT\_VHE implements the functionality identified by the value 0b0001 .

From Armv8.1, the value 0b0000 is not permitted.

Access to this field is RO.

## VMIDBits, bits [7:4]

Number of VMID bits.

| LO     | Meaning              |
|--------|----------------------|
| 0b0001 | LORegions supported. |

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMIDBits   | Meaning   |
|------------|-----------|
| 0b0000     | 8 bits    |
| 0b0010     | 16 bits   |

All other values are reserved.

FEAT\_VMID16 implements the functionality identified by the value 0b0010 .

Access to this field is RO.

## HAFDBS, bits [3:0]

Hardware updates to Access flag and Dirty state in translation tables.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HAFDBS   | Meaning                                                                                    |
|----------|--------------------------------------------------------------------------------------------|
| 0b0000   | Hardware update of the Access flag and dirty state are not supported.                      |
| 0b0001   | Support for hardware update of the Access flag for Block and Page descriptors.             |
| 0b0010   | As 0b0001 , and adds support for hardware update of dirty state.                           |
| 0b0011   | As 0b0010 , and adds support for hardware update of the Access flag for Table descriptors. |
| 0b0100   | As 0b0011 , and adds support for hardware tracking of Dirty state Structure.               |

## All other values are reserved.

FEAT\_HAFDBS implements the functionality identified by the values 0b0001 and 0b0010 .

FEAT\_HAFT implements the functionality identified by the value 0b0011 .

FEAT\_HDBSS implements the functionality identified by the value 0b0100 .

Access to this field is RO.

## Accessing ID\_AA64MMFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0111 | 0b001 |

if !IsFeatureImplemented(FEAT\_AA64) then

```
UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then
```

if IsFeatureImplemented(FEAT\_IDST) then

```
if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64MMFR1_EL1;
```