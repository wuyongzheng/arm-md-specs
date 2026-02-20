## D24.2.115 ID\_PFR1\_EL1, AArch32 Processor Feature Register 1

The ID\_PFR1\_EL1 characteristics are:

## Purpose

Gives information about the AArch32 programmers' model.

Must be interpreted with ID\_PFR0\_EL1.

For general information about the interpretation of the ID registers see 'Principles of the ID scheme for fields in ID registers'.

## Configuration

AArch64 System register ID\_PFR1\_EL1 bits [31:0] are architecturally mapped to AArch32 System register ID\_PFR1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to ID\_PFR1\_EL1 are UNDEFINED.

## Attributes

ID\_PFR1\_EL1 is a 64-bit register.

## Field descriptions

When FEAT\_AA32 is implemented:

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## GIC, bits [31:28]

System register GIC CPU interface.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GIC    | Meaning                                                                                  |
|--------|------------------------------------------------------------------------------------------|
| 0b0000 | GIC CPU interface system registers not implemented.                                      |
| 0b0001 | System register interface to versions 3.0 and 4.0 of the GIC CPU interface is supported. |
| 0b0011 | System register interface to version 4.1 of the GIC CPU interface is supported.          |

All other values are reserved.

Access to this field is RO.

## Virt\_frac, bits [27:24]

Virtualization fractional field. When the Virtualization field is 0b0000 , determines the support for Virtualization Extensions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Virt_frac   | Meaning                                                                                                                                                                                                                                                  |
|-------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000      | No Virtualization Extensions are implemented.                                                                                                                                                                                                            |
| 0b0001      | The following Virtualization Extensions are implemented:                                                                                                                                                                                                 |
|             | • The SCR.SIF bit, if EL3 is implemented. • The modifications to the SCR.AW and SCR.FW bits described in the Virtualization Extensions, if EL3 is implemented. • The MSR(banked register) and MRS(banked register) instructions. • The ERET instruction. |

## All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 when EL2 is implemented.
- 0b0001 when EL2 is not implemented.

This field is valid only when the value of ID\_PFR1\_EL1.Virtualization is 0, otherwise it holds the value 0b0000 .

Note

The ID\_ISAR registers do not identify whether the instructions added by the Virtualization Extensions are implemented.

Access to this field is RO.

## Sec\_frac, bits [23:20]

Security fractional field. When the Security field is 0b0000 , determines the support for Security Extensions.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Sec_frac   | Meaning                                                                                       |
|------------|-----------------------------------------------------------------------------------------------|
| 0b0000     | No Security Extensions are implemented.                                                       |
| 0b0001     | The following Security Extensions are implemented:                                            |
| 0b0010     | As for 0b0001 , plus the ability to access Secure or Non-secure physical memory is supported. |

All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 when EL3 is implemented.
- 0b0001 or 0b0010 when EL3 is not implemented.

This field is valid only when the value of ID\_PFR1\_EL1.Security is 0, otherwise it holds the value 0b0000 .

Access to this field is RO.

## GenTimer, bits [19:16]

Generic Timer support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| GenTimer   | Meaning                                                                                                                                        |
|------------|------------------------------------------------------------------------------------------------------------------------------------------------|
| 0b0000     | Generic Timer is not implemented.                                                                                                              |
| 0b0001     | Generic Timer is implemented.                                                                                                                  |
| 0b0010     | Generic Timer is implemented, and also includes support for CNTHCTL.EVNTIS and CNTKCTL.EVNTIS fields, and CNTPCTSS and CNTVCTSS counter views. |

All other values are reserved.

FEAT\_ECV implements the functionality identified by the value 0b0010 .

In Armv8.0, the only permitted value is 0b0001 .

From Armv8.6, the only permitted value is 0b0010 .

Access to this field is RO.

## Virtualization, bits [15:12]

Virtualization support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Virtualization   | Meaning                                                                                               |
|------------------|-------------------------------------------------------------------------------------------------------|
| 0b0000           | EL2, Hyp mode, and the HVCinstruction not implemented.                                                |
| 0b0001           | EL2, Hyp mode, the HVCinstruction, and all the features described by Virt_frac == 0b0001 implemented. |

All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 when EL2 is not implemented.
- 0b0001 when EL2 is implemented.

In an implementation that includes EL2, if EL2 cannot use AArch32 but EL1 can use AArch32, then this field has the value 0b0001 .

If EL1 cannot use AArch32, then this field has the value 0b0000 .

|     | Note                                                                |
|-----|---------------------------------------------------------------------|
| The | ID_ISARs do not identify whether the HVCinstruction is implemented. |

Access to this field is RO.

## MProgMod, bits [11:8]

M-profile programmers' model support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| MProgMod   | Meaning                                   |
|------------|-------------------------------------------|
| 0b0000     | Not supported.                            |
| 0b0010     | Support for two-stack programmers' model. |

All other values are reserved.

In Armv8-A the only permitted value is 0b0000 .

Access to this field is RO.

## Security, bits [7:4]

Security support.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Security   | Meaning                                                                                                             |
|------------|---------------------------------------------------------------------------------------------------------------------|
| 0b0000     | EL3, Monitor mode, and the SMCinstruction not implemented.                                                          |
| 0b0001     | EL3, Monitor mode, the SMCinstruction, and all the features described by Sec_frac == 0b0001 implemented.            |
| 0b0010     | As for 0b0001 , and adds the ability to set the NSACR.RFR bit. Not permitted in Armv8 as the NSACR.RFR bit is RES0. |

All other values are reserved.

In Armv8-A, the permitted values are:

- 0b0000 when EL3 is not implemented.
- 0b0001 when EL3 is implemented.

In an implementation that includes EL3, if EL3 cannot use AArch32 but EL1 can use AArch32, then this field has the value 0b0001 .

If EL1 cannot use AArch32, then this field has the value 0b0000 .

Access to this field is RO.

## ProgMod, bits [3:0]

Support for the standard programmers' model for Armv4 and later. Model must support User, FIQ, IRQ, Supervisor, Abort, Undefined, and System modes.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| ProgMod   | Meaning        |
|-----------|----------------|
| 0b0000    | Not supported. |
| 0b0001    | Supported.     |

All other values are reserved.

In Armv8-A, the permitted values are 0b0001 and 0b0000 .

If EL1 cannot use AArch32, then this field has the value 0b0000 .

Access to this field is RO.

## Otherwise:

<!-- image -->

## Bits [63:0]

Reserved, UNKNOWN.

## Accessing ID\_PFR1\_EL1

Accesses to this register use the following encodings in the System register encoding space:

<!-- formula-not-decoded -->

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0001 | 0b001 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif EL2Enabled() && HCR_EL2.TID3 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR1_EL1; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' ↪ → then UNDEFINED; elsif HaveEL(EL3) && IsFeatureImplemented(FEAT_IDTE3) && SCR_EL3.TID3 == '1' then if EL3SDDUndef() then
```

```
UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = ID_PFR1_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = ID_PFR1_EL1;
```