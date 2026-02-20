## G8.2.113 MIDR, Main ID Register

The MIDR characteristics are:

## Purpose

Provides identification information for the PE, including an implementer code for the device and a device ID number.

## Configuration

Some fields of the MIDR are IMPLEMENTATION DEFINED. For more information about the values of these fields for a particular Armv8 implementation, and any implementation-specific significance of these values, see the product documentation.

AArch32 System register MIDR bits [31:0] are architecturally mapped to AArch64 System register MIDR\_EL1[31:0].

AArch32 System register MIDR bits [31:0] are architecturally mapped to External register MIDR\_EL1[31:0].

This register is present only when FEAT\_AA32EL1 is implemented. Otherwise, direct accesses to MIDR are UNDEFINED.

## Attributes

MIDR is a 32-bit register.

## Field descriptions

<!-- image -->

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
| 0x50          | Applied Micro Circuits Corporation.      |
| 0x51          | Qualcomm Inc.                            |

| Implementer   | Meaning                    |
|---------------|----------------------------|
| 0x56          | Marvell International Ltd. |
| 0x69          | Intel Corporation.         |
| 0xC0          | Ampere Computing.          |

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

## Accessing MIDR

Accesses to this register use the following encodings in the System register encoding space:

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = VPIDR_EL2<31:0>; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t] = VPIDR; else R[t] = MIDR; elsif PSTATE.EL == EL2 then R[t] = MIDR; elsif PSTATE.EL == EL3 then R[t] = MIDR;
```