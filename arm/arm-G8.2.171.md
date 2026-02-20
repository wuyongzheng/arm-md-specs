## G8.2.171 VPIDR, Virtualization Processor ID Register

The VPIDR characteristics are:

## Purpose

Holds the value of the Virtualization Processor ID. This is the value returned by Non-secure EL1 reads of MIDR.

## Configuration

If EL2 is not implemented but EL3 is implemented, this register takes the value of the MIDR.

AArch32 System register VPIDR bits [31:0] are architecturally mapped to AArch64 System register VPIDR\_EL2[31:0].

This register is present only when FEAT\_AA32EL2 is implemented. Otherwise, direct accesses to VPIDR are UNDEFINED.

## Attributes

VPIDR is a 32-bit register.

## Field descriptions

<!-- image -->

| 31          | 24 23   | 20 19        | 16 15   | 4 3      |
|-------------|---------|--------------|---------|----------|
| Implementer | Variant | Architecture | PartNum | Revision |

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
| 0x50          | Applied Micro Circuits Corporation.      |
| 0x51          | Qualcomm Inc.                            |
| 0x56          | Marvell International Ltd.               |
| 0x69          | Intel Corporation.                       |
| 0xC0          | Ampere Computing.                        |

Arm can assign codes that are not published in this manual. All values not assigned by Arm are reserved and must not be used.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MIDR.Implementer.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Variant, bits [23:20]

An IMPLEMENTATION DEFINED variant number. Typically, this field is used to distinguish between different product variants, or major revisions of a product.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MIDR.Variant.
- Otherwise, this field resets to an architecturally UNKNOWN value.

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

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MIDR.Architecture.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## PartNum, bits [15:4]

An IMPLEMENTATION DEFINED primary part number for the device.

On processors implemented by Arm, if the top four bits of the primary part number are 0x0 or 0x7 , the variant and architecture are encoded differently.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MIDR.PartNum.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Revision, bits [3:0]

An IMPLEMENTATION DEFINED revision number for the device.

The reset behavior of this field is:

- On a Warm reset:
- When the highest implemented Exception level is EL3 or the highest implemented Exception level is EL2, this field resets to the value in MIDR.Revision.
- Otherwise, this field resets to an architecturally UNKNOWN value.

## Accessing VPIDR

Accesses to this register use the following encodings in the System register encoding space:

```
MRC{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then R[t] = VPIDR; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then R[t] = MIDR; elsif SCR.NS == '0' then UNDEFINED; else R[t] = VPIDR;
```

```
MCR{<c>}{<q>} <coproc>, {#}<opc1>, <Rt>, <CRn>, <CRm>{, {#}<opc2>}
```

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b100  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL2) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then
```

```
AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); else UNDEFINED; elsif PSTATE.EL == EL2 then VPIDR = R[t]; elsif PSTATE.EL == EL3 then if !HaveEL(EL2) then return; elsif SCR.NS == '0' then UNDEFINED; else VPIDR = R[t];
```

MRC{&lt;c&gt;}{&lt;q&gt;} &lt;coproc&gt;, {#}&lt;opc1&gt;, &lt;Rt&gt;, &lt;CRn&gt;, &lt;CRm&gt;{, {#}&lt;opc2&gt;}

| coproc   | opc1   | CRn    | CRm    | opc2   |
|----------|--------|--------|--------|--------|
| 0b1111   | 0b000  | 0b0000 | 0b0000 | 0b000  |

```
if !IsFeatureImplemented(FEAT_AA32EL1) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) && HSTR_EL2.T0 == '1' ↪ → then AArch64.AArch32SystemAccessTrap(EL2, 0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) && HSTR.T0 == '1' ↪ → then AArch32.TakeHypTrapException(0x03); elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA64EL2) && !ELUsingAArch32(EL2) then R[t] = VPIDR_EL2<31:0>; elsif EL2Enabled() && IsFeatureImplemented(FEAT_AA32EL2) && ELUsingAArch32(EL2) then R[t] = VPIDR; else R[t] = MIDR; elsif PSTATE.EL == EL2 then R[t] = MIDR; elsif PSTATE.EL == EL3 then R[t] = MIDR;
```