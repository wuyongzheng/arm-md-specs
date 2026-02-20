## G8.2.93 ID\_MMFR0, Memory Model Feature Register 0

The ID\_MMFR0 characteristics are:

## Purpose

Provides information about the implemented memory model and memory management support in AArch32 state.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch32 System register ID\_MMFR0 bits [31:0] are architecturally mapped to AArch64 System register ID\_MMFR0\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to ID\_MMFR0 are UNDEFINED.

## Attributes

ID\_MMFR0 is a 32-bit register.

## Field descriptions

| 31       | 28 27   | 24 23   | 20 19   | 16 15    | 12 11    | 8 7   | 4 3   | 0   |
|----------|---------|---------|---------|----------|----------|-------|-------|-----|
| InnerShr | FCSE    | AuxReg  | TCM     | ShareLvl | OuterShr | PMSA  | VMSA  |     |

## InnerShr, bits [31:28]

Innermost Shareability. Indicates the innermost shareability domain implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| InnerShr   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Implemented as Non-cacheable.                |
| 0b0001     | Implemented with hardware coherency support. |
| 0b1111     | Shareability ignored.                        |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 , 0b0001 , and 0b1111 .

This field is valid only if the implementation supports two levels of shareability, as indicated by ID\_MMFR0.ShareLvl having the value 0b0001 .

When ID\_MMFR0.ShareLvl is zero, this field is UNKNOWN.

Access to this field is RO.

## FCSE, bits [27:24]

Indicates whether the implementation includes the FCSE.

The value of this field is an IMPLEMENTATION DEFINED choice of:

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## AuxReg, bits [23:20]

Auxiliary Registers. Indicates support for Auxiliary registers.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| AuxReg   | Meaning                                                                                        |
|----------|------------------------------------------------------------------------------------------------|
| 0b0000   | None supported.                                                                                |
| 0b0001   | Support for Auxiliary Control Register only.                                                   |
| 0b0010   | Support for Auxiliary Fault Status Registers (AIFSR and ADFSR) and Auxiliary Control Register. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0010 .

Note

Accesses to unimplemented Auxiliary registers are UNDEFINED.

Access to this field is RO.

## TCM, bits [19:16]

Indicates support for TCMs and associated DMAs.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| TCM    | Meaning                                       |
|--------|-----------------------------------------------|
| 0b0000 | Not supported.                                |
| 0b0001 | Support is IMPLEMENTATION DEFINED.            |
| 0b0010 | Support for TCMonly, Armv6 implementation.    |
| 0b0011 | Support for TCMand DMA, Armv6 implementation. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

| FCSE   | Meaning           |
|--------|-------------------|
| 0b0000 | Not supported.    |
| 0b0001 | Support for FCSE. |

## ShareLvl, bits [15:12]

Shareability Levels. Indicates the number of shareability levels implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ShareLvl   | Meaning                                 |
|------------|-----------------------------------------|
| 0b0000     | One level of shareability implemented.  |
| 0b0001     | Two levels of shareability implemented. |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0001 .

Access to this field is RO.

## OuterShr, bits [11:8]

Outermost Shareability. Indicates the outermost shareability domain implemented.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| OuterShr   | Meaning                                      |
|------------|----------------------------------------------|
| 0b0000     | Implemented as Non-cacheable.                |
| 0b0001     | Implemented with hardware coherency support. |
| 0b1111     | Shareability ignored.                        |

All other values are reserved.

In Armv8-A, the permitted values are 0b0000 , 0b0001 , and 0b1111 .

Access to this field is RO.

## PMSA, bits [7:4]

Indicates support for a PMSA.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| PMSA   | Meaning                                                                   |
|--------|---------------------------------------------------------------------------|
| 0b0000 | Not supported.                                                            |
| 0b0001 | Support for IMPLEMENTATION DEFINED PMSA.                                  |
| 0b0010 | Support for PMSAv6, with a Cache Type Register implemented.               |
| 0b0011 | Support for PMSAv7, with support for memory subsections. Armv7-R profile. |
| 0b0100 | Support for PMSAv8-32, with base and limit. Armv8-R AArch32 profile.      |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0000 .

Access to this field is RO.

## VMSA, bits [3:0]

Indicates support for a VMSA.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| VMSA   | Meaning                                                                                                       |
|--------|---------------------------------------------------------------------------------------------------------------|
| 0b0000 | Not supported.                                                                                                |
| 0b0001 | Support for IMPLEMENTATION DEFINED VMSA.                                                                      |
| 0b0010 | Support for VMSAv6, with Cache and TLB Type Registers implemented.                                            |
| 0b0011 | Support for VMSAv7, with support for remapping and the Access flag. ARMv7-A profile.                          |
| 0b0100 | As for 0b0011 , and adds support for the PXNbit in the Short-descriptor translation table format descriptors. |
| 0b0101 | As for 0b0100 , and adds support for the Long-descriptor translation table format.                            |

All other values are reserved.

In Armv8-A, the only permitted value is 0b0101 .

Access to this field is RO.

## Accessing ID\_MMFR0

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0001 | 0b100  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HCR_EL2.TID3 == ↪ → '1' then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HCR.TID3 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else R[t] = ID_MMFR0; elsif PSTATE.EL == EL2 then R[t] = ID_MMFR0;
```

```
elsif PSTATE.EL == EL3 then R[t] = ID_MMFR0;
```