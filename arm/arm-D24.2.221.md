## D24.2.221 VPIDR\_EL2, Virtualization Processor ID Register

The VPIDR\_EL2 characteristics are:

## Purpose

Holds the value of the Virtualization Processor ID. This is the value returned by EL1 reads of MIDR\_EL1.

## Configuration

If EL2 is not implemented, reads of this register return the value of the MIDR\_EL1 and writes to the register are ignored.

This register has no effect if EL2 is not enabled in the current Security state.

AArch64 System register VPIDR\_EL2 bits [31:0] are architecturally mapped to AArch32 System register VPIDR[31:0].

This register is present only when FEAT\_AA64 is implemented. Otherwise, direct accesses to VPIDR\_EL2 are UNDEFINED.

## Attributes

VPIDR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:32]

Reserved, RES0.

## Implementer, bits [31:24]

The Implementer code. This field must hold an implementer code that has been assigned by Arm.

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

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Variant, bits [23:20]

An IMPLEMENTATION DEFINED variant number. Typically, this field is used to distinguish between different product variants, or major revisions of a product.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Architecture, bits [19:16]

Architecture version.

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

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## PartNum, bits [15:4]

An IMPLEMENTATION DEFINED primary part number for the device.

On processors implemented by Arm, if the top four bits of the primary part number are 0x0 or 0x7 , the variant and architecture are encoded differently.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Revision, bits [3:0]

An IMPLEMENTATION DEFINED revision number for the device.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing VPIDR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, VPIDR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x088]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then X[t, 64] = VPIDR_EL2; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then X[t, 64] = MIDR_EL1; else X[t, 64] = VPIDR_EL2;
```

MSR VPIDR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x088] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then VPIDR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then
```

```
if !HaveEL(EL2) then return; else VPIDR_EL2 = X[t, 64];
```

MRS &lt;Xt&gt;, MIDR\_EL1

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b000 | 0b0000 | 0b0000 | 0b000 |

```
if !IsFeatureImplemented(FEAT_AA64) then UnimplementedIDRegister(); elsif PSTATE.EL == EL0 then if IsFeatureImplemented(FEAT_IDST) then if EL2Enabled() && HCR_EL2.TGE == '1' then AArch64.SystemAccessTrap(EL2, 0x18); else AArch64.SystemAccessTrap(EL1, 0x18); else UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_FGT) && (!HaveEL(EL3) || SCR_EL3.FGTEn == '1') && ↪ → HFGRTR_EL2.MIDR_EL1 == '1' then AArch64.SystemAccessTrap(EL2, 0x18); elsif EL2Enabled() then X[t, 64] = VPIDR_EL2; else X[t, 64] = MIDR_EL1; elsif PSTATE.EL == EL2 then X[t, 64] = MIDR_EL1; elsif PSTATE.EL == EL3 then X[t, 64] = MIDR_EL1;
```