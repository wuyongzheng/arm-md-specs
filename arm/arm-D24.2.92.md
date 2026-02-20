## D24.2.92 ID\_AA64MMFR4\_EL1, AArch64 Memory Model Feature Register 4

The ID\_AA64MMFR4\_EL1 characteristics are:

## Purpose

Provides additional information about implemented memory model and memory management support in AArch64.

## Configuration

Note

Prior to the introduction of the features described by this register, this register was unnamed and reserved, RES0 from EL1, EL2, and EL3.

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_AA64MMFR4\_EL1 are UNDEFINED.

## Attributes

ID\_AA64MMFR4\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

| 63       | 63    | 63      | 48 47    | 44 43   | 40 39   | 40 39   | 36 35      | 32         |
|----------|-------|---------|----------|---------|---------|---------|------------|------------|
| RES0     | RES0  | RES0    | RES0     | SRMASK  | RES0    | RES0    | E3DSE RES0 | E3DSE RES0 |
| 31 28 27 | 24 23 | 24 23   | 20 19 16 | 15 12   | 11 8 7  | 11 8 7  | 4 3        | 0          |
| RMEGDI   | E2H0  | NV_frac | FGWTE3   | HACDBS  | ASID2   | EIESB   |            | PoPS       |

## Bits [63:48]

Reserved, RES0.

## SRMASK, bits [47:44]

Indicates support for bitwise write masks for the following registers:

- ACTLR\_EL1.
- CPACR\_EL1.
- SCTLR\_EL1.
- SCTLR2\_EL1.
- TCR\_EL1.
- TCR2\_EL1.
- ACTLR\_EL2.
- CPTR\_EL2.
- SCTLR\_EL2.
- SCTLR2\_EL2.
- TCR\_EL2.
- TCR2\_EL2.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| SRMASK   | Meaning                                                            |
|----------|--------------------------------------------------------------------|
| 0b0000   | Bitwise write masks for the specified registers are not supported. |
| 0b0001   | Bitwise write masks for the specified registers are supported.     |

FEAT\_SRMASK implements the functionality identified by the value 0b0001 .

From Armv9.6, the value 0b0000 is not permitted.

Access to this field is RO.

## Bits [43:40]

Reserved, RES0.

## E3DSE, bits [39:36]

Delegated SError exceptions from EL3. Describes support for delegated SError injection from EL3.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| E3DSE   | Meaning                                                                               |
|---------|---------------------------------------------------------------------------------------|
| 0b0000  | FEAT_E3DSE is not implemented.                                                        |
| 0b0001  | FEAT_E3DSE is implemented. The following are implemented:                             |
|         | • Register fields SCR_EL3.DSE and SCR_EL3.EnDSE. • Registers VSESR_EL3 and VDISR_EL3. |

All other values are reserved.

FEAT\_E3DSE implements the functionality described by the value 0b0001 .

Access to this field is RO.

## Bits [35:32]

Reserved, RES0.

## RMEGDI, bits [31:28]

RMEGranular Data Isolation.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| RMEGDI   | Meaning                                                                                                      |
|----------|--------------------------------------------------------------------------------------------------------------|
| 0b0000   | The Granular Data isolation GPI encodings are reserved.                                                      |
| 0b0001   | The Granular Data Isolation GPI encodings can be configured to be either reserved or No Access from this PE. |

All other values are reserved.

FEAT\_RME\_GDI implements the functionality described by the value 0b0001 .

Access to this field is RO.

## E2H0, bits [27:24]

Indicates support for programming HCR\_EL2.E2H.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| E2H0   | Meaning                                            |
|--------|----------------------------------------------------|
| 0b0000 | FEAT_E2H0 is implemented.                          |
| 0b1110 | FEAT_E2H0 is not implemented. HCR_EL2.NV1 is RES0. |
| 0b1111 | FEAT_E2H0 is not implemented.                      |

All other values are reserved.

If FEAT\_NV is not implemented, then the value 0b1110 is not permitted.

If FEAT\_E2H0 is implemented and FEAT\_VHE is not implemented, then HCR\_EL2.E2H is RES0.

If FEAT\_E2H0 is implemented and FEAT\_VHE is implemented, then HCR\_EL2.E2H can be programmed to 0 or 1.

If FEAT\_E2H0 is not implemented then:

- FEAT\_VHE is implemented.
- HCR\_EL2.E2H is RES1 and behaves as though it is 1.

Access to this field is RO.

## NV\_frac, bits [23:20]

Indicates support for a subset of FEAT\_NV and FEAT\_NV2 behaviors.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| NV_frac   | Meaning                                                                                                      |
|-----------|--------------------------------------------------------------------------------------------------------------|
| 0b0000    | Support for FEAT_NV and FEAT_NV2 is described in ID_AA64MMFR2_EL1.NV.                                        |
| 0b0001    | FEAT_NV and FEAT_NV2 are implemented, but all of the following apply:                                        |
| 0b0010    | As 0b0001 and adds stateful bits in specified _EL1 registers for software usage under nested virtualization. |

FEAT\_NV2p1 implements the functionality indicated by the value 0b0010 .

Access to this field is RO.

## FGWTE3, bits [19:16]

Indicates support for Fine Grained Write Trap EL3 feature.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| FGWTE3   | Meaning                                       |
|----------|-----------------------------------------------|
| 0b0000   | Fine Grained Write Trap EL3 is not supported. |
| 0b0001   | Fine Grained Write Trap EL3 is supported.     |

All other values are reserved.

FEAT\_FGWTE3 implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## HACDBS, bits [15:12]

Support for Hardware accelerator for cleaning Dirty state.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| HACDBS   | Meaning                                                         |
|----------|-----------------------------------------------------------------|
| 0b0000   | Hardware accelerator for cleaning Dirty state is not supported. |
| 0b0001   | Hardware accelerator for cleaning Dirty state is supported.     |

All other values are reserved.

FEAT\_HACDBS implements the functionality identified by the value 0b0001 .

Access to this field is RO.

## ASID2, bits [11:8]

Indicates support for concurrent use of two ASIDs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ASID2   | Meaning                        |
|---------|--------------------------------|
| 0b0000  | FEAT_ASID2 is not implemented. |
| 0b0001  | FEAT_ASID2 is implemented.     |

All other values are reserved.

From Armv9.5, the value 0b0000 is not permitted.

Access to this field is RO.

## EIESB, bits [7:4]

## When FEAT\_IESB is implemented:

Early Implicit Error Synchronization event. Indicates whether the implicit Error synchronization event inserted on taking an exception to ELx when SCTLR\_ELx.IESB is 1 is inserted before or after the exception is taken.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| EIESB   | Meaning                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
|---------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b1111  | FEAT_IESB is implemented. When SError exceptions are routed to EL3, and either FEAT_DoubleFault is not implemented or the Effective value of SCR_EL3.NMEA is 1, an implicit Error synchronization event might be inserted after an exception is taken to EL3.                                                                                                                                                                                                                             |
| 0b0000  | FEAT_IESB is not implemented, or behavior is not described.                                                                                                                                                                                                                                                                                                                                                                                                                               |
| 0b0001  | FEAT_IESB is implemented. When SError exceptions are routed to EL3, and either FEAT_DoubleFault is not implemented or the Effective value of SCR_EL3.NMEA is 1, an implicit Error synchronization event is inserted before an exception taken to EL3.                                                                                                                                                                                                                                     |
| 0b0010  | As 0b0001 , and also: • When SError exceptions are routed to EL1, and either FEAT_DoubleFault2 is not implemented or the Effective value of SCTLR2_EL1.NMEA is 1, an implicit Error synchronization event is inserted before an exception taken to EL1. • When SError exceptions are routed to EL2, and either FEAT_DoubleFault2 is not implemented or the Effective value of SCTLR2_EL2.NMEA is 1, an implicit Error synchronization event is inserted before an exception taken to EL2. |

All other values are reserved.

This field describes the PE behavior on taking an exception to ELx when SCTLR\_ELx.IESB is 1. This field does not describe the behavior when SCTLR\_ELx.IESB is 0.

The behavior described by this field only applies for the conditions described above. For example, if ID\_AA64MMFR4\_EL1.EIESB reads as 0b0001 , then it does not describe the behavior when SError exceptions are not routed to EL3, or when FEAT\_DoubleFault is implemented and the Effective value of SCR\_EL3.NMEA is 0.

Inserting the event before the exception is taken means that if the Error synchronization event causes an SError exception to become pending, and SError exceptions are not masked and not disabled, then the SError exception is taken in place of the original exception.

When FEAT\_IESB is not implemented, the only permitted value of this field is 0b0000 .

Access to this field is RO.

## Otherwise:

Reserved, RES0.

## PoPS, bits [3:0]

Support for the clean and invalidate to the Point of Physical Storage instructions:

- DC CIVAPS .
- If FEAT\_MTE2 is implemented, DC CIGDVAPS .

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PoPS   | Meaning                                                                                                     |
|--------|-------------------------------------------------------------------------------------------------------------|
| 0b0000 | The System instructions to clean and invalidate to the Point of Physical Storage are not implemented.       |
| 0b0001 | The specified System instructions to clean and invalidate to the Point of Physical Storage are implemented. |

FEAT\_PoPS implements the functionality described by the value 0b0001 .

All other values are reserved.

Access to this field is RO.

## Accessing ID\_AA64MMFR4\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, ID\_AA64MMFR4\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0111 | 0b100 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && (IsFeatureImplemented(FEAT_FGT) || !IsZero(ID_AA64MMFR4_EL1) || boolean ↪ → IMPLEMENTATION_DEFINED "ID_AA64MMFR4_EL1 trapped by HCR_EL2.TID3") && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR4_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_AA64MMFR4_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_AA64MMFR4_EL1;
```