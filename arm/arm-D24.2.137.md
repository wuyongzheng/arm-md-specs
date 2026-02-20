## D24.2.137 MIDR\_EL1, Main ID Register

The MIDR\_EL1 characteristics are:

## Purpose

Provides identification information for the PE, including an implementer code for the device and a device ID number.

## Configuration

AArch64 System register MIDR\_EL1 bits [31:0] are architecturally mapped to AArch32 System register MIDR[31:0].

AArch64 System register MIDR\_EL1 bits [31:0] are architecturally mapped to External register MIDR\_EL1[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to MIDR\_EL1 are UNDEFINED.

## Attributes

MIDR\_EL1 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Implementer, bits [31:24]

The Implementer code. This field must hold an implementer code that has been assigned by Arm.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Implementer   | Meaning                                  |
|---------------|------------------------------------------|
| 0x00          | Reserved for software use.               |
| 0x41          | Arm Limited.                             |
| 0x42          | Broadcom Corporation.                    |
| 0x43          | Cavium Inc.                              |
| 0x44          | Digital Equipment Corporation.           |
| 0x46          | Fujitsu Ltd.                             |
| 0x49          | Infineon Technologies AG.                |
| 0x4D          | Motorola or Freescale Semiconductor Inc. |
| 0x4E          | NVIDIA Corporation.                      |

| Implementer   | Meaning                             |
|---------------|-------------------------------------|
| 0x50          | Applied Micro Circuits Corporation. |
| 0x51          | Qualcomm Inc.                       |
| 0x56          | Marvell International Ltd.          |
| 0x69          | Intel Corporation.                  |
| 0xC0          | Ampere Computing.                   |

Arm can assign codes that are not published in this manual. All values not assigned by Arm are reserved and must not be used.

Access to this field is RO.

## Variant, bits [23:20]

Variant number. Typically, this field is used to distinguish between different product variants, or major revisions of a product.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Architecture, bits [19:16]

Architecture version.

The value of this field is an IMPLEMENTATION DEFINED choice of:

| Architecture   | Meaning                                                                   |
|----------------|---------------------------------------------------------------------------|
| 0b0001         | Armv4.                                                                    |
| 0b0010         | Armv4T.                                                                   |
| 0b0011         | Armv5 (obsolete).                                                         |
| 0b0100         | Armv5T.                                                                   |
| 0b0101         | Armv5TE.                                                                  |
| 0b0110         | Armv5TEJ.                                                                 |
| 0b0111         | Armv6.                                                                    |
| 0b1111         | Architectural features are individually identified in the ID_* registers. |

All other values are reserved.

Access to this field is RO.

## PartNum, bits [15:4]

Primary Part Number for the device.

On processors implemented by Arm, if the top four bits of the primary part number are 0x0 or 0x7 , the variant and architecture are encoded differently.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Revision, bits [3:0]

Revision number for the device.

This field has an IMPLEMENTATION DEFINED value.

Access to this field is RO.

## Accessing MIDR\_EL1

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, MIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.MIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() then X[t, 64] = VPIDR_EL2; else X[t, 64] = MIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = MIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MIDR_EL1;
```