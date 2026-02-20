## D24.2.64 HDBSSBR\_EL2, Hardware Dirty State Tracking Structure Base Register

The HDBSSBR\_EL2 characteristics are:

## Purpose

Control register for HDBSS base address.

## Configuration

This register is present only when FEAT\_HDBSS is implemented and FEAT\_AA64 is implemented. Otherwise, direct accesses to HDBSSBR\_EL2 are UNDEFINED.

## Attributes

HDBSSBR\_EL2 is a 64-bit register.

## Field descriptions

<!-- image -->

## Bits [63:56]

Reserved, RES0.

## BADDR, bits [55:12]

HDBSS base address, bits [55:12].

- Bits [55:12] of the base address are the value of this field.
- Bits [11:0] of the base address are 0.

Bits of this field above the implemented physical address size, indicated in ID\_AA64MMFR0\_EL1.PARange, are RES0.

Based on the value of the SZ field of this register, for encodings of the SZ field greater than 4KB, bits [(SZ+12-1):12] of this field are RES0 such that the base address of the HDBSS is aligned to its size.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Bits [11:4]

Reserved, RES0.

## SZ, bits [3:0]

Size of the HDBSS.

| SZ     | Meaning   |
|--------|-----------|
| 0b0000 | 4KB       |

All other values are reserved.

The reset behavior of this field is:

- On a Warm reset, this field resets to an architecturally UNKNOWN value.

## Accessing HDBSSBR\_EL2

Accesses to this register use the following encodings in the System register encoding space:

MRS &lt;Xt&gt;, HDBSSBR\_EL2

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_HDBSS) && IsFeatureImplemented(FEAT_AA64)) UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then X[t, 64] = NVMem[0x2E0]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HDBSSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HDBSSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else X[t, 64] = HDBSSBR_EL2; elsif PSTATE.EL == EL3 then X[t, 64] = HDBSSBR_EL2;
```

```
then
```

| SZ     | Meaning   |
|--------|-----------|
| 0b0001 | 8KB       |
| 0b0010 | 16KB      |
| 0b0011 | 32KB      |
| 0b0100 | 64KB      |
| 0b0101 | 128KB     |
| 0b0110 | 256KB     |
| 0b0111 | 512KB     |
| 0b1000 | 1MB       |
| 0b1001 | 2MB       |

MSR HDBSSBR\_EL2, &lt;Xt&gt;

| op0   | op1   | CRn    | CRm    | op2   |
|-------|-------|--------|--------|-------|
| 0b11  | 0b100 | 0b0010 | 0b0011 | 0b010 |

```
if !(IsFeatureImplemented(FEAT_HDBSS) && IsFeatureImplemented(FEAT_AA64)) then UNDEFINED; elsif PSTATE.EL == EL0 then UNDEFINED; elsif PSTATE.EL == EL1 then if EffectiveHCR_EL2_NVx() IN {'1x1'} then NVMem[0x2E0] = X[t, 64]; elsif EffectiveHCR_EL2_NVx() IN {'xx1'} then AArch64.SystemAccessTrap(EL2, 0x18); else UNDEFINED; elsif PSTATE.EL == EL2 then if HaveEL(EL3) && EL3SDDUndefPriority() && SCR_EL3.HDBSSEn == '0' then UNDEFINED; elsif HaveEL(EL3) && SCR_EL3.HDBSSEn == '0' then if EL3SDDUndef() then UNDEFINED; else AArch64.SystemAccessTrap(EL3, 0x18); else HDBSSBR_EL2 = X[t, 64]; elsif PSTATE.EL == EL3 then HDBSSBR_EL2 = X[t, 64];
```